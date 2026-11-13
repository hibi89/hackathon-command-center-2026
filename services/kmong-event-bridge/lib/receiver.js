import { createHmac, createSign, timingSafeEqual } from "node:crypto";
import roster from "../source_repositories.json" with { type: "json" };

export const HUB_REPO = "hibi89/hackathon-command-center-2026";
export const HUB_WORKFLOW = "kmong-hub-sync.yml";
const MAX_BODY = 1024 * 1024;
const DELIVERY_RE = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;
const API_ROOT = "https://api.github.com";
const ALLOWLIST = new Map(roster.repositories.map((item) => [
  item.repository.toLowerCase(),
  new Set(["main", ...item.branches]),
]));

export function verifySignature(raw, provided, secret) {
  if (!secret || typeof provided !== "string" || !/^sha256=[a-f0-9]{64}$/i.test(provided)) {
    return false;
  }
  const expected = createHmac("sha256", secret).update(raw).digest();
  const received = Buffer.from(provided.slice(7), "hex");
  return received.length === expected.length && timingSafeEqual(received, expected);
}

export function eligibleEvent(kind, data) {
  if (!data || typeof data !== "object" || !data.repository ||
      typeof data.repository.full_name !== "string") {
    return false;
  }
  const fullName = data.repository.full_name.toLowerCase();
  const branches = ALLOWLIST.get(fullName);
  if (!branches) return false;
  if (kind === "push") {
    if (typeof data.ref !== "string" || !data.ref.startsWith("refs/heads/")) return false;
    const branch = data.ref.slice("refs/heads/".length);
    if (!branches.has(branch)) return false;
    // The collector writes this file itself. Re-dispatching it creates an infinite feedback loop.
    if (fullName === HUB_REPO.toLowerCase() && branch === "kmong-productization" &&
        typeof data.head_commit?.message === "string" &&
        data.head_commit.message.startsWith("chore(kmong): refresh read-only GitHub evidence snapshot")) {
      return false;
    }
    return true;
  }
  if (kind === "workflow_run") {
    if (data.action !== "completed" || !data.workflow_run) return false;
    const run = data.workflow_run;
    if (typeof run.head_branch !== "string" || !branches.has(run.head_branch)) return false;
    const path = String(run.path || data.workflow?.path || "");
    return /(^|\/)final-blueprint-gate\.ya?ml(?:@[^ ]*)?$/i.test(path) ||
      run.name === "Final blueprint completion evidence gate";
  }
  return false;
}

export function signAppJwt(appId, privateKey, nowSeconds = Math.floor(Date.now() / 1000)) {
  if (!/^\d+$/.test(String(appId || "")) || !privateKey ||
      !privateKey.includes("PRIVATE KEY")) {
    throw new Error("invalid dispatch app configuration");
  }
  const segment = (obj) => Buffer.from(JSON.stringify(obj)).toString("base64url");
  const unsigned = segment({ alg: "RS256", typ: "JWT" }) + "." +
                   segment({ iat: nowSeconds - 60, exp: nowSeconds + 540, iss: String(appId) });
  const signer = createSign("RSA-SHA256");
  signer.update(unsigned);
  signer.end();
  return unsigned + "." + signer.sign(privateKey.replace(/\\n/g, "\n"), "base64url");
}

async function githubRequest(fetchImpl, path, token, method = "GET", body = undefined) {
  const response = await fetchImpl(API_ROOT + path, {
    method,
    headers: {
      Authorization: "Bearer " + token,
      Accept: "application/vnd.github+json",
      "X-GitHub-Api-Version": "2022-11-28",
      "Content-Type": "application/json",
      "User-Agent": "kmong-event-bridge",
    },
    body: body === undefined ? undefined : JSON.stringify(body),
    signal: AbortSignal.timeout(8000),
  });
  if (!response.ok) {
    throw new Error("GitHub API returned HTTP " + response.status);
  }
  if (response.status === 204) return {};
  return response.json();
}

export async function dispatchCentral(env, fetchImpl = fetch) {
  const jwt = signAppJwt(env.KMONG_DISPATCH_APP_ID, env.KMONG_DISPATCH_APP_PRIVATE_KEY);
  const installation = await githubRequest(
    fetchImpl, "/repos/" + HUB_REPO + "/installation", jwt);
  if (!Number.isInteger(installation.id) || installation.id < 1) {
    throw new Error("dispatch installation not found");
  }
  const token = await githubRequest(
    fetchImpl, "/app/installations/" + installation.id + "/access_tokens", jwt, "POST",
    { repositories: [HUB_REPO.split("/")[1]], permissions: { actions: "write" } });
  if (!token.token || !Array.isArray(token.repositories) || token.repositories.length !== 1 ||
      token.repositories[0].full_name?.toLowerCase() !== HUB_REPO.toLowerCase() ||
      token.permissions?.actions !== "write") {
    throw new Error("dispatch token must be limited to hub Actions:write");
  }
  await githubRequest(fetchImpl,
    "/repos/" + HUB_REPO + "/actions/workflows/" + HUB_WORKFLOW + "/dispatches",
    token.token, "POST", { ref: "main", inputs: { dry_run: "false" } });
}

function answer(status, obj) {
  return Response.json(obj, {
    status,
    headers: { "Cache-Control": "no-store" },
  });
}

export function health(env) {
  const configured = Boolean(env.KMONG_WEBHOOK_SECRET && env.KMONG_DISPATCH_APP_ID &&
    env.KMONG_DISPATCH_APP_PRIVATE_KEY && env.KMONG_DISPATCH_ENABLED === "true");
  return answer(configured ? 200 : 503, { status: configured ? "ready" : "not_configured" });
}

export async function receiveWebhook(request, env, fetchImpl = fetch) {
  if (!env.KMONG_WEBHOOK_SECRET) return answer(503, { status: "not_configured" });
  const providedLength = Number(request.headers.get("content-length") || 0);
  if (providedLength > MAX_BODY) return answer(413, { status: "too_large" });
  const raw = Buffer.from(await request.arrayBuffer());
  if (raw.length > MAX_BODY) return answer(413, { status: "too_large" });
  if (!verifySignature(raw, request.headers.get("x-hub-signature-256"),
                       env.KMONG_WEBHOOK_SECRET)) {
    return answer(401, { status: "invalid_signature" });
  }
  const delivery = request.headers.get("x-github-delivery");
  if (!delivery || !DELIVERY_RE.test(delivery)) {
    return answer(400, { status: "invalid_delivery" });
  }
  const event = request.headers.get("x-github-event") || "";
  if (event === "ping") return answer(200, { status: "pong" });
  if (event !== "push" && event !== "workflow_run") {
    return answer(202, { status: "ignored" });
  }
  let data;
  try {
    data = JSON.parse(raw.toString("utf8"));
  } catch {
    return answer(400, { status: "invalid_json" });
  }
  if (!eligibleEvent(event, data)) return answer(202, { status: "ignored" });
  if (env.KMONG_SOURCE_INSTALLATION_ID &&
      String(data.installation?.id) !== String(env.KMONG_SOURCE_INSTALLATION_ID)) {
    return answer(403, { status: "unexpected_installation" });
  }
  if (env.KMONG_DISPATCH_ENABLED !== "true" || !env.KMONG_DISPATCH_APP_ID ||
      !env.KMONG_DISPATCH_APP_PRIVATE_KEY) {
    return answer(503, { status: "dispatch_not_configured" });
  }
  try {
    await dispatchCentral(env, fetchImpl);
    // A 204 from GitHub means the workflow was queued, not that its job succeeded.
    return answer(202, { status: "queued" });
  } catch (error) {
    console.error("kmong webhook dispatch failed:", error instanceof Error ? error.message : "unknown");
    return answer(502, { status: "dispatch_failed" });
  }
}
