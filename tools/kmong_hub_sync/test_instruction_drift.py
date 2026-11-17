import json
import os
import unittest
from unittest.mock import patch
from instruction_drift import audit, blob_sha, to_markdown, load_snapshot, load_registry, load_env_snapshot
from pathlib import Path
from tempfile import TemporaryDirectory


class DriftTests(unittest.TestCase):
    @staticmethod
    def registry():
        return {"policy_id": "TEST-V1", "policy_blob_sha": blob_sha("latest"),
                "rules": [{"id": "P2_OWNER", "expected": "codex_sol_max",
                           "applies_to": ["chatgpt", "codex"],
                           "recommendation": "P2는 Codex Sol Max가 담당"}]}

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
