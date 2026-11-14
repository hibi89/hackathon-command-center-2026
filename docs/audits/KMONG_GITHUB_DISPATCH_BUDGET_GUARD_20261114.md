# 해총 GitHub 자동동기화 호출 폭주 방지 감사 — 2026-11-14 KST

## 사실 확인
- GitHub App GET403는 임의 권한 변경 문제가 아니라 실제 스캔 endpoint `/repos/hibi89/ai-code-checker/actions/workflows/final-blueprint-gate.yml/runs`의 `PRIMARY_RATE_LIMIT; remaining=0`로 확정.
- 자동 디스패치 주체 `kmong-hub-dispatcher[bot]`가 몇십초 간격으로 여러 workflow_dispatch를 발생시켰다. 원인 트리거/업스트림 호스트는 아직 미확정.
- GitHub REST 공식 문서: `GET /rate_limit`는 primary budget 미차감(secondary limit에는 영향 가능). 응답 헤더 권위/primary zero면 reset 대기 원칙: https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api
- 과거 본체 코드 main d2c07d1c의 [#43546942515](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43546942515) 및 [#43547119678](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43547119678) **SUCCESS UPDATED**, 29/29증거점수, 35 repo/80 refs, Astra 최신 feature branch 확인.

## 두 설계 대안 비교
| 설계 | 성능/안정성 | 비용 | 유지보수/제약 | 판정 |
|---|---|---|---|---|
| A. upstream webhook bot의 dispatch debounce 및 예약 통합 | GitHub workflow 생성 자체 감소, 가장 효율적 | 원칙상 무료 기존 호스트 활용 가능(과금은 미확인) | 봇 원본 저장소·호스트/로그 소유권 확인 필요; 현 세션에서 수정 권한 미확정 | 후속 조사 |
| B. 중앙 GitHub Actions App quota 선검사 + bot fixed-window 중복 차단 | source scan/API 수백회 낭비 방지; workflow 자체는 여전히 생성 | Python stdlib/기존 GitHub App, 신규 유료 API 0 | 기존 성공 경로 그대로; 가드 실제 검증 가능 | **구현** |

## 실제 구현·검증
- 코드 `hibi89/hackathon-command-center-2026@main:67212b67d0662ab29f7f5a995386ceb65e049d4c`.
- `.github/workflows/kmong-hub-sync.yml`: source token 발급 직후 `scan_gate`를 호출, `run_sync=true`일 때만 기존 Scan step 실행.
- `tools/kmong_hub_sync/quota_guard.py`: App `GET /rate_limit`의 `resources.core.remaining` 유효성 확인, 보수적 450 건 reserve, bot workflow_dispatch에 한해 UTC 30분 고정창의 최초 유효 요청만 허용; 조회 실패면 fail-closed. 로그에는 비밀/전체 API 본문 미기록. `DEFERRED`는 동기화 성공이 아님.
- `tools/kmong_hub_sync/test_quota_guard.py`: 12 단위테스트(초과/미달·사용자 수동/크론·봇 첫 요청/중복·취소 run·날짜 경계·비정상 데이터).
- [#43547282002](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43547282002) **75/75 PASS**, [#43547282039](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43547282039) 정책 gate SUCCESS.
- 실 봇 [#43547304082](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43547304082)·[#43547364351](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43547364351) `KMONG PREFLIGHT: DEFERRED_BOT_BURST remaining: 5538 reserve: 450`. workflow 종료 success이나 source scan step 각각 SKIPPED, 중앙 observation write 없음. 새로운 main 기능 점검 PASS, 새 full LIVE scan은 아직 미검증.

## 불변 조건·남은 위험
1. 공식 최종설계 지표와 GitHub 잠정 readiness scores 분리. DATA2WEB 과거 72, 기타28 UNASSESSED, 전체 상용100 0, 19개 상품 목록/등록0 유지.
2. user data·GitHub source repos·Vercel/실서비스·GitHub App permissions/secrets·가격/고객 원장 변경0. 원본 11/13 index 보존.
3. 유입 workflow_dispatch 그 자체가 폭주하는 현상은 B만으로 중단되지 않는다. 서비스 생성/로그/상태를 업스트림에서 추적하고 이벤트 coalescing 구현 필요.
4. 30분 사이 첫 유효 bot run도 rate 예산 부족(남은 450 미만)이면 `DEFERRED_PRIMARY_BUDGET`; 해당 경로는 synthetic test만 확인. 상태를 `UPDATED`라고 보고하지 말 것.
5. 정상 시나리오의 풀 스캔 + Central JSON bytes readback과 `NO_CHANGE`는 다음 정확 SHA 운영 실행에서 검증. 유료 API·중복 무의미 재시도 금지.
