# 2026-11-11 — 코인 패턴 분석기 70% 핵심 경로 / 병렬 개발 충돌 회피

## Why pivot from DBVORA?
DBVORA remained 55% despite several small P0 accuracy fixes; native Windows, a complete private checkout, and original archive gates were blocking final acceptance. More local isolated fixes without integrated evidence had diminishing value. Changed active priority to the coin analyzer's missing flexible custom formula product feature.

## Two alternative development routes
A) Integrate directly on concurrently edited feature/candle-pattern-analyzer. Faster one-branch delivery if alone, but another worker independently added custom_formula_scanner.py/test_custom_formula_scanner.py and moved HEAD multiple times. Risk of duplicate source overwrite/concurrent lease failure high.
B) Safe independent tested batch mode on feature/custom-batch-rule-engine, then draft PR #1 for interface consolidation. Selected. Avoids original source edits and preserves competing implementer's progress; slight integration overhead accepted.

## Implemented and tested
Separate optional batch engine custom_rule_engine.py (1..16 rules, same SQLite read-only streaming input, bounded JSON DSL, safe result CSV). Exact source/test Git blobs f0d16c11cdb8b57ec8cee52771206b2eb27fe705 / 6119c8302763e80d3e64481bbcb2b1f7b3b2c613; local Python3.13.5, strict ResourceWarning, **23/23 PASS** synthetic real SQLite/CSV. Main/collector, legacy scanners, user E: DB/WAL/SHM and production unchanged. Tests prove this isolated batch component only.

## Current measurable completion
- Coin Pattern Analyzer FINAL **50% unchanged**, target 70%. Batch code not merged or product-integrated, so no arbitrary uplift.
- DBVORA **55% unchanged**, separate Windows/NTFS gate.
- 16 active products sum 1015, average **63.4375%** unchanged.
- Draft PR: https://github.com/hibi89/candle_scraper/pull/1 ; source branch feature/custom-batch-rule-engine HEAD 4ed41932afd8c9d0219638810bc7f6501d895ef9. No paid CI or sales release.

## Critical next gates
1. Inspect current single-formula JSON schema/CLI and batch schema; settle one common customer interface rather than ship duplicate engines. PR mergeability was returned false; actual conflicts to inspect; no blind merge.
2. Run existing original analyzer, dual Bollinger, future review, formula and batch tests from a single authorized checkout SHA. Verify read-only DB source hash, CSV/HTML, no data leak.
3. Windows Python3.11, synthetic representative large DB, customer E: real DB only with separate consent, saved file/Windows EXE UX and legal commercial rights. Then evidence-based 50->70 decision.
