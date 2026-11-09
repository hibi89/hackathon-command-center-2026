# 크몽 상품화 17종 GitHub 개발 근거 재감사 — 2026-11-10 KST

## 범위와 판정 기준

기준: 해총 `kmong-productization/KMONG_PRODUCTIZATION.md` 2026-11-09 목록의 **17개** (KIC·PayPal·UGREEN 제외). 2026-11-10에 연결된 GitHub `hibi89` 계정에서 30개 접근 가능 저장소 목록, 각 후보 저장소 브랜치, 트리, STATUS/README/REQUIREMENTS 및 이전 테스트 기록을 읽고 교차 대조했다. 개인·고객 원본이나 비공개 소스 전문을 본 공개 보고서로 전송하지 않았다.

**최종 완성률(신규 %)** = 각 제품의 최초 확정 최종설계와 크몽 납품·배포에 필요한 통합/검증/권리 조건을 고려한 해총 **주관적·잠정적 진척 추정**. 공식 테스트 커버리지 비율이 아니며, 100%의 필수 승인 게이트는 아직 별도 검증이다. 과거 날짜의 CI PASS를 최신 HEAD 전체 PASS로 간주하지 않는다. 다수 앱은 최신 현장 고객·실 PC 테스트를 이번 감사 중 새로 실행하지 못했다. 숫자 변화는 **재평가/기준선 바로잡기**이지 이번 감사에서 코드가 개발됐다는 뜻이 아니다.

제품별 결정적 분리:
- 수집기 **기술 99%**(제품 STATUS 별도) ≠ **최종 판매상품 추정 94%**. 상업용 API 라이선스 확인 전 유료 판매·소스/EXE 제공 HOLD. 기술 완성도가 법적 허가를 대신하지 않는다.
- REA_APP은 독립 정적 분석기 `HAE@REA_APP/tools/rea-app`로 평가. AX FLOW A–E 전체 20%와 혼동하지 않는다.
- DBVORA `develop`의 문서-only '0%'는 개발 기능 브랜치 `feature/p0-db-map`의 실제 구현을 반영하지 못한다.
- HAE/Lightning 과거 91%는 **한정 합성 검증 매트릭스**이고 고객용 전체 상용 완성률이 아니다.
- AXMART³ (CUBE)는 **사이트/상품 유통 플랫폼**이지 PC CARE와 별개로 독립 고객용 소프트웨어가 완성된 것이 아니다.
- RAG Studio 기존 5%는 2026-10-28 이후 누적된 RAG 코드/테스트와 2026-11-10 P5.46 PREP 연동 초안을 누락한 구형 관리값이다.
- SMAX²의 범용 PREP는 비공개 브랜치에 남겨두고 공개 RAG에는 별도 계약/어댑터만 작성한다.

## 17개 상품별 코드·테스트·제약 확인

| 상품 | 구형 | 재산정 | 정본 저장소/브랜치 | 검증 근거 및 현재 최대 제약 | 근거 수준 |
|---|---:|---:|---|---|---|
| 코인 캔들 수집기 | 90% | **94%** | [candle_scraper@main](https://github.com/hibi89/candle_scraper) | Windows CI 147/147 PASS, EXE·ZIP 3종 및 제한된 실제 거래소 API 검사. 기술 완성도 별도 추정 99%. **잔여:** 업비트 유상 API 사용 프로그램 배포 제한·빗썸 상업권 미확인, 일반 Windows/전종목 장기시험 미완 | 상 |
| AI Code Checker | 75% | **78%** | [ai-code-checker@main](https://github.com/hibi89/ai-code-checker) | 10/31 STATUS 주관적 약 78%, Windows 실제 EXE 및 라이선스 출처 검수·신규 회귀 CI 기록 **잔여:** 71개 구성요소 LICENSE/NOTICE 검수, 고객 Windows/SmartScreen·PDF·배포권 미완 | 상 |
| REA_APP | 70% | **70%** | [HAE@REA_APP](https://github.com/hibi89/HAE) | tools/rea-app의 v0.3.0 독립 JS/TS 정적 분석·설계/변경영향 보고·Windows Gate R, 제한 범위 내부 MVP **잔여:** 고객용 판매 패키지, 다언어/광범위 저장소 호환성, 사용자 검증 미완. AX FLOW A–E 20%와 별개 | 중 |
| AI AutoML Analyst | 65% | **71%** | [AI_AutoML_Analyst@feature/kmong-v1](https://github.com/hibi89/AI_AutoML_Analyst) | 제품 STATUS의 정식 P0–P6 5/7(71%); Linux 273 PASS/3 SKIP, Windows·브라우저 CI 기록 **잔여:** 소유자별 PDF/ZIP 시각 최종 검수, OSS 폰트/NOTICE·판매 승인 미완 | 상 |
| REA_Web | 65% | **75%** | [REA_Web@feature/d27-windows-python-discovery](https://github.com/hibi89/REA_Web) | D27 기능·실행/설치 시나리오 코드와 다수 테스트, 기록상 27개 GitHub 워크플로 성공 **잔여:** 고객 실기기·원본 앱 복원 범위·유통권·정식 납품 E2E 미완 | 중 |
| SOVIA | 60% | **75%** | [SOVIA_sovereign@develop](https://github.com/hibi89/SOVIA_sovereign) | 오프라인 감사·SQLite·HTML/PDF·sanitized n8n 계약, 4개 OS/Python CI SUCCESS, 880 테스트 규모 **잔여:** 실제 고객 승인/PII 오탐, Windows 수동 검수·서명·보관 정책/상용 배포 미완 | 중 |
| Astra PDF Redesigner | 52% | **52%** | [astra_pdf_redesigner@integration/astra-commercial-core](https://github.com/hibi89/astra_pdf_redesigner) | 최초 7단계 기준 기존 52% 직접 기록; 91/91 Node 및 Windows 설치/Chrome·Edge 테스트 **잔여:** STEP5/7 및 BASIC/PRO/BUSINESS 확장, 실제 고객 PDF·스타일·OCR/패키징 미완 | 상 |
| DBVORA | 50% | **55%** | [DBVORA@feature/p0-db-map](https://github.com/hibi89/DBVORA) | 실제 기능 소스 131경로, SQLite 다중 DB 구조/UI·ZIP/ZSTD 복원, P0 대상 테스트70/70 및 13/13 통합 **잔여:** PostgreSQL·자동 스케줄·증분/중복 안전보관·고객 Windows·최신 전체 게이트 미검증. develop 문서 0%는 구형 | 중 |
| HAE | 45% | **65%** | [HAE@feature/axflow-mvp](https://github.com/hibi89/HAE) | apps/ax-flow 실제 로컬 엔진/GUI/LA 어댑터·DBVORA 조회, 소유자 Windows HAE+LA 합성 7/7 PASS **잔여:** OAuth/실 SaaS, DBVORA restore·인증, 고객 설치/보안 및 상용 E2E 미완. 과거 91%는 제한 합성 MVP 지표 | 중 |
| Lightning Azent | 45% | **60%** | [HAE@feature/lightning-azent](https://github.com/hibi89/HAE) | packages/lightning-azent 로컬 워크플로·재시작·스케줄·SQLite 복구, Windows 검증 LA65/65 + HAE84/84 **잔여:** HAE 실제 런타임 교체·외부 공급자 인증·배포/상업권 미완. 과거 91% 합성 매트릭스와 구분 | 중 |
| SMAX² | 40% | **45%** | [SMAX@frontend + preprocessing](https://github.com/hibi89/SMAX) | SELF 규칙·템플릿·로컬 CSV 프런트, PREP CSV/XLSX/TXT/HTML/DOCX 제한형 파서. 각 부분 검증 존재 **잔여:** 전체 SELF+PREP Native/Windows 통합 QA, 범용 PDF/DB, 고객 자동화 실행 및 판매 준비 미완 | 중 |
| 코인 패턴 분석기 | 40% | **50%** | [candle_scraper@feature/candle-pattern-analyzer](https://github.com/hibi89/candle_scraper) | SQLite 읽기 전용 EMA/BB 검색, 복수 종목·분봉·CSV·뷰어; 합성 23/23 통과 기록 **잔여:** 고객 임의 수식 범용성, 전종목 실DB·차트 대조·Windows EXE·상용 납품 검증 미완. 최신 재검증 ZIP 일부 GitHub 미반영 | 중 |
| AXMART³ (CUBE) | 35% | **45%** | [AX_MART@main](https://github.com/hibi89/AX_MART) | Cloudflare Pages 사이트·브랜드·상품 카드/검색·모바일 정적 UI 구현, 사용자 Chrome 주요 화면 확인 **잔여:** 소프트웨어 판매 플랫폼 본체(결제/사용자/다운로드/문의) 미완. 현재는 개발 제품 소개 사이트, 별도 완성 판매상품 아님 | 중 |
| AXMART PC CARE | 35% | **50%** | [AX_MART@feature/pc-care-usb](https://github.com/hibi89/AX_MART) | 읽기 전용 진단·보고·제한된 승인형 복구 기반, Windows PS 5.1 합성·Python 82·Node 117 내부 QA **잔여:** 물리 Windows/USB·WinRE·QR/A4·실수리 승인/복구 검증 미완. Release A/B HOLD | 중 |
| Web REA Studio | 30% | **40%** | [web-rea-studio@mvp-three-mode-20261018 (main 비교)](https://github.com/hibi89/web-rea-studio) | 사이트 관찰/증거·제한형 3모드 대시보드 메커니즘·오프라인 HTML/CSV UI, 역사적 CI·합성 검증 **잔여:** 실제 동적 사이트 복원 사례에서 Failed to fetch 확인; 최종 3모드 생성·재현 품질/실고객/출시 미완 | 중하 |
| EAI | 20% | **35%** | [EAI@feature/local-first-mvp](https://github.com/hibi89/EAI) | P0–P8 규칙형 로컬 메모리/CSV/증거/결정 지원, Linux 재구성본 Python 201 PASS 기록 **잔여:** 최신 바이트 동일 전체 체크아웃 미검증, Actions 실행 전 실패, Windows/Ollama/Qwen/일반 범용 AI 목표 미달 | 중하 |
| RAG Studio AX Edition | 5% | **55%** | [RAG_STUDIO@feature/p546-rag-prep-mapping](https://github.com/hibi89/RAG_STUDIO) | 검증된 SQLite·문서 인용·혼합질의·대시보드·PDF/DOCX, 기존 Windows/Linux 501 테스트 CI; 신규 PREP 매핑 11/11 **잔여:** Private SMAX PREP Native/승인 E2E·고객 데이터 자동 표준화·5 RAG 유형 완결·실물 설치/상용화 미완 | 중 |

## 개별 저장소/브랜치 SHA 고정 기록

| 제품 코드 | 확인 브랜치 | 확인 HEAD 또는 브랜치 SHA |
|---|---|---|
| COLLECTOR | `hibi89/candle_scraper@main` | `1f976770db4797bcaa846ed32962e306318971ca` |
| CHECKER | `hibi89/ai-code-checker@main` | `adf3f4ac8fab87c72d176011b0b719de39797db4` |
| REAAPP | `hibi89/HAE@REA_APP` | `2fe581b683f6a49779e71058cddbfd165871593a` |
| AUTOML | `hibi89/AI_AutoML_Analyst@feature/kmong-v1` | `4b7da83e037badab545ff14d03e7fe8cd049b52a` |
| REA_WEB | `hibi89/REA_Web@feature/d27-windows-python-discovery` | `97b6e5cab7b8ffb4e1ee7f5e593021f4dac2598d` |
| SOVIA | `hibi89/SOVIA_sovereign@develop` | `7418b23aff9b3abbd3faf5d1477e7244ec82b681` |
| ASTRA | `hibi89/astra_pdf_redesigner@integration/astra-commercial-core` | `b80830ab3219dbcf88556d60ce2c47c2dcec7764` |
| DBVORA | `hibi89/DBVORA@feature/p0-db-map` | `7f9a1c0d0f0e31f68fb600e47d04ccff1e22faaf` |
| HAE | `hibi89/HAE@feature/axflow-mvp` | `42d8de5d56f74ec0fa1908f16e162b538fe704e3` |
| LIGHTNING | `hibi89/HAE@feature/lightning-azent` | `9cba6424dadf3fadb0ccd6ed10040e322c4a62fa` |
| SMAX | `hibi89/SMAX@frontend + preprocessing` | `52e8a54f676a015e9fbee58def89e1cb84656d72 | ff94d0cd971ab143eb4b8b7665f308f85fb6df97` |
| PATTERN | `hibi89/candle_scraper@feature/candle-pattern-analyzer` | `d1302582de9cb1c178ee7ebe7d235036a119e185` |
| CUBE | `hibi89/AX_MART@main` | `fbb32362455378b85bcdd0b5037d1f338055fb71` |
| PCCARE | `hibi89/AX_MART@feature/pc-care-usb` | `b8706e0a77ec245acc7bc0672f121364c851f910` |
| WEBREA | `hibi89/web-rea-studio@mvp-three-mode-20261018 (main 비교)` | `d674d02e27b6b637b2bbb0e6157625c07c6167fb` |
| EAI | `hibi89/EAI@feature/local-first-mvp` | `8516d8b27dce9c0f422380af0bee669869d5f224` |
| RAG | `hibi89/RAG_STUDIO@feature/p546-rag-prep-mapping` | `5dca9368d40992ad9233529f0ec8d73145ce2e55` |

위 SHA는 **감사 시점 열람한 원격 브랜치**의 참조값이며, 표의 과거 CI 테스트는 동일 SHA에서 돌았다는 뜻이 아니다. 동일 제품의 실제 소비자 PC/고객/Production·상용권은 별도 확인해야 한다.

## 출시 여부와 우선 조치

**이번 감사에서 GitHub 개발·테스트 기록만으로 즉시 유료 판매 승인할 수 있는 상품은 확인되지 않았다.** CUBE 소개 사이트의 Cloudflare Production은 별개이며 결제/판매 성능 검증이 아니다. 크몽 상점의 현재 심사 상태/판매 게시 여부는 이번 GitHub 감사 범위가 아니므로 판단하지 않는다.

우선 확인:
1. 코인 수집기: Upbit 프로그램 유상 배포 규정·Bithumb 권리를 먼저 해결/제품 구성을 재설계. 사용자 승인 없이 유료 배포 불가.
2. AI Code Checker: EXE 포함 실제 제3자 라이선스/NOTICE와 구매자 PC 안전성 검수.
3. RAG Studio + SMAX PREP: 비공개 코드 반출 없이 소유자 승인·스키마/원본 출처·실파일 E2E부터 검증. RAG `develop`과 P5.46 feature가 갈라져 있으니 무단 병합 금지.
4. AutoML/SOVIA/REA_Web: 실제 사용자 납품 QA·라이선스/보안·가격/환불 검증 후 출시 결정.
5. REA_APP/HAE/Lightning/DBVORA/SMAX/CUBE/PC CARE/Web REA/EAI/코인 분석: 현재 증거의 범위 밖 기능·외부 인증·실장비 또는 구현 미반영 코드를 먼저 채운다.

## 범위 밖 2개 확장 상품

기존 문서 아래쪽의 **AI 개발품 납품 검수 서비스**(AI Code Checker + Graphify/agent-browser/Cloudflare audit)와 **AI Excel/CSV 매출·고객 분석 서비스**(AI AutoML + 온톨로지/다변수 ML) 기획 2건은 기존 17개 제품의 다음 패키지 후보이며, **별도 코드·상품 완성률 미산정**. 실제 합병/판매가 확인되지 않았다.

## GitHub 변경 원칙

**이번 작업은** 해총 `hackathon-command-center-2026@kmong-productization`의 상품 현황/감사/인수인계 문서만 바꾸는 것. 17개 원본 저장소·브랜치·코드·CI·배포·Library·고객데이터는 변경하지 않는다. 배포/판매/타 레포 병합·권한 변경 없이 사용자가 별도 제품 총괄과 계속 개발할 수 있다. 관측 범위: 연결된 GitHub 원격 텍스트·트리·기록, 신규 실행 테스트 0건. 실제 검증 100%를 주장하지 않는다.
