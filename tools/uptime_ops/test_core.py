"""Synthetic only: DNS and socket interactions are injected, never real network."""
from datetime import datetime, timedelta, timezone
from pathlib import Path
import copy
import io
import tempfile
import unittest
from unittest.mock import patch

from tools.uptime_ops.core import (
    GuardError, History, ProbeResult, Target, head_probe, load_targets, resolve_pinned,
)
from tools.uptime_ops.cli import main as cli_main


BASE = {
    "target_id": "owned_web",
    "url": "https://example.test/health",
    "approval_ref": "owner:sample-01",
    "consent": True,
    "allowed_ips": ["93.184.215.14"],
    "allow_private": False,
    "interval_seconds": 60,
    "timeout_seconds": 3,
}


def build(**kw):
    return Target.from_dict({**BASE, **kw})


def dns(*ips):
    return lambda host, port, **kwargs: [
        (2, 1, 6, "", (ip, port)) for ip in ips
    ]


class FakeSocket:
    def __init__(self, status):
        self.status = status
        self.sent = b""
        self.closed = False

    def sendall(self, payload):
        self.sent += payload

    def makefile(self, *args, **kwargs):
        return io.BytesIO(
            ("HTTP/1.1 %d TEST\r\nContent-Length: 0\r\nLocation: http://evil.test/\r\n"
             "\r\n" % self.status).encode("ascii"))

    def close(self):
        self.closed = True


class TargetGuardTests(unittest.TestCase):
    def fail(self, **changes):
        with self.assertRaises(GuardError):
            build(**changes)

    def test_approved_exact_https_config(self):
        self.assertEqual(build().resource(), "/health")

    def test_explicit_scope_consent_required(self):
        self.fail(consent=False)
        self.fail(approval_ref="")

    def test_never_embed_credentials(self):
        self.fail(url="https://user:pass@example.test/health")

    def test_no_query_tokens_or_fragments(self):
        self.fail(url="https://example.test/health?secret=xyz")
        self.fail(url="https://example.test/health#fragment")

    def test_reject_unsupported_url_and_port(self):
        self.fail(url="file:///etc/passwd")
        self.fail(url="https://example.test:99999/health")

    def test_no_loopback_or_metadata(self):
        self.fail(allowed_ips=["127.0.0.1"], allow_private=True)
        self.fail(allowed_ips=["169.254.169.254"], allow_private=True)
        self.fail(allowed_ips=["::1"], allow_private=True)

    def test_private_exact_pin_requires_explicit_consent(self):
        self.fail(allowed_ips=["192.168.1.50"])
        t = build(allowed_ips=["192.168.1.50"], allow_private=True)
        self.assertEqual(t.allowed_ips, ("192.168.1.50",))

    def test_never_accept_empty_pins_or_duplicate_targets(self):
        self.fail(allowed_ips=[])
        with tempfile.TemporaryDirectory() as td:
            conf = Path(td) / "targets.json"
            import json
            conf.write_text(json.dumps({"targets": [BASE, BASE]}))
            with self.assertRaises(GuardError):
                load_targets(conf)

    def test_no_period_under_30_seconds(self):
        self.fail(interval_seconds=1)

    def test_dns_rebind_to_unpinned_ip_denied(self):
        with self.assertRaisesRegex(GuardError, "outside approved"):
            resolve_pinned(build(), dns("93.184.215.14", "8.8.8.8"))

    def test_dns_to_private_ip_denied_for_public_target(self):
        with self.assertRaises(GuardError):
            resolve_pinned(build(), dns("10.0.0.10"))

    def test_pinned_dns_yields_exact_socket_address(self):
        self.assertEqual(resolve_pinned(build(), dns("93.184.215.14")),
                         "93.184.215.14")


class ProbeTests(unittest.TestCase):
    def run_fake(self, status):
        sock = FakeSocket(status)
        chosen = []
        def connect(address, timeout):
            chosen.append((address, timeout))
            return sock
        class TLS:
            def wrap_socket(self, raw, server_hostname):
                self.host = server_hostname
                return raw
        result = head_probe(build(), resolver=dns("93.184.215.14"),
                            connect=connect, tls_factory=TLS,
                            clock=lambda: 100.0)
        return result, sock, chosen

    def test_200_head_only_pinned_ip_correct_host(self):
        result, sock, chosen = self.run_fake(200)
        self.assertEqual(result.state, "UP")
        self.assertEqual(chosen, [(("93.184.215.14", 443), 3)])
        self.assertTrue(sock.sent.startswith(b"HEAD /health HTTP/1.1"))
        self.assertIn(b"Host: example.test", sock.sent)
        self.assertNotIn(b"Authorization:", sock.sent)

    def test_503_is_down(self):
        self.assertEqual(self.run_fake(503)[0].state, "DOWN")

    def test_redirect_is_unknown_and_never_followed(self):
        result, _, chosen = self.run_fake(302)
        self.assertEqual(result.detail, "REDIRECT_DENIED")
        self.assertEqual(len(chosen), 1)

    def test_authentication_required_not_marked_outage(self):
        self.assertEqual(self.run_fake(401)[0].state, "UNKNOWN")

    def test_dns_denial_opens_no_socket(self):
        with patch("socket.create_connection", side_effect=AssertionError("network")):
            result = head_probe(build(), resolver=dns("169.254.169.254"))
        self.assertEqual(result.detail, "DNS_DENIED")


class PersistenceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.target = build()
        self.db = History(Path(self.temp.name) / "events.sqlite")
        self.at = datetime(2026, 11, 15, 5, 0, tzinfo=timezone.utc)

    def tearDown(self):
        self.db.close()
        self.temp.cleanup()

    def step(self, seconds, state, detail="SYNTHETIC", **kw):
        return self.db.record(self.target, ProbeResult(state, detail, **kw),
                              self.at + timedelta(seconds=seconds))

    def test_down_alert_deduplicated_and_recovery(self):
        self.assertEqual(self.step(0, "UP"), [])
        self.assertEqual(self.step(60, "DOWN"), ["DOWN"])
        self.assertEqual(self.step(120, "DOWN"), [])
        self.assertEqual(self.step(180, "UP"), ["RECOVERED"])
        self.assertEqual([e[1] for e in self.db.events(self.target.target_id)],
                         ["DOWN", "RECOVERED"])

    def test_gap_marks_unobserved_not_full_uptime(self):
        self.step(0, "UP")
        self.assertEqual(self.step(600, "UP"), ["GAP"])
        self.assertEqual(self.step(660, "UP"), [])

    def test_gap_and_down_can_occurr_together(self):
        self.step(0, "UP")
        self.assertEqual(self.step(601, "DOWN"), ["GAP", "DOWN"])

    def test_unknown_does_not_close_incident(self):
        self.step(0, "DOWN")
        self.assertEqual(self.step(60, "UNKNOWN"), [])
        self.assertEqual(self.step(120, "UP"), ["RECOVERED"])

    def test_same_timestamp_retry_is_idempotent(self):
        self.assertEqual(self.step(0, "DOWN"), ["DOWN"])
        self.assertEqual(self.step(0, "DOWN"), [])
        self.assertEqual(len(self.db.events(self.target.target_id)), 1)

    def test_conflicting_same_timestamp_rejected(self):
        self.step(0, "UP")
        with self.assertRaises(GuardError):
            self.step(0, "DOWN")

    def test_rollback_clock_rejected(self):
        self.step(60, "UP")
        with self.assertRaisesRegex(GuardError, "clock moved backward"):
            self.step(0, "DOWN")

    def test_restart_uses_persisted_incident(self):
        self.step(0, "DOWN")
        self.db.close()
        self.db = History(Path(self.temp.name) / "events.sqlite")
        self.assertEqual(self.step(60, "DOWN"), [])
        self.assertEqual(self.step(120, "UP"), ["RECOVERED"])

    def test_csv_new_file_only_does_not_overwrite(self):
        self.step(0, "UP")
        output = Path(self.temp.name) / "export.csv"
        self.db.export_csv(output)
        self.assertIn("owned_web", output.read_text())
        self.assertNotIn("owner:sample", output.read_text())
        with self.assertRaises(FileExistsError):
            self.db.export_csv(output)

    def test_naive_datetime_rejected(self):
        with self.assertRaises(GuardError):
            self.db.record(self.target, ProbeResult("UP", "SYNTHETIC"),
                           datetime(2026, 11, 15))


class CliTests(unittest.TestCase):
    def test_validation_is_offline_by_default(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "targets.json"
            import json
            path.write_text(json.dumps({"targets": [BASE]}))
            with patch("socket.create_connection",
                       side_effect=AssertionError("network")):
                self.assertEqual(cli_main(["--config", str(path)]), 0)

    def test_live_without_explicit_target_and_db_refused(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "targets.json"
            import json
            path.write_text(json.dumps({"targets": [BASE]}))
            self.assertEqual(cli_main(["--config", str(path), "--live"]), 2)


if __name__ == "__main__":
    unittest.main()
