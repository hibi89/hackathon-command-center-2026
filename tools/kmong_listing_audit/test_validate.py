"""Mutation and fixture tests for the independent 29→19 commercial SKU gate."""
import copy
import json
from pathlib import Path
import unittest
from validate import CATALOG, INDEX, IntegrityError, validate


class ListingGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
        cls.index = json.loads(INDEX.read_text(encoding="utf-8"))

    def check_reject(self, change):
        catalog, index = copy.deepcopy(self.catalog), copy.deepcopy(self.index)
        change(catalog, index)
        with self.assertRaises(IntegrityError):
            validate(catalog, index)

    def test_actual_29_sources_map_exactly_once_to_19_listings_and_internal(self):
        rows = validate(self.catalog, self.index)
        self.assertEqual(len(rows), 29)
        self.assertEqual(len(set(r["record_id"] for r in rows)), 29)
        self.assertEqual(len(set(r["service_id"] for r in rows if r["service_id"])), 19)
        self.assertEqual(sum(r["service_id"] is None for r in rows), 1)

    def test_factory_ax_alias_is_explicit_not_an_orphan(self):
        row = next(r for r in validate(self.catalog, self.index)
                   if r["record_id"] == "CANDIDATE-04")
        self.assertEqual((row["product"], row["catalog_source"], row["service_id"]),
                         ("Factory AX 전체", "Factory AX", "KMONG-SVC-19"))

    def test_internal_cube_cannot_be_registered_as_sku(self):
        row = next(r for r in validate(self.catalog, self.index)
                   if r["record_id"] == "ACTIVE-17")
        self.assertIsNone(row["service_id"])
        self.assertEqual(row["product"], "AXMART³ CUBE")

    def test_duplicate_listing_source_rejected(self):
        self.check_reject(lambda c, i: c["ranked_services"][1]["source_products"].append(
            "DATA2WEB Studio"))

    def test_missing_source_record_rejected(self):
        self.check_reject(lambda c, i: i["records"].pop())

    def test_duplicate_or_changed_service_id_rejected(self):
        self.check_reject(lambda c, i: c["ranked_services"][2].update(
            service_id="KMONG-SVC-02"))

    def test_unapproved_alias_or_product_rename_rejected(self):
        self.check_reject(lambda c, i: i["records"][20].update(
            product="Factory AX unknown"))

    def test_registered_without_url_date_and_history_rejected(self):
        self.check_reject(lambda c, i: c["ranked_services"][0].update(
            listing_status="등록완료"))

    def test_unregistered_fake_url_rejected(self):
        self.check_reject(lambda c, i: c["ranked_services"][0].update(
            kmong_listing_url="https://kmong.com/fake"))

    def test_removed_history_policy_rejected(self):
        self.check_reject(lambda c, i: c["listing_lifecycle"].update(
            evidence_required_for_registered=False))

    def test_source_summary_mismatch_rejected(self):
        self.check_reject(lambda c, i: i["summary"].update(official_unassessed=27))

    def test_past_registration_remains_counted_when_listing_is_stopped(self):
        c = copy.deepcopy(self.catalog)
        c["ranked_services"][0].update(
            listing_status="판매중지",
            kmong_listing_url=None,
            published_at_kst=None,
            listing_history=[{"status": "등록완료", "evidence": "verified archive"},
                             {"status": "판매중지", "evidence": "owner decision"}],
        )
        c["listing_lifecycle"]["verified_registered_count"] = 1
        self.assertEqual(len(validate(c, self.index)), 29)

    def test_past_registration_cannot_disappear_from_registered_count(self):
        def change(c, i):
            c["ranked_services"][0].update(
                listing_status="판매중지",
                listing_history=[{"event": "등록완료", "evidence": "archive"}],
            )
            # Illegal: old count remains zero after an actual previous registration.
        self.check_reject(change)

    def test_future_real_listing_with_evidence_is_accepted(self):
        c = copy.deepcopy(self.catalog)
        c["ranked_services"][0].update(
            listing_status="등록완료",
            kmong_listing_url="https://kmong.com/gig/evidence",
            published_at_kst="2026-11-14",
            listing_history=[{"event": "등록완료", "evidence": "owner-verified"}],
        )
        c["listing_lifecycle"]["verified_registered_count"] = 1
        self.assertEqual(len(validate(c, self.index)), 29)


if __name__ == "__main__":
    unittest.main()
