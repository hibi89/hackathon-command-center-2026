# 해총 GitHub App 중앙 자동화 — 2026-11-17 최종 기술 수용 매트릭스

**임무 잠금:** GitHub App → 실제 HMAC-SHA256 Webhook → 기존 Vercel Production → GitHub Actions → 중앙 관측 원장. 사용자 승인 없는 다른 제품/환경/Production 작업 금지.

- 저장소: `hibi89/hackathon-command-center-2026`; 평가 기준 운영 브랜치 `kmong-productization@de3dd1584a11f9faf403b64aec72fc6b5b8aad2e`; `main@5542fb5bf13cba5f30a374afc423b875790ff58c`.
- 정본 기술 배점: [2026-11-14 고정 기술검증 100점표](KMONG_CENTRAL_85_RUNTIME_PARITY_20261114.md)와 [2026-11-15 반복 schedule 90점 판정](KMONG_NATIVE_SCHEDULE_90_AND_BRIDGE_ACCESS_20261115.md). 이 배점표는 **이력상 중앙 기술 증거표**이며, 사용자 승인 최종설계 전체의 공식 검증률/상용 출시 비율이 아니다.
- 사용자 확정 전체 기준: [OWNER-FINAL-BLUEPRINT-100](../strategy/FINAL_BLUEPRINT_COMPLETION_STANDARD_20261113.md). 전체 가중치 분모 미승인 → 공식 검증률 **UNASSESSED**. 실제 통과 근거만 인정하고 제품 점수/크몽 게시 상태를 변경하지 않는다.

## 1. 고정 기술검증표 전수 수용

| 구형 기술 수용항목 | 배점 | 실증 판정 | 증거와 한계 |
|---|---:|---|---|
| GitHub native schedule와 반복 안정성 | 25 | PASS | 서로 다른 실 `event=schedule` [#43590721340](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43590721340), [#43625442971](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43625442971) 성공. 추가 [#43968247391](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43968247391) 성공 및 80개 테스트/실 스캔 `NO_CHANGE`. GitHub 자체 일정 발행의 절대 시간 보장은 아님 |
| 중앙 수집 테스트 | 20 | PASS | 기존 Production main SHA [bridge CI #43824727247](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43824727247) Node78 + Python80 모두 PASS; 실제 bot E2E [#43859747199](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43859747199)에서 Python80 PASS |
| 원장 동기화 및 무결성 | 20 | PASS | [#43824732787](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43824732787) `UPDATED` → [원장 commit 9044413d](https://github.com/hibi89/hackathon-command-center-2026/commit/9044413d8a1a7337c28c7266dc7ad25ef67090e7). 실 E2E run [#43859747199](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43859747199) `NO_CHANGE`는 `DEFERRED`가 아니며 원장 blob `2dd7b2ed50d205b55a2050aad42df218481e7ceb` 동일. 35 repo / 80 ref / 29 product, unlinked0 / fingerprint0 |
| 제품 추적 SHA/CI 샘플 | 10 | PASS (기존 승인된 기술 증거) | [고정 기술검증 표](KMONG_CENTRAL_85_RUNTIME_PARITY_20261114.md)의 DATA2WEB·DBVORA·Astra·FFAX SHA/CI 교차 검증에 따른 기존 10점 인정. 이번 회차에 네 제품의 모든 최신 기능을 재검수한 것은 아니며 상용 통과를 뜻하지 않음 |
| 권한 및 공식 점수 보존 | 10 | PASS (중앙 작동 경로) | `.github/workflows/kmong-hub-sync.yml`: 소스 App `contents:read/actions:read` + 명시적 35개 저장소, 중앙 워크플로 `contents:write`는 이 repo의 관측 원장에만 사용. 수집 로그 `official scores: UNMODIFIED`. GitHub App 관리 UI에서 모든 설치 권한을 이번 회차에 재열람한 것은 아님 |
| 실제 Production GET/배포 소스 일치 | 5 | PASS | Production `GET /api/webhook` HTTP200 `ready`, `source_sha=5542fb5...`. [CI #43824727247](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43824727247)의 `READY_SHA_MATCHED` 및 Work 브라우저 검증 |
| **실제 서명 webhook push→dispatch→hub E2E** | **10** | **PASS (한 실제 전달의 인과성)** | Work 원본 GitHub App 관리 화면에서 확인한 Delivery `083bddec-e190-11f1-978d-156991bf2ef1` (실서명 헤더, HTTP202 `queued`). Vercel 로그의 `GitHub-Hookshot` POST202와 Request ID `r2g5s-1794829197598-6a1fe727f93c`, 실제 GitHub API `dispatches` 호출. [run #43859747199](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43859747199): 동일 UUID·bot actor·main SHA, SUCCESS + Python80 + Collector `NO_CHANGE` + 원장 readback. UUID만으로 암호학적 검증을 선언하지 않음 |

**좁은 기술 배점표 계산:** 기존 90점 인정 + 이번 실서명 E2E의 근거가 확보된 10점 = **100/100 기술 증거 후보** (7/7 영역 PASS). **이것은 역사적 중앙 기술 배점표의 후보 계산이며, 공식 구현완성률·검증완성률 100% 확정 또는 상용 승인과 다르다.** `data/haechong_active_mission_20261115.json`의 기존 잠정 90점 필드는 과거 인정 상태로 보존하며, 승인된 전체 분모가 확인되기 전 숫자를 자동 덮어쓰지 않는다.

## 2. 별도 수용조건과 검증 한계

| 항목 | 판정 | 이유/향후 안전 조치 |
|---|---|---|
| 실 GitHub App signed eligible push → Vercel → dispatcher → scan/ledger | PASS | Live Delivery/실 Vercel 요청/봇 Run/원장 연결 |
| 실행 SHA와 인증 통로 코드 | PASS | Main/Production SHA 일치, HMAC-SHA256 timing-safe 검증을 통과해야 `queued` 반환하는 현행 `receiver.js` 흐름 |
| 실제 Production에서 변조된 서명 HTTP401, 무허가 repo/branch 202 ignored, signed ping 200 재현 | **NOT_RUN (Production)** | 해당 시나리오는 Node 통합/단위 CI PASS이며, 같은 케이스의 새로운 실 Production 서명·비서명 트리거를 이 회차에 실행하지 않음. 향후 필요 시 사용자 승인된 비파괴적 실검증 필요 |
| 동시 웹훅 원자적 exactly-once/영속 큐 | **NOT_GUARANTEED** | 현재 30분 Actions 이력 기반 best-effort 통합. 고가용성/정확히 한 번 처리 보장에 대한 설계·고객 수용은 별도임 |
| Vercel Ignore Build Step의 이후 설정 상태 | **NOT_VERIFIED** | Work가 동일 코드 SHA를 재배포한 증거는 있으나 이후 Ignore Build 설정 지속 여부를 이 검수에서 변경/재조회하지 않음 |
| 최종설계 전체 요구 ID·승인된 100점 가중치·고객/권리/운영/출시 수용 | **UNASSESSED / RELEASE HOLD** | 공식 승인 분모 없음. 허위 100점·게시·고객 데이터 변경 금지 |

## 3. SHA 고정 실제 실행 근거

- 현재 본 감사 기준 SHA: 운영 `de3dd1584a11f9faf403b64aec72fc6b5b8aad2e`, main `5542fb5bf13cba5f30a374afc423b875790ff58c`. 본 감사 반영의 **결과 커밋 SHA**는 GitHub 최신 HEAD로 별도 확인한다.
- [임무 잠금 CI #43993225707](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43993225707): `de3dd1584a11f9faf403b64aec72fc6b5b8aad2e`, 검사 PASS, 적대적 테스트 18/18 PASS.
- [최신 native schedule #43968247391](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43968247391): `main@5542fb5...`, 2026-11-17 07:15 KST 생성, `KMONG PREFLIGHT: RUN`, Python80 PASS, Collector `NO_CHANGE`.
- [서명 E2E #43859747199](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43859747199): 2026-11-16 20:40–20:42 KST, bot `workflow_dispatch`, exact Delivery UUID, `NO_CHANGE`, 0 missing/unlinked/fingerprint; 원장 무변경은 정상.
- 독립 API 확인 대상인 `kmong-productization/data/kmong_hub_auto_observations.json`의 blob `2dd7b2ed50d205b55a2050aad42df218481e7ceb`, `no_official_score_authorization=true`.
- 증거의 층위: Delivery 응답 body는 **Work의 소유자 UI 관찰**, Vercel 실 POST 및 GitHub API 호출은 기존 연결 브라우저 로그 관찰, GitHub Actions·CI·원장 blob은 본 검수의 별도 GitHub 원격 조회. **이번 회차에 HMAC secret으로 직접 서명을 재계산하거나 실제 새 Delivery를 재발행하지 않았다.**

## 4. 최종 인수 및 다음 게이트

**기술 인수:** 좁은 중앙 기술 배점표 7/7 영역 PASS/100점 후보, 실제 E2E PASS. 불필요한 동일 E2E/CI/Production 재실행 금지.

**공식 최종 인수:** 제품 및 중앙 운영의 최종설계 전체 가중치가 사용자 승인됐다는 증거가 없으므로 공식 검증완성률 `UNASSESSED`. Production 음성경로 실증과 Ignore Build 운영 설정은 별도 미검증. **상용 RELEASE HOLD** 유지. 판매 등록, 보안/권한 변경, main 병합, Production 재배포는 이번 임무가 승인하지 않음.

**재개 조건:** 우선 사용자가 확정한 전체 최종설계 수용 매트릭스/가중치가 확인되면 해당 기준으로 공식 검증률 계산. 실제로 필요한 미검증 Production 음성 경로는 별도 허용된 비파괴적 테스트로만 확인. 다른 제품으로 임의 전환 금지.

## [2026-11-17 KST] HAECHONG_P1_P2_WORK_PRODUCTION_REVIEW — signed Ping exception retained

**Scope:** GitHub App → HMAC Webhook → existing Vercel Production → Actions → central ledger. Work's owner-authenticated browser performed live tests; this review independently checked GitHub commit diffs, current refs, Actions outcomes and deployed receiver source, but Vercel connector returned 404, so live Vercel observations remain **Work-attested**, not independently re-read.

| Acceptance item | Decision | Evidence boundary |
|---|---|---|
| P1 outside-Root source roster triggers Preview | **PASS (Work live + GitHub diff)** | Isolated branch `codex/p1-source-roster-detect-20261117` second commit [`0e0d7710`](https://github.com/hibi89/hackathon-command-center-2026/commit/0e0d7710eacd6d44360e14c371381349d24c963b) changes **only** `tools/kmong_hub_sync/source_repositories.json`, appending a blank line; verified GitHub commit patch. Work observed Preview `dpl_HjyZn5TohSWwVGnHXXuhdigaQfHq` Ready and build log `node ignore-build.mjs`, `WEBHOOK_RUNTIME_CHANGED`. Current main script includes roster in `ALWAYS_BUILD`. No allowlist semantic change. |
| P2 malformed HMAC | **PASS (Work live)** | Existing Production POST returned HTTP 401 `invalid_signature`; individual Production Request ID not supplied. |
| P2 signed disallowed push | **PASS (Work live)** | GitHub App Delivery `2429caaa-e235-11f1-89f6-2f8521ad4d0e`, from unlisted test branch, received HTTP 202; matching `eligibleEvent` fail-closed source reviewed. |
| P2 valid signed Ping | **NOT_RUN** | No safe authorized sender path identified without App setting changes; current receiver code returns `200 pong` *after* HMAC and delivery-ID verification, and CI tests passed previously. No Production 200 claim. |

**Crosschecks:** GitHub `main@5542fb5bf13cba5f30a374afc423b875790ff58c` unchanged. Work reported the same SHA on Production deployment `dpl_8n5GXuNFEX4hZNcSL6sfgJfCbjBj` before/after, `Ready`, without Production redeploy/settings change. Test branch HEAD `0e0d7710eacd6d44360e14c371381349d24c963b`. Four automatically triggered read-only push Actions [44006529786](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/44006529786), [44006529999](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/44006529999), [44008910588](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/44008910588), [44008910684](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/44008910684) GitHub API `success`. An unrelated EAI change caused existing hub sync [44007190941](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/44007190941) `success`; do not attribute its JSON observation updates to P1. Work reported central Markdown ledger blob `b125dd72713220cfc4e6d64677c03a794a1d2177` unchanged before/after. Current JSON auto-observations blob independently checked: `4fbaaf1b08b8e52b05152a41fa42996552b310bc`; `no_official_score_authorization=true`.

**Disposition:** Existing signed E2E and 7/7 historical technical acceptance retained; **internal-use operational path accepted with documented Ping exception**. Strict P1/P2 all-green closure **HOLD** until a legitimate signed Production Ping returns HTTP 200 or the user explicitly accepts this exception as the final stopping condition. No privileged setting changes are authorized by this review. Official whole-design weighted verification **UNASSESSED**, not 100%. Existing best-effort 30-minute dispatch coalescing still does not guarantee exactly-once. No change to Production, main, secrets, permissions, commercial status, scores or roster data in this documentation-only review.

