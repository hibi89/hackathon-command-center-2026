> **2026-11-10 KST 최신 크몽 17종 재조회·상태 정합성 확인:** 지정 GitHub 구현 브랜치 **18개 재조회** (SMAX 2브랜치), 나머지 16개 상품 구현 SHA는 기존 감사값과 동일, EAI는 정확 실행 소스 `88af3412d59dad8ea848322bdb75292adb7db9e4` [Linux 475/475 PASS](https://github.com/hibi89/EAI/actions/runs/42696296697), 문서-only 최신 HEAD `836f79272531df9b9d548f3f5070a4ab8f4a73a0`. 관리표 기준 **17종 = 50% 미만 3종 (Web REA Studio 40%, SMAX² 45%, AXMART³ CUBE 45%) / 정확히 50% 3종 / 초과 11종**. 다른 제품에 신규 전체 CI/실사용 증거가 없어 완성률 무단 상향 없음. 최종상품률은 추정·판매 HOLD. 상세 최신 근거: [2026-11-10 최신 17종 상품·18브랜치 HEAD 스냅샷](https://github.com/hibi89/hackathon-command-center-2026/blob/kmong-productization/docs/audits/KMONG_17_COMPLETION_SNAPSHOT_EAI50_20261110.md). 과거 본문에 남아 있는 EAI 35%와 Job 0 오류는 **구형 스냅샷**으로 현재 검증 상태가 아님.

> **2026-11-10 KST — EAI 최종상품 45→50%(+5%p 잠정), P20/P21/P22 정확 소스 CI 검증 및 인수인계:** `hibi89/EAI@feature/local-first-mvp` 독립 CPU typed goal 8→11. P20 `local_evidence_search`(로컬 명시 TXT/MD의 근거 위치 검색, SHA256+독립 검증, 기본 원문 미표시) **+2%p**, source `f73e97e5951549c72872b4d3213c159abecaa095` [CI 42694085666](https://github.com/hibi89/EAI/actions/runs/42694085666) **437/437 PASS**. P21 `resource_schedule`(동시 자원 제약·의존관계, 제한된 전역 최소완료시간 탐색 및 독립 proof) **+2%p**, source `82acf93e73279cd3e3cc5c676cc8b6dbce04b32b` [CI 42695135188](https://github.com/hibi89/EAI/actions/runs/42695135188) **456/456 PASS**. P22 `csv_robust_outliers`(중앙값/MAD 강건 이상 후보, 결측/비숫자/MAD0 보류, 원본 SHA256·별도 통계 검증) **+1%p**, 정확 통합 기능/테스트 SHA **`88af3412d59dad8ea848322bdb75292adb7db9e4`** [CI 42696296697](https://github.com/hibi89/EAI/actions/runs/42696296697) Linux Python3.11 **475/475 PASS, 0 FAIL/0 SKIP**, compileall/CLI smoke PASS. 초기 P20 path extension/resolve 순서 2 ERROR 및 초기 P22 tuple arithmetic 11 ERROR/1 FAIL은 정확 소스 최소 수정 후 전체 PASS; 오류 이력은 EAI HANDOFF에 기록. EAI 후속 docs-only HEAD `836f79272531df9b9d548f3f5070a4ab8f4a73a0`, [인수인계](https://github.com/hibi89/EAI/blob/feature/local-first-mvp/HANDOFF.md). **최종상품 50%는 최초 확정 범위 기준 잠정 평가이며 Linux 합성 테스트 통과 ≠ Windows·Ollama/Qwen·SearXNG·실고객·상용/배포 승인. RELEASE HOLD.** P13 doctor 10 합성 검사 유지. 기존 다른 **16개 크몽 상품·KIC/PayPal/UGREEN** 코드·완성률·권한·배포·판매 변경 없음. [P20](https://github.com/hibi89/EAI/blob/feature/local-first-mvp/docs/P20_LOCAL_EVIDENCE_SEARCH.md) · [P21](https://github.com/hibi89/EAI/blob/feature/local-first-mvp/docs/P21_RESOURCE_SCHEDULE.md) · [P22](https://github.com/hibi89/EAI/blob/feature/local-first-mvp/docs/P22_ROBUST_OUTLIERS.md).

> **2026-11-10 KST — EAI P19 로컬 CPU 다변량 상관관계 분석 완료 / 최종상품 44→45%(+1%p 잠정):** `hibi89/EAI@feature/local-first-mvp` 8번째 typed `csv_relationships`: 사용자가 명시한 2~6개 CSV 수치 열의 Pearson 상관관계 및 방향·강도를 110자리 Decimal CPU로 계산, 결측/비숫자 CONFLICT·표본 부족/상수 열 UNAVAILABLE, SHA256 + 원본 재계산 독립 영수증, 원문 셀값 비노출·원본 불변·온라인 모델/API 비용 없음. SHA 고정 배치/의존성 DAG 후속 목표 안전 보류 지원. 최신 **기능+테스트 SHA `d376a4dda5595385bd6a2f189b5e20e6090e4b27`** [Actions 42691179558](https://github.com/hibi89/EAI/actions/runs/42691179558) Linux Python3.11 **417/417 PASS, 0 FAIL**, compileall/CLI smoke PASS (+22 P19 tests). 후속 EAI docs-only HEAD `36a553ec48ae83750f62aa1ca2e3bcaa84de2487`. 초기 SHA `c01d9f4` [CI 42690998979](https://github.com/hibi89/EAI/actions/runs/42690998979)는 기대값 테스트 2 FAIL(실제 0.980609를 1.0 기대, 상수열 쌍 인덱스 선택 오류) 이후 **테스트만 수정해 전체 CI 통과**. 현재 EAI **45%**, 당일 목표 50%까지 5%p. 본 수치는 최종상품 잠정 평가, 통계 관계≠인과/예측·일반 AI 완성. 고객 Windows10/11/Qwen/Ollama/SearXNG·실자료·상용화 미검증 RELEASE HOLD. `main`, 나머지 16개 제품·해커톤 KIC/PayPal/UGREEN, 배포/권한·판매 상태 불변. [P19 설계·범위](https://github.com/hibi89/EAI/blob/feature/local-first-mvp/docs/P19_CPU_RELATIONSHIP_DISCOVERY.md).

> **2026-11-10 KST — EAI P18 독립 CPU SQLite 테이블 검증 완료 / 최종상품 43→44%(+1%p 잠정):** `hibi89/EAI@feature/local-first-mvp`에 7번째 typed goal `sqlite_table_audit` 추가. 로컬 단일 SQLite 일반 테이블 필수값 누락·반복 단일/복합 키 진단, SHA256 + 컬럼 중심 독립 receipt, 임의 SQL/파일쓰기/외부전송 금지, 16MiB/20k행/32열 제한, P12 배치·P14 DAG 종속 HOLD. 기능+전체 회귀 정확 소스 SHA **`ef220a017c3f7a14d20aaadfdbcdb40bd3feec28`** [Actions 42688535530](https://github.com/hibi89/EAI/actions/runs/42688535530) Linux Python3.11 **395/395 PASS, 0 FAIL, 0 SKIP**, compileall·CLI smoke PASS (+20 P18 테스트). EAI 후속 문서-only HEAD `de2d02b1cf28310b2b234c10b9aceff5181b98aa` ([P18 설계](https://github.com/hibi89/EAI/blob/feature/local-first-mvp/docs/P18_SQLITE_TABLE_AUDIT.md))은 CI 검증 소스 SHA와 구분. **EAI 44%**, 당일 목표 50%까지 6%p; 실제 Windows10/11, 고객 SQLite DB, 실 Qwen/Ollama/SearXNG, 설치·상용 출시 미검증 / RELEASE HOLD. P13 doctor는 기존 10개 합성 검사를 유지하며 P18은 독립 임시 SQLite DB 테스트로 검증. **다른 16개 제품의 완성률, KIC/PayPal/UGREEN, 배포·판매/권한 변경 없음.** 과거 EAI 43% 및 교차감사 CI 실패 문구는 당시 기록이며 최신 결과 아님.

# 크몽 17종 — 실제 브랜치 HEAD / Actions SHA 교차검증 (2026-11-10 KST)

> **현행 해석:** 이 문서의 기존 '1 SUCCESS, 2 FAILURE, 15개 HEAD Actions 없음' 및 EAI Job 0 분석은 최초 감사 시점의 역사적 집계입니다. 본문 브랜치 테이블 EAI 행은 현재 50% 기능 CI로 정정했고, 최신 17종·18브랜치 전체 HEAD 비교는 스냅샷에 별도 기록했습니다. GitHub CI 실행이 없는 다른 브랜치를 성공으로 간주하지 않습니다.

## 감사 목적과 범위
- 후속 감사 기준점: 해총 `kmong-productization@8cd6ef87257e222aa0895e384216a9e34b5ab3a6`; 1차 재평가 `docs/audits/KMONG_17_PRODUCT_COMPLETION_AUDIT_20261110.md` 보존.
- GitHub 연결 계정 `hibi89`의 13개 제품 저장소 브랜치 목록 API와 17개 상품에 대응하는 **18개 구현 브랜치 HEAD**를 직접 확인했다. SMAX²의 `frontend`와 `preprocessing`은 별도로 계산한다. Web REA Studio의 비교용 `main`은 확인했지만 현재 구현 브랜치 집계에서는 제외했다.
- 아래 18개 SHA 모두 1차 감사문서의 기록과 **일치**한다. 제품 소스/CI/브랜치/배포/권리/판매 설정은 수정하지 않았다.
- 같은 SHA에서의 GitHub Actions 이력만 `GET /repos/hibi89/{repo}/actions/runs?head_sha={sha}`로 대조했다. **결과: 1 SUCCESS, 2 FAILURE, 15개는 해당 HEAD의 Actions 실행 없음.** 15개가 코드 실패란 뜻이 아니며 과거 성공 로그를 현재 SHA 성공으로 승격하지 않는다. GitHub Actions 밖의 Windows/로컬 검증은 별도 기존 근거다.
- 새 테스트, 설치, 고객 PC 확인, 유료 API 호출, Production 브라우저 확인, 상점 심사는 이 감사에서 **0건**. 상품별 기존 최종 완성률과 출시 HOLD는 변경하지 않는다.

## 브랜치별 SHA와 해당 SHA Actions 판정

| 상품 코드 | 확인 구현 브랜치 | 원격 HEAD SHA | 동일 SHA Actions |
|---|---|---|---|
| COLLECTOR | `hibi89/candle_scraper@main` | `1f976770db4797bcaa846ed32962e306318971ca` | 동일 HEAD Actions 결과 미발견 |
| PATTERN | `hibi89/candle_scraper@feature/candle-pattern-analyzer` | `d1302582de9cb1c178ee7ebe7d235036a119e185` | 동일 HEAD Actions 결과 미발견 |
| CHECKER | `hibi89/ai-code-checker@main` | `adf3f4ac8fab87c72d176011b0b719de39797db4` | 동일 HEAD Actions 결과 미발견 |
| REAAPP | `hibi89/HAE@REA_APP` | `2fe581b683f6a49779e71058cddbfd165871593a` | 동일 HEAD Actions 결과 미발견 |
| AUTOML | `hibi89/AI_AutoML_Analyst@feature/kmong-v1` | `4b7da83e037badab545ff14d03e7fe8cd049b52a` | 동일 HEAD Actions 결과 미발견 |
| REAWEB | `hibi89/REA_Web@feature/d27-windows-python-discovery` | `97b6e5cab7b8ffb4e1ee7f5e593021f4dac2598d` | 동일 HEAD Actions 결과 미발견 |
| SOVIA | `hibi89/SOVIA_sovereign@develop` | `7418b23aff9b3abbd3faf5d1477e7244ec82b681` | [성공](https://github.com/hibi89/SOVIA_sovereign/actions/runs/40561071653) |
| ASTRA | `hibi89/astra_pdf_redesigner@integration/astra-commercial-core` | `b80830ab3219dbcf88556d60ce2c47c2dcec7764` | 동일 HEAD Actions 결과 미발견 |
| DBVORA | `hibi89/DBVORA@feature/p0-db-map` | `7f9a1c0d0f0e31f68fb600e47d04ccff1e22faaf` | 동일 HEAD Actions 결과 미발견 |
| HAE | `hibi89/HAE@feature/axflow-mvp` | `42d8de5d56f74ec0fa1908f16e162b538fe704e3` | 동일 HEAD Actions 결과 미발견 |
| LIGHTNING | `hibi89/HAE@feature/lightning-azent` | `9cba6424dadf3fadb0ccd6ed10040e322c4a62fa` | 동일 HEAD Actions 결과 미발견 |
| SMAX-FRONT | `hibi89/SMAX@frontend` | `52e8a54f676a015e9fbee58def89e1cb84656d72` | 동일 HEAD Actions 결과 미발견 |
| SMAX-PREP | `hibi89/SMAX@preprocessing` | `ff94d0cd971ab143eb4b8b7665f308f85fb6df97` | 동일 HEAD Actions 결과 미발견 |
| CUBE | `hibi89/AX_MART@main` | `fbb32362455378b85bcdd0b5037d1f338055fb71` | 동일 HEAD Actions 결과 미발견 |
| PCCARE | `hibi89/AX_MART@feature/pc-care-usb` | `b8706e0a77ec245acc7bc0672f121364c851f910` | 동일 HEAD Actions 결과 미발견 |
| WEBREA | `hibi89/web-rea-studio@mvp-three-mode-20261018` | `d674d02e27b6b637b2bbb0e6157625c07c6167fb` | 동일 HEAD Actions 결과 미발견 |
| EAI | `hibi89/EAI@feature/local-first-mvp` | `836f79272531df9b9d548f3f5070a4ab8f4a73a0` (docs-only) | 최신 기능+테스트 SHA `88af3412d59dad8ea848322bdb75292adb7db9e4` [Actions 475/475 SUCCESS](https://github.com/hibi89/EAI/actions/runs/42696296697); docs-only HEAD 자체의 동일 SHA 실행은 **미확인** |
| RAG | `hibi89/RAG_STUDIO@feature/p546-rag-prep-mapping` | `5dca9368d40992ad9233529f0ec8d73145ce2e55` | [실패·Job 0건](https://github.com/hibi89/RAG_STUDIO/actions/runs/42652519883) |

## 실패 실행의 증거 수준
1. **RAG Studio:** [실패 #42652519883](https://github.com/hibi89/RAG_STUDIO/actions/runs/42652519883), 현재 HEAD `5dca9368...`, 2026-11-10 01:13 KST 실행 정보에 `failure`로 표시되나 Jobs API 결과 **0건**. 실제 Node 테스트 실행/실패를 증명하지 못한다. 해당 workflow는 `.github/workflows/p545-verify.yml`이고 파일상 push 브랜치 필터가 `feature/p545-review-plan-export`이므로 새로운 P5.46 브랜치용 CI 계약·GitHub 실행 오류를 조사해야 한다. **정확한 원인 확정 불가**. 동일 조건에서 근거 없이 반복 재실행하거나 정책/권한 변경 금지.
2. **EAI:** [실패 #41210864766](https://github.com/hibi89/EAI/actions/runs/41210864766), 현재 HEAD `8516d8b2...`, Job `offline-checks` 1건 생성 후 **실행 단계 0건**. Job 로그 조회는 404 BlobNotFound; Python 테스트가 실제로 시작됐다는 증거 없음. 제품의 `STATUS.md`도 선행 P8 실행의 pre-step 실패와 원인 미확정으로 기록한다. Runner/워크플로 문제와 제품 회귀를 분리.
3. **SOVIA:** [성공 #40561071653](https://github.com/hibi89/SOVIA_sovereign/actions/runs/40561071653) 은 현재 `develop@7418b23a...`와 SHA가 일치하며 `SOVIA offline regression` 워크플로가 `completed/success`로 표시된다. 그 사실만으로 고객 Windows 보안/PII·배포 권리/판매 승인까지 성공한 것은 아니다.

## 최신 소스 직접 확인 — RAG / SMAX PREP 분리
- `RAG_STUDIO@feature/p546-rag-prep-mapping`의 실제 `src/prep-mapping-plan.mjs`, `src/prep-mapping-cli.mjs`, `docs/P546_RAG_PREP_MAPPING.md`를 조회했다. `RAG_PREP_MAPPING_PLAN_V1`은 로컬 CSV 검사 결과의 **매핑 제안**이며 `status: REVIEW_HOLD`, `approval: NOT_GRANTED`, `document_indexed: false`, `remote_upload: false`인 검토 보류 출력이다. 이 기능은 최종 Native PREP→RAG 데이터 수용 E2E가 아니다. 로컬 합성 P5.46 11/11 PASS 기록은 제품의 `STATUS/HANDOFF`에 있으나 현재 HEAD Actions 성공 기록과 다르다.
- Private `SMAX@preprocessing`의 `preprocessing/generic-csv.mjs`와 `preprocessing/SMAX_PREPROCESS_GENERIC_CSV_V1.schema.json`을 읽었다. 이 생산자 패키지도 `approval: NOT_GRANTED`, `READY_FOR_HUMAN_REVIEW` 계약이며, RAG의 별도 제안 계약과 **아직 승인된 수신/검증 어댑터 E2E 없음**. Public RAG에 Private SMAX 코드를 복사하거나 배포하지 않았으며 본 감사문서에 비공개 소스 전문을 넣지 않았다.
- 17종의 전체 소스·전체 테스트를 이 후속 감사에서 새로 실행하거나 모두 재독한 것은 아니다. 1차 17종 원격 감사와 HEAD/CI 및 위 고위험 계약 샘플 직접 검수의 증거 범위를 구분한다.

## 다음 총괄 조치 / 우선순위
1. KIC 11/12·PayPal 11/13 제출 담당은 각 대회 리드에 그대로 유지; 해총은 일정/상품화 감독만. UGREEN 별도 리드 원본·제출 상태 미변경.
2. RAG P5.46에서 workflow/event/branch 필터 및 실제 CI Job 생성·실행 증거를 확인하고, **동일 소스 SHA** 전체 Node/Windows/브라우저 검증까지 진행한 경우에만 CI 게이트를 통과로 수정한다. 기존 `develop`과 diverge된 feature의 강제 병합 금지.
3. EAI는 GitHub 선행 Job/runner 단계 실패 원인 증거를 먼저 확보하되 동일 무증거 재실행/유료 또는 권한 변경 금지. 로컬 201 테스트 기록은 이력으로 보존.
4. 수집기 94% 상품은 기술 99%와 분리; Upbit API 소프트웨어 유상판매 제한·Bithumb 권리 미확인 **판매 HOLD** 유지. 타 16종도 상품별 실제 납품·라이선스·보안·출시 승인 확인까지 판매 상태를 임의 변경하지 않는다.
5. 불필요한 완성률 재산정/형식적 커밋 대신, 새 증거가 생긴 제품의 기준선·검증 게이트·정확한 SHA를 갱신한다.

## 변경 기록
- 본 후속 감사의 변경 대상은 해총 관리 문서뿐이다. 제품별 13개 원본 저장소와 각 개발 브랜치 **전부 무수정**. 새 실행 테스트 **0건**. Vercel/Cloudflare/크몽 상점 변경 **0건**. 상품 최종완성률은 `KMONG_PRODUCTIZATION.md`의 17개 수치를 유지한다.
- 기준 시각: **2026-11-10 KST**. 정확한 문서 기준 커밋은 이 파일을 포함한 GitHub 커밋을 조회한다.

## 후속 사실 정정 · EAI P9 신규 코드/CI (2026-11-10 KST)

**2026-11-10 KST — EAI P9 후속 검증 (기존 감사 이후):** Private `hibi89/EAI@feature/local-first-mvp`에 상세 영수증 독립검증 기능 반영. 검증 기능·테스트 코드 SHA `da48d1764f8a369905ef34bd6810cb738efb8a2b`에서 [GitHub Actions #42659433939](https://github.com/hibi89/EAI/actions/runs/42659433939) `offline-checks` **211/211 PASS (0 FAIL)**, compileall/CLI smoke SUCCESS; 이후 `[skip ci]` 인수인계 문서-only HEAD `8c5a2a9f7c8229efeb320f435ca2f0d45181f47c`. 원래 17종 감사의 EAI `8516d8...` SHA는 **과거 스냅샷**, 당시 Actions FAILURE도 이전 실행 이력. 현재 CI 실패로 오판 금지. 현 상품 최종완성률 35% 유지(전체 범용 AI·고객 Windows·Ollama/Qwen·상용 출시 미검증), 원본/타 제품/배포·판매 변경 없음. [EAI P9 문서](https://github.com/hibi89/EAI/blob/feature/local-first-mvp/docs/P9_RECEIPT_DISPLAY_INTEGRITY.md).

- **신규 EAI 브랜치 최신 HEAD:** `8c5a2a9f7c8229efeb320f435ca2f0d45181f47c` (문서-only, `[skip ci]`). 기능 소스/테스트 검증 SHA `da48d1764f8a369905ef34bd6810cb738efb8a2b`; GitHub Actions [#42659433939](https://github.com/hibi89/EAI/actions/runs/42659433939) SUCCESS, 211 Python tests PASS. 이 보고서 위쪽의 EAI `8516d8...` 및 FAILURE는 **당시 감사 시점 역사 기록**이며 현재 브랜치·CI 상태로 사용하면 안 된다.
- EAI 외 16개 최종상품의 기존 기준선은 수정하지 않았다. EAI도 최종상품 35% 유지, 매출·판매승인·실기기/외부 런타임 검증 미진행.

## 신규 P10 변경·완성률 +1%p 기록 (2026-11-10 KST)

> **2026-11-10 KST — EAI P10 실기능 진척 +1%p (최신):** 기존 P9 영수증 검증에 이어 **세 번째 독립 CPU 목표 도메인 `plan_tasks`**(작업 12개 제한·시간/비용/선행조건·정확 최적 조합·동점 인간 보류·독립 결과 검증) 구현. 테스트 소스 SHA `843a1426ac4c2dcb4c0e957768bc94ea04078f02`, [GitHub Actions #42664669185](https://github.com/hibi89/EAI/actions/runs/42664669185) Linux Python3.11 **229/229 PASS, 0 FAIL**, compileall·CLI smoke PASS; 이후 문서-only EAI HEAD `b9aef18d1bb60adb14985393ef7609c2c97a723c`. **EAI 최종상품 완성률 35%→36% (+1%p 잠정)**, 기존 17종 전체 범위/다른 16개 수치 불변. 기술 부분 성공 ≠ 구매자 Windows/Qwen/Ollama/범용 AI/출시 승인. 원본·main/HAE/LA/타 제품/배포·API/판매 무수정. [P10 명세](https://github.com/hibi89/EAI/blob/feature/local-first-mvp/docs/P10_TASK_PORTFOLIO.md). 이전 EAI P9 35%와 오래된 Actions FAIL은 역사적 관측값.

- EAI 최신 원격 브랜치 HEAD `b9aef18d1bb60adb14985393ef7609c2c97a723c`는 `[skip ci]` 상태/인수인계 문서 커밋이고, 기능 소스 검증 SHA는 `843a1426ac4c2dcb4c0e957768bc94ea04078f02`. [GitHub Actions 42664669185](https://github.com/hibi89/EAI/actions/runs/42664669185) 로그 기준 Python3.11 `Ran 229 tests in 4.748s` / `OK`, 기존 211 + 신규 P10 18.
- **현재 EAI 최종상품 36%**(최종 확정 제품설계 100%, 주관적 진척 추정)로 갱신. 1차 감사의 35%와 과거 HEAD 실패 기록은 삭제하지 않고 시점별 보존. 타 제품·판매 승인·Product readiness는 변동 없음.

## EAI P11 최신 후속 사실 · 2026-11-10 KST

> **2026-11-10 KST — EAI P11 검증 후속, 제품 최종 37% (+1%p):** 새로운 네 번째 독립 CPU 도메인 `schedule_tasks`(작업 의존 DAG, 임계경로, 병렬 작업/여유시간, 마감 초과 HOLD, 원본 기반 독립 영수증 검사)를 `hibi89/EAI@feature/local-first-mvp`에 구현. P10/P11 큰 소수·초대형 수 정밀도 보강 포함. 검증 소스 SHA **`42d6b53400fd841d6f5f4e3db0e97583bf3996cd`**, [GitHub Actions #42666810963](https://github.com/hibi89/EAI/actions/runs/42666810963) **Python3.11 Linux 249/249 PASS / 0 FAIL, compileall/CLI smoke SUCCESS**, 정확 SHA 일치. 이후 EAI docs-only SHA `717e9bb105fe065377ea67a5aca199c4f77fff61`. 기존 최종상품 **36%→37% (+1%p 잠정)**; 나머지 16개 제품 수치·판매 HOLD·KIC/PayPal/UGREEN 역할/배포 변화 없음. 실제 Windows·Qwen/Ollama·고객사용·일반 AI·상용 배포 미검증. [EAI P11 설명](https://github.com/hibi89/EAI/blob/feature/local-first-mvp/docs/P11_CRITICAL_PATH_SCHEDULE.md). 앞선 P9/P10 내용은 시점별 기록이며 최신 평가 아님.

- 최신 EAI 원격 구현 브랜치 HEAD `717e9bb105fe065377ea67a5aca199c4f77fff61`는 [skip ci] 문서-only. 정밀도 보강 포함 **실제 테스트 코드 SHA `42d6b53400fd841d6f5f4e3db0e97583bf3996cd`**에서 Actions #42666810963 **249 PASS/0 FAIL**; 최초 P11 247 PASS SHA `7e625cd356cc579634ca0b8842cb2e1e9893f8d3`는 정밀도 보강 전 과거 증거.
- **37%는 17개 중 EAI 단일 제품의 잠정 전체상품 완성률.** 나머지 16개 수치 불변, 전체 판매승인/Windows/모델 연동 QA 없음. 과거 SHA/CI 실패 통계는 원래 감사 시점 스냅샷으로만 읽는다.

## EAI P13/P14 완결 증거 후속 추록 — 2026-11-10 KST

> **2026-11-10 KST — EAI 최종상품 38→40%(+2%p 잠정) / P13·P14 GitHub 전체 검증 완료:** 최신 기능+테스트 SHA **`bbd01576eed2573ffeab5a70eec0662fcb40bad0`** [GitHub Actions #42675220982](https://github.com/hibi89/EAI/actions/runs/42675220982) Python3.11 Linux **301/301 unittest PASS, 0 FAIL, compileall·CLI smoke PASS**. P13 오프라인 doctor 8개 실제 합성 진단+예상 상태 검사(테스트 14개), P14 의존성 기반 목표 파이프라인+원본 SHA256·정해진 실행 순서 영수증 보강(테스트 18개) 확인. 초기 P13/P14 두 Actions Job=0 실패는 과거 기록이고, 후속 Job 실제 실행 301개 PASS가 현재 최신 근거. EAI 문서-only 최신 HEAD `6373b5cf0366a545724456119587b810b799c64f`는 테스트 소스 SHA와 별개. EAI **40%**, 오늘 목표 50%까지 **10%p 남음**, 실제 Windows·Ollama/Qwen·SearXNG·고객 실사용·상업용 출시는 여전히 미검증/RELEASE HOLD. 나머지 16종 상품의 완성률/권리/배포 및 KIC·PayPal·UGREEN 변경 없음. [P13 문서](https://github.com/hibi89/EAI/blob/feature/local-first-mvp/docs/P13_OFFLINE_DOCTOR.md) · [P14 문서](https://github.com/hibi89/EAI/blob/feature/local-first-mvp/docs/P14_DEPENDENCY_PIPELINE.md).

- 정확 코드 SHA `bbd01576eed2573ffeab5a70eec0662fcb40bad0`에서 Ubuntu Python3.11 `Ran 301 tests in 5.244s`, `OK`, Job `offline-checks` completed/success. P13 관련 14 PASS, P14 18 PASS. 기존 P12 269 PASS를 유지하면서 추가 32 PASS.
- EAI 최종상품 잠정 38→**40%**. 당시 P13/P14 Job=0 실패는 이전 SHA의 CI 관측이며, 기능·테스트가 실제 실행된 최신 CI의 결과로 대체한다. 나머지 16종과 상점 출시/상업권 상태 변경 없음.

## EAI P15 신규 검증 · 2026-11-10 KST

> **2026-11-10 KST — EAI 최종상품 40→41%(+1%p 잠정) / P15 실사용 편의 개선 검증:** `hibi89/EAI@feature/local-first-mvp`에서 사용자 입력 목표파일의 실제 SHA256을 계산해 P12 `goal_batch`·P14 `goal_pipeline`용 JSON을 **stdout만 사용해 생성하는 `make-manifest` CLI**를 구현. 기존 솔버·원본·데이터 쓰기/외부 API 사용 없음. 기능+테스트 SHA **`c35269299f0cdfaa42c51eb8351db50b9e7ec93d`** [GitHub Actions #42676269100](https://github.com/hibi89/EAI/actions/runs/42676269100) Linux Python3.11 **320/320 PASS / 0 FAIL, compileall 및 CLI smoke PASS**, P15 신규 19 통합/보안 회귀. 이후 EAI docs-only HEAD **`273b8100034cc65b61fe1037037c13bf133f1722`**. 기존 40%→**41% (+1%p)**, 오늘 목표 50%까지 9%p 남음. 실제 고객 Windows·Qwen/Ollama·SearXNG/상용 출시는 미검증·RELEASE HOLD. **17개 중 EAI 1개만 수정, 다른 16종/KIC·PayPal·UGREEN/판매권한·배포는 불변**. [P15 근거](https://github.com/hibi89/EAI/blob/feature/local-first-mvp/docs/P15_MANIFEST_BUILDER.md).

- `hibi89/EAI` 테스트 소스 SHA `c35269299f0cdfaa42c51eb8351db50b9e7ec93d`에서 GitHub Actions run 42676269100 **320/320 PASS**, P15 신규 19건 포함한 Linux3.11 CLI+실배치/의존 DAG 합성 통합. EAI 최신 문서 HEAD `273b8100034cc65b61fe1037037c13bf133f1722`와 구분.
- EAI 전체상품 잠정 **41%**로 상향, 나머지 상품의 출고/권리/기능 평가 및 SHA 재감사는 수행하지 않았으며 수치 변경하지 않음.

## EAI P16/P17 단일 상품 후속 검사 — 2026-11-10 KST

> **2026-11-10 KST — EAI 최종상품 41→43%(+2%p 잠정), P16·P17 전체 실행 검증:** `hibi89/EAI@feature/local-first-mvp` 다섯 번째 독립 CPU 도메인 `csv_quality`(로컬 CSV 필수값/중복키/정확 숫자범위, 원본 해시·제한된 레코드 인덱스·독립 검증)와 여섯 번째 `csv_schema_drift`(두 CSV의 열 추가·삭제·순서 및 숫자/문자/혼합/빈열 타입 변화, 이중 소스 해시·독립 검증) 구현. P12/P14/P15 워크플로 연동, P13 doctor 10개 검증, 고객 실제 셀 값 외부 미출력/미전송. P16 검증 소스 SHA `954b72737338082d1d5ce5c327f5be29c96732ef` [Actions #42679425913](https://github.com/hibi89/EAI/actions/runs/42679425913) **348/348 PASS**. P17 최종 기능·테스트 SHA **`9b0b7438cd0e8756e87c7ca4d03d23a731773d91`** [Actions #42680542935](https://github.com/hibi89/EAI/actions/runs/42680542935) Python3.11 Linux **375/375 PASS/0 FAIL, compileall/CLI smoke PASS**, 신규 P16 28건·P17 27건 전체 회귀. EAI 문서-only 최신 HEAD **`68c55e6a13eac7a5dde32673ea65bbb5299b76c5`**, 검증 소스와 구분. 전체 최종완성률 **43%**, 당일 목표 50%까지 7%p. 실제 고객 Windows, Ollama/Qwen, SearXNG, 원본 데이터/상업권·배포 RELEASE HOLD. **나머지 16개 상품 수치·해커톤 KIC/PayPal/UGREEN·다른 저장소/배포/권한 변화 없음.** 중간 2개 테스트 기대값 실패는 수정 후 최종 375 PASS. [P16 명세](https://github.com/hibi89/EAI/blob/feature/local-first-mvp/docs/P16_CSV_QUALITY_GATE.md) · [P17 명세](https://github.com/hibi89/EAI/blob/feature/local-first-mvp/docs/P17_CSV_SCHEMA_DRIFT.md).

- 실제 Actions run 42680542935 소스 SHA `9b0b7438cd0e8756e87c7ca4d03d23a731773d91`, `Ran 375 tests in 7.529s` 및 `OK`/job SUCCESS. 이전 P16 `954b7273` run 42679425913 348/348 PASS. 가장 최근 GitHub EAI 문서 HEAD `68c55e6a13eac7a5dde32673ea65bbb5299b76c5`는 docs-only [skip ci]이므로 해당 코드 테스트 SHA와 혼동 금지.
- 이 업데이트는 EAI 1종에만 해당. 16개 상품의 브랜치/완성률 재감사 수행하지 않았으며 변동 없음. EAI 43%는 사용자 추정 최종상품 기준 잠정치로 판매/Windows QA 승인이 아님.
