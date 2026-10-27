# REA_APP — Source-less Application Analysis & Independent Reimplementation R&D

**Recorded:** 2026-10-27 KST  
**Owner priority:** **HIGH-VALUE LONG-TERM DEVELOPMENT CANDIDATE — explicitly preserve and revisit**  
**Decision state:** Strategy/roadmap only. **Not implemented, not legally cleared for a specific third-party application, not an approved commercial claim.**  
**Existing code owner:** Private `hibi89/AX_FLOW`, `REA_APP` branch, `tools/rea-app/`. **No new repo, code move, integration, live analysis or deployment is authorized by this note.**  
**Related execution order:** **REA_APP → independent LA (Lightning Agent; historical document name Lightning Azent) → HAE (Humanized Automation Ecosystem; historical AX FLOW).**

## 1. Owner's R&D thesis — preserve verbatim intent
A useful REA_APP must not stop at reverse engineering programs with published source. **When an app's source is unavailable**, analyze its *authorized, observable behavior*, infer bounded, testable **functional contracts**, and support **independent, original-code implementations** that can be improved and compared against those contracts.

**Meaning of “변형생산” here:** design and build a distinct program with similar *legitimately observed functionality*, altered user experience or improved capabilities, using new code and authorized test data. **NOT** perfect recovery of hidden source/model/algorithms, cloning protected UI/assets, extracting secrets, bypassing access controls, or making an unauthorized derivative of third-party code.

This broadens REA_APP from **static source-intelligence tool** to a possible **evidence-driven engineering workbench**, not merely a source decompiler or an app copier.

## 2. Proposed product architecture (UNBUILT except bounded SOURCE analyzer)

| Mode | Inputs and permitted methods | Evidence output | Current status |
| --- | --- | --- | --- |
| **SOURCE** | Authorized source repositories; AST/package/import/export/call analysis; snapshot comparison | Evidence-linked architecture/dependencies, file+line citations, change impact | **Limited JS/TS analyzer implemented** on REA_APP branch; current new code SHA full regression pending |
| **BEHAVIOR** | Consented, owned or otherwise authorized web/desktop/mobile test session; UI interactions; bounded request/response and file/state observation where access terms allow | Timestamped input/output/state transitions, observed errors, reproducible fixture traces, provenance and uncertainty | **NOT IMPLEMENTED** as a dedicated REA_APP capability |
| **BINARY** | Authorized local executable or program sample; permitted static file-format/binary analysis and limited sandbox experiments | Approximate modules/imports/symbols/entrypoints, observed behavior and uncertain findings | **NOT IMPLEMENTED**; format, OS and rights limitations substantial |
| **CONTRACT** | Merge only authorized evidence across modes | Versioned independent functional specification: input/output schemas, workflow/state transitions, error cases, limits, confidence/evidence tags and unobserved zones | **NOT IMPLEMENTED** |
| **IMPLEMENTATION VERIFICATION** | Compare clean original implementation against agreed fixtures and black-box observable results | Differential tests, behavior coverage, mismatch classification, regression receipts, manual review queue | **NOT IMPLEMENTED** |

**Separation of roles:** REA_APP discovers and documents; original implementation is undertaken separately (LA for automation engine, other approved projects as appropriate); an independent verifier tests behavior. Analysis artifacts are **not executable trusted instructions**.

## 3. Key differentiator hypothesis
Common static analysis products already provide dependency graphs, references, AST rules and code impact. These functions by themselves are **not proven competitive differentiation**.

The proposed wedge is a controlled end-to-end sequence:

**authorized observation → evidence-vs-hypothesis classification → testable behavioral contract → independent implementation spec → original-code build → differential verification**.

The candidate competitive advantage is **traceability and fewer unverified assumptions** across this full workflow, especially when source code does not exist or is inaccessible. This is a **hypothesis requiring benchmarks and customer validation**, not a claim of novelty, unrestricted coverage or commercial success.

## 4. Mandatory evidence and verification semantics
- For every behavior claim record: case/fixture ID, authorization/scope, timestamp, app version or snapshot, exact visible input/output (redacted or synthetic), observed/expected result, environment, test count, reproducibility.
- Status must separate **OBSERVED / INFERRED / UNKNOWN / UNSUPPORTED**. Never infer the server algorithm, implementation language, training data, proprietary datasets or inaccessible logic from UI output alone.
- Generate clean-room, **original** contracts and tests; explicitly separate implementers from any protected source that legal review prohibits accessing.
- Treat logs, prompts, stack traces, source captures, private endpoints and customer data as sensitive; no public repo uploads, raw data exfiltration or automated credentials harvesting.
- Automated diff tests may demonstrate **observable compatibility for tested cases** only. No 100% functional equivalence, universal app recreation, all-platform support, binary source recovery or independent IP clearance claim.

## 5. Recommended phased proof (prioritized R&D proposal; NOT a running project)
1. **R0 — REA_APP current-HEAD safety/regression first.** Re-run full Python + pinned Node parser tests on the exact latest REA_APP commit, including sensitive-file exclusion and file-open race checks. Verify source is not modified.
2. **R1 — Owned synthetic web app black-box proof.** Construct a tiny original app with deliberately withheld source from the observer. Use permitted browser/session recordings to map three functions, input/output schemas, one error flow and persistent-state transitions. Produce reproducible JSON evidence and an independent functional contract. Prefer local isolated fixtures; no outside website/real accounts.
3. **R2 — Separate independent implementation + differential test.** A separate implementation reconstructs supported **observable behavior only**, with distinct UI/source. Run ≥20 explicitly scoped functional test cases covering success, error, boundary and state changes, record mismatch categories. **No success claim before execution evidence.**
4. **R3 — Authorized installed-app proof.** Repeat with one owner-created packaged app. Inspect approved file I/O and binary metadata in a sandbox, record Windows/Linux support and unknowns; do not bypass DRM, licensing, protection, anti-tamper or access controls.
5. **R4 — Evaluate utility and productization.** Compare against manual analysis and existing tools on coverage, correctness, person-hours, false confidence, and reproducible quality. Decide whether REA_APP remains an internal LA/HAE R&D tool or merits a separate paid product. No commercial differentiation claim before measured evidence.

**Initial success gate:** One owned source-less fixture app → evidence-backed functional contract → separately built implementation → ≥20 reproducible behavior tests with documented gaps. **This is a proposed acceptance target, not a performed test.**

## 6. Legal, platform, and safety gates
- First establish ownership, permission, ToS/EULA and relevant law **for each target and mode**. Publicly viewable != permitted to reverse-engineer for competitive purposes; an app install ≠ right to copy/distribute its code.
- n8n remains **documentation/rights-review limited** as recorded in private `REA_APP/tools/rea-app/CHIEF_GATE_R_REVIEW.md`. Do not run source or binary analysis of n8n or competitive benchmarking without access/contract/legal authorization; do not transplant n8n code/definitions into LA.
- No login bypass, encryption/DRM circumvention, injection into third-party systems, rate-limit evasion, secret extraction, personal-account monitoring, bulk proprietary scraping or unauthorized API calls.
- User-owned synthetic or expressly authorized targets are the default. Real user/customer inputs, paid APIs, third-party hosting, repo visibility, redistribution and deployment require their own approvals.
- Source-less service internals/AI weights cannot be inferred with certainty from black-box traces; protect third-party copyright/trademarks/trade secrets.

## 7. Priority and current hackathon freeze
**High strategic importance; deferred execution, not an immediate new sprint.** Record and do not lose the idea. Current 2026 KIC/PayPal/UGREEN **initial submission freeze** remains authoritative: `docs/strategy/20261027_SUBMISSION_SCOPE_FREEZE.md`. The REA_APP expansion must **not** alter submission PDFs, demo, Skill ZIP, product scope, deadline, code, or leadership priorities.

After the immediate submission gates and when separately scheduled, the REA_APP lead can use this as the **north-star R&D backlog**; detailed engineering remains in private `hibi89/AX_FLOW@REA_APP`. The public chief repository contains **only broad non-secret strategy**, not source/customer evidence.

## 8. Handoff reminder
When chief is next invoked, highlight: **“REA_APP future expansion to analyze source-less apps through authorized BEHAVIOR/BINARY, generate evidence-backed independent contracts, and verify independently reimplemented software; important owner-mandated development candidate, intentionally deferred until contest milestones.”** Do not mistakenly mark any of these expansion modes as implemented.
