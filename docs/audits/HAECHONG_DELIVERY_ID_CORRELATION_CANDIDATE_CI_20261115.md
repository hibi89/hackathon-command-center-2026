# HAECHONG — opt-in delivery-ID correlation candidate and CI (2026-11-15 KST)

**Mission lock:** `HAECHONG_PRIMARY_MISSION_LOCK_V1` — GitHub App signed HMAC webhook → existing Vercel → central workflow_dispatch → 35 repositories / 80 refs / 29 source products. Work remains scoped to central automation only.

## Observed issue and two designs
- **A: time + bot actor heuristics.** No code/API changes and lowest maintenance, but repeated bot runs/coalescing mean this cannot prove that a particular signed GitHub App delivery caused an Actions job.
- **B: optional opaque Delivery UUID correlation.** Append validated `X-GitHub-Delivery` to `workflow_dispatch.source_delivery_id` and expose it in the Actions run name. Adds zero GitHub API calls or permissions, small schema/test maintenance, and deterministic candidate lookup when enabled. **Selected for isolated pre-deployment implementation.** The UUID is not itself proof of source integrity (the header is not included in the HMAC body; a manual dispatch may supply an ID). GitHub App Recent Deliveries, Production logs/SHA, bot actor and actual collector/ledger evidence still must be compared.

## Source and strict compatibility
- Repo: `hibi89/hackathon-command-center-2026`.
- Isolated code branch: `feature/kmong-webhook-bounded-ingress-20261114`.
- Parent SHA: `00d779629dc874dce3c124c65dbe3fa3e9fdf238`; new code SHA: `e78a474525b548a4fb2fe9dd1148a03c357559d4` (verified as GitHub remote head).
- Changes: `services/kmong-event-bridge/lib/receiver.js`, `test/receiver.test.js`, `.github/workflows/kmong-hub-sync.yml`, `services/kmong-event-bridge/README.md`.
- `KMONG_TRACE_DELIVERY_ID_ENABLED` defaults OFF. Unless exactly `true`, input remains the original `{dry_run:"false"}`. When enabled, a strict UUID is required before any API call. `source_delivery_id` is an OPTIONAL declared workflow input in this **feature branch**, not in the deployed `main`.
- **Critical rollout sequence** (not authorized/executed): owner approves main workflow schema update, verifies active main SHA; separately approves Vercel source deploy; finally approves enabling the flag. Enabling flag before main schema update risks 422 on GitHub dispatch. No new service/app/permissions/secrets are necessary.

## Exact remote verification
- [bridge CI #43691572769](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43691572769): Node **54/54 PASS**; Python **80/80 PASS**; combined **134/134 PASS**, FAIL **0**, ALLOWLIST check PASS; source SHA `e78a474525b548a4fb2fe9dd1148a03c357559d4`.
- [blueprint gate #43691572807](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43691572807): SUCCESS at the same source SHA.
- The bridge CI's read-only public Production GET: HTTP **200**, verdict **READY_SHA_NOT_MATCHED**, source SHA **2863165b06d407ba632f18ad7a85a7c98f1989af**.
- Production deployment and live signed POST/Ping/bad-signature/nonallowlisted events/Recent Deliveries/real UUID→bot run→collector→ledger causal correlation: **NOT_VERIFIED**. Previous bot `UPDATED` and `DEFERRED_BOT_BURST` are real records but do not close the live E2E gap.
- GitHub authenticated author/committer association: `hibi89`.

## Safety and status
- `main` preserved at `69e584e57a3a37fa72b406d62ccddf9eef9dfcf2`.
- Operating branch baseline before this report: `f0ab2771bb61c936e7c0077eddf408bf44ab0491`.
- Existing Vercel project `prj_veZOkRkhMEMEA6h7PiEIl3IKcthn` access returned 404 previously; same unsupported access call not repeated. Do not infer deletion.
- No original observation ledger, catalog, product status/percentages, customer data, GitHub App credentials, permissions, deployment, Vercel project, domain or environment setting changed.
- Central evidence-based completion score **provisional 90/100 unchanged**; real signed production E2E gate is blocked pending approved access/rollout.
- Git history preserves rollback parent. This file documents **CI-verified candidate code**, not an accepted live system.

## Next step and acceptance
1. Obtain owner-approved read access to **existing** Vercel project and the source GitHub App Recent Deliveries; never create a substitute project or repeat known 404 with unchanged credentials.
2. If owner approves coordinated rollout, update main workflow schema first, then Vercel deployment, then optional trace flag; re-run actual production SHA, invalid/signature/Ping/ignored/valid push tests.
3. For each accepted signed UUID, verify GitHub App delivery event/time and HTTP response, Vercel SHA and log, trace run actor/ID/status, `UPDATED` or `NO_CHANGE` rather than `DEFERRED`, and ledger SHA. If one link is missing, mark E2E unverified and keep 90/100.

**Audit scope:** GitHub refs/source/commit author, remote GitHub Actions job logs, and public GET executed within CI. No live signed POST or Production mutation.
