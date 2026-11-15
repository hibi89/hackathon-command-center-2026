# UPTIME OPS candidate — opt-in local monitoring prototype, synthetic validation

**Evidence date:** 2026-11-15 KST (final GitHub Actions test log 06:18:34 UTC / 15:18:34 KST)  
**Repository:** `hibi89/hackathon-command-center-2026`, branch `kmong-productization`  
**Tested implementation SHA:** `bea3fd7bb31b6c964e918ae6c0a50907f51eb785`  
**Scope:** self-contained `tools/uptime_ops/` Python stdlib/SQLite preview and read-only GitHub Actions. Existing central webhook, Vercel, 19-service catalog, official product ratings, registration history and approvals unchanged.

## Product position and two designs

- Approved incubation decision: existing SVC-14 website-quality and SVC-07 code-security additions remain unverified extensions, only UPTIME OPS is a new standalone *candidate*. WebOps QA 360 remains a draft bundle. No 20th registered listing is created.
- **Option A:** integrate an external monitoring stack (e.g., uptime-kuma). More UI features but external license/dependency, integration, hosting and operational ownership need independent approval and could create recurrent costs.
- **Option B chosen for this isolated prototype:** independent Python 3.11 standard-library CLI, SQLite local-only event history and exact-IP-pinned HEAD probe. No runtime paid API/dependency; narrower scope, no dashboard or 24/7 support. The repository already fixed local-first and no cloud defaults in the product intake plan.
- Implementation does not import, vendor, fork or redistribute external tools. Their licensing and buyer rights remain **NOT_VERIFIED**, and the prototype is not sale-ready.

## Implemented P0/P2 technical controls

1. Per-target opt-in manifest: `consent: true`, owner scope `approval_ref`, exact HTTP(S) URL, 1–8 approved IP pins, minimum 30-second intended interval, 1–15-second socket timeout. These are operator-supplied declarations, **not independent proof of ownership**.
2. DNS rebinding/SSRF boundary: at each live probe, DNS answer set must be within exact approved pins; connection goes to numeric IP, retaining original hostname for TLS SNI/Host header. No redirect following. Loopback, link-local/metadata, multicast, unspecified, reserved and IPv4-mapped IPv6 prohibited; optional private scope restricted to explicit RFC1918 IPv4 and IPv6 ULA pins. No credentials, query-string tokens, cookies or auth headers.
3. Read-only one-shot HEAD check classifies 2xx UP, redirects/auth/rate-limits UNKNOWN, ordinary 4xx/5xx DOWN, TLS/DNS safety errors UNKNOWN. No polling daemon, domain scan, automatic port scan or notification dispatch. TLS certificate validation remains on. Unexpected network errors do not cause retries or follow-up requests.
4. Local SQLite stores only target IDs, UTC timestamps, outcome/detail code/status/latency, last known state and events; URL, IP, approval data and response content are not persisted. Event deduplication, DOWN→RECOVERED, UNKNOWN not clearing incident, missed observation GAP after >2× intended interval, exact replay idempotency, backward clock rejection. CSV export refuses overwrites; Unix file permissions 0600, SQLite symlink target blocked.
5. Offline config validation is default. Actual network requires explicit CLI `--live --target <id> --db <new or approved path>`. No live targets configured or contacted during this work. The README has only synthetic fixtures; these do not authorize contact.

## Actual CI and regression evidence

| Code SHA | GitHub run | Test evidence |
|---|---|---|
| `16e8a059ce5e65c2b15847243cae338cafb824c1` | [#43684587087](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43684587087) | completed SUCCESS, **29/29 PASS** |
| `f90b64e66509136680d5926dd2386328f11516b5` | [#43684729250](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43684729250) | completed SUCCESS, **35/35 PASS** |
| **`bea3fd7bb31b6c964e918ae6c0a50907f51eb785`** | [#43684826982](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43684826982) | completed **SUCCESS, 37/37 PASS, 0 FAIL**; job `132722993150`, 2026-11-15 06:18:34 UTC `Ran 37 tests in 0.049s / OK` |

CI: Ubuntu/Python 3.11, synthetic fake DNS and sockets; network probes are **not** exercised against real services. Tests cover explicit consent, blocked credential URLs, metadata/loopback, port/URL injection, strict IP pin and DNS drift, redirect no-follow, 200/401/503 response branches, TLS socket cleanup, retries/idempotency, gap and restart events, CSV non-overwrite and local permissions. 19-SKU commercial integrity workflow [#43684001122](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43684001122) previously recorded **37/37 PASS** at its own earlier SHA; original catalog blob `93da57450d009039591fdd656fdf2477ab650384` is unchanged.

## Remaining requirements, restrictions, scoring

- **P0 pending:** owner-verified actual monitoring target rights, customer permission, target IP lifecycle/approval controls, actual usage terms and privacy.
- **P2 partial:** implementation is a single-shot backend prototype; safe retries/backoff, supervised real DNS/TLS/HTTP checks, Windows/NAS acceptance, durable retention and deletion policy with evidence, notification methods, scheduling/sleep behavior, UI, packaging and installer all **NOT_VERIFIED/NOT_IMPLEMENTED**. Periodic monitoring cannot be guaranteed when a device is off.
- **P3/P4 pending:** combined WebOps report, third-party license/NOTICE review, end-user documentation/support/pricing acceptance, real buyer validation and OWNER GO.
- **Central automation provisional 90/100 unchanged**: separate production signed HMAC webhook 10-point E2E still **BLOCKED/NOT_VERIFIED**, original Vercel project access discrepancy unresolved. No extra points claimed for new candidate work; official per-product final design score UNASSESSED.
- **Deployment and safety:** GitHub source code and synthetic CI only; no Production deployment, live external contact, customer data, secrets, GitHub App permissions, Vercel configuration, paid usage, actual Kmong listing, or main-branch merge.
- **Recovery:** implementation parent `549a3642b60a88cb9b8d2b42db0a910eb60405f2`; each code commit has exact parent in Git history. A revert must be normal and reviewed, never force push.

**Next safe work:** improve supervised test fixtures and local event retention/export/delete with synthetic data; real-world monitoring, network and Windows/NAS acceptance require explicit approved target/evidence. The central signed-webhook live gate must be addressed through existing Vercel project and GitHub App authorization rather than relabeling this prototype as 95/100.
