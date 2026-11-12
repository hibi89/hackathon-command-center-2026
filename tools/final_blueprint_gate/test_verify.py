import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from verify import audit

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

if __name__ == "__main__":
    unittest.main()
