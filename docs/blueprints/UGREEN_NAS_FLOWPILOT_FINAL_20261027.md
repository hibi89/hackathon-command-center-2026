# UGREEN — NAS FLOWPILOT: FINAL BUILD BLUEPRINT
**Status:** FINAL OWNER PRODUCT VISION, IN-CONTEST IMPLEMENTATION PROPOSED / NOT PROVEN. Existing repo only `hibi89/hibi89-ugreen-nas-hackathon@lead/ugreen`; no new repo or second contest submission. Parent: [Master](THREE_HACKATHON_MASTER_20261027.md). Existing ProjectReady remains a preserved earlier implementation artifact and a **delivery-readiness workflow template**, not the primary final product pitch. Historic G36/G37 artifact hashes/rights HOLD must not be silently rebranded or overwritten; replace as a newly authored FlowPilot Skill candidate in the existing contest repo with explicit comparison, new Creator/checker validation, user final sign-off.
**North star:** "A nonprogrammer describes a NAS task in normal language; Uliya AI plans a **supported** workflow, asks for missing parameters step by step, validates scope/authority, executes through registered expert agents and reports evidenced results." To help UGREEN compete on software usefulness rather than just NAS hardware specs. Do **not** promise replacing Synology DSM or unrestricted general-purpose automation at contest stage.

## A. Distinguish two different runtimes
**IN-CONTEST Uliya Skill:** Markdown-only `SKILL.md` + `references/*.md`; orchestrates *documented and actually registered* official NAS Expert Agents and UGOS CLI capabilities, not shell/JS/Python/Docker/n8n API. All actions must be explicitly checked against actual installed runtime, approvals and data-flow restrictions. No new persistent database, scheduler, arbitrary binary execution, HTTP posting, generic JSON external node creation or privilege escalation inside ZIP. Most useful initial workflow = user-approved read-only project handoff with adaptive slots; multiple bounded read-only workflows conditional on capabilities.
**POST-CONTEST NAS automation product:** independent already planned `hibi89/AX_FLOW` with typed validated workflow IR, local execution, SQLite ledger and user authority; optional supported NAS Docker build, SOVIA retrospective audit/risk adapter, DBVORA sanctioned read-only SQLite schema/backup/recovery and business data plane. n8n is a research reference; its official commercial licensing has to be resolved before letting outside customers generate/configure n8n workflows via API/UI/AI. Forcing n8n REST wrapper in Skill is both an unapproved runtime path and possible license issue. UGREEN does NOT automatically provide an Ollama/LLM/private off-cloud inference guarantee; document observed model/data flow.

## B. The contest Skill user story
User: "새 계약서를 보고 고객별로 정리하고, 납품 전 필수 문서가 있는지 점검해줘."
- **Intent resolution:** supported classification `HANDOFF_AUDIT` or `DOCUMENT_FIND_COMPARE` from an explicit allowlist. Unknown request => explain unsupported, offer constrained nearby template, NEVER synthesize arbitrary CLI/function.
- **Interactive required inputs:** ask only for missing `owner_authorized_root_folder`, `required_deliverables`, `candidate_project_folder`, `selection_of_final_version`, `read_content_permission` when necessary; ask user in normal language. No "enter API key into LLM chat" pattern. A generic slot list is not a guarantee of custom platform UI; Skill may ask follow-up in normal chat.
- **Plan preview:** list exactly which authorized folders/files to inspect and intended official read actions; ask user's consent for sensitive content. A requested "auto move/rename/notify everyday" should be marked **NOT_SUPPORTED / REQUIRES_SEPARATE_APPROVAL** unless actual official write/scheduler agents are validated and authorized; not silently promised.
- **Tool execution:** registered official Files Expert Agent `ug-filesystem ls/find/stat` in user scope; separately authorized Documents Expert Agent `ug-document metadata/qa/extract/reconcile` on exact selected documents **if** actual allowed and known data handling. Public capability catalog merely lists these labels; does not prove installed/runtime command syntax. Do not fabricate CLI flags, response fields, success proofs, or simulate NAS and call it live.
- **Validation:** check listing completeness, known final versions, required-document evidence and permission gaps. Required missing can be BLOCKED only when complete authorized scan proves absence; incomplete/denied => NEEDS_REVIEW. Returning "READY" requires positive proof of all mandatory checks. Avoid reading .env, .git, credentials, secrets, private keys or symlinks outside scope. No state-modifying actions without official support and user approval.
- **Output:** human-readable ordered workflow with steps and slots resolved, action outcomes, evidence references, READY/BLOCKED/NEEDS_REVIEW and next user step. Repeatable audit of same scope. Where no installed NAS agent is available, report `UNVERIFIED_RUNTIME`, not pretended completed action.

## C. FlowPilot as bounded dynamic composer rather than chatbot
A typed *logical* plan object (concept/Markdown schema, not executable arbitrary JSON engine):
```yaml
intent: HANDOFF_AUDIT
schema_version: 1
slots:
  authorized_folder: user-provided
  required_deliverables: user-provided
  content_review: separate-user-approval
steps:
  - kind: READ_FOLDER_LISTING # registered file-agent only
  - kind: CHECK_REQUIREMENTS # deterministic compare from actual evidence
  - kind: OPTIONAL_DOCUMENT_RECONCILE # authorized selected docs only
  - kind: REPORT_OUTCOME # source-linked response
outcome: READY|BLOCKED|NEEDS_REVIEW
unavailable_steps: [ ... ] # must not be invented away
```
- Intents can support e.g. locate documents, compare two authorized versions, delivery checklist verification. **No unrestricted DAG runtime in contest ZIP**.
- Slot resolution: `UNRESOLVED_REQUIRED -> ASK -> VALIDATE -> CONFIRM -> PLAN -> SAFE_TOOL -> VERIFY -> REPORT`. Tool failure => explicitly UNKNOWN/NEEDS_REVIEW. No auto-retry write.
- Small prevalidated set of "expert-agent recipes" is acceptable if officially supported; generated instructions are NOT proof of running automation. This dynamic composition is stronger than static one-purpose ProjectReady but still feasible.
- Evaluate an intentionally adversarial request asking to search outside scope or upload secrets: must refuse; an absent/partial capability should not declare finished workflow.

## D. Technology / component integration mapping
| Product | In-contest use | Full NAS ecosystem after contest |
| --- | --- | --- |
| ProjectReady NAS | Keep previous safe checklist logic and original submissions as evidence, new FlowPilot `HANDOFF_AUDIT` template rebuilt during contest | Ready-made industry template in workflow gallery |
| Existing `AX_FLOW` | **design pattern only** typed plan, input resolver, explicit approval, fail-closed checks; no runtime import or copied private source | Independent workflow runtime, event/cron where actually supported, connectors, retries, user-generated automations |
| n8n | conceptual node/trigger/reference; NO engine, REST API bridge, Python/JS shim in Skill | Optional separately licensed platform integration, or own independently developed AX_FLOW functionality |
| SOVIA | retrospective action-evidence/permission/unknown design principles as new Markdown, no Python executable | Genuine audit adapter, policy risk reports and actor/agent action records; live enforcement only separately implemented |
| DBVORA | read-only bounded file/metadata reasoning; NO local SQLite adapter in Skill ZIP | Authorized DB maps/snapshots/restore evidence behind NAS data-plane interface, never raw unrestricted NAS DB read |
| UGREEN official File/Document Expert Agents | only actual read actions verified in installed official NAS runtime | Native connector target for higher-capability product |
| local AI models | do not claim particular inference engine, perfect privacy or GPU acceleration without runtime proof | Optional owner-selected appropriately licensed local inference after real model/runtime test |

## E. Differentiation and scoring thesis
Instead of a hardcoded file-checker, describe a "Natural Language NAS Workflow Composer with Interactive Parameter Resolution and Evidence-Based Execution". Specific value: ordinary NAS owner need not build nodes, input gaps become human-readable questions rather than hallucinated defaults, and all tool effects are mapped to allowed registered capabilities. Judging dimensions (each 25%): user value, differentiation, implementation quality, fit to UGREEN AI NAS. The wedge is **native permissions and grounded NAS agent orchestration**, not running Docker software already usable on competing NAS devices.

## F. Demo matrix
Positive1: user describes vague "check delivery readiness"; Skill asks folder and required documents; owner supplies; actual official file listing covers correct authorized root; report referenced.
Positive2: two ambiguous versions of final artwork => NEEDS_REVIEW, user explicitly resolves and agent follows supported authorized flow.
Negative1: missing API/agent/action runtime => unsupported/NOT_CHECKED, no ghost automation.
Negative2: source folder incomplete, pagination/limit unknown or permissions denied => NEEDS_REVIEW (never incorrectly absent/READY).
Negative3: request to upload secret/copy outside scope/send notification or schedule execution when unsupported => refuse or park as future.
Negative4: misleading indirect/prompt injection in document filenames/content => treated as untrusted data, never instructions.
Repeat-run test: read-only actions do not modify source.
Documentation tests: exact frontmatter/schema/links/package hashes, 10 English answers ≤500 words, PDF ≤1 MB, ZIP zipped/unzipped ≤10 MB and Markdown-only file constraint, license disclosures. Check against official Creator/validator at actual source SHA. These are independent of actual NAS runtime proof.

## G. Submission and intellectual-property gates
Official: https://ugreenhackathon.devpost.com/rules, https://ugreenhackathon.devpost.com/
**Round1:** English PDF with 10 required questions, ≤500 substantive English words and ≤1 MB; package `SKILL.md` + directly linked Markdown refs, no executable scripts, <=10MB compressed/unpacked, <=1MB/file, <=100 files. Contest project and core workflow *newly authored during competition*. AI tools and third-party components/attribution/license disclosed. No real NAS or demo video required. Formal deadline **Nov16 16:45 KST** (Nov15 23:45 PST). Single UGREEN entry; its current ProjectReady package is preserved as an old candidate, not concurrently submitted as a second project.
**Round2 if finalist:** up to 30 invited around Nov21 PT, ONE official remote NAS day in Nov22–28 PT, must test same Skill and capture real NAS screen, public YouTube <3min, ZIP and video by **Dec1 16:45 KST**.
**Critical outstanding blocker from existing lead record:** official stand-alone Starter Kit applicable license / ownership rights inquiry to UGREEN sent but no verified response or entrant signoff; historic checked G36/G37 ProjectReady artifact is not approval to reuse core workflow as the NEW FlowPilot submission, nor actual NAS support. New package must undergo separate official Creator/checker and rights review, user must approve exact bytes before Devpost submission. No PDF overwrite, no publishing credentials/files in Public GitHub.

## H. Build gates (single existing UGREEN repo, priority after hard submission blockers)
**Now→Oct30:** inventory registered candidate agent read operations from official catalog. Clearly tag what is observed in documents vs verified in actual runtime. Define intent/slot/step allowlist and unsupported requests. Confirm/seek legal clarity of official kit terms.
**Oct30→Nov4:** write NEW FlowPilot Markdown `SKILL.md` + linked references; implement 2 bounded workflows, priority HANDOFF_AUDIT template, explicit user slot questions; test 6 scenarios above using offline synthetic fixtures (must label simulation).
**Nov4→Nov8:** use official creator/checker supported on local dev setup and validate source SHA; no Python/JS in ZIP. Produce concise English 10-question PDF focused on dynamic but bounded composer; all 4 evaluation dimensions and data flow.
**Nov8→Nov14:** rights review, supply exact offline checker results, compare new document to preserved old ProjectReady, consider fallback if unsupported slot-interactivity: allow supported plain-language follow-up and narrower read-only action only; don't swap to a second project after submitting Round1. Release holds on unverified license/consent, no unsupported workarounds.
**Nov14–16:** owner approves exact PDF/ZIP source/rights and final upload, preserve immutable artifacts + Devpost receipt before official 16:45 KST.
**If finalist:** preflight actual assigned NAS capability and consent, use one allotted day to record real dynamic input resolution + read tool execution + evidence report; quickly remove unsupported claims rather than fabricate runtime. Finish same-Skill ZIP+video by Dec1 16:45 KST.
**Postcontest:** AX_FLOW independent runner + user-friendly nodes/slots + local SQLite / DBVORA observability / SOVIA audit; realistic NAS hardware resource sizing and Docker compatibility; corporate partnership pitch only backed by working proof, not prizes promised.

## I. Why this beats naive "n8n JSON generation"
Generating a syntactically correct n8n JSON can still call nonexistent nodes, lack credentials, violate consent or fail at runtime. Real value is **constrained capability registry + interactive typed slot completion + deterministic checks + authorized tool execution + independent result verification**. This also distinguishes the solution from generic LLM-generated pseudocode. In the contest, it is a safe Uliya-first demonstrator. Later, full AX_FLOW can power wider workflows with approved integrations. No unsupported vendor/runtime claims.

## J. Do not claim today
No verified deployed FlowPilot Skill, no documented functioning general-purpose n8n REST bridge in contest environment, no actual NAS account access yet, no rights clearance, no SOVIA/DBVORA production module in NAS, no scored win odds. Existing ProjectReady had prior offline tests and candidate PDF/ZIP; those are separate and must not be presented as new FlowPilot pass.
