## 2026-11-12 KST — PREP P85 export proof, JSON integrity and 104 Linux tests (LATEST)
- Private source: hibi89/prep, feature/core-extraction; code commit **9a7e6f6cc69632158211587d87a0a6c09da674ce**, docs HEAD **b3bed36d6438b1a3603ffb686451f740becf8e4e**.
- Opt-in CSV/HTML export SHA-256 sidecar with original-source receipt; JSON normalized result/queue/mapping checksum verifier; Unicode-hidden formula risk hardening and unmapped formula review. A linked pair cannot be guaranteed crash-atomic; CSV-only output preserved by default, hash != signature.
- Linux Node22.16.0 **104/104 PASS, FAIL0 SKIP0**, separate network-disabled Linux namespace **104/104 PASS**, npm run check and npm pack dry-run PASS; freshly staged 7-file local runtime archive installed offline, CLI/SDK and CSV export+receipt validation PASS. Full GitHub docs package and hosted Actions CI NOT RUN.
- SMAX private upstream code not copied or modified; read-only comparison found different date/decimal/boolean/size/receipt semantics. Six PREP contract tests are NOT executable cross-repo golden parity; rights/compatibility gate remains. No Windows/consumer/production verification.
- PREP functional P85 candidate advanced, but official **85% NOT CERTIFIED**, 70% parity prerequisite not certified; canonical product rate **UNASSESSED**, RELEASE HOLD.
- Existing **16 active Kmong product scores untouched** (1369 percentage points / 16 = 85.5625%); independent PREP not included in the denominator. No account permission, runner-cost, license, release or private data change.

---

## 2026-11-12 KST — newer P85 Linux evidence (supersedes older 6/6-only snapshot below)
- Source/implementation SHA: PRIVATE hibi89/prep feature/core-extraction **07255335dc3b6de4f9c8c3e8bacdf06c87d4eb0e**; updated PREP documentation HEAD **bed64033fda577e8c5c892975c809e45993bff08**.
- Exact GitHub-blob-matched source and tests restored into controlled Linux Node22.16.0 environment. Full native npm test **75 PASS, 0 FAIL, 0 SKIP**; npm run check PASS. Repeated full 75/75 PASS in Linux network-disabled namespace. Six added security cases cover XSS/CSP, safe JSON keys, CSV formula-risk, file non-overwrite/cleanup and invalid UTF-8.
- package.json pack-files allowlist and local npm pack dry-run PASS; locally staged runtime tarball freshly installed offline with SDK/report/CLI smoke PASS. This did NOT include the full remote README and SDK contract docs, and was not a published package. Manual GitHub-hosted CI never dispatched; native Windows, source-rights/SMAX parity goldens and standalone CSV receipt remain unverified.
- **P85 still PARTIAL / NOT CERTIFIED; PREP standalone canonical completion UNASSESSED; RELEASE HOLD**. Hub active 16 product denominator and **1369 percentage-point total / 85.5625% average** unchanged. No private code, customer data, paid runner use or production deployment.
- See PREP STATUS/HANDOFF/ACCEPTANCE_MATRIX at docs HEAD bed64033 for full evidence and restrictions.

---

# PREP P85 hardening — PARTIAL candidate (2026-11-12 KST)

## Evidence and scope
- Original, private source: `hibi89/prep@feature/core-extraction`, code commit `29316f13818765d374aeefdd29e4420b680e3014`; docs/STATUS/HANDOFF commit `3e58e21875205376276021fc2547728f3c1832f4`.
- Implemented without SMAX import: static HTML report, user-data HTML escaping, strict offline CSP, 200-row+issue preview limit, new-only .html output via CLI, private `@private/prep-engine/sdk` preview subpath and contract, six report tests + two integration tests; CI YAML is manual-only / not invoked.
- **Actually run** Linux Node22.16.0 `node --test test/report.test.mjs`: **6/6 PASS, FAIL0, SKIP0**. `node --check src/report.mjs` PASS. Exact source/test Git blob SHA matches executed local files: `84daeeea1af5d3667d112df87d6f755aefdad2a9` / `2f55aaa4d1e466b789d0b3d4507b9a5c5dec7720`.
- **NOT RUN on updated commit**: existing 61 baseline plus 8 newly declared tests as one suite, new 2 HTML CLI integration tests, package smoke, Linux hosted CI, Windows native, any authorized consumer E2E. Earlier **61/61** PASS is valid only for older source SHA; do NOT sum to claim 69 PASS.
- **Completion:** P85 *partial implementation*, **85% milestone NOT CERTIFIED**, canonical full product completion **UNASSESSED**; previous P70 engineering feature candidate remains without formal certification. RELEASE HOLD.
- Open gates: original SMAX contract parity/rights/license and golden mapping; CSV output lacks independent receipt, HTML is only preview; Linux full CI/security suite, Windows and consumer test/owner acceptance. SHA-256 is integrity, **not authenticity**.

## Operational limits
- No original SMAX/private customer data copied; SMAX, PREP main/develop and any consuming app untouched. No paid APIs, account/billing changes, production deployment or workflow dispatch.
- Source rollback SHA `7379b80290f86d1cdefaf7215bef26326dd37f30`; document-only hub update does not change active Kmong product scores.
- Existing active 16-product completion accounting: **1369 percentage points / 16 = 85.5625% average**, unchanged; PREP remains outside denominator.
- Next: approved CI runner verification (or exact local full-suite run), source-provenance golden parity and CSV receipt/export contract hardening; assess P85 only from the acceptance matrix.

Source of truth: private PREP `HANDOFF.md`, `STATUS.md`, `docs/ACCEPTANCE_MATRIX.md`, and `docs/SDK_CONTRACT.md`.
