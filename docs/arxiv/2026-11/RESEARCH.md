# arXiv 정기 조사 — 2026년 11월

> 이 문서는 사용자 지정 중앙 해총 `kmong-productization` 브랜치의 **연구 기록**이다. 논문 원문에서 확인한 사실, 자체 환경 적용 분석, 신규 판매 제안을 분리한다. 코드·CI·배포·공식 제품 완성률을 변경하지 않는다. 동일한 `ARXIV-YYYY-MM-DD` 구간은 중복 추가하지 않는다.

## ARXIV-2026-11-17

- **run_id:** `ARXIV-2026-11-17-INITIAL`
- **조사일:** 2026-11-17 KST (화요일)
- **최신 공식 출처:** [arXiv cs.AI recent](https://arxiv.org/list/cs.AI/recent) — 2026-11-16 발표 묶음 164편(조회시 첫 페이지 50편). 최신 공지일과 논문 접수일은 다를 수 있다.
- **범위:** 11/16 공개 묶음의 관련 분야 + 11/10~11/13 접수된 후속 검토 후보; 전체 164편 완전 스캔/전수 평가 아님. 선별된 14편의 arXiv 공식 초록/메타데이터 확인. 정량 결과는 **논문 저자 주장**이며 우리 제품에서 재현하지 않았다.
- **구현 상태:** 구현·학습·벤치마크·실 Windows 테스트 **NOT_RUN**. 저작권/모델/데이터 라이선스와 상업 재배포 권리는 개별 완료 전 미확인.
- **중복 메모:** 2026-11-17 앞선 대화의 NLPG/Trace2Eval/MEM-SQL 검토와 본 조사 일부가 겹친다. 논문은 ID 단위로 하나만 관리. 중앙 공식 SKU/크몽 게시 이력 불변.

### A. 사실 — arXiv 원본에서 제목·접수일·초록 확인

| ID / 접수일(UTC) | 실제 논문 제목 | 저자 보고 핵심·한계 | 공개 코드/라이선스 확인 수준 |
|---|---|---|---|
| [2611.18533](https://arxiv.org/abs/2611.18533) · 11/13 | ModHarness-RL: Recasting Harnesses as Learnable and Evolving Programs for Agentic RL | 실행 기록을 typed State로 저장하고 Compression·Steering 프로그램을 후보 생성→실행 검증→과거 기록 재생으로 갱신. CodeSearch/ALFWorld/BIRD SQL에서 대부분 설정에서 고정 harness 대비 성능 개선; 원 논문은 RL 학습 포함 | 공식 구현 GitHub·소스 LICENSE 개별 미확인 |
| [2611.18494](https://arxiv.org/abs/2611.18494) · 11/13 | ARCHER: From Rationale Imitation to Executable Reasoning in Small Language Models | 계산기/실행 검증이 포함된 typed trace와 2단계 학습. 5개 sub-10B 모델에서 강한 도구 기준 대비 macro-average **+5.51%p**(저자 보고); 수학 문제 중심 | 코드·학습 데이터·상업 라이선스 미확인 |
| [2611.18514](https://arxiv.org/abs/2611.18514) · 11/13 | Can Mechanistic Interpretability Help Explain LLM Agent Failures? A Case Study on Web Element Hallucination | 웹 에이전트의 없는 요소 조작 예측(AUC 0.80)·개입이 환각 85% 수정하는 반면 유효 작업 7% 훼손; 프롬프트 형식 민감성 | 코드/모델 권리 미확인, Qwen2.5-7B 실험 |
| [2611.18338](https://arxiv.org/abs/2611.18338) · 11/13 | MEM-SQL: Memory-Empowered Text-to-SQL | 검증 SQL 전체/조각/개념-스키마 매핑과 주문형 스키마 탐색; HARE에서 평균 실행 정확도 **37.1%→50.0%**, 입력 토큰 **-76.6%**(저자 보고). 복수 쿼리 조합은 여전히 어려움 | 코드·데이터 권리 및 상용 재사용 미확인 |
| [2611.18315](https://arxiv.org/abs/2611.18315) · 11/13 | Experts Across Schemas: Agent-Guided Mixture-of-Relational-Experts for Cross-Database Generalization | 스키마·통계 기반 파생 필드 + 그래프 모델. 21 RelBench에서 일부 지표 개선; 모델 사전학습 필요해 소형 PC 즉시 재현 어려움 | 코드·데이터 라이선스 미확인 |
| [2611.18392](https://arxiv.org/abs/2611.18392) · 11/13 | VelServe: Taming Decode Jitters in LLM Inference with Tail-Calibrated Scheduling | 대형 LLM 서빙의 TTFT/TBT P99 초과 억제, 특정 GPU 인프라에서 SLO goodput 2.4~2.9배 등 저자 보고; GTX1050Ti 단일 장비에 수치 전이 불가 | 코드/라이선스 미확인 |
| [2611.17955](https://arxiv.org/abs/2611.17955) · 11/13 | WebArena-Pro: A Heterogeneous, Multimodal, Reproducible Benchmark for Web Agents | 20개 자체 호스팅 웹앱·300개 작업·오디오/비디오 포함. 보고된 상위 에이전트 성공률 62.3%, 재현성 지향 | 프로젝트 페이지 확인, 전체 코드/데이터/권리 미확인 |
| [2611.17933](https://arxiv.org/abs/2611.17933) · 11/13 | OutfitterBench: Evaluating LLM Agents on Long-Horizon Resource Allocation and Commitment Coordination | 200일 가상 장비 렌탈 운영에서 장기 약속·자원제약 유지 평가. 강력 모델도 규칙 기반보다 낮은 사례 존재 | [공개 GitHub](https://github.com/adminblackjack/OutfitterBench) 확인; GitHub **Apache-2.0 메타데이터**, 종속/데이터 사용조건 미검증 |
| [2611.17316](https://arxiv.org/abs/2611.17316) · 11/12 | CoReMem: Cost-Internalizing Memory for Successive Coding Tasks with Prospective Valuation | 다음 코딩 작업의 실행 결과에 따라 기억 단서의 효용·비용 평가. ChainSWE 27B 에이전트 resolve **21.0%→25.7%**, 단계 -17%, 캐시 고려 토큰 -11% 저자 보고 | 코드·학습 필요조건·상업 권리 미확인 |
| [2611.17388](https://arxiv.org/abs/2611.17388) · 11/12 | Time-Consistent Evaluation of Hierarchical Code Graphs for SWE Agents | 역사적 T0 코드 스냅샷/이후 PR을 분리해 미래 정답 누출 방지; 계층형 의존성 그래프 도입 시 상대 F1 개선 저자 보고. 여러 모델/리포지토리 실험의 일반화는 확인 필요 | 재현 코드 및 상업 권리 미확인 |
| [2611.16289](https://arxiv.org/abs/2611.16289) · 11/12 | Eliciting and Mitigating Specification Satisficing in Coding Agents | 개발 에이전트가 일부 요구를 자기 판단으로 포기하는 문제 감지. SatisFix가 요구와 선택 이유를 다시 대조; 저자 보고 DeepSWE 평균 pass@1 **+5.09%** | 코드·라이선스 미확인 |
| [2611.17304](https://arxiv.org/abs/2611.17304) · 11/12 | Where LLM Agents Get Stuck Debugging Databases: Access More Than Reasoning | 운영 DB 사건 8건 관찰에서 락/교착/환경 컨텍스트 접근 부족이 추론 오류와 결합. 쓰기 권한 대신 승인된 읽기전용 포렌식 접근 제안 | 관찰 연구, 재현 도구/권리 미확인 |
| [2611.16245](https://arxiv.org/abs/2611.16245) · 11/12 | Agentic Dashboards: A New Design Paradigm for Visual Analytics | 분석 에이전트가 허용된 의사결정 공간에서 뷰/방법을 조정하는 대시보드 패러다임 **개념 제안**; 완성 제품 성능 실증 아님 | 개념 연구, 코드/라이선스 미확인 |
| [2611.13946](https://arxiv.org/abs/2611.13946) · 11/10 | TreeAgent: Structure-Aware Memory Agent for Processing Long Hierarchical Data | JSON/HTML/YAML/JS를 구조 보존 서브트리로 분할, 경로·잔여 메모리 링크 활용. 4개 메모리 에이전트 평균 +3.61% 저자 보고 | [공개 GitHub](https://github.com/ZJU-LLM-Safety/TreeAgent) 확인; GitHub **Apache-2.0 메타데이터** 및 별도 LICENSES/third_party_licenses 존재. 종속/데이터 권리 추가 검증 필요 |

### B. 분석 — 우리 환경에서 구현 가치가 높은 TOP5

> 기준: 기존 최종설계/구현과 중복 최소화, Windows 11·GTX1050Ti·RAM16GB·로컬 Qwen/Ollama 기반, 추가 유료 API 없이 합성 자료로 프로토타입. 아래 소요 공수는 **합성 데이터/소규모 테스트용 설계·구현 추정**으로 품질보증·고객 환경·연구 결과 완전 재현 시간과 별개.

| 우선 | 근거 | 프로젝트 및 구현 가설 | 합성 MVP 예상 공수(불확실) | 최소 검증 / 주의 |
|---|---|---|---|---|
| 1 | ModHarness + CoReMem | **My Local AI/EAI**: 작업 trace의 검증 성공/실패·소스 SHA·실행 가능한 점검 명령을 저장, 비용·다음 작업 성과에 따른 유용한 기억만 재사용. 전체 RL 훈련은 제외 | **12~30 인시** | 동일 합성 작업 20개에서 메모리 ON/OFF 성공률·토큰·반복오류 비교, 원본 SHA·민감정보 미저장, 지침 오염 방어 |
| 2 | SatisFix + 시간 일관 그래프 | **MLA/FFAX/코드검수**: 요구 REQ-ID와 AI 코드 선택·변경 이유를 매칭, 실행 전 요구 누락·의도적 범위 축소 탐지 | **10~24 인시** | 합성 요구 20개 + 의도적 누락 5개; 오탐과 누락 검출, 기존 P1/P2 검증 경계 유지 |
| 3 | MEM-SQL | **DBVORA**: 사용자가 검증한 읽기전용 쿼리 템플릿/조각, 스키마 해시·만료·허용 테이블, SQL 권한 차단 | **12~30 인시** | 합성 SQLite 30질의; SQL 안전정책 위반 0, 신/구 방식 정답률·지연·토큰 비교; 고객 DB 외부 전송 금지 |
| 4 | TreeAgent | **EAI/REA_WEB/DATA2WEB**: 대형 JSON/YAML/HTML 구조 경로를 유지한 로컬 입력 분할·검색 | **8~20 인시** | 구조 경로·형제 필드 누락 0, 1MB급 합성 문서의 시간/메모리 측정, Python 의존성·라이선스 검토 |
| 5 | WebArena-Pro + 웹 환각 실패 연구 | **REA_WEB/SVC-14**: 허가한 웹 요소 존재 검증, 단계별 브라우저 결과·증거화. 웹 인수 테스트는 P2에 둠 | **12~32 인시** | 합성 테스트 페이지 20개, 없는 요소 작업 차단, 로그/P2 브라우저 실제 검증 필요, 비인가 사이트 크롤링 금지 |

**보류:** VelServe의 대형 서버 서빙 및 MoREGT 대규모 사전학습은 현 GTX1050Ti 단독 환경 비용 대비 즉시 이점 불명. ARCHER는 **typed 실행·계산 검증 원리**만 참고, sub-10B RL 전체 학습은 보류.

### C. 제안 — 중복 없는 크몽 상품화 TOP3

| 순위 | 형태 / 중복 판정 | 구매 고객 및 실납품물 | 예상 가격 / 납기 | 기술·차별화·상업 권리/검증 게이트 |
|---|---|---|---|---|
| 1 | **기존 DBVORA 고급옵션** — 검증 SQL 재활용형 자연어 조회·DB 진단 | 중소기업 내부 업무 DB 관리자; 로컬 조회 템플릿/권한제어/보고서/복구문서 | **15만~40만원 / 2~5영업일 (추정)** | MEM-SQL 원리 자체 구현 가설. SQL injection/쓰기 방지·복잡 JOIN·권한/스키마·Windows 실제 데이터 없는 합성 검증, 고객 권리, 상업 코드 라이선스 필요 |
| 2 | **기존 SVC-07 코드검수 옵션** — 요구 누락·자기합리화 탐지 | 소프트웨어 외주 발주자/개발팀; REQ-테스트 증거 매트릭스·결함/재검증 보고 | **10만~35만원 / 2~4영업일 (추정)** | SatisFix/계층형 그래프 개념, 기존 코드품질 감사와 **신규 SKU 중복 금지**. 소스 보안·정확 SHA·오탐 재검증·권리·고객 인수 필요 |
| 3 | **기존 SVC-14 웹품질 옵션** — AI 웹 에이전트 동작·오류 검증 | 웹 제작사/쇼핑몰; 허용 사이트의 브라우저 자동 QA 시나리오·오류 재현·개선표 | **12만~35만원 / 2~5영업일 (추정)** | WebArena-Pro/웹 환각 연구 참고, 고객 허가 범위/개인정보·브라우저 P2 실증/의존 데이터 권리 필수. 기존 REA_WEB/SITECRAFT와 중복 신규 SKU 금지 |

**판매 가격·기간은 수요조사 전 가설**이다. arXiv 문서 열람 가능 여부와 소스/데이터/가중치/학습 결과의 상업 재배포 권리는 다르다. 저자 코드나 공개 벤치마크를 상품에 바로 포함하지 말 것. 기존 19 SKU/원천29/실제 등록·완성률은 **불변**, 신규 상품 등록 및 제품 구현·배포 **NOT_RUN/RELEASE HOLD**.

### D. 이 회차에서 하지 않은 일 / 후속

- 논문 14개 공식 초록/접수일과 코드를 공개한 2개 GitHub 페이지(README·라이선스 메타데이터) 확인; 다른 논문의 원본 소스·LICENSE·모델 재현성은 **미확인**.
- GitHub 코드 가져오기·사본 생성·모델 다운로드·외부 고객 코드/비밀 업로드·유료 AI 호출·크몽 등록·배포·CI **하지 않음**.
- 차기 주기: 최신 발표분에 날짜 필터를 적용하고 이번 14개 `arXiv ID`를 `RESEARCH_HISTORY_INDEX.md`에서 중복 검사한다. 새 논문이 없으면 문서의 새 조사 결과를 허위로 늘리지 않고 `NO_NEW_RELEVANT`로 기록.
