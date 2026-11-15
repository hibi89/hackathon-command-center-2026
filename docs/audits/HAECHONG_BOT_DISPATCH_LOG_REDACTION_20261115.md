# Haechong GitHub App: actual dispatcher activity and log-redaction hardening

Date: 2026-11-15 KST. Operating branch: kmong-productization. Feature branch: feature/kmong-webhook-bounded-ingress-20261114.
Verified feature commit: cf2d90ae5f709ca2e824a1b26a163437d9ed75f3. Central provisional score: 90/100 unchanged.

## Actual GitHub Actions evidence (read-only source)

GET of GitHub workflow_dispatch runs proves kmong-hub-dispatcher[bot] actor invoked the hub workflow. It does NOT prove upstream GitHub signed delivery or attribution to Vercel, because no delivery UUID or request logs are accessible.

- Run https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43658496602: 2026-11-15 00:30:22 UTC, SUCCESS and actual UPDATED scan of 35 repos / 80 refs / 29 products, no fingerprint errors or official score changes.
- Run https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43658499842: 2026-11-15 00:30:25 UTC, SUCCESS but preflight DEFERRED_BOT_BURST: NOT_SYNCED, zero source scan/snapshot changes. A workflow SUCCESS is not proof of synchronization.
- Runs https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43678839627 and https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43679174366: real bot dispatch activity at 04:55 and 05:00 UTC, each UPDATED in a different fixed 30-minute window.

Upstream burst coalescing is best-effort and not atomic. The three-second pair shows duplicate bot-dispatch calls exist; the downstream quota guard protected against duplicate scanning, not duplicate workflow creation. Cause of the duplication is unverified.

## Code decision and evidence

Option A: retain raw thrown error.message in console.error for diagnostics; creates risk that upstream request errors expose tokens or payload strings in logs. Rejected.
Option B: emit a constant upstream_unavailable log value and preserve 502 dispatch_failed response. Chosen: no external cost, no permissions changed, safer logging with fewer diagnostics.

Only feature branch services/kmong-event-bridge/lib/receiver.js and test/receiver.test.js changed. New adversarial test throws a synthetic error containing Authorization bearer material and synthetic webhook secret; asserts 502, one fixed safe log line and no secret in captured logs.

CI https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43688060055 at cf2d90ae5f709ca2e824a1b26a163437d9ed75f3: Node 44/44 PASS, Python collector 80/80 PASS, total 124/124, zero failures. Separate final blueprint gate https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43688060049 succeeded.

The same CI runner performed a public read-only Production GET: HTTP 200, READY_SHA_NOT_MATCHED, source_sha=2863165b06d407ba632f18ad7a85a7c98f1989af. The corrected feature code is NOT deployed. No actual signed webhook POST, delivery correlation or new Production SHA parity is verified.

## Remaining blocker / permission boundary

Existing Vercel project ID prj_veZOkRkhMEMEA6h7PiEIl3IKcthn is not readable through previously tested connection methods (404). Avoid reattempting unchanged denied calls. Existing GitHub App Recent Deliveries has not been inspected. Completion requires authorized existing-project visibility and a correlated real signed event with receipt/response -> workflow_dispatch ID -> scan result -> ledger readback. No merge, deploy, secret change, permission expansion or new project without owner approval. Original catalogue, ledger, main and source repositories unchanged.
