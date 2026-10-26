> **KIC ONLY — 2026-10-27 LATER USER DECISION / OVERRIDES EARLIER KIC AutoML-DEFER WORDING:** [KIC evidence-rich finance analysis + adapted AutoML analysis architecture](KIC_PROOFINVEST_ANALYSIS_AUTOML_DIRECTION_20261027.md) now specifies KIC final product emphasis: broad verified financial/capital/ownership/business signals, including paid/bonus offerings, major shareholding changes and potential dilution, analyzed with purpose-adapted AutoML components where scientifically justified. DB is optional support, not core. **ML modeling is conditional on adequate point-in-time data and valid group/time holdout.** Protect prelim PDF/submission (any actual PDF edit needs separate approval) and preserve current ProofInvest code until KIC lead implements/test-verifies. PayPal design remains awaiting user reflection and unchanged; UGREEN unchanged. This later design addendum takes precedence for KIC alone.

# FINAL DESIGN BASELINE — KIC / PayPal / UGREEN
> 2026-10-27 KST · Owner delegated final architecture selection to hackathon-command chief (“해총”). **DESIGN FIXED**; contest-lead implementation, release, credential use, external API calls, original submissions and rights approvals remain separate gates. This does not assert real E2E, Devpost/DAKER submission or official license clearance.

## Decision
Three separate products, three separate existing contest repositories and leads. No new shared runtime, no cross-repo wholesale merge, no SMAX private-source publication. Reuse **verified design invariants and small justified code patterns**, not assumed compatible modules. All new code follows contest ownership/AI originality/license rules, existing healthy functionality and originals preserved.

### Architecture options (qualitative assessment)
| Option | Schedule / cost | Quality and maintenance | Resolution |
| --- | --- | --- | --- |
| A. Merge RAG/SOVIA/DBVORA/SMAX/REA/AutoML into contest applications | Highest migration, dependency, licensing and integration cost, especially inside submission week | Wider attack surface, less judge reproducibility; UGREEN Markdown-only incompatibility | REJECT |
| B. Contest-native core + narrow proof/abstention/audit techniques + outside QA | Low incremental cost if implemented in current language and only where a test demonstrates a gap | Focused product quality, easiest to maintain and explain, lowest submission risk | **SELECT** |
| C. Leave contest apps untouched, never leverage existing validation patterns | Lowest near-term cost | Misses selectively useful provenance/audit techniques and repeatable offline QA | REJECT as permanent policy; acceptable for any individual feature that adds no net value |

## 1. KIC — ProofInvest (public name unchanged)
Repository: `hibi89/hibi89-kic-proofinvest`, implementation owner `lead/kic`.
**Final product**: evidence-grounded enterprise/industry financial research and risk agent: grounded findings, comparable verified financial facts, cautious risk results, and a readable evidence ledger. Not an automated investment recommendation.
**Runtime concept**:
1. User chooses company, as-of date and authorized data scope.
2. Research Agent organizes legal/authorized company/industry references (source URL, title, publication/collection date, source IDs).
3. Verification Agent cross-checks fiscal year, statement basis (CFS/OFS), units, primary-source consistency, date and conflict; unresolved facts remain WITHHELD.
4. Risk Agent calculates only admissible comparable metrics via current Decimal/fail-closed code; no synthetic data presented as real.
5. Report Agent exposes conclusion + cited source + underlying numeric basis + gaps + human review status.
**Existing implementation evidence**: `proofinvest/research.py` and `risk.py` already reject some bad/mismatched/unsupported evidence. Existing timestamp and Decimal tests are offline, NOT actual authenticated OpenDART data.
**RAG_STUDIO decision**: ADOPT only source-fidelity/contradiction/abstention *architecture and targeted test ideas*. Its actual `src/evidence-router.mjs` currently speaks sales/returns/shipping and cannot be dropped into financial research. No separate RAG server, vector database or data ingestion dependency unless proven necessary at finalist stage.
**AI_AutoML_Analyst**: DEFER missingness/profiling option to finalists if a truly needed CSV/Excel data-quality gate cannot be satisfied more cheaply. No unrelated ML forecasting or automation in preliminary.
**KIC prelim acceptance**: organizer template PDF, all seven mandatory components, <=10 pages, original sources/rules, exact team/title/upload approval, final receipt by **2026-11-12 10:00 KST**. Do not delay PDF for code. **Only if finalist**: demonstrate judge-runnable prototype URL + code+presentation PDF by **2026-12-22 10:00 KST**; optional video for bonus.

## 2. PayPal — Freelancer Payment Agent (public name unchanged)
Repository: `hibi89/hibi89-paypal-ai-hackathon`, owner `lead/paypal`.
**Final product**: AI assists freelancer quote and explicit milestone/checkout proposal, but payment authority remains human; one traceable PayPal Sandbox order/approval/capture result tied to the approved exact quote.
**Critical single path**:
`request -> AI suggested quote (not authority) -> owner human approve version+USD amount+merchant -> durable authenticated server session -> claim/idempotency gate -> Sandbox create order -> buyer approves -> server GET + capture/GET reconcile -> audit receipt + outcome`.
**States**: DRAFT / PROPOSED / APPROVED / BUYER_ACTION_REQUIRED / VERIFIED_PAID / FAILED / UNKNOWN_NEEDS_RECONCILIATION. No 'paid' from a UI callback, client-supplied approval object or unverified sandbox response. No automatic real-money payments.
**Current in-repo components**: `src/pilot_checkout_session_store.mjs`, `src/paypal_sandbox_transport.mjs`, payment ledger and safe unknown/idempotent claim patterns. Real merchant/buyer order cycle and clean judge setup remain unverified at lock.
**SOVIA decision**: ADOPT a **minimal JS-native, embedded audit contract** only if existing payment ledger does not already emit sufficient fields: quote version; human actor/approval time; intended amount/currency/merchant; action type; attempted and verified provider refs; result; UNKNOWN/reconciliation reason; timestamp; source/bounded digest. Secret, access token and private user data never logged. SOVIA Python service, multi-agent rule engine, dashboard and vendor dependencies are NOT dependencies.
**Outside release QA**: apply `ai-code-checker` offline scan where supported, explicitly marking JavaScript coverage gaps; apply selected `REA_Web` zip/manifest/hash, traversal and source-manifest *ideas* in a PayPal-specific release preflight. Do not embed REA_Web's unrelated delivery schema, copy whole Python stack or claim complete security proof.
**SMAX²**: DEFER private CSV/report/export and subscriptions; not needed to prove one full AI+PayPal order path, must not copy private code into a public contest repository.
**PayPal acceptance** by **2026-11-13 05:00 KST**: one real authorized Sandbox buyer+merchant flow with AI-produced suggestion and human amount approval; judge-reproducible runnable app (local setup allowed), verifiable correct capture state, safe secrets, visible root open-source LICENSE, public testable source/English setup, public YouTube functioning demo under 3 minutes, and Devpost receipt. Existing offline CI and isolated OAuth/Gemini HTTP 200 do NOT prove this. **Review Go/No-go on Nov 10** if buyer approval/real flow remains unproven, without silently abandoning entry.

## 3. UGREEN — ProjectReady NAS (public name unchanged)
Repository: `hibi89/hibi89-ugreen-nas-hackathon`, owner `lead/ugreen`.
**Final product**: original contest-created Markdown Skill for authorized project-delivery folder review, assessing whether mandatory documents exist, whether owner-confirmed final versions are unambiguous and whether supported permission/privacy checks suffice.
**Skill flow**:
`user-provided folder + mandatory checklist + authorization -> verify registered official expert-agent capabilities -> bounded read-only listing/checks -> evidence for each mandatory item/version/access -> READY | BLOCKED | NEEDS_REVIEW + cited next action`.
**Decision contract**: READY only with complete positive evidence for ALL required checks; BLOCKED when required file absence is established from complete authorized listing; NEEDS_REVIEW on scan truncation, restricted materials, ambiguous versions, unsupported permission checks and incomplete evidence. Never infer "missing" from permission failure; never inspect secrets or escape folder, mutate NAS, run arbitrary Python or direct SQLite introspection.
**SOVIA**: ADOPT permission/evidence/abstention *principles* in the newly authored Markdown workflow, not pre-existing runtime or shipped code.
**DBVORA**: ADOPT only read-only bounded metadata-inventory *principles*. Actual `dbvora/connectors/sqlite_reader.py` is a LOCAL SQLite Python connector and not an authorized Uliya/NAS runtime. DO NOT embed or invoke it in the Skill.
**Present owner-review artifact state at design lock (per lead report, not verified here anew)**: Round1 G37 PDF+G36 Markdown Skill ZIP, offline checker reviewed, exact-rights and applicable official standalone kit license response **HOLD**. Vendor inquiry sent, not permission granted. User exact artifact approval and submission still required.
**Round1 acceptance** by **2026-11-16 16:45 KST**: newly developed Skill/core workflow, prescribed `SKILL.md` + linked Markdown references ZIP only, 10-question English PDF <=500 substantive words and <=1MB, ZIP constraints, source/licenses/tool-use disclosures, appropriate rights proof or hold decision, Devpost receipt. No NAS demo or public source requirement in Round1. **If finalist**, validate actual assigned NAS registered agents/permissions and produce same-Skill functional package + actual NAS video for Round2, not a separate project.

## Cross-project use disposition (8 proposed links)
| Contest | Existing project | Fixed disposition |
| --- | --- | --- |
| KIC | RAG_STUDIO | Architecture/test patterns only; no sales router module |
| KIC | AI_AutoML_Analyst | DEFER until finalist with demonstrated ingestion need |
| PayPal | SOVIA_sovereign | Small in-process audit contract; reuse existing ledger first |
| PayPal | REA_Web | Outside release package/hash preflight concept, no runtime integration |
| PayPal | ai-code-checker | Outside offline QA with explicit language/coverage limits |
| PayPal | SMAX² | DEFER private CSV/report integration, no public source export |
| UGREEN | DBVORA | Bounded metadata read-only principle only, NO SQLite connector |
| UGREEN | SOVIA_sovereign | Permission / UNKNOWN / evidence principle only, NO runtime code |

## Sequencing and freeze
**No scope creep before valid submissions.** Current owner SMAX-first focus up to approximately Nov 7 is preserved unless owner changes it. Complete low-cost auth/rights/exact-file prechecks earlier if feasible, as delaying actual PayPal E2E to Nov7 poses substantial schedule risk.
1. Protect KIC organizer-compliant PDF and DAKER receipt; internal target Nov10.
2. Put almost all required engineering on PayPal one true real-Sandbox+AI buyer path, clean run and public demo; internal target Nov12 evening KST.
3. Keep UGREEN exact PDF+ZIP immutable unless justified by failed rule/rights validation; internal target Nov14–15, license approval external HOLD.
4. After accepted initial submissions or finalist invitations, reconsider deferred modules against explicit actual need, without changing the three fixed product identities.

## Minimal verification matrix
- KIC: real-source authenticity separate from offline validation; citation/year/unit conflicts refuse; exact signed-off PDF and backend receipt.
- PayPal: unauthorized quote/order rejected before PayPal calls; duplicate/timeout UNKNOWN safe; actual buyer approval+capture+GET and ownership verified; cold-start instructions runnable by judges; secrets absent from repo/video.
- UGREEN: incomplete/denied listing -> NEEDS_REVIEW; confirmed required missing -> BLOCKED; all evidenced -> READY; restricted path/unauthorized agent impossible; official checker and exact artifact hash; rights signoff; receipt.
- Across all: regression PASS != external live PASS != official contest receipt. No new paid service or source publication without owner approval.

## Governance / owner authorization
Design-only lock under owner's 2026-10-27 request. No code merges, no contest-lead scope change executed, no GitHub repo publication permission changed, no external provider call or final submission made. Implementation owners must read this as the chief architecture baseline; changes need evidence+owner approval. Central STATUS/HANDOFF track status separately. Current official rules checked Oct27 KST:
- https://daker.ai/public/hackathons/kic-ai-agent-competition
- https://paypalaihackathon.devpost.com/rules
- https://ugreenhackathon.devpost.com/rules
- https://ugreenhackathon.devpost.com/
