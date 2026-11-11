# 크몽 활성 16종 최종완성률 — 2026-11-11 KST 현재 조회 정본

> **현재 16종 / 합계 1123%p / 산술 평균 70.1875% (≈70.19%) / 70% 미만 2종(PC CARE·CUBE 각 50%) / 70% 이상 14종.** 각 %는 최종 고객 납품 설계 기준의 **주관적·잠정적 엔지니어링 추정**으로 공식 테스트 통과율·유료 판매 승인률이 아니다. **전 상품 RELEASE HOLD.** 기술 70% ≠ 상용 70% 또는 완료.

- 범위: `hibi89/hackathon-command-center-2026@kmong-productization` 활성 16종. 소유자 지시로 **Web REA Studio(과거 40%)는 독립 크몽 상품 목록 제외/원본 보존**, `REA_Web`은 계속 75%로 별도 관리.
- 확인 방법: 2026-11-11 KST 연결된 GitHub 실제 구현 브랜치의 **12개 저장소 / 18개 브랜치 HEAD**를 직접 조회(16개 제품 정본 + SMAX `preprocessing`·`frontend` 보조 브랜치). 상품별 HANDOFF/STATUS 및 이전 CI·감사 근거 대조. **이번 갱신에서 신규 테스트 실행 0건**, 지난 성공 CI는 해당 코드 SHA로만 인용한다. 완성률 임의 상향·신규 코드 작성 없음.
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
| HAE | **70%** | `hibi89/HAE@feature/axflow-mvp` (`d192e98daca8`) | SQLite 보호/백업 일부 성공; 전체 CI Linux·Windows 실패 남음 |
| Lightning Azent | **70%** | `hibi89/HAE@feature/lightning-azent` (`9dd2a6e10ffa`) | 부분 격리 27 PASS, 실제 HAE↔LA 통합 E2E·Windows 미확인 |
| DBVORA | **70%** | `hibi89/DBVORA@feature/p0-db-map` (`9e27a5cda271`) | SQLite/PG 메타데이터+ZIP/ZSTD, Linux 부분 178 PASS, Chromium 9; 실PG·전체460·Windows 미검증 |
| RAG Studio AX Edition | **70%** | `hibi89/RAG_STUDIO@feature/p546-rag-prep-mapping` (`5dca9368d409`) | Linux 571 PASS/2 SKIP·Windows 573 PASS(검증 소스 a3f10f95); Private PREP/실고객 미검증 |
| Astra PDF Redesigner | **70%** | `hibi89/astra_pdf_redesigner@feature/astra-p52-to-p70-20261111` (`8f987462dc7c`) | STEP4/5/7 추가; 코드 dab6e365 Chrome/Edge CI 107 PASS·Windows NSIS SUCCESS; 실제 PDF 미검증 |
| 코인 패턴 분석기 | **70%** | `hibi89/candle_scraper@feature/candle-pattern-analyzer` (`8eafcb075959`) | P1~P6 합성 원본 101 PASS, 실제 3.6GB·Windows/EXE/상업권 미검증 |
| SMAX² | **70%** | `hibi89/SMAX@feature/prep-self-owner-mapping-p8` (`67fc66f9b8ca`) | P8~P12 별도 feature 17 부분 PASS; preprocessing 본 브랜치는 50% 기록, Native 전체 통합 미검증 |
| EAI | **70%** | `hibi89/EAI@feature/local-first-mvp` (`379d0c7a77e9`) | P23~P30, 코드 8cdad74a Ubuntu 582 PASS; 진짜 Qwen/Windows/실고객 미검증 |
| AXMART PC CARE | **50%** | `hibi89/AX_MART@feature/pc-care-usb` (`b8706e0a77ec`) | Windows USB·WinRE·실수리·QR/A4·복구 검증 미완 |
| AXMART³ CUBE | **50%** | `hibi89/AX_MART@feature/cube-commerce-core` (`bb37b754c8e6`) | 상품 카탈로그/ZIP 검사/정적 페이지 46 PASS; 계정·결제·배포·고객 E2E 미완 |


## 최신화 의무 및 기준

새 제품 코드·기능·CI·실사용 증거가 발생하면 반드시 [갱신 프로토콜](KMONG_COMPLETION_SYNC_PROTOCOL_20261111.md)로 **상품 원본 HANDOFF/STATUS → GitHub SHA·테스트 검증 → 해총 이 문서와 `KMONG_PRODUCTIZATION.md` 표/합계 → 해총 HANDOFF/STATUS**를 같은 작업 단위에서 동기화한다. 수치 상승 근거가 없으면 **% 유지**하고 새 근거/검증 한계만 기록한다. 다른 채팅이 이 파일을 자동 갱신하는 연결은 존재하지 않으므로, 기록을 수행하지 못했으면 `SYNC_PENDING`으로 명시한다. 이 문서는 위 시점의 스냅샷이며 이후 다른 채팅의 신규 커밋은 별도 재조회 필요.

### 재현성 체크
- 16개 상품 고유명, 합계 1123, 평균 70.1875%, 70% 미만 2종(50%,50%), 활성 Web REA Studio 제외.
- EAI CI [42960081154](https://github.com/hibi89/EAI/actions/runs/42960081154) SUCCESS at `8cdad74a256d3e132870dfd28a875dd4425ffa77`.
- ASTRA UI [42957762014](https://github.com/hibi89/astra_pdf_redesigner/actions/runs/42957762014) 및 Windows [42957762000](https://github.com/hibi89/astra_pdf_redesigner/actions/runs/42957762000) SUCCESS at `dab6e365f5c9d57e285eaf71cb840ecc41513c6e`.
- RAG [42943551661](https://github.com/hibi89/RAG_STUDIO/actions/runs/42943551661) SUCCESS at `a3f10f95db086f363fed3acff48425ca09b77d4f`. 이후 docs-only SHA와 구분.
