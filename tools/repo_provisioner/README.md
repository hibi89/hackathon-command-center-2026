# Haechong Repository Provisioner — owner-only private GitHub repository creation

Development candidate only. **The workflow is not operational until the feature branch is reviewed/merged to kmong-productization and separate credential setup is completed.** No repositories were actually created by this candidate. No main merge, Vercel/Production changes or sensitive credential updates were done.

## Intended mobile-first operation

Owner command: "해총아, REQ-Evidence-Auditor A/B/C를 비공개 레포로 생성하고 해총 표준 공시해라".

The web GPT checks the latest central HEAD, confirms the owner-authorized names and uses the connected GitHub file-create action to add exactly one new file:

    requests/repo_provisioner/<unique-request-id>.json

The file follows the example at examples/req-evidence-auditor-abc.json. A push to kmong-productization by hibi89 triggers the GitHub Action. The Action tests and validates the request and uses a separate limited GitHub App token to create 1-3 PRIVATE repos. It adds provenance metadata and AGENTS/HANDOFF/STATUS/REQUIREMENTS documents linking the exact central canonical SHA. The completed URLs appear in Actions logs. The GPT must read actual results before reporting success.

Every request must be a new uniquely named JSON file; editing existing requests does not retrigger creation. A new request must not be created casually from a bare "ㄱ"; require explicit user intent to provision repos.

## Owner one-time setup (manual or ChatGPT Work)

1. In GitHub Settings > Developer settings > GitHub Apps create a **dedicated** App for Repository Provisioning. Repository permissions: **Repository creation: Read and write**; **Contents: Read and write**; Metadata: Read. Do not grant Administration/Delete or org-wide permissions. Install it in the personal account hibi89 and approve new permissions. Github introduced separate repository_creation:write permission on 2026-10-13 to avoid broad Administration write.
2. In GitHub repository hibi89/hackathon-command-center-2026 > Settings > Secrets and variables > Actions, configure two secrets: REPO_PROVISIONER_APP_ID and REPO_PROVISIONER_PRIVATE_KEY. Paste credentials only in GitHub Secrets, NEVER into ChatGPT, source files, PR comments or issues. The App should have access to repositories it creates and Contents write to bootstrap.
3. Review the feature branch and the workflow, then give specific approval to integrate it into kmong-productization. This source branch itself is inert. DO NOT merge main or touch existing webhook/Vercel Production.
4. Submit one harmless disposable private repository request and inspect actual creation, bootstrapping, visibility and idempotent retry before using real product names.

## Command line

    python3 -B -m unittest discover -s tools/repo_provisioner -p 'test_*.py' -v
    python3 -B tools/repo_provisioner/provision.py --request examples/req-evidence-auditor-abc.json --policy-sha <40-char-central-commit>

Dry run needs no token, network or GH settings. Execute mode additionally requires --execute --confirm <matching-request-id>, GH_REPO_PROVISIONER_TOKEN and HAECHONG_PROVISIONER_ENABLE=YES_CREATE_PRIVATE_REPOS. No paid API usage by the script itself (GitHub service limits still apply).

## Fail-closed boundaries

- Only the personal account hibi89 and PRIVATE repositories are allowed, at most three per request, validated names, GitHub actor hibi89, exactly one NEW request file per push.
- Never overwrite an existing unrelated repo, mutate an existing file, change privacy, delete, rename, transfer, alter permissions or modify Production. A partially created repo remains intact; retry is allowed only with matching .haechong-provisioner.json provenance, otherwise manual recovery.
- New work areas receive generic policy documents **not actual product requirements**. Project-specific REQ/SWU IDs, design, allowed paths, integration responsibilities and tests must be assigned before product P1 work begins.
- A workflow run from this branch alone does NOT establish real repository creation or GitHub App permissions. Report NOT_RUN until verified.

## Canonical sources

- https://github.com/hibi89/hackathon-command-center-2026/blob/kmong-productization/docs/strategy/OWNER_DEV_EXECUTION_CANONICAL_20261116.md
- https://github.com/hibi89/hackathon-command-center-2026/blob/kmong-productization/docs/strategy/GPT6_HIGH_STANDARD_WORK_UNIT_20261117.md
