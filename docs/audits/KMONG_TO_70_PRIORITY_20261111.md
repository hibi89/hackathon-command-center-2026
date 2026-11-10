# 크몽 활성 16종 70% 달성 우선순위 — 2026-11-11 KST

## Scope and baseline
- Management source: `KMONG_PRODUCTIZATION.md`, 16 active products, sum **1015%p**, arithmetic average **63.4375%** (latest recorded checkpoint from 2026-11-10). No new full customer/Windows regression across all 16 products.
- Target: all 8 below 70% reach 70% under original confirmed final deliverable criteria, **not** merely mocked-unit-test or code-file count. Required uplift **148 percentage points summed over 8**, projected average 1163/16 = **72.6875%** only **if verified targets are reached**.
- Products already at/above 70% (8) remain unchanged. Web REA Studio is excluded by owner direction; no repo deletion.

## Prioritized execution order
| Priority | Product | Current | Target | Uplift | Rationale / first gate |
|---:|---|---:|---:|---:|---|
| 1 | DBVORA | 55% | 70% | +15pp | HAE/SOVIA dependency; full-source regression and fail-closed local observability |
| 2 | Coin Pattern Analyzer | 50% | 70% | +20pp | Direct Kmong monetization; arbitrary user-defined formula support + actual Windows DB sample validation |
| 3 | RAG Studio AX Edition | 55% | 70% | +15pp | Private SMAX PREP approval boundary; actual schema/ingestion E2E |
| 4 | SMAX² | 50% | 70% | +20pp | Reusable PREP/SELF connector; native full parser and business report E2E |
| 5 | Astra PDF Redesigner | 52% | 70% | +18pp | Standalone document product; STEP 5/7 and package/visual regression |
| 6 | EAI | 50% | 70% | +20pp | Shared AI engine; Windows/Qwen/Ollama/SearXNG reality and safe local I/O |
| 7 | AXMART PC CARE | 50% | 70% | +20pp | Windows/USB/WinRE hardware access dependency, safety validation |
| 8 | AXMART³ CUBE | 50% | 70% | +20pp | Product platform payments/account/download/after-sales complexity, no production mutation yet |

## Two execution strategies considered
- A, standalone sales-first: prioritize coin pattern analyzer then Astra PDF. Faster path to commercial packages, low ecosystem leverage and still blocked by end-user QA/licensing.
- B, dependency-first (selected): harden DBVORA, then coin pattern analyzer and RAG/SMAX. Better reuse and lower cross-product rework; DBVORA's archive safety and customer database boundary make its 70% milestone harder than a simple P0 bug fix.
- No paid CI, real customer data upload, external DB credentials, automatic deletion, new repo, public branch promotion, main/production rewrite or release approval is inferred from this plan.

## Executed work in this turn: DBVORA P0-08
- Repo `hibi89/DBVORA`, private `feature/p0-db-map`; code commits `0518269d8b1686f4dae686ebaec358eca41a4a7d` and `9d1d4b0898c5293f34f01feff4894c5ed97aabb1`; gate/doc HEAD `098d027e7475392b2d789a25accd51d4b3cc4832`.
- Generated HTML/JSON partial-write cleanup by filename+device/inode fail-closed rule; integrated new tests declared and release-gate required files/expected Python discovery **324→336**. No main/develop/production/customer data touched.
- Exact tested cleanup helper blob `060b48cde0b1cdd5ddd8bc3559ae48cfa6caa210`; local isolated Linux Python **7/7 PASS**, 0 FAIL, isolated syntax PASS. New 5 full-source SQLite publication tests, current >=336 suite, native Windows, Node DOM/real browser, power-cut **NOT RUN**. P0-08's cleanup is best effort, not crash-atomic two-file publish.
- **No % uplift credited. DBVORA remains 55%, other 15 unchanged, 16-product average 63.4375%, RELEASE HOLD.**
- Next: authorized complete checkout verify targeted publication+storage tests then full release gate; fix observed failures. Source evidence in `hibi89/DBVORA/docs/P0_08_PUBLICATION_RECOVERY_20261111.md`.

## Commit/rollback policy
Use existing independent feature branches only; maintain source and customer data. Verify SHA, author/committer and CI at each major milestone. Stop and pivot after unrecoverable repeated environment failures; no false PASS. New evidence required before raising %.

## 2026-11-11 KST — after P4, priority #2 Coin Analyzer provisional 65%
- Previous priority table above is the **starting baseline**. Coin Pattern Analyzer: **50→65% provisional** based on canonical P1/P2 shared-DSL single/multirule search, P3 five customer template patterns, and P4 unified CLI + offline HTML reporting. Code SHA `33ed7ae00341016b8c6e42a43eb0f6d610e0b742`. Product 70 remains **5pp away**, not marked complete; required true P4 P1/P2 E2E four and full regression remain NOT RUN, Windows/real 3.6GB DB/EXE/license HOLD.
- Isolated P4 CLI dispatch (mock) 8 + actual safe report 13 **21/21 PASS** at exact newly pushed blobs; separate prior P1/P2/P3 36 PASS, distinct Git SHA. The experimental independent batch Draft PR #1 remains unmerged to avoid duplicate rule DSL.
- Current active-product arithmetic = earlier 1015%p +15%p = **1030%p** /16 = **64.375%** provisional. Do not rewrite earlier historical 50% baseline or count old draft code in final-product ratio. Actual 70 requires same-SHA acceptance. Original customer data, main, release unchanged.
