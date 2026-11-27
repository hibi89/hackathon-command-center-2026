# arXiv → 크몽 연구 상품 후보 영구 원장

> 본 원장은 **개발·상품화 가설**이다. 크몽 판매/다운로드 권한·상품 등록/실매출/완성률을 뜻하지 않는다. 기존 `KMONG-SVC-01..19` 및 29 원천/등록 이력은 중앙 `data/kmong_service_catalog_20261113.json`이 정본. 동일 고객문제를 신규 SKU로 중복 생성하지 않는다. 공개 논문·저자 코드·학습 데이터의 상업 이용 권리와 고객 자료 처리권한은 각각 검증 필요.

| 후보 고유 키 / 첫 발견 | 근거 arXiv | 고객·구체 납품물 | 예상 가격 / 기간 / 난이도(모두 추정) | 기존 SKU/독립성 | 차별화·상업/보안 제한·필수 검증 |
|---|---|---|---|---|---|
| ARXIV-IDEA-SQL-MEM-01 · 2026-11-17 | [MEM-SQL 2611.18338](https://arxiv.org/abs/2611.18338), [DB 포렌식 2611.17304](https://arxiv.org/abs/2611.17304) | 사내 DB 관리자·소상공인; **검증 SQL 재사용·읽기전용 자연어 조회 구성, 템플릿, 리포트·복구 가이드** | **15만~40만원 / 2~5영업일 / 중상** | **DBVORA 고급 기능/기존 상품 연계**. 별도 신규 SKU 아님 | 재검증된 SQL 재사용, 고객 DB 외부전송 없이 로컬 우선. SQL injection/쓰기 차단·권한·스키마 변경·SQLite 합성 데이터/실고객 승인·코드/데이터/모델 상업권 검증. 현재 NOT_BUILT·RELEASE HOLD |
| ARXIV-IDEA-REQ-QA-01 · 2026-11-17 | [SatisFix 2611.16289](https://arxiv.org/abs/2611.16289), [Hierarchical Code Graphs 2611.17388](https://arxiv.org/abs/2611.17388) | SW 외주 발주자·작은 개발팀; **최종요구 REQ-ID 대 코드/테스트/SHA 증거, 누락·회귀·오탐 보고서** | **10만~35만원 / 2~4영업일 / 중상** | **기존 KMONG-SVC-07 코드 검수 고급 옵션**. 신규 SKU 아님 | 에이전트 자기합리화 탐지와 시점 누출 방지. 승인 코드 로컬 처리·원본 무변경·수용 매트릭스·객관적 재검증·소스/고객 권리 필요. 현재 NOT_BUILT·RELEASE HOLD |
| ARXIV-IDEA-WEB-AGENT-QA-01 · 2026-11-17 | [WebArena-Pro 2611.17955](https://arxiv.org/abs/2611.17955), [Web Hallucination 2611.18514](https://arxiv.org/abs/2611.18514) | 쇼핑몰·웹 제작사; **허가 사이트의 브라우저 에이전트 QA 시나리오·재현 증거·수정 우선순위 보고** | **12만~35만원 / 2~5영업일 / 중상** | **기존 KMONG-SVC-14 REA_WEB/SITECRAFT 고급 옵션**. 신규 SKU 아님 | '없는 UI 요소 클릭' 방어, 실제 P2 브라우저 테스트. 인증/로그인·고객 데이터/웹 서비스 허가·외부 평가 데이터/모델 상업권·로그 삭제 기준 필요. 현재 NOT_BUILT·RELEASE HOLD |

## 연구 기반 내부 기술 후보 (크몽 게시 예정 목록과 분리)
- **ARXIV-RD-HARNESS-01 (2026-11-17):** [ModHarness-RL](https://arxiv.org/abs/2611.18533) + [CoReMem](https://arxiv.org/abs/2611.17316)에서 가져온 '검증된 실행 기록·문맥 압축·가치 평가' 원리. My Local AI/EAI/HAE에 우선 적용 가능성을 연구하지만 현재 미구현; 고객 상품 아님.
- **ARXIV-RD-TREEMEM-01 (2026-11-17):** [TreeAgent](https://arxiv.org/abs/2611.13946) 구조 보존 문맥 분할 아이디어. EAI/REA_WEB/DATA2WEB 관련. 소스 Apache-2.0 메타데이터만 확인; LICENSE/NOTICE/데이터 별도 검증 필요.

## 운영 불변조건
- 예상 판매가격·납기는 시장 검증 전 가설이며 매회 허위 매출/상품 게시 상태 갱신 금지.
- 실제 새 아이디어를 발견해도 기존 19 SKU/현재 원장의 후보와 고객 목적이 동일하면 **EXTENSION**으로 연결만 하고 중복 후보 ID 생성 금지.
- 기존 후보를 재검토하면 최초 발견일·원본 URL·이전 판단을 보존하고 일자별 재검토 메모만 누적한다.
- 고객 개인/비공개 자료 공개, 유료 API, 권한/상용 출시/크몽 등록은 사용자 별도 승인 필요.


## 2026-11-20 연구 재검토 — ARXIV-2026-11-20-1130-KST
- **기존 ARXIV-RD-HARNESS-01 확장:** [SCH 2611.24357](https://arxiv.org/abs/2611.24357) 상태/증거 분리 및 [Timeout Cascades 2611.24324](https://arxiv.org/abs/2611.24324) 무료 우선 라우팅을 MLA/EAI/HAE/SOVIA/FFAX 내부 옵션으로 검토. 기존 고객문제 중복으로 **신규 SKU/후보 ID 생성 0**.
- **기존 ARXIV-IDEA-REQ-QA-01 재검토:** [SCAFFOLD 2611.23990](https://arxiv.org/abs/2611.23990)의 버전·권한·근거 유효성 원칙을 SVC-07 검수 옵션에 추가 검토. 개념 논문, 구현/검증 없음. 추정 12~35만원·3~6일·중상.
- **기존 ARXIV-IDEA-WEB-AGENT-QA-01 재검토:** [Visual Audit 2611.24867](https://arxiv.org/abs/2611.24867)의 동일 관찰 예산 비교를 SVC-14/REA_WEB 옵션으로 검토. 추정 12~35만원·2~5일·중상.
- **GateWatch 2611.24619:** MLA/SOVIA 규칙 기반 모니터링의 연구 참고만. Gemma/vLLM/SAE 실험 수치는 GTX1050Ti에서 미재현. 모델·데이터·의존권리 미확인.
- **고객 인수/권리:** 로컬 합성 QA, 원본 불변, 명시적 권한, 민감정보 비전송, LICENSE/NOTICE/모델/데이터 상업권리 개별 확인 필수. 신규 19 SKU 변경·크몽 등록·출시·실구현 **없음**.


## 2026-11-24 research review — ARXIV-2026-11-24-1130-KST
- ARXIV-IDEA-REQ-QA-01: [2611.27112](https://arxiv.org/abs/2611.27112), [2611.26666](https://arxiv.org/abs/2611.26666), [2611.27829](https://arxiv.org/abs/2611.27829): existing SVC-07 option, independent policy enforcement and version-bound evidence/contract checks; KRW 120k–350k / 2–5 days / medium-high.
- ARXIV-RD-HARNESS-01: [2611.27090](https://arxiv.org/abs/2611.27090): recovery test pack and state reconciliation, existing internal research only, MLA/EAI HOLD; hypothetical KRW 100k–300k / 2–5 days / medium-high.
- ARXIV-IDEA-SQL-MEM-01: [2611.26665](https://arxiv.org/abs/2611.26665): DBVORA read-only ledger consistency audit extension; KRW 150k–400k / 3–6 days / medium-high.
- Existing customer problems retained, no new candidate IDs/SKUs. Full catalog not independently re-read. Prices unvalidated. Customer-authorized local data, disposable fixtures, independent acceptance, commercial LICENSE/NOTICE/dependency/model/data rights review required. No code reuse, implementation, registration or release.


## 2026-11-27 research review — ARXIV-2026-11-27-1130-KST
- ARXIV-IDEA-REQ-QA-01: [2611.34617](https://arxiv.org/abs/2611.34617), [2611.34875](https://arxiv.org/abs/2611.34875): SVC-07 early risk-stratified tests and diff-scope report; KRW 100k–300k / 2–4 days / medium-high. Full independent acceptance remains mandatory.
- ARXIV-IDEA-SQL-MEM-01: [2611.32636](https://arxiv.org/abs/2611.32636): DBVORA invariant test extension, read-only report; KRW 100k–300k / 2–5 days / medium-high.
- ARXIV-RD-HARNESS-01: [2611.34624](https://arxiv.org/abs/2611.34624), [2611.34327](https://arxiv.org/abs/2611.34327): memory replay and budget comparison, internal research only; KRW 80k–250k / 2–4 days / medium, MLA/EAI HOLD.
- No new customer problem IDs or SKU. Full catalog not reread; prices unvalidated. Customer-authorized local data, independent acceptance, commercial LICENSE/NOTICE/dependency/model/data rights review required. No implementation, registration or release.
