# WORKNOVA Desk — P85 Windows acceptance gate (2026-11-14 KST)

**Status:** Formal full blueprint completion **UNASSESSED / requested 85% NOT CERTIFIED**. Keep **[작업중]**, **RELEASE HOLD**, no Kmong registration. Do not infer completion from engineering-stage labels.

## Source and exact evidence

- Repo: private hibi89/Freelancer, branch product/worknova-desk-local
- Verified product commit: 0b5354c20b1eaf1b3354432ee92f24aedbce03a4; preceding commit 7ffa1c078016f9a4fedb78a3831899202cc1eb9c.
- Added tools/windows_acceptance.py and tests/test_windows_acceptance_runner.py; updated README, STATUS, HANDOFF and docs/P85_WINDOWS_GAP_20261114.md. Three new source/test files have Git blob SHA parity with locally tested content.
- Linux Python 3.13.5 125/125 unittest PASS (previous 123 + 2 new), 0 FAIL/0 SKIP; Linux Tk 8.6 Xvfb GUI four flows PASS; existing Python-required portable ZIP rebuild PASS.
- New Windows helper intentionally returns ok:false on Linux. **Real Windows PowerShell/install/upgrade/uninstall/GUI/Word, OS ACL/encryption, standalone signed EXE, commercial font rights and actual buyer cases NOT RUN/NOT VERIFIED.** No hosted or paid CI.

## Why 85% cannot be claimed and what the owner must do

WD-01..WD-14 are the unchanged final denominator. The 100-point assessment exists only as an **unapproved proposal** (Freelancer/docs/FINAL_BLUEPRINT_WEIGHT_PROPOSAL.md). Engineering gates P50/P70/P85 are not a final-design percentage.

Recommended no-cloud/no-new-charge one-time user action: on an owned Windows 10/11 machine with existing Python 3.11+ and Tk, in the complete repo checkout run

    py -3 -B tools\windows_acceptance.py

The runner creates and cleans a temporary child LOCALAPPDATA profile with synthetic data, exercises the actual PowerShell installer without admin/policy bypass, checks upgrade/data retention/recovery and package hashes. **It does not access the user's existing customer DB or normal program folder.** The summary is not real buyer/commercial acceptance.

Alternative is GitHub hosted windows-latest Actions, potentially using/billing minutes; NOT initiated without explicit cost approval. After Windows verification, owner must approve/change full WD weights and separately review font/legal/NOTICE, customer acceptance and release. The code agent can handle remaining code changes independently.

Original PayPal repo, Freelancer main, unrelated Kmong products and user data unchanged. Product Vercel/Production N/A. **[작업중], RELEASE HOLD**.
