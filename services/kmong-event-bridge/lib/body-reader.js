// Bounded, raw-byte body reader for signed GitHub webhook deliveries.
export class BodyReadError extends Error {
  constructor(status, code) {
    super(code);
    this.status = status;
    this.code = code;
  }
}

function cancelQuietly(streamOrReader) {
  if (!streamOrReader) return;
  try {
    const pending = streamOrReader.cancel();
    if (pending && typeof pending.catch === "function") pending.catch(() => {});
  } catch {
    // Returning an error response must not be blocked by cancellation failures.
  }
}

async function readWithAbort(reader, signal) {
  if (!signal) return reader.read();
  if (signal.aborted) throw new BodyReadError(503, "request_timeout");
  return new Promise((resolve, reject) => {
    const onAbort = () => {
      signal.removeEventListener("abort", onAbort);
      cancelQuietly(reader);
      reject(new BodyReadError(503, "request_timeout"));
    };
    signal.addEventListener("abort", onAbort, { once: true });
    reader.read().then(
      (value) => {
        signal.removeEventListener("abort", onAbort);
        resolve(value);
      },
      (error) => {
        signal.removeEventListener("abort", onAbort);
        reject(error);
      },
    );
  });
}

export async function readLimitedBody(request, maxBytes = 1024 * 1024, deadline = undefined) {
  if (!Number.isSafeInteger(maxBytes) || maxBytes < 1) {
    throw new TypeError("invalid max body limit");
  }
  const claimedLength = request.headers.get("content-length");
  if (claimedLength !== null) {
    if (!/^\d+$/.test(claimedLength)) {
      cancelQuietly(request.body);
      throw new BodyReadError(400, "invalid_content_length");
    }
    if (BigInt(claimedLength) > BigInt(maxBytes)) {
      cancelQuietly(request.body);
      throw new BodyReadError(413, "too_large");
    }
  }
  if (!request.body) return Buffer.alloc(0);

  const reader = request.body.getReader();
  const chunks = [];
  let size = 0;
  try {
    while (true) {
      const { done, value } = await readWithAbort(reader, deadline);
      if (done) return Buffer.concat(chunks, size);
      if (!(value instanceof Uint8Array)) {
        throw new BodyReadError(400, "invalid_body");
      }
      if (value.byteLength > maxBytes - size) {
        throw new BodyReadError(413, "too_large");
      }
      size += value.byteLength;
      chunks.push(Buffer.from(value));
    }
  } catch (error) {
    cancelQuietly(reader);
    if (error instanceof BodyReadError) throw error;
    throw new BodyReadError(400, "invalid_body");
  } finally {
    reader.releaseLock();
  }
}
