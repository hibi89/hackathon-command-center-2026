"""Evidence-readiness review out of 100 for 29 Kmong source products.

NOT official final-blueprint completion. It scores existence/traceability of
repository evidence with one fixed public rubric. A reviewed CI claim only
counts if the exact GitHub run is successful at its pinned SHA/branch.
Buyer acceptance and rights never auto-pass. Source GitHub App remains read-only.
"""
import json
from pathlib import Path
from urllib.parse import quote

import re

REPO_RE = re.compile(r"^hibi89/[A-Za-z0-9_.-]+$", re.I)
SHA40 = re.compile(r"^[0-9a-f]{40}$")


def safe_ref(ref):
    return (isinstance(ref, str) and bool(re.fullmatch(r"[A-Za-z0-9._/-]+", ref))
            and not ref.startswith(("/", "-")) and not ref.endswith("/")
            and all(part not in {"", ".", ".."} for part in ref.split("/")))

ROSTER = Path(__file__).with_name("provisional_evidence_roster_20261114.json")
WEIGHTS = {
    "linked_product_ref": 10,
    "product_blueprint_file": 10,
    "implementation_file": 10,
    "documented_scoped_tests": 10,
    "successful_pinned_functional_ci": 20,
    "linux_and_windows_jobs": 10,
    "documented_ci_packaging": 10,
    "documented_ci_negative_tests": 10,
    "physical_buyer_os_acceptance": 5,
    "rights_and_owner_sale_go": 5,
}
assert sum(WEIGHTS.values()) == 100


def _safe_artifact(item, allowed):
    if not isinstance(item, dict):
        raise ValueError("artifact must be object")
    repo, branch, path = (item.get(k) for k in ("repo", "branch", "path"))
    if not isinstance(repo, str) or not REPO_RE.fullmatch(repo) or repo.lower() not in allowed:
        raise ValueError("artifact repository not allowlisted")
    if not safe_ref(branch) or not isinstance(path, str) or not path or path.startswith("/") or "\\" in path:
        raise ValueError("unsafe artifact ref/path")
    if any(part in {"", ".", ".."} for part in path.split("/")):
        raise ValueError("unsafe artifact traversal")
    return repo, branch, path


def load_manifest(allowed, path=ROSTER):
    obj = json.loads(Path(path).read_text(encoding="utf-8"))
    if obj.get("schema_version") != 1 or obj.get("kind") != "CURATED_PRELIMINARY_REPOSITORY_EVIDENCE":
        raise ValueError("unsupported evidence scoring roster")
    rows = obj.get("records")
    if not isinstance(rows, list) or len(rows) != 29:
        raise ValueError("must explicitly assess exact 29 products")
    ids = set()
    for item in rows:
        rid = item.get("record_id") if isinstance(item, dict) else None
        if not isinstance(rid, str) or rid in ids or not (
            rid.startswith("ACTIVE-") or rid.startswith("CANDIDATE-")):
            raise ValueError("invalid/duplicate record ID")
        ids.add(rid)
        for key in ("source", "blueprint"):
            if item.get(key) is not None:
                _safe_artifact(item[key], allowed)
        ci = item.get("ci")
        if ci is not None:
            if (not isinstance(ci, dict) or ci.get("repo", "").lower() not in allowed
                    or not isinstance(ci.get("run_id"), int) or isinstance(ci["run_id"], bool)
                    or ci["run_id"] <= 0 or not isinstance(ci.get("head_sha"), str)
                    or not SHA40.fullmatch(ci["head_sha"]) or not safe_ref(ci.get("branch"))
                    or not item.get("source") or item["source"]["repo"].lower() != ci["repo"].lower()):
                raise ValueError("unsafe/unlinked CI evidence")
        for k in ("scoped_tests_documented", "package_ci_evidence", "negative_test_ci_evidence",
                  "real_buyer_acceptance", "rights_and_sale_approved"):
            if type(item.get(k)) is not bool:
                raise ValueError("nonboolean claim")
        if item["real_buyer_acceptance"] or item["rights_and_sale_approved"]:
            raise ValueError("customer/rights cannot be self-certified by source snapshot")
    expected = {f"ACTIVE-{i:02d}" for i in range(1, 18)} | {f"CANDIDATE-{i:02d}" for i in range(1, 13)}
    if ids != expected:
        raise ValueError("29 product IDs mismatch")
    return {x["record_id"]: x for x in rows}


def _metadata(observer, item):
    repo, branch, path = item["repo"], item["branch"], item["path"]
    ref = observer.head(repo, branch, missing_ok=True)
    if ref["status"] != "PRESENT":
        return None
    api_path = (f"/repos/{repo}/contents/{quote(path, safe='/')}?"
                f"ref={quote(branch, safe='')}")
    obj = observer.api_get(api_path, allow_404=True)
    if not isinstance(obj, dict) or obj.get("type") != "file":
        return None
    sha = obj.get("sha")
    if not isinstance(sha, str) or not SHA40.fullmatch(sha):
        raise RuntimeError("invalid GitHub contents SHA")
    return {"git_blob_sha": sha, "head_sha": ref["sha"],
            "repository": repo, "branch": branch, "path": path}


def _run(observer, ci):
    if ci is None:
        return None, False, False
    obj = observer.api_get(f"/repos/{ci['repo']}/actions/runs/{ci['run_id']}", allow_404=True)
    if not isinstance(obj, dict):
        return None, False, False
    valid = (obj.get("id") == ci["run_id"] and obj.get("status") == "completed"
             and obj.get("conclusion") == "success"
             and obj.get("head_sha") == ci["head_sha"] and obj.get("head_branch") == ci["branch"])
    if not valid:
        return {"run_id": ci["run_id"], "status": "NOT_ACCEPTED",
                "reason": "missing/failed/stale SHA or branch GitHub run"}, False, False
    payload = {"run_id": ci["run_id"], "status": "EXACT_SHA_SUCCESS",
               "source_sha": ci["head_sha"], "branch": ci["branch"],
               "url": f"https://github.com/{ci['repo']}/actions/runs/{ci['run_id']}"}
    jobs = observer.api_get(f"/repos/{ci['repo']}/actions/runs/{ci['run_id']}/jobs?per_page=100", allow_404=True)
    if not isinstance(jobs, dict) or not isinstance(jobs.get("jobs"), list):
        return payload, True, False
    if jobs.get("total_count", len(jobs["jobs"])) > len(jobs["jobs"]):
        return payload, True, False
    good = [str(j.get("name", "")).lower() for j in jobs["jobs"]
            if isinstance(j, dict) and j.get("conclusion") == "success"]
    cross = (any("windows" in n or "win202" in n for n in good)
             and any("ubuntu" in n or "linux" in n for n in good))
    payload["cross_os_jobs_validated"] = bool(cross)
    return payload, True, cross


def score_snapshot(snapshot, observer, allowed_repositories, index):
    """Numerical proof coverage, not product quality or official final completion."""
    if snapshot.get("no_official_score_authorization") is not True:
        raise ValueError("official score immutability required")
    allowed = {x.lower() for x in allowed_repositories}
    roster = load_manifest(allowed)
    rows = snapshot.get("products", [])
    products = index.get("records", [])
    if len(rows) != 29 or len(products) != 29:
        raise ValueError("29 records required")
    canonical = {x["record_id"]: x for x in products}
    if set(canonical) != set(roster) or {x["record_id"] for x in rows} != set(roster):
        raise ValueError("central index/observation and scoring IDs differ")
    for row in rows:
        rid = row["record_id"]
        entry = roster[rid]
        points = {k: 0 for k in WEIGHTS}
        proof = {}
        risk = []
        if row.get("status") == "PRESENT" and isinstance(row.get("head_sha"), str) and SHA40.fullmatch(row["head_sha"]):
            points["linked_product_ref"] = 10
        if entry.get("blueprint"):
            bp = _metadata(observer, entry["blueprint"])
            if bp:
                points["product_blueprint_file"] = 10
                proof["blueprint"] = bp
        if entry.get("source"):
            src = _metadata(observer, entry["source"])
            if src:
                points["implementation_file"] = 10
                proof["implementation"] = src
                if (entry["scoped_tests_documented"]
                        and _metadata(observer, {"repo": entry["source"]["repo"],
                                                 "branch": entry["source"]["branch"], "path": "HANDOFF.md"})):
                    points["documented_scoped_tests"] = 10
        ci, passed, cross = _run(observer, entry.get("ci"))
        if ci:
            proof["functional_ci"] = ci
        if passed and points["implementation_file"]:
            points["successful_pinned_functional_ci"] = 20
            if cross:
                points["linux_and_windows_jobs"] = 10
            if entry["package_ci_evidence"]:
                points["documented_ci_packaging"] = 10
            if entry["negative_test_ci_evidence"]:
                points["documented_ci_negative_tests"] = 10
            if entry.get("ci", {}).get("branch") != entry.get("source", {}).get("branch"):
                risk.append("CI validates a different historical branch, not the current source head")
            elif proof["implementation"]["head_sha"] != entry["ci"]["head_sha"]:
                risk.append("CI source SHA differs from current documentation/source branch head")
        if entry.get("source") and (canonical[rid].get("repository") != entry["source"]["repo"] or canonical[rid].get("tracked_branch") != entry["source"]["branch"]):
            risk.append("Central product link differs from actual implementation source")
        # No automated assignment for physical buyer, legal usage rights or sale approval.
        numeric = sum(points.values())
        row["provisional_evidence_readiness"] = {
            "score": numeric, "denominator": 100, "status": "AUTOMATED_METADATA_PLUS_REVIEWED_EVIDENCE",
            "rubric": "GITHUB_EVIDENCE_READINESS_V1", "rubric_weights": WEIGHTS,
            "points": points, "proof": proof, "risk": risk,
            "official_final_completion": "NOT_DERIVED",
            "product_100_percent_certified": False, "commercial_release_authorized": False,
            "limitations": "Fixed evidence-readiness metric; not product functional coverage, owner-approved per-REQ weights, independent buyer QA or commercial clearance."
        }
    snapshot["summary"]["provisional_evidence_scores"] = len(rows)
    snapshot["summary"]["provisional_official_certifications"] = 0
    snapshot["provisional_score_policy"] = "GITHUB_EVIDENCE_READINESS_V1_NOT_OFFICIAL_COMPLETION"
    return snapshot


def markdown_scores(snapshot, index):
    names = {r["record_id"]: r["product"] for r in index["records"]}
    lines = ["### 29개 제품 — GitHub 검증증거 확보점수 (잠정·공식률 아님)", "",
             "| 제품 | 작업자 내부 보고 | 증거점수/100 | 공식 사용자 수용점수 |",
             "|---|---:|---:|---:|"]
    official = {r["record_id"]: r["official_final_completion"] for r in index["records"]}
    for row in sorted(snapshot["products"], key=lambda x: (-x["provisional_evidence_readiness"]["score"], x["record_id"])):
        score = row["provisional_evidence_readiness"]["score"]
        worker = row["worker_report"]["percent"]
        w = str(worker) + "%" if worker is not None else "미기록"
        current_official = official[row["record_id"]]
        if current_official == "UNASSESSED":
            current_official = "미산정"
        lines.append(f"| {names[row['record_id']]} | {w} | {score} | {current_official} |")
    lines.extend(["", "이 수치의 100점 분모는 GitHub 증거 접근성/재현성/실물 확인으로 구성한 공통 기준입니다. **제품 최종설계 달성률 100점과 다릅니다.**",
                  "누락 증거에 0점이 매겨져도 개발 자체가 없다는 의미가 아닙니다. 의뢰인 PC/라이선스·권리·판매 GO는 자동 통과되지 않습니다."])
    return "\n".join(lines) + "\n"
