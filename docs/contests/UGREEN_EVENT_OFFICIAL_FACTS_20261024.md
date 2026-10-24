# UGREEN 대회 공식 사실 확인 공시 — 통합 해커톤 총괄용 (2026-10-24 KST)

> **사용자 직접 요청:** UGREEN Devpost Rules / Resources / Starter Kit 자료를 중앙 총괄도 읽을 수 있도록 공시한다. UGREEN 최신 정본은 [UGREEN 공식 상세 브리프](https://github.com/hibi89/hibi89-ugreen-nas-hackathon/blob/lead/ugreen/docs/contest/UGREEN_OFFICIAL_BRIEF_20261024.md)와 UGREEN `lead/ugreen` 현재 HEAD. 공식 규정과 상충 시 Devpost **Rules**가 우선. 이 문서는 대회 정보·감독 지침이지 코드 배포·Devpost 접수·공식 개발 검수 자체가 아니다.

## 1. 운영에 중요한 공식 사실

| 항목 | 공식 내용 |
|---|---|
| 행사 | UGREEN Hackathon 2026 on AI NAS — Bring Your Skills to UGOS |
| 예선 제출 최종 마감 | **2026-11-15 23:45 PST = 2026-11-16 16:45 KST** |
| 예선 제출 필수 | 공식 UGOS Skill Creation Tool로 만들어진 Uliya Skill, **영문 10문항 PDF (답변 합계 ≤500단어)**, **초기 SKILL.md 기반 ZIP ≤10MB** |
| 예선에 불필요 | 실제 NAS 실행/보유, 실동작 영상, 공개 repo, 테스트 보고서 |
| Round 1 선발 | **최대 30개** 프로젝트, 2026-11-21 PT 초청 예정 |
| 본선 실기 | 2026-11-22~28 PT 중 **하루**, iDX6011 Pro 64GB NAS 무료 원격 이용(초청자 한정) |
| 본선 최종 마감 | **2026-11-30 23:45 PST = 2026-12-01 16:45 KST** |
| 본선 제출 필수 | 실제 NAS에서 실행되는 최종 Skill ZIP + 실기 시연 YouTube 영상(3분 미만, 영어 내레이션/자막) |
| 심사 (동일 가중치) | User Value / Innovation & Differentiation / Technical Quality / AI NAS Fit & Validation |
| 트랙 | Workflow Automation / Memories / Creativity / Open Innovation (4종, 1트랙 선택) |
| 총상금 | **USD $46,000** (Gold 20k, Silver 10k, Bronze 6k, Most Creative 5k ×2) |
| 대회 도구 | [공식 Starter Kit](https://ai.ugreen.com/pages/hackathon-starter-kit); 지원 환경 WorkBuddy / Claude / Codex |
| 참가자 정책 | 대한민국 포함 성년 개인 참가 가능, 최대 3인 팀, 작품은 신규 원작 및 권리·AI 도움·외부 데이터 흐름 고지 필수 |

근거: [Official Rules](https://ugreenhackathon.devpost.com/rules) · [Resources / FAQ](https://ugreenhackathon.devpost.com/resources) · [Starter Kit](https://ai.ugreen.com/pages/hackathon-starter-kit). 현지 PT→KST 날짜 변환에 **11월 PST +17h** 적용. 주최 측이 일정·규칙 변경 시 공식 원문을 다시 확인할 것. 대회 페이지의 참가자 숫자는 변동되므로 진행 원장의 고정 성과로 취급하지 않음.

## 2. 총괄용 핵심 구분

- Round1 **공식 제작 도구 실제 사용**은 P0 필수. 원본 자체제작 Skill 초안·211개 합성 테스트·GitHub Actions에서 임시 폴더 복사한 결과만으로는 **공식 Creator 실생성 증거가 아니다**.
- 사용자에게서 전달받은 Codex 보고: 참가자 Windows PC에 `uliya-skill-kit` ZIP(기존 공개 SHA 검증) 설치 성공, Codex 재시작 후 official Skill이 노출돼 공식 작성 절차에 착수했다는 화면. **이 정보는 사용자 보고·화면 기반이며 중앙 GitHub에서 독립 실행을 확인한 게 아니다**. 개인정보성 로컬 설치 경로는 중앙 저장소에 복제하지 않는다.
- **미해결 P0:** Codex의 공식 Tool로 실제 신규 파일 생성/공식 체크 결과 + SHA + 사용자 승인 증거가 아직 이 브리프 작성 시점 제출되지 않았다. `CREATION_NOT_EVIDENCED`, `CHECKER_NOT_RUN_OR_NOT_EVIDENCED`, `NOT_APPROVED_FOR_SUBMISSION`, `DEVPOST_NOT_SUBMITTED`.
- UGREEN 기존 정본 합성 211/211 PASS; 최신 [G16 제안서/Skill ZIP DRAFT CI](https://github.com/hibi89/hibi89-ugreen-nas-hackathon/actions/runs/40087085326) 성공. **합성 테스트는 공식 NAS 실증이 아님**.
- **중앙 총괄 행동**: UGREEN 측에서 실제 Creator 수행 결과가 오면 먼저 사용자/UGREEN 담당자 승인 범위 내에서 출처·생성물·검사·권리 조건을 재검수. 이어 PDF/ZIP 해시·AI 고지/개인정보·단일 Project 제출 조건 및 Devpost 승인권 확인. 무분별한 기능 확장/합성 테스트로 P0 지연 금지. 사용자가 별도 승인하지 않으면 공개 제출 실행 금지.
- 내부 조기 제출 목표 11/10 또는 11/14는 **운영상 목표**, 공식 마감 11/16 16:45 KST가 정본. `DONE 2 / PARTIAL 12 / BLOCKED 3 / NOT_STARTED 7`은 기존 날짜별 계획의 상태이지 실제품 8%라는 뜻이 아님.

## 3. 총괄에서 바로 열 링크

- [UGREEN lead/ugreen START_HERE](https://github.com/hibi89/hibi89-ugreen-nas-hackathon/blob/lead/ugreen/START_HERE.md)
- [UGREEN **공식 대회 규정/지원 링크 종합 공시**](https://github.com/hibi89/hibi89-ugreen-nas-hackathon/blob/lead/ugreen/docs/contest/UGREEN_OFFICIAL_BRIEF_20261024.md)
- [UGREEN 24일 마스터 진행표](https://github.com/hibi89/hibi89-ugreen-nas-hackathon/blob/lead/ugreen/MASTER_PROGRESS.md)
- [UGREEN 공식 Creator 작업자 실행 런북](https://github.com/hibi89/hibi89-ugreen-nas-hackathon/blob/lead/ugreen/docs/submission/G12_OFFICIAL_CREATOR_CODEX_RUNBOOK.md)

**이 공시는 자동 통지가 아니다.** 다음 통합 총괄 채팅이 열리면 해당 저장소의 최신 START_HERE 안내를 읽고 이 문서와 UGREEN 실제 HEAD를 직접 비교한다.
