import json
import os
import unittest
from unittest.mock import patch
from instruction_drift import audit, blob_sha, to_markdown, load_snapshot, load_registry, load_env_snapshot, annotation_messages, input_error_note, parse_snapshot, main
from pathlib import Path
from tempfile import TemporaryDirectory


class DriftTests(unittest.TestCase):
    @staticmethod
    def registry():
        return {"policy_id": "TEST-V1", "policy_blob_sha": blob_sha("latest"),
                "rules": [{"id": "P2_OWNER", "expected": "codex_sol_max",
                           "applies_to": ["chatgpt", "codex"],
                           "recommendation": "P2는 Codex Sol Max가 담당"}]}

    def test_duplicate_snapshot_keys_fail_closed_at_every_depth(self):
        samples = (
            '{"schema_version":1,"schema_version":1,"profiles":{"chatgpt":{"rules":{}}}}',
            '{"schema_version":1,"profiles":{"chatgpt":{"rules":{}},"chatgpt":{"rules":{}}}}',
            '{"schema_version":1,"profiles":{"chatgpt":{"rules":{"P2_OWNER":"legacy","P2_OWNER":"codex_sol_max"}}}}',
            '{"schema_version":1,"profiles":{"chatgpt":{"rules":{},"rules":{}}}}',
        )
        for sample in samples:
            with self.subTest(sample=sample), self.assertRaisesRegex(
                    ValueError, "Duplicate JSON object key"):
                parse_snapshot(sample.encode("utf-8"))

    def test_registry_rejects_duplicate_keys_and_unrecognized_fields(self):
        with TemporaryDirectory() as td:
            p = Path(td) / "rules.json"
            original = (Path(__file__).parent / "instruction_alignment_rules.json").read_text(
                encoding="utf-8")
            p.write_text(original.replace('"schema_version": 1,',
                                          '"schema_version": 1, "schema_version": 1,', 1),
                         encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Duplicate JSON object key"):
                load_registry(p)
            for extra_scope in ("top", "rule"):
                obj = load_registry()
                if extra_scope == "top":
                    obj["unexpected_payload"] = "SYNTHETIC_TEST_VALUE"
                else:
                    obj["rules"][0]["unexpected_payload"] = "SYNTHETIC_TEST_VALUE"
                p.write_text(json.dumps(obj), encoding="utf-8")
                with self.subTest(extra_scope=extra_scope), self.assertRaises(ValueError):
                    load_registry(p)

    def test_registry_rejects_controls_in_public_guidance(self):
        with TemporaryDirectory() as td:
            p = Path(td) / "rules.json"
            for field in ("policy_anchor", "recommendation"):
                for control in (chr(27) + "[31m", chr(0x2028), chr(9)):
                    obj = load_registry()
                    obj["rules"][0][field] += control
                    p.write_text(json.dumps(obj), encoding="utf-8")
                    with self.subTest(field=field, control=repr(control)):
                        with self.assertRaises(ValueError):
                            load_registry(p)

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

    def test_deep_snapshot_json_fails_with_sanitized_schema_error(self):
        deeply_nested = ("[" * 1200 + "0" + "]" * 1200).encode("ascii")
        with self.assertRaisesRegex(ValueError, "JSON nesting limit exceeded"):
            parse_snapshot(deeply_nested)

    def test_snapshot_file_read_is_bounded_by_schema_limit(self):
        with TemporaryDirectory() as td:
            path = Path(td) / "oversized.json"
            path.write_bytes(b"x" * 65536)
            with self.assertRaisesRegex(ValueError, "Instruction snapshot too large"):
                load_snapshot(str(path))

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

    def test_registry_cannot_silently_remove_or_replace_approved_rule(self):
        with TemporaryDirectory() as td:
            p = Path(td) / "rules.json"
            for mutation in ("missing", "unexpected", "no_anchor", "wrong_path", "no_path"):
                obj = load_registry()
                if mutation == "missing":
                    obj["rules"].pop()
                elif mutation == "unexpected":
                    obj["rules"][0]["id"] = "AN_UNAPPROVED_RULE"
                elif mutation == "no_anchor":
                    del obj["rules"][0]["policy_anchor"]
                elif mutation == "wrong_path":
                    obj["policy_path"] = "docs/strategy/OTHER_POLICY.md"
                else:
                    del obj["policy_path"]
                p.write_text(json.dumps(obj), encoding="utf-8")
                with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                    load_registry(p)

    def test_registry_has_pinned_anchors_for_every_operating_rule(self):
        registry = load_registry()
        self.assertEqual(len(registry["rules"]), 10)
        self.assertTrue(all(rule.get("policy_anchor") for rule in registry["rules"]))

    def test_cli_summary_end_to_end_when_accounts_unavailable(self):
        from contextlib import redirect_stdout
        from io import StringIO
        with TemporaryDirectory() as td:
            summary = Path(td) / "summary.md"
            stdout = StringIO()
            with (patch("instruction_drift.load_registry", return_value=self.registry()),
                  patch("instruction_drift.fetch_policy", return_value="latest"),
                  patch("sys.argv", ["advisory", "--summary", str(summary)]),
                  patch.dict(os.environ, {"HAECHONG_INSTRUCTION_RULE_SNAPSHOT_JSON": ""}),
                  redirect_stdout(stdout)):
                main()
            obj = json.loads(stdout.getvalue().splitlines()[0])
            self.assertEqual(obj["policy_source_status"], "CURRENT")
            self.assertEqual(obj["profile_results"]["chatgpt"]["status"], "NOT_VERIFIED_NO_SNAPSHOT")
            self.assertIn("Personal instruction verification pending", stdout.getvalue())
            self.assertIn("NOT_VERIFIED_NO_SNAPSHOT", summary.read_text(encoding="utf-8"))

    def test_cli_input_error_no_secret_echo_or_false_success(self):
        from contextlib import redirect_stdout
        from io import StringIO
        with TemporaryDirectory() as td:
            summary = Path(td) / "summary.md"
            stdout = StringIO()
            with (patch("instruction_drift.load_registry", return_value=self.registry()),
                  patch("instruction_drift.fetch_policy", return_value="latest"),
                  patch("sys.argv", ["advisory", "--summary", str(summary)]),
                  patch.dict(os.environ, {"HAECHONG_INSTRUCTION_RULE_SNAPSHOT_JSON":
                                           '{"schema_version":1,"profiles":{"chatgpt":{"raw_instructions":"PRIVATE_TOKEN_VALUE","rules":{}}}}'}),
                  redirect_stdout(stdout)):
                with self.assertRaises(SystemExit) as raised:
                    main()
            self.assertEqual(raised.exception.code, 2)
            self.assertIn("NOT_EVALUATED_INPUT_ERROR", summary.read_text(encoding="utf-8"))
            self.assertNotIn("PRIVATE_TOKEN_VALUE", stdout.getvalue() + summary.read_text(encoding="utf-8"))

    def test_registry_has_public_rules(self):
        self.assertEqual(len(load_registry()["rules"]), 10)

    def test_blob_hash_matches_git(self):
        self.assertEqual(blob_sha("test content"), "08cf6101416f0ce0dda3c80e627f333854c4085c")

    def test_no_snapshot_is_unverified(self):
        report = audit(self.registry(), "latest")
        self.assertEqual(report["profile_results"]["chatgpt"]["status"], "NOT_VERIFIED_NO_SNAPSHOT")
        self.assertEqual(report["profile_results"]["codex"]["status"], "NOT_VERIFIED_NO_SNAPSHOT")

    def test_policy_rule_anchor_present_has_no_candidates(self):
        registry = self.registry()
        registry["rules"][0]["policy_anchor"] = "latest"
        report = audit(registry, "latest")
        self.assertEqual(report["policy_source_status"], "CURRENT")
        self.assertEqual(report["potential_rule_review_ids"], [])

    def test_policy_change_missing_anchor_flags_candidate_and_never_verifies(self):
        registry = self.registry()
        registry["rules"][0]["policy_anchor"] = "latest"
        report = audit(registry, "changed", {"codex": {"rules": {"P2_OWNER": "codex_sol_max"}}})
        self.assertEqual(report["policy_source_status"], "CHANGED_REVIEW_REQUIRED")
        self.assertEqual(report["potential_rule_review_ids"], ["P2_OWNER"])
        self.assertEqual(report["profile_results"]["codex"]["status"], "NOT_EVALUATED_POLICY_UNCURRENT")
        self.assertIn("P2_OWNER", to_markdown(report, registry))
        self.assertIn("앵커 검사는 보조 신호", to_markdown(report, registry))

    def test_policy_change_with_anchor_still_requires_manual_review(self):
        registry = self.registry()
        registry["rules"][0]["policy_anchor"] = "unchanged_anchor"
        report = audit(registry, "changed unchanged_anchor")
        self.assertEqual(report["policy_source_status"], "CHANGED_REVIEW_REQUIRED")
        self.assertEqual(report["potential_rule_review_ids"], [])
        self.assertIn("모든 관련 규칙을 수동 검토", to_markdown(report, registry))

    def test_policy_current_with_missing_anchor_is_not_misreported_match(self):
        registry = self.registry()
        registry["rules"][0]["policy_anchor"] = "not_in_latest"
        report = audit(registry, "latest", {"codex": {"rules": {"P2_OWNER": "codex_sol_max"}}})
        self.assertEqual(report["policy_source_status"], "RULE_ANCHOR_MISMATCH")
        self.assertEqual(report["action"], "REVIEW_RULE_ANCHOR_MISMATCH")
        self.assertEqual(report["profile_results"]["codex"]["status"], "NOT_EVALUATED_POLICY_UNCURRENT")
        self.assertTrue(any("registry mismatch" in x for x in annotation_messages(report)))

    def test_registry_rejects_invalid_rule_anchor(self):
        with TemporaryDirectory() as td:
            p = Path(td) / "rules.json"
            for invalid in (123, [], "", "x" * 241, "a" + chr(10) + "b"):
                obj = load_registry()
                obj["rules"][0]["policy_anchor"] = invalid
                p.write_text(json.dumps(obj), encoding="utf-8")
                with self.subTest(anchor_type=type(invalid).__name__), self.assertRaises(ValueError):
                    load_registry(p)

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

    def test_summary_owner_checklist_is_explicitly_unverified(self):
        registry = self.registry()
        report = audit(registry, "latest")
        summary = to_markdown(report, registry)
        self.assertIn("소유자 수동 점검 목록", summary)
        self.assertIn("P2_OWNER (chatgpt, codex)", summary)
        self.assertIn("기대 규칙", summary)
        self.assertIn("실제 계정 설정은 미조회", summary)

    def test_summary_checklist_restricted_to_missing_rules(self):
        registry = self.registry()
        declaration = {"chatgpt": {"rules": {"P2_OWNER": "codex_sol_max"}},
                       "codex": {"rules": {}}}
        report = audit(registry, "latest", declaration)
        summary = to_markdown(report, registry)
        self.assertIn("P2_OWNER (codex)", summary)
        self.assertNotIn("P2_OWNER (chatgpt, codex)", summary)
        self.assertEqual(report["action"], "COMPLETE_OWNER_RULE_SNAPSHOT")

    def test_summary_skips_checklist_when_snapshot_rules_match(self):
        registry = self.registry()
        declaration = {"chatgpt": {"rules": {"P2_OWNER": "codex_sol_max"}},
                       "codex": {"rules": {"P2_OWNER": "codex_sol_max"}}}
        report = audit(registry, "latest", declaration)
        self.assertEqual(report["action"], "SNAPSHOT_RULES_MATCH_ACCOUNT_UNVERIFIED")
        self.assertNotIn("소유자 수동 점검 목록", to_markdown(report, registry))

    def test_summary_does_not_apply_stale_policy_checklist(self):
        registry = self.registry()
        report = audit(registry, "changed-policy")
        self.assertEqual(report["action"], "UPDATE_RULE_BASELINE_AND_REVIEW_INSTRUCTIONS")
        self.assertNotIn("소유자 수동 점검 목록", to_markdown(report, registry))

    def test_conflict_action_prioritized_over_missing_snapshot(self):
        registry = self.registry()
        declaration = {"chatgpt": {"rules": {"P2_OWNER": "legacy_owner"}}}
        report = audit(registry, "latest", declaration)
        self.assertEqual(report["action"], "REVIEW_DECLARED_CONFLICTS")
        self.assertNotIn("legacy_owner", to_markdown(report, registry))

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
