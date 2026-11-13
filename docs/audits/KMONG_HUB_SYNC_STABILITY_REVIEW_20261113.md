# Kmong hub event bridge — read-only stability verification (2026-11-13 KST)

> 2026-11-13 17:07 KST observation window. This is a code-and-GitHub-Actions audit; NOT a proof of future loss-free operation. No webhook, secret, Vercel, environment, GitHub App permission, product completion, or deployment setting was changed.

## Verified refs / non-destructive scope
- Repository: `hibi89/hackathon-command-center-2026`. Main base HEAD `e1ad0802cb7bdf783c1d99c6f0b259ec96daf015`. Kmong branch was observed advancing from the handoff `7f522e3e` to `b8cb3a7b` and later `1ac00954040697c541b5a5e28a3313e4074a2e59`; re-query before any kmong write.
- Read order: HANDOFF -> STATUS -> AGENTS -> REQUIREMENTS -> real `.github/workflows/kmong-hub-sync.yml`, `tools/kmong_hub_sync/sync.py`, `services/kmong-event-bridge/lib/receiver.js` and tests.
- Existing E2E read-only snapshot approach left intact; no new run was manually dispatched for this audit. Previously verified 35 repositories / 70 refs / 29 linked products; zero blocking fingerprint alerts. Official final-design scores, registration histories and work markers were not changed.

## P1 — CANCELLED explanation and observed burst
- [Run #43386827934](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43386827934): success, one successful job.
- [Run #43386834669](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43386834669) and [#43386854036](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43386854036): cancelled, **zero jobs**; cancelled before execution.
- [Run #43386858726](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43386858726): success, one successful job.
- The workflow uses a single `concurrency.group: kmong-hub-source-evidence` and `cancel-in-progress: false`. GitHub Actions permits only one running and one pending run in a concurrency group: a newer pending run replaces a previous pending run even with `cancel-in-progress: false`. This explains the zero-job cancellations, based on code and timing; per-delivery root-cause evidence from webhook logs was not retrieved.
- At audit query, the workflow had **35 workflow_dispatch** executions: **17 success / 18 cancelled**, and all listed executions belonged to the same sync workflow. This is expected pending-run coalescing under repeated pushes, not evidence that 18 data writes failed. However, each dispatch still consumes request/queue capacity, and there is no durable per-delivery replay/deduplication store.
- The current receiver explicitly excludes the generated `kmong-productization` snapshot push (indeed that branch is absent from central allowlist), so the reviewed code prevents that direct feedback loop. Other legitimate tracked branches and their completion workflows can produce bursts; exact source of every dispatch remains unverified.

## P2 — schedule
- Trusted main workflow cron: `10 2 * * *` (11:10 KST). GitHub Actions run query filtered by `event=schedule` returned **0** events. Cron was restored by main commit `98d353001f9ea8fd2b74dc1e7517a0fbdff5e64e` at 2026-11-13 14:35 KST, *after* the 11:10 slot.
- Earliest following daily slot: 2026-11-14 11:10 KST (subject to GitHub scheduler delays). Production schedule behavior is **UNVERIFIED**, not failed.
- Code tests cover scheduled write permission and absent-initial-snapshot fail-closed behavior, but unit tests do not establish real schedule execution.

## P3 — failure handling / consistency
- [Run #43390636084](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43390636084) succeeded after **26/26 Python unittest PASS**. Its log confirms `UPDATED`, 35 repos, 70 tracked refs, 29 products/29 present refs, fingerprint alerts 0, official scores UNMODIFIED, and snapshot commit `b57050d6a22c6d7df5ddfbf9f91b405fae6671c1`.
- Source App read token and hub write token are separate. Source App install repository set is checked exactly; inventory/pin/drift are fail-closed; transient GitHub 429/502/503/504/network failures get up to one retry; writes use prior blob SHA, readback equality, equal-content NO_CHANGE; scheduled events cannot initialize missing snapshot. No live fault injection performed; full recovery after prolonged outage, quota exhaustion or lost webhook is **UNVERIFIED**.
- Receiver validates HMAC and installation ID, limits body size, restricts repo/branch and workflow name, dispatches hub workflow only. It validates delivery UUID syntax but **does not maintain dedup/replay state**; authenticated replay could enqueue another request. Pre-existing owner-declined Webhook Secret rotation risk remains **OPEN**; do not print or rotate it without approval.
- GitHub Apps and Vercel Production status/URL were not independently revalidated; an earlier Vercel connector 404 is not classified as a Production outage. No Production deployment occurred.

## Stability options and decision
1. **Keep existing last-state coalescing + daily reconciliation (selected, no code change)**: zero new infra/cost, low maintenance, 26 tests and repeated successful jobs; tolerates pending cancellation for *latest-state observation*, but cannot ensure immediate update or full event history. Revisit after next actual cron.
2. **Add durable event-idempotency/queue plus retry/replay (design only, NOT approved)**: better per-delivery assurance and rate reduction but requires state store / extra infrastructure / privacy, secret and cost review, tests, and explicit owner approval. A no-state, in-memory serverless debounce is insufficient for durable de-duplication across instances.

## Kmong final-design scores and next steps
- Canonical [final-design baseline](https://github.com/hibi89/hackathon-command-center-2026/blob/kmong-productization/docs/audits/KMONG_FINAL_BLUEPRINT_BASELINE_20261113.md) retains 17 active + 12 candidate products, **29/29 official final-blueprint completion rates UNASSESSED** until accepted weighted requirement-to-code/SHA/E2E tracing. Historical engineering 85/95 milestones are **not** certified final-design rates.
- [19-service catalog](https://github.com/hibi89/hackathon-command-center-2026/blob/kmong-productization/docs/strategy/KMONG_29_TO_19_SERVICE_CATALOG_20261113.md) and linked 29-module service mapping, all [작업중]/[사용자 개입 필요]/RELEASE HOLD/등록완료 history remain untouched.
- Next: inspect `schedule` run after 2026-11-14 11:10 KST (including delayed/no-run result); compare its exact SHA and readback with the then-current hub and source refs; inspect webhook delivery/diagnostic logs only with approved access; assess dispatch burst rate and API quota before proposing a change. No forced extra workflow run, empty commit, Vercel redeploy or authority change.

## Ten-part handoff
1. Goal/scope/architecture: GitHub Source App -> Vercel webhook -> Dispatcher App -> central Actions -> read-only hub JSON; official final blueprint 100 is separate.
2. Done/decision: P1 pending-cancel cause strongly supported; P2 schedule unverified; P3 source code and real success log checked. Keep current coalescing, no code changes.
3. Tests: existing run #43390636084 26 PASS / 0 FAIL / 0 SKIP; no additional new test runs; latest successful snapshot verified from logs.
4. State: P1 investigated, P2 waiting for real cron, P3 partial verification, P4 final-blueprint product scoring pending.
5. Failure evidence/alternatives: zero-job pending cancellations; no durable replay; retry once and fail-closed; options above. Do not use unsafe production fault injection.
6. Repo/ref/SHA/paths: main base `e1ad0802cb7bdf783c1d99c6f0b259ec96daf015`; hub branch moving, confirm latest before writes; workflow/receiver/sync paths above.
7. Production/commands: webhook `https://kmong-hub-event-bridge.vercel.app/api/webhook` per previous handoff (not rechecked); `python3 -B -m unittest discover -s tools/kmong_hub_sync -p "test_*.py" -v`; node test `services/kmong-event-bridge/test/receiver.test.js` (new run not executed).
8. Original/backup/security: preserve Source/Dispatcher App split, production config, token/PEM/secret, source repos, central JSON and former SHA; do not expose secrets. Git history is the rollback reference.
9. Next/acceptance/approval: real cron success + data readback, bounded duplicate stress/capacity review, longer observation; durable queue requires separate approval.
10. Date/evidence: 2026-11-13 KST; GitHub remote run/job/log/commit/code results; historical run dates as in links; documentation-commit SHA must be checked after writing.
