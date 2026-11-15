import test from "node:test";
import assert from "node:assert/strict";
import { assessDeliveryChain } from "../audit-e2e.mjs";

const SHA = "a".repeat(40);
const PREVIOUS = "b".repeat(40);
const MAIN_SHA = "69e584e57a3a37fa72b406d62ccddf9eef9dfcf2";
const UUID = "123e4567-e89b-12d3-a456-426614174000";
function fixture() {
  return {
    production: { http_status: 200, status: "ready", source_sha: SHA },
    delivery: { id: UUID, event: "push", repository: "hibi89/hackathon-command-center-2026",
      branch: "main", http_status: 202, receiver_status: "queued",
      delivered_at: "2026-11-15T08:00:00Z" },
    run: { id: 43691572769, name: "Kmong hub sync | delivery:" + UUID,
      actor: "kmong-hub-dispatcher[bot]", event: "workflow_dispatch", head_branch: "main",
      repository: "hibi89/hackathon-command-center-2026",
      workflow_id: 416801860, path: ".github/workflows/kmong-hub-sync.yml",
      head_sha: MAIN_SHA, status: "completed", conclusion: "success",
      created_at: "2026-11-15T08:00:10Z",
      updated_at: "2026-11-15T08:02:00Z" },
    collector: { run_id: 43691572769, outcome: "UPDATED", scanned: true, tests_passed: true,
      repositories: 35, references: 80, products: 29, missing_references: 0, fingerprint_errors: 0 },
    ledger: { run_id: 43691572769, before_sha: PREVIOUS, after_sha: SHA,
      observed_at: "2026-11-15T08:03:00Z" },
  };
}
const assess = (data, expected = SHA, expectedMain = MAIN_SHA) =>
  assessDeliveryChain(data, expected, expectedMain);
const assertRejected = (data, code, expected = SHA) => {
  const result = assess(data, expected);
  assert.equal(result.code, code);
  assert.equal(result.signed_hmac_e2e, "NOT_VERIFIED");
  assert.equal(result.score_increment, 0);
};

test("internally coherent 35/80/29 snapshot never claims signed HMAC verification", () => {
  const result = assess(fixture());
  assert.deepEqual(result, { verdict: "CORRELATED_NOT_VERIFIED",
    code: "INDEPENDENT_LIVE_ATTESTATION_REQUIRED", signed_hmac_e2e: "NOT_VERIFIED",
    score_increment: 0 });
});
test("missing actual source evidence fails incomplete", () => {
  const evidence = fixture();
  delete evidence.delivery;
  assert.equal(assess(evidence).verdict, "EVIDENCE_INCOMPLETE");
});
test("wrong expected Production SHA always blocks scoring", () =>
  assertRejected(fixture(), "PRODUCTION_SHA_NOT_MATCHED", PREVIOUS));
test("Production HTTP 200 with a different deployed SHA still blocks", () => {
  const evidence = fixture(); evidence.production.source_sha = PREVIOUS;
  assertRejected(evidence, "PRODUCTION_SHA_NOT_MATCHED");
});
test("coalesced delivery cannot impersonate queued dispatch", () => {
  const evidence = fixture(); evidence.delivery.receiver_status = "coalesced";
  assertRejected(evidence, "DELIVERY_NOT_QUEUED");
});
test("unapproved repository or branch prevents delivery correlation", () => {
  for (const [repo, branch] of [["evil/repo", "main"],
    ["hibi89/hackathon-command-center-2026", "kmong-productization"]]) {
    const evidence = fixture(); evidence.delivery.repository = repo; evidence.delivery.branch = branch;
    assertRejected(evidence, "DELIVERY_SCOPE_OR_ID_INVALID");
  }
});
test("broken UUID and wrong event both prevent correlation", () => {
  for (const [field, value] of [["id", "not-a-uuid"], ["event", "issues"]]) {
    const evidence = fixture(); evidence.delivery[field] = value;
    assertRejected(evidence, "DELIVERY_SCOPE_OR_ID_INVALID");
  }
});
test("manual or wrong bot run cannot stand in for webhook-triggered run", () => {
  for (const [field, value] of [["actor", "hibi89"], ["event", "schedule"],
    ["name", "Kmong hub sync | delivery:other"], ["head_branch", "feature/unknown"],
    ["conclusion", "failure"]]) {
    const evidence = fixture(); evidence.run[field] = value;
    assertRejected(evidence, "ACTIONS_RUN_NOT_CORRELATED");
  }
});
test("GitHub Actions real REST updated_at must exist; absent completed_at is normal", () => {
  const evidence = fixture();
  assert.equal("completed_at" in evidence.run, false);
  assert.equal(assess(evidence).verdict, "CORRELATED_NOT_VERIFIED");
  delete evidence.run.updated_at;
  assertRejected(evidence, "CAUSAL_TIMESTAMPS_INVALID");
});

test("unrelated workflow ID or path cannot impersonate central collector", () => {
  for (const [field, value] of [
    ["workflow_id", 416801861], ["path", ".github/workflows/unrelated.yml"],
    ["repository", "another-owner/hackathon-command-center-2026"],
  ]) {
    const evidence = fixture();
    evidence.run[field] = value;
    assertRejected(evidence, "ACTIONS_RUN_NOT_CORRELATED");
  }
});

test("old main SHA or untrusted independent main SHA cannot match the run", () => {
  const evidence = fixture();
  evidence.run.head_sha = PREVIOUS;
  assertRejected(evidence, "ACTIONS_RUN_NOT_CORRELATED");
  assert.equal(assess(fixture(), SHA, "not-a-sha").code, "INVALID_INPUT");
});

test("queued or in-progress Actions cannot be counted despite synthetic success", () => {
  for (const status of ["queued", "in_progress", undefined]) {
    const evidence = fixture(); evidence.run.status = status;
    assertRejected(evidence, "ACTIONS_RUN_NOT_CORRELATED");
  }
});

test("DEFERRED_BOT_BURST is never a successful scan even with green Actions", () => {
  const evidence = fixture(); evidence.collector.outcome = "DEFERRED_BOT_BURST";
  assertRejected(evidence, "COLLECTOR_NOT_SYNCED");
});
test("a missing scan or wrong inventory cannot count as UPDATED", () => {
  for (const [field, value] of [["scanned", false], ["references", 70],
    ["missing_references", 1], ["fingerprint_errors", 1]]) {
    const evidence = fixture(); evidence.collector[field] = value;
    assertRejected(evidence, "COLLECTOR_NOT_SYNCED");
  }
});
test("an unchanged ledger cannot support UPDATED", () => {
  const evidence = fixture(); evidence.ledger.after_sha = PREVIOUS;
  assertRejected(evidence, "LEDGER_READBACK_INCONSISTENT");
});
test("NO_CHANGE accepted only when before and after ledger blob SHAs are identical", () => {
  const evidence = fixture(); evidence.collector.outcome = "NO_CHANGE";
  assertRejected(evidence, "LEDGER_READBACK_INCONSISTENT");
  evidence.ledger.after_sha = PREVIOUS;
  assert.equal(assess(evidence).verdict, "CORRELATED_NOT_VERIFIED");
});
test("run and ledger IDs must match exactly", () => {
  const evidence = fixture(); evidence.ledger.run_id += 1;
  assertRejected(evidence, "LEDGER_READBACK_INCONSISTENT");
});
test("reverse causal order or timezone-less timestamps are invalid", () => {
  for (const [part, field, value] of [
    ["run", "created_at", "2026-11-15T07:00:10Z"],
    ["ledger", "observed_at", "2026-11-15T08:01:00Z"],
    ["delivery", "delivered_at", "2026-11-15T08:00:00"],
  ]) {
    const evidence = fixture(); evidence[part][field] = value;
    assertRejected(evidence, "CAUSAL_TIMESTAMPS_INVALID");
  }
});
test("invalid caller expected SHA fails closed", () => {
  assertRejected(fixture(), "INVALID_INPUT", "undefined");
  const res = assess(null);
  assert.equal(res.code, "INVALID_INPUT");
});
