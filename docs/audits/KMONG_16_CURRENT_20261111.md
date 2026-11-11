# 크몽 활성 16종 최종완성률 — 2026-11-11 KST 현재 조회 정본

> **현재 16종 / 합계 1166%p / 산술 평균 72.875% (≈72.88%) / 70% 미만 0종 / 70% 이상 16종 / 85% 미만 15종.** 각 %는 최종 납품 범위 대비 주관적·잠정적 엔지니어링 추정이며 공식 테스트 완료율·판매 승인률이 아니다. **전 상품 RELEASE HOLD.**

- 범위: `hibi89/hackathon-command-center-2026@kmong-productization` 활성 16종. 소유자 지시로 **Web REA Studio(과거 40%)는 독립 크몽 상품 목록 제외/원본 보존**, `REA_Web`은 계속 75%로 별도 관리.
- 확인 방법: 2026-11-11 KST 연결된 GitHub 실제 구현 브랜치의 **12개 저장소 / 18개 브랜치 HEAD**를 직접 조회(16개 제품 정본 + SMAX `preprocessing`·`frontend` 보조 브랜치). 상품별 HANDOFF/STATUS 및 이전 CI·감사 근거 대조. 기존 16종 정합 조회 당시 신규 테스트 0건. 이번 PC CARE는 별도 신규 Node 11 PASS·Chromium 합성 UI 검증 및 정확 GitHub 기능 SHA 재평가를 추가했다. 과거 성공 CI는 해당 코드 SHA에만 귀속한다.
- 주의: SMAX²는 `preprocessing@3830cb27` 자체 HANDOFF가 **50% 구형 범위**이고 별도의 `feature/prep-self-owner-mapping-p8@67fc66f9` P8–P12 기능에 따라 해총이 **70% 잠정**으로 산정했다. 상호 브랜치 병합·전체 Native E2E는 **미검증/미승인**. ASTRA도 `integration/astra-commercial-core`의 구형 52%와 새 기능 브랜치의 잠정 70%를 구분한다.
- 보존/한계: 각 제품 본 브랜치, 고객 원본·토큰, 권한/과금, Vercel/Cloudflare Production, 상용 출시 상태 전부 변경 없음. 비공개 저장소 내 상세 구현 코드를 이 공개 중앙 문서로 복사하지 않는다.

## 16개 목록 (내림차순)

| 제품 | 최종상품 잠정 완성률 | 구현 정본 브랜치 (조회 HEAD) | 핵심 증거와 미검증 사항 |
|---|---:|---|---|
| 코인 캔들 수집기 | **94%** | `hibi89/candle_scraper@main` (`1f976770db47`) | Windows 147 PASS(기존); 기술 99%와 판매상품 94% 분리, 거래소 상업권 미확인 |
| AI Code Checker | **78%** | `hibi89/ai-code-checker@main` (`adf3f4ac8fab`) | Windows EXE/GUI 일부 검증, LICENSE/NOTICE·구매자 PC 검증 미완 |
| REA_Web | **75%** | `hibi89/REA_Web@feature/d27-windows-python-discovery` (`97b6e5cab7b8`) | Lite/Pro 분리, 설치·고객 납품 E2E 미확인 |
| SOVIA | **75%** | `hibi89/SOVIA_sovereign@develop` (`7418b23aff9b`) | 다중 OS CI 기존 기록, 고객 PII/권리/사용 승인 미검증 |
| AI AutoML Analyst | **71%** | `hibi89/AI_AutoML_Analyst@feature/kmong-v1` (`4b7da83e037b`) | 기존 Linux 273 PASS/3 SKIP, 구매자 PDF/ZIP·라이선스 최종 QA 미완 |
| REA_APP | **70%** | `hibi89/HAE@REA_APP` (`2fe581b683f6`) | 독립 JS/TS 정적 분석 CLI 내부 MVP, 고객 상품 패키징 미완 |
| HAE | **73%** | `hibi89/HAE@feature/axflow-mvp` (기능 `14c8a7b75b07`; 문서 `b69d71eca3c2`) | Windows/Linux 최신 204 중 195 PASS/2 FAIL/7 SKIP, 신규 실 HAE↔LA↔SQLite↔**DBVORA 계약 모의 서버** E2E 2 PASS/OS. [Actions #42976273517](https://github.com/hibi89/HAE/actions/runs/42976273517) 전체 FAILURE는 기존 ZIP/pyz 소스 동기화 차단 2건. 실 DBVORA/OAuth/고객·출시 미검증, RELEASE HOLD |
| Lightning Azent | **70%** | `hibi89/HAE@feature/lightning-azent` (`9dd2a6e10ffa`) | 부분 격리 27 PASS, 실제 HAE↔LA 통합 E2E·Windows 미확인 |
| DBVORA | **70%** | `hibi89/DBVORA@feature/p0-db-map` (`9e27a5cda271`) | SQLite/PG 메타데이터+ZIP/ZSTD, Linux 부분 178 PASS, Chromium 9; 실PG·전체460·Windows 미검증 |
| RAG Studio AX Edition | **70%** | `hibi89/RAG_STUDIO@feature/p546-rag-prep-mapping` (`5dca9368d409`) | Linux 571 PASS/2 SKIP·Windows 573 PASS(검증 소스 a3f10f95); Private PREP/실고객 미검증 |
| Astra PDF Redesigner | **70%** | `hibi89/astra_pdf_redesigner@feature/astra-p52-to-p70-20261111` (`8f987462dc7c`) | STEP4/5/7 추가; 코드 dab6e365 Chrome/Edge CI 107 PASS·Windows NSIS SUCCESS; 실제 PDF 미검증 |
| 코인 패턴 분석기 | **70%** | `hibi89/candle_scraper@feature/candle-pattern-analyzer` (`8eafcb075959`) | P1~P6 합성 원본 101 PASS, 실제 3.6GB·Windows/EXE/상업권 미검증 |
| SMAX² | **70%** | `hibi89/SMAX@feature/prep-self-owner-mapping-p8` (`67fc66f9b8ca`) | P8~P12 별도 feature 17 부분 PASS; preprocessing 본 브랜치는 50% 기록, Native 전체 통합 미검증 |
| EAI | **70%** | `hibi89/EAI@feature/local-first-mvp` (`379d0c7a77e9`) | P23~P30, 코드 8cdad74a Ubuntu 582 PASS; 진짜 Qwen/Windows/실고객 미검증 |
| AXMART PC CARE | **70%** | hibi89/AX_MART@feature/pc-care-offline-casepack-20261111 (9c25ec379899; 기능 163fd38be68c) | 오프라인 상담 UI·내부ZIP 등록, Node11 PASS·Chromium 합성 UI; 실제 Windows/USB/WinRE/QR·PDF·복구 미검증, 출시 HOLD |
| AXMART³ CUBE | **70%** | `hibi89/AX_MART@feature/cube-commerce-core` (`061addb6e19c`) | P4 로컬 지원 메타데이터·P5 거래 HOLD 영수증·P6 ZIP 내부 CRC·P7 무JS FAQ·P8 SHA 고정 CLI/빌드 통합. Node22 Linux 신규 정확 소스 26/26 PASS; 전체 npm test/build·실 브라우저/Windows/고객/Cloudflare 미검증, 회원/결제/다운로드 미구현 · RELEASE HOLD |


## 2026-11-11 HAE P4 최신 소스 CI·계약 E2E 재검증 (73% 유지)

> **2026-11-11 KST — HAE 73% 유지 / Windows·Ubuntu 소스 회귀 수리 및 DBVORA 계약 합성 E2E 갱신:** `hibi89/HAE@feature/axflow-mvp` 기능·테스트 SHA `14c8a7b75b079c8904792cbf3eaae7d1eeded60b`, 인수인계 문서 HEAD `b69d71eca3c2ac0cb5cc7e1bf9295d065630c09e`. [Actions #42976273517](https://github.com/hibi89/HAE/actions/runs/42976273517) Windows·Ubuntu 각각 **204 tests = 195 PASS, 2 FAIL, 7 SKIP, 0 ERROR**, 전체 CI는 **FAILURE**(미교체 기존 ZIP/pyz vs 신규 소스 parity 2 FAIL). 기존 Windows 7 FAIL+13 ERROR에서 남은 2 FAIL/0 ERROR로 감소; 실제 HAE↔LA 승인 CSV→합성 SQLite→DBVORA **p0-01.v1 계약 모의 서버** 조회·연결 장애 시 원본 SHA/실행상태 보존 E2E 신규 2 PASS/양OS. 실 DBVORA 서버·Google OAuth/Gmail/Sheets·고객 Windows·새 버전 패키지/출시는 미검증, 출시 **RELEASE HOLD**. 이 증거는 기존 임시 73점의 테스트 신뢰도 향상이지 신규 영업 기능 달성이 아니므로 **73% 유지**, 85% 미달. 원본 바이너리/비공개 코드/고객자료/다른 15종/Production 불변. 활성 16종 **합계 1166%p / 평균 72.875% / 85미만 15종 / 70미만 0종**.

## 2026-11-11 HAE 73% 업데이트

> **2026-11-11 KST — HAE TOP1 실개발 70→73%(+3%p) 최신화:** private `hibi89/HAE@feature/axflow-mvp` 소스 `4f19b367f0573a553b0f89965dca7fab32a5c09d` 및 인수인계 HEAD `2a1d90fd4db480cb7d88645ade43420186aaa5ae`. Windows cp1252 콘솔 한글 경로 안전 출력·포트 실패 검증 및 소유자 지정 **synthetic-only offline SQLite** 메타데이터 조회/관계 목록 CLI 추가. Linux 신규 스코프 14/14 PASS, 전체 [GitHub Actions #42972148842](https://github.com/hibi89/HAE/actions/runs/42972148842) Windows/Ubuntu 둘 다 **FAILURE**(기존 배포 소스 불일치/잔여 회귀). 기존 배포 ZIP·비공개 고객 데이터·main·외부 인증/권한 미수정, 상용출시 HOLD. 진척 73%는 주관적 제품 범위 재평가이며 85% **미달**. 활성 16종 합계 **1166%p**, 평균 **72.875%(≈72.88%)**, 85 미만 **15종**, 70 미만 **0종**. [긴급도 TOP3](docs/audits/KMONG_UNDER85_TOP3_20261111.md).

## 2026-11-11 PC CARE 70% 재평가

> **2026-11-11 KST — AXMART PC CARE 잠정 최종상품 50→70% 재감사·사용자 상담 UI 연결:** 비공개 hibi89/AX_MART의 feature/pc-care-offline-casepack-20261111 기능 SHA 163fd38be68c8fac09289373a3f2a0f5d021f846, 인수인계 docs HEAD 9c25ec379899b7e982cba429acf4ef9d01b8ce6e. 오프라인 JSON 상담 화면·수동 인쇄·개인정보 필터를 기존 이력 비교·내부시험 ZIP/QA 등록과 연결. 원격 정확 blob 3개가 실행 소스 해시와 일치했고 Linux Node22 **11 PASS/0 FAIL/0 SKIP**, Chromium 합성 UI JSON→검토→인쇄·민감값0·오류0·외부요청0·390px overflow0 확인. 기존 2026-10-31 전체 *synthetic* QA(Python 79 PASS/3 SKIP, Node117/PS5.1/ZIP PASS)는 예전 SHA 한정. **현재 P14 전체 Windows/ZIP/CI·실기기·WinRE/QR·실인쇄/복구 미검증, RELEASE HOLD.** 이전 중앙 50점은 과거 구현범위 재감사와 신규 고객 진입점 통합으로 70점 잠정 평가(HEALTH16+ANALYZE16+REPORT18+RESCUE4+RECOVER7+QA9)했으며 단일 UI 11테스트로 20점 올린 것이 아니다. 활성 **16종 합계 1143%p / 평균 71.4375%(≈71.44%) / 70% 미만 1종 AXMART³ CUBE 50%**. 원본 PC CARE 브랜치·운영 main/Cloudflare/고객파일/과금·권한 불변. [제품 근거](https://github.com/hibi89/AX_MART/blob/feature/pc-care-offline-casepack-20261111/products/pc-care/docs/P14_70_COVERAGE_20261111.md).

> **2026-11-11 KST CUBE 중간목표 50→70% 잠정(+20%p) 검증·동기화:** private AX_MART [feature/cube-commerce-core@061addb6](https://github.com/hibi89/AX_MART/commit/061addb6e19c15b537181fcd278ce52878f07707)에서 고객지원 메타데이터·HOLD 거래요청·ZIP 경로/CRC·무스크립트 지원 안내·원본 SHA 고정 로컬 CLI 구현. 기능/테스트 소스 10개 Blob SHA와 Linux Node22 격리 실행 파일 일치, **신규 테스트 26 PASS/0 FAIL/0 SKIP**. 기존 원본 전체 npm test/build·실 Windows/고객·Production 검증 없음. 회원·실결제·실문의 수집·다운로드·상용 출시는 **미구현/RELEASE HOLD**. 기존 허브에 반영된 PC CARE 70% 보존. **활성 16종 모두 개발 잠정 ≥70%, 합계 1163%p, 평균 72.6875%.**

## 최신화 의무 및 기준

새 제품 코드·기능·CI·실사용 증거가 발생하면 반드시 [갱신 프로토콜](KMONG_COMPLETION_SYNC_PROTOCOL_20261111.md)로 **상품 원본 HANDOFF/STATUS → GitHub SHA·테스트 검증 → 해총 이 문서와 `KMONG_PRODUCTIZATION.md` 표/합계 → 해총 HANDOFF/STATUS**를 같은 작업 단위에서 동기화한다. 수치 상승 근거가 없으면 **% 유지**하고 새 근거/검증 한계만 기록한다. 다른 채팅이 이 파일을 자동 갱신하는 연결은 존재하지 않으므로, 기록을 수행하지 못했으면 `SYNC_PENDING`으로 명시한다. 이 문서는 위 시점의 스냅샷이며 이후 다른 채팅의 신규 커밋은 별도 재조회 필요.

### 재현성 체크
- 16개 상품 고유명, 합계 1166, 평균 72.875%, 70% 미만 0종(활성 전체 16종 70% 이상 잠정), Web REA Studio 제외. CUBE 061addb6/PC CARE 9c25ec37 서로 다른 feature.
- EAI CI [42960081154](https://github.com/hibi89/EAI/actions/runs/42960081154) SUCCESS at `8cdad74a256d3e132870dfd28a875dd4425ffa77`.
- ASTRA UI [42957762014](https://github.com/hibi89/astra_pdf_redesigner/actions/runs/42957762014) 및 Windows [42957762000](https://github.com/hibi89/astra_pdf_redesigner/actions/runs/42957762000) SUCCESS at `dab6e365f5c9d57e285eaf71cb840ecc41513c6e`.
- RAG [42943551661](https://github.com/hibi89/RAG_STUDIO/actions/runs/42943551661) SUCCESS at `a3f10f95db086f363fed3acff48425ca09b77d4f`. 이후 docs-only SHA와 구분.
