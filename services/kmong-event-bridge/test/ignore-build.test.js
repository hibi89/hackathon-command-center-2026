import test from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { requiresBuild, decision } from "../ignore-build.mjs";

test("runtime code/config/allowlist changes always require Vercel build", () => {
  for (const path of [
    "services/kmong-event-bridge/lib/receiver.js",
    "services/kmong-event-bridge/api/webhook.js",
    "services/kmong-event-bridge/vercel.json",
    "services/kmong-event-bridge/ignore-build.mjs",
    "services/kmong-event-bridge/package.json",
    "services/kmong-event-bridge/source_repositories.json",
    "tools/kmong_hub_sync/source_repositories.json",
  ]) assert.equal(requiresBuild([path]), true, path);
});

test("docs, CI and unrelated changes can skip with a verified successful baseline", () => {
  for (const path of [
    "STATUS.md", "HANDOFF.md",
    "services/kmong-event-bridge/README.md",
    "services/kmong-event-bridge/probe-production.mjs",
    "services/kmong-event-bridge/test/receiver.test.js",
    "tools/kmong_hub_sync/quota_guard.py",
  ]) assert.equal(requiresBuild([path]), false, path);
  assert.equal(requiresBuild([]), false);
  assert.equal(requiresBuild(["README.md", "services/kmong-event-bridge/lib/receiver.js"]), true);
});

test("missing or inconsistent comparison metadata builds fail-open", () => {
  assert.equal(requiresBuild(null), true);
  assert.equal(requiresBuild([null]), true);
  assert.equal(decision({}, ".").build, true);
  assert.equal(decision({
    VERCEL_GIT_PREVIOUS_SHA: "0".repeat(40),
    VERCEL_GIT_COMMIT_SHA: "1".repeat(40),
  }, ".").build, true);
});

test("Vercel ignored build step uses safe source script and preserves function settings", () => {
  const config = JSON.parse(readFileSync(new URL("../vercel.json", import.meta.url), "utf8"));
  assert.equal(config.ignoreCommand, "node ignore-build.mjs");
  assert.equal(config.framework, null);
  assert.equal(config.functions["api/*.js"].maxDuration, 10);
});
