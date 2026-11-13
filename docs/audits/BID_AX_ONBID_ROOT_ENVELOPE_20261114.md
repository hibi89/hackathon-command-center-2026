# BID AX — Onbid 15157252 actual JSON envelope: root header/body

**2026-11-14 KST · confirmed product commit** [bd101d566d222c5a5587461202834b179ed9cf96](https://github.com/hibi89/Freelancer/commit/bd101d566d222c5a5587461202834b179ed9cf96)

## User-confirmed evidence and what it means

- Previously, user PC Windows/Python3.11 fetched one JSON reply from `onbid_result_list` (15157252), quarantined 15,930-byte packet, local digest passed, but old inspector emitted `UNRECOGNIZED_ENVELOPE`.
- The user showed only the field-name shape: `raw_response` root keys `header`, `body`; `header` = `resultCode,resultMsg`; `body` = `items,numOfRows,pageNo,totalCount`. Actual code and values, items and identifiers, API key, and raw packet **not received**.
- Parser had assumed only `response.header/body`; updated to accept either direct or wrapped, rejecting mixed ambiguities. Status, page/total/count, canonical stored digest, sensitive field reflection and import/legal approvals gates stay conservative. Existing packet not changed.
- Product local Linux Python3.13.5 **215/215 PASS**, 0 FAIL, with new 7 test cases and previous 208 regression; compileall PASS. Product GitHub changed paths (code/tests/docs/STATUS/HANDOFF) read back **5/5**, code blob `bcaa81c5e97ab1c58c9daa38321f92934738f5bf`. New actual Windows parse: **NOT_RUN**.
- API 4 applications and shared key user-confirmed; the program neither received nor embedded the key. No additional external request or paid CI. A JSON response and canonical hash do not prove an authorized successful Onbid business response.

## Final blueprint status

R01–R29 fixed, **official final completion UNASSESSED**, 85% NOT proven, `[작업중]`, RELEASE HOLD, Kmong not registered. Existing `CANDIDATE-10` / `KMONG-SVC-18` references, other products, 29 originals, 19 sale categories and past registrations preserved.

## Next acceptance

Use the original user-local packet, **offline**, with updated `api-inspect`; report only `state` / `reason` and safe count summary. Do not send key or original JSON. Next verify official response codes, page consistency, field mapping and business rights; Windows EXE, real 100 notices/10 independent reviews and customer acceptance remain unverified.

Sources: product [change note](https://github.com/hibi89/Freelancer/blob/product/bid-ax-public-procurement/docs/ONBID_ROOT_ENVELOPE_FIX_20261114.md); earlier [first live response](BID_AX_ONBID_FIRST_LIVE_RESPONSE_20261114.md).
