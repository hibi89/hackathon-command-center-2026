# WORKNOVA Desk — full final blueprint P85 verification audit (2026-11-14 KST)

**Owner objective:** actual 85% of the full canonical WD-01..WD-14 product, not completion of a bounded "P85 engineering" checklist. Evaluation weights in private `docs/FINAL_BLUEPRINT_WEIGHT_PROPOSAL.md` remain unapproved; do NOT invent an 85% pass. Official final percent **UNASSESSED / target NOT CERTIFIED**. **[작업중] / RELEASE HOLD / sale not listed**.

## Exact GitHub code and change scope

- Private product repo: `hibi89/Freelancer`, `product/worknova-desk-local` HEAD [fb71ca9a65f8d1a067a2b53eb18fbdac0580054b](https://github.com/hibi89/Freelancer/commit/fb71ca9a65f8d1a067a2b53eb18fbdac0580054b).
- Previous baseline code: `0b5354c20b1eaf1b3354432ee92f24aedbce03a4`. No changes to `Freelancer@main`, PayPal hackathon or any other product.
- New opt-in offline encrypted SQLite backup (AES-256-GCM + scrypt, optional locally installed `cryptography`), hidden password UI/CLI, authenticated new-only restore, checksum pin, no external service or customer-data transfer.
- This is **encrypted backup only**; active SQLite and restored database remain plaintext. The Python-required Windows source ZIP is NOT a signed standalone EXE. No password/key, private customer data, font or .env committed.

## Tests executed in model's Linux container

| Evidence | Actual observed status |
|---|---|
| Linux Python3.13.5 unittest | **141 PASS / 0 FAIL / 0 SKIP** (previous 125 + new 16) |
| Tk8.6 Xvfb scripted real GUI | **5/5 PASS**, incl. password dialog, backup, restore and overwrite refusal |
| Source `compileall` | PASS |
| Portable build/extract + allowlist | 15/15 source/script hashes verified PASS; CLI init/verify PASS; modified source rejected |
| Windows acceptance helper on Linux | Explicit exit3 / **NOT Windows validation**, correct safety result |
| Resource-leak warnings | Python emitted `ResourceWarning: unclosed database` during existing suite; unresolved |
| Native Windows PowerShell/GUI/Word/Defender | **NOT RUN**; no native Windows runtime, paid/private Actions budget not confirmed |
| Customer, signed EXE, legal/font rights | **NOT RUN** |

The GitHub feature code key files (`worknova_desk/__main__.py`, `gui.py`, `tests/test_secure_backup.py`, build/verifier/installer scripts) match local Git blob IDs and GitHub's returned tree. `worknova_desk/secure_backup.py` semantics were reproduced directly in GitHub; its docstrings differ from the locally exercised copy, so the local 141 tests do NOT by themselves constitute a hosted exact-SHA CI run.

## Full-scope blocker list and next

WD-01 authenticated roles/retention, WD-06 actual buyer delivery proof, WD-08 independent signature/tamperproofing, WD-09 Windows recovery and OS data protection, WD-11 real native Windows accessibility, WD-12 licensed Korean Word/PDF render, WD-13 signed Windows distribution and live DB ACL/encryption, WD-14 10 actual buyer acceptances, full tax/legal/NOTICE/support/sale signoff remain unverified.

Do not charge GitHub private Windows-hosted CI without confirmed included quota/budget approval. No Vercel Production is applicable. Preserve code rollback history, all prior registrations, the central registry's other rows, and **[작업중]** until actual WD weighted acceptance and P85 are evidenced. No user action was requested in this turn.
