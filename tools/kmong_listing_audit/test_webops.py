"""Adversarial mutations for draft WebOps intake and commercial guardrails."""
import copy
import json
import unittest

from validate import CATALOG, IntegrityError
from webops import INTAKE, validate_webops


class WebOpsIntakeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
        cls.intake = json.loads(INTAKE.read_text(encoding="utf-8"))

    def reject(self, change):
        catalog, intake = copy.deepcopy(self.catalog), copy.deepcopy(self.intake)
        change(catalog, intake)
        with self.assertRaises(IntegrityError):
            validate_webops(catalog, intake)

    def test_current_19_services_two_extensions_one_candidate_are_drafts(self):
        result = validate_webops(self.catalog, self.intake)
        self.assertEqual(result, {"extensions": 2, "candidates": 1,
                                  "existing_listings": 19, "published_from_intake": 0})

    def test_candidate_not_promoted_to_an_existing_sku(self):
        self.reject(lambda c, i: i["new_candidates"][0].update(
            candidate_id="KMONG-SVC-20"))

    def test_duplicate_extension_does_not_pass_set_check(self):
        self.reject(lambda c, i: i["extensions"][1].update(service_id="KMONG-SVC-14"))

    def test_extension_sellable_flag_rejected(self):
        self.reject(lambda c, i: i["extensions"][0].update(commercial_ready=True))

    def test_extension_listing_status_published_rejected(self):
        self.reject(lambda c, i: i["extensions"][0].update(listing_status="등록완료"))

    def test_candidate_published_without_authorization_rejected(self):
        self.reject(lambda c, i: i["new_candidates"][0].update(
            listing_status="등록완료", release_hold=False))

    def test_candidate_fake_url_rejected(self):
        self.reject(lambda c, i: i["new_candidates"][0].update(
            kmong_listing_url="https://kmong.com/gig/fake"))

    def test_candidate_history_cannot_be_fabricated(self):
        self.reject(lambda c, i: i["new_candidates"][0].update(
            listing_history=[{"event": "등록완료", "evidence": "claim"}]))

    def test_bundle_cannot_become_new_sku(self):
        self.reject(lambda c, i: i["bundle"].update(status="REGISTERED"))

    def test_bundle_missing_component_rejected(self):
        self.reject(lambda c, i: i["bundle"]["components"].pop())

    def test_catalog_reference_must_match_incubation_registry(self):
        self.reject(lambda c, i: c["trending_product_intake_20261115"].update(
            new_candidate_id="KMONG-CAND-UNKNOWN"))

    def test_catalog_publish_authorization_not_implicit(self):
        self.reject(lambda c, i: c["trending_product_intake_20261115"].update(
            publish_authorized=True))

    def test_external_license_evidence_cannot_be_invented(self):
        self.reject(lambda c, i: i.update(
            third_party_license_text_verified_in_this_run=True))

    def test_registered_count_drift_rejected(self):
        self.reject(lambda c, i: i.update(kmong_registered_count_change=1))

    def test_services_are_not_silently_appended(self):
        self.reject(lambda c, i: c["ranked_services"].append(
            {"service_id": "KMONG-SVC-20"}))

    def test_development_status_cannot_be_auto_approved(self):
        self.reject(lambda c, i: i["new_candidates"][0].update(
            development_status="PRODUCTION_READY"))


if __name__ == "__main__":
    unittest.main()
