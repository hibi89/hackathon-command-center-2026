# 크몽 17종 — 실제 브랜치 HEAD / Actions SHA 교차검증 (2026-11-10 KST)

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
| EAI | `hibi89/EAI@feature/local-first-mvp` | `8516d8b27dce9c0f422380af0bee669869d5f224` | [실패·실행 단계 없음](https://github.com/hibi89/EAI/actions/runs/41210864766) |
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
