# Kmong 29-source → 19-listing audit

Runs on the existing **kmong-productization** branch, offline, without source repository writes, secrets, products, approvals or Vercel builds.

- Exact sources: 29 product-index records. Commercial: 28 source-to-listing assignments across 19 permanent service IDs. Internal only: AXMART³ CUBE.
- Explicit sole canonical naming alias: source index `Factory AX 전체` → catalog `Factory AX` on `KMONG-SVC-19`. No fuzzy matching.
- Validates posting lifecycle evidence, preservation of listing history and unaltered official completion summary. It does **not** compute completion percentages or approve listings.
- Run: `python3 -B tools/kmong_listing_audit/validate.py` and `python3 -B -m unittest discover -s tools/kmong_listing_audit -p 'test_*.py' -v`.
- CI: `.github/workflows/kmong-listing-catalog-integrity.yml` (hub branch only). Read-only token. Relevant data/script changes only. No cron, webhook trigger, or Vercel deployment.

Any user-approved change to 29/19 mapping or SKU IDs needs a separate versioned decision and careful migration, not a silent relaxation of these assertions. A PASS confirms mapping and posting metadata integrity only, not independent functional QA, rights, commercial readiness, or final 100%.
