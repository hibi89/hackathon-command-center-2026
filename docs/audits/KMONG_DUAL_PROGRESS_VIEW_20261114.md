# 해총 크몽: 작업자 보고율 + GitHub Actions 증거 검증률 병기

> 2026-11-14 KST 사용자 확정. **현재 이 문서는 기준표이고 자동 업데이트되는 실시간 화면은 아니다.** 동기화되는 실제 값은 [중앙 관찰 JSON](../../data/kmong_hub_auto_observations.json)의 `products[].worker_report` 및 `products[].machine_evidence_score`를 따른다.

## 표시 원칙

- **작업자 보고:** 2026-11-13 중앙 감사에 기록된 16개 제품의 과거 내부 엔지니어링 진척. 최신 공식 최종설계 비율 아님. 근거 없는 제품은 '미기록'.
- **자동 증거 재계산:** 승인받은 100점 전체 요구와 가중치가 불변이며 같은 소스 SHA의 GitHub Actions가 실제 성공한 경우에만 합산. **테스트 합격률을 완성률로 바꾸지 않음.** DATA2WEB 승인 점수표 72점이 초기 유일한 자동 재산정 후보이고 나머지 28개는 미산정.
- **기존 공식 정본:** 별도 검증된 사용자 확정 수용 비율. 자동 점수 후보가 이 필드를 덮어쓰지 않으며, 출시 HOLD/상품 등록완료 이력을 바꾸지 않음.

| ID | 제품 | 작업자 보고(과거) | 자동 검증률 | 기존 공식 정본 |
|---|---|---:|---:|---:|
| ACTIVE-01 | 코인 캔들 수집기 | 95% (2026-11-13 내부) | 미산정 | 미산정 |
| ACTIVE-02 | HAE | 85% (2026-11-13 내부) | 미산정 | 미산정 |
| ACTIVE-03 | AI Code Checker | 95% (2026-11-13 내부) | 미산정 | 미산정 |
| ACTIVE-04 | SMAX² | 85% (2026-11-13 내부) | 미산정 | 미산정 |
| ACTIVE-05 | DATA2WEB Studio | 미기록 | 채점 재검증 중 | 72% |
| ACTIVE-06 | REA_Web | 85% (2026-11-13 내부) | 미산정 | 미산정 |
| ACTIVE-07 | SOVIA | 95% (2026-11-13 내부) | 미산정 | 미산정 |
| ACTIVE-08 | AI AutoML Analyst | 95% (2026-11-13 내부) | 미산정 | 미산정 |
| ACTIVE-09 | REA_APP | 85% (2026-11-13 내부) | 미산정 | 미산정 |
| ACTIVE-10 | Lightning Azent | 85% (2026-11-13 내부) | 미산정 | 미산정 |
| ACTIVE-11 | DBVORA | 95% (2026-11-13 내부) | 미산정 | 미산정 |
| ACTIVE-12 | RAG Studio AX Edition | 95% (2026-11-13 내부) | 미산정 | 미산정 |
| ACTIVE-13 | Astra PDF Redesigner | 85% (2026-11-13 내부) | 미산정 | 미산정 |
| ACTIVE-14 | 코인 패턴 분석기 | 85% (2026-11-13 내부) | 미산정 | 미산정 |
| ACTIVE-15 | EAI | 85% (2026-11-13 내부) | 미산정 | 미산정 |
| ACTIVE-16 | AXMART PC CARE | 85% (2026-11-13 내부) | 미산정 | 미산정 |
| ACTIVE-17 | AXMART³ CUBE | 95% (2026-11-13 내부) | 미산정 | 미산정 |
| CANDIDATE-01 | KUODRA | 미기록 | 미산정 | 미산정 |
| CANDIDATE-02 | PREP | 미기록 | 미산정 | 미산정 |
| CANDIDATE-03 | FFAX | 미기록 | 미산정 | 미산정 |
| CANDIDATE-04 | Factory AX 전체 | 미기록 | 미산정 | 미산정 |
| CANDIDATE-05 | AZENTFLOW AX | 미기록 | 미산정 | 미산정 |
| CANDIDATE-06 | CITEVAULT AX | 미기록 | 미산정 | 미산정 |
| CANDIDATE-07 | SITECRAFT AX | 미기록 | 미산정 | 미산정 |
| CANDIDATE-08 | PROOFQA AX | 미기록 | 미산정 | 미산정 |
| CANDIDATE-09 | ONTOINSIGHT AX | 미기록 | 미산정 | 미산정 |
| CANDIDATE-10 | BID AX | 미기록 | 미산정 | 미산정 |
| CANDIDATE-11 | FlowPilot Universal | 미기록 | 미산정 | 미산정 |
| CANDIDATE-12 | WORKNOVA Desk | 미기록 | 미산정 | 미산정 |

## 실제 검증과 한계

- [자동 이중 수치 코드](https://github.com/hibi89/hackathon-command-center-2026/blob/main/tools/kmong_hub_sync/dual_progress.py) 및 [구현 규칙](https://github.com/hibi89/hackathon-command-center-2026/blob/main/docs/strategy/KMONG_DUAL_PROGRESS_SCORING_20261114.md). 신규 GitHub Actions Job Summary에도 29개 이중 수치 표가 표시된다.
- 신규 첫 실 App run #43537749724는 **37/37 유닛테스트 PASS** / 35 저장소 80 ref / 29 product link / 역사 보고16개 수집 PASS였으나, DATA2WEB `original_blueprint_scope` 문구 불일치로 **승인72 자동재계산은 FAIL-CLOSED / 미산정**. 검증기 문자열 수정 main SHA `32bb7d45aa3b2e0dc0a4941b409b3bc36bc8930a` 반영, 실제 후속 run과 score72 판정은 별도 확인 전까지 미검증.
- 현행 자동 점수는 제품별 승인 채점표·정확 실행 SHA가 마련된 경우에만; DATA2WEB의 72는 22개 VERIFIED/11개 PENDING의 **기존 사용자 승인 점수**다. **실고객 OS/저작권·라이선스/권리/판매 승인 모두 별도.**
- 기존 29개 원천 제품/19개 서비스, `[작업중]`/`[사용자 개입 필요]`, `RELEASE HOLD`/등록 이력 전부 보존. 현행 16개 작업자 최신 보고 형식 자동입력은 후속 과제.

**서로 다른 세 열을 평균 내거나 상대 차이를 최종완성률로 확정하지 않는다.**
