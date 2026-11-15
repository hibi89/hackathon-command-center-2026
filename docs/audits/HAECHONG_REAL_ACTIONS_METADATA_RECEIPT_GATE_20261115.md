# HAECHONG — real GitHub Actions metadata contract and workflow identity hardening

**Verified 2026-11-15 17:11 KST** · `HAECHONG_PRIMARY_MISSION_LOCK_V1` · central GitHub App HMAC webhook → original Vercel → hub Actions → 35 repositories / 80 refs / 29 products.

## Confirmed live evidence (not signed-webhook proof)

Read-only GitHub Actions REST + exact job logs:
- [Dispatcher run #43678839627](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43678839627), 2026-11-15 04:55:29 UTC, `kmong-hub-dispatcher[bot]`, completed/success, `workflow_dispatch`, `KMONG PREFLIGHT: RUN`, Python 80 PASS, `KMONG HUB SYNC: UPDATED`, **35 repo / 80 branches / 29 products, 0 missing, 0 fingerprint alerts, official scores UNMODIFIED**.
- [Dispatcher run #43679174366](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43679174366), 2026-11-15 05:00:28 UTC, same actor and event, completed/success, `KMONG PREFLIGHT: RUN`, Python 80 PASS, `KMONG HUB SYNC: UPDATED`, **35/80/29, 0 missing, 0 fingerprint alerts, official scores UNMODIFIED**. UTC 30-minute bucket changed at 05:00; two runs do not demonstrate a same-bucket duplicate failure.
- Actual REST workflow metadata of these runs: `workflow_id=416801860`, `path=.github/workflows/kmong-hub-sync.yml`, `head_sha=69e584e57a3a37fa72b406d62ccddf9eef9dfcf2`, `created_at`, `updated_at`, `status=completed` and `conclusion=success`. **The REST object does not provide `completed_at`**. It does not expose a verified signed webhook Delivery UUID. Both bot runs are real, but their *origin* remains unverified.
- Current read-only hub observation JSON reports **repository_count=35, tracked_branch_count=80, product_links=29, 0 missing references, 0 blocking fingerprint issues, `no_official_score_authorization=true`**. This readback does not bind a particular webhook ID to a particular commit.

## Actual defect and chosen fix

Prior candidate offline evidence checker demanded fabricated `run.completed_at`; feeding a real GitHub Actions REST run would invariably fail. It also did not pin the workflow ID, path, source repository, or exact trusted central main SHA.

Two approaches evaluated: (A) keep a synthetic `completed_at` completion field (simple but impossible to source directly from REST and weakly authenticates the run), or (B) align with REST `updated_at` and reject any wrong workflow ID/path/repo/main SHA/status (selected; no additional API calls/permissions/cost; small test/doc maintenance). `updated_at` is only an observed timestamp upper bound, not cryptographic attestation.

At isolated feature `a676985554708e681340f7b6e62bbdbd720e9683` (parent `c58685aeae77dea01cf20c6b0a022b43149230db`):
- Updated `services/kmong-event-bridge/audit-e2e.mjs` to accept *two independently trusted SHA arguments* (expected Vercel deployed commit and expected central main commit), verify real Actions REST fields and identity `416801860`, fail closed for misattribution.
- Added 4 hostile regression tests to `test/audit-e2e.test.js`, updated `docs/E2E_AUDIT_CONSISTENCY_GATE.md` with real REST schema and CLI.
- Corrected stale `README.md` claims: **the original bridge project already exists** `prj_veZOkRkhMEMEA6h7PiEIl3IKcthn` (previous access 404, do not repeat same call or create a replacement), `main` schedule currently `23 * * * *` UTC hourly, native scheduled runs verified, 35/80/29 rather than historical 35/70/29.

## Exact CI verification and remaining hard blocker

- [Webhook bridge CI #43693309296](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43693309296) at `a676985554708e681340f7b6e62bbdbd720e9683`: **Node 73/73 + Python 80/80 = 153/153 PASS, 0 FAIL**; allowlist parity check PASS.
- [Final Blueprint Gate #43693309331](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43693309331): **SUCCESS**.
- The same CI runner public Production GET: HTTP **200**, verdict **READY_SHA_NOT_MATCHED**, original SHA `2863165b06d407ba632f18ad7a85a7c98f1989af` (different from isolated source `a676985554708e681340f7b6e62bbdbd720e9683`). Feature remains not deployed to Production.
- **NOT_VERIFIED:** source GitHub App Recent Deliveries/real HMAC signed POST/actual Vercel deploy SHA match, UUID→verified GitHub App Delivery→receiver→central dispatch→scan→ledger link. Existing project 404 access is not evidence of deletion.
- New verifier *still* reports `CORRELATED_NOT_VERIFIED` and **score_increment=0**, even with coherent sanitized evidence. It cannot assert HMAC from a JSON file.

## Safety, operational sequence and rollback

- `main=69e584e57a3a37fa72b406d62ccddf9eef9dfcf2` untouched. Operating docs baseline before this audit `1306adb2066d8c7ea4094e8831190f65662ca81f`.
- No Production deployment, Vercel/project/secret/domain, source/dispatch GitHub App permissions, customer data, original observation ledger, catalog, registration status or official score changed. No unrelated product work. Feature parent commit provides rollback.
- Do not repeat prior Vercel project 404 with unchanged account. To close remaining 10 points, obtain owner-approved access to **original project** and GitHub App Recent Deliveries; separately approve main workflow optional trace input, compatible original Vercel deploy and trace flag (in that order); collect actual signed delivery/response logs, correct Production SHA, bot workflow ID/path/run ID, collector `UPDATED`/`NO_CHANGE` (not `DEFERRED`), and ledger SHA. Do not infer proof from time/actor alone.
- **Provisional completion 90/100 remains unchanged; signed live E2E is a blocked external acceptance gate.**

**Evidence scope:** read-only GitHub REST run metadata + original job logs + observation JSON summary, exact isolated GitHub CI logs and CI public Production GET. No live signed POST and no Vercel management read retry.
