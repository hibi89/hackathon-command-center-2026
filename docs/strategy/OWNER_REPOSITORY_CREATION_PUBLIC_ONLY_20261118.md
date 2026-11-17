# Owner decision — NEW GitHub repositories PUBLIC-only (2026-11-18 KST)

Create all NEW repositories with visibility PUBLIC; reject private creation requests and never change visibility of existing repositories. Verify the API response is public. Names, descriptions, source and bootstrap docs must not contain customer material, secrets or private designs. Any risk requires HOLD. App permissions, Production, main merge, repository deletion, third-party data transmission and paid services remain separately gated.

The Repository Provisioner requires dedicated GitHub App Repository creation write and Contents write, owner-attributed new JSON request on kmong-productization and explicit repo variable `REPO_PROVISIONER_ENABLED=true` before execution. Document provenance, exact SHA and the result; unperformed E2E is NOT_RUN.
