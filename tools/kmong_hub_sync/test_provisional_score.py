"""Provisional evidence readiness: safeguards against invented final percentages."""
import copy
from pathlib import Path
import unittest
from urllib.parse import parse_qs, urlsplit

from provisional_score import (WEIGHTS, _run, load_manifest, markdown_scores,
                               score_snapshot, _safe_artifact)

class Stub:
    def __init__(self, rows, bad_run=False, no_source=False):
        self.pins = {e["ci"]["run_id"]: e["ci"] for e in rows.values() if e["ci"]}
        self.bad_run=bad_run
        self.no_source=no_source
    def head(self, repo, branch, missing_ok=False):
        return {"sha":"a"*40, "status":"PRESENT"}
    def api_get(self, path, allow_404=False):
        if "/contents/" in path:
            if self.no_source and path.endswith("blueprint_score.py?ref=feature%2Ffinal-blueprint-p85-evidence-20261113"):
                return None
            return {"type":"file", "sha":"b"*40}
        for runid,pin in self.pins.items():
            if f"/actions/runs/{runid}/jobs?" in path:
                return {"total_count":2,"jobs":[
                    {"name":"tests ubuntu-latest","conclusion":"success"},
                    {"name":"tests windows-latest","conclusion":"success"}]}
            if path.endswith(f"/actions/runs/{runid}"):
                return {"id":runid,"status":"completed","conclusion":"failure" if self.bad_run else "success",
                        "head_sha":pin["head_sha"],"head_branch":pin["branch"]}
        return None


def fixture():
    from provisional_score import ROSTER
    import json
    entries=load_manifest({x["source"]["repo"].lower() for x in json.loads(ROSTER.read_text())["records"]
                            if x["source"]} | {"hibi89/freelancer","hibi89/hae",
                                               "hibi89/hibi89-paypal-ai-hackathon","hibi89/hibi89-ugreen-nas-hackathon"})
    products=[]
    observations=[]
    for id,rec in entries.items():
        index_repo=rec["source"]["repo"] if rec.get("source") else "hibi89/hibi89-ugreen-nas-hackathon"
        index_ref=rec["source"]["branch"] if rec.get("source") else "lead/ugreen"
        products.append({"record_id":id,"repository":index_repo,"tracked_branch":index_ref,
                         "product":id,"official_final_completion":"UNASSESSED"})
        observations.append({"record_id":id,"repository":index_repo,"tracked_branch":index_ref,
                             "head_sha":"a"*40,"status":"PRESENT",
                             "worker_report":{"percent":95}})
    snapshot={"no_official_score_authorization":True,"summary":{},"products":observations}
    return entries,products,snapshot


class EvidenceScoreTests(unittest.TestCase):
    def test_weights_exact_100(self):
        self.assertEqual(sum(WEIGHTS.values()),100)
    def test_roster_has_all_29(self):
        entries,_,_=fixture()
        self.assertEqual(len(entries),29)
        self.assertIn("ACTIVE-05",entries)
        self.assertIn("CANDIDATE-12",entries)
    def test_reject_unapproved_repo(self):
        with self.assertRaises(ValueError):
            _safe_artifact({"repo":"outsider/source","branch":"main","path":"x.py"},{"hibi89/hae"})
    def test_reject_path_escape(self):
        with self.assertRaises(ValueError):
            _safe_artifact({"repo":"hibi89/HAE","branch":"main","path":"../secrets"},{"hibi89/hae"})
    def test_reject_missing_29(self):
        entries,products,snapshot=fixture()
        with self.assertRaises(ValueError):
            score_snapshot(snapshot,Stub(entries),{e["source"]["repo"] for e in entries.values() if e.get("source")},{"records":products[:-1]})
    def test_score_all_29_without_official_mutation(self):
        entries,products,snapshot=fixture()
        allowed={e["source"]["repo"] for e in entries.values() if e.get("source")} | {"hibi89/Freelancer","hibi89/HAE"}
        ret=score_snapshot(snapshot,Stub(entries),allowed,{"records":products})
        self.assertEqual(ret["summary"]["provisional_evidence_scores"],29)
        self.assertTrue(all(isinstance(x["provisional_evidence_readiness"]["score"],int) for x in ret["products"]))
        self.assertEqual(ret["products"][4]["provisional_evidence_readiness"]["score"],90)
        self.assertEqual(ret["products"][0]["worker_report"]["percent"],95)
        self.assertEqual(products[4]["official_final_completion"],"UNASSESSED")
        self.assertIn("GITHUB_EVIDENCE_READINESS_V1",ret["provisional_score_policy"])
        self.assertIn("ACTIVE-05",markdown_scores(ret,{"records":products}))
    def test_failure_run_never_grants_ci(self):
        entries,products,snapshot=fixture()
        ret=score_snapshot(snapshot,Stub(entries,bad_run=True),{e["source"]["repo"] for e in entries.values() if e.get("source")} | {"hibi89/Freelancer"}, {"records":products})
        points=ret["products"][4]["provisional_evidence_readiness"]["points"]
        for key in ("successful_pinned_functional_ci","linux_and_windows_jobs","documented_ci_packaging","documented_ci_negative_tests"):
            self.assertEqual(points[key],0)
    def test_missing_implementation_blocks_ci_grant(self):
        entries,products,snapshot=fixture()
        ret=score_snapshot(snapshot,Stub(entries,no_source=True),{e["source"]["repo"] for e in entries.values() if e.get("source")} | {"hibi89/Freelancer"}, {"records":products})
        pts=ret["products"][4]["provisional_evidence_readiness"]["points"]
        self.assertEqual(pts["implementation_file"],0)
        self.assertEqual(pts["successful_pinned_functional_ci"],0)
    def test_buyer_rights_always_zero(self):
        entries,products,snapshot=fixture()
        ret=score_snapshot(snapshot,Stub(entries),{e["source"]["repo"] for e in entries.values() if e.get("source")} | {"hibi89/Freelancer"}, {"records":products})
        for row in ret["products"]:
            points=row["provisional_evidence_readiness"]["points"]
            self.assertEqual(points["physical_buyer_os_acceptance"],0)
            self.assertEqual(points["rights_and_owner_sale_go"],0)
    def test_bad_manifest_claim_fails_closed(self):
        entries,_,_=fixture()
        from provisional_score import ROSTER
        raw=ROSTER.read_text()
        import tempfile, json
        data=json.loads(raw)
        data["records"][0]["real_buyer_acceptance"]=True
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/"bad.json"
            path.write_text(json.dumps(data))
            allowed={e["source"]["repo"].lower() for e in entries.values() if e.get("source")} | {"hibi89/freelancer"}
            with self.assertRaises(ValueError):
                load_manifest(allowed,path)
    def test_old_historical_ci_marks_risk(self):
        entries,products,snapshot=fixture()
        ret=score_snapshot(snapshot,Stub(entries),{e["source"]["repo"] for e in entries.values() if e.get("source")} | {"hibi89/Freelancer"}, {"records":products})
        self.assertTrue(ret["products"][0]["provisional_evidence_readiness"]["risk"])
    def test_score_does_not_mutate_snapshot_official_flag(self):
        entries,products,snapshot=fixture()
        snapshot["no_official_score_authorization"]=False
        with self.assertRaises(ValueError):
            score_snapshot(snapshot,Stub(entries),{e["source"]["repo"] for e in entries.values() if e.get("source")} | {"hibi89/Freelancer"}, {"records":products})

if __name__ == "__main__":
    unittest.main()
