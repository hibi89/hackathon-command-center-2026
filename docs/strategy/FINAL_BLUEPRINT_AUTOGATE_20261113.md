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

## Read-only same-repository canonical fingerprint gate (2026-11-13 KST)
- For the audited HAE ecosystem, `canonical_pins.json` records the observed Git blob SHA of `hibi89/HAE@main/docs/ECOSYSTEM_CANONICAL.md`; it is **not a signed owner approval or an approved 100-point rubric**.
- The reusable workflow checks out the caller's own `main` into `.final-blueprint-canonical` **only for `hibi89/HAE`**, using the existing read-only caller token. Private bytes stay inside that caller job; the public repo stores only a file path and fingerprint.
- The additional check fails closed for a missing/moved main blueprint, missing/duplicated required pin, inaccessible checkout, unsafe path, or changed Git blob. It runs **before** manifest inspection; no manifest still means official `UNASSESSED`, not certification.
- The other 34 repositories are not yet pinned and remain `NOT_CONFIGURED`. Updating the central registry without independent review is not secure approval; branch protection/signatures would require separate consent.
- The check does not prove semantic requirement coverage, CI evidence authenticity, the user's rubric approval, functional completion or product readiness. It does not automatically write into `kmong-productization` or change any product score.

## 35-repository main-tree discovery: 28 anchor fingerprints / 7 no anchor (2026-11-13)

- Read-only Git Trees scans covered 35/35 inventory repositories' `main` branches. Found 28/35 plausible documentation anchor files and recorded exact Git blob fingerprints with `main` ref. Other 7 currently have no defensible final-blueprint anchor in `main`: `AI_AutoML_Analyst`, `self-hosted-n8n-reliability-lab`, `project-book`, `SMAX`, `RAG_STUDIO`, `EAI`, `work-hell-dungeon`. Feature-branch-only final designs still require separate review; do not treat these seven as lacking any implementation.
- Of 28, the 10 clearly named canonical/final blueprint documents are `enforce` file-integrity pins; 18 other generic requirements/specification anchors are `observe` mode, **not** approved final design. A mismatch for observe emits `DRIFT_REVIEW_REQUIRED` in the report without failing feature CI. Enforced mismatch/missing checkout fails closed.
- The reusable workflow conditionally reads the same caller repository's `main` only for the 28 known anchor repositories, with existing `contents: read`. All original 70 thin caller workflows and product source remain unchanged. The public registry contains file paths and Git blob hashes, not the private documents themselves.
- A pinned hash verifies a file's bytes at time of scan, never semantic coverage, owner-approval authenticity, CI run provenance, or acceptance of full 100% final blueprint. The official 29 product scores remain `UNASSESSED`. New code tests ensure registry identities, coverage counts and mode behavior.
