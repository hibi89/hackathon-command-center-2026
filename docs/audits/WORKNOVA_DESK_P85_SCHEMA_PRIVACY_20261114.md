# WORKNOVA Desk P85 — Schema admission & offline customer privacy (2026-11-14 KST)

## Canonical source and exact references
- Private product: `hibi89/Freelancer@product/worknova-desk-local`
- Tested and committed source: [`4d116918cc096d0a87605d07a4dd80da3ce35959`](https://github.com/hibi89/Freelancer/commit/4d116918cc096d0a87605d07a4dd80da3ce35959), Github source Blob SHA parity **18/18** against local text bytes.
- Product STATUS/HANDOFF documentation head: [`7ffa1c078016f9a4fedb78a3831899202cc1eb9c`](https://github.com/hibi89/Freelancer/commit/7ffa1c078016f9a4fedb78a3831899202cc1eb9c).
- Prior feature HEAD [`4e8adf0f61281006bcb570aa2f6282925168b0f7`](https://github.com/hibi89/Freelancer/commit/4e8adf0f61281006bcb570aa2f6282925168b0f7); unchanged main/PayPal repo and other product entries.

## Verified local implementation (NOT equivalent to final 85%)
1. WD-08/09: reject an existing unrelated `PRAGMA user_version=0` SQLite/empty file, malformed bytes, incomplete v2 table catalog/quote version columns and altered audit record *before* accepting it as an existing WORKNOVA owner ledger. Existing unapproved/foreign database bytes preserved; a SHA-matching foreign SQLite backup is also rejected without creating a recovery destination. Fresh explicit init remains v2; v1 legacy migration still requires explicit backup.
2. WD-01: customer portfolio JSON from user selection, no scope/item text/stage title/delivery note/bank references/evidence paths. Customer name redacted by default; disclosing name requires two explicit CLI flags. Output new file only, POSIX 0600, read snapshot consistency and no network. Amounts and IDs remain confidential; **no multi-user login or at-rest encryption**.
3. WD-11/13: Tk GUI customer summary export; strict allowlist extended to **14** app/script files plus `FILE_MANIFEST.json`; package requires installed Python and is NOT a signed standalone EXE or PowerShell-native proof.

## Reproducible evidence
- Development Linux Python **3.13.5**, `PYTHONPATH=. python -m unittest discover -s tests -q`: **123 PASS, 0 FAIL, 0 SKIP** (previous 104 + new 19).
- Real Tk8.6 Linux Xvfb widget automation **4/4** (quote/contract/collection, lifecycle+evidence, first-run consent, privacy summary redaction/no overwrite), but **Windows GUI NOT RUN**.
- `python -m compileall -q worknova_desk scripts`: PASS.
- Deterministic Python-source portable ZIP newly extracted into clean local directory; verifier **14/14** and `python -m worknova_desk --db ./new.sqlite init`/ `verify`: PASS, no installed Windows app tested.
- Tests use synthetic data; private customer databases, backups, tokens and commercial font files were never used or uploaded. Plaintext local financial exports are confidential and not payment certification.

## Stop / final blueprint assessment
Canonical full WD-01..14 + unapproved 100-point proposal unchanged. **Formal final completion UNASSESSED, owner target 85% NOT CERTIFIED, `[작업중]` retained, RELEASE HOLD, actual Kmong registration NOT DONE.**
Remaining: native Win10/11 non-admin PowerShell install/upgrade/rollback, signed standalone EXE, OS ACL/at-rest encryption/auth, Windows Word/PDF/font rights, buyer acceptances, tax/legal/NOTICE/support owner approval and approved final weights. No paid CI, hosted deployment, Vercel production or original PayPal changes. Product evidence is in private `docs/P85_SCHEMA_PRIVACY_20261114.md`.

Updated 2026-11-14 KST; status based on local tests and exact GitHub SHA only. This audit does NOT certify physical Windows installation, legal compliance or production readiness.
