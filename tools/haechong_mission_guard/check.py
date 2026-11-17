#!/usr/bin/env python3
"""Haechong mission continuity check; validates top-of-file authority before resume."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
MARKER = "> **[HAECHONG_PRIMARY_MISSION_LOCK_V1]** PRIMARY_MISSION=GITHUB_APP_CENTRAL_AUTOMATION_90_TO_100; `ㄱ`/`ㄱㄱ` resumes GitHub App → signed HMAC webhook → Vercel bridge → central Actions → ledger; side-product development requires an explicit NEW owner instruction. `HANDOFF` recency cannot override this lock."
NEXT = "> **[HAECHONG_NEXT_GATE]** One real signed GitHub App Delivery -> existing Production main@5542fb5 -> bot Actions #43859747199 -> collector NO_CHANGE -> ledger readback is E2E PASS (2026-11-16; Delivery response Work-attested, GitHub/Vercel execution independently cross-checked). Whole-design weighted verification UNASSESSED; historical provisional engineering score 90/100 is NOT official completion. RELEASE HOLD; retain GitHub App mission, no side-product switch, main merge or Production change without owner GO."
FILES = ("HANDOFF.md", "STATUS.md", "AGENTS.md")
POLICY_PATH = "data/haechong_active_mission_20261115.json"

class MissionLockError(ValueError):
    pass

def require(condition, why):
    if not condition:
        raise MissionLockError(why)

def check(contents):
    """Input mapping is immutable to allow mutation tests; no network/no writes."""
    for path in FILES:
        source = contents.get(path)
        require(isinstance(source, str), "missing primary document: " + path)
        first = source.splitlines()[:2]
        require(first == [MARKER, NEXT], "active mission lost top priority in " + path)
    try:
        p = json.loads(contents[POLICY_PATH])
    except (KeyError, json.JSONDecodeError, TypeError) as exc:
        raise MissionLockError("missing or invalid mission policy") from exc
    require(type(p) is dict, "policy must be object")
    frozen = {
        "schema_version": 1,
        "policy_id": "HAECHONG_PRIMARY_MISSION_LOCK_V1",
        "role": "HAECHONG_CENTRAL",
        "primary_mission": "GITHUB_APP_CENTRAL_AUTOMATION_90_TO_100",
        "resume_commands": ["ㄱ", "ㄱㄱ"],
        "resume_scope": "GITHUB_APP_ONLY",
        "main_goal": "LIVE_SIGNED_HMAC_DELIVERY_AND_DEPLOYED_SHA_EVIDENCE",
        "current_provisional_score": 90,
        "signed_live_hmac_e2e_verified": True,
        "work_status": "LIVE_SIGNED_E2E_PASS_OFFICIAL_ACCEPTANCE_UNASSESSED",
        "fallback_scope": "CENTRAL_APP_ONLY",
        "side_product_development_allowed": False,
        "project_switch_requires_explicit_owner_approval": True,
        "project_switch_owner_approval_recorded": False,
        "source_webhook_branch": "feature/kmong-webhook-bounded-ingress-20261114",
        "runtime_branch": "main",
        "operating_branch": "kmong-productization",
        "protected_customer_status": "NO_COMMERCIAL_POSTING_OR_RELEASE",
        "e2e_evidence": {"delivery_id":"083bddec-e190-11f1-978d-156991bf2ef1","delivery_http_status":202,"delivery_status":"queued","vercel_request_id":"r2g5s-1794829197598-6a1fe727f93c","workflow_run_id":43859747199,"workflow_dispatch_actor":"kmong-hub-dispatcher[bot]","workflow_run_conclusion":"success","collector_outcome":"NO_CHANGE","production_main_sha":"5542fb5bf13cba5f30a374afc423b875790ff58c","ledger_blob_sha":"2dd7b2ed50d205b55a2050aad42df218481e7ceb"},
    }
    for key, expected in frozen.items():
        actual = p.get(key)
        require(type(actual) is type(expected) and actual == expected,
                "mission lock drift: " + key)
    require(isinstance(p.get("notes"), str) and
            "HANDOFF" in p["notes"] and
            "product" in p["notes"], "mission/side-work precedence missing")
    return "HAECHONG_MISSION_LOCK: PASS GitHub App primary / traced live E2E receipt / official whole-design UNASSESSED"

def main():
    try:
        values = {p: (ROOT / p).read_text(encoding="utf-8")
                  for p in (*FILES, POLICY_PATH)}
        print(check(values))
    except (MissionLockError, OSError) as exc:
        print("HAECHONG_MISSION_LOCK: FAIL", exc, file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
