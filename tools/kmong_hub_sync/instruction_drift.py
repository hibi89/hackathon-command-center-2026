#!/usr/bin/env python3
"""Read-only policy/instruction alignment advisor; never accesses private accounts."""
import argparse
import hashlib
import json
import os
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

HERE = Path(__file__).resolve().parent
CONFIG = HERE / "instruction_alignment_rules.json"
POLICY_URL = ("https://raw.githubusercontent.com/hibi89/hackathon-command-center-2026/"
              "kmong-productization/docs/strategy/OWNER_DEV_EXECUTION_CANONICAL_20261116.md")
PROFILES = ("chatgpt", "codex")


def blob_sha(contents):
    data = contents.encode("utf-8")
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


def load_registry(path=CONFIG):
    obj = json.loads(Path(path).read_text(encoding="utf-8"))
    if (not isinstance(obj, dict) or obj.get("schema_version") != 1 or not isinstance(obj.get("policy_id"), str)
            or not isinstance(obj.get("policy_blob_sha"), str)
            or not isinstance(obj.get("rules"), list)):
        raise ValueError("Invalid instruction alignment registry")
    keys = set()
    for rule in obj["rules"]:
        if not isinstance(rule, dict):
            raise ValueError("Invalid alignment rule")
        applies = rule.get("applies_to", [])
        if (not isinstance(rule, dict) or not isinstance(rule.get("id"), str)
                or not isinstance(rule.get("expected"), str)
                or not isinstance(rule.get("recommendation"), str)
                or not isinstance(applies, list)
                or not all(isinstance(value, str) and value in PROFILES for value in applies)
                or not applies or rule["id"] in keys):
            raise ValueError("Invalid or duplicate alignment rule")
        keys.add(rule["id"])
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
    if len(contents) > 32768:
        raise ValueError("Instruction snapshot too large")
    obj = json.loads(contents)
    if not isinstance(obj, dict) or obj.get("schema_version") != 1:
        raise ValueError("Invalid instruction snapshot schema")
    profiles = obj.get("profiles")
    if not isinstance(profiles, dict) or set(profiles) - set(PROFILES):
        raise ValueError("Invalid instruction profiles")
    for item in profiles.values():
        if not isinstance(item, dict) or not isinstance(item.get("rules"), dict):
            raise ValueError("Invalid instruction profile rule mapping")
    return profiles


def load_snapshot(path):
    return parse_snapshot(Path(path).read_bytes()) if path else None


def load_env_snapshot():
    raw = os.environ.get("HAECHONG_INSTRUCTION_RULE_SNAPSHOT_JSON", "")
    return parse_snapshot(raw.encode("utf-8")) if raw else None


def audit(registry, source, snapshots=None):
    expected_sha = registry["policy_blob_sha"]
    source_sha = blob_sha(source) if source is not None else None
    source_status = ("UNAVAILABLE" if source is None else
                     "CURRENT" if source_sha == expected_sha else "CHANGED_REVIEW_REQUIRED")
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
        "profile_results": by_profile,
        "actual_account_settings_access": "UNAVAILABLE",
        "action": ("UPDATE_RULE_BASELINE_AND_REVIEW_INSTRUCTIONS" if source_status == "CHANGED_REVIEW_REQUIRED"
                   else "RETRY_POLICY_SOURCE" if source_status == "UNAVAILABLE"
                   else "OWNER_PROVIDE_RULE_SNAPSHOT" if snapshots is None
                   else "REVIEW_PROFILE_RECOMMENDATIONS"),
    }


def to_markdown(report):
    rows = ["### 해총 개인지침·Codex 지침 충돌 권고 (advisory)",
            f"- 정책 정본: `{report['policy_id']}` / 원격 상태: `{report['policy_source_status']}`",
            f"- 실제 계정 설정 직접 읽기: `{report['actual_account_settings_access']}`",
            f"- 권고: `{report['action']}`"]
    for name, item in report["profile_results"].items():
        rows.append(f"- {name}: `{item['status']}`; 충돌 규칙: "
                    + (", ".join(f"`{v}`" for v in item["conflicts"]) or "없음/미확인"))
        for fix in item["recommendations"]:
            rows.append(f"  - `{fix['rule_id']}`: {fix['text']}")
    rows.append("- 주의: 지침 원문은 수집·저장·출력하지 않으며, 사본 일치는 계정 실제 적용을 증명하지 않습니다.")
    return "\n".join(rows) + "\n"


def annotation_messages(report):
    """Sanitized, actionable Actions annotations; never include supplied rule values."""
    status = report["policy_source_status"]
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
            stream.write("### Instruction advisory: NOT_EVALUATED_INPUT_ERROR\\n"
                         "- Policy/account comparison was skipped. Check the non-sensitive rule format without pasting secret values into logs.\\n")


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
            stream.write(to_markdown(report))
    for message in annotation_messages(report):
        print(message)


if __name__ == "__main__":
    main()
