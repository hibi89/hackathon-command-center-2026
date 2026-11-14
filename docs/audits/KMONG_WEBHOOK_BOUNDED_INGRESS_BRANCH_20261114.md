# KMONG webhook bounded-ingress hardening candidate — 2026-11-14 KST

## Scope and baseline

- Goal: progress toward the fixed central provisional technical rubric 85/100 → 95/100 → 100/100, without attributing offline fixes to live signed webhook E2E.
- Production baseline: `main@69e584e57a3a37fa72b406d62ccddf9eef9dfcf2`, `services/kmong-event-bridge/lib/receiver.js` old blob `13d287c3d239532fadeccbca27d349cc3d36f0b9`.
- Isolated GitHub feature branch: `feature/kmong-webhook-bounded-ingress-20261114@74c715f39f0e2aa358b90e26c635b4c2acebfca0`. This branch is **not merged or deployed**.
- Files changed from main: `services/kmong-event-bridge/lib/body-reader.js` (new), `lib/receiver.js`, `test/body-reader.test.js` (new), `test/receiver.test.js`.

## Design comparison and choice

**A. Minimal code-only hardening (implemented in isolated branch):** stream request body through a 1 MiB byte counter instead of `await request.arrayBuffer()`; reject declared excessive bodies early; don't trust underreported Content-Length; cancel readers safely on error; return 400 for invalid body metadata/read failure; retain 413/401/202/502 response contracts. Four sequential GitHub requests share a maximum 8.5-second total deadline with each individual request additionally limited to 8 seconds. Cost: no new infrastructure or credential; operational risk: moderate (needs full regression/CI and eventual authorized rollout). Maintains existing non-atomic best-effort coalescing semantics.

**B. Durable queue and atomic per-delivery locking (not implemented):** better replay protection and multi-instance concurrency correctness, but involves new persistent service, secrets, billing and operational design. Requires separate user authorization. A cannot be called exactly-once delivery or signed E2E.

## Verification obtained

- Local Node v22.16.0 standalone body-reader tests: **7 PASS / 0 FAIL**, covering exact 1 MiB boundary, chunked excess, forged short Content-Length, declared oversize, malformed header, source stream failure, and empty/config guard.
- New feature-branch tests added: seven `test/body-reader.test.js` cases plus two `receiver.test.js` integrations (forged-length streamed HTTP413/no dispatch; total deadline abort). These nine feature-branch cases and the full existing regression suite are **CI NOT RUN / unverified**. Do not quote the 7 standalone local tests as a full GitHub CI result.
- Branch SHA remote readback: `74c715f39f0e2aa358b90e26c635b4c2acebfca0`. Compare to main: ahead 1 commit; four above files only.
- Authorized read-only `GET /actions/runs?event=schedule&per_page=20` yielded **total_count=1** and only #43590721340 SUCCESS. Second distinct native GitHub schedule completion not seen; no +5.
- Connected personal and hibi89-team Vercel scopes each show only `project08-executive`, **not the webhook bridge project**. Bridge hostname inspection yielded not-found via authenticated Vercel connector. This is an access limitation, not proof that the public endpoint is down. Do not repurpose project08 or create projects/change secrets without approval.
- Actual GitHub signed ping/401/push→Vercel→dispatch→collector→ledger readback remains **NOT_VERIFIED**, no +10.

## Existing live reliability evidence retained

- Two distinct half-hour bursts were verified in the prior [real bot-burst audit](KMONG_CENTRAL_BOT_BURST_LIVE_20261114.md): collector runs 43597859177 and 43600052895 each 80 PASS/UPDATED, paired runs 43597862952 and 43600053198 DEFERRED_BOT_BURST, no second expensive scan. This is **not** webhook ingress E2E.
- Central ledger latest independently readback during prior observation: 35 repos/80 branches/29 products, unlinked 0, fingerprint 0; official score untouched.

## Gate, risk and next actions

1. Complete offline integrated regression, including mocked timeout cancellation, then review the feature branch against main; optional GitHub PR CI **only after evaluating any automatic Vercel Preview deployment side-effect** and obtaining required deployment authorization.
2. Once owner has authorized access to the actual *existing* webhook Vercel project and GitHub App delivery setup, verify real signed ping 200, bad HMAC 401, ignored repository/branch, signed eligible push 202, newly dispatched GitHub Action SUCCESS, and exact ledger SHA readback. Preserve source App read-only scopes. Don't log or transmit keys.
3. Verify a second distinct GitHub-native `schedule` run and corresponding 80 tests/snapshot readback; never count bot workflow_dispatch as schedule.
4. Only then change the fixed technical score. **Current recognized central provisional score 85/100**. Production code/endpoint, GitHub main, secrets, source permissions, cron, official product scores, registrations and original data unchanged.

## Hand-off information

- Main: `69e584e57a3a37fa72b406d62ccddf9eef9dfcf2`
- Feature branch: `74c715f39f0e2aa358b90e26c635b4c2acebfca0`
- Operation branch: `kmong-productization` (read remote HEAD after audit commit)
- Local verification: `node --test body-reader.test.mjs` (isolated fixture only, 7/7)
- Full GitHub test command after safe PR approval: `npm test --prefix services/kmong-event-bridge`; `python3 -B -m unittest discover -s tools/kmong_hub_sync -p 'test_*.py' -v`.
- Production reference URL: `https://kmong-hub-event-bridge.vercel.app/api/webhook`; previous GET 200/ready/source parity evidence only, not a new run.
- KST audit day: 2026-11-14. GitHub operations were read-only except for isolated feature-branch code commit and operation-branch documentation.

## Exact Git-blob local verification and test-harness correction (2026-11-14 22:54 KST)

- Recreated the **exact committed** `lib/body-reader.js` and `test/body-reader.test.js` files in an isolated Node 22.16.0 test directory. `git hash-object` matched GitHub blobs `26c1975450b56af8c85100ecd38066af44f58897` and `d95cdf5092fb0b5269eddb6651dbff158ece0366`, respectively. `node --test test/body-reader.test.js` **7 PASS / 0 FAIL**. This upgrades the earlier loose standalone equivalence to byte-identical Git source+test verification, but still **does not** validate the entire receiver or integrated GitHub CI.
- Additional local timeout smoke caught a synthetic test-harness issue: `AbortSignal.timeout` uses an unref'ed timer, so a mocked stalled Promise alone may terminate Node test execution with an unsettled await. A referenced keepalive timer is now added **only to the new synthetic timeout test**, and cleared after the assertion. Runtime smoke with a referenced event-loop timer PASS.
- Latest isolated feature branch commit: `a8077bd01cbdfd4be1da33640b67bdf0449896f0` (`test(kmong): keep synthetic deadline rejection alive`). Earlier implementation commit `74c715f39f0e2aa358b90e26c635b4c2acebfca0` remains its ancestor. This feature branch is unmerged and undeployed; whole receiver/collector regression CI pending.
- GitHub `event=schedule` API at 2026-11-14T13:53:56Z / 22:53 KST: **total_count=1**; second independent schedule event still absent. Provisional central technical score **85/100 unchanged**. No claim that synthetic or isolated tests earned the E2E 10 points.
