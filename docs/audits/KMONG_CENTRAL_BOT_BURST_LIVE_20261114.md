# KMONG 중앙 봇 동시 디스패치 실증 및 보안 위험 감사 — 2026-11-14 KST

## Scope and immutable evidence

- Central repo: `hibi89/hackathon-command-center-2026`; Production source reference `main@69e584e57a3a37fa72b406d62ccddf9eef9dfcf2`.
- GitHub REST `GET /actions/runs?per_page=100` returned 731 overall runs and **one schedule event on the returned first page**: [#43590721340](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43590721340), completed success, 2026-11-14T11:35:04Z. This first-page observation **does not independently establish the all-history schedule total**. A second distinct native schedule PASS has not been verified; no extra 5 points.
- Closely timed bot `workflow_dispatch` runs:
  - [#43597859177](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43597859177), created 2026-11-14T13:03:52Z, job `132456104753` SUCCESS. Log: `KMONG PREFLIGHT: RUN remaining: 5750 reserve: 450`, Python unit suite **80 PASS / 0 FAIL**, `KMONG HUB SYNC: UPDATED repositories: 35 tracked branches: 80 product records: 29 linked refs: 29 unlinked refs: 0 fingerprint alerts: 0 official scores: UNMODIFIED`.
  - [#43597862952](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43597862952), created 2026-11-14T13:03:54Z, job `132456576917` SUCCESS but log explicitly `KMONG PREFLIGHT: DEFERRED_BOT_BURST remaining: 5750 reserve: 450`. Unit test and source-scan steps SKIPPED; no snapshot sync. Successful workflow status **must not** be interpreted as successful second collection.
- Separate GitHub repository readback: `data/kmong_hub_auto_observations.json` blob `b2ac54b5ed7dbd137263e3f306a48d01138d5d61`, summary `repository_count=35`, `tracked_branch_count=80`, `product_links=29`, `product_refs_unlinked=0`, `blocking_fingerprint_issues=0`, `provisional_official_certifications=0`. This is a point-in-time snapshot, not a buyer certification.
- Baseline inspected without production mutation: `services/kmong-event-bridge/lib/receiver.js@13d287c3d239532fadeccbca27d349cc3d36f0b9`, `test/receiver.test.js@9907026618778482cf18b4bd5f3f5756bf457dda`, `tools/kmong_hub_sync/quota_guard.py@e0103374b0fc56c839c2255d098e41206f46ea60`.

## Verified boundary

This real two-run pair establishes that the **collector's bot burst guard deferred the second scan** in this instance. It does **not** establish atomic webhook admission, simultaneous signed POST behavior, retry/delivery guarantees, replay protection, a second native schedule success, or actual signed GitHub → Vercel → dispatch → collector E2E.

## Identified code risks (static review, not exploited or live-verified)

1. In `receiveWebhook`, a request with absent or low `Content-Length` reaches `await request.arrayBuffer()` before the post-read 1 MiB cap. The existing oversized-body test only asserts HTTP413 and no GitHub API calls; it does not prove the body is bounded *during* ingestion. A slow or chunked oversized request could consume memory/time first.
2. Each GitHub request uses an independent 8-second timeout, while the documented Vercel function budget is 10 seconds. Three dependent GET/POST operations plus dispatch can exhaust total time before a reliable response.
3. The 30-minute workflow-history gate is intentionally best-effort, not an atomic lock. Persistent replay guarantees for webhook deliveries are absent.

## Minimal-change alternatives / approval gates

**A. Recommended for a subsequent authorized code change:** read webhook request.body with a byte-counted stream and immediately cancel when bytes exceed 1 MiB; preserve 413/401/202/502 API contracts. Add tests for absent/forged length, many small chunks, exact boundary, early cancellation, and malformed signature. Add an overall request deadline within the hosting budget; fail closed. Pros: no new infrastructure or fees; modest code/testing scope. Limit: still not atomic across concurrent dispatches or durable across failures.

**B. Structural option requiring separate approval:** platform ingress limits plus durable atomic delivery ID / queue (database or KV). Pros: strong replay and concurrency semantics. Cons: infrastructure complexity, operating cost, secrets/permissions, production cutover, and failure recovery migration.

No source code, cron, GitHub App privileges, deployment, secrets, official scores, ledger data, or product history was modified by this audit. Option A is proposed, **not implemented**. Any main/Production integration or configuration/security-permission adjustment awaits explicit owner approval and live tests.

## Score / gates

- Central provisional technical score: **85/100 unchanged**.
- Native schedule repeat: **0/5 additional** until a second distinct `event=schedule` run is verified with PASS and snapshot readback.
- Signed webhook E2E: **0/10 additional** until actual signed deliveries and central evidence are confirmed.
- Production: retains previous partial GET/runtime-parity evidence only; no new browser, signed POST, or full-service certification in this run.

## Follow-up: second independent 30-minute collection bucket (2026-11-14 22:30–22:32 KST)

- [#43600052895](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43600052895), bot workflow_dispatch at 2026-11-14T13:30:02Z, job `132462692827` SUCCESS: `PREFLIGHT RUN`, **80 tests PASS**, `SYNC UPDATED` (35/80/29; unlinked 0, fingerprint 0, official scores UNMODIFIED).
- [#43600053198](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43600053198), same bot event timestamp, job `132463053679` SUCCESS but `PREFLIGHT DEFERRED_BOT_BURST`, test/scan steps SKIPPED and no second sync. This is a *deferred job*, not an additional completed observation.
- Independent central JSON readback after this pair: blob `eae16be34269042ad038c66c975caefbeca8b85f`, 35 repositories/80 tracked branches/29 linked products, zero missing/unlinked refs, zero fingerprint alerts, zero official certification.
- Interpretation: burst deferral **observed in two separate half-hour buckets** (22:03 and 22:30 KST). The second `schedule` run and signed webhook live E2E gates remain unverified; **score stays 85/100**. No authorization to infer atomic webhook deduplication or Production signed-delivery success.
