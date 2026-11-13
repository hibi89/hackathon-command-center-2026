import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from verify import audit
from canonical_scope import inspect_canonical, REQUIRED_REPOS

class GateTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "docs").mkdir()
        self.bp = self.root / "REQUIREMENTS.md"
        self.bp.write_text("FINAL BLUEPRINT\n", encoding="utf-8")

    def payload(self):
        return {
            "schema_version": 1,
            "product": "Example",
            "blueprint": {
                "path": "REQUIREMENTS.md",
                "sha256": hashlib.sha256(self.bp.read_bytes()).hexdigest(),
                "owner_approval_reference": "owner-approved-example"},
            "requirements": [{"id": "R-01", "weight": 100, "status": "UNVERIFIED", "evidence": []}],
            "official_final_completion": "UNASSESSED",
        }

    def save(self, data):
        (self.root / "docs/final_blueprint_evidence.json").write_text(json.dumps(data), encoding="utf-8")

    def test_no_manifest_is_unassessed_not_certified(self):
        data, ok = audit(self.root, "hibi89/demo")
        self.assertTrue(ok)
        self.assertEqual(data["gate"], "UNASSESSED")
        self.assertEqual(data["official_final_completion"], "UNASSESSED")

    def test_valid_rubric_never_claims_certification(self):
        self.save(self.payload())
        data, ok = audit(self.root, "hibi89/demo")
        self.assertTrue(ok)
        self.assertEqual(data["gate"], "EVIDENCE_FORMAT_OK")
        self.assertEqual(data["official_final_completion"], "UNASSESSED")

    def test_numeric_claim_fails(self):
        p = self.payload()
        p["official_final_completion"] = 85
        self.save(p)
        data, ok = audit(self.root, "hibi89/demo")
        self.assertFalse(ok)
        self.assertIn("numeric official score", "\n".join(data["errors"]))

    def test_changed_blueprint_fails(self):
        p = self.payload()
        self.bp.write_text("UNAPPROVED CHANGE\n", encoding="utf-8")
        self.save(p)
        data, ok = audit(self.root, "hibi89/demo")
        self.assertFalse(ok)
        self.assertIn("mismatch", "\n".join(data["errors"]))

    def test_reduced_scope_fails_weight_check(self):
        p = self.payload()
        p["requirements"][0]["weight"] = 85
        self.save(p)
        data, ok = audit(self.root, "hibi89/demo")
        self.assertFalse(ok)
        self.assertIn("100", "\n".join(data["errors"]))

    def test_fake_cross_repository_evidence_fails(self):
        p = self.payload()
        p["requirements"][0].update({"status":"VERIFIED","evidence":[{
            "source_sha":"a"*40,
            "test_id":"fake-test",
            "ci_run_url":"https://github.com/other/private/actions/runs/1"}]})
        self.save(p)
        data, ok = audit(self.root, "hibi89/demo")
        self.assertFalse(ok)
        self.assertIn("VERIFIED requires", "\n".join(data["errors"]))


    def test_bool_schema_version_rejected(self):
        p = self.payload()
        p["schema_version"] = True
        self.save(p)
        data, ok = audit(self.root, "hibi89/demo")
        self.assertFalse(ok)
        self.assertIn("schema_version", "\n".join(data["errors"]))

    def test_unhashable_status_returns_structured_error(self):
        p = self.payload()
        p["requirements"][0]["status"] = []
        self.save(p)
        data, ok = audit(self.root, "hibi89/demo")
        self.assertFalse(ok)
        self.assertIn("status invalid", "\n".join(data["errors"]))

    def test_partial_claim_requires_actual_proof_reference(self):
        p = self.payload()
        p["requirements"][0]["status"] = "PARTIAL"
        self.save(p)
        data, ok = audit(self.root, "hibi89/demo")
        self.assertFalse(ok)
        self.assertIn("PARTIAL requires", "\n".join(data["errors"]))

    def test_unverified_malformed_proof_rejected(self):
        p = self.payload()
        p["requirements"][0]["evidence"] = [{"source_sha": "b" * 40, "test_id": "t", "ci_run_url": "https://invalid.example/runs/1"}]
        self.save(p)
        data, ok = audit(self.root, "hibi89/demo")
        self.assertFalse(ok)
        self.assertIn("invalid same-repo proof", "\n".join(data["errors"]))


class CanonicalScopeTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / "caller"
        self.root.mkdir()
        (self.root / "docs").mkdir()
        self.main = Path(self.tmp.name) / "main"
        (self.main / "docs").mkdir(parents=True)
        self.original = b"OWNER-CANONICAL-HAE\n"
        (self.main / "docs/ECOSYSTEM_CANONICAL.md").write_bytes(self.original)
        self.pins = Path(self.tmp.name) / "pins.json"
        self.save_pin()

    def save_pin(self, pins=None):
        if pins is None:
            digest = hashlib.sha1(b"blob " + str(len(self.original)).encode() + b"\0" + self.original).hexdigest()
            pins = [{"repository":"hibi89/HAE", "ref":"main", "mode":"enforce",
                     "path":"docs/ECOSYSTEM_CANONICAL.md", "git_blob_sha":digest}]
        self.pins.write_text(json.dumps({"schema_version":1, "pins":pins}), encoding="utf-8")

    def check(self):
        return audit(self.root, "hibi89/HAE", canonical_root=self.main, pins_path=self.pins)

    def test_matching_main_only_document_without_manifest_is_unassessed(self):
        data, ok = self.check()
        self.assertTrue(ok)
        self.assertEqual(data["gate"], "UNASSESSED")
        self.assertEqual(data["canonical_blueprint"]["status"], "MATCHED")
        self.assertEqual(data["official_final_completion"], "UNASSESSED")

    def test_changed_canonical_rejected_even_without_manifest(self):
        (self.main / "docs/ECOSYSTEM_CANONICAL.md").write_text("MODIFIED")
        data, ok = self.check()
        self.assertFalse(ok)
        self.assertEqual(data["gate"], "CANONICAL_SCOPE_INVALID")
        self.assertEqual(data["canonical_blueprint"]["status"], "DRIFT_DETECTED")

    def test_missing_main_checkout_rejected(self):
        data, ok = audit(self.root, "hibi89/HAE", pins_path=self.pins)
        self.assertFalse(ok)
        self.assertEqual(data["canonical_blueprint"]["status"], "CHECKOUT_MISSING")

    def test_missing_main_blueprint_rejected(self):
        (self.main / "docs/ECOSYSTEM_CANONICAL.md").unlink()
        data, ok = self.check()
        self.assertFalse(ok)
        self.assertEqual(data["canonical_blueprint"]["status"], "FILE_MISSING_OR_UNSAFE")

    def test_removed_pin_cannot_silently_disable_hae(self):
        self.save_pin([{"repository":"hibi89/demo","ref":"main","path":"README.md","git_blob_sha":"a"*40}])
        data, ok = self.check()
        self.assertFalse(ok)
        self.assertEqual(data["canonical_blueprint"]["status"], "PIN_MISSING_OR_DUPLICATE")

    def test_duplicate_repo_pin_rejected(self):
        p = json.loads(self.pins.read_text())["pins"][0]
        self.save_pin([p,p])
        data, ok = self.check()
        self.assertFalse(ok)
        self.assertIn("duplicated", " ".join(data["errors"]))

    def test_unpinned_repo_stays_unassessed_without_checkout(self):
        data, ok = audit(self.root, "hibi89/demo", pins_path=self.pins)
        self.assertTrue(ok)
        self.assertEqual(data["canonical_blueprint"]["status"], "NOT_CONFIGURED")
        self.assertEqual(data["gate"], "UNASSESSED")

    def test_altered_fingerprint_rejected(self):
        p = json.loads(self.pins.read_text())["pins"][0]
        p["git_blob_sha"] = "b"*40
        self.save_pin([p])
        data, ok = self.check()
        self.assertFalse(ok)
        self.assertEqual(data["canonical_blueprint"]["status"], "DRIFT_DETECTED")

    def test_manifest_cannot_bypass_canonical_drift(self):
        manifest = {"schema_version":1,"product":"HAE",
                    "official_final_completion":"UNASSESSED"}
        (self.root / "docs/final_blueprint_evidence.json").write_text(json.dumps(manifest))
        (self.main / "docs/ECOSYSTEM_CANONICAL.md").write_text("MODIFIED")
        data, ok = self.check()
        self.assertFalse(ok)
        self.assertEqual(data["gate"], "CANONICAL_SCOPE_INVALID")


class CentralPinRegistryTest(unittest.TestCase):
    def setUp(self):
        self.registry = json.loads((Path(__file__).with_name("canonical_pins.json")).read_text(encoding="utf-8"))
        self.pins = self.registry["pins"]

    def test_registered_repository_pins_are_unique(self):
        repo_names = [x["repository"].lower() for x in self.pins]
        self.assertEqual(len(repo_names), len(set(repo_names)))
        self.assertEqual(len(repo_names), 31)

    def test_enforced_repos_match_fail_closed_code_list(self):
        enforced = {x["repository"].lower() for x in self.pins if x["mode"] == "enforce"}
        self.assertEqual(enforced, REQUIRED_REPOS)
        self.assertEqual(len(enforced), 9)

    def test_unpinned_repos_separate_from_pins(self):
        pinned = {x["repository"].lower() for x in self.pins}
        missing = {x.lower() for x in self.registry["not_pinned_main"]}
        self.assertFalse(pinned & missing)
        self.assertEqual(len(missing), 4)

    def test_git_blob_fingerprint_and_main_paths_are_valid(self):
        from canonical_scope import SHA40
        for pin in self.pins:
            self.assertTrue(pin["ref"] == "main" or pin["ref"].startswith("feature/"))
            self.assertRegex(pin["git_blob_sha"], SHA40)
            self.assertTrue(pin["path"].endswith((".md", ".txt")))
            self.assertIn(pin["mode"], ("enforce", "observe"))

    def test_observe_mode_reports_drift_without_certifying_or_blocking(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "docs").mkdir()
            file = root / "docs/REQUIREMENTS.md"
            file.write_text("changed")
            pins = root / "pins.json"
            pins.write_text(json.dumps({"schema_version":1,"pins":[{"repository":"hibi89/demo",
               "ref":"main","path":"docs/REQUIREMENTS.md","git_blob_sha":"a"*40,"mode":"observe"}]}))
            state, errors = inspect_canonical("hibi89/demo", root, pins)
            self.assertEqual(state["status"], "DRIFT_REVIEW_REQUIRED")
            self.assertEqual(errors, [])

    def test_workflow_checkout_repos_match_registry(self):
        workflow = (Path(__file__).parents[2] / ".github/workflows/blueprint-validation.yml").read_text()
        for pin in self.pins:
            self.assertIn(pin["repository"], workflow)

if __name__ == "__main__":
    unittest.main()
