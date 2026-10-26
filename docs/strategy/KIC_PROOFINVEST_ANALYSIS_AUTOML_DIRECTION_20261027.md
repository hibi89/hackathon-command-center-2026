# KIC ProofInvest — evidence-first, analysis-centered financial AI + adapted AutoML
**Decision:** USER-APPROVED DIRECTION / DESIGN-ONLY. 2026-10-27 KST.
**Scope:** ONLY KIC. PayPal Freelancer Payment Agent is UNDER USER DELIBERATION: **NO CHANGE**. UGREEN likewise unchanged.
**Supersession:** This is the newest KIC design-direction addendum, taking precedence over the narrower KIC AutoML-DEFER wording inside `docs/strategy/FINAL_THREE_HACKATHON_COMPOSITION_20261027.md`. It does **not** order premature implementation or edit the original already drafted KIC proposal, does not waive mandatory source authentication, and does not modify GitHub code.

## 1. Product outcome
One KIC ProofInvest agent that transforms **diverse, authorized, point-in-time issuer/industry evidence** into reliable, explainable corporate **financial / capital / shareholder / governance / industry** analysis. Database is support infrastructure, NOT product value. Existing Research → Verification → Risk & Reporting stays and is enriched by purpose-adapted AI_AutoML_Analyst analytical engines.

**Question answered:** "What financially and structurally changed in this company, why might the change matter, how do peers compare, and which findings are supported, disputed or not known?" This is NOT automatic stock buy/sell advice or guaranteed price prediction.

## 2. Data catalog — breadth of sources, depth of analysis
Each observation must carry `issuer_id / scope / as_of / fiscal_period / published_at / collected_at / document_id or URL / unit / transformation / evidence_status`. Ownership facts must identify the reporting person, relationship and disclosure basis. Company-published facts vs machine-derived estimates must not be conflated.

| Priority | Evidence family | Required example questions/features | Correctness caveats |
| --- | --- | --- | --- |
| **P0** | **financial statements**: revenue, operating income, profit, cash flow, liabilities/equity, liquidity, borrowing, interest burden | growth vs cash generation, debt/equity and coverage, multi-year deterioration vs recovery | CFS/OFS, interim vs annual and consolidated differences, fiscal year, restatements, KRW/units |
| **P0** | **paid equity offerings (유상증자)**: announcement, planned/actual new shares, price, proceeds, purpose, shareholder participation | percentage dilution under a specified participation assumption; working-capital/debt-refinancing vs capex purpose; pre/post number of shares | approval or proposal ≠ completed allotment; distinguish registered/paid-up, capital vs market value |
| **P0** | **bonus issues (무상증자), capital reductions (감자)** | changes in issued share count, existing-holder proportional allocation, equity reclassification vs new cash | bonus share distribution ordinarily does not inject new cash or automatically dilute proportionate ownership; price arithmetic must not be confused with value creation |
| **P0** | **major shareholder / governance**: top owner and related-party holdings, changes, disclosed large holdings | control changes, major holder participation in offerings, comparing dates and class of shares | beneficial owners vs nominal holders; report/update date and total voting shares basis |
| **P1** | CB/BW/exchangeable securities, conversion exercises and potential shares | potential diluted share count, scenarios with conversion prices/time; bounded hypothetical | potential ≠ issued; conditions and unknown exercised balances prevent exact prediction |
| **P1** | treasury stock buyback/disposal/cancellation, dividend policy | changes in treasury shares / distribution, cash affordability, shareholder-return context | buyback ≠ cancellation; reporting dates and cash availability |
| **P1** | debt instruments, maturities, refinancing, pledged shares and disclosed material governance events | solvency/capital raising interaction, covenants when publicly documented | no speculation about hidden covenants or future bankruptcy |
| **P1** | business/industry/peer group, segment reports, market share and sector context | compare peers only after same-period/scope/units and common definitions | public disclosure availability differs by sector and company |
| **P2** | material contracts, litigation, audit opinions, disclosures of significant investments, qualitative business commentary | text evidence search, timeline of structural changes and uncertainty | no sentiment-to-share-price causal claim |
| **P2** | market/valuation series where licensed and point-in-time aligned | scenario-oriented PE/PB and price vs fundamentals | not required for minimal MVP; external market price/data right checks |

**Primary candidate:** official OpenDART raw filings and structured company / finance / major-events / shareholding endpoints, official issuer IR; other KRX/market sources only where source conditions and access are verified. Check actual API availability, keys, limits, terms/redistribution, filing coverage and missing/null semantics. Public availability does not prove all reuse rights.

## 3. Architecture: adapt technology, never blindly connect two full apps
`user issuer+as_of+question → source acquisition (when authorized) → original-document/date/unit provenance gate → canonical issuer-event-feature rows → deterministic accounting/capital/shareholding calculations → conditional adapted AutoML → explanation with evidence IDs and abstention → reviewable report`.

**Reuse map:**
- `ProofInvest/proofinvest/research.py`: preserve existing point-in-time source assertions and provenance schema, extend only after actual primary source validation. Existing `risk.py` verifies structural constraints; it DOES NOT authenticate original DART.
- `AI_AutoML_Analyst/backend/app/services/profiler.py`: adapt missing/duplicate/cardinality/outlier/quality diagnostics for issuer-period-event tables.
- `AI_AutoML_Analyst/backend/app/services/automl_runner.py`, model-selection/evaluation stack: optional validated supervised modeling or peer anomaly comparison **ONLY if labeled panel is sufficiently populated**. Reuse scikit-learn/Pandas methods and tests; do not import entire FastAPI/HTML/browser/Windows sales app as KIC dependency.
- Existing AutoML supports model comparison, Dummy baseline, grouped/temporal holdout in its commercial branch, but one arbitrary CSV automatic target selection does not make a scientifically valid finance model; selection must be explicit, domain-reviewed and adapted.
- RAG_STUDIO source/quote/contradiction/abstention design remains OPTIONAL for textual disclosures, never its sales/returns/shipping-specific router.
- DBVORA schema map / safe read-only inventory, backup/restore are OPTIONAL engineering patterns if actual evidence volume requires them; standalone DBVORA is not a scientific analysis dependency.

**Data strategy:** original filings may live as authorized read-only files with hash + citation; normalized records can start as bounded CSV/JSON artifacts. Add local SQLite only when cross-company/period joins and repeated runs justify it; archive raw vs derived data separately and never push private/unlicensed data to public repositories. Do not create PostgreSQL or data warehouse infrastructure as an early requirement.

## 4. Analytical principles (the real differentiation)
**Layer A — deterministic compulsory:** calculate debt, cash, capital, dilution, maximum share counts, ownership changes, relative growth and peer comparisons with arithmetic and primary evidence. Show source, formula, base shares, assumptions, reporting date and missing values. Incomplete terms => scenario/range or UNKNOWN, not false precision.
**Layer B — ML conditional:** supervised classification/regression must have explicitly chosen, economically meaningful and reproducible target/label; enough issuer-time samples, sufficiently representative population and defensible baseline. Possibilities include *future financing stress* or *next-period financial deterioration*, but only if labels/validation can be made valid; do not hard-code financial-performance forecast or "will stock rise" as product claim. Prefer well-grounded descriptive anomaly/cluster/outlier profile when labels do not exist; do not conflate ML flags with wrongdoing or causation.
**Anti-leakage contract:** point-in-time availability (announcement dates as well as financial periods), separate issuers/groups, out-of-time validation; restatement awareness, train-only preprocessing, no future revisions/targets as features, benchmark vs Dummy/simple rules, class imbalance and calibration/uncertainty where meaningful. Publish sample counts, splits, accuracy/recall/precision or MAE as appropriate, failure cases, and unsupported conditions.
**Agent quality:** tool boundary, bounded requests, manual confirmation for uncertain events, fail-closed source issues; LLM may help extract/narrate but cannot override documented arithmetic or fabricate primary evidence.

## 5. One achievable MVP story (prelim plan / finalist code)
**Selected primary case:** "Company issues new shares while cash generation weakens and the major shareholder changes exposure." 
- User requests issuer + as-of date.
- Agent obtains permitted multi-year statement and capital increase/shareholder disclosure data.
- Shows historical cash flow and debt trend, issuance purpose, post-issue share count and conditional dilution, major-holder change if comparable primary holdings exist.
- Compares one suitable peer or prior year on matched basis.
- Produces **verified / conflict / unavailable** explanation with citations, and a side-by-side output separating fact / rule-derived measure / ML-only exploratory signal / unanswered question.
- If a legitimate multi-company multi-year training panel is absent, explicitly skips supervised ML and renders deterministic financial analysis + data-quality report. This is an accepted safe demonstration, not a failed mandatory feature.

## 6. Two implementation designs
| | A — Plug full commercial AutoML website into ProofInvest | B — Integrate a narrow analyst service/library adapted to finance |
| --- | --- | --- |
| Reuse | GUI/routes/upload/storage + original CSV engine | Reuse profiler/feature processing/model selection/evaluation/report components and tests |
| Time/cost | Larger dependency and build/test work, added browser and install burden | Lower integration cost; focus on evidence-to-analysis contract |
| Quality | Ordinary target choice and random CV can produce leakage or meaningless predictions | Correct finance target, time split and abstention explicitly implemented |
| Maintenance | Two product lifecycles/conflicting APIs | One KIC product, controlled adapter boundaries |
| Decision | **REJECT** | **SELECT**, build ONLY after protected preliminary submission |

## 7. Milestones and guards
**Now / until Nov12 10:00 KST PRELIM:** Keep the previously drafted 10-page PDF and Library originals **unchanged** until owner authorizes an exact reviewed revision. In *planning*, ensure proposal makes the new analytical value proposition, point-in-time source/data availability, clear agent workflow and realistic finalist MVP credible. KIC lead decides if a narrow PDF text change is needed, with owner exact-file approval, visual/template check and deadline buffer. Do NOT start bulk ingestion, cloud database or AutoML web-app merger before acceptance.
**If finalist from Dec3 to Dec22 10:00 KST:** 1) validate at least one real original disclosure with official source; 2) build schema and one capital-change/ownership case; 3) deliver a functioning agent with source-cited calculation and quality gates; 4) conditional trained-model demo only with valid dataset/time-split and independent test; 5) cold-start demo URL and reproducible code/documented limits.
**After competition:** expand company/industry source catalog, scheduled updates, cross-company standardized panel, robust predictive modeling, storage/index if warranted, commercial dashboard.

## 8. Required test cases
- paid offering: new shares and actual/proposed status, participation-vs-nonparticipation dilution with exact share denominator
- bonus offering: shareholder proportion remains stable under pro-rata issuance; no fictional financing proceeds
- largest shareholder percentage: period and basis mismatch => INCOMPARABLE, never delta
- CB/BW: potential dilution separate from current shares, UNKNOWN if rights terms missing
- financial reports: CFS vs OFS and restatement/time-window mismatch => WITHHELD
- ML: temporal/group leakage trap must be rejected; insufficient labels/rows => NO_TRAIN with baseline analytics available; result grounded with metrics and citations
- data ingestion: API denied/truncated/limit/error => explicit incomplete, no confident analysis
- original-filing source URL vs manually entered data metadata clearly separated

## 9. Boundaries / decision status
- Architecture selection and data-catalog expansion: **USER CONFIRMED** in 2026-10-27 conversation.
- Existing KIC `lead/kic` code / tests / PDF / source files: **NOT CHANGED by command center**.
- Underlying AutoML repository: **NOT CHANGED**; link/reuse is an upcoming implementer decision, no whole-app port.
- Official data/API, trained ML, real-world accuracy, submission: **NOT VERIFIED / NOT DONE**.
- PayPal remains **USER THINKING / UNCHANGED**. UGREEN **UNCHANGED**.
- Existing direction in FINAL_THREE_HACKATHON_COMPOSITION_20261027.md remains authoritative for **PayPal/UGREEN**; this addendum overrides only **KIC AutoML priority / research scope**.
- Source of practical capabilities: `hibi89/AI_AutoML_Analyst@feature/kmong-v1`, `hibi89/hibi89-kic-proofinvest@lead/kic`, verified by code reading (not running).
- Rule reference: https://daker.ai/public/hackathons/kic-ai-agent-competition ; OpenDART categories: https://opendart.fss.or.kr/intro/infoApiList.do
