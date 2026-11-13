# Kmong hub webhook branch-coverage audit — 2026-11-13 KST

> **Result: CONFIRMED EVENT-TRIGGER GAP / NO CONFIRMED MISSING SNAPSHOT DATA.** This is a read-only audit. No code, GitHub App permissions, webhook secrets, Vercel project/deploy, Actions schedule, central observation JSON, product statuses or registration history were modified.

## 1. Evidence base and scope

- Central repo `hibi89/hackathon-command-center-2026`, trusted `main` analyzed at `546498f78a7389f81a4bf37d35fe3a39341d1637`. Source allowlist `tools/kmong_hub_sync/source_repositories.json` blob `e40f71b05d5c8a2dcaba204450d3ec368df2e4f5`; deployed-code source `services/kmong-event-bridge/lib/receiver.js` on same main.
- Latest-read product index `kmong-productization/data/final_blueprint_product_index_20261113.json` blob `05805c495c4ee91828b516b1bf5396b88b881cfd` containing 29 product-to-repository/branch references.
- Latest-read `kmong-productization/data/kmong_hub_auto_observations.json` blob `1a1714f95335fbf6121bfa6fa9a2301d45384283`; summary 35 source repositories, 70 explicitly rostered refs, 29/29 current snapshot product refs PRESENT, 0 fingerprint alerts.
- In the receiver, `ALLOWLIST` is derived ONLY from the 35-repository source roster: allowed branches are `main` plus `item.branches`. Both `push` and relevant `workflow_run` events are rejected for branches absent in this map. Product index is not imported by receiver.
- Cross-joining the 29 product refs with the receiver's exact branch allowlist yields **19 eligible and 10 NOT_ELIGIBLE** product references. These 10 can still be collected by full repo scans from other allowed events / manual dispatch / cron; they cannot initiate a collector on their own branch event.
- At the time of a separately executed live SHA check, **all 10/10** unallowlisted product refs had exactly matching current GitHub ref SHA and observation JSON product SHA. Thus there is **no evidence of stale or lost data now**. This is not proof of prompt/event-level completeness in future.
- This audit adds no manual `workflow_dispatch`. [Run #43391524004](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43391524004) and [#43391557763](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43391557763) both completed SUCCESS, 26/26 Python tests each and `UPDATED` respective hub snapshots at `4ab24d4ad766e65be62586929356c6740b5e226d` and `d9775b5d0064044a56490264b7dfedb1c15780e0`. They do not prove that every product branch triggers.

## 2. Ten product refs not eligible to trigger a standalone webhook sync

| Product ID | Repository | Product-tracked branch | Current receiver event eligibility |
|---|---|---|---|
| `ACTIVE-01` | `hibi89/candle_scraper` | `feature/kmong-collector-p95-delivery-integrity-20261112` | `NOT_ELIGIBLE` |
| `ACTIVE-05` | `hibi89/data2web_studio` | `feature/final-blueprint-p85-evidence-20261113` | `NOT_ELIGIBLE` |
| `ACTIVE-07` | `hibi89/SOVIA_sovereign` | `feature/kmong-la-review-p2-20261112` | `NOT_ELIGIBLE` |
| `ACTIVE-12` | `hibi89/RAG_STUDIO` | `feature/p546-rag-prep-mapping` | `NOT_ELIGIBLE` |
| `ACTIVE-13` | `hibi89/astra_pdf_redesigner` | `integration/astra-commercial-core` | `NOT_ELIGIBLE` |
| `ACTIVE-14` | `hibi89/candle_scraper` | `feature/coin-pattern-p85-forward-eval-20261112` | `NOT_ELIGIBLE` |
| `ACTIVE-15` | `hibi89/EAI` | `feature/kmong-eai-85-p31-20261112` | `NOT_ELIGIBLE` |
| `ACTIVE-16` | `hibi89/AX_MART` | `feature/pc-care-p15-p18-85-20261112` | `NOT_ELIGIBLE` |
| `CANDIDATE-04` | `hibi89/factory-ax-ecosystem` | `feature/data-verify` | `NOT_ELIGIBLE` |
| `CANDIDATE-10` | `hibi89/Freelancer` | `product/bid-ax-public-procurement` | `NOT_ELIGIBLE` |

> Count: **ACTIVE 8**, **CANDIDATE 2**, total 10. The separate roster's fixed 35 extra branches are not the same set as the 29 product references.

## 3. Root cause and risk

- `source_repositories.json` was designed as a fixed 35-main + 35-extra branch collection roster. In contrast, `final_blueprint_product_index_20261113.json` references product delivery branches independent of that roster. The collector intentionally fetches product refs even when outside the explicit 70, which is why the snapshot correctly shows 29 PRESENT.
- The receiver's event allowlist is **not** the union of product index refs; its eligibility filter remains frozen in an earlier static 70-ref set. Consequently, updates only on these 10 excluded branches will be ignored at webhook intake and will not cause immediate sync on their own. The daily `10 2 * * *` scheduled fallback has **0 observed real schedule runs** at this audit and cannot be treated as proven protection.
- This is an **availability/observability gap**, not an observed unauthorized write or current corruption. Independent risk: rapid allowed-event bursts currently show 1-running/1-pending Actions concurrency queue replacement; this can coalesce latest-state refreshes but does not provide exactly-once history.

## 4. Two minimum-change remediation designs (both REQUIRE owner approval before implementation)

### Option A — extend the shared source roster to cover all product refs (recommended)

1. Update `tools/kmong_hub_sync/source_repositories.json` to add exactly the 10 missing product refs (without removing or changing existing refs). Rebuild the bridge's mirrored roster `services/kmong-event-bridge/source_repositories.json`.
2. Adjust `tools/kmong_hub_sync/sync.py` pinned inventory expectations from 35 additional branches to 45, and tests: Python roster/snapshot assertions 70→80; Node bridge allowlist count 35→45. Add **cross-file regression test** that all 29 product index refs are in the source allowlist; fail CI on future drift.
3. Keep existing source-only read App, dispatcher hub-only Actions App, HMAC/installation checks, own `kmong-productization` snapshot feedback exclusion, readback/optimistic blob SHA, and cron unchanged. Dry-run first, verify on fixed SHA, then one approved production deployment and legitimate event E2E check.
4. **Tradeoffs:** single shared source of truth, simpler runtime, little or no extra distinct ref lookups because 10 product refs are already fetched/cached by the collector; explicit `tracked_branch_count` changes from historical 70 to 80. Requires source/test edits, CI, and **approved Vercel redeploy**; changes 35+35 original roster structure and thus requires policy acceptance.

### Option B — keep collector's 70 refs and add a separate product-webhook allowlist

1. Snapshot the exact 29 product refs into a *second* version-controlled allowlist consumed by receiver, leaving collector's 35+35 roster and 70-ref report intact.
2. Add a CI guard comparing the second allowlist with the canonical hub index at an exact reviewed SHA; require update/redeploy on new product branch. Receiver remains fail-closed for unknown branches; no new privileged tokens or data writes.
3. **Tradeoffs:** preserves existing collector output/test inventory and avoids extra scans, but creates a second artifact to maintain, potential synchronization/drift risk, and still requires tested code changes plus **approved Vercel redeploy**.

**Do not** simply accept all branches in 35 repositories: this expands event load, triggers more wasted dispatches, and dilutes review scope. **Do not** introduce in-memory debounce as a guarantee of durable duplicate suppression; cross-instance replay would remain.

## 5. Acceptance tests / gates

- Unit test: every product tracked branch eligible; out-of-roster repository/tag/restricted central observation branch remain blocked; relevant allowed `push` and specific `workflow_run` accepted; signature/installation/size caps unchanged.
- Python unit tests + Node receiver tests PASS at exact GitHub SHA; one dry-run snapshot; readback preserves official `UNASSESSED` and immutable registration history.
- Validate actual Vercel Production SHA and one legitimate source branch event after approved release; confirm Actions dispatch, 29 refs present and a subsequent NO_CHANGE; detect unintended feedback/dispatch bursts.
- User approval required for changing the 35+35 roster, real workflow behavior and Vercel redeployment. No automatic PR merge/production modification authorized by this document.

## 6. Ten-part handoff

1. **Goal and scope:** fix the mismatch between collector product coverage and event trigger coverage while preserving source-read/dispatcher-write split.
2. **Completed:** 29-vs-70 static audit, ten missing trigger refs, ten direct SHA-vs-snapshot equal observations. No code changes.
3. **Tests:** pure data cross-join 29 products: 19 eligible/10 missing. Remote live-ref 10 comparisons: 10 matches/0 mismatches; prior Actions #43391524004/#43391557763 26 Python PASS each. No new local Node/Python or Production tests.
4. **Current:** P1 gap confirmed; P2 schedule unverified; P3 no known product snapshot corruption; P4 product scoring remains 29/29 UNASSESSED.
5. **Failure/evidence/pivot:** receiver's fixed allowlist excludes 10 refs. Option A/B above, each requires user approval. No repeated pointless dispatch.
6. **Source SHA/paths:** main base `546498f78a7389f81a4bf37d35fe3a39341d1637`; roster blob `e40f71b05d5c8a2dcaba204450d3ec368df2e4f5`; index blob `05805c495c4ee91828b516b1bf5396b88b881cfd`; snapshot blob `1a1714f95335fbf6121bfa6fa9a2301d45384283`; branch heads are concurrent and may change. Refresh before implementation.
7. **Production:** `https://kmong-hub-event-bridge.vercel.app/api/webhook` as recorded; Production SHA/runtime not independently revalidated in this audit. Commands: Python `python3 -B -m unittest discover -s tools/kmong_hub_sync -p "test_*.py" -v`, Node `node --test services/kmong-event-bridge/test/receiver.test.js`.
8. **Source/backup/security:** old main and kmong HEADs preserved; never change GitHub App permissions, secret or source product repos without approval. Do not reveal credentials.
9. **Next steps/acceptance:** obtain approval for A (preferred) or B; code + tests + review before authorized deploy; check next real cron event 2026-11-14 11:10 KST.
10. **KST/time/source:** 2026-11-13 after 17:15 KST; read-only GitHub refs and latest hub snapshots, Actions log; documentation baseline commit requires readback.
