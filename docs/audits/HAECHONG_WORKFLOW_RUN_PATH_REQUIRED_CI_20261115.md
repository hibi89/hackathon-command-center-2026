# HAECHONG — workflow_run canonical path required (2026-11-15 17:19 KST)

**Mission lock:** `HAECHONG_PRIMARY_MISSION_LOCK_V1` → GitHub App SHA256 HMAC webhook → original Vercel bridge → central Actions → read-only collector ledger. **Central 90/100 provisional; real signed HMAC POST E2E NOT_VERIFIED.**

## Confirmed defect and alternatives
The isolated bridge `eligibleEvent("workflow_run")` accepted `workflow_run.name = "Final blueprint completion evidence gate"` when **both** `workflow_run.path` and top-level `workflow.path` were missing. A display name is not a unique workflow path, creating unnecessary non-target dispatch risk. Existing exact-path security tests covered unrelated explicit paths, but had retained a name-only fallback.

Compared A) name-only fallback for backward compatibility (accepts ambiguous events), versus B) require an exact allowlisted canonical workflow path supplied by the run or top-level workflow (adopted; no new API, permissions, infra or cost). The run path has precedence. Missing paths now produce `202 ignored` with **zero** GitHub API calls. The trade-off is a false negative if a legitimate webhook omits both path fields; the existing best-effort hourly schedule still provides independent reconciliation. Source `workflow_run.path` and `workflow.path` do **not** by themselves prove the signature or source delivery.

## Exact source and tested implementation
- Repository `hibi89/hackathon-command-center-2026`.
- Isolated feature: `feature/kmong-webhook-bounded-ingress-20261114`.
- Parent `a676985554708e681340f7b6e62bbdbd720e9683`; new feature SHA **`c663bc3814cff896d8efd5014117348dfd23c377`**, remotely confirmed.
- Modified `services/kmong-event-bridge/lib/receiver.js`, `test/receiver.test.js` and `README.md`. Four new adversarial tests cover name-only rejection, HMAC-signed name-only 202/zero GitHub calls, conflicting run vs top-level workflow paths, and malformed/untrusted top-level path rejection.
- Real [bridge CI #43693953755](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43693953755): Node 22 **77/77 PASS** + Python **80/80 PASS** = **157/157 PASS**, FAIL 0, allowlist parity step SUCCESS. [Final Blueprint #43693953780](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43693953780): **SUCCESS**, exact feature SHA.
- Same GitHub runner's public GET: HTTP **200**, `READY_SHA_NOT_MATCHED`, deployed `2863165b06d407ba632f18ad7a85a7c98f1989af`; feature SHA **not in Production**. No signed POST executed in this test.

## Preservation and live acceptance
- `main=69e584e57a3a37fa72b406d62ccddf9eef9dfcf2` unchanged. Operating documentation base `e2a1779b4757421777b01f717ce1a67f4491bc3f`.
- Existing original project: `prj_veZOkRkhMEMEA6h7PiEIl3IKcthn`, `https://kmong-hub-event-bridge.vercel.app/api/webhook`. Prior management 404 under current connection remains blocked; same ineffective access not repeated and deletion not inferred.
- No Vercel deployment, secrets, App permissions, source repositories, original 35/80/29 observation JSON, official scores, registration/history, main workflow/schedule, or unrelated product changes.
- Zero point increase: GitHub App source Recent Deliveries, actual signed POST and real Delivery UUID → deployed SHA → dispatcher bot Actions run → collector UPDATED/NO_CHANGE → ledger blob causal chain **NOT_VERIFIED**.
- Next: authorized access to **existing** Vercel and original GitHub App Recent Deliveries; separate owner approvals for `main` workflow schema promotion, compatible Production deployment and optional trace flag in that order. Prove actual signature receipt, Ping/401 invalid/202 ignored/queued, workflow dispatch, scan result and ledger readback. Do not count `DEFERRED_BOT_BURST`, `coalesced`, or green Actions alone as a successful sync.

**Rollback**: feature parent is an unchanged Git commit; no force push or original data edits. This is branch-only CI evidence, not live Production acceptance.
