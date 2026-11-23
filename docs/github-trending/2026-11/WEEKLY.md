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


## WEEKLY-2026-11-23 — RUN WEEKLY-2026-11-23-1029-KST

### 사실 — 공식·대체 자료 분리
- 공식 GitHub Trending https://github.com/trending?since=weekly 직접 접근: restricted URL. **공식 주간 TOP30, 일간 TOP20, 월간 TOP30 및 공식 표시 stars this week/today/month 전부 미확인.** 외부 순번을 공식 순위로 인용하지 않는다.
- **대체 독립 관측** https://zhuikan.com/b/weekly (2026-11-23 표기, UTC 02:00/14:00 스냅샷 기반 주간 별 차이). 아래 1~30은 **대체 사이트 자체 주간 성장순**이며 GitHub 공식 Trending 순위가 아니다. 수치는 변동 가능하며 원본 GitHub의 공식 주간 증가량과 동일하다고 단정할 수 없다.
- github-trending-daily 브랜치 2026-11 DAILY.md의 11/17~11/23 기록 읽기 전용 비교. 11/23 일간도 공식 순위 접근 실패, 외부 ddewhurst 16개 관찰. 순위 직접 비교는 불가.
- 아래 README/Licensing/커밋/릴리스는 **이번 주간 실행에서의 개별 검증**만 기재한다. 이전 일간 검증은 이번 주간 PASS로 재사용하지 않는다.

| 대체 성장순(공식 아님) | 저장소 URL | 핵심 기능 / 실용 사례 | 외부 7일 별 증가 | 이번 회차 개별 확인 상태 |
|---:|---|---|---:|---|
| 1 | [morluto/rea](https://github.com/morluto/rea) | 역공학 에이전트 / 승인된 바이너리 분석 | +12,328 (외부) | README 미확인; LICENSE 미확인; 최근 커밋 미확인; 릴리스 미확인 |
| 2 | [BaaRai/ARTEX](https://github.com/BaaRai/ARTEX) | 자동 침투테스트 / 승인된 보안 평가 | +11,877 (외부) | README 미확인; LICENSE API AGPL-3.0 (원문 미확인); 최근 커밋 미확인(pushed_at 11/22 UTC); 릴리스 미확인 |
| 3 | [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | 취약점 조사 스킬 / 코드 보안 검수 | +10,616 (외부) | README 미확인; LICENSE 미확인; 최근 커밋 미확인; 릴리스 미확인 |
| 4 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | 코딩 에이전트 원격 제어 / 개발 운영 | +10,025 (외부) | README 미확인; LICENSE 미확인; 최근 커밋 미확인; 릴리스 미확인 |
| 5 | [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) | 모델 접근 플러그인 / 개인 실험 | +7,302 (외부) | README 미확인; LICENSE 미확인; 최근 커밋 미확인; 릴리스 미확인 |
| 6 | [stablyai/orca](https://github.com/stablyai/orca) | 다중 에이전트 운영 / 개발팀 작업 관리 | +7,221 (외부) | README 미확인; LICENSE 미확인; 최근 커밋 미확인; 릴리스 미확인 |
| 7 | [storytold/craft-anything](https://github.com/storytold/craft-anything) | 소프트웨어 분석 / 재구현 연구 | +6,880 (외부) | README 미확인; LICENSE 미확인; 최근 커밋 미확인; 릴리스 미확인 |
| 8 | [obra/superpowers](https://github.com/obra/superpowers) | 개발 스킬 프레임워크 / 표준 개발 | +6,062 (외부) | README 미확인; LICENSE 미확인; 최근 커밋 미확인; 릴리스 미확인 |
| 9 | [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5) | 게임 실행파일 포팅 / 권리 확인된 연구 | +6,020 (외부) | README 미확인; LICENSE 미확인; 최근 커밋 미확인; 릴리스 미확인 |
| 10 | [ccch1mneyyy/dsh-Go](https://github.com/ccch1mneyyy/dsh-Go) | 모바일 에이전트 / PC 원격 제어 | +5,886 (외부) | README 미확인; LICENSE 미확인; 최근 커밋 미확인; 릴리스 미확인 |
| 11 | [anefzaoui/misterdownloadmanager](https://github.com/anefzaoui/misterdownloadmanager) | 다운로드 관리자 / 파일 관리 | +5,731 (외부) | README 미확인; LICENSE 미확인; 최근 커밋 미확인; 릴리스 미확인 |
| 12 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | 코딩 스킬 / 불필요한 코드 감소 | +5,478 (외부) | README 미확인; LICENSE 미확인; 최근 커밋 미확인; 릴리스 미확인 |
| 13 | [mattpocock/skills](https://github.com/mattpocock/skills) | 개발자 스킬 / 코드 작성 절차 | +5,377 (외부) | README 미확인; LICENSE 미확인; 최근 커밋 미확인; 릴리스 미확인 |
| 14 | [nexu-io/html-anything](https://github.com/nexu-io/html-anything) | 편집 가능한 모션그래픽 / 쇼츠 제작 | +5,254 (외부) | README 미확인; LICENSE 미확인; 최근 커밋 미확인; 릴리스 미확인 |
| 15 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | 로컬 음성 생성·전사 / 영상 자막 | +5,226 (외부) | README 미확인; LICENSE 미확인; 최근 커밋 미확인; 릴리스 미확인 |
| 16 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | 에이전트 성능 최적화 / 개발 절차 | +5,186 (외부) | README 미확인; LICENSE 미확인; 최근 커밋 미확인; 릴리스 미확인 |
| 17 | [ItsNotRexed/Leonida](https://github.com/ItsNotRexed/Leonida) | 게임 재컴파일 / 권리 확인된 연구 | +5,175 (외부) | README 미확인; LICENSE 미확인; 최근 커밋 미확인; 릴리스 미확인 |
| 18 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | 웹 수집 API / 허가된 데이터 추출 | +4,882 (외부) | README 미확인; LICENSE 미확인; 최근 커밋 미확인; 릴리스 미확인 |
| 19 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | 최근 동향 리서치 / 근거 조사 | +4,853 (외부) | README 미확인; LICENSE 미확인; 최근 커밋 미확인; 릴리스 미확인 |
| 20 | [libracoder/kiri](https://github.com/libracoder/kiri) | 컨테이너 런타임 / 로컬 개발 | +4,702 (외부) | README 미확인; LICENSE 미확인; 최근 커밋 미확인; 릴리스 미확인 |
| 21 | [dream-num/univer](https://github.com/dream-num/univer) | 문서·시트 SDK / 업무 UI | +4,499 (외부) | README 미확인; LICENSE 미확인; 최근 커밋 미확인; 릴리스 미확인 |
| 22 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 디자인 검수 스킬 / UI QA | +4,300 (외부) | README 미확인; LICENSE 미확인; 최근 커밋 미확인; 릴리스 미확인 |
| 23 | [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | 디자인 품질 스킬 / UI 개선 | +4,068 (외부) | README 미확인; LICENSE 미확인; 최근 커밋 미확인; 릴리스 미확인 |
| 24 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | 레퍼런스 기반 UI 스킬 / FE 제작 | +3,964 (외부) | README 미확인; LICENSE 미확인; 최근 커밋 미확인; 릴리스 미확인 |
| 25 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | 에이전트 플러그인 실행기 / 개발 자동화 | +3,954 (외부) | README 미확인; LICENSE 미확인; 최근 커밋 미확인; 릴리스 미확인 |
| 26 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | 보안 감사 스킬 / 검증 보고 | +3,940 (외부) | README 미확인; LICENSE 미확인; 최근 커밋 미확인; 릴리스 미확인 |
| 27 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | 앱 CLI 생성 / 업무 자동화 | +3,918 (외부) | README 미확인; LICENSE 미확인; 최근 커밋 미확인; 릴리스 미확인 |
| 28 | [google-research/paper-orchestra](https://github.com/google-research/paper-orchestra) | 논문 작성 에이전트 / 연구 지원 | +3,896 (외부) | README 미확인; LICENSE 미확인; 최근 커밋 미확인; 릴리스 미확인 |
| 29 | [erkamyaman/rust-anything](https://github.com/erkamyaman/rust-anything) | 행동 비교 기반 Rust 변환 / 레거시 이전 | +3,822 (외부) | README 미확인; LICENSE 미확인; 최근 커밋 미확인; 릴리스 미확인 |
| 30 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | 코드·SQL 지식그래프 / 구조 분석 | +3,687 (외부) | README 미확인; LICENSE 미확인; 최근 커밋 미확인; 릴리스 미확인 |

- **추가 관찰(대체 30위 밖)**: [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill) 대체 37위 +3,552; 로컬 FFmpeg 기반 자막·쇼츠·리프레임. GitHub API SPDX MIT, pushed_at 2026-11-23 00:22 UTC; README/최근 커밋 SHA/릴리스 원문 미확인. [nexu-io/html-anything](https://github.com/nexu-io/html-anything)은 GitHub API 메타데이터 응답에서 라이선스·설명 확인 불가이므로 상업 재배포 권리 미확인.
- BaaRai/ARTEX는 GitHub API SPDX AGPL-3.0, pushed_at 2026-11-22 22:01 UTC 확인. LICENSE 원문/종속물·최근 커밋 SHA/릴리스 미확인. 위 표의 나머지 개별 검사는 NOT_RUN. **모든 저장소를 검증 완료로 주장하지 않음**.

### 분석 — 최근 7일 및 일간 대비 새 흐름
- 11/23 일간 외부 목록의 Claude-BugHunter, firecrawl, superpowers, CLI-Anything가 주간 대체 상위 30에도 등장한다. 주간에는 t3code/orca/dsh-Go 등의 **다중·원격 에이전트 운영**, impeccable/hallmark/taste-skill 등의 **디자인 품질 스킬**, html-anything/VoiceStudio의 **편집 가능한 영상·음성**이 추가로 부각된다. 이는 GitHub 별 증가 관측이지 구매 수요 실증이 아니다.
- HAE: t3code/orca/CLI-Anything 승인형 작업관리 참고. SOVIA: Claude-BugHunter/security-audit-skill의 재현 근거 검수. DBVORA: Graphify의 SQL 구조 그래프. REA_WEB: impeccable/taste-skill 레퍼런스 UI QA. KIC: last30days-skill 출처 기록. PayPal: 승인형 에이전트 작업 추적. UGREEN: kiri의 로컬 런타임 연구. candle_scraper: firecrawl의 허가된 수집·출처 추적. **전부 분석만 수행, 기존 저장소에 코드 결합 없음.**
- 게임 포팅/역공학/자동 침투 테스트는 별도 소프트웨어 권리·대상 소유자 허가·공격 범위·AGPL 의무 때문에 즉시 크몽 상품화에서 제외. 무료 모델 무제한 주장도 실제 약관·비용 검증 전 채택하지 않는다.

### 제안 — 기존 저장소 없이 독립 납품 TOP3 (추정, 미출시)
1. **한국어 쇼츠·자막 로컬 제작 패키지**: 고객 강의자·팟캐스터·소규모 마케터; 납품 MP4 3~5개, SRT, 썸네일, 재편집 설명서. **8만~25만원 / 1~2일 / 난이도 중 (추정)**. 원본 https://github.com/kajisho5/ffmpeg-skill (GitHub API MIT, 원문 미검증), https://github.com/nexu-io/html-anything (라이선스 미확인); 후자 소스 번들/상업 재배포 HOLD. 차별화 한국어 수동 교정·무료 로컬 렌더·수정 가능한 납품. 필수 Windows 1050Ti 실제 렌더, 음원/영상 권리, 폰트·코덱, 자막 싱크, FFmpeg 종속 라이선스. 기존 autoclip·Handy/VoiceStudio 후보와 **중복 통합**.
2. **레퍼런스 UI 품질 감사·개선 보고**: 고객 쇼핑몰·소형 웹 제작사; 납품 화면별 차이표·반응형 캡처·수정 우선순위·검증 보고. **7만~25만원 / 1~3일 / 난이도 중 (추정)**. 원본 https://github.com/pbakaus/impeccable , https://github.com/Leonxlnx/taste-skill (LICENSE 원문·상업 권리 미확인, 직접 재배포 HOLD). 차별화 레퍼런스 대비 실측·모바일 재현·기능 검수 분리. 필수 고객 사이트 허가, 이미지/폰트 권리, 브라우저 실측, 개인정보 비수집. REA_WEB·FFAX와 별도 독립 **감사 서비스**로만 검토.
3. **로컬 코드·SQL 구조 시각화 보고서**: 고객 프리랜서 개발자·레거시 인수팀; 납품 읽기전용 의존성·SQL 관계 그래프, HTML/PDF, 위험·미확인 목록. **10만~35만원 / 1~3일 / 난이도 중상 (추정)**. 원본 https://github.com/Graphify-Labs/graphify , https://github.com/HKUDS/CLI-Anything (라이선스 원문·종속물 미확인, 재배포 HOLD). 차별화 외부 업로드 0·근거 파일 위치·수동 확인. 필수 고객 소스 취급 동의, 로컬 오프라인 검증, 정확성·대용량 성능, SQL 비밀 마스킹. DBVORA/SOVIA/기존 Graphify 후보와 중복 방지.

### 안전·보존
- 기존 2026-11-13 기준 상품 30개·조사 이력 69개 및 11/16 기록 보존. 기존 코드/CI/권한/배포/고객 자료·유료 API 변경 없음. 주간 브랜치 이외 쓰기 없음. 공식 순위와 상업 이용 권리 미확인은 그대로 미확인 처리.
