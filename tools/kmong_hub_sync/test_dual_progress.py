"""Dual-report security and score integrity tests: no network or user data."""
import base64
import copy
import json
import unittest
from dual_progress import APPROVED, attach_dual_progress, replay_pinned_scorecard, worker_baseline, markdown_summary

P = APPROVED["ACTIVE-05"]
def good_card():
    return {
        "contract": P["contract"], "denominator": 100,
        "weights_status": "OWNER_DELEGATED_APPROVED",
        "owner_approval_scope": "SCORING_SCALE_AND_FIXED_R01_R33_WEIGHTS_ONLY_NOT_RELEASE",
        "original_blueprint_scope": "R01-R33_ALL_INCLUDED_NO_OMISSIONS",
        "final_completion_method": "SUM_ONLY_VERIFIED_FULL_REQUIREMENT_WEIGHTS_NO_PARTIAL_WITHOUT_PREAPPROVED_RULE",
        "release_status": "RELEASE_HOLD_SALE_NO_GO",
        "evidence_baseline": {"code_sha": P["source_sha"], "github_actions_run": P["run_id"]},
        "item_count": 33,
        "items": [{"id": f"R{i:02d}", "weight": 4 if i <= 1 else 3 if i <= 3 else 2 if i <= 30 else 1,
                   "state": "PENDING", "source_code_sha": None} for i in range(1, 34)],
    }

def corrected_card():
    card = good_card()
    # Exactly 100 fixed test weights; a new synthetic rubric does not imply 72 or approval.
    card["items"] = [{"id": f"R{i:02d}", "weight": 4 if i <= 1 else 3,
                       "state": "VERIFIED" if i <= 20 else "PENDING",
                       "source_code_sha": P["source_sha"] if i <= 20 else None} for i in range(1, 34)]
    # 4 + 32*3 = 100. Verified first20 = 4 + 19*3 = 61.
    return card

def good_run():
    return {"id": P["run_id"], "head_sha": P["source_sha"], "head_branch": P["branch"],
            "status": "completed", "conclusion": "success"}

class Fake:
    def __init__(self, card=None, run=None, bad_blob=False):
        self.card=card or corrected_card(); self.run=run or good_run(); self.bad_blob=bad_blob
    def api_get(self, path, allow_404=False):
        if "/contents/" in path:
            return {"sha": "f"*40 if self.bad_blob else P["blob"],"type":"file",
                    "encoding":"base64", "content":base64.b64encode(json.dumps(self.card).encode()).decode()}
        return self.run

class DualTests(unittest.TestCase):
    def test_worker_baseline_is_explicit_historical_not_official(self):
        b=worker_baseline()
        self.assertEqual(len(b["reported"]),16)
        self.assertNotIn("ACTIVE-05",b["reported"])
    def test_valid_scorecard_replays_only_approved_scope(self):
        s=replay_pinned_scorecard(corrected_card(), good_run(), P)
        self.assertEqual(s["percent"],61)
        self.assertFalse(s["release_authorized"])
    def test_forged_bigger_weight_rejected(self):
        c=corrected_card();c["items"][0]["weight"]=50
        with self.assertRaises(ValueError):replay_pinned_scorecard(c,good_run(),P)
    def test_duplicate_requirement_rejected(self):
        c=corrected_card();c["items"][1]["id"]="R01"
        with self.assertRaises(ValueError):replay_pinned_scorecard(c,good_run(),P)
    def test_stale_ci_run_rejected(self):
        r=good_run();r["head_sha"]="e"*40
        with self.assertRaises(ValueError):replay_pinned_scorecard(corrected_card(),r,P)
    def test_incomplete_ci_rejected(self):
        r=good_run();r["conclusion"]="failure"
        with self.assertRaises(ValueError):replay_pinned_scorecard(corrected_card(),r,P)
    def test_unapproved_sale_go_rejected(self):
        c=corrected_card();c["release_status"]="RELEASE_GO"
        with self.assertRaises(ValueError):replay_pinned_scorecard(c,good_run(),P)
    def test_pending_source_claim_rejected(self):
        c=corrected_card();c["items"][-1]["source_code_sha"]=P["source_sha"]
        with self.assertRaises(ValueError):replay_pinned_scorecard(c,good_run(),P)
    def test_worker_score_does_not_become_auto_score(self):
        s={"no_official_score_authorization":True,"summary":{},
            "products":[{"record_id":f"ACTIVE-{i:02d}" if i<=17 else f"CANDIDATE-{i-17:02d}",
                         "repository":P["repository"] if i==5 else "hibi89/else",
                         "tracked_branch":P["branch"] if i==5 else "main",
                         "status":"PRESENT"} for i in range(1,30)]}
        d=attach_dual_progress(s,Fake())
        self.assertEqual(d["summary"]["pinned_rubrics_replayed"],1)
        self.assertEqual(d["summary"]["historical_worker_reports"],16)
        self.assertEqual(d["products"][0]["worker_report"]["percent"],95)
        self.assertIsNone(d["products"][0]["machine_evidence_score"]["percent"])
        self.assertEqual(d["products"][4]["machine_evidence_score"]["percent"],61)
        self.assertIn("ACTIVE-01",markdown_summary(d))
    def test_scorecard_blob_drift_fails_closed(self):
        s={"no_official_score_authorization":True,"summary":{},
            "products":[{"record_id":f"ACTIVE-{i:02d}" if i<=17 else f"CANDIDATE-{i-17:02d}",
                         "repository":P["repository"] if i==5 else "hibi89/else",
                         "tracked_branch":P["branch"] if i==5 else "main",
                         "status":"PRESENT"} for i in range(1,30)]}
        d=attach_dual_progress(s,Fake(bad_blob=True))
        self.assertEqual(d["summary"]["pinned_rubrics_replayed"],0)
        self.assertIsNone(d["products"][4]["machine_evidence_score"]["percent"])
        self.assertEqual(d["products"][4]["machine_evidence_score"]["status"],"UNASSESSED")
if __name__=="__main__":
    unittest.main()
