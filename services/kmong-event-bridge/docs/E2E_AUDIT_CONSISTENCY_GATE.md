# GitHub App → central Actions evidence-chain consistency gate

This offline tool is an **evidence consistency checker**, not a live HMAC verifier or evidence collector. It cannot award any of the central provisional 90→100 acceptance points on its own. A manually authored JSON can pass its consistency checks; independent GitHub App Recent Deliveries, existing Vercel Production SHA/logs, GitHub Actions and ledger readback remain mandatory.

Run with Node 22+ on the isolated source:

```bash
node services/kmong-event-bridge/audit-e2e.mjs \
  "<trusted-expected-deployed-commit-SHA>" \
  "<trusted-central-main-commit-SHA>" \
  /path/to/sanitized-evidence.json
```

Do not commit the JSON or secrets, raw webhook bodies, private keys, App tokens, request headers, customer data or full GitHub delivery logs. The tool prints only a fixed enum-like verdict/code and never echoes evidence. Both trusted SHAs (deployed Vercel bridge commit and central `main` commit) come from **independent read-only verification**, not the evidence file. The hub workflow ID `416801860` and exact path `.github/workflows/kmong-hub-sync.yml` are pinned to the verified existing GitHub Actions workflow; if GitHub legitimately recreates it, first reverify the ID and update the checker with a reviewed commit.

## Sanitized schema

```json
{
  "production": { "http_status": 200, "status": "ready", "source_sha": "<40-hex-sha>" },
  "delivery": {
    "id": "<github-delivery-uuid>", "event": "push",
    "repository": "<allowlisted-repository>", "branch": "<allowlisted-branch>",
    "http_status": 202, "receiver_status": "queued",
    "delivered_at": "<timestamp-with-timezone>"
  },
  "run": {
    "id": 1, "name": "Kmong hub sync | delivery:<github-delivery-uuid>",
    "actor": "kmong-hub-dispatcher[bot]", "event": "workflow_dispatch",
    "repository": "hibi89/hackathon-command-center-2026",
    "workflow_id": 416801860, "path": ".github/workflows/kmong-hub-sync.yml",
    "head_sha": "<trusted-central-main-commit-SHA>",
    "head_branch": "main", "status": "completed", "conclusion": "success",
    "created_at": "<timestamp-with-timezone>", "updated_at": "<timestamp-with-timezone>"
  },
  "collector": {
    "run_id": 1, "outcome": "UPDATED", "scanned": true, "tests_passed": true,
    "repositories": 35, "references": 80, "products": 29,
    "missing_references": 0, "fingerprint_errors": 0
  },
  "ledger": {
    "run_id": 1, "before_sha": "<40-hex-sha>",
    "after_sha": "<40-hex-sha>", "observed_at": "<timestamp-with-timezone>"
  }
}
```

GitHub's actual run REST object uses `created_at`, `updated_at`, `status`, `path`, `workflow_id`, and `head_sha`; it does not supply the former mock-only `completed_at`. The final `updated_at` is only an observation time upper bound, not cryptographic completion proof. A manually assembled run/ledger correlation may still be fabricated; do not grant E2E credit without source attestations.

All values must be copied from independently checked, real sources. `NO_CHANGE` requires identical before and after SHA; `UPDATED` requires different SHA. `DEFERRED_BOT_BURST` and `coalesced` are **not synced**. Any mismatch yields `EVIDENCE_REJECTED` or `EVIDENCE_INCOMPLETE`.

An internally consistent report returns **`CORRELATED_NOT_VERIFIED`** with `signed_hmac_e2e=NOT_VERIFIED` and `score_increment=0`. Only an independently reviewed live delivery-to-run chain can satisfy the remaining score. This never calls an external API and requires no new secrets, cloud infrastructure, branch permissions or Production changes.
