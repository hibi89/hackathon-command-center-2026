> **2026-10-27 LATER PRODUCT-PLATFORM REFINEMENT / OWNER INSTRUCTION:** BID OWL is being repurposed **on a new existing-repo branch** as **Disclosure Lightning** (the word "Lightning" means fast; NOT "Lightening"): authorized official SEC EDGAR filings discovery/fetch/amendment and source-provenance, to supply KIC ProofInvest Global. See private `hibi89/Bid_Owl@feature/disclosure-lightning/DISCLOSURE_LIGHTNING_BLUEPRINT.md`. **One separate universal Data Preprocessor** is a user-planned explicit exception to previous no-new-projects priority; it cleans/standardizes/quality-checks SEC/DART/PDF/CSV/DB without pretending to create a new repo here. Pipeline: official SEC EDGAR → Disclosure Lightning raw immutable indexed filings → independent Data Preprocessor normalized quality-gated facts → KIC ProofInvest Global verified finance/capital/ownership + ML/DL. Existing `Bid_Owl@main` and `feature/bid-owl-v1-basic-mvp` preserved; **no GitHub repo rename actually performed**, no live SEC requests or code implementation claimed, no KIC original code/PDF changed; owner may rename existing Bid_Owl repository through GitHub Settings when desired. Public KIC must not copy private Bid Owl code absent explicit owner licensing and publication decision. SEC published fair-access guidance limits aggregate requests to <=10/s, not evasion. PayPal/UGREEN products unchanged by this refinement.

# KIC — PROOFINVEST 2.0: FINAL BUILD BLUEPRINT
**Status:** FINAL USER PRODUCT DIRECTION, IMPLEMENTATION NOT YET ACCEPTED. Owner: KIC lead on existing `hibi89/hibi89-kic-proofinvest@lead/kic`. Parent coordination: [Master](THREE_HACKATHON_MASTER_20261027.md). Product name unchanged. This file supersedes narrower optional-ML position of old `FINAL_THREE_HACKATHON_COMPOSITION_20261027.md`; existing [data-source & AutoML details](../strategy/KIC_PROOFINVEST_ANALYSIS_AUTOML_DIRECTION_20261027.md) remain valid unless contradicted.
**Product claim:** "Public, permitted company/industry disclosures → verifiable Research/Verification/Risk → human-readable, point-in-time financial/capital/shareholder change analysis → complementary ML on structured history and pretrained deep-learning extraction of original filing language." This is an institutional analyst copilot, **NOT** an auto-buy/sell agent, guaranteed financial forecasting tool or an end-to-end self-training LLM.

## A. Product user and differentiator
A research analyst enters issuer, analysis as-of date, target questions (e.g., paid offering and controlling-shareholder dilution), peer group if requested. Product collects only legally accessible trusted data, normalizes numeric evidence and text and produces a report separating (1) documentary fact, (2) transparent calculation, (3) exploratory ML risk signal, (4) deep-learning-supported text extraction, (5) conflict/unavailable. The differentiator is **temporal provenance + capital structure events + reliable cross-source argument**, not that multiple algorithms run.

## B. Complete data catalog
P0 (minimum): identifiers (corp/issuer ID, filing ID), annual CFS/OFS, period and corrected filing; financials (sales, operating profit, net profit, liabilities, equity, operating cashflow, cash, borrowings); paid equity offering events (decision vs actual allocation, original/new shares, offering price, funds and purpose, controlling shareholder participation); bonus issues and capital reductions (distinguish no incoming cash); largest shareholder and specially related holders' reported shares/% and date; company and peer basics.
P1: CB/BW/exchange rights + potential shares, stock buyback/cancellation, dividends, debt maturity, public large-holding changes, material contracts, industry segment/competitor statements, corporate actions and public controversy.
P2: licensed market price/valuation series, external articles, complex filings/embeddings and extended multi-market coverage.
**Source path:** First-party OpenDART disclosures and structured endpoints, issuer investor-relations primary PDFs, then duly licensed/retrievable industrial/market references. No unstated guarantees for which endpoint returns each field. Every fact records `entity_id, source_id, URL, disclosure_id, publication_time, collection_time, as_of, fiscal_period, CFS/OFS, unit, status, content_digest, rights_status`. For share figures add `base_outstanding_shares, new_shares, investor_participation, voting_basis`. Unavailable/ambiguous means WITHHELD, not zero.

## C. Pipeline / integration contract
```text
Issuer + As-of + Question
  -> Research agent: official evidence candidate discovery + document/issuer/period tracing
  -> Verification agent: original source identity, revisions, period, units, CFS/OFS, ownership/share denominators
  -> Normalized event/fact snapshot: fact|source|status|confidence_basis (confidence cannot fabricate provenance)
  -> Deterministic financial/capital analyzer:
        solvency/cashflow trends, planned-vs-actual offering status, shareholder dilution scenarios
  -> Conditional numeric AI_AutoML_Analyst adapter:
        profiling/outlier or supervised model if legitimate labels & enough issuer/time samples
  -> Document semantic DL adapter:
        pretrained financial-language encoder/transformer for extraction & evidence retrieval;
        original quote validated by deterministic provenance checks / manually labeled cases
  -> Risk agent and report agent:
        evidence-backed facts + formulas + contextual judgment + model signals + unknowns
```
- **ML** adapt `AI_AutoML_Analyst@feature/kmong-v1`: `profiler.py`, `automl_runner.py`, `model_selector`, train-only preprocess, Dummy baseline and model comparison, time/group-aware holdout, reporting components. Do not import its customer FastAPI storefront or arbitrary CSV target suggestion. Start with safe descriptive profiles; supervised financial-stress/outcome labels only if economically meaningful. Never label future outcomes on post-event features. Disclose holdout counts, MAE or PR/recall as appropriate, calibration/coverage if claiming likelihood. Insufficient samples => `NO_TRAIN` and deterministic analysis still runs.
- **Deep learning** use an appropriately licensed pretrained text model (Korean-language filing handling and latency evaluated), embeddings/semantic retrieval + bounded structured fields such as `capital_raise_purpose`, `execution_status`, `risk_factor_text`, `source_span`. Large model use or an embedding call alone does not prove task-specialized accuracy. Evaluate precision/recall or exact evidence extraction on human-labeled issuer filings, require source spans and contradictions flag. No from-scratch expensive training. Model family chosen after real test, not prematurely hard-coded.
- **Improvement loop** append new authorized disclosed outcomes, maintain dated dataset/version and original model artifacts, re-train offline only on approved schedule, compare independent out-of-time score and calibration vs incumbent; approve new model only if better, otherwise rollback. This is auditable improvement, NOT unchecked self-modifying continuous learning.
- **RAG_STUDIO** optional provenance/text retrieval design only. **DBVORA** not required; start artifact JSON/CSV and file hashes, SQLite only on actual multi-issuer/period join need. Disclose source/provider usage rights.

## D. One persuasive end-to-end case
A target company reports worsening operating cashflow and an announced paid offering; the largest shareholder's holding changes and possible CB conversion is visible.
1. Verify actual filing versions and whether share issuance was only announced or completed.
2. Calculate ratio of offered shares to existing shares; if nonparticipant shareholding 10% of 100m original shares, 25m new shares means 8% pro forma (assuming no purchase), **scenario not forecast**.
3. Compare operating cashflow, gross debt and dilution against primary records. Bonus offering is treated as proportional allocation and no automatic value creation.
4. Show document extractor's original source sentence and label, not just a prose LLM opinion.
5. If time-series and peer labels sufficient, show ML exploratory signal plus last-date holdout; otherwise mark `ML_SKIPPED: DATA_INSUFFICIENT`.
6. Produce executive 1-page finding + drill-down references, conflict/unknown and alternatives.

## E. Data interfaces (logical, not database mandate)
`Source`: id/uri/disclosure/time/hash/license; `Fact`: metric/value/unit/period/basis/status/source_id; `CapitalEvent`: kind/status/terms/shares/proceeds/participation; `OwnershipSnapshot`: holder/class/shares/denominator/disclosure date; `Extraction`: doc/span/model/version/human_review; `AnalysisRun`: as_of/input_hash/fact_ids/ML_version/DL_version/result/review. Derived values never written as if first-party facts. Link source hashes into report.

## F. Tests / acceptance
- Bad missing/no source, future source and input lookahead, duplicate source URL => refused.
- Mismatched CFS/OFS, periods, currency, share base, ownership reporting date => explicit INCOMPARABLE.
- Paid offering: shareholder participation assumptions vs nonparticipation, planned/actual status.
- Bonus issuance no automatic capital inflow or old-holder percentage dilution.
- CB rights potential vs issued; correct missing terms.
- Offline ML temporal leakage and cross-issuer groups, dummy/simple rule baseline; no labeled panel => NO_TRAIN, not fake model score.
- Deep-learning source text: compare to curated finite manual labels and measure extraction accuracy, non-source explanation => WITHHELD.
- One official first-party source identity/actual OpenDART with rights and reproducibility **before claiming live product**.
- Public finalist demo URL responsive, read-only safe, screen/README test reproducible; no real-money trade.

## G. Stage gates
**Now→Nov12 10:00 KST:** protect existing private KIC proposal. Update exact PDF only after user approves rendered file, ensure official 7 headings and <=10 pages. Tell concise story ML+DL used for separate defensible tasks, realistic sample-driven performance validation rather than "infinite learning". DAKER team leader final conversion and actual receipt user-gated.
**If finalist Dec3→Dec22 10:00:** real official issuer ingestion, complete P0 event & ownership case, computed explanations, pretrained extractor offline test, conditional AutoML on genuine labeled panel (or honest no-train), working demo URL/code/PDF. Prioritize sample fidelity and legitimate source disclosure over breadth. Do not promise financial prediction precision until measured.
**Post-contest:** more issuers/industries, labeled temporal panel, model registry/drift, append-only eval, DB joins/observability.

## H. What actually exists as of last evidence
KIC code `proofinvest/research.py` and `risk.py`, `evidence_scenarios.py` include local/offline/source-status checks and manual issuer figures; previously verified 254/254 offline tests at related Oct25 SHA. This **does not mean** live OpenDART, new shareholding ingestion, trained ML, DL extraction or final PDF/DAKER submission exist. Future execution/commit belongs only to the KIC lead.
