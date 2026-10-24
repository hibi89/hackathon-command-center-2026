> **2026-10-24 사용자 지정 최상위 수뇌부 역할:** 새 채팅과 매 감독 요청은 [SUPERVISOR_MANDATE.md](SUPERVISOR_MANDATE.md)를 먼저 읽고 **독립 코드·CI·총작업표 검수, 필요 업무 추가, 불필요한 일 보류, 시정 추적**을 수행한다. [시정 원장](../data/supervisor_findings.json) 미해결 항목을 매번 다시 확인한다. 다음에 나오는 구형 채팅/역할 기록보다 4개 채팅 운영 규칙이 우선이다.

# 통합 총괄 재개·상시 최신화 프로토콜

> 역할: 2026 AI 해커톤 전체 총괄. 단일 출처는 현재 `main`의 검증된 GitHub 문서이고, 개발 원본·상세 진척은 각 대회 총괄 소유 브랜치이다.

## 1. 신규 채팅의 무조건 첫 단계
1. `START_HERE.md` → `HANDOFF.md` → `STATUS.md` → `AGENTS.md` → `REQUIREMENTS.md` → `SCHEDULE.md` → `RISKS.md` → `projects/KIC.md`, `projects/PAYPAL.md`, `projects/UGREEN.md` 순서로 읽는다. `data/checkpoints.json`은 비교/자동 검증용.
2. GitHub 리포지토리 및 브랜치 `HEAD`를 조회하여 보고서의 작성일·커밋 기준점과 구분한다. 변경 파일이 있으면 해당 최신 원격 증거를 확인한다.
3. KIC는 `hibi89/hibi89-kic-proofinvest` `lead/kic`의 `docs/roles/lead/TO_HACKATHON_LEAD.md`를 **고정 진입점**으로 읽는다. 필요 시 같은 브랜치의 `STATUS/HANDOFF`와 Actions·소스 확인. feature 브랜치 직접 지시 금지.
4. PayPal·UGREEN은 전담 저장소가 생기기 전까지 `projects/*.md`의 계획/미검증 상태를 유지한다. 저장소 생기면 URL, 총괄 브랜치, 보고 진입 경로, 원격 SHA, CI 및 담당 상태를 명시한다.

## 2. 새 중요한 작업 종료 시 (동일 응답 안에서)
- (가) **증거:** 사용자 제공 공식 화면, 주최 공식 자료, 대회 총괄 원격 HEAD·보고, CI/실 API/배포/제출 증거를 확보·등급 구분(확인/보고만/미검증/미적용).
- (나) **분석:** 변경된 목표·요구·일정·위험·사용자 승인 요청을 확인; 개발/권한/비용 변경은 승인을 먼저 받는다.
- (다) **업데이트:** 해당 대회 `projects/*.md` → 필요하면 `SCHEDULE.md`·`RISKS.md`·`REQUIREMENTS.md` → `STATUS.md` → `data/checkpoints.json` → `HANDOFF.md` → `START_HERE.md`·`README.md`.
- (라) **검증:** 각각 기존 blob SHA를 조회하고 충돌 없는 최소 수정, 원격 `main` HEAD와 전체 파일 트리·핵심 요약·JSON 파싱 및 서로 다른 파일의 표기 일관성 확인한다.
- (마) **보고:** 사용자에게 변경 파일, 확인한 SHA, 테스트/CI, 안 한 작업 및 다음 우선순위를 간단히 보고한다.
- (바) 변경 없는 단순 질의는 **빈 커밋/형식적 문서 갱신 금지**. 새 채팅 생성만으로 불필요한 기록 갱신 금지.

## 3. 인수인계 필수 10항
1. 전체 목표·확정 요구·기술/산출물.
2. 현재까지 완료한 기능·결정 근거와 변경 내역.
3. 테스트 명령·PASS/FAIL 수·실제/미검증 범위.
4. 완료/진행/대기/차단 및 작업 중단점.
5. 장애·실패 근거·원인·시도·재시도 금지·대안.
6. 저장소·브랜치·원격 SHA·보고 경로.
7. Production URL/Vercel/실행 명령·환경(없는 경우 미적용).
8. 원본 자산/백업·인증 관리·수정 금지 범위(비밀값 미기재).
9. 다음 최우선 작업·절차·완료 기준·승인 필요 사항.
10. 작성 KST·원격 확인 시각·근거·기준 커밋.

단순 상태표가 아니라 **새 채팅에서 바로 다음 작업을 실행할 만큼** 구체적으로 작성한다. 다음 채팅에서 이미 해결된 실패 시도·불필요한 검수 반복 금지.

## 4. 필수 구분 및 기록 규칙
- 참가 등록 ≠ 작품 생성 ≠ 최종 제출 ≠ (해당되는 대회만) 본선 ≠ 수상.
- 합성/오프라인 CI 성공 ≠ 실제 API 성공 ≠ Production 정상 검증.
- 계획·후보 ≠ 사용자 확정. 일부 성공 ≠ 전체 완료.
- PayPal Stage One/Two = 동일 작품의 **심사 절차**, 별도 공식 '본선 진출'이 아님.
- KIC 상위 12팀과 UGREEN 최대 30팀 = **공식으로 공고된 본선 규모**, 실제 선발 전 상태는 미진출/결과 대기.
- GitHub에 미래 자신의 커밋 SHA를 미리 적을 수 없음. 본문 SHA는 **관측 당시 이전 원격 HEAD**로 시점 표기; 실제 새 HEAD는 최종 실 조회 후 사용자에게 보고.
- 모든 공식 시간 KST 변환 확인. Devpost 표기는 11월부터 PST(UTC−8). 공식 Rules/Schedule 차이 발생 시 불일치 기록하고 안전한 내부 목표 사용.

## 5. 보안·권한·비용·데이터 소유
- 본 통합 저장소는 **Public**; 비밀번호, API 키, 사용자 계정 식별정보, 개인 신상, 미공개 고객사 자료, 제출 원본 파일, 개인정보 금지.
- 새 저장소/브랜치 설계·데이터 계약·유료 API·보안 설정 변경 및 기존 원본 수정은 필요 시 사용자 승인.
- KIC 기능 개발·PR·최종 제출 책임은 KIC 총괄. PayPal/UGREEN 담당 총괄도 동일하게 자기 개발 저장소를 소유한다.
- Git 이력 강제 수정, force push, 빈 커밋 반복, 실검증 없이 성공 표현 금지.

## 6. 체크 방식과 업데이트 조건
- 이 문서는 **검증·기록 워크플로**일 뿐 실제 백그라운드 실행기가 아니다. ChatGPT의 다른 채팅/외부 보고는 자동으로 모이지 않는다.
- 사용자 지시 `ㄱ`/상태 점검/주요 작업 종료 또는 채팅방 이동 직전에 GitHub 자료를 **실제로 조회하고** 의미 있는 변경사항이 있을 때 기록한다.
- 추후 `workflow_dispatch`나 cron 자동 점검을 추가하려면 인증·API 한도·보안·비용·오탐 검토하고 사용자 동의 후 분리 구현한다.
- 최종 완료 기준: 원격 GitHub 커밋 존재, SHA 확인, 핵심 문서 상호 일치, 변경 사항 누락 없음. 배포 없는 운영 문서는 Production `미적용`.

## 7. 사용자에게 전달할 신규 채팅 시작 프롬프트
> 너는 2026 AI 해커톤 KIC·PayPal·UGREEN 전체 총괄이다. 먼저 GitHub `hibi89/hackathon-command-center-2026`의 `main/START_HERE.md`부터 `HANDOFF.md`, `STATUS.md`, `AGENTS.md`, `REQUIREMENTS.md`, `SCHEDULE.md`, `RISKS.md`, `projects/*.md`를 읽고 실제 SHA와 맞춰 현황을 복원하라. 전체 일정·위험·공식 성과만 감독하며 각 대회 개발 총괄 역할은 침범하지 말 것. 이후 사용자 `ㄱ` 지시에 따라 가장 중요한 다음 일을 진행하고, 주요 작업이 끝나면 관련 문서·HANDOFF·START_HERE를 GitHub에 갱신 및 원격 SHA 검증하라. 검증 없는 완료 주장 금지.

## 8. 13개 역할별 새 채팅방으로 넘어갈 때
- [13개 인수인계 프롬프트](CHAT_TRANSITION_PROMPTS_13.md)에서 새 채팅이 담당할 **한 역할**만 선택하여 코드블록 전체를 첫 메시지로 전송한다.
- 각 역할이 원격 브랜치 HEAD·소스·CI와 과거 보고 차이를 직접 검증하도록 한다.
- 대회 총괄/기능 담당자의 역할별 문서는 담당 브랜치만 소유한다. 통합 총괄은 상황실 문서만 수정한다.

## 9. 현행 7개 채팅방 동적 작업 라우터가 13개 역할별 채팅 지침에 우선
- 과거 13개 채팅방 프롬프트는 이력으로만 보존. 지금은 [7개 실제 채팅방 재개 프롬프트](CHAT_TRANSITION_PROMPTS_7.md)를 사용.
- 대회별 총괄이 유일한 READY 작업을 관리: KIC `lead/kic:docs/roles/lead/NEXT_TASK.md`, PayPal `lead/paypal:docs/dispatch/ACTIVE_TASK.md`, UGREEN `lead/ugreen:docs/dispatcher/CURRENT_TASK.md`.
- 대회별 범용 작업자 채팅은 매 호출 최신 원격 READY를 확인, **지시 지정 feature 브랜치만** 수정. 총괄 검수 전에 두 번째 기능으로 자동 전환하지 않는다.

## 2026-10-24 KST — 신규 사용자 결정: 4개 채팅 직접개발 체제
- 3개 대회 총괄이 직접 개발/테스트/커밋/검수·제출 준비까지 책임. 실제 채팅은 **통합 1 + 대회 총괄 3 = 4개**로 축소. 별도 작업자 채팅 및 채팅 간 작업 인수 폐지. 기능별 브랜치와 코드·이전 작업 이력은 유지.
- [4개 채팅 현행 정책](docs/FOUR_CHAT_EXECUTION_PROTOCOL.md), [4개 시작 프롬프트](docs/CHAT_TRANSITION_PROMPTS_4.md), [전환 확인](docs/audits/FOUR_CHAT_TRANSITION_AUDIT_20261024.md) 참조. 이전 7개/13개 운영 기록보다 본 최신 결정을 우선.
- 전환 직전 PayPal PPL-001 feature READY_FOR_REVIEW, 합성 테스트 11 PASS(작업자 보고), Sandbox 실 API BLOCKED_BY_ACCESS. 해당 대회 총괄이 직접 최신 HEAD 및 코드/검수 보고를 확인 후 **중복 구현하지 않고 인계**할 것.
- KIC/PayPal/UGREEN 소유 저장소를 이 통합 총괄은 수정하지 않는다. 사용자가 대회별 총괄에 개편을 지시했으나 **그 저장소에 실제 반영됐는지는 별도 GitHub 검수 대기**. 제품 배포·공식 제출 상태 변경 주장 없음.

## 고정 단문 복원 및 상시 최신화
- `[해커톤총괄 깃헙 레포지토리 확인하고 작업하셈]`로 새로운 채팅이 시작되면 [통합 진입](../CHAT_BOOTSTRAP.md)의 역할·HEAD 확인·실행·검수 순서를 따라라.
- 매 중요 작업 종료/채팅 이전에 STATUS, HANDOFF, START_HERE, checkpoints와 필요 프로젝트 기록을 동기화해 커밋하고 실제 SHA를 확인하라. `CHAT_BOOTSTRAP.md`는 역할/경로/재개 규칙이 바뀔 때 갱신한다. 구형 7개/13개 채팅 운영은 미적용. 무변경 빈 커밋 금지.
