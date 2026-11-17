import json
import os
import unittest
from unittest.mock import patch
from instruction_drift import audit, blob_sha, to_markdown, load_snapshot, load_registry, load_env_snapshot, annotation_messages, input_error_note, parse_snapshot
from pathlib import Path
from tempfile import TemporaryDirectory


class DriftTests(unittest.TestCase):
    @staticmethod
    def registry():
        return {"policy_id": "TEST-V1", "policy_blob_sha": blob_sha("latest"),
                "rules": [{"id": "P2_OWNER", "expected": "codex_sol_max",
                           "applies_to": ["chatgpt", "codex"],
                           "recommendation": "P2는 Codex Sol Max가 담당"}]}

    def test_missing_snapshot_generates_notice_not_false_conflict(self):
        report = audit(self.registry(), "latest")
        messages = annotation_messages(report)
        self.assertEqual(len(messages), 1)
        self.assertIn("::notice title=Personal instruction verification pending", messages[0])
        self.assertNotIn("conflict", messages[0].lower())

    def test_malformed_registry_rule_arrays_rejected(self):
        with TemporaryDirectory() as td:
            p = Path(td) / "rules.json"
            invalid = self.registry()
            invalid["schema_version"] = 1
            invalid["rules"][0]["applies_to"] = [["chatgpt"]]
            p.write_text(json.dumps(invalid), encoding="utf-8")
            with self.assertRaises(ValueError):
                load_registry(p)

    def test_conflict_annotation_never_contains_original_value(self):
        profiles = {"chatgpt": {"rules": {"P2_OWNER": "actual_secret_policy"}}}
        report = audit(self.registry(), "latest", profiles)
        messages = annotation_messages(report)
        self.assertTrue(any("::warning title=Instruction alignment recommendation" in x for x in messages))
        self.assertNotIn("actual_secret_policy", "\\n".join(messages))

    def test_incomplete_snapshot_generates_notice(self):
        report = audit(self.registry(), "latest", {"codex": {"rules": {}}})
        self.assertTrue(any("comparison incomplete" in x for x in annotation_messages(report)))

    def test_policy_uncurrent_blocks_all_account_notifications(self):
        report = audit(self.registry(), "old", {"codex": {"rules": {"P2_OWNER": "old"}}})
        messages = annotation_messages(report)
        self.assertEqual(len(messages), 1)
        self.assertIn("Canonical policy changed", messages[0])

    def test_invalid_input_note_does_not_leak_values(self):
        from contextlib import redirect_stdout
        from io import StringIO
        with TemporaryDirectory() as td:
            p = Path(td) / "summary.md"
            b = StringIO()
            with redirect_stdout(b):
                input_error_note(str(p))
            summary = p.read_text(encoding="utf-8")
            self.assertIn("NOT_EVALUATED_INPUT_ERROR", summary)
            self.assertEqual(len(summary.splitlines()), 2)
            self.assertNotIn("rule_snapshot_raw", b.getvalue() + summary)

    def test_malformed_snapshot_top_level_types_fail_closed(self):
        for invalid in (b"null", b"[]", b"true", b'"raw private instruction text"',
                        b'{"schema_version":true,"profiles":{"chatgpt":{"rules":{}}}}'):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                parse_snapshot(invalid)

    def test_malformed_snapshot_profile_shapes_fail_closed(self):
        samples = (
            {"schema_version": 1, "profiles": []},
            {"schema_version": 1, "profiles": {}},
            {"schema_version": 1, "profiles": ["chatgpt"]},
            {"schema_version": 1, "profiles": {"chatgpt": []}},
            {"schema_version": 1, "profiles": {"chatgpt": {"rules": []}}},
            {"schema_version": 1, "profiles": {"chatgpt": {"rules": {"P2_OWNER": None}}}},
            {"schema_version": 1, "profiles": {"chatgpt": {"rules": {"P2_OWNER": 1}}}},
            {"schema_version": 1, "profiles": {"chatgpt": {"rules": {"P2_OWNER": "raw personal information with spaces"}}}},
            {"schema_version": 1, "profiles": {"chatgpt": {"rules": {"P2_OWNER": "x" * 65}}}},
            {"schema_version": 1, "profiles": {"chatgpt": {"rules": {}}, "profile_text": "sensitive"}},
            {"schema_version": 1, "profiles": {"chatgpt": {"rules": {}, "raw_instructions": "PRIVATE"}}},
            {"schema_version": 1, "profiles": {"chatgpt": {"rules": {"P2 OWNER": "valid"}}}},
        )
        for obj in samples:
            with self.subTest(obj_type=type(obj.get("profiles")).__name__, obj=str(obj)[:120]):
                with self.assertRaises(ValueError):
                    parse_snapshot(json.dumps(obj).encode("utf-8"))

    def test_malformed_snapshot_extra_top_level_field_rejected(self):
        obj = {"schema_version": 1, "profiles": {"chatgpt": {"rules": {}}},
               "raw_account_text": "do not send"}
        with self.assertRaises(ValueError):
            parse_snapshot(json.dumps(obj).encode())

    def test_valid_minimal_snapshot_and_partial_profile(self):
        obj = {"schema_version": 1, "profiles": {"chatgpt": {"rules": {"P2_OWNER": "legacy_owner"}}}}
        parsed = parse_snapshot(json.dumps(obj).encode("utf-8"))
        self.assertEqual(parsed["chatgpt"]["rules"]["P2_OWNER"], "legacy_owner")

    def test_registry_rejects_multiline_and_duplicate_public_rules(self):
        with TemporaryDirectory() as td:
            p = Path(td) / "rules.json"
            for mutation in ("newline", "duplicate", "sha", "list", "empty", "bad_id"):
                obj = load_registry()
                if mutation == "newline":
                    obj["rules"][0]["recommendation"] += chr(10) + "unauthorized"
                elif mutation == "duplicate":
                    obj["rules"].append(dict(obj["rules"][0]))
                elif mutation == "sha":
                    obj["policy_blob_sha"] = "0" * 39
                elif mutation == "list":
                    obj["rules"][0]["applies_to"] = ["chatgpt", "chatgpt"]
                elif mutation == "empty":
                    obj["rules"] = []
                else:
                    obj["rules"][0]["id"] = "id with spaces"
                p.write_text(json.dumps(obj), encoding="utf-8")
                with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                    load_registry(p)

    def test_registry_has_public_rules(self):
        self.assertEqual(len(load_registry()["rules"]), 10)

    def test_blob_hash_matches_git(self):
        self.assertEqual(blob_sha("test content"), "08cf6101416f0ce0dda3c80e627f333854c4085c")

    def test_no_snapshot_is_unverified(self):
        report = audit(self.registry(), "latest")
        self.assertEqual(report["profile_results"]["chatgpt"]["status"], "NOT_VERIFIED_NO_SNAPSHOT")
        self.assertEqual(report["profile_results"]["codex"]["status"], "NOT_VERIFIED_NO_SNAPSHOT")

    def test_policy_change_detected(self):
        self.assertEqual(audit(self.registry(), "different")["policy_source_status"], "CHANGED_REVIEW_REQUIRED")

    def test_stale_policy_blocks_false_snapshot_match(self):
        profiles = {"codex": {"rules": {"P2_OWNER": "codex_sol_max"}}}
        result = audit(self.registry(), "changed", profiles)
        self.assertEqual(result["profile_results"]["codex"]["status"], "NOT_EVALUATED_POLICY_UNCURRENT")

    def test_unavailable_policy_not_marked_current(self):
        self.assertEqual(audit(self.registry(), None)["policy_source_status"], "UNAVAILABLE")

    def test_conflict_and_safe_recommendation(self):
        profiles = {"chatgpt": {"rules": {"P2_OWNER": "instant_with_secret_ABC"}}}
        report = audit(self.registry(), "latest", profiles)
        self.assertEqual(report["profile_results"]["chatgpt"]["conflicts"], ["P2_OWNER"])
        self.assertNotIn("secret_ABC", json.dumps(report))
        self.assertNotIn("secret_ABC", to_markdown(report))
        self.assertIn("P2는 Codex", to_markdown(report))

    def test_matches_snapshot_is_not_actual_account_verification(self):
        profiles = {"codex": {"rules": {"P2_OWNER": "codex_sol_max"}}}
        report = audit(self.registry(), "latest", profiles)
        self.assertEqual(report["profile_results"]["codex"]["status"], "SNAPSHOT_RULES_MATCH")
        self.assertFalse(report["profile_results"]["codex"]["account_settings_independently_verified"])

    def test_summary_lists_missing_known_rule_ids_not_private_snapshot_values(self):
        report = audit(self.registry(), "latest", {"chatgpt": {"rules": {}}})
        summary = to_markdown(report)
        self.assertIn("미제공 규칙 ID: `P2_OWNER`", summary)
        self.assertIn("비교 미완료", summary)
        self.assertNotIn("SNAPSHOT_RULES_MATCH", summary)

    def test_summary_explicitly_marks_absent_account_instructions_unverified(self):
        summary = to_markdown(audit(self.registry(), "latest"))
        self.assertIn("NOT_VERIFIED_NO_SNAPSHOT", summary)
        self.assertIn("사본이 없어 실제 충돌 여부를 판정하지 못했습니다", summary)

    def test_missing_rule_detected(self):
        report = audit(self.registry(), "latest", {"chatgpt": {"rules": {}}})
        self.assertEqual(report["profile_results"]["chatgpt"]["status"], "INCOMPLETE_SNAPSHOT")

    def test_unknown_rules_not_exposed(self):
        profiles = {"codex": {"rules": {"P2_OWNER": "codex_sol_max", "secret_info": "password"}}}
        self.assertNotIn("password", json.dumps(audit(self.registry(), "latest", profiles)))

    def test_snapshot_file_no_raw_text_in_output(self):
        with TemporaryDirectory() as td:
            p = Path(td) / "snapshot.json"
            p.write_text(json.dumps({"schema_version": 1, "profiles": {
                "chatgpt": {"rules": {"P2_OWNER": "legacy"}}}}), encoding="utf-8")
            self.assertEqual(load_snapshot(str(p))["chatgpt"]["rules"]["P2_OWNER"], "legacy")

    def test_absent_optional_secret_is_unverified(self):
        with patch.dict(os.environ, {"HAECHONG_INSTRUCTION_RULE_SNAPSHOT_JSON": ""}):
            self.assertIsNone(load_env_snapshot())

    def test_owner_provided_secret_snapshot_is_parsed_without_logging(self):
        value = {"schema_version": 1, "profiles": {"codex": {
            "rules": {"P2_OWNER": "legacy_owner"}}}}
        with patch.dict(os.environ, {"HAECHONG_INSTRUCTION_RULE_SNAPSHOT_JSON": json.dumps(value)}):
            parsed = load_env_snapshot()
        result = audit(self.registry(), "latest", parsed)
        self.assertEqual(result["profile_results"]["codex"]["status"], "DECLARED_CONFLICT")
        self.assertNotIn("legacy_owner", json.dumps(result))

    def test_oversize_secret_snapshot_rejected(self):
        with patch.dict(os.environ, {"HAECHONG_INSTRUCTION_RULE_SNAPSHOT_JSON": "x" * 32769}):
            with self.assertRaises(ValueError):
                load_env_snapshot()

    def test_reject_unsupported_profile(self):
        with TemporaryDirectory() as td:
            p = Path(td) / "snapshot.json"
            p.write_text('{"schema_version":1,"profiles":{"unknown":{"rules":{}}}}')
            with self.assertRaises(ValueError):
                load_snapshot(str(p))


if __name__ == "__main__":
    unittest.main()
