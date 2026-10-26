# 2026-10-27 KST — Nov 7 start feasibility audit: KIC, PayPal, UGREEN

## User plan and conclusion
Owner plans to concentrate on three hackathons **starting around 2026-11-07**, after prioritizing SMAX² up to that date. Assessment: **KIC preliminary submission FEASIBLE CONDITIONALLY; UGREEN Round 1 FEASIBLE CONDITIONALLY; PayPal FUNCTIONAL SUBMISSION HIGH-RISK** if major development/test/upload waits until Nov 7. These are schedule judgments, not guarantees; earliest blocking dependencies (account, rights, sandbox, participant authorization) should be checked by the owner before Nov 7 without requiring major development.

## Official deadlines and required scope
All deadline times below are **Asia/Seoul**. Nov 7 00:00 is only a reference for measuring headroom; the actual first work hour may be later.

| Contest | Official Korean deadline | Full days after Nov 7 00:00 | Mandatory for near deadline | Evidence |
| --- | --- | --- | --- | --- |
| KIC ProofInvest **preliminary** | **Nov 12, 2026 10:00 KST** | 5d 10h | Organizer template-based PDF <=10 pages; core sections summary, problem, service, AI agent, data, MVP plan, impact; authenticated DAKER participant/team submit and receipt | https://daker.ai/public/hackathons/kic-ai-agent-competition |
| PayPal AI Hackathon | **Nov 13, 2026 05:00 KST** (Nov 12 noon PST) | 6d 5h | Actually functional PayPal developer/Sandbox + AI project, runnable test/demo or reproducible build, public licensed source repo, accurate English description/instructions, public YouTube demo under 3 minutes; Devpost form and receipt | https://paypalaihackathon.devpost.com/rules |
| UGREEN AI NAS Round 1 | **Nov 16, 2026 16:45 KST** (Nov 15 23:45 PST) | 9d 16h45m | English <=500-word 10-point proposal PDF <=1MB, initial Markdown-only Skill ZIP <=10MB compliant Uliya format and third-party disclosures, eligible Devpost entry/receipt. No real NAS operation, demo video, public repo **required for Round1** | https://ugreenhackathon.devpost.com/rules |

KIC **finalist** MVP/demo/code are due later **Dec 22 10:00 KST** only after advancing from prelim; don't spend Nov7-12 on full MVP at the expense of PDF. UGREEN Round2 real NAS demo only if selected. PayPal requirements are strict at first submission: offline mocks alone cannot replace functional demo.

## GitHub lead branch evidence checked 2026-10-27
- KIC `hibi89/hibi89-kic-proofinvest@lead/kic`: latest STATUS opening records offline tests **254/254 PASS** (code SHA `2273a497`, CI 40111994431), overall 60-day task ledger **29 DONE/3 BLOCKED/28 NOT_STARTED** includes many later milestones and must not be translated to preliminary readiness. DAKER logged-in team-leader UI with empty title and PDF drop zone confirmed on 10/25; final submit rights/backend success and receipt **NOT VERIFIED**. Frozen 10-page draft PDF/PPTX and 6 Library copies retained; exact final PDF selection and rule/visual check pending; OpenDART external validation pending but NOT mandatory for proposal-only prelim.
- PayPal `hibi89/hibi89-paypal-ai-hackathon@lead/paypal`: offline 347/347 CI PASS, owner-run genuine **Sandbox OAuth HTTP 200** and **Gemini one genuine text HTTP 200** (only initial proof). **Actual Orders create → buyer approve → GET confirm, callback/merchant ownership, end-to-end frontend, public judge-accessible runnable build, <3min YouTube, Devpost submission NOT VERIFIED**. Ledger: **12 DONE/3 PARTIAL/3 NOT_STARTED** out of 18; D03 65% PARTIAL, D04 80% PARTIAL, D15 20% PARTIAL; published remaining 2–5h for D03 and 5–10h for D15 are *partial-task planning assumptions*, not reliable all-in completion times. No automatic or repeated financial Sandbox calls; require separate approval.
- UGREEN `hibi89/hibi89-ugreen-nas-hackathon@lead/ugreen`: prepared exact Round1 **PDF** (5,227 bytes, English Q&A 378/500 words) and **Skill ZIP** (5,685 bytes) independently QAed with 269/269 offline PASS (CI 40321597804); first-party static checker PASS. G42 adversarial tests later **staged, CI pending** at last branch status. Ledger **14 DONE/3 BLOCKED/7 NOT_STARTED** of 24. Real NAS/Agent runtime and permission **not verified**; this is **not Round1 mandatory** per official rules. Crucial **RIGHTS/LICENSING HOLD**: official standalone kit's applicable license not established, rights/disclosure review pending, participant already emailed organizer nas-support@ugreen.com on Oct26 (sent proof, not reply). Originality/Creator provenance and exact Devpost submit authorization unverified. Round1 does **not** demand 3-minute demo despite a separate sponsor marketing-page description having inconsistent text; use specific official Rules.
- In all three: NO confirmed official submission receipts, no verified prizes.

## Critical-path schedule and control dates (proposed; no automated work)
- **Before Nov 7 — lightweight dependency check only** if owner can spare a few minutes without interrupting SMAX development:
  - KIC: verify DAKER title/team-leader PDF upload controls and that final approved compliant PDF is accessible; hold submit until explicit owner authorization.
  - PayPal: confirm owner can log into Sandbox, produce truly runnable public-source candidate, understands YouTube/English requirement, and actual buyer/merchant permissions. No unapproved orders, payments, provider calls or public releases.
  - UGREEN: check for official license/support reply; plan exact permitted own-code/Markdown-only materials and third-party disclosures. Do not assert rights granted from unanswered email.
- **Nov 7–8: KIC priority** — inspect organizer template sections, finalize frozen proposal PDF and title; independent text/size/visual QA, confirm submit form. **Internal submission target Nov 10, not Nov 12**.
- **Nov 9–12: PayPal highest execution cost** — demonstrate genuine sandbox PayPal+AI flow, privacy/credential hygiene, public open-source runnable repository and safe setup, record proper public YouTube <3m, reproduce from clean environment. **Go/no-go Nov 10 EOD**: if buyer flow/working build remains impossible, do not misrepresent mocks. **Internal submit target Nov 12 evening KST**, not 05:00 next morning.
- **Nov 13–14: UGREEN Round1** — match PDF to official word/size checklist, SKILL.md and license/third-party disclosure, ZIP/hash/structure, identify unresolved legal/permission risks, owner Devpost manual entry and final receipt. **Internal target Nov 14 or Nov 15 morning KST**. Nov 15 afternoon buffer reserved, no false reliance on Nov16 16:45.
- Because work can overlap, prepare UGREEN rights response check **before** Nov13, rather than waiting for submission day. Do not assume email response will arrive. If license provenance cannot be established, seek organizer clarification or use properly authorized original material; no unauthorized reuse.
- **Portfolio priority rule:** if time short, protect confirmed KIC and UGREEN Round1 *valid* submissions instead of pushing them aside for an unverifiable PayPal demo. If all three are required, owner will need parallel prevalidation now; impossible to promise 100% completion starting Nov7.

## Feasibility judgments
- **KIC: feasible with material risk from human access/approval and final PDF.** Preliminary-only, existing draft; do not expand scope into full MVP.
- **UGREEN: feasible with highest likelihood of meeting technical Round1 submission shape from existing artifacts**, subject to rights/ownership and final human submission. Round2 NAS proof can wait unless rules change.
- **PayPal: high schedule risk** because even a green offline CI and isolated OAuth/AI probe are not a judge-runnable end-to-end integration plus licensed public repo, YouTube and English demo. Reserve 2–3+ days and enforce stop/go gate; actual work may exceed any task-level estimate.
- Any work-hours estimates are uncertain; the repo does not establish real measured burn-down hours. Do not equate task DONE counts with release readiness.

## Owner approvals and handoff
- No actual Devpost, DAKER submission, payment, API/sandbox order, credential access, repo visibility/publication changed by this audit.
- Exact organizer links above. This documentation-only audit is not a build/test/release/submit.
- On the next user resume, check the newest repo HEAD + Actions and status at submission time; dates and statuses can change. Cite source this document and latest contest pages.
