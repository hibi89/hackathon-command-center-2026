"""Current-index safety: preserve historical state and 29-record acceptance."""
import copy
import unittest

from sync import INDEX_PATH, validate_current_index


def valid_index():
    records = [
        {"record_id": f"ACTIVE-{i:02d}", "official_final_completion": "UNASSESSED"}
        for i in range(1, 18)
    ] + [
        {"record_id": f"CANDIDATE-{i:02d}", "official_final_completion": "UNASSESSED"}
        for i in range(1, 13)
    ]
    records[4]["official_final_completion"] = "72%"
    records[-1].update({"repository": "hibi89/Freelancer",
                        "tracked_branch": "product/worknova-desk-local"})
    return {
        "derived_from": {
            "path": "data/final_blueprint_product_index_20261113.json",
            "preserved_original": True,
        },
        "summary": {"official_unassessed": 28, "official_certified": 0,
                    "official_partial_scored": 1},
        "records": records,
    }


class CurrentIndexTest(unittest.TestCase):
    def test_reads_only_new_current_index(self):
        self.assertEqual(INDEX_PATH, "data/final_blueprint_product_index_current.json")

    def test_correct_29_are_accepted_without_modification(self):
        index = valid_index()
        original = copy.deepcopy(index)
        self.assertIs(validate_current_index(index), index)
        self.assertEqual(index, original)

    def test_product_link_to_old_hackathon_rejected(self):
        index = valid_index()
        index["records"][-1]["repository"] = "hibi89/hibi89-paypal-ai-hackathon"
        with self.assertRaisesRegex(ValueError, "WORKNOVA"):
            validate_current_index(index)

    def test_wrong_official_count_rejected(self):
        index = valid_index()
        index["summary"]["official_unassessed"] = 29
        with self.assertRaisesRegex(ValueError, "summary"):
            validate_current_index(index)

    def test_baseline_lineage_is_mandatory(self):
        index = valid_index()
        index["derived_from"]["preserved_original"] = False
        with self.assertRaisesRegex(ValueError, "historical"):
            validate_current_index(index)

    def test_duplicate_product_is_rejected(self):
        index = valid_index()
        index["records"][0]["record_id"] = "ACTIVE-02"
        with self.assertRaisesRegex(ValueError, "duplicate"):
            validate_current_index(index)


if __name__ == "__main__":
    unittest.main()
