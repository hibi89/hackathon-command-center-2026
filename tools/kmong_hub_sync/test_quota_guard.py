"""Offline tests for the App primary budget and burst dispatch guard."""
import unittest
from pathlib import Path
from quota_guard import (
    BOT_ACTOR, CORE_RESERVE, GuardError, bot_is_first_eligible_run,
    core_budget, decide, utc_epoch,
)


def run(number, created, actor=BOT_ACTOR, conclusion=None):
    return {"id": number, "event": "workflow_dispatch",
            "actor": {"login": actor}, "created_at": created,
            "conclusion": conclusion}


class QuotaGuardTests(unittest.TestCase):
    def test_rate_budget_valid(self):
        self.assertEqual(core_budget({"resources": {"core": {"remaining": 500, "reset": 1795000000}}}), (500, 1795000000))

    def test_fail_closed_on_missing_budget(self):
        for payload in ({}, {"resources": {"core": {"remaining": "500", "reset": 1795000000}}},
                        {"resources": {"core": {"remaining": 500, "reset": None}}}):
            with self.subTest(payload=payload), self.assertRaises(GuardError):
                core_budget(payload)

    def test_primary_exhausted_deferred_before_bot_query(self):
        self.assertEqual(decide(0, "workflow_dispatch", BOT_ACTOR), "DEFERRED_PRIMARY_BUDGET")
        self.assertEqual(decide(CORE_RESERVE-1, "schedule", ""), "DEFERRED_PRIMARY_BUDGET")
        self.assertEqual(decide(CORE_RESERVE, "schedule", ""), "RUN")

    def test_owner_manual_dispatch_allowed_when_budget_is_safe(self):
        self.assertEqual(decide(800, "workflow_dispatch", "hibi89"), "RUN")

    def test_bot_first_run_in_fixed_bucket_allowed(self):
        payload = {"workflow_runs": [run(101, "2026-11-14T02:05:10Z"),
                                     run(100, "2026-11-14T01:59:59Z")]}
        self.assertTrue(bot_is_first_eligible_run(payload, 101))
        self.assertEqual(decide(800, "workflow_dispatch", BOT_ACTOR, 101, payload), "RUN")

    def test_bot_burst_second_run_deferred(self):
        payload = {"workflow_runs": [run(102, "2026-11-14T02:08:00Z"),
                                     run(101, "2026-11-14T02:05:10Z")]}
        self.assertFalse(bot_is_first_eligible_run(payload, 102))
        self.assertEqual(decide(800, "workflow_dispatch", BOT_ACTOR, 102, payload), "DEFERRED_BOT_BURST")

    def test_new_bucket_can_run(self):
        payload = {"workflow_runs": [run(103, "2026-11-14T02:30:00Z"),
                                     run(102, "2026-11-14T02:29:59Z")]}
        self.assertTrue(bot_is_first_eligible_run(payload, 103))

    def test_cancelled_prior_does_not_starve_new_run(self):
        payload = {"workflow_runs": [run(102, "2026-11-14T02:08:00Z"),
                                     run(101, "2026-11-14T02:05:10Z", conclusion="cancelled")]}
        self.assertTrue(bot_is_first_eligible_run(payload, 102))

    def test_untrusted_actor_not_used_as_bot_reference(self):
        payload = {"workflow_runs": [run(102, "2026-11-14T02:08:00Z"),
                                     run(101, "2026-11-14T02:05:10Z", actor="someone-else")]}
        self.assertTrue(bot_is_first_eligible_run(payload, 102))

    def test_missing_current_run_fails_closed(self):
        with self.assertRaises(GuardError):
            bot_is_first_eligible_run({"workflow_runs": [run(101, "2026-11-14T02:05:10Z")]}, 102)

    def test_invalid_timestamps_fail_closed(self):
        for x in ("2026-11-14T02:05:10", "not-time", None):
            with self.subTest(x=x), self.assertRaises(GuardError):
                utc_epoch(x)

    def test_malformed_rate_limit_does_not_claim_run(self):
        with self.assertRaises(GuardError):
            decide("800", "schedule", "")



class ScheduledRecoveryPolicyTests(unittest.TestCase):
    def test_hourly_default_branch_schedule_and_source_budget_gate(self):
        path = Path(__file__).resolve().parents[2] / ".github/workflows/kmong-hub-sync.yml"
        body = path.read_text(encoding="utf-8")
        self.assertIn("cron: '23 * * * *'", body)
        self.assertIn("vars.KMONG_SYNC_ENABLED == 'true'", body)
        self.assertIn("scan_gate.outputs.run_sync == 'true'", body)
        self.assertIn("KMONG_SYNC_DRY_RUN: ${{ inputs.dry_run }}", body)

    def test_source_read_app_and_hub_scopes_unchanged(self):
        path = Path(__file__).resolve().parents[2] / ".github/workflows/kmong-hub-sync.yml"
        body = path.read_text(encoding="utf-8")
        self.assertIn("permission-contents: read", body)
        self.assertIn("permission-actions: read", body)
        self.assertIn("KMONG_HUB_TOKEN: ${{ github.token }}", body)
        self.assertNotIn("pull_request_target:", body)


if __name__ == "__main__":
    unittest.main()
