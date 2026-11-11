# Kmong <85% urgency TOP3 — 2026-11-11 KST

**Scope:** 16 active projects from the canonical roster, not older 17-product snapshot. Provisional completion percentages are subjective product scope estimates, not release authorizations. User asked to start TOP1 without interfering with other owner chats.

| Priority | Product | Before this work | After this work | Why urgent | Blocker |
|---|---|---:|---:|---|---|
| 1 | HAE | 70% | **73% provisional** | Ecosystem workflow core, Windows/Linux CI regressions; impacts dependent products | Old checked-in bundled artifacts incompatible with current source, Windows path/junction regressions, full CI FAIL; real DBVORA/OAuth absent |
| 2 | SMAX² | 70% | 70% | Local PREP→SELF standardized source/quality prerequisite for wider customer products | Separate feature and original preprocessing branches, real Native full test and UI E2E unverified |
| 3 | RAG Studio AX Edition | 70% | 70% | Customer-facing local intelligence product with cross-product SMAX ingestion value | True private SMAX mapping integration and customer/Windows acceptance unverified |

**Chosen work:** HAE branch `feature/axflow-mvp`. Changes: safe diagnostic ASCII escaping for Korean paths on cp1252, exact fail-closed port collision contract, and opt-in synthetic-only SQLite schema/FK metadata inventory+CLI. No actual DBVORA API or customer DB access. Unit tests **14/14 Linux PASS**. Exact source code SHA `4f19b367f0573a553b0f89965dca7fab32a5c09d`, documentation HEAD `2a1d90fd4db480cb7d88645ade43420186aaa5ae`. Full Windows+Ubuntu GitHub Actions [42972148842](https://github.com/hibi89/HAE/actions/runs/42972148842) **FAILURE**; release HOLD. Goal 85% not met and cannot be claimed from isolated tests.

All other 13 items below 85 retain previously audited scores; none is declared released. Canonical after-sync 16-product sum 1166%p and mean 72.875%, 15 products <85 and one 94%; all 16 >=70. End-of-task central updates are manual, not automatic.
