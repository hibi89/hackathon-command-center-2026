// Pure, offline consistency gate for sanitized GitHub App -> Actions evidence.
// Never certifies HMAC verification: independent live attestation is mandatory.
import { readFileSync } from "node:fs";
import roster from "./source_repositories.json" with { type: "json" };

const SHA = /^[0-9a-f]{40}$/i;
const UUID = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;
const BOT = "kmong-hub-dispatcher[bot]";
const HUB_REPO = "hibi89/hackathon-command-center-2026";
const HUB_WORKFLOW_ID = 416801860;  // Read-only GitHub API, existing main workflow.
const HUB_WORKFLOW_PATH = ".github/workflows/kmong-hub-sync.yml";
const EXPECTED_REPOS = 35;
const EXPECTED_REFS = 80;
const EXPECTED_PRODUCTS = 29;
const allowed = new Map(roster.repositories.map(
  (entry) => [entry.repository.toLowerCase(), new Set(["main", ...entry.branches])],
));

function validTime(value) {
  if (typeof value !== "string" || !/^\d{4}-\d\d-\d\dT/.test(value) ||
      !/(?:Z|[+-]\d\d:\d\d)$/.test(value)) return null;
  const ms = Date.parse(value);
  return Number.isFinite(ms) ? ms : null;
}

function isSha(value) {
  return typeof value === "string" && SHA.test(value);
}

function failed(code, verdict = "EVIDENCE_REJECTED") {
  return { verdict, code, signed_hmac_e2e: "NOT_VERIFIED", score_increment: 0 };
}

// Evidence MUST come from independent, read-only inspection of actual sources.
// A crafted fixture may be internally consistent: never interpret it as proof.
export function assessDeliveryChain(evidence, expectedProductionSha, expectedMainSha) {
  if (!evidence || typeof evidence !== "object" || Array.isArray(evidence) ||
      !isSha(expectedProductionSha) || !isSha(expectedMainSha)) {
    return failed("INVALID_INPUT");
  }
  const { production: p, delivery: d, run: r, collector: c, ledger: l } = evidence;
  if (![p, d, r, c, l].every(x => x && typeof x === "object" && !Array.isArray(x))) {
    return failed("REQUIRED_SOURCE_MISSING", "EVIDENCE_INCOMPLETE");
  }

  if (p.http_status !== 200 || p.status !== "ready" ||
      !isSha(p.source_sha) || p.source_sha.toLowerCase() !== expectedProductionSha.toLowerCase()) {
    return failed("PRODUCTION_SHA_NOT_MATCHED");
  }
  if (typeof d.id !== "string" || !UUID.test(d.id) ||
      !["push", "workflow_run"].includes(d.event) ||
      typeof d.repository !== "string" || typeof d.branch !== "string" ||
      !allowed.get(d.repository.toLowerCase())?.has(d.branch)) {
    return failed("DELIVERY_SCOPE_OR_ID_INVALID");
  }
  if (d.http_status !== 202 || d.receiver_status !== "queued") {
    return failed("DELIVERY_NOT_QUEUED");
  }

  const expectedRunName = "Kmong hub sync | delivery:" + d.id.toLowerCase();
  if (!Number.isSafeInteger(r.id) || r.id <= 0 || r.event !== "workflow_dispatch" ||
      r.actor !== BOT || r.head_branch !== "main" ||
      r.workflow_id !== HUB_WORKFLOW_ID || r.path !== HUB_WORKFLOW_PATH ||
      r.repository !== HUB_REPO || r.status !== "completed" ||
      typeof r.head_sha !== "string" ||
      r.head_sha.toLowerCase() !== expectedMainSha.toLowerCase() ||
      typeof r.name !== "string" || r.name.toLowerCase() !== expectedRunName.toLowerCase() ||
      r.conclusion !== "success") {
    return failed("ACTIONS_RUN_NOT_CORRELATED");
  }
  if (c.run_id !== r.id || !["UPDATED", "NO_CHANGE"].includes(c.outcome) ||
      c.scanned !== true || c.tests_passed !== true ||
      c.repositories !== EXPECTED_REPOS || c.references !== EXPECTED_REFS ||
      c.products !== EXPECTED_PRODUCTS ||
      c.missing_references !== 0 || c.fingerprint_errors !== 0) {
    return failed("COLLECTOR_NOT_SYNCED");
  }
  if (l.run_id !== r.id || !isSha(l.before_sha) || !isSha(l.after_sha) ||
      (c.outcome === "UPDATED" && l.before_sha.toLowerCase() === l.after_sha.toLowerCase()) ||
      (c.outcome === "NO_CHANGE" && l.before_sha.toLowerCase() !== l.after_sha.toLowerCase())) {
    return failed("LEDGER_READBACK_INCONSISTENT");
  }
  const delivered = validTime(d.delivered_at);
  const created = validTime(r.created_at);
  // Actual GitHub Actions GET /actions/runs/{id} exposes updated_at,
  // NOT completed_at. Its final updated timestamp is a conservative
  // observable bound, not a claimed cryptographic event completion time.
  const updated = validTime(r.updated_at);
  const observed = validTime(l.observed_at);
  if ([delivered, created, updated, observed].some(t => t === null) ||
      !(delivered <= created && created <= updated && updated <= observed)) {
    return failed("CAUSAL_TIMESTAMPS_INVALID");
  }

  // Deliberately never returns VERIFIED: a supplied JSON report cannot
  // attest to HMAC computation, Vercel logs, App deliveries or GitHub reads.
  return failed("INDEPENDENT_LIVE_ATTESTATION_REQUIRED", "CORRELATED_NOT_VERIFIED");
}

async function main(argv) {
  if (argv.length !== 3 || !isSha(argv[0]) || !isSha(argv[1])) {
    console.error("Usage: node audit-e2e.mjs <trusted-production-sha> <trusted-main-sha> <sanitized-evidence.json>");
    process.exitCode = 2;
    return;
  }
  let evidence;
  try {
    evidence = JSON.parse(readFileSync(argv[2], "utf8"));
  } catch {
    console.error("Evidence could not be read or parsed (details suppressed).");
    process.exitCode = 2;
    return;
  }
  const assessment = assessDeliveryChain(evidence, argv[0], argv[1]);
  // No payloads, headers, tokens, or untrusted strings are printed.
  console.log(JSON.stringify(assessment));
  if (assessment.verdict !== "CORRELATED_NOT_VERIFIED") process.exitCode = 1;
}

if (process.argv[1] && /(?:^|[/\\])audit-e2e\.mjs$/.test(process.argv[1])) {
  await main(process.argv.slice(2));
}
