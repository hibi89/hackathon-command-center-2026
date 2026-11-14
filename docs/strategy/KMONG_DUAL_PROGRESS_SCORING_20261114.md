# 크몽 두 개의 완성률 병기 — 작업자 보고 × GitHub 검증 증거

**기준/승인:** 사용자 2026-11-14 KST, [최종설계 100점 정책](FINAL_BLUEPRINT_COMPLETION_STANDARD_20261113.md) 및 [GPT-only 제품화 프로토콜](https://github.com/hibi89/hackathon-command-center-2026/blob/kmong-productization/docs/strategy/KMONG_GPT_ONLY_P100_DESIGN_AUDIT_LISTING_PROTOCOL_20261114.md) 우선. **이 문서는 공식 점수 자동 승인 권한을 추가하지 않는다.**

## 1. 2개 수치 + 별도 상용 판정

| 표시 열 | 정의 | 수치 산정·검증 | 변경 권한 |
|---|---|---|---|
| **작업자 보고율** | 담당자가 보고한 기존 엔지니어링 마일스톤. 과거 95/85는 그대로 남기되 **최종설계 공식률 아님** | 현재 버전은 2026-11-13 중앙 감사표에 있는 16개 과거 내부 수치만 구조화. 사용자 인수·새 SHA 반영이 아니므로 `HISTORICAL_INTERNAL_MILESTONE` 표기. DATA2WEB의 72는 승인된 요구가중 점수이므로 '작업자 과거 보고'로 중복 표기하지 않음 | 담당자 원본 보고 변경은 정해진 증거/날짜/브랜치 업데이트 후만 |
| **GitHub 자동 증거 점수** | **승인된 고정 100점 채점표**에서 요구별 `VERIFIED` 가중치를 합산한 후보 재계산 결과. Actions 초록불/테스트 PASS 개수 자체를 백분율로 환산하지 않음 | 승인된 동일 blob SHA 채점표 + 전체 요구 수100 + EXACT source SHA의 실제 GitHub Actions run `completed/success` + 범위·보류값 불변을 확인한 경우에만. 현재 초기 pin은 DATA2WEB 1종이며 기존 승인 72/100을 *재연산*하는 단계. 독립 고객/법무 수용 아님 | 전용 읽기 전용 App이 중앙 snapshot JSON `machine_evidence_score`에 별도 기록. **기존 `official_final_completion` 필드 덮어쓰기 금지** |
| **최종 판정·상용 승인** | 요구사항의 승인100점 전체, 보안/고객 환경·권리, 제품 설치·지원/가격·판매 정책, 사용자 GO | 독립 검수 및 소유자 최종 승인. `RELEASE HOLD`/게시 `등록완료`는 자동 변경 불가 | 사용자 승인/검증된 게시 이력만 |

작업자 보고 95%와 자동 점수 72%가 나와도 어느 하나를 기계적으로 최종 수치로 채택하거나 평균하지 않는다. **차이는 누락된 요구/증거를 조사할 우선순위**로만 사용한다. 자동 점수가 없으면 **미산정(0 아님)**.

## 2. 안전한 초기 구현 범위

- 기존 `tools/kmong_hub_sync/sync.py` 스캔 35 repos / 80 refs / 29 linked products과 GitHub App READ 권한, 중앙 hub 관찰 JSON **단일 write**를 유지한다.
- `dual_progress.py`는 현재 16개 역사적 보고율과 모든 29개 `UNASSESSED` 기본값을 붙인다. DATA2WEB는 사용자 위임 승인 배점 R01~R33 정본 scorecard Git blob `79c08ce8fe9b9c9b34a82373e5e04d1785e409a2`, 승인 범위, GitHub Actions [43509224663](https://github.com/hibi89/data2web_studio/actions/runs/43509224663) source `23a2d1293755294a58a20b98dc34e229a1e54f82`가 동일일 때 기존 72/100 점수를 재연산할 수 있다. 당시 CI는 합성+호스팅 기준이며, 고객 수용·상업권/출고 승인 아님.
- DATA2WEB 카드에 외부 고객·권리 미수용 11개/28점이 `PENDING`이다. 승인된 source manifest·채점표 blob가 바뀌면 점수를 자동 승격하지 않고 `UNASSESSED` 대기. 다른 28개는 승인 분모·정확 SHA·추적 증거가 하나씩 충족되기 전까지 미산정.
- GitHub Actions job summary에는 29개 ID별 2개 값과 상태를 함께 표시; snapshot JSON은 history/auto를 모두 담는다. **새 실시간 웹 대시보드/Vercel은 아직 개발하지 않았으므로 제공 주장 금지.**
- `HISTORICAL_INTERNAL_MILESTONE`, `PINNED_APPROVED_RUBRIC_REPLAY`, `UNASSESSED`는 서로 다른 검증 수준이다. 개별 작업자가 채팅에서 보고한 95%에 대해 구조화한 최신 `worker_progress.json` 수집은 별도 미구현 단계이며, 현 단계의 16개 수치는 11/13 역사 스냅샷임을 반드시 표시한다.

## 3. 다음 완성 조건

1. `python3 -B -m unittest discover -s tools/kmong_hub_sync -p 'test_*.py' -v` 신규 단위/보안 테스트 전체 PASS.
2. 정확 main 코드 SHA/워크플로 실행, GitHub App 인증 READ 및 `dry_run=true`에서 29개 필드, DATA2WEB 기존 승인72점 채점 재실행·회귀·결함 거부 확인.
3. `dry_run=false` 기존 중앙 단일 JSON write에서 중복 실행 `NO_CHANGE`, 내용 readback 및 기존 29제품 official/19서비스/등록완료 불변 확인. **실제 run 전에 코드·권한·원본 보호 확인**.
4. 제품별 현행 담당자 보고 구조화·각 정본/채점표 승인·새 정확 SHA 수용증거가 쌓이면 일괄 점수를 가정하지 말고 개별 whitelist에 pin 추가. 모델/브라우저/고객 법적 승인까지 검증.
5. 실제 제품 개발·완성률 공식 확정·크몽 게시/결제/외부 시스템 변경은 이 자동관찰의 범위가 아니다.

**현재 구현 판정:** 소스/테스트 작성만으로 운영 완료 아님. 정확 GitHub Actions/실 동기화 검증 전까지 신규 기능 **검증 대기**, 기존 중앙 점수·상태 유지.
