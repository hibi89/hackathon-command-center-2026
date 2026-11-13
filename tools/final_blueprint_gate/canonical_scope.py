"""Verify audited main-branch blueprint identity without exporting private file content."""
import hashlib
import json
from pathlib import Path
import re

REQUIRED_REPOS = frozenset({"hibi89/hae"})
SHA40 = re.compile(r"^[0-9a-f]{40}$")
MAX_BYTES = 2 * 1024 * 1024


def safe_file(root, rel):
    if not isinstance(rel, str) or not rel or rel.startswith("/") or "\\" in rel or ".." in Path(rel).parts:
        return None
    root = Path(root).resolve()
    candidate = root / rel
    if not candidate.is_file() or not candidate.resolve().is_relative_to(root):
        return None
    return candidate


def inspect_canonical(repo, canonical_root=None, pins_path=None):
    """Return (non-secret status, errors); never certify a product score."""
    name = (repo or "").lower()
    empty = {"status": "NOT_CONFIGURED"}
    if pins_path is None:
        pins_path = Path(__file__).with_name("canonical_pins.json")
    try:
        registry = json.loads(Path(pins_path).read_text(encoding="utf-8"))
        if not isinstance(registry, dict) or type(registry.get("schema_version")) is not int or registry["schema_version"] != 1:
            raise ValueError("bad schema")
        pins = registry.get("pins")
        if not isinstance(pins, list) or not pins:
            raise ValueError("pin list absent")
        matches = [p for p in pins if isinstance(p, dict) and isinstance(p.get("repository"), str)
                   and p["repository"].lower() == name]
    except (OSError, ValueError, TypeError) as exc:
        if name in REQUIRED_REPOS:
            return {"status": "INVALID_PIN_REGISTRY"}, [f"canonical registry invalid: {exc}"]
        return empty, []
    if len(matches) != 1:
        if name in REQUIRED_REPOS or matches:
            return {"status": "PIN_MISSING_OR_DUPLICATE"}, ["canonical repo pin missing or duplicated"]
        return empty, []
    pin = matches[0]
    result = {"status": "PENDING", "repository": name, "ref": pin.get("ref"),
              "path": pin.get("path"), "expected_git_blob_sha": pin.get("git_blob_sha"),
              "scope": "file identity only; owner acceptance not certified"}
    if pin.get("ref") != "main" or not isinstance(pin.get("git_blob_sha"), str) or not SHA40.fullmatch(pin["git_blob_sha"]):
        return {**result, "status": "INVALID_PIN"}, ["invalid canonical pin ref or fingerprint"]
    if canonical_root is None:
        return {**result, "status": "CHECKOUT_MISSING"}, ["same-repository main checkout required"]
    path = safe_file(canonical_root, pin.get("path"))
    if path is None:
        return {**result, "status": "FILE_MISSING_OR_UNSAFE"}, ["canonical file missing or outside main checkout"]
    try:
        if path.stat().st_size > MAX_BYTES:
            return {**result, "status": "OVERSIZED"}, ["canonical file exceeds bounded limit"]
        raw = path.read_bytes()
    except OSError:
        return {**result, "status": "UNREADABLE"}, ["canonical file unreadable"]
    digest = hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw).hexdigest()
    if digest != pin["git_blob_sha"]:
        return {**result, "status": "DRIFT_DETECTED", "observed_git_blob_sha": digest}, [
            "canonical file changed versus audited fingerprint; independent review required"]
    return {**result, "status": "MATCHED"}, []
