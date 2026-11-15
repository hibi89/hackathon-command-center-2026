# Haechong GitHub App — signed workflow event path hardening

**Date:** 2026-11-15 KST
**Central task:** GitHub App → signed HMAC ingress → existing Vercel bridge → Actions dispatch → read-only ledger.
**Source repo:** `hibi89/hackathon-command-center-2026`
**Isolated branch:** `feature/kmong-webhook-bounded-ingress-20261114`
**Final tested source SHA:** `5553b9d1bb86839a570226978e8191d86fab32b2`
**Deployment:** NOT merged/deployed; central technical verification 90/100 unchanged.

## Verified defect and design comparison

Read-only review of `services/kmong-event-bridge/lib/receiver.js` showed that `eligibleEvent("workflow_run", ...)` accepted a signed completed workflow with a **non-blueprint path** if the display name alone matched `Final blueprint completion evidence gate`. A legitimate source repository can name a different workflow identically, causing a redundant central dispatch despite a mismatch with the intended path allowlist. Authentication/HMAC cannot prevent this semantic misclassification.

Two zero-infrastructure options:
- A. Trust either display name or path, preserve permissive compatibility but allow unrelated same-name workflow runs to trigger dispatch. Rejected.
- B. When GitHub supplies a concrete workflow path, require `final-blueprint-gate.yml` path match; use the existing display name fallback only if no workflow path exists. **Implemented** as a minimal change, preserving normal event compatibility without a new API or credential.

The source change is localized to `services/kmong-event-bridge/lib/receiver.js`; two synthetic tests added to `services/kmong-event-bridge/test/receiver.test.js` verify same-name unrelated path is ignored (and dispatch count stays zero), while known path and empty-path compatibility still pass. Original source App allowlist and collector JSON unchanged. No new permissions, secrets, service, data writes or webhooks introduced.

## Exact executed CI sequence

1. Initial isolated code SHA `983450bf7e95432ebcca95762fc28ce2fc2f236d` failed [#43686890654](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43686890654) due a mistakenly double-escaped regex literal: `SyntaxError: Invalid regular expression`. Node part 13 pass, one file-level failure. The new logic was **not** accepted on this failed SHA.
2. Corrected regex syntax at `5553b9d1bb86839a570226978e8191d86fab32b2`. [Bridge CI #43686959469](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43686959469) completed **SUCCESS** with Node **43/43 PASS** + Python collector **80/80 PASS**, total **123/123 PASS**, zero FAIL. Source roster parity check also SUCCESS.
3. Exact-head [Final blueprint gate #43686959426](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43686959426) completed SUCCESS. These are CI and synthetic event tests, **not** actual GitHub App delivery confirmation.

## Read-only Production evidence

The same successful GitHub Actions runner performed anonymous non-mutating `GET https://kmong-hub-event-bridge.vercel.app/api/webhook`. Actual job log recorded:

`KMONG_PRODUCTION_GET_PROBE {"http_status":200,"verdict":"READY_SHA_NOT_MATCHED","source_sha":"2863165b06d407ba632f18ad7a85a7c98f1989af"}`.

This proves only a responding **older** production GET/health route at that observed time, not live signed POST, dispatch, new SHA, service health under load, nor a working real webhook. It positively demonstrates that `5553b9d1bb86839a570226978e8191d86fab32b2` is **not** the public Production SHA. Current GitHub `main@69e584e57a3a37fa72b406d62ccddf9eef9dfcf2` was unchanged during this work. Current Vercel project/deployment metadata remains inaccessible through the previously denied connected account (404); do not repeat identical denied calls or infer deletion.

## Next primary gate and authorization

- Existing Vercel project `prj_veZOkRkhMEMEA6h7PiEIl3IKcthn` and source GitHub App **Recent Deliveries** must become readable through owner-authorized access.
- Read actual Production deployment SHA/logs and verify genuine signed ping (200), invalid signature (401), ignored repo/branch (202), authorized push (202 queued), central `workflow_dispatch` SUCCESS and ledger UPDATED/NO_CHANGE with exact SHA.
- The feature hardening remains isolated until explicit approval for merge and Production deployment; do not assume a CI pass deploys it.
- Central provisional technical verification **90/100 unchanged**; signed E2E last 10 points unverified. Mission lock `HAECHONG_PRIMARY_MISSION_LOCK_V1` remains authoritative. No pivot to side products.
