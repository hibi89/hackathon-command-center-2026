# 크몽 Coin Pattern Custom Formula P1 — 2026-11-11 KST

## Scope / priority
- Hub 16 active products, baseline 1015 percentage-points / 16 = 63.4375% recorded; DBVORA currently in separate chat, explicitly excluded from this turn.
- Next highest urgency: Coin Pattern Analyzer at 50%, goal 70%. Direct custom-formula analysis product; existing static EMA/BB scanners insufficient for custom paid requests.
- Existing repo `hibi89/candle_scraper@feature/candle-pattern-analyzer`; latest feature SHA `cfb4b821fdd650203b7d63561c5b11c20ebfd50c`; collector `main` and user SQLite untouched.

## Selected design and implemented P1
1. Rejected arbitrary user Python import: fast extensibility but no security boundary.
2. Selected strict JSON/allow-listed expression tree: deterministic, local read-only data, reusable scanner and rule SHA256. Maintenance remains standard-library-only and no API charges.
3. Added `custom_formula_scanner.py` (source blob `8a6a858a58348717498e190eea3f1ff86132d375`), `test_custom_formula_scanner.py` (test blob `75974dd5c656e74b1295f803216384d95d24220c`), `docs/CUSTOM_FORMULA_SCANNER_20261111.md`. SMA/EMA/BB Upper/Lower, field comparisons, golden/dead crosses, all/any/not; eight minute timeframes, multiple DBs, full-history warmup with recent-N signal filter, atomic UTF8 BOM CSV and canonical rule hash. Max nodes/lookback/matches. None calls exchange APIs.
4. Exact local source/test Git hashes matched remote blobs after removing only trailing final newline; source code content otherwise equal. Feature commits source `e713891`, tests `3e712c2`, docs `875836c`, STATUS `a0efe89`, HANDOFF `cfb4b821`.

## Verification
- Synthetic Linux Python 3.13 local `python -W error -m unittest -v test_custom_formula_scanner.py`: **15 PASS / 0 FAIL**. `compileall` PASS.
- Tests cover SMA cross, BB, JSON rejection, schema compatibility, SQLite readonly/digest unchanged, CSV BOM, existing output preservation, match limit, latest-N warmup, CLI. Only synthetic SQLite, not user market data.
- GitHub full repository regression, actual Windows10/11, 3.6GB user E: database, chart parity, EXE and installation/consumer UX, trading returns, licensing and commercial release: **NOT VERIFIED**. GitHub status list: 0 reported items on inspected SHA; does not establish full Actions history.

## Outcome / next gate
- **No arbitrary completion uplift**: Coin Pattern final-product rate remains **50%**, below 70%; all other 15 products unchanged; 16-product average remains **63.4375%**. This is genuine bounded-feature development, not 70% product sign-off.
- Next: authorized full branch checkout; run `python -W error -m unittest -v test_custom_formula_scanner.py test_pattern_analyzer.py test_dual_bollinger_scanner.py` and repo-wide unit tests. Then isolated Windows copy of actual DB (do not mutate original), perf/QA and CSV viewer/EXE validation. Reassess percent on actual evidence.
- Both product and hub RELEASE HOLD; no paid CI triggered, no production, accounts, user data, collector main, private source content copied into public hub, or other contest/repo edits.
- Rollback: isolated feature commits via standard Git revert. Original local files preserved; source ZIP available in current conversation's session, not a permanent backup.
