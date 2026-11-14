# Kmong 29-source → 19-listing audit

Runs on the existing **kmong-productization** branch, offline, without source repository writes, secrets, products, approvals or Vercel builds.

- Exact sources: 29 product-index records. Commercial: 28 source-to-listing assignments across 19 permanent service IDs. Internal only: AXMART³ CUBE.
- Explicit sole canonical naming alias: source index `Factory AX 전체` → catalog `Factory AX` on `KMONG-SVC-19`. No fuzzy matching.
- Validates posting lifecycle evidence, preservation of listing history and unaltered official completion summary. It does **not** compute completion percentages or approve listings.
- Run: `python3 -B tools/kmong_listing_audit/validate.py` and `python3 -B -m unittest discover -s tools/kmong_listing_audit -p 'test_*.py' -v`.
- CI: `.github/workflows/kmong-listing-catalog-integrity.yml` (hub branch only). Read-only token. Relevant data/script changes only. No cron, webhook trigger, or Vercel deployment.

Any user-approved change to 29/19 mapping or SKU IDs needs a separate versioned decision and careful migration, not a silent relaxation of these assertions. A PASS confirms mapping and posting metadata integrity only, not independent functional QA, rights, commercial readiness, or final 100%.

## Historical registration metadata gate (2026-11-14)

An event named `등록완료` must carry `kmong_listing_url` (official `https://kmong.com/...` or `https://www.kmong.com/...`), `published_at_kst` (real canonical `YYYY-MM-DD` date) and a nonempty `evidence` reference. Active records must agree with the most recent historical registration. Sales suspension, privatization, and deletion may retain the old event but cannot quietly reset a once-registered service to `미등록`. Even then, the gate checks **metadata consistency**, not whether a seller really controls the account or the externally referenced listing exists; only owner and marketplace evidence can establish that. It also cannot detect removal of an entire historic event if someone independently edits the registry and counts without a retained version; Git history is the backup and comparison evidence.
