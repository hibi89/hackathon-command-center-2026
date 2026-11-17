# Haechong primary mission guard — GitHub App focus (2026-11-15, evidence reconciled 2026-11-17)

User-directed root cause: the newest HANDOFF.md item about UPTIME OPS was incorrectly promoted above the original 90→100 GitHub App automation objective. The newest progress note must **not** override the owner-designated role.

Primary mission: GitHub App source events → existing Vercel HMAC ingress → central GitHub Actions dispatch → 35/80/29 read-only observations and snapshot. Resume commands `ㄱ` or `ㄱㄱ` target the **primary mission only**. Vercel access blockage permits adjacent GitHub App code/test/security/recovery/evidence work; it never implicitly authorizes another product build. UPTIME OPS files remain as historical code and are out of scope until fresh explicit user direction.

Automation: `check.py` verifies the exact first two governance lines in `AGENTS.md`, `STATUS.md`, `HANDOFF.md` and fields in a machine-readable policy. It rejects simple prepend/priority drift, fake 100%, removal or tampering of the pinned E2E evidence receipt, and unapproved product switch. 18 negative/positive regression tests. The dedicated read-only CI runs only when these governance paths change; no cron, webhook trigger, Vercel setting, GitHub App permission or secret change.

Two candidate solutions:
1. Instructions only in HANDOFF/STATUS: inexpensive, but a later assistant can prepend a product task, exactly what happened (rejected).
2. Immutable-at-runtime owner mission contract + top-of-file invariant + CI (selected). No infrastructure cost; stronger detection of accidental drift, but not a substitute for human review or mandatory branch protections.

Limitations: The check guards document priority and policy metadata, **not the model's future choice or all code paths**. A deliberately edited validator/workflow or changes made without CI could bypass it; this CI is not claimed to be mandatory without branch protection. Owner-approved mission changes require an explicit instruction, an auditable versioned policy/test update and separate rollout acceptance. A real signed Delivery E2E was verified on 2026-11-16: UUID `083bddec-e190-11f1-978d-156991bf2ef1` -> Production queued -> bot Actions #43859747199 -> collector NO_CHANGE -> exact ledger readback. Historical provisional engineering score stays 90/100; **official full-blueprint weighted verification remains UNASSESSED**, RELEASE HOLD. A fabricated UUID, fixture, offline consistency output, or schedule run cannot replace real live evidence.

The guard pins the exact source SHA, delivery UUID, run ID, request ID, and ledger blob as an immutable historical receipt. Its pass result certifies local policy/document consistency, **not** replayed cryptographic verification or future delivery uptime. A new official acceptance decision requires a separate evidence review.

Run offline: `python3 -B tools/haechong_mission_guard/check.py` and `python3 -B -m unittest discover -s tools/haechong_mission_guard -p 'test_*.py' -v`.

## Append-only governance updates without CI regression (2026-11-17)

**Protected invariant:** Every `AGENTS.md`, `STATUS.md` and `HANDOFF.md` on the operating branch must start with the exact two lines `MARKER` and `NEXT` defined by `check.py`. The first two lines are **not available for the latest note**. Write new notes starting at line 3; never insert after only the first line. Only use SHA-checked GitHub file updates and read back the result.

Following two CI failures caused by putting new STATUS/HANDOFF notes between the locked first two lines, the headers were restored with commits `0ce35f5e` (AGENTS), `c40717d4` (STATUS), `3e93784f` (HANDOFF). [Run #44022041391](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/44022041391) **PASS, 18 guard tests**, keeping the original guard strict.

The **pure** `compose.insert_after_mission_lock(source, addendum)` helper returns properly ordered content (or rejects bad headers/duplicate messages) without writing or exposing files. Its tests include idempotency, no override of the top two lines and unsafe inputs. No automatic production deployment/permission changes are associated with this helper.
