import test from "node:test";
import assert from "node:assert/strict";
import { createHmac, createPrivateKey, createPublicKey, createVerify, generateKeyPairSync } from "node:crypto";
import { readFileSync } from "node:fs";
import roster from "../source_repositories.json" with { type: "json" };
import { HUB_REPO, verifySignature, eligibleEvent, signAppJwt, health, receiveWebhook, dispatchCentral, shouldCoalesceDispatch } from "../lib/receiver.js";

const SOURCE = roster.repositories.find((r) => r.repository.toLowerCase() !== HUB_REPO.toLowerCase() && r.branches.length > 0);
const HUB = roster.repositories.find((r) => r.repository.toLowerCase() === HUB_REPO.toLowerCase());
const DELIVERY = "123e4567-e89b-12d3-a456-426614174000";
const { privateKey, publicKey } = generateKeyPairSync("rsa", {
  modulusLength: 2048,
  privateKeyEncoding: { type: "pkcs8", format: "pem" },
  publicKeyEncoding: { type: "spki", format: "pem" },
});
const env = {
  KMONG_WEBHOOK_SECRET: "test-webhook-secret-not-for-production",
  KMONG_DISPATCH_ENABLED: "true",
  KMONG_DISPATCH_APP_ID: "12345",
  KMONG_DISPATCH_APP_PRIVATE_KEY: privateKey,
  KMONG_SOURCE_INSTALLATION_ID: "181468120",
};
const payload = (repository = SOURCE.repository, branch = SOURCE.branches[0]) => ({
  installation: { id: 181468120 },
  repository: { full_name: repository },
  ref: "refs/heads/" + branch,
  head_commit: { message: "update product source" },
});
function incoming(kind, obj, options = {}) {
  const raw = options.raw || JSON.stringify(obj);
  const sig = "sha256=" + createHmac("sha256", options.secret || env.KMONG_WEBHOOK_SECRET).update(raw).digest("hex");
  return new Request("https://bridge.invalid/api/webhook", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-Hub-Signature-256": options.signature || sig,
      "X-GitHub-Event": kind,
      "X-GitHub-Delivery": options.delivery || DELIVERY,
    },
    body: raw,
  });
}
function mockGitHub(overrides = {}) {
  const requests = [];
  let counter = 0;
  const result = async (url, init) => {
    requests.push({ url, init, body: init?.body && JSON.parse(init.body) });
    counter += 1;
    const code = overrides.errorAt === counter ? 403 : counter === 4 ? 204 : counter === 2 ? 201 : 200;
    const body = counter === 1 ? { id: 222222 } :
      counter === 2 ? {
        token: "fake-one-hour-token",
        repositories: [{ full_name: HUB_REPO }],
        permissions: { actions: overrides.actions || "write" },
      } : counter === 3 ? { workflow_runs: overrides.workflowRuns ?? [] } : null;
    return new Response(body === null ? null : JSON.stringify(body), {
      status: code, headers: body ? { "content-type": "application/json" } : {},
    });
  };
  return { requests, result };
}

test("source allowlist mirrors canonical roster without widening inventory", () => {
  const original = JSON.parse(readFileSync(new URL("../../../tools/kmong_hub_sync/source_repositories.json", import.meta.url)));
  assert.deepEqual(roster, original);
  assert.equal(roster.repositories.length, 35);
  assert.equal(roster.repositories.reduce((n, r) => n + r.branches.length, 0), 45);
});

test("newly covered product branches accept only approved push and blueprint workflow events", () => {
  const required = [
    ["hibi89/candle_scraper", "feature/kmong-collector-p95-delivery-integrity-20261112"],
    ["hibi89/data2web_studio", "feature/final-blueprint-p85-evidence-20261113"],
    ["hibi89/SOVIA_sovereign", "feature/kmong-la-review-p2-20261112"],
    ["hibi89/RAG_STUDIO", "feature/p546-rag-prep-mapping"],
    ["hibi89/astra_pdf_redesigner", "integration/astra-commercial-core"],
    ["hibi89/candle_scraper", "feature/coin-pattern-p85-forward-eval-20261112"],
    ["hibi89/EAI", "feature/kmong-eai-85-p31-20261112"],
    ["hibi89/AX_MART", "feature/pc-care-p15-p18-85-20261112"],
    ["hibi89/factory-ax-ecosystem", "feature/data-verify"],
    ["hibi89/Freelancer", "product/bid-ax-public-procurement"],
  ];
  assert.equal(required.length, 10);
  for (const [repo, branch] of required) {
    assert.equal(eligibleEvent("push", payload(repo, branch)), true, repo + "@" + branch);
    assert.equal(eligibleEvent("workflow_run", {
      repository: { full_name: repo },
      action: "completed",
      workflow_run: {
        head_branch: branch,
        path: repo + "/.github/workflows/final-blueprint-gate.yml@main",
      },
    }), true, repo + "@" + branch);
  }
  assert.equal(eligibleEvent("push", payload(HUB_REPO, "kmong-productization")), false);
  assert.equal(eligibleEvent("push", payload(required[0][0], "unrelated-unsafe-branch")), false);
});

test("signature validation constant-time, rejects missing and tampered input", () => {
  const raw = Buffer.from('{"ok":true}');
  const sig = "sha256=" + createHmac("sha256", "key").update(raw).digest("hex");
  assert.equal(verifySignature(raw, sig, "key"), true);
  assert.equal(verifySignature(Buffer.from('{"ok":false}'), sig, "key"), false);
  assert.equal(verifySignature(raw, "sha256=1", "key"), false);
  assert.equal(verifySignature(raw, "", "key"), false);
  assert.equal(verifySignature(raw, sig, ""), false);
});
test("ignore untrusted repo and branches, reject tags", () => {
  assert.equal(eligibleEvent("push", payload("outside/fake", "main")), false);
  assert.equal(eligibleEvent("push", payload(SOURCE.repository, "not-in-roster")), false);
  assert.equal(eligibleEvent("push", { ...payload(), ref: "refs/tags/v1" }), false);
  assert.equal(eligibleEvent("push", payload()), true);
});
test("ignore non-tracked central hub branch and generated observation commits", () => {
  assert.ok(HUB);
  assert.equal(HUB.branches.includes("kmong-productization"), false);
  const p = payload(HUB_REPO, "kmong-productization");
  p.head_commit.message = "chore(kmong): refresh read-only GitHub evidence snapshot [skip ci]";
  assert.equal(eligibleEvent("push", p), false);
  p.head_commit.message = "docs: user status update";
  assert.equal(eligibleEvent("push", p), false);
  assert.equal(eligibleEvent("push", payload(HUB_REPO, "main")), true);
});
test("only final blueprint completed runs are relevant", () => {
  const r = {
    repository: { full_name: SOURCE.repository },
    action: "completed",
    workflow_run: {
      head_branch: SOURCE.branches[0],
      path: SOURCE.repository + "/.github/workflows/final-blueprint-gate.yml@main",
    },
  };
  assert.equal(eligibleEvent("workflow_run", r), true);
  assert.equal(eligibleEvent("workflow_run", { ...r, action: "requested" }), false);
  assert.equal(eligibleEvent("workflow_run", {
    ...r, workflow_run: { ...r.workflow_run, path: ".github/workflows/other.yml" },
  }), false);
});
test("JWT is signed RS256 and has constrained lifetime", () => {
  const jwt = signAppJwt("12345", privateKey, 2000000000);
  const [head, body, sig] = jwt.split(".");
  assert.deepEqual(JSON.parse(Buffer.from(head, "base64url").toString()), { alg: "RS256", typ: "JWT" });
  assert.deepEqual(JSON.parse(Buffer.from(body, "base64url").toString()), {
    iat: 1999999940, exp: 2000000540, iss: "12345",
  });
  const verifier = createVerify("RSA-SHA256");
  verifier.update(head + "." + body);
  verifier.end();
  assert.equal(verifier.verify(publicKey, Buffer.from(sig, "base64url")), true);
  assert.throws(() => signAppJwt("", privateKey));
  assert.throws(() => signAppJwt("12345", ""));
});
test("health requires all dispatch credentials and enabled flag", async () => {
  assert.equal((await health(env).json()).status, "ready");
  assert.equal(health({ ...env, KMONG_DISPATCH_ENABLED: "false" }).status, 503);
});
test("signed ping accepted without any dispatch", async () => {
  const { result, requests } = mockGitHub();
  const r = await receiveWebhook(incoming("ping", { zen: "hi" }), env, result);
  assert.equal(r.status, 200);
  assert.equal((await r.json()).status, "pong");
  assert.equal(requests.length, 0);
});
test("unsigned or bad delivery requests never call GitHub", async () => {
  const { result, requests } = mockGitHub();
  assert.equal((await receiveWebhook(incoming("push", payload(), { signature: "sha256=" + "0".repeat(64) }), env, result)).status, 401);
  assert.equal((await receiveWebhook(incoming("push", payload(), { delivery: "bad-id" }), env, result)).status, 400);
  assert.equal(requests.length, 0);
});
test("invalid JSON with valid HMAC rejects, unknown event ignored", async () => {
  const { result, requests } = mockGitHub();
  assert.equal((await receiveWebhook(incoming("push", payload(), { raw: "{" }), env, result)).status, 400);
  assert.equal((await receiveWebhook(incoming("issues", payload()), env, result)).status, 202);
  assert.equal(requests.length, 0);
});
test("ignore unapproved repos/branches and prevent feedback loops", async () => {
  const { result, requests } = mockGitHub();
  assert.equal((await receiveWebhook(incoming("push", payload("evil/other", "main")), env, result)).status, 202);
  const p = payload(HUB_REPO, "kmong-productization");
  p.head_commit.message = "chore(kmong): refresh read-only GitHub evidence snapshot [skip ci]";
  assert.equal((await receiveWebhook(incoming("push", p), env, result)).status, 202);
  assert.equal(requests.length, 0);
});
test("reject unexpected installation and disabled dispatch", async () => {
  const { result, requests } = mockGitHub();
  const p = payload();
  p.installation.id = 42;
  assert.equal((await receiveWebhook(incoming("push", p), env, result)).status, 403);
  assert.equal((await receiveWebhook(incoming("push", payload()), { ...env, KMONG_DISPATCH_ENABLED: "false" }, result)).status, 503);
  assert.equal(requests.length, 0);
});
test("signed tracked push queues one hub-only Actions dispatch", async () => {
  const { result, requests } = mockGitHub();
  const response = await receiveWebhook(incoming("push", payload()), env, result);
  assert.equal(response.status, 202);
  assert.equal((await response.json()).status, "queued");
  assert.equal(requests.length, 4);
  assert.equal(requests[0].url, "https://api.github.com/repos/" + HUB_REPO + "/installation");
  assert.equal(requests[1].body.repositories.length, 1);
  assert.deepEqual(requests[1].body.permissions, { actions: "write" });
  assert.equal(requests[2].url, "https://api.github.com/repos/" + HUB_REPO + "/actions/workflows/kmong-hub-sync.yml/runs?event=workflow_dispatch&per_page=30");
  assert.equal(requests[3].url, "https://api.github.com/repos/" + HUB_REPO + "/actions/workflows/kmong-hub-sync.yml/dispatches");
  assert.deepEqual(requests[3].body, { ref: "main", inputs: { dry_run: "false" } });
});
test("API failure is surfaced and does not claim queue success", async () => {
  const { result, requests } = mockGitHub({ errorAt: 3 });
  const response = await receiveWebhook(incoming("push", payload()), env, result);
  assert.equal(response.status, 502);
  assert.equal((await response.json()).status, "dispatch_failed");
  assert.equal(requests.length, 3);
});
test("refuse wider-than-one-repository dispatch token", async () => {
  const { result } = mockGitHub({ actions: "read" });
  await assert.rejects(dispatchCentral(env, result), /hub Actions:write/);
});
test("serverless body cap rejects payload before GitHub API calls", async () => {
  const { result, requests } = mockGitHub();
  const tooBig = { ...payload(), junk: "X".repeat(1048576) };
  const request = incoming("push", tooBig);
  const response = await receiveWebhook(request, env, result);
  assert.equal(response.status, 413);
  assert.equal(requests.length, 0);
});

test("recent bot workflow dispatch coalesces before POST without storing private data", async () => {
  const recent = [{ event: "workflow_dispatch", actor: { login: "kmong-hub-dispatcher[bot]" },
    conclusion: "success", created_at: new Date().toISOString() }];
  const { result, requests } = mockGitHub({ workflowRuns: recent });
  const response = await receiveWebhook(incoming("push", payload()), env, result);
  assert.equal(response.status, 202);
  assert.equal((await response.json()).status, "coalesced");
  assert.equal(requests.length, 3);
  assert.equal(requests.some((r) => r.url.endsWith("/dispatches")), false);
});

test("other actor and cancelled bot runs cannot suppress an eligible event", async () => {
  for (const run of [
    { event: "workflow_dispatch", actor: { login: "hibi89" }, created_at: new Date().toISOString() },
    { event: "workflow_dispatch", actor: { login: "kmong-hub-dispatcher[bot]" },
      conclusion: "cancelled", created_at: new Date().toISOString() },
  ]) {
    const { result, requests } = mockGitHub({ workflowRuns: [run] });
    const response = await receiveWebhook(incoming("push", payload()), env, result);
    assert.equal((await response.json()).status, "queued");
    assert.equal(requests.length, 4);
  }
});

test("fixed 30-minute UTC buckets match the existing collector burst guard", () => {
  const nowMs = Date.parse("2026-11-14T03:01:00Z");
  const bot = (date) => ({ event: "workflow_dispatch", actor: { login: "kmong-hub-dispatcher[bot]" },
    created_at: date });
  assert.equal(shouldCoalesceDispatch({ workflow_runs: [bot("2026-11-14T03:00:00Z")] }, nowMs), true);
  assert.equal(shouldCoalesceDispatch({ workflow_runs: [bot("2026-11-14T02:59:59Z")] }, nowMs), false);
  assert.equal(shouldCoalesceDispatch({ workflow_runs: [] }, nowMs), false);
  assert.throws(() => shouldCoalesceDispatch({ workflow_runs: "unexpected" }, nowMs));
  assert.throws(() => shouldCoalesceDispatch({ workflow_runs: [bot("not-a-date")] }, nowMs));
  assert.throws(() => shouldCoalesceDispatch({ workflow_runs: [bot("2026-11-14T03:10:00Z")] }, nowMs));
});

test("ambiguous full GitHub history page fails closed to prevent bot burst", () => {
  const nowMs = Date.parse("2026-11-14T03:01:00Z");
  const page = Array.from({ length: 30 }, (_, n) => ({
    event: "workflow_dispatch", actor: { login: "hibi89" },
    created_at: "2026-11-14T03:00:30Z", id: n + 1,
  }));
  assert.equal(shouldCoalesceDispatch({ workflow_runs: page }, nowMs), true);
});

test("GitHub history GET failure stops dispatch fail-closed", async () => {
  const { result, requests } = mockGitHub({ errorAt: 3 });
  const response = await receiveWebhook(incoming("push", payload()), env, result);
  assert.equal(response.status, 502);
  assert.equal((await response.json()).status, "dispatch_failed");
  assert.equal(requests.length, 3);
  assert.equal(requests.some((r) => r.url.endsWith("/dispatches")), false);
});

test("public health response exposes only a validated deployment commit, not credentials", async () => {
  const valid = "a".repeat(40);
  const good = await health({ ...env, VERCEL_GIT_COMMIT_SHA: valid }).json();
  assert.deepEqual(good, { status: "ready", source_sha: valid, bridge_feature: "coalesce-v1" });
  const bad = await health({ ...env, VERCEL_GIT_COMMIT_SHA: "untrusted_value" }).json();
  assert.deepEqual(bad, { status: "ready", source_sha: null, bridge_feature: "coalesce-v1" });
  const disabled = await health({ ...env, KMONG_DISPATCH_ENABLED: "false", VERCEL_GIT_COMMIT_SHA: valid }).json();
  assert.deepEqual(disabled, { status: "not_configured", source_sha: valid, bridge_feature: "coalesce-v1" });
});
test("read-only deployment probe distinguishes SHA match from unknown and disabled", async () => {
  const { classify } = await import("../probe-production.mjs");
  const sha = "a".repeat(40);
  assert.deepEqual(classify(200, { status: "ready", bridge_feature: "coalesce-v1", source_sha: sha }, sha),
    { verdict: "READY_SHA_MATCHED", source_sha: sha });
  assert.equal(classify(200, { status: "ready", bridge_feature: "coalesce-v1" }, sha).verdict, "READY_VERSION_UNVERIFIED");
  assert.equal(classify(200, { status: "ready" }, sha).verdict, "READY_FEATURE_UNVERIFIED");
  assert.equal(classify(200, { status: "ready", bridge_feature: "coalesce-v1", source_sha: sha }, "b".repeat(40)).verdict, "READY_SHA_NOT_MATCHED");
  assert.equal(classify(503, { status: "not_configured" }, sha).verdict, "NOT_CONFIGURED");
  assert.equal(classify(403, {}, sha).verdict, "PROTECTED_OR_UNAUTHORIZED");
  assert.equal(classify(404, {}, sha).verdict, "NOT_FOUND");
});

test("forged small Content-Length on streamed oversized webhook fails before dispatch", async () => {
  const { result, requests } = mockGitHub();
  const raw = Buffer.from(JSON.stringify({ ...payload(), junk: "X".repeat(1048576) }));
  const sig = "sha256=" + createHmac("sha256", env.KMONG_WEBHOOK_SECRET).update(raw).digest("hex");
  const stream = new ReadableStream({
    start(controller) {
      controller.enqueue(raw.subarray(0, 524288));
      controller.enqueue(raw.subarray(524288));
      controller.close();
    },
  });
  const req = new Request("https://bridge.invalid/api/webhook", {
    method: "POST", duplex: "half", body: stream,
    headers: {
      "content-length": "1",
      "x-hub-signature-256": sig,
      "x-github-event": "push",
      "x-github-delivery": DELIVERY,
    },
  });
  const response = await receiveWebhook(req, env, result);
  assert.equal(response.status, 413);
  assert.equal((await response.json()).status, "too_large");
  assert.equal(requests.length, 0);
});

test("single 8.5-second maximum dispatch budget fails closed on stalled GitHub call", async () => {
  const stalled = (_, init) => new Promise((resolve, reject) => {
    if (init.signal.aborted) return reject(init.signal.reason);
    init.signal.addEventListener("abort", () => reject(init.signal.reason), { once: true });
  });
  // AbortSignal.timeout() uses unref'ed timers. Keep the synthetic stalled
  // fetch test alive so the timeout can actually be observed in Node's test runner.
  const keepAlive = setTimeout(() => {}, 250);
  try {
    await assert.rejects(dispatchCentral(env, stalled, 25), (error) => error.name === "TimeoutError");
  } finally {
    clearTimeout(keepAlive);
  }
  await assert.rejects(dispatchCentral(env, stalled, 8501), TypeError);
});
