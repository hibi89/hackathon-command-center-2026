# Haechong Repository Provisioner — owner-only PUBLIC GitHub repository creation

**PUBLIC-only provisioning is operational on `kmong-productization` for the owner-attributed GitHub file-request path.** Actual synthetic E2E and same-request safe rerun PASS (2026-11-18 KST): [Actions #44140981604](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/44140981604), [PUBLIC test repository](https://github.com/hibi89/haechong-provisioner-e2e-20261118-02), source/policy SHA `09bd637e1bce4441b56263f51a19b05c8de20548`, created repo `main` SHA `20639517ee6eaeaae74bfae0f41f1bc8dc4d714f`. Initial job result `CREATED`, rerun result `RESUMED`, both PASS. No existing main merge or Vercel/Production change. Implementation/verification % `UNASSESSED` (denominator not established).

## Intended mobile-first operation

Owner command: "해총아, REQ-Evidence-Auditor A/B/C를 공개(Public) 레포로 생성하고 해총 표준 공시해라".

The web GPT checks the latest central HEAD, confirms the owner-authorized names and uses the connected GitHub file-create action to add exactly one new file:

    requests/repo_provisioner/<unique-request-id>.json

The file follows the example at examples/req-evidence-auditor-abc.json. An owner-attributed push to kmong-productization triggers the GitHub Action only when REPO_PROVISIONER_ENABLED=true is enabled. The Action tests and validates the request and uses a separate limited GitHub App token to create 1-3 PUBLIC repos. It adds provenance metadata and AGENTS/HANDOFF/STATUS/REQUIREMENTS documents linking the exact central canonical SHA. The completed URLs appear in Actions logs. The GPT must read actual results before reporting success.

Every request must be a new uniquely named JSON file; editing existing requests does not retrigger creation. A new request must not be created casually from a bare "ㄱ"; require explicit user intent to provision repos.

## Owner one-time setup (manual or ChatGPT Work)

1. In GitHub Settings > Developer settings > GitHub Apps create a **dedicated** App for Repository Provisioning. Repository permissions: **Repository creation: Read and write**; **Contents: Read and write**; Metadata: Read. Do not grant Administration/Delete or org-wide permissions. Install it in the personal account hibi89 and approve new permissions. Github introduced separate repository_creation:write permission on 2026-10-13 to avoid broad Administration write.
2. In GitHub repository hibi89/hackathon-command-center-2026 > Settings > Secrets and variables > Actions, configure two secrets: REPO_PROVISIONER_APP_ID and REPO_PROVISIONER_PRIVATE_KEY. Paste credentials only in GitHub Secrets, NEVER into ChatGPT, source files, PR comments or issues. The dedicated App must grant only Repository creation write and Contents write, plus Metadata read; NO Administration/Delete. Action v2 inherits the minimal App installation permissions because it has no individual Repository creation input. PUBLIC repository names, descriptions and code must not include private/customer/secrets.
3. After explicit owner activation approval, set Actions repo variable `REPO_PROVISIONER_ENABLED=true` under Settings > Secrets and variables > Actions > Variables. Without this variable the provision job is skipped. Review the feature branch and give specific approval before integration into kmong-productization. This source branch itself is inert. DO NOT merge main or touch existing webhook/Vercel Production.
4. Submit one harmless disposable public repository request and inspect actual creation, bootstrapping, visibility and idempotent retry before using real product names.

## Command line

    python3 -B -m unittest discover -s tools/repo_provisioner -p 'test_*.py' -v
    python3 -B tools/repo_provisioner/provision.py --request examples/req-evidence-auditor-abc.json --policy-sha <40-char-central-commit>

Dry run needs no token, network or GH settings. Execute mode additionally requires --execute --confirm <matching-request-id>, GH_REPO_PROVISIONER_TOKEN and HAECHONG_PROVISIONER_ENABLE=YES_CREATE_PUBLIC_REPOS. No paid API usage by the script itself (GitHub service limits still apply).

## Fail-closed boundaries

- Only the personal account hibi89 and PUBLIC repositories are allowed, at most three per request, validated names, GitHub actor hibi89, exactly one NEW request file per push.
- Never overwrite an existing unrelated repo, mutate an existing file, change privacy, delete, rename, transfer, alter permissions or modify Production. A partially created repo remains intact; retry is allowed only with matching .haechong-provisioner.json provenance, otherwise manual recovery.
- Request schema must contain `"visibility":"public"`. Private requests are rejected and existing repositories retain their current visibility.\n- New work areas receive generic policy documents **not actual product requirements**. Project-specific REQ/SWU IDs, design, allowed paths, integration responsibilities and tests must be assigned before product P1 work begins.
- A workflow run from this branch alone does NOT establish real repository creation or GitHub App permissions. Report NOT_RUN until verified.

## Canonical sources

- https://github.com/hibi89/hackathon-command-center-2026/blob/kmong-productization/docs/strategy/OWNER_DEV_EXECUTION_CANONICAL_20261116.md
- https://github.com/hibi89/hackathon-command-center-2026/blob/kmong-productization/docs/strategy/GPT6_HIGH_STANDARD_WORK_UNIT_20261117.md

## Mandatory PUBLIC mode — 2026-11-18 user decision
All NEW GitHub repositories must be PUBLIC, with no changes to existing repository visibility. Stop if the intended repository name or description risks leaking customer data, secrets, private designs or other non-public content.
