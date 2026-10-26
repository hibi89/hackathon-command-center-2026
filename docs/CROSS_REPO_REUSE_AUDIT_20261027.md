# 2026-10-27 — Hackathon-first feasibility and GitHub reuse audit

STATUS: Recommendation only. The owner asked about shifting to hackathons immediately, and reuse of existing software. This report does NOT change the existing SMAX work order, submit entries, copy private code, or run external APIs.

## Recommendation
Prioritize time-limited hackathons now, with three different completion definitions. First finalize KIC preliminary PDF and UGREEN Round 1 PDF/Skill ZIP, then give almost all engineering attention to PayPal's REAL Sandbox+AI E2E, judge reproducibility and demo video. KIC/UGREEN are early-round submissions, not the end of any finalist obligations. Awards are uncertain, not weekly income.

Official KST deadlines:
- KIC: 2026-11-12 10:00, organizer-based <=10-page proposal PDF only. Finalists need MVP URL, code and PDF by Dec 22 KST. https://daker.ai/public/hackathons/kic-ai-agent-competition
- PayPal: 2026-11-13 05:00, runnable PayPal+AI project (not offline mock), publicly accessible open-source repo/LICENSE, English instructions, public <3min YouTube functioning demo. https://paypalaihackathon.devpost.com/rules
- UGREEN Round 1: 2026-11-16 16:45, English ten-question <=500-word <=1MB proposal PDF plus newly developed Uliya SKILL.md and linked Markdown references ZIP; no executable scripts and no NAS demo/video required. Finalists return for Nov22–30 PST NAS testing and Round2 submission. https://ugreenhackathon.devpost.com/rules

## Current official project sources checked
- KIC public lead/kic: proofinvest/engine.py, research.py, risk.py use Decimal fail-closed numeric reasoning and evidence timestamps. Historical offline 254 tests PASS, final proposal submission receipt absent. An existing 10-page proposal draft is reported; final PDF access/approval still needed.
- PayPal public lead/paypal: src/paypal_sandbox_transport.mjs, pilot_checkout_session_store.mjs, hosting_preflight.mjs, d1_claim.mjs contain checkout proof binding and conservative operation states. Historical 347 offline PASS; user-run OAuth and Gemini basic HTTP 200 proven, actual buyer Order create/approve/GET and judge-run build not proven. No video or receipt.
- UGREEN public lead/ugreen: skill/projectready-nas/SKILL.md, skill/projectready-nas/references/decision-policy.md, src/projectready/policy_guard.py. Ready-to-review PDF+ZIP independently checked (269 offline PASS); exact rights/license inquiry unresolved, official NAS validation not required Round1, final submission absent.

## Cross-repo reuse decisions from source inspection

| Target | Source existing repo and real file | Reusable capability | Decision |
| --- | --- | --- | --- |
| PayPal | ai-code-checker main: offline_core.py; offline_coverage.py | Offline bounded source scan, honest 'unknown' skipped coverage | Use as EXTERNAL QA, not payment-runtime integration; cannot claim full JS security audit |
| PayPal | REA_Web feature/d27-windows-python-discovery: rea/provenance.py, rea/safe_publish.py | SHA/manifest audit; fail-closed local package publication | Use design or independent artifact QA for judge distribution, not whole Python stack |
| PayPal | SOVIA_sovereign develop: sovia_audit.py; sovia_history.py | Offline audit rules and digest-only event history | Adapt consent/evidence states only if needed; DO NOT add a separate Python service before real Orders demo |
| PayPal/KIC later | RAG_STUDIO feature/p31-dashboard-hardening: src/validate.mjs; src/evidence-router.mjs | Strict package fields/hashes; grounded evidence router abstains on unsupported/conflicting claims | Reuse design tests; sales-specific schema NOT drop-in; optional until actual mandatory submission accepted |
| KIC finalists later | AI_AutoML_Analyst feature/kmong-v1: backend/app/services/profiler.py | Pandas column missingness/cardinality profiles | Optional data-quality gate, cannot independently authenticate DART; NOT a prelim dependency |
| KIC finalists later | DBVORA feature/p0-db-map: dbvora/connectors/sqlite_reader.py | Restricted SQLite metadata read-only connector | Optional safe local data adapter, private owner code; no reason to port for prelim |
| UGREEN Round1 | SOVIA_sovereign: risk rule / withheld outcomes; DBVORA: restricted read-only inventory | Permission-first, UNKNOWN instead of guessing, source traceability | PATTERNS ONLY in newly authored Markdown Skill, NEVER raw code/runtime copied into ZIP; official registered NAS agents only |
| UGREEN Round1 | REA_Web provenance verifier and code-checker | Offline archive and static quality checking | QA OUTSIDE the submitted Markdown-only ZIP |
| KIC/UGREEN PDF | astra_pdf_redesigner lead/astra-commercial-20261025 | PDF layout / page count / print acceptance techniques | Use only if existing artifacts fail specific quality gate; do not rebuild PDF tool |
| PayPal optional | private SMAX CSV normalization and sales-report prototypes | Data mapping and explicit review states | Private source must stay private; possible patterns only with owner-specific publication approval; not contest mandatory |

Policy cautions:
- UGREEN organizer permits an older *idea* but requires new Skill and core workflow developed during this event; old Skills/submission content cannot simply be recycled. UGREEN ZIP must include only required SKILL.md and linked Markdown references, not executable code, secret files or unapproved external data.
- PayPal permits projects substantially updated during event. Full source + visible LICENSE are mandatory; private-source copy and customer/API credentials in public GitHub prohibited without owner approval and sound license review.
- KIC welcomes lawful external AI/data but requires an original entry and source attribution; do not overbuild a preliminary PDF into full software.
- Some inspected public repositories have no root open-source LICENSE; public visibility is NOT a third-party grant. Private code stays private in this public audit. Existing owner intellectual property decisions remain theirs; no automatic cross-repo merge.
- The best leverage is already-tested QA and evidence-first rules, not new features or a wholesale app merge.

## Suggested priority switch schedule (pending owner choice)
1. Oct27–29: finish independent KIC PDF/template checks and UGREEN licensed/disclosed PDF+ZIP review, with human final-file approval; attempt early valid submission only after explicit authorization. Track receipts and exact artifact SHA.
2. Oct29–Nov8: PayPal genuine Sandbox buyer flow (single owner-approved test), AI-bound quote, clean reproducible runnable demo, public LICENSE/README/English docs, less-than-3-minute real YouTube video, form preflight. No real payments or credentials in public repo.
3. Nov9–12: patch PayPal critical failures only and ensure all confirmed receipts; KIC has Nov12 10:00 deadline, PayPal Nov13 05:00.
4. Nov13–16: UGREEN rights/format gate and Round1 final submission; keep buffer.
5. After initial submissions resume other projects, unless UGREEN makes finals in Nov (one assigned real NAS day Nov22–28 and Round2 due Nov30 PST) or KIC makes finals on Dec3 (prototype due Dec22).

No code merged, no rights cleared, no source license granted, no jobs begun by this documentation-only audit. GitHub source files checked and official rules last retrieved Oct27 KST.
