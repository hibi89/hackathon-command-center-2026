# PAYPAL — AI WORK MARKETPLACE: FINAL BUILD BLUEPRINT
**Status:** OWNER-REQUESTED FINAL PRODUCT ARCHITECTURE / NEW SOFTWARE NOT CLAIMED. Existing application repository `hibi89/hibi89-paypal-ai-hackathon@lead/paypal` remains; retain its original safe payment modules and historical files. This document supersedes original single-freelancer agent *product positioning*, not its payment/authorization contracts. Parent: [Master](THREE_HACKATHON_MASTER_20261027.md).
**Promise:** Global two-sided service-project marketplace: a client describes work, AI structures needs and ranks suitable opted-in talent, transparent data analysis provides **reference** prices, humans negotiate and accept the quote, actual PayPal Sandbox checks out, SOVIA-style audit and DBVORA operations track trust and data integrity. No unlicensed claim of "all PayPal users available" or multi-seller PayPal approval.

## A. Core actors and one case
- **Client:** country/language/project scope/deadline/budget, accepts skill and pricing disclosures.
- **Talent:** self-registers with explicit consent, supported country/payment onboarding, skills/portfolio/availability/requested rate. Identity/skill verification separate from marketing claims.
- **Operator/admin:** manages abusive listings, audit views, retention and disputes without unilateral payment authority.
- Demo: authorized synthetic client creates e-commerce mini project, matches 3 synthetic opted-in freelancer candidates, sees AI comparison and reference price with transparent data quality label, approves seller/amount, PayPal Sandbox buyer actually approves order, safe backend reads provider capture, event ledger shows seller-linked receipt. This is ONE end-to-end product demo (not slides pretending transactions).

## B. Product workflows
```text
Client project intake
 → LLM converts narrative to typed structured skills, deliverables, time, currency, budget constraints
 → interactive follow-up only for essential missing fields
 → consented freelancer profile search (skills/language/country availability, deterministic filters)
 → candidate rerank (hybrid deterministic + optional ML if lawful outcomes)
 → transparent match explanations and contraindications
 → price analyzer: verified similar completed-contract dataset / supervised ML if data sufficient,
     otherwise rule-based published references with sample counts or "insufficient comparable data"
 → human freelancer/client negotiation (offers and quote versions, milestones)
 → owner explicit approval of merchant, quote version, amount and currency
 → authenticated durable session + D1/SQLite duplicate-claim
 → PayPal Sandbox create order → genuine buyer approval → capture → server GET reconcile
 → SOVIA audit event trail (retrospective), DBVORA read-only topology/recovery observability
 → contract/delivery/complaint/refund/dispute records (records only at first; actual refund requires approval)
```
AI does not autonomously release/capture/refund funds or claim payment from a URL redirect.

## C. Price intelligence (this must be honest)
- Structured features: task domain and complexity, features/deliverables, deadline, skill requirements, region/currency, experience tier, hours if independently reasonable, contract scope, negotiated terms and date. Preserve country/currency exchange-rate timestamp when doing normalized comparisons.
- **Label choice:** negotiated **contracted price** and, separately, final **paid/settled amount**; exclude cancelled contracts from a naïve completed-price distribution but retain for bias analysis. Never train on a seller's initial asking price and label it executed transaction value. No other users' PayPal payments; only lawful consented marketplace transactions and external appropriately licensed aggregates.
- **ML:** repurpose `AI_AutoML_Analyst` scikit-learn preprocessing/regression, baselines, group/time split and model evaluation, not customer web app. Model comparison by category, cold-start backoff to transparent comparable cases. Median/quantile or conformal intervals only when held-out coverage validates them; never advertise 80% confidence without actual statistical coverage. Log absolute error, category bias and coverage; retrain offline with evaluation & human gate.
- **Matching:** deterministic eligibility filter before AI rank, explain match by skills/experience and deadlines, missing profile or identity info disclosed. Optional learned ranker only with sufficiently sized unbiased feedback; no fabricated success rates/100%-matching displays. Avoid discriminatory protected-attribute inference.
- **MVP price output:** for synthetic demonstrator show `SYNTHETIC_EXAMPLE` and label no observed-market baseline; if lawful market comparator is available, show provenance, counts and limits. No fabricated "global big data".

## D. Transactional DB & data contracts
**Payment authority:** existing Node JS secure payment logic; `src/pilot_checkout_session_store.mjs` local `node:sqlite` for dev/prototype, `migrations/d1/0001_payment_claims.sql`, `src/d1_claim.mjs`, `src/d1_recovery.mjs` for Cloudflare D1 adaptation. **Deployment and true Cloudflare D1 runtime not verified; D1 and node:sqlite are NOT plug compatible.** Prefer actually validated store over speculative migration. Database PK/unique constraints and strict approved-quote/merchant binding are mandatory; cloud/runtime changes require separate QA.

Logical entities (field lists illustrative not existing implemented schema):
| Entity | Critical fields/relations |
| --- | --- |
| users | internal random ID, role, verified session, consent, country/currency; PII separate |
| freelancer_profiles | user FK, skill taxonomy, portfolio pointers, rate basis, availability, self-reported vs verified evidence |
| projects | client FK, request version, requirements, requested budget and active status |
| matches | project/profile FK, rank version, eligible reasons, explanation & data-quality status |
| price_estimations | project FK, features hash, data version, model version, reference price band, interval coverage/provenance, estimation type |
| quotes/contracts | project+freelancer FK, exact version, currency, amount, scope, negotiated status, approval records |
| payment_attempts | quote version, merchant, order ID, capture IDs, amount, idempotency key, status, provider GET evidence, timestamps |
| refund_cases | payment FK, requester, reason source and status, authorized amount, provider refs; manual and Sandbox only at first |
| disputes/complaints | transaction FK, complaint type, reported reason vs operator classification vs AI hypothesis, evidence pointers, updates, outcomes |
| audit_events | actor_type/user vs AI, action, request_id, previous/new state, affected object/hash, source, time; no secrets/raw prompts |
| model_runs | dataset version and rights, split, metrics, numeric comparison and validation |
**Integrity & tenancy:** enforce authorization per client/freelancer; single merchant sandbox on demo, do not falsely claim actual marketplace splits, escrow or multi-vendor production. Role-based visibility; no cross-tenant dispute view; private fields encrypted or minimal, retention/redaction/purge mapped, logs never embed keys or raw customer inputs. Unique provider webhook event IDs, separately verified signature, prevent UI callback authority.

## E. SOVIA and DBVORA must have distinct, truthful roles
**SOVIA core = retrospective signed/append-only-*designed* transaction/agent action audit.** Reuse SOVIA event schema/policy/report ideas and write small compatible Node adapter to existing payment ledger first: recommend-vs-approved price mismatch, unauthorized action attempt, duplicate attempt, unexpected refund/status, missing receipts, failed webhook verification, unusual complaint patterns (flags, NOT verdict of fraud). Existing SOVIA repo is Python offline; direct full microservice integration is NOT required for single hackathon transaction. Auth service / payment ledger must block unsafe transitions BEFORE audit, not rely on retrospective SOVIA for live defense. The audit trail can be tamper-evident with per-record digest but hashes do not prove external truth or authenticated identity. Integrating full SOVIA actual service/report may be added after a proven needed seam.
**DBVORA core = read-only schema visibility, local database map, growth metrics and approved snapshot/restore audit.** It is not the transaction ledger and must not modify live payments. Adapters for local SQLite can reuse documented safe `mode=ro` strategies only under rights/license; Cloudflare D1 observability requires an entirely separate read-only adapter or export, no filesystem assumptions. Do not connect DBVORA to public user traffic in the critical checkout path. MVP can show a synthetic/schema-only topology report if proven, otherwise visibly defer without pretending operational integration.
**Original-code source boundary:** both DBVORA and AX_FLOW may be private. Public contest repo must not include private licensed business code without explicit owner open-source decision. Implement contest-specific bounded original interfaces and attribution, or expose mock contract; not a full product paste.

## F. Fail-safe payment state machine
`REQUESTED → PROPOSED → OWNER_APPROVED → ORDER_CREATE_PENDING → BUYER_ACTION_REQUIRED → PROVIDER_VERIFIED → CAPTURE_PENDING → PAID_VERIFIED`.
`FAILED`, `CANCELLED` and `UNKNOWN_RECONCILIATION_REQUIRED` stay separate; disputed/partially refunded/refunded states are separately recorded as later provider-confirmed events, not an arbitrary destructive overwrite of paid history.
- Approval = authenticated human actor bound to quote ID, exact version, price/currency and merchant.
- First durable atomic claim and idempotency key committed **before** external POST; failed/timeout/unknown POST must not be blindly retried. Cross-check via PayPal GET and reconciliation.
- Buyer return URL is never proof of paid state; capture must be authenticated server-side and provider-confirmed.
- Webhook verification signature and dedupe event ID mandatory before treating as authority.
- Refund execution / capture real orders only explicit owner-approved Sandbox scope; no real card/live platform, no AI money authority.
- No platform fee split, multi-seller onboarding, payouts, escrow or instant complaint decision without genuine PayPal enablement/partner/compliance approvals.

## G. Tests and demo
**Required actual test:** one real authorized seller business sandbox + buyer personal sandbox, corresponding app, 1 virtual USD order plus separate owner approval → AI structure/match → accepted exact quote → PayPal sandbox order → buyer action → server capture + GET reconcile → audit receipt. Keep keys off GitHub/video.
Synthetic/fault unit scenarios: fake matched freelancer; non-consented/mismatched seller; unauthorized quote amount/merchant/tampered approved object; repeat clicks; double capture; broken return token; stale checkout session; ambiguous POST; invalid webhook; tenant isolation; refund requested without approval; optional price model insufficient data leads "not validated" label.
**Repo release:** root open source LICENSE with compatible public code; clear README of significant 2026 hackathon updates, start/stop and clean judge test steps, distinct synthetic vs actual sandbox footage; public YouTube demo <3 min; Devpost complete and receipt. Prior 347/347 CI only offline and earlier single real OAuth+Gemini 200 **do not prove** actual orders/buyer/capture or full AI+PayPal UI. Need judge cold run from clean env.

## H. Milestones
P0 **immediate through Nov2:** preserve checkout infrastructure; seller/buyer/merchant/callback owner approval; prove first genuine Sandbox order path. This is top critical-path gate.
P1 **Nov2–6:** thin platform screens for client post/talent opt-in / AI match / price fallback / quote approval / audit receipt. Use curated synthetic only, no claims of demand/sales. Have two roles and one functioning match.
P2 **Nov6–9:** SOVIA-style embedded event contract and dispute/refund *record schema only*; DBVORA observability if proven on safe read-only adapter; no second service risk. Run injection/idempotency/secret scans. Standalone full SOVIA/DBVORA may remain postcontest.
P3 **Nov9–10:** full actual end-to-end and screen capture rehearsal; if absent by Nov10, stop new feature work and focus checkout or report ineligibility risk.
P4 **Nov10–Nov12:** freeze public source, LICENSE, precise demo and public YouTube <3min, English submission, testable instructions, official Devpost owner approval and receipt before **Nov13 05:00 KST**.
P5 **postcontest:** data accumulation/consent, valid price ML, dispute taxonomy analytics, additional seller partners, formal SOVIA+DBVORA interoperability, commercial review and sales. Do not claim these today.

## I. Explicit difference from original plan
**Preserved:** AI quote, human approval, payment once/idempotency/UNKNOWN safety, contract+milestones, cancel/refund tracking, safe provider. **Elevated to product core:** user registration, discovery/AI matching, explainable price analytics, trust and audit, marketplace data model. **Deferred for valid submission:** subscriptions, mass payout, full SaaS/partner seller onboarding, production fraud detection, 10k concurrent users, real-price prediction without labels, full DBVORA live stack. Single existing repo and one hackathon submission.

**KPI hypothesis to measure, not yet established:** qualified candidate recall@3, estimate range empirical coverage/MAE, verified transaction completion %, refund/dispute classification completeness, prevented duplicate external charges, judge cold setup time. No actual customer counts or win rates.
