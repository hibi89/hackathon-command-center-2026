#!/usr/bin/env python3
"""Read-only, fail-closed final-blueprint evidence gate (stdlib only).

Passing format does not certify a product. Missing manifest means UNASSESSED.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import sys
from urllib.parse import urlparse

VERSION = 1
MANIFEST = "docs/final_blueprint_evidence.json"
SHA = re.compile(r"^[0-9a-f]{40}$")
STATES = {"VERIFIED", "PARTIAL", "UNVERIFIED", "BLOCKED"}

def valid_proof(proof, repo):
    if not isinstance(proof, dict):
        return False
    sha, test, url = proof.get("source_sha"), proof.get("test_id"), proof.get("ci_run_url")
    if not isinstance(sha, str) or not SHA.fullmatch(sha):
        return False
    if not isinstance(test, str) or not test.strip() or not isinstance(url, str):
        return False
    parsed = urlparse(url)
    if parsed.scheme != "https" or parsed.netloc != "github.com" or parsed.query or parsed.fragment:
        return False
    m = re.fullmatch(r"/([^/]+/[^/]+)/actions/runs/[0-9]+/?", parsed.path)
    return bool(m and (not repo or m.group(1).lower() == repo.lower()))

def audit(root, repo):
    out = {
        "schema_version": VERSION, "repo": repo or "unknown",
        "manifest": MANIFEST, "official_final_completion": "UNASSESSED",
        "gate": "UNASSESSED", "errors": [],
        "notes": ["Structural evidence check only; not independent feature acceptance."]
    }
    p = root / MANIFEST
    if not p.is_file():
        out["notes"].append("No approved evidence manifest; no official score.")
        return out, True
    errors = out["errors"]
    try:
        obj = json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        errors.append(f"manifest invalid: {exc}")
        return out, False
    if not isinstance(obj, dict):
        errors.append("manifest must be a JSON object")
        return out, False
    if obj.get("schema_version") != VERSION:
        errors.append("schema_version must be 1")
    if not isinstance(obj.get("product"), str) or not obj["product"].strip():
        errors.append("product must be named")

    bp = obj.get("blueprint")
    if not isinstance(bp, dict):
        errors.append("blueprint must be an object")
        bp = {}
    rel = bp.get("path")
    approval = bp.get("owner_approval_reference")
    if not isinstance(approval, str) or not approval.strip():
        errors.append("owner approval reference required; agents cannot approve scope")
    if not isinstance(rel, str) or not rel or rel.startswith("/") or ".." in Path(rel).parts:
        errors.append("blueprint path must be safe and repository-relative")
    else:
        file = root / rel
        if not file.is_file() or not file.resolve().is_relative_to(root.resolve()):
            errors.append("blueprint not found inside repository")
        else:
            expected = bp.get("sha256")
            if not isinstance(expected, str) or hashlib.sha256(file.read_bytes()).hexdigest() != expected.lower():
                errors.append("blueprint SHA256 mismatch (scope drift)")

    items = obj.get("requirements")
    if not isinstance(items, list) or not items:
        errors.append("nonempty requirements array required")
        items = []
    ids, total = set(), 0
    for i, item in enumerate(items):
        tag = f"requirements[{i}]"
        if not isinstance(item, dict):
            errors.append(f"{tag} must be an object")
            continue
        rid = item.get("id")
        if not isinstance(rid, str) or not re.fullmatch(r"[A-Za-z0-9._-]{1,80}", rid):
            errors.append(f"{tag}.id invalid")
        elif rid in ids:
            errors.append(f"{tag}.id duplicated")
        else:
            ids.add(rid)
        weight = item.get("weight")
        if isinstance(weight, bool) or not isinstance(weight, int) or weight < 1 or weight > 100:
            errors.append(f"{tag}.weight must be integer 1..100")
        else:
            total += weight
        state = item.get("status")
        if state not in STATES:
            errors.append(f"{tag}.status invalid")
            continue
        proof = item.get("evidence", [])
        if state == "VERIFIED" and (not isinstance(proof, list) or not proof or not all(valid_proof(x, repo) for x in proof)):
            errors.append(f"{tag}.VERIFIED requires exact-SHA test ID and same-repo CI run URL")
        elif proof and not isinstance(proof, list):
            errors.append(f"{tag}.evidence must be an array")
    if total != 100:
        errors.append(f"rubric must represent entire approved blueprint and sum to 100, got {total}")
    if obj.get("official_final_completion", "UNASSESSED") != "UNASSESSED":
        errors.append("numeric official score forbidden before independent acceptance")
    out["notes"].append("Test URL existence, PASS conclusion, true coverage and approval authenticity NOT checked.")
    out["gate"] = "INVALID_CLAIM" if errors else "EVIDENCE_FORMAT_OK"
    return out, not errors

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path, default=Path("blueprint-gate-result.json"))
    args = parser.parse_args()
    data, ok = audit(args.repo.resolve(), os.getenv("GITHUB_REPOSITORY", ""))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Blueprint gate: {data['gate']}; official=UNASSESSED")
    for note in data["notes"]:
        print("NOTE:", note)
    for err in data["errors"]:
        print("ERROR:", err, file=sys.stderr)
    if os.getenv("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as f:
            f.write("### Final-blueprint gate: " + data["gate"] + "\n\nOfficial: **UNASSESSED** (not 0%).\n")
    return 0 if ok else 1

if __name__ == "__main__":
    raise SystemExit(main())
