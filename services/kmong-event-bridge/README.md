# Kmong event-driven GitHub observer bridge

**Status:** source code and isolated CI are implemented; **live webhook/dispatch is NOT enabled or verified** until GitHub App webhook configuration, a central-only dispatch App, and Vercel production environment are configured and tested.

## Decision / alternatives

| Approach | Freshness | Ongoing infrastructure | Security / operational cost |
|---|---|---|---|
| GitHub-only daily cron (current fallback) | ~daily, GitHub schedule may delay/drop | no extra external service | Tested collector, but live `schedule` still unverified |
| Poll all 35 repos every 5 minutes | periodic, still not immediate | repeated GitHub Actions and API calls; GitHub cron unreliable | low complexity, higher waste; **rejected** |
| **GitHub App push + workflow_run webhooks → Vercel function → central workflow_dispatch** | starts upon event delivery; no continuously running PC/server | one short serverless request per relevant event + one normal collector workflow run | additional hosting and hub-only Action write credential; **selected** |

## Flow and preserved boundaries

1. Existing `kmong-hub-source-auditor` App (already installed with **All repositories**, read-only Contents/Actions) subscribes to **push** and **workflow_run** in GitHub App *Permissions & events*. Turn Webhook Active ON and configure Vercel endpoint and strong, independently generated **Webhook secret**. Do not send App PEM or secrets in a chat.
2. Vercel production function `POST /api/webhook` reads **raw bytes** and validates `X-Hub-Signature-256` with timing-safe SHA-256 HMAC. No unauthenticated event, non-allowlisted repo/branch, tag, unrelated workflow or own observer snapshot update triggers a collector. GitHub `ping` returns `pong`.
3. Function only dispatches if `KMONG_DISPATCH_ENABLED=true`. It signs a short-lived JWT for a **SECOND, distinct** `kmong-hub-dispatcher` GitHub App, installed **only** on `hibi89/hackathon-command-center-2026` with **Actions: Read & write** (Metadata read automatic). Existing source App remains **read-only**: **do not** grant it Actions write across all installed repositories.
4. Receiver obtains second App's 1-hour installation token scoped to exactly the central repo and only `Actions: write`. It reads the hub workflow's recent dispatch runs, then only if no non-cancelled bot run exists in the current UTC 30-minute bucket invokes GitHub `POST /actions/workflows/kmong-hub-sync.yml/dispatches` on `main`, input `dry_run=false`. Duplicate events return HTTP 202 `coalesced` without a dispatch; GET failure fails closed with 502. No extra database, token scope expansion, or paid service. This is **best-effort**, not atomic: concurrent Vercel instances can race. API 204 means *queued* only, **not** completed.
5. The **existing, already live-tested collector** `tools/kmong_hub_sync/sync.py` runs as a standard GitHub Actions job. It mints a separate read-only 35-repository source App token, reads branch HEAD/Actions/pin metadata, and uses its repository-local GITHUB_TOKEN to conditionally update **only** `kmong-productization/data/kmong_hub_auto_observations.json`. Repeated identical observations produce `NO_CHANGE`, no commit.
6. Keep the original UTC `10 2 * * *` daily schedule as best-effort missed-event reconciliation. The current workflow's `concurrency` serializes dispatcher/batch activity with `cancel-in-progress: false`, and GitHub pending runs coalesce under load. Independently, central Actions `quota_guard.py` gates the expensive source scan at the same UTC 30-minute window and skips repeated tests. Neither layer stops simultaneous webhook races or guarantees event history; the daily schedule remains a best-effort reconciliation. **No claim of exactly-once deliveries, guaranteed 5-minute SLA, or guaranteed scheduled runs.**

**Never** automatically raise official completion percentages, alter product registration/history, source code, pinned schema, branch protections, secrets, or runtime permissions to overcome failed events. Default fail-closed. All webhook deliveries contain GitHub push/CI metadata and are processed by the user's Vercel account; incoming full bodies are not persisted by this code. Do not log payloads, tokens or private keys.

## Vercel project and env (requires deployment/account authorization)

New dedicated Vercel project (do **not** attach to unrelated `project08-executive`), linked to existing GitHub `hibi89/hackathon-command-center-2026`, production `main`, root directory `services/kmong-event-bridge`, Node >=22, no install dependencies.

| Environment variable | Scope | Value/control |
|---|---|---|
| `KMONG_WEBHOOK_SECRET` | Vercel Production **secret** | Strong independently generated secret, exactly matching source GitHub App Webhook secret |
| `KMONG_DISPATCH_APP_ID` | Vercel Production | Numeric **App ID** of second central-only dispatch App (not Client ID) |
| `KMONG_DISPATCH_APP_PRIVATE_KEY` | Vercel Production **secret** | PEM from second GitHub App; never upload in GitHub or chat |
| `KMONG_SOURCE_INSTALLATION_ID` | Vercel Production optional, recommended | Existing source App installation ID as a plain numeric string; rejects payloads from other installations |
| `KMONG_DISPATCH_ENABLED` | Vercel Production | Start with `false`; set `true` **only after** webhook signature and event tests complete |

Health: `GET /api/webhook` returns HTTP 503 `not_configured` until all credentials and the dispatcher enable toggle are present; after enable, HTTP 200 `ready`. This is not proof of GitHub connectivity. The GitHub App Webhook URL is `https://<verified-vercel-production-host>/api/webhook`, content-type `application/json`. Use official GitHub **Recent Deliveries** to see HTTP 200 `pong` and relevant push HTTP 202 `queued`.

**Credential boundaries:** original GitHub App is read-only source access. Second dispatch App Actions:write installation is central-only; any request to expand it, use PATs, or add paid services is out-of-scope and needs approval. This requires account UI access; GitHub connector in this chat cannot register/edit GitHub Apps or fill PEM Secrets.

## CI / verification gates

```bash
cmp tools/kmong_hub_sync/source_repositories.json services/kmong-event-bridge/source_repositories.json
npm test --prefix services/kmong-event-bridge
python3 -B -m unittest discover -s tools/kmong_hub_sync -p 'test_*.py' -v
```

The branch-only CI verifies the exact 35-repo allowlist matches the collector roster; 16 Node security/dispatch regressions plus existing 26 Python collector tests. **Mock GitHub responses cannot count as live webhook or Vercel verification.**

### Live acceptance procedure (after account setup)

1. Confirm Vercel deployment **Ready** and anonymous HTTPS response from `GET /api/webhook`; 503 before enable must not be declared healthy. Confirm no unexpected auth/protection page. Inspect logs without secrets.
2. GitHub App Webhook **Ping** must show delivery `200 pong`. A tampered signature must be HTTP 401. Ignore a non-allowlisted repository and an untracked branch (`202 ignored`).
3. With second App installed on the hub only, set `KMONG_DISPATCH_ENABLED=true` and redeploy if necessary. Trigger a **non-destructive push** to a tracked branch; GitHub delivery should report `202 queued`. Verify a **new** central Actions run is `event=workflow_dispatch` and its execution is `SUCCESS`, 35/70/29 evidence matches expected; verify `UPDATED` or `NO_CHANGE` and the observer snapshot readback. A webhook 202 is **not** success of the collector.
4. Confirm legitimate `workflow_run:completed` from `final-blueprint-gate.yml` also queues sync. Confirm observer's own hub snapshot commit does **not** create an infinite event loop. Confirm burst handling and API failure returns 502, do not lose data or change official scores.
5. Inspect actual daily `schedule` event separately; GitHub may delay/drop scheduled events. Since no durable event delivery queue/replay store is implemented in the bridge, GitHub retry/redelivery and daily reconciliation are operational safeguards, **not** guaranteed recovery. Operational sign-off requires incident/error handling and sustained live evidence.

## Rollback

1. In Vercel, set `KMONG_DISPATCH_ENABLED=false` (or disable source App Webhook Active). Do not uninstall the already-proven source read App or delete its PEM secret.
2. Original daily `cron: '10 2 * * *'` and existing manual `dry_run=true/false` collector continue unaffected. Prior snapshot and Git SHA history remain available.
3. If needed, revert only event bridge / bridge-test commits from the integration branch; never force push or rewrite central product history. Re-enable only after signature/auth/run acceptance succeeds.

## Proven boundaries as of 2026-11-13 KST

- Existing collector: manual `DRY_RUN`, actual `UPDATED` first write and `NO_CHANGE` all **live verified** on GitHub; 35 repos, 70 refs, 31 pins, 29 products (28 linked, 1 unlinked); official 29/29 `UNASSESSED`.
- GitHub Actions daily `schedule`: configured but still **not observed** as an actual event; earlier short-window cron experiment was reverted.
- New event bridge: CI-tested design; **Vercel deployment, actual webhook activation, second App installation, incoming signed delivery, and end-to-end source push→hub run remain pending**.

## 2026-11-14 upstream burst mitigation (code verified; Production unverified)

- GitHub `main@254c9e54551a58c6d97e46bb22272fcf9bab6154`: `lib/receiver.js` now reads the existing central workflow dispatch history using the **already hub-scoped Actions:write** installation token; returns `202 coalesced` rather than dispatching a duplicate bot run in the same UTC 30-minute bucket. Malformed/unavailable GitHub history returns `502 dispatch_failed`, with no dispatch.
- No new database, API key, infrastructure project or paid services. App permissions, secret handling, original snapshot and score authority unchanged. No atomic cross-instance lock: simultaneous webhook deliveries can race, although central preflight still reduces excess scans.
- [Bridge GitHub Actions #43549954047](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43549954047): Node **22/22 PASS**, Python collector **75/75 PASS**, source allowlist comparison success. [Final Blueprint Gate #43549954069](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43549954069): SUCCESS.
- The central post-guard real bot run [#43549435131](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43549435131) separately proved preflight RUN + 75 tests + `UPDATED`, 35 repos/80 refs/29 products, 0 fingerprint alerts; this was **before** upstream code deployment verification.
- **Not yet confirmed:** whether `https://kmong-hub-event-bridge.vercel.app/api/webhook` is serving this GitHub SHA, Vercel Production deployment state or source webhooks after deploy. The connected Vercel account does not list that project; published URL is not accessible through available page-inspection tools. This is not evidence of an outage. There are still zero observed `event=schedule` runs after the designated slot; cron cannot be advertised as a proven fallback. Source fixes in GitHub cannot be presented as a Production rollout without SHA and live trigger checks.
- Rollback: normal Git revert of `lib/receiver.js` and tests if regressions appear. On an already connected Production project, verify its exact deployed Git SHA before deciding whether a redeploy is needed; never silently create a new Vercel project, change env/secrets, or broaden permissions.

