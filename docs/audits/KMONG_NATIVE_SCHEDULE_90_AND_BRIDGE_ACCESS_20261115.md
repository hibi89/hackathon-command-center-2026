# Central schedule recurrence verified; Vercel bridge access discrepancy

**Date:** 2026-11-15 KST
**Marker:** KMONG_SCHEDULE_90_VERCEL_BRIDGE_ACCESS_20261115
**Repo:** `hibi89/hackathon-command-center-2026`
**Scope:** Read-only GitHub Actions/jobs/logs/ledger, Vercel account/team/project/alias/deployment/events, email deployment notice, and source structure. No Production POST, permissions, secrets, cron, deployments, official scores, or runtime source modified.

## Fixed score: 85 -> 90/100 (provisional central technical verification only)

| Acceptance evidence | Earlier schedule | Second independent schedule |
|---|---|---|
| Workflow ID | 416801860 | 416801860 |
| Run ID | 43590721340 | 43625442971 |
| event | `schedule` | `schedule` |
| Created UTC | 2026-11-14 11:35:04 | 2026-11-14 18:14:06 |
| KST | Nov 14 20:35 | Nov 15 03:14 |
| HEAD | `69e584e57a3a37fa72b406d62ccddf9eef9dfcf2` | same |
| Job | SUCCESS | SUCCESS |
| Python unittest | 80 PASS / 0 FAIL | 80 PASS / 0 FAIL |
| Collector log | UPDATED | UPDATED |
| Observed counts | 35 repos, 80 refs, 29 records | 35 repos, 80 refs, 29 records |
| Missing refs / fingerprint | 0 / 0 | 0 / 0 |
| Official scores | UNMODIFIED | UNMODIFIED |

Second job: `132540111098`, first job `132434645723`. Latest operating JSON remote blob `910252a355b13352076e2c73fe8c2d4ed5e6f829`, summary 35 repositories / 80 tracked branches / 29 links, 0 missing links and 0 fingerprint alerts, `no_official_score_authorization=true`, `provisional_official_certifications=0`. Each job's scanning step ran (not DEFERRED). A subsequent ledger update may change the blob; do not infer that the latest blob is the exact immediate post-run blob. GitHub's `23 * * * *` schedule was delayed; two real runs satisfy the fixed 5-point repeat gate, not a guaranteed hourly SLA.

**Scoring:** scheduling 25/25, collection 20/20, ledger 20/20, SHA/CI 10/10, authority 10/10, public GET runtime parity 5/5, **signed webhook live E2E 0/10**; **central 90/100**. This never changes product official completion.

## Signed webhook E2E still blocked by ownership/API access

Production known from prior authenticated Runner GET (not repeated this turn): `https://kmong-hub-event-bridge.vercel.app/api/webhook` HTTP 200, old source SHA `2863165b06d407ba632f18ad7a85a7c98f1989af`; isolated hardened branch `feature/kmong-webhook-bounded-ingress-20261114@9e7e756bd9f4f8dabd517bf327c1488961f3d7a9` is CI 121/121 PASS but NOT deployed.

**New read-only provenance:** Vercel authenticated user `godls5898-7447`, team slug `hibi89`, team ID `team_oDTHTX6ht90nzgUWxnpzZxhU`. Team activity events show the bridge project's ID `prj_veZOkRkhMEMEA6h7PiEIl3IKcthn`, same GitHub repo, and branch preview events (e.g. `dpl_G4Lu49LCc8kuan4kxxfeJV6MhYH2`, `kmong-productization@6377c923...`). Recent preview events ended `CANCELED / EARLY_IGNORE_STEP`; do NOT mistake these for Production outcomes. A Nov 13 Vercel notification links to a failed preview and reports `Root Directory "services/kmong-event-bridge" does not exist` on operating branch. GitHub confirms the bridge directory exists on `main` but **not** on `kmong-productization`. Do not copy runtime source into the operating branch merely to suppress preview notices.

**Access inconsistency:** Vercel `list_projects` under connected team and default context shows only unrelated `project08-executive`; `get_project` by verified bridge ID or name returns 404, `get_deployment` by recent event ID returns 404, and alias lookup shows no matching alias. Thus bridge provenance is now located in Vercel event history, but active project management, actual deployment details and live request logs are **inaccessible / NOT_VERIFIED**, not proven deleted or broken. Do not repeat identical denied requests. Confirm dashboard team grant/current project visibility through explicit owner authorization; do not create a replacement or reuse `project08-executive`.

## Next authorized evidence gate

1. Owner verifies the existing `https://vercel.com/hibi89/kmong-hub-event-bridge` project page and team/project grant, or explicitly approves reauthorization of the connected Vercel team. Read access only initially.
2. With actual project access, read current Production deployment SHA, required configuration presence without exposing values, and sanitized function logs. Keep current Production unchanged until rollout approval.
3. Inspect source GitHub App's **Recent Deliveries** with owner-authorized UI: actual GitHub signed Ping 200, invalid-signature 401, non-allowlisted repo/branch 202 ignored, actual eligible push 202 queued, new central `workflow_dispatch` SUCCESS, collector UPDATED/NO_CHANGE and exact ledger readback. Do not claim synthetic HMAC requests are real delivery evidence.
4. Separately seek explicit approval before hardened-branch merge, Vercel deployment, GitHub App settings/secret changes, or introducing durable queue/lock. Existing 121 PASS CI is sufficient for code readiness; do not rerun without a code delta.

**Stop / pivot:** two different read-only access methods (team project list/name, and verified project/deployment IDs) return 404 even though event history exists. Further same-credential retries cannot establish ownership. Recommended A: reauthorize existing team (free/minimal, requires owner consent); B: owner dashboard inspection (free/manual); C: new project/queue (changes configuration/cost/security and is NOT approved).
