# GitHub Trending — 2026년 11월 주간 기록

## 2026-11-09 주간 보고(과거 보고 재구성, 미재검증)
- 당시 **GitHub 공식 주간 Trending 직접 조회 차단**으로 보고됨. 대체 집계 Git Homed 2026-11-08 19:57 KST 자료에 근거한 30개 순위를 보고했으므로 공식 GitHub 순위로 취급하지 않는다.
- 관찰 후보: t3code, security-audit-skill, skills, auto-ontology, Scrapling, claude-mem, OpenMausBot, Graphify, MoneyPrinterTurbo, Handy 등.
- 당시 상품 제안: 웹 데이터 수집·CSV 정리, 코드/SQL 구조 분석, 오프라인 음성 변환.
- 전체 30개 README/라이선스/최근 커밋 개별 검증은 완료되지 않았음.

## 향후 기록 형식
주간 종료일(KST), 공식 URL, 조회시각, 공식 1~30위, 증거 링크, 라이선스/활동, 전주·일간 비교, 기존 프로젝트 접목, 독립 상품 TOP3, 미검증을 별도 기록한다.


## WEEKLY-2026-11-16 — 2026-11-16 10:28 KST (RUN WEEKLY-2026-11-16)

### 사실 / 공식 순위 검증
- GitHub 공식 https://github.com/trending?since=weekly 직접 열람: **restricted URL 오류**. 따라서 공식 주간 1~30위와 GitHub 공식 표시 stars this week **모두 미확인**. 다른 사이트의 순위·별 증가량을 공식값으로 대체하지 않는다.
- 비교: github-trending-daily 브랜치 2026-11 DAILY.md 11/13~11/16 읽기 전용 확인. 일간 11/16도 공식 실시간 순위 접근 실패. 일간과 주간의 집계 기간·기준이 달라 직접 순위 비교 불가.
- **독립 대체 집계**: https://trend.ondo.sh/github/en.html (2026-11-15 기준, 'Rising this week' 최근 7일 별 증가 TOP10; GitHub 공식 주간 순위 아님). 아래 +값은 **해당 사이트 자체 집계**이고 GitHub 공식 stars this week가 아니다.

| 대체 성장순서 (공식 주간 순위 아님) | 저장소 / URL | 핵심 기능 / 실용 사례 | 대체 사이트 7일 별 증가 | README | LICENSE | 최근 커밋/릴리스 |
|---:|---|---|---:|---|---|---|
| 1 | [morluto/rea](https://github.com/morluto/rea) | 바이너리 역공학 MCP / 승인된 분석 | +18,387 | 미확인 | 미확인 | 미확인 |
| 2 | [meta/astryx](https://github.com/meta/astryx) | React 디자인 시스템 / UI 제작 | +12,714 | 미확인 | 미확인 | 미확인 |
| 3 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | 사용자명 OSINT / 합법적 계정 조사 | +9,533 | 미확인 | 미확인 | 미확인 |
| 4 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | 코딩 에이전트 관리 / 개발 워크플로 | +9,103 | 미확인 | 미확인 | 미확인 |
| 5 | [mattpocock/skills](https://github.com/mattpocock/skills) | 에이전트 스킬 / 개발 절차 표준화 | +6,615 | 미확인 | 미확인 | 미확인 |
| 6 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | 로컬 음성 생성·더빙 / 자막·녹취 | +6,527 | 미확인 | GitHub API AGPL-3.0 (원문 미확인) | pushed_at 2026-11-16 00:57 UTC, 개별 커밋/릴리스 미확인 |
| 7 | [stablyai/orca](https://github.com/stablyai/orca) | 다중 코딩 에이전트 병렬 실행 / 개발 관리 | +6,475 | 미확인 | GitHub API MIT (원문 미확인) | pushed_at 2026-11-16 01:28 UTC, 개별 커밋/릴리스 미확인 |
| 8 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | 다단계 보안 감사 스킬 / 승인된 코드 감사 | +6,456 | 미확인 | 미확인 | 미확인 |
| 9 | [anthropics/skills](https://github.com/anthropics/skills) | 재사용 AI 스킬 / 업무 자동화 | +5,846 | 미확인 | 미확인 | 미확인 |
| 10 | [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot) | 셀프호스팅 에이전트 / 팀 챗봇 | +5,209 | 미확인 | 미확인 | 미확인 |

- 대체 성장순서 11~30은 자료에 표시되지 않아 미확인. 공식 1~30은 전부 미확인. 개별 README·LICENSE 본문·최신 커밋 SHA·릴리스는 이번 주간 실행에서 위 10개 전체 확인하지 못함. 일부 기존 일간 검증은 날짜가 달라 주간 개별 검증으로 재사용하지 않음.
- 추가 신규 관찰: [NVIDIA/SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator) — 스킬 품질·중복·실행 효과 평가. GitHub API 라이선스 메타데이터 Apache-2.0, pushed_at 2026-11-16 00:53 UTC; README/라이선스 원문/최근 커밋·릴리스 미확인. 이는 11/15 대체 사이트 일간 12위로 표시된 항목이며 **공식 주간 12위가 아님**.

### 분석 — 일간 대비 흐름 / 기존 제품 연계 (미구현)
- 11/13~16 일간 기록의 웹 품질·코드 보안·승인형 에이전트에서, 주간 대체 집계는 **다중 에이전트 제어(t3code/orca), 스킬 표준화·평가(skills/SkillEvaluator), 로컬 음성(VoiceStudio)**의 지속 수요 신호를 보여준다. 다만 표본이 Trending 선정 저장소에 한정되어 시장 수요 증거는 아니다.
- HAE: orca/t3code 승인형 병렬 실행 및 SkillEvaluator 스킬 품질 게이트; SOVIA: security-audit-skill의 독립 증거 검증; DBVORA: 스킬 기반 스키마 QA; REA_WEB: astryx UI 패턴 참고(원본 재배포 금지 전제); KIC: 스킬 평가를 분석 재현성 검증에 참고; PayPal WORKNOVA: 인간 승인 에이전트 제어; UGREEN: NAS 작업 스킬 평가; candle_scraper: 분석 스킬 회귀 테스트. 기존 제품 코드 호환성·성능 미검증.
- **주의:** 2026-11-12~15 보도된 GitHub Actions 악성 PR·토큰 탈취 캠페인 때문에 외부 스킬/Actions를 즉시 실행·설치하지 말고 소스·권한·실행 스크립트를 격리 검토해야 한다. https://www.techradar.com/pro/security/thousands-of-github-repositories-targeted-in-widespread-attack-4-800-accounts-already-compromised-to-steal-cloud-credentials

### 제안 — 독립 판매 TOP3 (모두 가격·기간 추정, 기존 제품 중복 등록 금지)
1. **AI 스킬 품질·중복 검수 패키지** — 고객: AI 자동화 도입 개발팀; 납품: 스킬 충돌/중복 매트릭스, 실행 전후 평가 리포트, 재현 가능한 테스트 케이스; **12만~40만원 / 2~4일 / 난이도 중상**. 원본 NVIDIA/SkillEvaluator (GitHub API Apache-2.0, 원문·NOTICE·종속물 미확인). 차별화: 점수보다 재현 증거·실패 사례·사람 승인 게이트. 필수: 테스트 모델 비용 0원 경로, 고객 스킬 반출 금지, 악성 스크립트 격리, 실제 개선효과 검증. HAE의 기능과 겹치므로 독립 납품 서비스와 기존 제품 기능을 구분.
2. **로컬 음성·자막 업무 자동화** — 고객: 영상 편집자/교육 제작사; 납품: 로컬 설치, SRT, 더빙 테스트, 사용설명서; **15만~45만원 / 2~5일 / 난이도 중상**. VoiceStudio GitHub API AGPL-3.0(원문 미확인); 네트워크 서비스·수정본 배포 의무, 모델 가중치·음성 초상권·데이터 동의 확인 전 번들 재판매 보류. 차별화: 한국어 오프라인·데이터 비반출 검증. 기존 Handy 기반 음성 상품 후보와 통합·중복 제거 우선.
3. **다중 코딩 에이전트 운영환경 구축** — 고객: 1인 개발자·소규모 개발팀; 납품: worktree 격리 설정, 승인 체크포인트, 회귀 테스트·운영 매뉴얼; **15만~50만원 / 2~5일 / 난이도 상**. stablyai/orca GitHub API MIT(원문·종속물 미확인), t3code 권리 미확인. 차별화: 권한 최소화·실패 복구·비용 상한·중복 실행 방지. 고객 에이전트 구독·비밀키·Git 권한을 별도 확인. HAE 및 EAI 기존 개발과 중복 여부 심사 후 독립 서비스로만 취급.

### 변경 및 보존
- 2026-11-13 기준 후보 30개·기존 연구 69개 보존. 신규 조사 repo는 RESEARCH_HISTORY_INDEX.md에 별도 추가; 신규 독립 아이디어는 PRODUCT_IDEAS.md에 중복을 피하여 추가. GitHub 코드/배포/CI/권한 변경 없음.
