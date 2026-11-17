"""Regression tests for safe STATUS/HANDOFF/AGENTS content insertion."""
import unittest
from compose import insert_after_mission_lock, HEADER
from check import MARKER, NEXT, MissionLockError


class ComposeTests(unittest.TestCase):
    def test_insert_below_exact_two_protected_lines(self):
        original = HEADER + "## Prior status\n"
        candidate = insert_after_mission_lock(original, "## New actual evidence\nDetails")
        self.assertEqual(candidate.splitlines()[:2], [MARKER, NEXT])
        self.assertIn("## New actual evidence\nDetails\n## Prior status", candidate)

    def test_repeated_same_addendum_is_noop(self):
        original = HEADER + "## Previous\n"
        once = insert_after_mission_lock(original, "## New\nDetails")
        self.assertEqual(insert_after_mission_lock(once, "## New\nDetails"), once)

    def test_reject_existing_invalid_header(self):
        with self.assertRaises(MissionLockError):
            insert_after_mission_lock("## note\n" + HEADER, "## new")

    def test_reject_empty_addendum(self):
        for invalid in ("", "\n", "  \n"):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                insert_after_mission_lock(HEADER + "## Previous\n", invalid)

    def test_reject_mission_header_in_addendum(self):
        with self.assertRaises(ValueError):
            insert_after_mission_lock(HEADER + "## Previous\n", MARKER)

    def test_reject_large_addendum(self):
        with self.assertRaises(ValueError):
            insert_after_mission_lock(HEADER + "## Previous\n", "x" * 16001)


if __name__ == "__main__":
    unittest.main()
