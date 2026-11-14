"""Dual progress observation: historical worker reports vs pinned, CI-checked rubric.

This module NEVER modifies the official completion, approval, release or listing status.
A successful CI run alone is never a percentage. Only explicitly allowlisted immutable
scorecard blobs with a same-SHA completed successful baseline run may be replayed.
"""
import base64
import json
import re
from pathlib import Path
from urllib.parse import quote

BASELINE_PATH = Path(__file__).with_name("worker_progress_baseline.json")
SHA40 = re.compile(r"^[0-9a-f]{40}$")
APPROVED = {
    "ACTIVE-05": {
        "repository": "hibi89/data2web_studio",
        "branch": "feature/final-blueprint-p85-evidence-20261113",
        "path": "data/final_blueprint_scorecard_v1.json",
        "blob": "79c08ce8fe9b9c9b34a82373e5e04d1785e409a2",
        "contract": "DATA2WEB_OWNER_APPROVED_100_POINT_SCORECARD_V1",
        "run_id": 43509224663,
        "source_sha": "23a2d1293755294a58a20b98dc34e229a1e54f82",
    },
}


def worker_baseline(path=BASELINE_PATH):
    obj = json.loads(Path(path).read_text(encoding="utf-8"))
    if obj.get("schema_version") != 1 or obj.get("kind") != "HISTORICAL_INTERNAL_WORKER_REPORTS":
        raise ValueError("untrusted historical worker baseline")
    entries = obj.get("reported")
    if not isinstance(entries, dict) or len(entries) != 16:
        raise ValueError("unexpected worker baseline count")
    for key, val in entries.items():
        if not re.fullmatch(r"ACTIVE-\d{2}", key) or type(val) is not int or not (0 <= val <= 100):
            raise ValueError("invalid worker historical percentage")
    return obj


def replay_pinned_scorecard(card, run, pin):
    """Return a bounded candidate only after strict immutable artifact and CI checks.

    It replays an already owner-approved aggregate; it is NOT independent assessment of
    each requirement, customer acceptance, or permission to change the official score.
    """
    if not isinstance(card, dict) or not isinstance(run, dict):
        raise ValueError("scorecard/run must be objects")
    if (card.get("contract") != pin["contract"] or card.get("denominator") != 100
            or card.get("weights_status") != "OWNER_DELEGATED_APPROVED"
            or card.get("owner_approval_scope") != "SCORING_SCALE_AND_FIXED_R01_R33_WEIGHTS_ONLY_NOT_RELEASE"
            or card.get("original_blueprint_scope") != "R01-R33_ALL_INCLUDED_NO_OMISSIONS"
            or card.get("final_completion_method") != "SUM_ONLY_VERIFIED_FULL_REQUIREMENT_WEIGHTS_NO_PARTIAL_WITHOUT_PREAPPROVED_RULE"
            or card.get("release_status") != "RELEASE_HOLD_SALE_NO_GO"):
        raise ValueError("scorecard contract, scope or release invariant mismatch")
    base = card.get("evidence_baseline", {})
    if (not isinstance(base, dict) or base.get("code_sha") != pin["source_sha"]
            or base.get("github_actions_run") != pin["run_id"]):
        raise ValueError("untrusted scorecard evidence baseline")
    if (run.get("id") != pin["run_id"] or run.get("head_sha") != pin["source_sha"]
            or run.get("head_branch") != pin["branch"] or run.get("status") != "completed"
            or run.get("conclusion") != "success"):
        raise ValueError("GitHub Actions run did not prove exact baseline SHA success")
    items = card.get("items")
    if not isinstance(items, list) or len(items) != 33 or card.get("item_count") != 33:
        raise ValueError("33 original requirements required")
    by_id = {}
    weight_sum = score = 0
    for item in items:
        if not isinstance(item, dict):
            raise ValueError("invalid scorecard item")
        rid, weight, state = item.get("id"), item.get("weight"), item.get("state")
        if not isinstance(rid, str) or not re.fullmatch(r"R(?:0[1-9]|[12][0-9]|3[0-3])", rid) or rid in by_id:
            raise ValueError("invalid, duplicated or missing requirement ID")
        if type(weight) is not int or weight <= 0 or weight > 100:
            raise ValueError("invalid requirement weight")
        if state not in {"VERIFIED", "PENDING"}:
            raise ValueError("unapproved partial or unknown scoring state")
        if state == "VERIFIED":
            if item.get("source_code_sha") != pin["source_sha"]:
                raise ValueError("verified item is not tied to approved CI source")
            score += weight
        elif item.get("source_code_sha") is not None:
            raise ValueError("pending item incorrectly claims source acceptance")
        by_id[rid] = True
        weight_sum += weight
    if weight_sum != 100 or len(by_id) != 33:
        raise ValueError("entire approved 100-point scope is not covered")
    return {
        "status": "PINNED_APPROVED_RUBRIC_REPLAY",
        "percent": score,
        "denominator": 100,
        "provenance": "approved fixed scorecard blob + completed successful exact-SHA baseline Actions run",
        "source_run_id": pin["run_id"],
        "source_sha": pin["source_sha"],
        "scorecard_blob_sha": pin["blob"],
        "limitations": "Historical approved item classifications; no fresh item-by-item CI, real-customer, rights or retail acceptance",
        "release_authorized": False,
    }


def attach_dual_progress(snapshot, observer, report=None):
    """Enrich only the dedicated observation snapshot, never authoritative index."""
    if not isinstance(snapshot, dict) or snapshot.get("no_official_score_authorization") is not True:
        raise ValueError("untrusted observation snapshot")
    rows = snapshot.get("products")
    if not isinstance(rows, list) or len(rows) != 29:
        raise ValueError("expected 29 product observation rows")
    baseline = worker_baseline() if report is None else report
    history = baseline["reported"]
    if len({row["record_id"] for row in rows}) != 29:
        raise ValueError("duplicate observation products")
    scored = 0
    for row in rows:
        rid = row["record_id"]
        pct = history.get(rid)
        row["worker_report"] = {
            "percent": pct,
            "status": "HISTORICAL_INTERNAL_MILESTONE" if pct is not None else "NOT_RECORDED_IN_BASELINE",
            "as_of_kst": baseline["as_of_kst"],
            "source": baseline["source"],
            "not_official_final_completion": True,
        }
        candidate = {"status": "UNASSESSED", "percent": None,
                     "reason": "No approved pinned 100-point scorecard + exact-SHA CI evidence"}
        pin = APPROVED.get(rid)
        if pin and row.get("status") == "PRESENT" and row.get("repository") == pin["repository"] and row.get("tracked_branch") == pin["branch"]:
            try:
                path = f"/repos/{pin['repository']}/contents/{quote(pin['path'], safe='/')}?ref={quote(pin['branch'], safe='')}"
                obj = observer.api_get(path, allow_404=True)
                if not isinstance(obj, dict) or obj.get("sha") != pin["blob"] or obj.get("type") != "file" or obj.get("encoding") != "base64":
                    raise ValueError("approved scorecard blob unavailable or changed")
                raw = base64.b64decode(obj["content"], validate=False).decode("utf-8")
                card = json.loads(raw)
                run = observer.api_get(f"/repos/{pin['repository']}/actions/runs/{pin['run_id']}", allow_404=True)
                candidate = replay_pinned_scorecard(card, run, pin)
                scored += 1
            except (ValueError, TypeError, KeyError, UnicodeError, OSError, RuntimeError) as exc:
                candidate = {"status": "UNASSESSED", "percent": None,
                             "reason": "Pinned rubric / CI verification failed: " + str(exc)[:160]}
        row["machine_evidence_score"] = candidate
    snapshot["dual_progress_kind"] = "HISTORICAL_WORKER_VS_PINNED_CI_EVIDENCE"
    snapshot["summary"]["historical_worker_reports"] = sum(row["worker_report"]["percent"] is not None for row in rows)
    snapshot["summary"]["pinned_rubrics_replayed"] = scored
    snapshot["scope"] = "Read-only refs, workflow metadata, canonical digests and approved pinned-scorecard CI replay"
    return snapshot


def markdown_summary(snapshot):
    lines = ["### 크몽 담당자 보고율 vs GitHub 증거 채점", "",
             "| 제품 ID | 담당자 보고 (과거 내부) | 증거 기반 재계산 | 상태 |",
             "|---|---:|---:|---|"]
    for row in snapshot["products"]:
        a, b = row["worker_report"], row["machine_evidence_score"]
        worker = str(a["percent"]) + "%" if a["percent"] is not None else "미기록"
        machine = str(b["percent"]) + "%" if b["percent"] is not None else "미산정"
        lines.append(f"| {row['record_id']} | {worker} | {machine} | {b['status']} |")
    lines.extend(["", "작업자 수치는 과거 내부 기록이며 공식률이 아닙니다. 자동 점수는 승인된 불변 채점표와 동일 SHA Actions 성공을 확인한 경우에만 표시합니다.",
                  "이 표는 고객 수용/상업권/출시/공식률을 승인하거나 변경하지 않습니다."])
    return "\n".join(lines) + "\n"
