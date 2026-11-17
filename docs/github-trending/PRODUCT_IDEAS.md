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


## 2026-11-13 발견·재검토 (중복 후보는 기존 항목 유지)
- **웹사이트 품질 점검** (기존 후보 보강): 원본 https://github.com/GoogleChrome/modern-web-guidance-src ; 발견일 2026-11-13(이번 색인 확인); 타깃 웹 제작사/쇼핑몰; 납품물 URL 품질 리포트·증거·수정 우선순위; 70,000~200,000원 / 1~2일 추정; 라이선스 미확인·원본 코드 재배포 보류; 차별화 모바일·접근성 재현 증거; 검증: 사이트 허가, README/LICENSE, 브라우저 회귀.
- **AI 개발환경·스킬 검수** (기존 후보 보강): 원본 https://github.com/addyosmani/agent-skills ; 발견일 2026-11-13 재확인; 타깃 개인 개발자; 납품 스킬·검수 체크리스트; 50,000~250,000원 / 1~3일 추정; 라이선스 미확인·원본 스킬 재배포 보류; 차별화 비용·권한·테스트 게이트; 검증: 모델별 호환·비밀 유출·LICENSE.
- **코드 품질·보안 점검** (기존 후보 보강): 원본 https://github.com/openai/codex-security ; 발견일 2026-11-13 재확인; 타깃 소형 SaaS; 납품 근거 기반 취약점 감사; 100,000~300,000원 / 2~4일 추정; 라이선스·상용 이용 조건 미확인, 번들 금지; 차별화 재현 가능한 오탐 분류; 검증: 고객 승인, 민감 코드 외부 전송, README/LICENSE/최근 릴리스.


## 2026-11-14 발견·재검토 (기존 후보 중복 등록 금지)
- **웹사이트 품질 점검** (기존 후보 보강): 원본 https://github.com/GoogleChrome/modern-web-guidance-src 및 https://github.com/ChromeDevTools/chrome-devtools-mcp ; 발견일 2026-11-14 재확인; 타깃 웹 제작사/쇼핑몰; 납품 브라우저 증거·품질 보고서; 70,000~200,000원 / 1~2일 추정; 라이선스 미확인·코드 재배포 금지; 차별화 모바일/접근성·재현 절차; 검증 README/LICENSE, 고객 허가, 회귀 테스트.
- **코드 품질·보안 점검** (기존 후보 보강): 원본 https://github.com/alibaba/open-code-review 및 https://github.com/openai/codex-security ; 발견일 2026-11-14 재확인; 타깃 소형 SaaS; 납품 정적 규칙·오탐 구분 감사; 100,000~350,000원 / 2~4일 추정; 라이선스·API 비용 미확인, 번들 보류; 차별화 증거 기반 위험도; 검증 고객 코드 처리 승인, README/LICENSE, 최근 릴리스, 외부 전송.
- **서버·NAS 가동률 모니터링 설치** (신규 여부는 기존 원장 확인 필요): 원본 https://github.com/louislam/uptime-kuma ; 발견일 2026-11-14; 타깃 소형 사업장/NAS 사용자; 납품 로컬 모니터링·알림 설정·운영서; 120,000~350,000원 / 1~3일 추정; 라이선스·의존성 상용 조건 미확인, 재배포 보류; 차별화 장애 복구 테스트; 검증 보안 설정, 알림 실동작, Windows/NAS 설치.


## 2026-11-15 검증 보강 (기존 후보 갱신 기록; 신규 후보 중복 생성 없음)
- **웹사이트 품질 점검** — 원본 https://github.com/GoogleChrome/modern-web-guidance-src (2026-11-13 최초 관찰, 2026-11-15 검증), https://github.com/ChromeDevTools/chrome-devtools-mcp (2026-11-14 관찰). 타깃 웹 제작사/쇼핑몰; 납품 브라우저 증거·품질 보고서; 가격 70,000~200,000원/기간 1~2일 추정. 차별화 모바일/접근성 재현. 전자 README 확인, API 라이선스 메타데이터 Apache-2.0, 최근 커밋 2026-11-14 확인, latest release 미확인; 후자 라이선스 미확인. 상업 이용 전 LICENSE 원문·의존성·고객 허가 검증.
- **코드 품질·보안 점검** — 원본 https://github.com/alibaba/open-code-review (2026-11-14 관찰, 2026-11-15 검증), https://github.com/openai/codex-security (2026-11-13 관찰). 타깃 소형 SaaS; 납품 코드 위치·오탐 구분 감사; 가격 100,000~350,000원/기간 2~4일 추정. 차별화 재현 증거. 전자 README 확인, API 라이선스 메타데이터 Apache-2.0, 릴리스 v1.13.9 확인; 후자 미검증. 모델 약관·고객 코드 외부 전송·LICENSE 원문 필수 검증.
- **서버·NAS 가동률 모니터링 설치** — 원본 https://github.com/louislam/uptime-kuma (2026-11-14 관찰, 2026-11-15 검증). 타깃 NAS 사용자/소형 사업장; 납품 대시보드·알림·운영서; 가격 120,000~350,000원/기간 1~3일 추정. 차별화 장애 복구 테스트. README 확인, API 라이선스 메타데이터 MIT, 릴리스 2.5.11 확인. LICENSE 원문·의존성·설치 보안·실제 알림 검증 필요.


## 2026-11-16 상품화 검증 업데이트 (기존 후보 3건 갱신, 신규 중복 후보 0)
- **웹사이트 품질·브라우저 감사 (기존 후보)** — 원본 [GoogleChrome/modern-web-guidance-src](https://github.com/GoogleChrome/modern-web-guidance-src) (최초 2026-11-12 기록) + [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) (2026-11-14 관찰). 고객: 쇼핑몰·웹 제작사. 납품: URL별 실브라우저 오류/접근성/성능 증거 및 우선순위 PDF. **7만~20만원 / 1~2일 / 중 (추정)**. 두 원본 모두 2026-11-16 GitHub API LICENSE SPDX **Apache-2.0**, README 파일·최근 커밋·릴리스 조회 완료(본문·종속 라이선스 미감사). 차별화: 모바일 재현/수정 전후 비교. 검증: 고객 허가·민감정보 비수집·Chrome 실증·NOTICE·상표·의존성. 기존 REA_WEB/SVC-14 확장과 중복 가능, 신규 SKU 자동 등록 금지.
- **코드 품질·보안 감사 (기존 후보)** — 원본 [alibaba/open-code-review](https://github.com/alibaba/open-code-review) (2026-11-14 관찰) + [openai/codex-security](https://github.com/openai/codex-security) (2026-11-12 기록). 고객: 소규모 SaaS·개발팀. 납품: 정적 규칙/AI 판정 구분·오탐 재검증·수정 가이드. **10만~35만원 / 2~4일 / 중상 (추정)**. 둘 다 API LICENSE SPDX **Apache-2.0**, README·최근 커밋·릴리스 조회 완료. 차별화: 위치·재현 증거. 검증: 소스 소유자 승인·외부 모델/유료 API OFF·민감정보 보호·LICENSE/NOTICE·모델 서비스 약관·취약점 공개 정책. 기존 SOVIA/코드검수/SVC-07과 중복 주의.
- **NAS·서버 가동률 감시 설치 (기존 후보)** — 원본 [louislam/uptime-kuma](https://github.com/louislam/uptime-kuma) (2026-11-14 관찰). 고객: NAS 운영자·소형 사업장. 납품: 자체 서버 모니터링·알림/복구 테스트·운영서. **12만~35만원 / 1~3일 / 중 (추정)**. API LICENSE SPDX **MIT**, README·최근 커밋·릴리스 2.5.11 조회 완료. 차별화: 로컬 운영·장애 복구 실증. 검증: 설치 권한·실 NAS/Windows·알림/백업 복구·네트워크 보안·라이선스 원문·종속물. 24/7 보장 금지, 기존 UGREEN과 다른 고객 구매 목적. 신규 서비스/등록 여부는 중앙 원장 별도 승인 필요.
- **검증 한계:** 2026-11-16 공식 GitHub Trending 실시간 순위/증가량 미확인. 위는 과거 후보의 원본 GitHub 메타데이터 재확인으로 실제 상업적 수요·재배포 권리·완성품 검증을 뜻하지 않음. 다른 AGPL-3.0/GPL-3.0 프로젝트는 해당 배포·네트워크 의무 검토 전 상용 번들 제외.


## 2026-11-17 일간 발견 — 기존 후보 중복 제거 및 독립 납품 가설 (2026-11-17 KST)

> **추정/제안**이며 상용화 승인 아님. GitHub 공식 Trending 직접 열람 불가; 공식 GitHub 검색 색인 표시 12개 순서만 확인. 오늘의 확정 TOP20 순위가 아님. 이전 30개 후보와 기존 69개 조사 이력, 기존 8개 요약 후보, 11/13~16 추가 기록 모두 보존. 새 후보와 기존 후보의 동일성은 고객 납품물 기준으로 판정한다.

| 독립 판매 후보·중복 판단 | 원본 프로젝트·발견일 | 타깃 고객·납품물 | 가격/기간 추정·난이도 | 라이선스 메타데이터 / 상업 이용 위험 | 차별화·필수 검증 |
|---|---|---|---|---|---|
| **AI 문서·스프레드시트 편집기 설치·맞춤화** (기존 CSV/Excel 로컬 분석 후보와 목적·납품물 다름, **신규 연구 후보 1**) | [dream-num/univer](https://github.com/dream-num/univer), **2026-11-17** | 중소기업 영업·운영팀 / 고객 소유 환경 문서·표 편집기·템플릿·설치·복구서 | **180,000~600,000원 / 2~5일 / 중상** | GitHub API SPDX Apache-2.0. 원문/NOTICE·상용 SDK·추가 모듈·상표·종속물 미감사. 고객 원본·유료 서비스 미사용 | 로컬 우선 업무 템플릿. 실제 브라우저 편집·저장·내보내기·백업/복구·권한·오프라인 동작/라이선스 검증 필수 |
| **에이전트 승인·진행상황 UI** (기존 AI 개발환경·스킬 검증과 다른 UI 납품, **신규 연구 후보 2**) | [ag-ui-protocol/ag-ui](https://github.com/ag-ui-protocol/ag-ui), [backnotprop/plannotator](https://github.com/backnotprop/plannotator), **2026-11-17** | 자동화 운영팀 / 승인·거부·진행상태·감사 UI 및 합성 데모 | **150,000~500,000원 / 2~4일 / 중상** | API SPDX MIT/Apache-2.0. 원문·NOTICE·종속물·모델/API 서비스 계약 미감사 | 사람이 최종 승인하는 에이전트. 권한 분리·중복실행·감사로그·오류복구·접근성·외부 전송/모델 비용 검증 필수 |
| **AI 스킬 품질·중복 평가 서비스** (**기존 AI 개발환경·스킬 검증 후보의 고급 옵션으로 흡수, 중복 신규 상품 아님**) | [NVIDIA/SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator), **2026-11-17** | AI 에이전트 개발팀 / 합성 평가 결과·충돌 분석·수정 우선순위 보고 | **100,000~350,000원 / 1~3일 / 중** | API SPDX Apache-2.0. 원문·NOTICE·평가 데이터·모델 약관 미감사 | 합성 데이터·재현 가능한 평가. 스킬 호환·재현성·오탐·민감정보 외부 전송/유료 API 0 검증 필수 |

### 이번 날짜 기존 후보 재사용 및 권리 주의
- 기존 **웹 품질 감사**는 ChromeDevTools/chrome-devtools-mcp + GoogleChrome/modern-web-guidance-src의 SVC-14 고도화 참고. 기존 **코드 보안 감사**는 alibaba/open-code-review + elementalsouls/Claude-BugHunter의 SVC-07 고도화 참고. 신규 중복 SKU 추가 금지.
- [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills)는 REA_WEB/FFAX UI 고도화 참고; [ggml-org/ggml](https://github.com/ggml-org/ggml)는 로컬 추론 연구, [tradermonty/claude-trading-skills](https://github.com/tradermonty/claude-trading-skills)는 KIC/candle_scraper 분석 체크리스트 참고.
- [Tencent/LoopForge](https://github.com/Tencent/LoopForge)는 HAE/AX Dev Factory 워크플로 연구에 적합하나 GitHub SPDX **NOASSERTION**으로 라이선스·상업 재배포 권리 미확인. 원문 검증 전 소스 통합/재배포 보류.
- 위 3개 TOP 추천 중 신규 연구 후보는 2개, 기존 후보 기능 보강 1개. 실제 크몽 판매 등록·중앙 원장 변경·구현·고객 수요 검증·배포는 **하지 않음**. 이 문서는 브랜치 내 후보 아이디어만 누적.
