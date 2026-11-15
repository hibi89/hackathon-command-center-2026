# Haechong central GitHub App — workflow_run origin/path guard audit

Verification time: 2026-11-15 16:16 KST (GitHub Actions run logs 07:16 UTC).
Repo: hibi89/hackathon-command-center-2026; feature: feature/kmong-webhook-bounded-ingress-20261114.
Verified source SHA: `fe4749d763f794f2aa77bd1ece90c1d26b31817a`; Production/main unchanged; central provisional score 90/100 unchanged.

## Defect and design decision

The signed GitHub workflow_run envelope had a branch allowlist and a filename-suffix check, but did not restrict the pathname to `.github/workflows/` or reject a mismatch between the top-level repository and the run's `head_repository`/`repository` if present. Thus, unrelated or fork-origin completed workflows with a coincidentally allowed branch/path suffix could trigger a central dispatch. Signatures authenticate GitHub as sender, but do not by themselves establish that the run is within the intended origin/scope.

Option A: keep filename-only matching and infer trust from a signed sender; no compatibility changes, but extra false dispatch/burst and ambiguous origin. Rejected.
Option B: require an exact `.github/workflows/final-blueprint-gate.yml` or `.yaml` workflow path when present, and require any run-supplied head/base repository identities to match the signed envelope's allowlisted repository; retain previous display-name fallback only when no path is available, retaining synthetic compatibility. Chosen: no new external calls, credentials or operational costs, and narrower dispatch scope.

## Code / actual tests

Changed only `services/kmong-event-bridge/lib/receiver.js` and `services/kmong-event-bridge/test/receiver.test.js` on the isolated feature branch. Added three synthetic tests: (1) block same filename outside `.github/workflows` including docs/arbitrary paths and similarly named directories; (2) signed same-branch, same-workflow event with a fork `head_repository` must return HTTP 202 ignored without dispatch; (3) matching head/base repository remains eligible but inconsistent base repository is denied. Existing 44 Node tests remain preserved.

- [Bridge CI #43689210139](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43689210139), exact feature `fe4749d763f794f2aa77bd1ece90c1d26b31817a`: **Node 47/47 PASS; Python collector 80/80 PASS; 127/127 total, 0 FAIL**; repository allowlist comparison succeeded.
- [Blueprint Gate #43689210136](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43689210136): SUCCESS on same SHA.
- Real GitHub Actions API readback of runs #43689210136 and #43688060049: `path=.github/workflows/final-blueprint-gate.yml`, `head_repository=hibi89/hackathon-command-center-2026`, `repository=hibi89/hackathon-command-center-2026`, event=push. These real metadata fields match the new policy; this is NOT a full webhook payload test or a signed incoming delivery.
- Same CI runner production read-only GET response: HTTP 200, `READY_SHA_NOT_MATCHED`, old `source_sha=2863165b06d407ba632f18ad7a85a7c98f1989af`. This proves only GET response and feature SHA mismatch, not signed POST or E2E, nor full live service function.

## Blocker / scope / next verification

Known existing Vercel bridge project `prj_veZOkRkhMEMEA6h7PiEIl3IKcthn` remains unavailable through previous team/project API visibility (404). Do not retry unchanged denied endpoints. No recent signed GitHub App delivery receipts or Vercel incoming POST logs available. Without the delivery UUID/signature receipt, exact existing Production deployment SHA and matching central workflow_dispatch/collector snapshot, the causal end-to-end gate remains **NOT_VERIFIED**.

The change is **feature-branch only**: no merge into main, Vercel Production update, secret/permission change, new project, customer data, source catalog, product registration or official scoring modification. Prior feature SHA `cf2d90ae5f709ca2e824a1b26a163437d9ed75f3` stays in Git history. For operational completion: owner-authorized existing Vercel/App delivery access, read current Production SHA, verify signed Ping 200 and tamper 401, event filtering 202 and relevant push 202 queued, correlate real dispatcher run SUCCESS and collector UPDATED/NO_CHANGE with readback; no credit for synthetic-only tests.
