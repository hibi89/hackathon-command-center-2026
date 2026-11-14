// Read-only production probe: never dispatches events or changes deployed settings.
const endpoint = process.env.KMONG_PROBE_URL || "https://kmong-hub-event-bridge.vercel.app/api/webhook";
const expected = process.env.GITHUB_SHA || "";
const sha40 = /^[0-9a-f]{40}$/i;
export function classify(status, body, expectedSha) {
  if (status === 200 && body?.status === "ready") {
    if (body.bridge_feature !== "coalesce-v1")
      return { verdict: "READY_FEATURE_UNVERIFIED", source_sha: null };
    const sourceSha = sha40.test(body.source_sha || "") ? body.source_sha : null;
    if (!sourceSha) return { verdict: "READY_VERSION_UNVERIFIED", source_sha: null };
    return { verdict: sha40.test(expectedSha) && sourceSha === expectedSha ?
      "READY_SHA_MATCHED" : "READY_SHA_NOT_MATCHED", source_sha: sourceSha };
  }
  if (status === 503 && body?.status === "not_configured")
    return { verdict: "NOT_CONFIGURED", source_sha: null };
  if (status === 401 || status === 403)
    return { verdict: "PROTECTED_OR_UNAUTHORIZED", source_sha: null };
  if (status === 404) return { verdict: "NOT_FOUND", source_sha: null };
  return { verdict: "UNVERIFIED_HTTP_" + status, source_sha: null };
}
async function main() {
  let result;
  try {
    const response = await fetch(endpoint, {
      method: "GET", redirect: "manual", headers: { Accept: "application/json" },
      signal: AbortSignal.timeout(12000),
    });
    let body = null;
    if (/application\/json/i.test(response.headers.get("content-type") || "")) {
      const raw = (await response.text()).slice(0, 2048);
      try { body = JSON.parse(raw); } catch { /* Unexpected JSON: never infer version. */ }
    }
    result = { http_status: response.status, ...classify(response.status, body, expected) };
  } catch {
    result = { http_status: null, verdict: "UNREACHABLE_OR_TIMEOUT", source_sha: null };
  }
  console.log("KMONG_PRODUCTION_GET_PROBE " + JSON.stringify(result));
  console.log("A missing or different source SHA is NOT proof of the latest code running in Production.");
  if (process.env.GITHUB_STEP_SUMMARY) {
    const { appendFileSync } = await import("node:fs");
    appendFileSync(process.env.GITHUB_STEP_SUMMARY,
      "\n### Kmong bridge public Production GET probe (not a deployment gate)\n" +
      "- HTTP: " + (result.http_status ?? "unreachable") + "; verdict: **" + result.verdict +
      "**; SHA: " + (result.source_sha || "unverified") + "\n" +
      "- GET only; no webhook POST, secrets, auth bypass, or Production setting changes.\n");
  }
}
if (process.argv[1]?.endsWith("/probe-production.mjs")) await main();
