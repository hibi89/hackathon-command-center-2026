import base64
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from provision import ProvisionError, create_one, documents, main, validate
from from_push import get_new_request, eligible


def example():
    return {
        "schema_version": 1,
        "request_id": "req-evidence-auditor-abc-20261118",
        "owner": "hibi89",
        "names": ["REQ-Evidence-Auditor-A", "REQ-Evidence-Auditor-B", "REQ-Evidence-Auditor-C"],
        "project": "REQ Evidence Auditor", "visibility": "public",
        "approval": "owner-requested-create-and-bootstrap-only",
    }


POLICY_SHA = "f" * 40


class FakeClient:
    def __init__(self, existing=False, private=False):
        self.existing = existing
        self.private = private
        self.files = {}
        self.creation_payload = None

    def api(self, method, path, body=None):
        if method == "GET" and path == "/repos/hibi89/REQ-Evidence-Auditor-A":
            return (200, {"private": self.private, "default_branch": "main"}) if self.existing else (404, None)
        if method == "POST" and path == "/user/repos":
            self.creation_payload = body
            return 201, {"private": False, "default_branch": "main", "full_name": "hibi89/REQ-Evidence-Auditor-A"}
        if "/contents/" in path:
            filename = path.split("/contents/")[-1]
            if method == "GET":
                if filename in self.files:
                    return 200, {"content": base64.b64encode(self.files[filename].encode()).decode()}
                return 404, None
            if method == "PUT":
                self.files[filename] = base64.b64decode(body["content"]).decode()
                return 201, {}
        raise AssertionError(f"unmocked call {method} {path}")


class ProvisionerTest(unittest.TestCase):
    def test_valid_request_and_policy(self):
        r = validate(example())
        self.assertEqual(len(r["names"]), 3)
        files = documents(r, r["names"][0], POLICY_SHA)
        self.assertEqual(len(files), 5)
        self.assertIn("UNASSESSED", files["STATUS.md"])
        self.assertIn(POLICY_SHA, files["AGENTS.md"])\n        self.assertIn("PUBLIC", files["AGENTS.md"])\n        self.assertEqual(json.loads(files[".haechong-provisioner.json"])["visibility"], "public")

    def test_invalid_names_or_approval(self):
        cases = [("names", ["../escape"]), ("names", ["a", "A"]),
                 ("names", ["a", "b", "c", "d"]), ("names", []),
                 ("visibility", "private"), ("visibility", True), ("visibility", "Public"), ("owner", "attacker"),
                 ("approval", "no")]
        for key, val in cases:
            q = example()
            q[key] = val
            with self.subTest(key=key, val=val), self.assertRaises(ProvisionError):
                validate(q)

    def test_dry_run_no_api_calls(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "example.json"
            p.write_text(json.dumps(example()))
            with patch("urllib.request.urlopen", side_effect=AssertionError("network call")):
                self.assertEqual(main(["--request", str(p), "--policy-sha", POLICY_SHA]), 0)

    def test_execute_requires_gate(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "example.json"
            p.write_text(json.dumps(example()))
            with patch.dict(os.environ, {}, clear=True):
                self.assertEqual(main(["--request", str(p), "--policy-sha", POLICY_SHA,
                                       "--execute", "--confirm", example()["request_id"]]), 2)

    def test_create_public_five_documents(self):
        c = FakeClient()
        r = create_one(c, example(), example()["names"][0], POLICY_SHA)
        self.assertEqual(r["result"], "CREATED")
        self.assertIs(c.creation_payload["private"], False)
        self.assertEqual(len(c.files), 5)\n        self.assertEqual(r["visibility"], "public")

    def test_resume_only_with_exact_marker(self):
        c = FakeClient(existing=True)
        with self.assertRaises(ProvisionError):
            create_one(c, example(), example()["names"][0], POLICY_SHA)
        c.files[".haechong-provisioner.json"] = documents(example(), example()["names"][0], POLICY_SHA)[".haechong-provisioner.json"]
        c.files["AGENTS.md"] = "customer edits"
        result = create_one(c, example(), example()["names"][0], POLICY_SHA)
        self.assertEqual(result["result"], "RESUMED")
        self.assertEqual(c.files["AGENTS.md"], "customer edits")

    def test_existing_private_refused(self):
        with self.assertRaises(ProvisionError):
            create_one(FakeClient(existing=True, private=True), example(), example()["names"][0], POLICY_SHA)

    def test_private_request_rejected(self):\n        q = example()\n        q["visibility"] = "private"\n        with self.assertRaises(ProvisionError):\n            validate(q)\n\n    def test_push_owner_path_guard(self):
        self.assertFalse(eligible("requests/repo_provisioner/../../evil.json"))
        with self.assertRaises(ValueError):
            get_new_request("a" * 40, "b" * 40, "someone-else")


if __name__ == "__main__":
    unittest.main()
