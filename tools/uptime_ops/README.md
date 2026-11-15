# UPTIME OPS — isolated local-first P0/P2 technical preview

**Owner-approved product status:** candidate \`KMONG-CAND-UPTIME-01\`, not an existing 20th listing. **NOT BUILT as commercial product / NOT REGISTERED / RELEASE HOLD.** This is an independent stdlib-only prototype, not a supported 24/7 service, and does not touch the central 19-service catalog or existing webhook Production.

## Choice and safety contract

A. Adopt an external uptime monitoring stack: ready UI, but license/dependency/hosting costs, cloud deployment and ownership require new review (deferred). B. Build a small stand-alone Python 3.11 + SQLite core: zero extra dependencies, local-first, narrower functionality and manual consent (chosen for P0/P2 prototype).

Only the exact configured HTTP(S) HEAD URI can be requested. Operator must supply \`consent: true\`, specific ownership/scope \`approval_ref\`, exact hostname/port/path, and 1–8 previously approved IP pins. DNS is verified against those pins on each live call; socket connects by numeric pin, preventing DNS rebinding between resolution and connection. Private RFC1918 targets additionally need \`allow_private: true\`; loopback, link-local (including cloud metadata), reserved, IPv4-mapped IPv6 and multicast are denied. HTTPS certificate validation remains enabled. Redirects are **not followed**, HTTP auth/cookies are not supplied, and there is no auto-discovery, port scan, credential storage, background polling or third-party notification. Hostname/URL and consent are never stored in SQLite. The consent field is an operator declaration, **not proof** that a customer actually owns the endpoint.

Every run is opt-in. \`python -m tools.uptime_ops.cli --config targets.json\` validates configuration **without network**. One authorized live sample (not to be used in CI): \`python -m tools.uptime_ops.cli --config targets.json --target owned_web --db ./uptime_ops.sqlite --live\`. Example with **synthetic values only**:

\`\`\`json
{"targets":[{"target_id":"owned_web","url":"https://example.test/health","approval_ref":"owner:sample-01","consent":true,"allowed_ips":["93.184.215.14"],"allow_private":false,"interval_seconds":60,"timeout_seconds":3}]}
\`\`\`

Use your own explicitly permitted target and verified IP pins; the synthetic example is not permission to contact that host. No live calls are run during GitHub CI.

SQLite checks preserve UTC timestamps (timezone-aware), statuses UP/DOWN/UNKNOWN and bounded evidence codes; events capture opening, recovery and **UNOBSERVED_INTERVAL** gaps greater than 2× expected interval. Replaying the exact check timestamp+result is idempotent. UNKNOWN does not silently close a DOWN incident. Export CSV using \`--db existing.sqlite --export-csv new.csv\` with config; the exporter refuses to overwrite an existing file. The prototype has **no long-running timer**, dashboards, notification integrations, retention automation or tested Windows installer; sleep/offline periods cannot be measured as uptime.

## Tests / validation

\`\`\`bash
python3 -B -m unittest discover -s tools/uptime_ops -p 'test_*.py' -v
\`\`\`

GitHub workflow \`.github/workflows/kmong-uptime-ops-prototype.yml\` runs only isolated Python 3.11 synthetic CI with read-only permissions. Tests inject DNS and socket responses (no real HTTP). Results do **not** establish customer approval, real network behavior, Windows/NAS acceptance, proprietary asset rights, OSS redistributability, official completion percentages, or marketplace readiness. Future P2: supervised real-network tests with owned target, retry/backoff policy, state history retention and Windows/NAS packaging; P3/P4: UI, integrations, compliance, licensing, customer sign-off and owner GO. The original hub 90/100 webhook E2E gate is unrelated and still blocked.
