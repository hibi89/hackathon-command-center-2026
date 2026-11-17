# Kmong event-driven GitHub observer bridge

**Current evidence (2026-11-17):** A real signed GitHub App Delivery → existing Vercel Production → central Actions → observer ledger chain was attested on **2026-11-16** (bot [run #43859747199](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43859747199), collector `NO_CHANGE` and ledger readback). A later central [run #44020977616](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/44020977616) independently showed `UPDATED` (35 repositories/80 refs/29 products). **These are dated receipts, not proof of the current Production source SHA or a new signed Ping 200.** The current Vercel deployment SHA remains `NOT_VERIFIED` in this review, and this PR #6 code is feature-only, **not deployed**. No replacement project, secret, permission or Production change is authorized.

## Decision / alternatives

| Approach | Freshness | Ongoing infrastructure | Security / operational cost |
|---|---|---|---|
| GitHub-only hourly cron (current fallback) | best effort; GitHub schedule may delay/drop | no extra external service | Real native schedule `UPDATED` confirmed; does not prove live webhook |
| Poll all 35 repos every 5 minutes | periodic, still not immediate | repeated GitHub Actions and API calls; GitHub cron unreliable | low complexity, higher waste; **rejected** |
| **GitHub App push + workflow_run webhooks → Vercel function → central workflow_dispatch** | starts upon event delivery; no continuously running PC/server | one short serverless request per relevant event + one normal collector workflow run | additional hosting and hub-only Action write credential; **selected** |

## Flow and preserved boundaries

1. Existing `kmong-hub-source-auditor` App (already installed with **All repositories**, read-only Contents/Actions) subscribes to **push** and **workflow_run** in GitHub App *Permissions & events*. Turn Webhook Active ON and configure Vercel endpoint and strong, independently generated **Webhook secret**. Do not send App PEM or secrets in a chat.
2. Vercel production function `POST /api/webhook` reads **raw bytes** and validates `X-Hub-Signature-256` with timing-safe SHA-256 HMAC. No unauthenticated event, non-allowlisted repo/branch, tag, unrelated workflow or own observer snapshot update triggers a collector. GitHub `ping` returns `pong`.
3. Function only dispatches if `KMONG_DISPATCH_ENABLED=true`. It signs a short-lived JWT for a **SECOND, distinct** `kmong-hub-dispatcher` GitHub App, installed **only** on `hibi89/hackathon-command-center-2026` with **Actions: Read & write** (Metadata read automatic). Existing source App remains **read-only**: **do not** grant it Actions write across all installed repositories.
4. Receiver obtains second App's 1-hour installation token scoped to exactly the central repo and only `Actions: write`. It reads the hub workflow's recent dispatch runs, then only if no non-cancelled bot run exists in the current UTC 30-minute bucket invokes GitHub `POST /actions/workflows/kmong-hub-sync.yml/dispatches` on `main`, input `dry_run=false`. Duplicate events return HTTP 202 `coalesced` without a dispatch; GET failure fails closed with 502. No extra database, token scope expansion, or paid service. This is **best-effort**, not atomic: concurrent Vercel instances can race. API 204 means *queued* only, **not** completed.
5. The **existing, already live-tested collector** `tools/kmong_hub_sync/sync.py` runs as a standard GitHub Actions job. It mints a separate read-only 35-repository source App token, reads branch HEAD/Actions/pin metadata, and uses its repository-local GITHUB_TOKEN to conditionally update **only** `kmong-productization/data/kmong_hub_auto_observations.json`. Repeated identical observations produce `NO_CHANGE`, no commit.
6. The existing `main` workflow currently specifies UTC `23 * * * *` **hourly** (best-effort missed-event reconciliation; verified native schedule runs exist). The `concurrency` group serializes dispatcher/batch activity with `cancel-in-progress: false`; the `quota_guard.py` defers duplicate bot scans per UTC 30-minute bucket. Neither layer stops simultaneous webhook races or guarantees event history; the hourly schedule remains best effort. **No claim of exactly-once deliveries, guaranteed 5-minute SLA, or guaranteed scheduled runs.**

**Never** automatically raise official completion percentages, alter product registration/history, source code, pinned schema, branch protections, secrets, or runtime permissions to overcome failed events. Default fail-closed. All webhook deliveries contain GitHub push/CI metadata and are processed by the user's Vercel account; incoming full bodies are not persisted by this code. Do not log payloads, tokens or private keys.

## Vercel project and env (requires deployment/account authorization)

**Existing project only:** `prj_veZOkRkhMEMEA6h7PiEIl3IKcthn`, host `https://kmong-hub-event-bridge.vercel.app`. Preserve its original GitHub integration and settings. Current Vercel connector received 404 for its details under this connection, so account/project ownership must be verified through existing authorized access; **do not create a replacement or attach to unrelated `project08-executive`**. The source project root is `services/kmong-event-bridge`, Node >=22, no install dependencies; deployment and secret changes require separate owner approval.

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

The isolated branch CI verifies the exact 35-repo allowlist against the collector roster; GitHub Actions #43692455914 previously passed Node69 + Python80 tests. Always recheck the exact candidate SHA; case counts are historical evidence, not a live acceptance claim. **Mock GitHub responses cannot count as live webhook or Vercel verification.**

### Live acceptance procedure (after account setup)

1. Confirm Vercel deployment **Ready** and anonymous HTTPS response from `GET /api/webhook`; 503 before enable must not be declared healthy. Confirm no unexpected auth/protection page. Inspect logs without secrets.
2. GitHub App Webhook **Ping** must show delivery `200 pong`. A tampered signature must be HTTP 401. Ignore a non-allowlisted repository and an untracked branch (`202 ignored`).
3. With second App installed on the hub only, set `KMONG_DISPATCH_ENABLED=true` and redeploy if necessary. Trigger a **non-destructive push** to a tracked branch; GitHub delivery should report `202 queued`. Verify a **new** central Actions run is `event=workflow_dispatch` and its execution is `SUCCESS`, 35/80/29 evidence matches expected; verify `UPDATED` or `NO_CHANGE` and the observer snapshot readback. A webhook 202 is **not** success of the collector.
4. Confirm legitimate `workflow_run:completed` from `final-blueprint-gate.yml` also queues sync. Confirm observer's own hub snapshot commit does **not** create an infinite event loop. Confirm burst handling and API failure returns 502, do not lose data or change official scores.
5. Inspect actual daily `schedule` event separately; GitHub may delay/drop scheduled events. Since no durable event delivery queue/replay store is implemented in the bridge, GitHub retry/redelivery and daily reconciliation are operational safeguards, **not** guaranteed recovery. Operational sign-off requires incident/error handling and sustained live evidence.

## Rollback

1. In Vercel, set `KMONG_DISPATCH_ENABLED=false` (or disable source App Webhook Active). Do not uninstall the already-proven source read App or delete its PEM secret.
2. The current **hourly** `cron: '23 * * * *'` and existing manual `dry_run=true/false` collector remain separate from the bridge; the schedule is best effort and can be delayed or skipped. Prior snapshot and Git SHA history remain available. Do not alter Production or workflow scheduling without owner GO.
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


### 2026-11-14: no-secret Production feature probe

The anonymous `GET /api/webhook` response includes `bridge_feature: "coalesce-v1"` in this revision, plus a public `source_sha` only when Vercel provides a valid 40-character `VERCEL_GIT_COMMIT_SHA`. The non-blocking GitHub Actions `probe-production.mjs` distinguishes an older/unknown feature from a proven `READY_SHA_MATCHED` deployment without making webhook POST requests. HTTP 200 `ready` alone never proves source parity or exact running SHA. A missing feature field indicates an older/unknown deployed build, not automatically a service outage.

### 2026-11-14: hourly budget-gated GitHub recovery schedule

- `main` collector's existing `schedule` is changed from one 11:10 KST daily scan to `23 * * * *`: one best-effort **hourly** reconciliation, to reduce potential stale snapshots while the Vercel webhook deployment is unverified. GitHub can delay or drop scheduled jobs; this is not an SLA or proof that cron actually fired.
- The existing `KMONG_SYNC_ENABLED=true` flag, 450-call App core reserve, read-only source token, central-only conditional snapshot WRITE, idempotent `NO_CHANGE`, and `DEFERRED` semantics are unchanged. If the budget guard blocks a scheduled run, no source scan or hub update occurs. No new services or credentials; the central repo is public and uses a standard `ubuntu-latest` runner.
- Expected reservation: up to 24 scheduled attempts/day **if GitHub delivers them and the existing enable flag is true**, versus one/day previously. Actual App usage, completion and absence of paid charges must be verified from run logs/billing; GitHub documentation currently lists standard hosted Actions in public repos as free.
- Confirm an actual `event=schedule` run, its `RUN/DEFERRED` status, and central observation JSON readback before stating that the recovery fallback works. Revert the cron-only change through a normal commit if API pressure or unwanted jobs are observed.

## 2026-11-15 opt-in delivery correlation candidate (feature branch only)

Two evidence methods were evaluated: (A) timestamp + bot actor matching (no new code or API usage, but ambiguous under burst dispatches); (B) an opaque GitHub `X-GitHub-Delivery` UUID passed as an optional `workflow_dispatch.source_delivery_id` and displayed in Actions `run-name` (no extra API calls or credential scope, deterministic lookup). Candidate B is implemented **only in the isolated branch** and is **off by default** through `KMONG_TRACE_DELIVERY_ID_ENABLED`. This is an audit hint, **not** proof of valid webhook delivery by itself (manual dispatch can provide the same input).

**Rollout HOLD, requires explicit owner approval:** First merge the optional input schema into the existing **main** workflow and confirm it is active. Only afterwards deploy the matching Vercel source and, separately, approve setting `KMONG_TRACE_DELIVERY_ID_ENABLED=true`. Turning on the flag before the main workflow accepts the input can cause GitHub API 422 and failed dispatch. Never use this candidate to silently change Production, Vercel configuration, GitHub App permissions, secrets or source history. Existing workflow without the flag uses its original `{dry_run:false}` input, so it remains compatible. For genuine E2E acceptance compare GitHub App Recent Deliveries (ID, signed event, HTTP response), Production SHA, trace run's actor/event/creation time, collector result (`UPDATED`/`NO_CHANGE` vs `DEFERRED`) and ledger readback; a typed-in UUID alone cannot certify a signed source.

## 2026-11-15 workflow_run path fail-closed candidate (isolated branch)

A name-only event previously fell back to `run.name = Final blueprint completion evidence gate` if both `workflow_run.path` and `workflow.path` were missing. Workflow display names are not unique; this creates an avoidable non-target workflow dispatch risk. Two approaches: A retain name-only compatibility (risks unintended cross-workflow scans), B require the precise allowlisted `.github/workflows/final-blueprint-gate.yml` or `.yaml` path from either run or workflow metadata (adopted). The run path takes precedence; if both are absent, return `202 ignored` with zero GitHub API calls. Canonical paths and HMAC, repository, branch and installation restrictions remain unchanged. This may omit an event whose GitHub webhook provides no path; hourly scheduled reconciliation remains available, and the trade-off is recorded rather than claiming zero false negatives. This code is **not deployed** and requires the existing owner approval process for merging/deployment.


### Decision: history ambiguity versus duplicate dispatch

| Candidate | Behavior on incomplete GitHub Actions history | Cost/safety | Decision |
|---|---|---|---|
| Continue and queue anyway | Fast if API is partially unavailable | May repeat a run, causing extra API usage and ambiguous receipts | Rejected |
| **Fail closed and rely on reconciling scan / owner redelivery** | Return `502` at bridge, defer internal bot scan on invalid history | Uses existing infrastructure but freshness can lag | Selected |

The two guards operate at distinct layers: bridge gate suppresses a duplicate `workflow_dispatch` request; Actions gate suppresses a redundant **collector scan** if multiple dispatches raced. Neither is an atomic lock or guarantees exactly-once processing. A `502` is not proof of an event permanently lost; automatic schedule and owner-initiated safe redelivery are separate recovery paths, with their own limits.

## 2026-11-17 isolated dispatch-history defense (PR #6, not deployed)

- The event bridge requires a complete, correctly shaped first page of GitHub Actions dispatch history. Missing `total_count`, partial short pages, absent actor/event metadata, and unordered timestamps result in safe `502 dispatch_failed` without posting another run.
- The Actions collector's own budget/duplicate gate independently rejects incomplete, malformed, duplicate-ID or out-of-order bot history and reports `DEFERRED_BOT_HISTORY_UNVERIFIED` instead of starting a scan. These checks use existing read-only API calls and introduce no new secrets/services or atomic locking claims.
- The `kmong-productization` observer-ledger push is outside the allowlist regardless of commit message, preserving loop isolation. Cases are covered by synthetic tests; the two gate layers are **not** an exactly-once guarantee. Existing hourly schedule/redelivery recovery remains best effort.
- PR #6 is on a feature branch only. Main, Vercel Production, GitHub App permissions, workflow configuration, ledger and official completion are unchanged. User GO is separately required for main/Production rollout; this document is not live deployment proof.
