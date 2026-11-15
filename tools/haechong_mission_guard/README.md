# Haechong primary mission guard — GitHub App focus (2026-11-15)

User-directed root cause: the newest HANDOFF.md item about UPTIME OPS was incorrectly promoted above the original 90→100 GitHub App automation objective. The newest progress note must **not** override the owner-designated role.

Primary mission: GitHub App source events → existing Vercel HMAC ingress → central GitHub Actions dispatch → 35/80/29 read-only observations and snapshot. Resume commands `ㄱ` or `ㄱㄱ` target the **primary mission only**. Vercel access blockage permits adjacent GitHub App code/test/security/recovery/evidence work; it never implicitly authorizes another product build. UPTIME OPS files remain as historical code and are out of scope until fresh explicit user direction.

Automation: `check.py` verifies the exact first two governance lines in `AGENTS.md`, `STATUS.md`, `HANDOFF.md` and fields in a machine-readable policy. It rejects simple prepend/priority drift, fake 100%, lost E2E blocker and unapproved product switch. 14 negative/positive regression tests. The dedicated read-only CI runs only when these governance paths change; no cron, webhook trigger, Vercel setting, GitHub App permission or secret change.

Two candidate solutions:
1. Instructions only in HANDOFF/STATUS: inexpensive, but a later assistant can prepend a product task, exactly what happened (rejected).
2. Immutable-at-runtime owner mission contract + top-of-file invariant + CI (selected). No infrastructure cost; stronger detection of accidental drift, but not a substitute for human review or mandatory branch protections.

Limitations: The check guards document priority and policy metadata, **not the model's future choice or all code paths**. A deliberately edited validator/workflow or changes made without CI could bypass it; this CI is not claimed to be mandatory without branch protection. Owner-approved mission changes require an explicit instruction, an auditable versioned policy/test update and separate rollout acceptance. The central score stays provisional 90/100 until a **real signed webhook E2E** is independently verified. False credentials, synthetic HMAC or GitHub schedule runs never count.

Run offline: `python3 -B tools/haechong_mission_guard/check.py` and `python3 -B -m unittest discover -s tools/haechong_mission_guard -p 'test_*.py' -v`.
