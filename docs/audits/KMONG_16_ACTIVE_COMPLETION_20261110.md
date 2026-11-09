# 크몽 현행 16종 관리 명단 — 2026-11-10 KST

## 결정
사용자 승인에 따라 **Web REA Studio(과거 40%)**를 크몽 독립 판매·개발 관리 범위에서 제외한다. 이는 `hibi89/web-rea-studio` GitHub 저장소 삭제나 기존 소스·테스트·감사 자료의 삭제가 아니다. 그 프로젝트는 **개발 보류/역사적 보존**으로 기록하며, REA_Web과 통합도 현재 수행하지 않는다.

- 현행 상품 **16종**, 50% 미만 **2종** (`SMAX² 45%`, `AXMART³ CUBE 45%`), 50% 정확히 **3종**, 초과 **11종**.
- `REA_Web` 기존 완성률 **75%** 유지. Web REA Studio를 제외한다고 REA_Web이 더 완성된 것으로 평가하지 않는다.
- SMAX²는 사용자 지시에 따라 핵심 개발 우선. `hibi89/SMAX@frontend` SHA `52e8a54f676a015e9fbee58def89e1cb84656d72`; `@preprocessing` SHA `ff94d0cd971ab143eb4b8b7665f308f85fb6df97` (현재 개발 시작 전 기준).
- 상용판매/권리/고객·Windows 실기기 검증 미완 **HOLD**. 완성률은 소스·테스트·사용자 인수 조건에 따른 잠정 평가; 번호를 바꾼 사실 자체로 진척률을 변경하지 않는다.

## 현행 16종

| 제품 | 구형 11/09 | 최종 완성률 재산정 | 핵심 확인/출시 조건 |
| 코인 캔들 수집기 | 90% | **94%** | 업비트 유상 API 사용 프로그램 배포 제한·빗썸 상업권 미확인 |
| AI Code Checker | 75% | **78%** | 71개 구성요소 LICENSE/NOTICE 검수 |
| REA_Web | 65% | **75%** | 고객 실기기·원본 앱 복원 범위·유통권·정식 납품 E2E 미완 |
| SOVIA | 60% | **75%** | 실제 고객 승인/PII 오탐 |
| AI AutoML Analyst | 65% | **71%** | 소유자별 PDF/ZIP 시각 최종 검수 |
| REA_APP | 70% | **70%** | 고객용 판매 패키지 |
| HAE | 45% | **65%** | OAuth/실 SaaS |
| Lightning Azent | 45% | **60%** | HAE 실제 런타임 교체·외부 공급자 인증·배포/상업권 미완. 과거 91% 합성 매트릭스와 구분 |
| DBVORA | 50% | **55%** | PostgreSQL·자동 스케줄·증분/중복 안전보관·고객 Windows·최신 전체 게이트 미검증. develop 문서 0%는 구형 |
| RAG Studio AX Edition | 5% | **55%** | Private SMAX PREP Native/승인 E2E·고객 데이터 자동 표준화·5 RAG 유형 완결·실물 설치/상용화 미완 |
| Astra PDF Redesigner | 52% | **52%** | STEP5/7 및 BASIC/PRO/BUSINESS 확장 |
| 코인 패턴 분석기 | 40% | **50%** | 고객 임의 수식 범용성 |
| AXMART PC CARE | 35% | **50%** | 물리 Windows/USB·WinRE·QR/A4·실수리 승인/복구 검증 미완. Release A/B HOLD |
| AXMART³ (CUBE) | 35% | **45%** | 소프트웨어 판매 플랫폼 본체(결제/사용자/다운로드/문의) 미완. 현재는 개발 제품 소개 사이트 |
| SMAX² | 40% | **45%** | 전체 SELF+PREP Native/Windows 통합 QA |
| EAI | 20% | **50%** | P20 로컬 텍스트 증거 검색·P21 공유자원 최적 일정·P22 MAD 이상치 분석, 독립 영수증/배치 DAG 보류. [Linux Python3.11 전체 475/475 CI PASS](https://github.com/hibi89/EAI/actions/runs/42696296697) (검증 SHA `88af3412`); 실제 Windows·Qwen/Ollama·고객 원본·상용 판매 HOLD |

## 감사 이력

- [과거 17종 최초 재감사](KMONG_17_PRODUCT_COMPLETION_AUDIT_20261110.md)
- [과거 17종 SHA 교차검증](KMONG_17_HEAD_CI_SHA_CROSSCHECK_20261110.md)
- [과거 17종 EAI 50% 스냅샷](KMONG_17_COMPLETION_SNAPSHOT_EAI50_20261110.md)
- 변경 기준: 2026-11-10 KST, 소유자 요청. 코드·계정·결제·배포·Git 브랜치 삭제 또는 병합 없음.
