# REQUIREMENTS — 2026 해커톤 3개 통합 관리

## 고정 목표
1. 세 대회 공식 제출 요건·기한 충족.
2. KIC/UGREEN 본선 진출 혹은 공식적으로 확인 가능한 성과 기록.
3. 실제 작동 AI 프로그램과 재현 가능한 GitHub·데모·문서 확보.
4. 이후 판매 가능한 프리랜서 솔루션 포트폴리오 개발. 수상/상금은 부차적 목표.

## 대회별 제품과 기능
- **KIC 확정: ProofInvest** = 산업·기업 리서치 / 공시·재무 교차검증 / 설명 가능한 재무 위험 탐지. 기존 전담 GitHub `hibi89/hibi89-kic-proofinvest` 유지.
- **PayPal 잠정: AI 프리랜서 계약·결제 에이전트** = AI 견적·PayPal 결제 / 납품·단계 관리 / 구독 청구 예외 처리. API Sandbox 기능성과 심사 적합성 확인 전 주제 확정 금지.
- **UGREEN 확정 제품 방향: ProjectReady NAS** = 납품 요구사항과 허가받은 NAS 파일 증거를 대조해 Ready / Blocked / Needs Review를 근거와 함께 제시하는 단일 Uliya Skill. missing-files / version-conflicts / privacy는 단일 Skill의 역할 분담이며, 실제 Uliya CLI·권한·PII 지원은 미검증이므로 지원 불가 기능을 약속하지 않는다. 공식 Kit 분석과 기술 계약 확정은 별도 게이트.

## 전체 총괄 최소 지표(대회별)
- 참가 등록/팀 전환, 주제 확정, 필수 제출물(체크리스트), 실제 작동 기능(0~3), 테스트 성공·실패, 미검증 API/배포/보안, 저장소 URL·브랜치·SHA·CI, 공식 제출, 본선/수상 증빙.
- 항목이 확인되지 않으면 `미확인` 또는 `미적용`으로 기록하고 수치를 지어내지 않는다.

## 제출 조건 — 공식 요약
- KIC: **2026-11-12 10:00 KST** 예선 PDF(공식 양식, 10페이지 이내); 본선 선발 시 **12-22 10:00 KST** 데모 URL/실행 코드 링크/발표 PDF.
- PayPal: **2026-11-13 05:00 KST** 실제 동작 프로젝트, 공개 오픈소스 저장소(루트에 라이선스), 실행 안내 또는 호스팅 데모, 3분 미만 공개 YouTube 시연 및 AI·PayPal 기술 설명.
- UGREEN: **2026-11-16 16:45 KST** 500 English words 이내·1MB 이하 제안 PDF, 공식 규격 pre-test ZIP(압축/해제 둘 다 10MB 이하, 파일당 1MB 이하, 100개 이하). Round 1은 SKILL.md 및 선택적 참조 Markdown만 허용되는 패키지 계약을 확인. 실제 NAS는 본선에서 검증.

세부 원문과 조건은 `projects/*.md`의 공식 링크에서 재확인한다.
## 본선 규모·공식 성과 단계 (2026-10-24 규정 대조)
- KIC: 예선 상위 **12팀 본선**, 그중 최종 **6팀 수상**.
- UGREEN: 예선 상위 **최대 30팀 본선**, 최종 **5개 수상작**.
- PayPal: **공식 본선 정원 없음**. Stage One 테마/API 적합성 pass/fail → Stage Two 기술·디자인·효용·혁신·발표 동등 평가. Stage Two를 자동으로 공식 본선 진출 이력이라고 표현하지 않는다.
- 포트폴리오 단계는 **대회 참가 등록 / 유효 작품 제출 / 공식 발표된 본선 진출(있는 대회) / 공식 수상**으로 분리하고, 증거 없는 수상·본선 이력 금지.
- 신규 채팅 첫 진입점 [START_HERE.md](START_HERE.md), 작업 종료 후 동시 최신화 [CONTINUITY_PROTOCOL.md](docs/CONTINUITY_PROTOCOL.md).
