# Three-hackathon stretch roadmap — after eligibility and stable base (2026-10-24 KST)

**Decision type:** conditional engineering strategy drafted by integrated chief in response to user asking what to build if the three projects finish ahead of schedule. **This document is NOT a new ACTIVE order to leads, not permission to bypass existing P0 owner-account gates, not authorization for paid services, official submission, or confidential data publication.** Lead `docs/FROM_HACKATHON_COMMAND.md` ACTIVE/P0 always outranks stretch goals.

**Primary outcomes:** (1) eligibility and actual submission proof, (2) scoring-relevant standout moment, (3) reproducible public portfolio demonstrator. Plan dates are KST; calendar progress % is NOT software maturity.

## Keep the gates first
- **KIC**: authenticated DAKER individual/team-leader/submit-button authority; exact entrant-approved <=10-page official-template PDF. Current day ledger **28 DONE/3 BLOCKED/29 NOT_STARTED** on `lead/kic@6e0a896b19154b41a1197b7420f2cb43e7d53a70`. Official Round 1 is **proposal PDF**, not mandatory production deploy. Round 1 deadline **2026-11-12 10:00 KST**; finals only if selected (Dec 3 results; Dec 22 prototype/demo/README/PDF).
- **PayPal**: authorized genuinely working PayPal Sandbox OAuth/Orders+buyer/capture evidence and actual AI response; user-safe judge reproduction + publicly visible <3-minute video + public OSS LICENSE. Current **12 DONE/2 PARTIAL/1 BLOCKED/3 NOT_STARTED** on `lead/paypal@ae90cabddbab8444ef0a49fa8538b651108d2960`. Deadlines **2026-11-13 05:00 KST**; public hosted URL optional only if judge can actually run build following README; synthetic demos alone ineligible.
- **UGREEN**: evidence that participant actually used the *official UGOS Skill Creation Tool* to CREATE the initial Skill in supported assistant, compare actual generated Markdown, review rights/dataflow/AI disclosures and submit exact PDF+ZIP with receipt. Current **2 DONE/12 PARTIAL/3 BLOCKED/7 NOT_STARTED** on `lead/ugreen@cb29c2f4197ff9edd2f89c96d6da2d8c44384845`. Round 1 deadline **2026-11-16 16:45 KST**; no live NAS/video required in Round1. Finalists have separate assigned single-day NAS remote access Nov 22–28 PT and Round2 deadline Nov 30 23:45 PT (Dec 1 16:45 KST).

## Rank-one conditional stretch per contest

### KIC — evidence-traceable investment research Agent
**Why:** round-one PDF evaluates problem, business usefulness, agent design, sources and MVP feasibility. Real usefulness, source truth, and explainability differentiate from a generic RAG chatbot. Build as a finalist preparation / demonstration branch, keeping submitted frozen preliminary PDF intact.

- **Core showcase:** one realistic public permitted company-and-period question, Research → primary-source Verification → Risk verdict (or UNKNOWN) → 1-page cited report. Every figure and claim is linked to original issuer/source date/report code, unit, calculation, timestamp and verification status. An unavailable source must remain `NOT_VERIFIED`; never upgrade synthetic fixtures into real source evidence.
- **Differentiating moment:** click one red-flag metric → inspect source and denominator; discover missing/mismatched filing → system *withholds* ratio and explains why, instead of hallucinating a risk rating. Compare at most 2–3 truly verified peers and one historical period if original permissible facts are available.
- **Acceptance:** reproducible recorded 3-case demo: valid matched facts, mismatched sources, denominator invalid; at least one authorized real DART filing trace confirmed before labeling anything LIVE. Offline synthetic acceptable as openly labeled fallback, not official verified evidence.
- **Avoid:** more investment-factor counts, PDF cosmetic loops or LLM orchestration complexity ahead of actual DAKER submission permission.

### PayPal — single compelling AI-to-payment transaction with human safeguards
**Why:** judging equally weighs PayPal+AI depth, end-user design, impact, novelty and presentation. Stage-one minimum is a genuinely functional AI+PayPal integration.

- **Core showcase:** client brief → actual AI drafts bounded scope/milestone quote → seller reviews/edits & explicitly approves exact price/currency → real PayPal Sandbox buyer approval → server-side retrieval/capture confirmation → receipt/milestone state visible. Keep event chain reproducible with two safe sandbox roles.
- **Differentiating moment:** AI warns about a changed scope/invoice or incorrect amount before any payment. The operator sees exact approved amount and a "request approval again" path; payment is held rather than guessed. No autonomous real-money payment/escrow/regulated custody claim.
- **Acceptance:** one allowed real Sandbox transaction and one genuine AI-generation receipt (secret-redacted), end-to-end demo with wrong-merchant, mismatched-amount, duplicate webhook, interrupted request tests; use verified idempotency for uncertain outcomes. A <3-minute YouTube video shows actual on-device operation; README allows judge to execute or interact. Availability of reviewer sandbox account must be handled by the entrant under provider rules without public credential leakage.
- **Avoid:** more fake D1, subscription, production hosting and peripheral integrations before real Provider gate. Optional stretch *after* base: tiny conversion dashboard or frictionless buyer-view only if demo remains coherent.

### UGREEN — NAS-local ProjectReady delta and provenance review
**Why:** Round1 scored equally on user value, differentiation, technical quality and **NAS-specific fit**. "List missing files" alone is easily compared to a generic AI folder tool; repeat-run evidence with safe version/permission decisions makes it distinctive.

- **Core showcase:** owner-authorized NAS folder and explicit checklist → source-backed PRESENT / MISSING (only complete scans) / NOT_CHECKED / VERSION_REVIEW report → compare a second run with prior authorized snapshot → "newly missing / changed / ambiguous versions / unchanged" digest and precise owner next steps. No file reads outside scope, and no secret path echo.
- **Differentiating moment:** a supposed final file disappears or there are two possible final versions; instead of quietly selecting the newest or declaring READY, agent flags the change and asks human to choose. Unavailable Agent permissions remain NOT_CHECKED, never fake a verified absence.
- **Acceptance:** official UGOS Creator output and later (if finalist) actual registered NAS agent path/complete-listing evidence; 5 reproducible synthetic scenarios for Round1 explanation (already exist, reuse), explicit safe I/O, handling a missing permission and truncated listing. Stronger NAS Fit: cite actual approved NAS file/knowledge capabilities, show local persisted historical evidence only if supported by real permissions/SDK. Round1 submission ZIP remains Markdown-only as per rules; don't insert scripts/JSON/bin.
- **Avoid:** repeated static SDK spelunking, unapproved live NAS scan, cloud data exfiltration, adding executable to 4-file entry, claiming simulated 211 passes prove official NAS compatibility.

## Shared portfolio release layer — after contest-specific submission gates
One short English product summary, a 60–150-second labeled honest walkthrough for each, one architecture/decision diagram, reproduction README, CI evidence, threat/limitations section, synthetic-data fallback clearly differentiated from real provider validation, and links to contest receipts or state NOT_SUBMITTED. Release only assets with validated rights. Keep contest originality and third-party license disclosures separate. No extra premium integrations solely for sponsor-prize eligibility unless user opts in.

## Priority/stop decision rule
1. **P0 external proof before expansion**: if access blocked, prepare only one concise owner action checklist and deterministic safe test harness. Do not spend successive work units on mock replacements.
2. **P1 one scoring-relevant differentiator per contest** only when initial product and exact release path are verified or a genuinely independent task cannot endanger deadline.
3. **P2 polish** user journey/video/reproducible docs; keep max scope bounded.
4. No feature counts or elapsed-hour percentages manufactured from dates. Any additional release or account/paid/third-party action requires entrant permission and a fresh compliance check.
5. Supervisor may suggest/stretch backlog in command center; child lead starts work only after current active priorities and user approval conditions, preserving latest lead schedules. Avoid altering original 60/18/24 day DONE statuses based solely on plan.

## Official evaluation sources
- KIC [official DAKER call](https://daker.ai/public/hackathons/kic-ai-agent-competition): preliminary PDF, 10-page limit, later finals with executable demo and agent.
- PayPal [Devpost Rules](https://paypalaihackathon.devpost.com/rules): stage 1 viability + genuine PayPal Developer Platform and AI, 5 equally weighted criteria, functional repo/test build and public YouTube under 3 minutes.
- UGREEN [Devpost Rules](https://ugreenhackathon.devpost.com/rules): official Creator requirement, Round1 PDF/ZIP and no NAS runtime, four equally weighted criteria; finalist-only NAS remote test and Round2 submission.
