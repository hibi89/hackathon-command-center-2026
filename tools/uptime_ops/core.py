"""UPTIME OPS isolated P0/P2 prototype: opt-in, pinned, HEAD-only checks.

Stdlib-only; no background service, discovery, redirects, credentials, or cloud calls.
Synthetic CI must inject both DNS resolution and socket connection.
"""
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
import csv
import http.client
import ipaddress
import json
import os
import re
import socket
import sqlite3
import ssl
import time
from urllib.parse import urlsplit


class GuardError(ValueError):
    """Unsafe or unapproved monitoring input; no network operation permitted."""


TARGET_ID = re.compile(r"[A-Za-z0-9_][A-Za-z0-9_-]{0,63}\Z")
APPROVAL = re.compile(r"[A-Za-z0-9_:/.-]{3,80}\Z")
HOSTNAME = re.compile(r"[A-Za-z0-9.-]{1,253}\Z")
PATH = re.compile(r"/[A-Za-z0-9/_~.%-]*\Z")
DETAIL = re.compile(r"[A-Z0-9_]{1,40}\Z")
STATES = {"UP", "DOWN", "UNKNOWN"}


def checked_address(text, allow_private):
    try:
        address = ipaddress.ip_address(text)
    except (ValueError, TypeError) as exc:
        raise GuardError("invalid pinned IP address") from exc
    if (address.is_loopback or address.is_link_local or address.is_multicast or
            address.is_unspecified or address.is_reserved or
            (address.version == 6 and address.ipv4_mapped is not None)):
        raise GuardError("loopback, link-local, reserved, mapped or multicast IP denied")
    # is_private also includes several non-RFC1918 special-use ranges; do
    # not make those reachable merely by enabling private LAN monitoring.
    approved_lan = (
        address.version == 4 and any(
            address in ipaddress.ip_network(cidr) for cidr in
            ("10.0.0.0/8", "172.16.0.0/12", "192.168.0.0/16"))
        or address.version == 6 and
        address in ipaddress.ip_network("fc00::/7")
    )
    if not address.is_global and not (allow_private and approved_lan):
        raise GuardError("nonpublic IP denied unless explicitly pinned RFC1918/ULA")
    return str(address)


@dataclass(frozen=True)
class Target:
    target_id: str
    url: str
    approval_ref: str
    consent: bool
    allowed_ips: tuple
    allow_private: bool = False
    interval_seconds: int = 60
    timeout_seconds: int = 5

    @classmethod
    def from_dict(cls, data):
        if not isinstance(data, dict):
            raise GuardError("target must be an object")
        keys = {"target_id", "url", "approval_ref", "consent", "allowed_ips",
                "allow_private", "interval_seconds", "timeout_seconds"}
        if set(data) - keys:
            raise GuardError("unknown target configuration fields")
        if (not isinstance(data.get("target_id"), str) or
                not TARGET_ID.fullmatch(data["target_id"]) or
                not isinstance(data.get("approval_ref"), str) or
                not APPROVAL.fullmatch(data["approval_ref"]) or
                data.get("consent") is not True):
            raise GuardError("explicit target identity and scope consent required")
        private = data.get("allow_private", False)
        if type(private) is not bool:
            raise GuardError("allow_private must be boolean")
        interval = data.get("interval_seconds", 60)
        timeout = data.get("timeout_seconds", 5)
        if type(interval) is not int or not 30 <= interval <= 86400:
            raise GuardError("interval must be 30..86400 seconds")
        if type(timeout) is not int or not 1 <= timeout <= 15:
            raise GuardError("timeout must be 1..15 seconds")
        ips = data.get("allowed_ips")
        if not isinstance(ips, list) or not 1 <= len(ips) <= 8:
            raise GuardError("1..8 exact approved IP pins required")
        pins = tuple(checked_address(ip, private) for ip in ips)
        if len(set(pins)) != len(pins):
            raise GuardError("duplicate IP pin")
        obj = cls(target_id=data["target_id"], url=data.get("url"),
                  approval_ref=data["approval_ref"], consent=True,
                  allowed_ips=pins, allow_private=private,
                  interval_seconds=interval, timeout_seconds=timeout)
        obj.parsed()
        return obj

    def parsed(self):
        if (not isinstance(self.url, str) or self.url != self.url.strip() or
                any(ord(ch) < 33 or ord(ch) == 127 for ch in self.url)):
            raise GuardError("invalid URL or raw control characters")
        try:
            parts = urlsplit(self.url)
            port = parts.port
            host = parts.hostname
        except ValueError as exc:
            raise GuardError("invalid URL/port") from exc
        if (parts.scheme not in {"http", "https"} or not host or
                parts.username is not None or parts.password is not None or
                parts.query or parts.fragment or "#" in self.url or
                "?" in self.url or not PATH.fullmatch(parts.path or "/")):
            raise GuardError("only exact credential-free HTTP(S) HEAD URL allowed")
        if port is None:
            port = 443 if parts.scheme == "https" else 80
        if not 1 <= port <= 65535:
            raise GuardError("invalid port")
        try:
            ipaddress.ip_address(host)
        except ValueError:
            if (not HOSTNAME.fullmatch(host) or host.endswith(".") or
                    ".." in host or any(label.startswith("-") or label.endswith("-")
                                     for label in host.split("."))):
                raise GuardError("unsafe hostname")
        return parts, host, port

    def resource(self):
        parts, _, _ = self.parsed()
        return parts.path or "/"


def load_targets(path):
    raw = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(raw, dict) or set(raw) != {"targets"}:
        raise GuardError("config must contain only targets")
    targets = raw["targets"]
    if not isinstance(targets, list) or not 1 <= len(targets) <= 25:
        raise GuardError("1..25 individually authorized targets required")
    parsed = [Target.from_dict(item) for item in targets]
    if len({t.target_id for t in parsed}) != len(parsed):
        raise GuardError("duplicate target ID")
    return parsed


def resolve_pinned(target, resolver=socket.getaddrinfo):
    _, host, port = target.parsed()
    try:
        literal = ipaddress.ip_address(host)
    except ValueError:
        literal = None
    if literal is not None:
        resolved = {checked_address(str(literal), target.allow_private)}
    else:
        answers = resolver(host, port, type=socket.SOCK_STREAM)
        if not answers:
            raise GuardError("DNS returned no addresses")
        try:
            resolved = {checked_address(answer[4][0], target.allow_private)
                        for answer in answers}
        except (IndexError, TypeError, ValueError) as exc:
            raise GuardError("invalid DNS response") from exc
    if not resolved or not resolved.issubset(set(target.allowed_ips)):
        raise GuardError("DNS changed outside approved exact IP pins")
    # Connect to the IP directly; never permit the HTTP library to re-resolve.
    return sorted(resolved)[0]


@dataclass(frozen=True)
class ProbeResult:
    state: str
    detail: str
    status_code: int | None = None
    elapsed_ms: int = 0

    def __post_init__(self):
        if (self.state not in STATES or not DETAIL.fullmatch(self.detail) or
                (self.status_code is not None and
                 (type(self.status_code) is not int or
                  not 100 <= self.status_code <= 599)) or
                type(self.elapsed_ms) is not int or self.elapsed_ms < 0):
            raise GuardError("unsafe probe-result data")


def head_probe(target, *, resolver=socket.getaddrinfo,
               connect=socket.create_connection, tls_factory=ssl.create_default_context,
               clock=time.monotonic):
    """One explicit HEAD, pinned socket, verified TLS, and zero redirect following."""
    start = clock()
    try:
        chosen_ip = resolve_pinned(target, resolver)
    except (GuardError, OSError):
        return ProbeResult("UNKNOWN", "DNS_DENIED")
    parts, host, port = target.parsed()
    conn = http.client.HTTPConnection(host, port, timeout=target.timeout_seconds)
    try:
        raw = connect((chosen_ip, port), timeout=target.timeout_seconds)
        if parts.scheme == "https":
            try:
                conn.sock = tls_factory().wrap_socket(raw, server_hostname=host)
            except BaseException:
                raw.close()  # TLS handshake failure must not leak a raw socket.
                raise
        else:
            conn.sock = raw
        # HTTPConnection uses the original host in Host header and never resolves
        # again since sock was already attached; no cookies or auth headers.
        conn.request("HEAD", target.resource(), headers={"User-Agent": "UPTIME-OPS/preview"})
        response = conn.getresponse()
        status = response.status
        elapsed = max(0, int((clock() - start) * 1000))
        if 200 <= status <= 299:
            return ProbeResult("UP", "HTTP_OK", status, elapsed)
        if 300 <= status <= 399:
            return ProbeResult("UNKNOWN", "REDIRECT_DENIED", status, elapsed)
        if status in {401, 403, 405, 407, 429}:
            return ProbeResult("UNKNOWN", "REVIEW_REQUIRED", status, elapsed)
        if 400 <= status <= 599:
            return ProbeResult("DOWN", "HTTP_ERROR", status, elapsed)
        return ProbeResult("UNKNOWN", "UNEXPECTED_HTTP", status, elapsed)
    except ssl.SSLError:
        return ProbeResult("UNKNOWN", "TLS_VERIFY_ERROR")
    except (TimeoutError, socket.timeout):
        return ProbeResult("DOWN", "CONNECT_TIMEOUT")
    except (OSError, http.client.HTTPException):
        return ProbeResult("DOWN", "CONNECT_ERROR")
    finally:
        conn.close()


class History:
    """Durable local check/event ledger; never persists URLs, credentials or response bodies."""

    def __init__(self, path):
        self.path = Path(path)
        if self.path.is_symlink():
            raise GuardError("refusing SQLite symlink destination")
        self.conn = sqlite3.connect(str(self.path), timeout=5)
        self.conn.execute("PRAGMA busy_timeout=5000")
        self.conn.executescript("""
            CREATE TABLE IF NOT EXISTS checks(
              target_id TEXT NOT NULL, checked_at TEXT NOT NULL,
              state TEXT NOT NULL, detail TEXT NOT NULL,
              status_code INTEGER, elapsed_ms INTEGER NOT NULL,
              PRIMARY KEY(target_id, checked_at)
            );
            CREATE TABLE IF NOT EXISTS current_state(
              target_id TEXT PRIMARY KEY, last_checked_at TEXT NOT NULL,
              last_known TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS events(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              target_id TEXT NOT NULL, occurred_at TEXT NOT NULL,
              kind TEXT NOT NULL, note TEXT NOT NULL,
              UNIQUE(target_id, occurred_at, kind)
            );
        """)
        if os.name != "nt":
            os.chmod(self.path, 0o600)

    def close(self):
        self.conn.close()

    def record(self, target, result, when):
        if not isinstance(target, Target) or not isinstance(result, ProbeResult):
            raise GuardError("typed target and result required")
        if not isinstance(when, datetime) or when.tzinfo is None:
            raise GuardError("timestamp must include timezone")
        timestamp = when.astimezone(timezone.utc).isoformat(timespec="microseconds")
        with self.conn:
            old = self.conn.execute(
                "SELECT state, detail, status_code, elapsed_ms FROM checks "
                "WHERE target_id=? AND checked_at=?",
                (target.target_id, timestamp)).fetchone()
            if old is not None:
                if old == (result.state, result.detail,
                           result.status_code, result.elapsed_ms):
                    return []  # exact replay is idempotent
                raise GuardError("conflicting observation at same timestamp")
            previous = self.conn.execute(
                "SELECT last_checked_at, last_known FROM current_state "
                "WHERE target_id=?", (target.target_id,)).fetchone()
            events = []
            last_known = "UNKNOWN" if previous is None else previous[1]
            if previous is not None:
                prev = datetime.fromisoformat(previous[0])
                if when.astimezone(timezone.utc) <= prev:
                    raise GuardError("clock moved backward; refusing false timeline")
                if (when.astimezone(timezone.utc) - prev).total_seconds() > (
                        target.interval_seconds * 2):
                    events.append(("GAP", "UNOBSERVED_INTERVAL"))
            if result.state == "DOWN" and last_known != "DOWN":
                events.append(("DOWN", "INCIDENT_OPEN"))
            elif result.state == "UP" and last_known == "DOWN":
                events.append(("RECOVERED", "INCIDENT_CLOSED"))
            known = last_known if result.state == "UNKNOWN" else result.state
            self.conn.execute(
                "INSERT INTO checks VALUES(?,?,?,?,?,?)",
                (target.target_id, timestamp, result.state,
                 result.detail, result.status_code, result.elapsed_ms))
            self.conn.execute(
                "INSERT INTO current_state VALUES(?,?,?) "
                "ON CONFLICT(target_id) DO UPDATE SET "
                "last_checked_at=excluded.last_checked_at, last_known=excluded.last_known",
                (target.target_id, timestamp, known))
            for kind, note in events:
                self.conn.execute(
                    "INSERT INTO events(target_id,occurred_at,kind,note) VALUES(?,?,?,?)",
                    (target.target_id, timestamp, kind, note))
            return [kind for kind, _ in events]

    def events(self, target_id):
        return self.conn.execute(
            "SELECT occurred_at, kind, note FROM events WHERE target_id=? ORDER BY id",
            (target_id,)).fetchall()

    def export_csv(self, output_path):
        # x mode prevents accidental overwrites of user originals.
        fd = os.open(output_path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as out:
            writer = csv.writer(out)
            writer.writerow(["target_id", "checked_at", "state", "detail",
                             "status_code", "elapsed_ms"])
            writer.writerows(self.conn.execute(
                "SELECT target_id, checked_at, state, detail, status_code, elapsed_ms "
                "FROM checks ORDER BY checked_at, target_id"))
