#!/usr/bin/env python3
"""Read-only policy/instruction alignment advisor; never accesses private accounts."""
import argparse
import hashlib
import json
import os
import re
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

HERE = Path(__file__).resolve().parent
CONFIG = HERE / "instruction_alignment_rules.json"
POLICY_URL = ("https://raw.githubusercontent.com/hibi89/hackathon-command-center-2026/"
              "kmong-productization/docs/strategy/OWNER_DEV_EXECUTION_CANONICAL_20261116.md")
PROFILES = ("chatgpt", "codex")
# Policy v2.1 cannot silently omit an approved rule or switch its source
# without a reviewed code change. This list is public and contains no account data.
REQUIRED_RULE_IDS = frozenset((
    "P0_DESIGN_OWNER", "P1_IMPLEMENTATION_OWNER", "P2_VALIDATION_OWNER",
    "P3_ASTRA_ROLE", "P4_POST_ASTRA_REVIEW", "P1_BROWSER_DEFERRAL",
    "BOTTLENECK_REPLAN", "PROGRESS_METRICS", "MISSION_LOCK",
    "OWNER_APPROVAL",
))
POLICY_PATH = "docs/strategy/OWNER_DEV_EXECUTION_CANONICAL_20261116.md"


def _unique_object_pairs(pairs):
    """Reject ambiguous duplicate JSON keys without exposing their values."""
    obj = {}
    for key, value in pairs:
        if key in obj:
            raise ValueError("Duplicate JSON object key")
        obj[key] = value
    return obj


def _decode_strict_json(contents):
    # Reject excessive structural depth independently of Python/JSON decoder
    # recursion limits. Brackets inside quoted strings are not structural.
    source = contents.decode("utf-8") if isinstance(contents, bytes) else contents
    quoted = escaped = False
    depth = 0
    for char in source:
        if quoted:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                quoted = False
        elif char == '"':
            quoted = True
        elif char in "[{":
            depth += 1
            if depth > 64:
                raise ValueError("JSON nesting limit exceeded")
        elif char in "]}":
            depth -= 1
    try:
        return json.loads(source, object_pairs_hook=_unique_object_pairs)
    except RecursionError:
        raise ValueError("JSON nesting limit exceeded") from None


def blob_sha(contents):
    data = contents.encode("utf-8")
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


def load_registry(path=CONFIG):
    """Public policy rules are version-pinned; never interpret malformed input."""
    obj = _decode_strict_json(Path(path).read_text(encoding="utf-8"))
    if (not isinstance(obj, dict) or type(obj.get("schema_version")) is not int
            or obj["schema_version"] != 1
            or not isinstance(obj.get("policy_id"), str)
            or not re.fullmatch(r"[A-Z][A-Z0-9_.-]{2,80}", obj["policy_id"])
            or not isinstance(obj.get("policy_blob_sha"), str)
            or not re.fullmatch(r"[a-f0-9]{40}", obj["policy_blob_sha"])
            or not isinstance(obj.get("rules"), list) or not obj["rules"]
            or set(obj) - {"schema_version", "policy_id", "policy_path",
                           "policy_blob_sha", "rules"}
            or obj.get("policy_path") != POLICY_PATH):
        raise ValueError("Invalid instruction alignment registry")
    keys = set()
    for rule in obj["rules"]:
        if not isinstance(rule, dict) or set(rule) - {
                "id", "expected", "applies_to", "recommendation", "policy_anchor"}:
            raise ValueError("Invalid alignment rule")
        applies = rule.get("applies_to")
        key = rule.get("id")
        expected = rule.get("expected")
        recommendation = rule.get("recommendation")
        anchor = rule.get("policy_anchor")
        if (not isinstance(anchor, str) or not 1 <= len(anchor) <= 240
                or not anchor.isprintable()):
            raise ValueError("Invalid policy rule anchor")
        if (not isinstance(key, str) or not re.fullmatch(r"[A-Z][A-Z0-9_]{1,63}", key)
                or not isinstance(expected, str)
                or not re.fullmatch(r"[a-z][a-z0-9_]{0,63}", expected)
                or not isinstance(recommendation, str)
                or not 1 <= len(recommendation) <= 512
                or not recommendation.isprintable()
                or not isinstance(applies, list) or not applies
                or any(not isinstance(p, str) or p not in PROFILES for p in applies)
                or len(set(applies)) != len(applies)
                or key in keys):
            raise ValueError("Invalid or duplicate alignment rule")
        keys.add(key)
    if keys != REQUIRED_RULE_IDS:
        raise ValueError("Incomplete or unexpected instruction alignment rule IDs")
    return obj


def fetch_policy():
    request = Request(POLICY_URL, headers={"User-Agent": "haechong-instruction-alignment/1"})
    try:
        with urlopen(request, timeout=8) as response:
            content = response.read(131073)
        if len(content) > 131072:
            return None
        return content.decode("utf-8")
    except (HTTPError, URLError, TimeoutError, UnicodeError, OSError):
        return None


def parse_snapshot(contents):
    """Accept only normalized, non-sensitive rule IDs: never raw instruction text.

    This does not attest to the actual ChatGPT/Codex account settings; it is an
    owner-provided *declaration* of the state the owner checked independently.
    """
    if len(contents) > 32768:
        raise ValueError("Instruction snapshot too large")
    obj = _decode_strict_json(contents)
    if (not isinstance(obj, dict) or type(obj.get("schema_version")) is not int
            or obj["schema_version"] != 1 or set(obj) != {"schema_version", "profiles"}):
        raise ValueError("Invalid instruction snapshot schema")
    profiles = obj.get("profiles")
    if (not isinstance(profiles, dict) or not profiles
            or any(not isinstance(name, str) or name not in PROFILES for name in profiles)):
        raise ValueError("Invalid instruction profiles")
    for item in profiles.values():
        if not isinstance(item, dict) or set(item) != {"rules"}:
            raise ValueError("Invalid instruction profile object")
        values = item["rules"]
        if not isinstance(values, dict):
            raise ValueError("Invalid instruction profile rule mapping")
        for key, value in values.items():
            if (not isinstance(key, str)
                    or not re.fullmatch(r"[A-Z][A-Z0-9_]{1,63}", key)
                    or not isinstance(value, str)
                    or not re.fullmatch(r"[a-z][a-z0-9_]{0,63}", value)):
                raise ValueError("Snapshot must contain only short normalized rule IDs/values")
    return profiles


def load_snapshot(path):
    if not path:
        return None
    # Read at most one byte beyond the public 32 KiB schema limit. Never load
    # an arbitrary-sized owner-supplied file into memory before validating it.
    with open(path, "rb") as stream:
        return parse_snapshot(stream.read(32769))


def load_env_snapshot():
    raw = os.environ.get("HAECHONG_INSTRUCTION_RULE_SNAPSHOT_JSON", "")
    return parse_snapshot(raw.encode("utf-8")) if raw else None


def audit(registry, source, snapshots=None):
    expected_sha = registry["policy_blob_sha"]
    source_sha = blob_sha(source) if source is not None else None
    source_status = ("UNAVAILABLE" if source is None else
                     "CURRENT" if source_sha == expected_sha else "CHANGED_REVIEW_REQUIRED")
    # Anchors locate obvious rule changes; their presence never proves semantic equivalence.
    missing_anchors = ([rule["id"] for rule in registry["rules"]
                        if rule.get("policy_anchor") and source is not None
                        and rule["policy_anchor"] not in source])
    if source_status == "CURRENT" and missing_anchors:
        source_status = "RULE_ANCHOR_MISMATCH"
    by_profile = {}
    for name in PROFILES:
        if source_status != "CURRENT":
            by_profile[name] = {"status": "NOT_EVALUATED_POLICY_UNCURRENT", "conflicts": [],
                                "missing_rule_ids": [], "recommendations": []}
            continue
        record = (snapshots or {}).get(name)
        if record is None:
            by_profile[name] = {"status": "NOT_VERIFIED_NO_SNAPSHOT", "conflicts": [],
                                "missing_rule_ids": [], "recommendations": []}
            continue
        values = record["rules"]
        conflicts, missing, recommendations = [], [], []
        for rule in registry["rules"]:
            if name not in rule["applies_to"]:
                continue
            key = rule["id"]
            if key not in values:
                missing.append(key)
            elif values[key] != rule["expected"]:
                conflicts.append(key)
                recommendations.append({"rule_id": key, "text": rule["recommendation"]})
        by_profile[name] = {
            "status": ("DECLARED_CONFLICT" if conflicts else
                       "INCOMPLETE_SNAPSHOT" if missing else "SNAPSHOT_RULES_MATCH"),
            "conflicts": conflicts, "missing_rule_ids": missing,
            "recommendations": recommendations,
            "account_settings_independently_verified": False,
        }
    return {
        "policy_id": registry["policy_id"],
        "policy_source_status": source_status,
        "expected_policy_blob_sha": expected_sha,
        "observed_policy_blob_sha": source_sha,
        "potential_rule_review_ids": missing_anchors,
        "profile_results": by_profile,
        "actual_account_settings_access": "UNAVAILABLE",
        "action": ("UPDATE_RULE_BASELINE_AND_REVIEW_INSTRUCTIONS" if source_status == "CHANGED_REVIEW_REQUIRED"
                   else "REVIEW_RULE_ANCHOR_MISMATCH" if source_status == "RULE_ANCHOR_MISMATCH"
                   else "RETRY_POLICY_SOURCE" if source_status == "UNAVAILABLE"
                   else "REVIEW_DECLARED_CONFLICTS" if any(v["status"] == "DECLARED_CONFLICT" for v in by_profile.values())
                   else "COMPLETE_OWNER_RULE_SNAPSHOT" if any(v["status"] == "INCOMPLETE_SNAPSHOT" for v in by_profile.values())
                   else "OWNER_PROVIDE_RULE_SNAPSHOT" if any(v["status"] == "NOT_VERIFIED_NO_SNAPSHOT" for v in by_profile.values())
                   else "SNAPSHOT_RULES_MATCH_ACCOUNT_UNVERIFIED"),
    }


def to_markdown(report, registry=None):
    """Explain known public rules; never infer or echo private account instructions."""
    rows = ["### 해총 개인지침·Codex 지침 충돌 권고 (advisory)",
            f"- 정책 정본: `{report['policy_id']}` / 원격 상태: `{report['policy_source_status']}`",
            f"- 실제 계정 설정 직접 읽기: `{report['actual_account_settings_access']}`",
            f"- 권고: `{report['action']}`"]
    if report["policy_source_status"] != "CURRENT":
        candidates = report.get("potential_rule_review_ids", [])
        rows.append("- 원격 정본 변경/조회 실패 상태에서는 계정 지침 일치를 판정하지 않습니다.")
        if candidates:
            rows.append("- 우선 재검토할 공개 규칙 ID: " +
                        ", ".join("`" + key + "`" for key in candidates))
        rows.append("- **앵커 검사는 보조 신호일 뿐입니다.** 누락된 앵커가 없어도 정책 문구가 변경되었다면 모든 관련 규칙을 수동 검토하세요.")
    for name, item in report["profile_results"].items():
        rows.append(f"- {name}: `{item['status']}`; 충돌 규칙: "
                    + (", ".join(f"`{v}`" for v in item["conflicts"]) or "없음/미확인"))
        missing = item.get("missing_rule_ids", [])
        if missing:
            rows.append("  - 미제공 규칙 ID: " + ", ".join(f"`{v}`" for v in missing)
                        + " (비교 미완료, 일치 판정 아님)")
        if item["status"] == "NOT_VERIFIED_NO_SNAPSHOT":
            rows.append("  - 계정 지침 사본이 없어 실제 충돌 여부를 판정하지 못했습니다.")
        for fix in item["recommendations"]:
            rows.append(f"  - `{fix['rule_id']}`: {fix['text']}")
    if registry is not None and report["policy_source_status"] == "CURRENT":
        unresolved = {}
        for rule in registry["rules"]:
            names = []
            for name in rule["applies_to"]:
                profile = report["profile_results"][name]
                if profile["status"] == "NOT_VERIFIED_NO_SNAPSHOT":
                    names.append(name)
                elif rule["id"] in profile.get("missing_rule_ids", []):
                    names.append(name)
            if names:
                unresolved[rule["id"]] = (names, rule)
        if unresolved:
            rows.extend(["", "#### 소유자 수동 점검 목록 — 실제 계정 설정은 미조회",
                         "아래는 현재 정본의 **기대 규칙**이며 적용 여부를 확인한 결과가 아닙니다. "
                         "계정 지침을 직접 확인한 뒤 비민감 규칙 ID/값만 등록하세요."])
            for key, (names, rule) in unresolved.items():
                rows.append("- [ ] " + key + " (" + ", ".join(names) + "): "
                            + rule["recommendation"] + " — 기준 " + rule["expected"])
    rows.append("- 주의: 지침 원문은 수집·저장·출력하지 않으며, 사본 일치는 계정 실제 적용을 증명하지 않습니다.")
    return "\n".join(rows) + "\n"


def annotation_messages(report):
    """Sanitized, actionable Actions annotations; never include supplied rule values."""
    status = report["policy_source_status"]
    if status == "RULE_ANCHOR_MISMATCH":
        return ["::warning title=Instruction policy registry mismatch::Expected public rule anchors do not match the pinned policy; no account check was made"]
    if status != "CURRENT":
        return ["::warning title=Instruction policy review::Canonical policy changed or is unavailable; review rule baseline before comparing account settings"]
    profiles = report["profile_results"]
    messages = []
    if any(profile["status"] == "DECLARED_CONFLICT" for profile in profiles.values()):
        messages.append("::warning title=Instruction alignment recommendation::Declared instruction rule conflicts exist; see the job summary for fixed replacement guidance")
    if any(profile["status"] == "INCOMPLETE_SNAPSHOT" for profile in profiles.values()):
        messages.append("::notice title=Instruction comparison incomplete::One or more declared rules are missing from the provided snapshot")
    if any(profile["status"] == "NOT_VERIFIED_NO_SNAPSHOT" for profile in profiles.values()):
        messages.append("::notice title=Personal instruction verification pending::Current ChatGPT or Codex account instructions cannot be read; owner-supplied non-sensitive rule snapshot is needed")
    return messages


def input_error_note(summary_path):
    """Never reflect untrusted secret input in annotations or job summaries."""
    message = "::warning title=Instruction advisory input error::Invalid policy rule registry or owner snapshot; no account settings were checked"
    print(message)
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as stream:
            stream.write("### Instruction advisory: NOT_EVALUATED_INPUT_ERROR\n"
                         "- Policy/account comparison was skipped. Check the non-sensitive rule format without pasting secret values into logs.\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--snapshot", help="Optional local minimal rule-ID export; never raw instruction text")
    parser.add_argument("--summary", help="GitHub Actions job summary file")
    args = parser.parse_args()
    try:
        registry = load_registry()
        # No profile source configured means NOT_VERIFIED, never an inferred match.
        snapshot = load_snapshot(args.snapshot) if args.snapshot else load_env_snapshot()
        report = audit(registry, fetch_policy(), snapshot)
    except (ValueError, TypeError, OSError, json.JSONDecodeError):
        input_error_note(args.summary)
        raise SystemExit(2)
    print(json.dumps(report, ensure_ascii=False, sort_keys=True))
    if args.summary:
        with open(args.summary, "a", encoding="utf-8") as stream:
            stream.write(to_markdown(report, registry))
    for message in annotation_messages(report):
        print(message)


if __name__ == "__main__":
    main()
