# Haechong GitHub App — exact-root signed workflow path verification

Date: 2026-11-15 16:28 KST. Source repository: hibi89/hackathon-command-center-2026.
Central primary mission remains GITHUB_APP_CENTRAL_AUTOMATION_90_TO_100 and side-product work stays deferred.
Isolated source branch: feature/kmong-webhook-bounded-ingress-20261114; final code SHA: 00d779629dc874dce3c124c65dbe3fa3e9fdf238.

## Discovery, options, and implementation

Earlier regex `/(^|\/)\.github\/workflows\/final-blueprint-gate\.ya?ml/` accepted a correctly named `.github/workflows` suffix even if placed under an arbitrary nested directory or another owner/repository prefix. The envelope's allowlisted repository identity alone did not ensure that the path prefix agreed with that repository.

Option A: retain suffix matching. Simple and compatible, but fails path provenance and may dispatch an unapproved workflow event. Rejected.
Option B: exact root-relative GitHub workflow path or an optional owner/repo prefix equal to the envelope's approved repository, with an optional GitHub @ref suffix. Same networking/API cost; fewer false positives, minimal code maintenance. Selected.

Implementation adds `approvedBlueprintWorkflowPath(path, fullName)` to `services/kmong-event-bridge/lib/receiver.js`. The existing `eligibleEvent()` uses it only when GitHub supplies a workflow path, preserving the no-path legacy name fallback (known compatibility limitation; a missing path cannot prove workflow identity). Paths with nested `.github`, other repo prefixes, case-changed filenames, malformed ref suffix, arbitrary path traversal or trailing data are denied. Legitimate absolute repo prefix or `.github/workflows` relative paths pass; existing head/base repository checks stay active.

Three test cases added to `services/kmong-event-bridge/test/receiver.test.js`: canonical/invalid path table, HMAC-signed foreign-prefix event ignored with zero GitHub API calls, and canonical signed path leading to a single dispatch. All synthetic, no outbound webhook POST.

## Verified sequence

- Initial source commit `d1ada9fc5a65f2d1add3a16bd9f71e068f48b479`: [CI #43690012904](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43690012904) FAIL 49/50 Node; legitimate-event test fixture omitted required source installation ID and therefore correctly received 403 instead of expected 202. The receiver code was not bypassed or weakened.
- Fixed only synthetic test fixture in 00d779629dc874dce3c124c65dbe3fa3e9fdf238 by supplying the test-owned source installation ID. [Bridge CI #43690096549](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43690096549) SUCCESS **50/50 Node + 80/80 Python = 130/130 PASS, 0 FAIL**. Source roster parity step succeeded.
- [Final Blueprint Gate #43690096537](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43690096537) SUCCESS at the same source SHA.
- CI runner read-only public GET to `https://kmong-hub-event-bridge.vercel.app/api/webhook`: HTTP 200, `READY_SHA_NOT_MATCHED`, source SHA `2863165b06d407ba632f18ad7a85a7c98f1989af`. This demonstrates that the latest feature code is NOT deployed. It does not prove real signed webhook POST, delivery causality, or complete Production function verification.

## Scope, blocker, and exit criteria

Changed files restricted to isolated feature `services/kmong-event-bridge/lib/receiver.js` and `test/receiver.test.js`. Unmodified: `main@69e584e57a3a37fa72b406d62ccddf9eef9dfcf2`, old Vercel Production, GitHub App settings, permissions, secrets, cron, collector JSON, 29 sources/19 product registrations, official scores. Exact GitHub parent chain retains earlier SHA `fe4749d763f794f2aa77bd1ece90c1d26b31817a` and failed fixture commit.

Central technical verification remains provisional **90/100**. A real GitHub App HMAC delivery must be correlated with Vercel receipt response/log, current Production SHA, a new bot workflow_dispatch run, actual collector UPDATED/NO_CHANGE and ledger readback. The existing Vercel project management API was previously denied with 404; do not retry the same denied path or create a replacement project. Owner approval is required to restore access, alter GitHub App permissions/secrets, merge, or deploy. Until then this isolated security change is code-level verification only.
