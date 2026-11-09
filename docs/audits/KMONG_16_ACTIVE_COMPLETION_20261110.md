> **2026-11-10 KST — SMAX² 50% 잠정 달성 / 크몽 활성 16종 평균 62.1875% ≈ 62.2%:** `hibi89/SMAX@preprocessing`의 P5 제한형 최대8 CSV 안전 배치(+2%p), P6 오프라인 CSP/no-script 검토 HTML(+1%p), P7 한국어·영어 고객 CSV 열 매핑 후보(미확정/승인 필수,+2%p) 기능·회귀 테스트/문서 개발. SMAX² 기존 **45→50% (잠정 제품 범위 기준)**, 16개 상품 기존 990/16=61.875%에서 **995/16=62.1875%**, 50% 미만은 **AXMART³(CUBE) 45% 하나**, 정확히 50% 4개, 초과 11개. 최신 정확 코드+테스트 SHA `3190da505efcd55e7e83a1eabe994fbd8c9e5718`, docs-only HEAD `3830cb276f560d58e8181ba384d9cbe64815737c`. **P7 GitHub 실제 코드+테스트 blob SHA와 Node22 파일 일치 Native 28/28 PASS** (18 라이브러리, 10 CLI 검사시 원본 CSV parser/reader는 test stub); P7 원본 parser 연결 V8 9/9; P5 V8 17/17, P6 V8 14/14, P3 SHA256 정확 원본 V8 14/14, P3→P4→P5 V8 실제 합성 데이터 집계 9건 PASS/1 하네스 `structuredClone` 미실행. **GitHub `preprocessing` Actions 0회/전체 Native `npm run test:preprocessing` 미실행, 실 Windows/SELF UI/고객 자료/출시 미검증**. 50%는 출시 성공이나 원본 Native 전체 회귀 PASS가 아니다. RELEASE HOLD. `main/frontend/backend`·외부 레포·권한/과금/Production/원본 변경 없음. [SMAX 인수인계](https://github.com/hibi89/SMAX/blob/preprocessing/HANDOFF.md), [P5](https://github.com/hibi89/SMAX/blob/preprocessing/docs/PREP_SELF_BATCH_20261110.md), [P6](https://github.com/hibi89/SMAX/blob/preprocessing/docs/PREP_SELF_HTML_REPORT_20261110.md), [P7](https://github.com/hibi89/SMAX/blob/preprocessing/docs/PREP_SELF_COLUMN_SUGGEST_20261110.md).

> **2026-11-10 KST — SMAX² P4 추가 검증·16종 전체 평균 유지:** 정확 P4 코드 SHA `9358eb0a383b2d89b2bb574a8ac88577542bf334`, 문서 최신 HEAD `a9eb2e23626e8a4ce60998b2f6c2b9756ab9eb73`. Node22.16에서 실제 SHA 동일 CLI `node --check` PASS, Native 파일 I/O 격리 11/11 PASS + 실제 CLI 자식프로세스 격리 3/3 PASS = **14/14 PASS(도메인 PREP/SELF는 stub)**. GitHub에 Native 원본 통합 테스트 16개/전체 `npm run test:preprocessing` 등록했으나 **실제 전체 실행 NOT_RUN**, `preprocessing` Actions 0건. **SMAX² 최종상품 잠정 45% 유지**, 크몽 활성 **16종 단순 산술 평균 61.875% ≈ 61.9%** 유지, 50% 미만 `SMAX²` 및 `AXMART³` 2개, Web REA Studio 보존·독립 관리 제외. [SMAX P4 검증 경계](https://github.com/hibi89/SMAX/blob/preprocessing/docs/PREP_SELF_PREVIEW_CLI_20261110.md). Native 전체/Windows/고객/실 UI·판매 보류, 무단 CI 과금/원본·권한·배포 변경 없음.

> **2026-11-10 KST — SMAX² P4 실행형 로컬 PREP→SELF CLI 개발, 전체 진행률 최신화:** `hibi89/SMAX@preprocessing` 정확 기능+테스트 커밋 `9358eb0a383b2d89b2bb574a8ac88577542bf334`, 최신 문서 HEAD `9b8ab43dc03cc3badf73d1df374893d08bd3c7f9`. `self-preview-cli.mjs`의 엄격 `--input CSV --config JSON`/2MiB·64KiB 한계/실제 Node regular-file·symlink·UTF-8·전후 파일 메타데이터(시간·크기·inode) 검사 및 PREP SHA256 출처 기록/승인 전 로컬 집계 출력과 exit0·2·1. 정확 CLI blob `8a59c0877655ff734251e131c162e6dbceb05fed`과 Node22.16 로컬 `git hash-object` 일치, `node --check` PASS, **Node Native 파일 I/O 11/11 PASS (도메인 PREP/SELF는 스텁 사용)**, 기존 P3 V8 14/14 PASS(crypto·UTF8 테스트 대체). 신규 테스트 `tests/self-preview-cli.test.mjs` 16개는 GitHub 체크인·`npm run test:preprocessing` 등록했으나 실제 원본 저장소의 Native 통합·전체 CI·Windows/고객 환경 **NOT_RUN**. 완성률 **SMAX² 45% 유지, RELEASE HOLD**. 해총 현행 **16개 상품 산술 단순 평균 61.875% ≈ 61.9%** (가중 평균·판매 출시율 아님); 50% 미만 2개 `SMAX² 45%`·`AXMART³ CUBE 45%`. Web REA Studio 비활성/역사 소스 보존. `frontend`/`main`/KIC/PayPal/UGREEN/배포/권한/실고객 수정 없음. [SMAX 최신 인수인계](https://github.com/hibi89/SMAX/blob/preprocessing/HANDOFF.md) · [P4 설계/테스트 경계](https://github.com/hibi89/SMAX/blob/preprocessing/docs/PREP_SELF_PREVIEW_CLI_20261110.md).

> **SMAX² 작업 재개 — 2026-11-10 KST:** 비공개 `hibi89/SMAX@preprocessing`에 기존 Generic CSV PREP의 원본·검토 영수증을 검증한 뒤 SELF 매출 보고의 **승인 전 로컬 초안**을 생성하는 `self-preview-gate.mjs` 추가. PREP 오류/중복/수식 또는 SELF 집계 보류가 있으면 `REVIEW_HOLD`; 정상에도 `NOT_GRANTED`/실행 미수행, 원본·고객 행·파일·외부 전송 없음. 기능 SHA `037576e74359e2961838dc8891b7f196c47ece03`, 최신 문서 HEAD `101a9d3f9f82e1a285b2d1b2ea8cac1605ee9bea`. 실제 GitHub 기존 모듈+신규 테스트의 **격리 V8 14/14 PASS(암호화 해시·UTF8 API test double)**만 확인; Node Native 전체 `npm run test:preprocessing`/Windows/E2E/Actions **미검증**. 따라서 **SMAX² 45% 잠정 유지**, RELEASE HOLD. `frontend`/`main` 자동 병합·원본 변경 없음. [비공개 SMAX 인수인계](https://github.com/hibi89/SMAX/blob/preprocessing/HANDOFF.md) · [P3 계약](https://github.com/hibi89/SMAX/blob/preprocessing/docs/PREP_SELF_PREVIEW_GATE_20261110.md).

# 크몽 현행 16종 관리 명단 — 2026-11-10 KST

## 결정
사용자 승인에 따라 **Web REA Studio(과거 40%)**를 크몽 독립 판매·개발 관리 범위에서 제외한다. 이는 `hibi89/web-rea-studio` GitHub 저장소 삭제나 기존 소스·테스트·감사 자료의 삭제가 아니다. 그 프로젝트는 **개발 보류/역사적 보존**으로 기록하며, REA_Web과 통합도 현재 수행하지 않는다.

- 현행 상품 **16종**, 50% 미만 **1종** (`AXMART³ CUBE 45%`), 50% 정확히 **4종** (SMAX², EAI, 코인 패턴 분석기, AXMART PC CARE), 초과 **11종**. 전체 단순 평균 **62.1875% ≈ 62.2%**.
- `REA_Web` 기존 완성률 **75%** 유지. Web REA Studio를 제외한다고 REA_Web이 더 완성된 것으로 평가하지 않는다.
- SMAX² 최신 기능 기준 `3190da505efcd55e7e83a1eabe994fbd8c9e5718`, 문서 `3830cb276f560d58e8181ba384d9cbe64815737c`: P3/P4 이후 P5 배치+검증·P6 오프라인 HTML·P7 헤더 후보 안내 기능 구현으로 **잠정 45→50%**. P7 Native 28 PASS(라이브러리 18/CLI 원본 parser·reader stub 10), P5/P6 실제 기능 V8 회귀 확인. 실 전체 Native repo/Windows/SELF UI/출시 검증 미완, RELEASE HOLD. `hibi89/SMAX@frontend` `52e8a54f676a015e9fbee58def89e1cb84656d72`, `@preprocessing` `3830cb276f560d58e8181ba384d9cbe64815737c`.
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
| SMAX² | 40% | **50%** | P5 최대8 CSV 안전 배치, P6 CSP 정적 HTML 검토, P7 사용자 매핑 후보; Native P7 격리 28 PASS, 전체 Native NPM·Windows·SELF UI/상용 E2E 미검증. 정확 기능 SHA `3190da50`, RELEASE HOLD |
| EAI | 20% | **50%** | P20 로컬 텍스트 증거 검색·P21 공유자원 최적 일정·P22 MAD 이상치 분석, 독립 영수증/배치 DAG 보류. [Linux Python3.11 전체 475/475 CI PASS](https://github.com/hibi89/EAI/actions/runs/42696296697) (검증 SHA `88af3412`); 실제 Windows·Qwen/Ollama·고객 원본·상용 판매 HOLD |

## 감사 이력

- [과거 17종 최초 재감사](KMONG_17_PRODUCT_COMPLETION_AUDIT_20261110.md)
- [과거 17종 SHA 교차검증](KMONG_17_HEAD_CI_SHA_CROSSCHECK_20261110.md)
- [과거 17종 EAI 50% 스냅샷](KMONG_17_COMPLETION_SNAPSHOT_EAI50_20261110.md)
- 변경 기준: 2026-11-10 KST, 소유자 요청. 코드·계정·결제·배포·Git 브랜치 삭제 또는 병합 없음.
