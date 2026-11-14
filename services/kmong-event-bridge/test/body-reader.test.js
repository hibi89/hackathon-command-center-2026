import test from "node:test";
import assert from "node:assert/strict";
import { BodyReadError, readLimitedBody } from "../lib/body-reader.js";

function streamRequest(chunks, { headers = {}, onRead = () => {} } = {}) {
  let index = 0;
  const body = new ReadableStream({
    pull(controller) {
      onRead();
      if (index < chunks.length) controller.enqueue(chunks[index++]);
      else controller.close();
    },
  });
  return new Request("https://webhook.invalid/", { method: "POST", body, duplex: "half", headers });
}
test("accept exact 1 MiB preserving raw bytes", async () => {
  const a = Buffer.alloc(524288, 1), b = Buffer.alloc(524288, 2);
  const raw = await readLimitedBody(streamRequest([a, b]));
  assert.equal(raw.length, 1048576);
  assert.ok(raw.subarray(0, a.length).equals(a));
  assert.ok(raw.subarray(a.length).equals(b));
});
test("cut off chunked oversized body before full accumulation", async () => {
  let pulls = 0;
  const r = streamRequest(
    [Buffer.alloc(524288, 1), Buffer.alloc(524289, 2), Buffer.alloc(100)],
    { onRead: () => pulls++ },
  );
  await assert.rejects(readLimitedBody(r), (e) => e instanceof BodyReadError && e.status === 413);
  assert.ok(pulls <= 3, "oversized request should not drain remaining chunks");
});
test("forged short Content-Length does not bypass actual byte cap", async () => {
  const r = streamRequest([Buffer.alloc(700), Buffer.alloc(400)], {
    headers: { "content-length": "1" },
  });
  await assert.rejects(readLimitedBody(r, 1024), (e) => e.status === 413);
});
test("reject declared oversized request before reading stream", async () => {
  let pulls = 0;
  const r = streamRequest([Buffer.alloc(10)], {
    headers: { "content-length": "1048577" }, onRead: () => pulls++,
  });
  await assert.rejects(readLimitedBody(r), (e) => e.status === 413);
});
test("invalid Content-Length is a safe 400", async () => {
  const r = streamRequest([Buffer.alloc(4)], { headers: { "content-length": "junk" } });
  await assert.rejects(readLimitedBody(r), (e) => e.status === 400);
});
test("stream read failure cannot be interpreted as a complete signed body", async () => {
  const body = new ReadableStream({
    start(controller) { controller.error(new Error("network disconnected")); },
  });
  const r = new Request("https://webhook.invalid/", { method: "POST", body, duplex: "half" });
  await assert.rejects(readLimitedBody(r), (e) => e.status === 400 && e.code === "invalid_body");
});
test("empty body allowed and invalid cap rejected", async () => {
  const r = new Request("https://webhook.invalid/", { method: "POST" });
  assert.equal((await readLimitedBody(r)).length, 0);
  await assert.rejects(readLimitedBody(r, 0), TypeError);
});
