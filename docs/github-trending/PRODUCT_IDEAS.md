# GitHub Trending → 크몽·프리랜서 상품화 후보 누적표

> 아이디어와 예상 가격·기간은 **제안/추정**이며 고객 수요·실판매·실구현 검증이 아니다. 기존 상품과 중복 시 독립 신제품을 무단 생성하지 않는다.

| 후보 | 오픈소스/참고 기술 | 고객 납품물 | 초기 예상 가격(원) | MVP 목표 | 필수 검증 |
|---|---|---|---|---|---|
| 웹사이트 품질 점검 | agent-browser, modern-web-guidance | 브라우저 시나리오·스크린샷·HTML 보고 | 70,000~200,000 | 2~8시간 | 브라우저, 테스트 권한, 재배포 권리 |
| 허가된 웹 데이터 수집 | Scrapling | Windows 실행, CSV/XLSX, 중복 제거·로그 | 70,000~350,000 | 2~4시간 | 대상 사이트 약관·권리·변경 대응 |
| 코드 품질·보안 점검 | Ruff, security-audit-skill, Codex Security(연구) | 정적 분석·근거·검증 상태·보고서 | 50,000~250,000 | 2~5시간 | 오탐, AI 비용, 라이선스, 코드 외부 전송 |
| CSV/Excel 로컬 분석 | Sure(아이디어 참고), auto-ontology(연구) | 오프라인 정제·차트·보고 | 60,000~400,000 | 3~8시간 | CSV 호환성, 금융 데이터 권리, AGPL 코드 비포함 여부 |
| AI 개발환경·스킬 검증 | agent-skills, improve(연구) | 스킬·검수 계획·테스트 실행 설정 | 50,000~250,000 | 2~6시간 | 에이전트 호환, 모델 비용, 코드 비밀 |
| 로컬 음성 녹취·자막 | Handy | 녹취·SRT·한국어 UI | 50,000~250,000 | 2~4시간 | 모델·배포 라이선스, 한국어 정확도 |
| 스마트홈 자동화 | ha-mcp | 기기 연동·자동화 규칙·백업 | 100,000~600,000 | 4~8시간 | 실제 장비·권한·보안 |
| 코드/SQL 구조 분석 | Graphify | 의존성 그래프·HTML 보고 | 100,000~500,000 | 3~6시간 | 언어 지원·의존성 라이선스·성능 |

## 기존 프로젝트 접목 후보(최신 코드 미검증)
- HAE: agent-browser/agent-desktop 승인형 실행, agent-skills 검증, Graphify 구조 이해.
- SOVIA: security-audit-skill/Codex Security 감사 근거, Graphify 관계 분석.
- DBVORA: auto-ontology/Graphify SQL·스키마 탐색.
- REA_WEB: Scrapling(허가된 웹 관찰), modern-web-guidance(품질). **원래 웹사이트 분석·재구축 제품과 DATA2WEB 분리 유지**.
- KIC: daily_stock_analysis, auto-ontology 재무 데이터 관계 분석 참고.
- PayPal WORKNOVA: agent-browser Sandbox UI 회귀 테스트.
- UGREEN FlowPilot: Agent Skills 절차 표준화.
- candle_scraper: LZ4 저장 최적화, Kronos·daily_stock_analysis 분석 연구.

## 상품화 게이트
라이선스 및 전이 의무 확인 → 로컬 무료 운영·모델/API 비용 확인 → 원본·보안·데이터 권리 확인 → MVP → 실제 Windows 설치·오류 복구·회귀 테스트 → 고객 설명서·판매 정책 → 등록 승인. MVP 2~4시간과 상품화 1~2일은 목표이지 보장 아님.

## 통합 상품 원장 및 과거 조사 목록
- **30개 수익화 후보의 상세 정보(각각 고객·납품물·가격/시간 추정·라이선스/제약·연계·보고일)**: [MONETIZATION_IDEAS_MASTER.md](MONETIZATION_IDEAS_MASTER.md)
- **69개 원본 저장소 이력(과거 언급일·URL·미재검증 표기)**: [RESEARCH_HISTORY_INDEX.md](RESEARCH_HISTORY_INDEX.md)
- 향후 신규 후보는 **이 브랜치의 본 PRODUCT_IDEAS.md에 조사일·증거·가설·검증 상태를 날짜별 누적**. 월간 예약이 두 브랜치의 후보를 중앙 마스터로 통합한다.


## 2026-11-16 주간 신규 검토 (제안, 미출시; 기존 30개 보존)
| 발견일 | 후보 / 중복 판단 | 타깃 | 납품물 | 가격·기간 추정 | 원본·권리 | 차별화 | 검증 |
|---|---|---|---|---|---|---|---|
| 2026-11-16 | AI 스킬 품질·중복 검수 (기존 AI 개발환경·스킬 검증의 **고도화**, 신규 중복 상품 ID 생성 금지) | AI 자동화 팀 | 충돌 매트릭스·재현 테스트·근거 보고 | 12만~40만원 / 2~4일 | https://github.com/NVIDIA/SkillEvaluator ; API Apache-2.0, 원문·NOTICE·의존성 미검증 | 실행 전후 효과 검증·권한 통제 | 모델 비용 0원 경로, 고객 스킬 반출 방지, 격리 실행, 라이선스 본문 |
| 2026-11-16 | 로컬 음성·자막 자동화 (기존 Handy 후보 **통합 검토**) | 교육·영상 제작자 | 오프라인 설치·SRT·더빙·매뉴얼 | 15만~45만원 / 2~5일 | https://github.com/debpalash/VoiceStudio ; API AGPL-3.0, 원문·모델 권리 미검증 | 한국어·비반출 | AGPL 의무·모델 사용권·목소리 동의·Windows 테스트 |
| 2026-11-16 | 다중 코딩 에이전트 운영환경 (HAE/EAI와 중복 검토) | 1인·소형 개발팀 | worktree 격리·승인·복구 가이드 | 15만~50만원 / 2~5일 | https://github.com/stablyai/orca ; API MIT, 원문·종속물 미검증 | 사람 승인·실패 복구·비용 통제 | 구독비·실기기·Git 권한·보안·중복 실행 |
