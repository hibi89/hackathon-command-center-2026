# GitHub Actions native schedule missing — read-only escalation evidence

**Verified:** 2026-11-14 19:10 KST. **Scope:** `hibi89/hackathon-command-center-2026`; workflow ID **416801860**; `.github/workflows/kmong-hub-sync.yml`. This is a diagnostic record, **not** a claim that GitHub has accepted a support ticket.

## Verified facts

- Repository metadata: PUBLIC, not archived, not disabled; default branch `main`, SHA `69e584e57a3a37fa72b406d62ccddf9eef9dfcf2` (main last commit at **14:10:59 KST**, after the cron change).
- Workflow YAML exists on `main`: `schedule: - cron: '23 * * * *'`. It also has `workflow_dispatch`; job is guarded by `vars.KMONG_SYNC_ENABLED == 'true'`, but a false job-level `if` would still leave a workflow run, unlike the observed zero runs. Actual workflow state **NOT_VERIFIED**.
- Last cron edit `f4d8cbe42a4e3dd6db62ba6792c61a1414e0bbc9`, recorded **2026-11-14 12:32:27 KST**; linked GitHub author & committer both `hibi89`. Connected account profile also reports `hibi89` active for API calls; this reduces, but does not eliminate, concerns about scheduler actor access/state. We cannot read the scheduler's stored actor identity or status.
- Exact GitHub REST `GET /repos/hibi89/hackathon-command-center-2026/actions/runs?event=schedule&per_page=20` returned **HTTP success, total_count=0** at **2026-11-14 19:07+ KST**. No schedule run ID, timestamps, conclusion or jobs. Slots 13:23 through 18:23 KST have occurred since the cron change; 18:23 is already ~44 minutes old at that read. This is evidence of **unobserved scheduled events**, not proof of whether GitHub internally queued or dropped them.
- Manual/bot dispatch works: [#43580833312](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43580833312), 18:30:06–18:32:19 KST, `event=workflow_dispatch`, bot actor `kmong-hub-dispatcher[bot]`, COMPLETED/SUCCESS, `RUN` preflight 5750/450, **80 Python PASS**, `UPDATED` 35 repositories/80 refs/29 products/0 unlinked/0 fingerprints; owner official scores unchanged. A separate 18:25 bot [#43580489725](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43580489725) also succeeded, but both were dispatch events, not schedule.
- Latest 18:30 observation blob **`3efabbd4a9df2e97e2590cfa8a98cb78b5083a22`** has 35/80/29, 0 fingerprint issues, 0 unlinked refs. Four actively edited products are point-in-time observations and can later drift.
- Attempted GitHub API `/actions/workflows?per_page=100` and `/actions/permissions` through connected GitHub tool: **400 connector allowlist error**. This does **not** prove a disabled workflow or insufficient GitHub permissions. GitHub API workflow state `active` / `disabled_*` and registered scheduler actor remain **NOT_VERIFIED**.
- [GitHub official status page](https://www.githubstatus.com/) reported Actions Operational / no incidents for November 14 at the time checked; this does not rule out a repository-specific scheduler issue. [GitHub troubleshooting docs](https://docs.github.com/en/actions/how-tos/troubleshoot-workflows) confirm that cron can be delayed/dropped and may stop when the scheduler's associated actor is suspended, deleted or deprovisioned. [Other November 2026 community report](https://github.com/orgs/community/discussions/212519) describes same zero-schedule/run distinction, but is **not** proof of this repository's cause.

## Remaining diagnostics (read-only first)

1. By a permitted GitHub interface or GitHub Support, inspect **workflow ID 416801860**, path and `state`; capture whether it is `active` or `disabled_*`, and check whether scheduled event registration exists.
2. Inspect associated scheduled **actor identity / account status** in GitHub's authoritative scheduler (connected public GitHub author does not prove backend actor state).
3. If state and actor are valid, request GitHub Support investigation of schedule registration or event creation, providing zero-run API, exact cron edit SHA, last main push, and successful manual dispatch run above.
4. After an additional hour, requery `event=schedule`; do not treat old manual dispatch success as scheduled recovery.

## Change options and boundaries

- **A — current recommendation:** keep existing working dispatch/collector and monitor hourly schedule read-only. No extra Actions cost, minimal risk, but missed periodic reconciliation remains possible.
- **B — conditional after root cause or explicit approval:** owner-initiated GitHub workflow re-enable / cron edit to refresh registration; requires GitHub-authorized UI/commit and could change actor. Do not perform without verification and user consent.
- **C — architectural durable replay queue:** prevents some missed follow-on changes, but adds storage/coordination/API costs and changes operational behavior; separate design and approval required.

**No claim of completed native schedule, signed webhook 2-delivery E2E, Vercel Production SHA, commercial release, or 100% final-blueprint acceptance.** No cron, token, permission, source code, original data, synthetic buyer status, or ledger manually changed in this diagnostic.

## Reusable GitHub Support description

`Public repository hibi89/hackathon-command-center-2026, workflow ID 416801860 at .github/workflows/kmong-hub-sync.yml, default main. Since linked-user cron change f4d8cbe42 (2026-11-14 12:32 KST) to 23 * * * *, 6 :23 slots passed but GET actions/runs?event=schedule returns total_count 0 through 19:07 KST. Manual workflow_dispatch #43580833312 succeeds, all jobs green (80 tests, updated 35/80/29). Please check whether the workflow is registered/active for schedule, what actor GitHub stores for its schedule, and why no schedule events are being created. We have not changed cron again. Exact main SHA 69e584e57a3a and repository is public/non-archived.`
