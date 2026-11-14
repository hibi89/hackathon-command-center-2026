# 해총 주말 4상품 소스 추적·자동채점 한도 사고 감사 — 2026-11-14 KST

## 범위·정본
- 중앙 `hibi89/hackathon-command-center-2026` `main@d2c07d1c7b3b657c02ac9f80d5046334c570013f`; `kmong-productization`의 현행 29개 인덱스.
- 영업 단위는 기존 19개 크몽 서비스 원장. 이번 감사 대상은 원천 DATA2WEB Studio·DBVORA·FFAX·Astra PDF Redesigner 4개이며 GitHub 추적 정정 외 제품 코드·원본 고객 데이터·등록 이력·라이선스/가격·RELEASE HOLD 변경 없음.
- **수치는 서로 다른 것:** 작업자 내부 보고(과거), `GITHUB_EVIDENCE_READINESS_V1` 공통 증거확보점수, 제품별 최종설계 승인점수, 판매 GO. 서로 환산/상향 금지.

## 원격 증거와 최신 소스 확인
| 제품 | 중앙 LIVE 마지막 관찰 HEAD | 직접 조회한 소스 브랜치 HEAD | 확인 근거/다음 이슈 |
|---|---|---|---|
| DATA2WEB Studio | `02ef2b5d` | `f04197f0`, `feature/final-blueprint-p85-evidence-20261113` | CSP 실코드 `cab44263`: Win345/Ubuntu344+1SKIP 4/4 SUCCESS [#43544123800](https://github.com/hibi89/data2web_studio/actions/runs/43544123800), Mac/CodeQL 별도 SUCCESS. 최종 설계 72/100은 22요건 과거 승인, 현 HEAD 신규 전항목 재수용은 아님; 11개 항목 28점 보류. |
| DBVORA | `eab26716` | `21e545cb`, `feature/p0-db-map` | Win616PASS+1SKIP/Ubuntu617PASS [#43543990300](https://github.com/hibi89/DBVORA/actions/runs/43543990300), Win+Ubuntu Chromium 8/8×2 [#43544065399](https://github.com/hibi89/DBVORA/actions/runs/43544065399); 미서명 preview ZIP [#43544666021](https://github.com/hibi89/DBVORA/actions/runs/43544666021). 실제 고객 Win10·실 PG TLS·권리/수용 미검증. |
| FFAX | `85e0980c` | `e4693e44`, `feature/ffax-workbench-p85-20261112` | 합성 Node113·React12, 실제 Chromium·axe, Windows/Linux CI 4/4 SUCCESS [#43543877740](https://github.com/hibi89/frontend-foundry-ax/actions/runs/43543877740); 내부 고정 AC점수 80/100 잠정, 공식 최종설계 미산정. 실제 로컬 모델 12프롬프트·소유자 UX 수용 필요. |
| Astra PDF Redesigner | `b80830ab` (구 integration) | `025fb271`, `feature/astra-p71-pdf-source-parity-20261112` | Git compare 구 integration 대비 **ahead 66/behind 0**, P89 `cabe0adf` Chrome·Edge [#43544304090](https://github.com/hibi89/astra_pdf_redesigner/actions/runs/43544304090) 및 Windows NSIS [#43544304096](https://github.com/hibi89/astra_pdf_redesigner/actions/runs/43544304096) SUCCESS. 신규 P90 `8d604a06` 개별 CI 조회 당시 실행 중이므로 완료로 산정하지 않음. PRO/BUSINESS 영구템플릿·실 GGUF/OCR·고객 PDF/권리 미검증. |

## 이번 실제 정정
1. Astra를 사용자 작업 중인 최신 독립 상용 개발 브랜치로 설정한다. `main/tools/kmong_hub_sync/provisional_evidence_roster_20261114.json`의 ACTIVE-13 blueprint·source·기준 CI를 P89 동일 브랜치로 일치시켰다.
2. `test_provisional_score.py`에 ACTIVE-13 추적 브랜치·CI SHA/실고객·판매 미승인 상태 회귀 테스트를 추가했다. [source observer tests #43545642300](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43545642300) **SUCCESS**, [blueprint gate #43545642364](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43545642364) **SUCCESS**. 테스트 성공은 LIVE App write가 아니다.
3. `data/final_blueprint_product_index_current.json` ACTIVE-13만 갱신, 구 링크와 원본 `data/final_blueprint_product_index_20261113.json` 보존. 공식 최종완성률·작업중·등록완료/19개 서비스·법률/상용 권한 전부 불변.

## 실제 GitHub App 실패·복구 규칙
- `main@d2c07d1c` 자동 수집 [#43545668765](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43545668765) 및 [#43545644640](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43545644640): **FAILURE**.
- 실제 job 로그: `/repos/hibi89/ai-code-checker/actions/workflows/final-blueprint-gate.yml/runs` -> HTTP 403 `PRIMARY_RATE_LIMIT; remaining=0; retry_after=none`, `no write accepted`. 같은 오류 구 SHA [#43545621530](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43545621530)에도 발생했으므로 Astra 코드 수정 때문이라고 오판 금지.
- 다수 `workflow_dispatch`가 짧은 구간에 관측됐다. **재호출 금지**; primary hourly limit reset 후 기존 예약/정상 주기 실행에서 확인. Rate limit 해소 전 무료 우회 토큰/권한 증설/강제 GitHub write 없음.
- 관찰 JSON `data/kmong_hub_auto_observations.json`은 구 성공분 그대로, 실패 시 절대 성공으로 갱신하지 않는다. 다음 자동 실행 성공+readback 후 최신 Astra와 4상품 HEAD/공통 증거 점수를 재검수한다. NO_CHANGE는 입력 동일 조건에서만 유효.

## 출고·구매자 수용
- 최종설계 공식 수치: DATA2WEB 승인 과거 **72/100**(현HEAD 신규 전수수용 미확인), 나머지28 `UNASSESSED`; 상용100 인증0, 크몽 게시/수금 승인0.
- 2026-11-14 13:00 KST 사용자 통합 작업 알림은 각 제품 담당 쪽에 별도 예약돼 있다. 새로운 중복 알림/PC 반복 요구 생성하지 않는다.
- 감사 자체는 고객 PC·독립 법무·고객 PDF·실 PG·로컬 LLM 작동 검증이 아니다. 합성/호스팅 CI로 구매자 수용 대체 금지.

## 후속 우선순위
1. GitHub 기본 API 한도 회복 이후 한 번의 정상 자동 동기화와 중앙 snapshot readback; 강제 반복 dispatch 지양.
2. 최신 소스 SHA와 승인된 제품별 100점 REQ 매핑을 분리 검수, 판매 전 필수 권리/실기기/독립승인은 사용자에게 13시 일괄.
3. FlowPilot Universal 원천 소스 별도 확인; UGREEN 해커톤 Skill과 합쳐 공식 상용 점수를 만들지 않는다.

**상태:** Astra source mapping commit 완료 / main 테스트 PASS / hub LIVE 최신 재동기화 **BLOCKED(primary rate limit)** / 29개 공식 점수·상용 출시 판단 변경 없음.
