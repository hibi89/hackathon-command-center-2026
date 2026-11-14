# KMONG central webhook shared-deadline hardening — actual CI acceptance

**As of:** 2026-11-14 23:09 KST (GitHub Actions events 14:06–14:07 UTC).  
**Fixed central provisional technical score:** **85/100**, NOT 95/100.  
**Source:** `hibi89/hackathon-command-center-2026`.  
**Runtime baseline:** `main@69e584e57a3a37fa72b406d62ccddf9eef9dfcf2` (unchanged).  
**Isolated feature branch:** `feature/kmong-webhook-bounded-ingress-20261114@9e7e756bd9f4f8dabd517bf327c1488961f3d7a9` (unmerged; no Production rollout).

## Implemented and independently verified

- Earlier isolated feature branch added a streaming, actual-byte-counted 1 MiB raw webhook body cap and a capped 8.5 s GitHub dispatch deadline; [previous GitHub run #43602535978](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43602535978) passed Node 37/37 and Python 80/80 (117 total, 0 FAIL).
- New commit `9e7e756bd9f4f8dabd517bf327c1488961f3d7a9` now enforces **one shared deadline beginning when POST is received** (not merely before GitHub calls). A stalled/chunked body read aborts safely and reports `503 request_timeout`; the same `AbortSignal` limits the four sequential GitHub API calls, each already limited to 8 s. Before any GitHub call, an expired deadline fails closed. Existing 413 oversize, 401 bad HMAC, 202 ignored/queued/coalesced, and 502 dispatch failure contracts are retained.
- Four new adversarial regression cases: stalled stream cancellation, expired body deadline, aborted incoming request with zero GitHub calls, and already-expired shared dispatch deadline.
- **Actual GitHub Actions run [#43603161042](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43603161042), at exact feature SHA: COMPLETED/SUCCESS.** Node 41/41 PASS, Python 80/80 PASS; **121 PASS/0 FAIL/0 SKIP**. Source App allowlist parity step also SUCCESS. This is synthetic/mocked security regression, not real GitHub webhook delivery.
- Same exact feature SHA [final blueprint gate #43603160877](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43603160877): COMPLETED/SUCCESS.
- The CI performed read-only Production GET (HTTP 200; `READY_SHA_NOT_MATCHED`, source SHA `2863165b06d407ba632f18ad7a85a7c98f1989af`). The mismatch is expected for an unmerged feature branch; it does **not** prove that the new hardening runs in Production.

## Separate live schedule and ledger gates

- GitHub REST `GET /actions/runs?event=schedule&per_page=30` returned `total_count=1`, only native `schedule` [#43590721340](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43590721340) COMPLETED/SUCCESS. A second independent native schedule run with source-scan evidence has not been verified; the reserved **5 points remain unearned**.
- Latest central JSON readback during this work: blob `79a851306d1b5d86e05dfc9f986ac7e13b8c5ec5`, summary 35 repositories, 80 tracked branches, 29 product links, zero unlinked product refs, zero fingerprint alerts, zero official certifications. A GitHub `workflow_dispatch` is **never** counted as native `schedule`.
- Connected Vercel personal and hibi89-team accounts list only unrelated `project08-executive`; no accessible `kmong-hub-event-bridge` project. Live signed GitHub Ping, invalid signature, relevant push → Vercel → dispatch → collector → JSON exact readback remain **NOT_VERIFIED**, so the reserved **10 points remain unearned**. This access limitation is not evidence of endpoint failure.

## Recommended next steps and protected boundaries

1. Do not change score, `main`, Production, cron, source App privileges, Vercel secrets/projects, customer data, original snapshot or product registration while evidence gates are unfulfilled.
2. If the existing webhook Vercel project is surfaced with proper owner authorization, record its exact project/team/deployment, and verify signed real GitHub deliveries in controlled order (ping 200, tampered 401, ignored repo/branch 202, eligible push 202 queued; subsequent actual GitHub workflow SUCCESS and ledger UPDATED/NO_CHANGE with SHA readback). Inspect safe logs without exposing PEM/secret; do not use test-signed local requests to claim live E2E.
3. Independently verify a second future native `schedule` run after GitHub schedules it. Confirm `event=schedule`, job/test results and ledger readback before awarding its 5 points.
4. Only after reviewing the isolated candidate and approving the actual rollout, consider merging to `main`/deploying; approval is required for deployment/security configuration changes. Implementation A (current zero-infrastructure bounded stream/shared deadline) is low-cost; implementation B (durable queue+atomic lock) requires design review and separate cost/permission approval.
5. Rollback baseline: feature branch parent `95a5022387030bc96faaa27b0dd834039eb3646a`; runtime `main@69e584e57a3a37fa72b406d62ccddf9eef9dfcf2`. Revert normal commits only, never force push.

**Conclusion:** Code/CI readiness advanced, but central *fixed 100-point acceptance evidence* remains **85/100**. 95/100 or 100/100 cannot be represented as verified before real signed E2E and/or a second native schedule.
