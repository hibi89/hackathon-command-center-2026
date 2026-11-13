import base64
import json
from pathlib import Path
import unittest
from urllib.parse import parse_qs, unquote, urlsplit

from sync import (ROOT, REGISTRY, ROSTER, GitHubAPI, Observer, collect_snapshot,
                  decode_contents, hub_path, load_registry, reconcile_hub,
                  safe_ref, validate_registry, determine_dry_run)


def as_content(obj, sha="a" * 40):
    raw = json.dumps(obj).encode("utf-8")
    return {"type": "file", "encoding": "base64", "content": base64.b64encode(raw).decode(),
            "sha": sha}


class HubFake:
    def __init__(self, existing=None, tamper=False):
        self.existing = existing
        self.tamper = tamper
        self.writes = []

    def get(self, path, token, allow_404=False):
        if not token:
            raise AssertionError("missing test token")
        if path != hub_path("data/kmong_hub_auto_observations.json", "kmong-productization"):
            raise AssertionError(path)
        if self.existing is None:
            return None
        return as_content(self.existing, sha="a" * 40)

    def put(self, path, token, data):
        if path != hub_path("data/kmong_hub_auto_observations.json"):
            raise AssertionError(path)
        self.writes.append(data)
        raw = base64.b64decode(data["content"])
        self.existing = json.loads(raw)
        if self.tamper:
            self.existing["tampered"] = True
        return {"commit": {"sha": "f" * 40}}


class SourceFake:
    def __init__(self, roster, pins):
        self.roster, self.pins = roster, pins
        self.missing = set()
        self.pin_mutations = {}
        self.calls = []
        self.refs = {}
        for entry in roster:
            name = entry["repository"]
            self.refs[(name, "main")] = "b" * 40
            for b in entry["branches"]:
                self.refs[(name, b)] = "c" * 40
        for pin in pins.values():
            self.refs[(pin["repository"], pin["ref"])] = "d" * 40

    def get(self, path, token, allow_404=False):
        self.calls.append(path)
        if token != "app-read-token":
            raise AssertionError("must not use central write token for source reads")
        if path == "/installation/repositories?per_page=100":
            return {"total_count":len(self.roster),
                    "repositories":[{"full_name":x["repository"]} for x in self.roster]}
        if path.endswith("/actions/workflows/final-blueprint-gate.yml/runs?branch=main&per_page=1"):
            return {"workflow_runs":[]}
        if "/actions/workflows/final-blueprint-gate.yml/runs?" in path:
            return {"workflow_runs":[]}
        if "/git/ref/heads/" in path:
            front, branch = path.split("/git/ref/heads/", 1)
            name = front.removeprefix("/repos/")
            ref = (name, unquote(branch))
            if ref in self.missing or ref not in self.refs:
                return None if allow_404 else (_ for _ in ()).throw(AssertionError("unexpected missing branch"))
            return {"object":{"sha":self.refs[ref]}}
        if "/contents/" in path:
            front, other = path.split("/contents/", 1)
            repo = front.removeprefix("/repos/")
            raw, query = other.split("?", 1)
            ref = parse_qs(query)["ref"][0]
            pin = self.pins.get(repo.lower())
            if pin is None or pin["path"] != unquote(raw) or pin["ref"] != ref:
                raise AssertionError("unknown pinned content")
            if (repo, ref) in self.missing:
                return None
            return {"type":"file", "sha":self.pin_mutations.get(repo, pin["git_blob_sha"])}
        raise AssertionError("unexpected GET " + path)


class ExecutionModeTest(unittest.TestCase):
    def test_cron_is_not_accidentally_dry_run(self):
        self.assertFalse(determine_dry_run("schedule", ""))

    def test_manual_defaults_to_dry_run(self):
        self.assertTrue(determine_dry_run("workflow_dispatch", ""))
        self.assertTrue(determine_dry_run("workflow_dispatch", "true"))

    def test_manually_selected_write_is_respected(self):
        self.assertFalse(determine_dry_run("workflow_dispatch", "false"))

    def test_unexpected_event_cannot_write(self):
        self.assertTrue(determine_dry_run("pull_request", "false"))
        self.assertTrue(determine_dry_run("", "false"))


class RosterTest(unittest.TestCase):
    def test_roster_has_exact_35_repositories_and_35_extra_branches(self):
        repos, pins = load_registry()
        self.assertEqual(len(repos), 35)
        self.assertEqual(len(pins), 31)
        self.assertEqual(sum(len(x["branches"]) for x in repos), 35)

    def test_all_inventory_repositories_are_unique_and_covered(self):
        roster = json.loads(ROSTER.read_text())
        registry = json.loads(REGISTRY.read_text())
        repos, pins = validate_registry(roster, registry)
        self.assertEqual({x["repository"].lower() for x in repos},
                         {x.lower() for x in registry["not_pinned_main"]} | set(pins))

    def test_missing_one_repo_fails_before_network(self):
        roster = json.loads(ROSTER.read_text())
        registry = json.loads(REGISTRY.read_text())
        roster["repositories"].pop()
        with self.assertRaises(ValueError):
            validate_registry(roster, registry)

    def test_invalid_ref_rejected(self):
        for bad in ("", "../main", "a//b", "a/../b", "/main", "main?", "a b", "a/"):
            self.assertFalse(safe_ref(bad), bad)
        for good in ("main", "feature/axflow-mvp", "lead/paypal", "integration/develop"):
            self.assertTrue(safe_ref(good), good)

    def test_pin_registry_change_must_match_roster(self):
        roster = json.loads(ROSTER.read_text())
        registry = json.loads(REGISTRY.read_text())
        registry["pins"][0]["repository"] = "hibi89/UNKNOWN"
        with self.assertRaises(ValueError):
            validate_registry(roster, registry)


class CollectorTest(unittest.TestCase):
    def setUp(self):
        self.roster, self.pins = load_registry()
        self.api = SourceFake(self.roster, self.pins)
        self.observer = Observer(self.api, "app-read-token")
        self.index = {"records":[{"record_id":f"PROD-{i:02d}",
                                  "repository":self.roster[0]["repository"],
                                  "tracked_branch":"main"} for i in range(29)]}

    def test_normal_snapshot_is_deterministic_and_never_scores(self):
        first = collect_snapshot(self.observer, self.roster, self.pins, self.index)
        self.assertEqual(first, collect_snapshot(self.observer, self.roster, self.pins, self.index))
        self.assertEqual(first["summary"]["repository_count"], 35)
        self.assertEqual(first["summary"]["tracked_branch_count"], 70)
        self.assertEqual(first["summary"]["product_links"], 29)
        self.assertEqual(first["summary"]["canonical_matched"], 31)
        self.assertEqual(first["summary"]["canonical_not_configured"], 4)
        self.assertNotIn("official_final_completion", json.dumps(first))

    def test_app_installation_missing_repo_blocks_whole_sync(self):
        self.api.roster = self.roster[:-1]
        with self.assertRaisesRegex(RuntimeError, "35 approved"):
            collect_snapshot(self.observer, self.roster, self.pins, self.index)

    def test_enforced_drift_reports_blocker_but_does_not_score(self):
        name = next(p["repository"] for p in self.pins.values() if p["mode"] == "enforce")
        self.api.pin_mutations[name] = "f" * 40
        result = collect_snapshot(self.observer, self.roster, self.pins, self.index)
        self.assertIn(name, result["blocking_repositories"])
        self.assertEqual(result["summary"]["blocking_fingerprint_issues"], 1)

    def test_observe_mode_drift_is_not_blocking(self):
        name = next(p["repository"] for p in self.pins.values() if p["mode"] == "observe")
        self.api.pin_mutations[name] = "f" * 40
        result = collect_snapshot(self.observer, self.roster, self.pins, self.index)
        self.assertEqual(result["summary"]["blocking_fingerprint_issues"], 0)
        self.assertEqual(next(x for x in result["repositories"] if x["repository"] == name)
                         ["canonical"]["status"], "DRIFT_REVIEW_REQUIRED")

    def test_missing_nonmain_branch_is_not_mistaken_for_current(self):
        entry = next(x for x in self.roster if x["branches"])
        branch = entry["branches"][0]
        self.api.missing.add((entry["repository"], branch))
        result = collect_snapshot(self.observer, self.roster, self.pins, self.index)
        b = next(x for x in result["repositories"] if x["repository"] == entry["repository"])
        self.assertEqual(b["work_branches"][0]["status"], "MISSING")

    def test_duplicate_product_ids_rejected(self):
        self.index["records"][1]["record_id"] = self.index["records"][0]["record_id"]
        with self.assertRaisesRegex(ValueError, "duplicate product"):
            collect_snapshot(self.observer, self.roster, self.pins, self.index)


class WriteTest(unittest.TestCase):
    def setUp(self):
        self.snapshot = {"schema_version":1, "generated_by":"kmong-hub-sync",
                         "no_official_score_authorization":True,
                         "repositories":[{"repository":"hibi89/demo", "main": {"head_sha":"b"*40}}]}

    def test_dry_run_never_writes_or_marks_success(self):
        api = HubFake()
        result = reconcile_hub(api, "central-write-token", self.snapshot, True)
        self.assertEqual(result["result"], "DRY_RUN")
        self.assertEqual(api.writes, [])

    def test_first_write_confirmed_by_readback(self):
        api = HubFake()
        result = reconcile_hub(api, "central-write-token", self.snapshot, False)
        self.assertEqual(result["result"], "UPDATED")
        self.assertEqual(result["commit"], "f" * 40)
        self.assertEqual(len(api.writes), 1)
        self.assertNotIn("sha", api.writes[0])
        self.assertEqual(api.writes[0]["branch"], "kmong-productization")

    def test_repeated_equal_snapshot_makes_no_commit(self):
        api = HubFake(existing=self.snapshot)
        result = reconcile_hub(api, "central-write-token", self.snapshot, False)
        self.assertEqual(result["result"], "NO_CHANGE")
        self.assertFalse(api.writes)

    def test_changed_snapshot_uses_existing_file_sha(self):
        api = HubFake(existing={"schema_version":1,"generated_by":"kmong-hub-sync"})
        result = reconcile_hub(api, "central-write-token", self.snapshot, False)
        self.assertEqual(result["result"], "UPDATED")
        self.assertEqual(api.writes[0]["sha"], "a" * 40)

    def test_foreign_or_user_owned_file_not_overwritten(self):
        api = HubFake(existing={"official_final_completion":"UNASSESSED"})
        with self.assertRaisesRegex(RuntimeError, "managed evidence snapshot"):
            reconcile_hub(api, "central-write-token", self.snapshot, False)
        self.assertFalse(api.writes)

    def test_readback_mismatch_does_not_claim_success(self):
        api = HubFake(tamper=True)
        with self.assertRaisesRegex(RuntimeError, "did not match"):
            reconcile_hub(api, "central-write-token", self.snapshot, False)

    def test_index_reader_rejects_nonfile(self):
        with self.assertRaises(ValueError):
            decode_contents({"type":"dir","encoding":"base64","content":""})


if __name__ == "__main__":
    unittest.main()
