# Final blueprint evidence gate (2026-11-13 KST)

The standard-library verifier is in tools/final_blueprint_gate/verify.py.
A caller's tiny Actions workflow invokes the shared workflow from this public
repository; private code stays on its own GitHub runner. No private artifacts
are uploaded to this public command center.

On push: if docs/final_blueprint_evidence.json is absent, the result is
UNASSESSED (not 0%, and not a certification). When present, the checker
validates schema, declared owner approval reference, blueprint SHA256,
unique requirements, full 100-point rubric, evidence URL shape, and refuses
numeric official completion before independent acceptance.

Example manifest:
    {
      "schema_version": 1,
      "product": "EXAMPLE",
      "blueprint": {
        "path": "REQUIREMENTS.md",
        "sha256": "SHA256_OF_APPROVED_FILE",
        "owner_approval_reference": "OWNER_APPROVAL_REFERENCE"
      },
      "requirements": [
        {"id": "R1", "weight": 100, "status": "UNVERIFIED", "evidence": []}
      ],
      "official_final_completion": "UNASSESSED"
    }

Limitations: This checker does not prove that tests passed, that reported tests
cover a requirement, that approval references are authentic, or that all
requirements were included. Those require independent review and additional
verification. Green CI means evidence format acceptable or manifest absent,
NOT final-product acceptance. Existing 85/95 engineering values remain history.

Automatic cross-repository writes to kmong-productization are NOT configured:
the caller GITHUB_TOKEN cannot write to another repository. A separately
authorized scoped credential/GitHub App would be needed. The central ledger
stays unchanged until evidence is independently verified and authorized.

No secrets, paid API, new credential, deployment, branch protection, or
write permissions are used.

## Schema hardening — 2026-11-13 KST

- Every provided evidence item is now syntactically checked, including `UNVERIFIED` and `BLOCKED` entries. `PARTIAL` claims, like `VERIFIED`, require same-repository CI run URL, test ID and exact source-SHA-shaped reference; otherwise mark `UNVERIFIED`.
- Reject boolean `schema_version=true` and unhashable requirement status values as structured invalid inputs instead of mistakenly accepting or throwing an unhandled exception.
- Four added negative regression tests bring the structural unit-test suite from 6 to 10 cases. These checks do **not** verify whether a CI run exists or passed, whether a SHA matches that run, whether all owner-approved requirements were retained, or whether a user actually approved the blueprint. They cannot certify a numeric official score.
- No caller workflow, private product code, product manifests, permissions, external API calls, secret, production deployment, central ledger score, or previous history changed.
