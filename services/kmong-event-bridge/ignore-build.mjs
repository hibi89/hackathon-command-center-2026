import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const REPO_PATH = "services/kmong-event-bridge/";
const ALWAYS_BUILD = new Set(["tools/kmong_hub_sync/source_repositories.json"]);
const WITHOUT_RUNTIME_EFFECT = new Set([
  REPO_PATH + "README.md",
  REPO_PATH + "probe-production.mjs",
]);
const SHA40 = /^[a-f0-9]{40}$/i;

export function requiresBuild(paths) {
  if (!Array.isArray(paths)) return true;
  for (const path of paths) {
    if (typeof path !== "string" || !path) return true;
    if (ALWAYS_BUILD.has(path)) return true;
    if (path.startsWith(REPO_PATH) &&
        !path.startsWith(REPO_PATH + "test/") &&
        !WITHOUT_RUNTIME_EFFECT.has(path)) return true;
  }
  return false;
}

function git(args, cwd) {
  const result = spawnSync("git", args, {
    cwd, encoding: "utf8", timeout: 10000,
    stdio: ["ignore", "pipe", "pipe"], maxBuffer: 1024 * 1024,
  });
  if (result.error || result.status !== 0) throw new Error("git comparison unavailable");
  return result.stdout.trim();
}

export function decision(env = process.env, cwd = process.cwd()) {
  const previous = env.VERCEL_GIT_PREVIOUS_SHA;
  const current = env.VERCEL_GIT_COMMIT_SHA;
  // Compare against last SUCCESSFUL deployment, not just HEAD^: failed builds may intervene.
  if (!SHA40.test(previous || "") || !SHA40.test(current || "")) {
    return { build: true, reason: "MISSING_SUCCESSFUL_DEPLOYMENT_BASELINE" };
  }
  try {
    const root = git(["rev-parse", "--show-toplevel"], cwd);
    git(["cat-file", "-e", previous + "^{commit}"], root);
    git(["cat-file", "-e", current + "^{commit}"], root);
    git(["merge-base", "--is-ancestor", previous, current], root);
    const output = git(["diff", "--no-renames", "--name-only", previous, current, "--"], root);
    const paths = output ? output.split(/\r?\n/) : [];
    const build = requiresBuild(paths);
    return { build, reason: build ? "WEBHOOK_RUNTIME_CHANGED" : "NO_WEBHOOK_RUNTIME_CHANGE" };
  } catch {
    // Shallow checkout, unavailable git objects, or non-ancestor? Build rather than lose a fix.
    return { build: true, reason: "GIT_DIFF_UNAVAILABLE_FAIL_OPEN" };
  }
}

if (process.argv[1] && fileURLToPath(import.meta.url) === process.argv[1]) {
  const result = decision();
  console.log("KMONG_VERCEL_IGNORED_BUILD_STEP:", result.reason);
  // Vercel: 0 = skip, 1 = continue building.
  process.exitCode = result.build ? 1 : 0;
}
