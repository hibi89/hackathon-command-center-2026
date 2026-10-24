# 2026-10-24 — 3대회 단일 작업자/3대회 동시 운영 실사 보고

**결론: 운영 구조 통과(문서 기반 정적 계약), 1회 전체 실행 사이클 테스트는 아직 미실시.**

## 사용자 확정 운영 정책
- **세 해커톤(KIC/PayPal/UGREEN)은 서로 병렬로 진행**한다.
- **각 해커톤 내부 기능 개발은 작업자 채팅 단 1개에서 한 번에 기능 1개만** 수행한다.
- 13개 AI 담당 역할(전체 1 + 대회 총괄 3 + 기능 9)은 GitHub 책임 영역으로 유지하되 실사용 채팅방은 **전체 총괄 1 + 대회 총괄 3 + 범용 기능 작업자 3 = 총 7개**다.
- 각 총괄만 단일 READY 지시서를 변경할 수 있고, 지정 기능 브랜치의 실제 결과 보고·테스트를 검수한 후 새 ID/브랜치로 전환한다. GitHub는 자동 실행·알림·분산 잠금을 제공하지 않으며 사용자가 작업자/총괄 채팅에서 수동 호출한다.

## 실사한 단일 활성 지시/진입 경로
| 대회 | 총괄 HEAD 실사 시점 | 단일 지시 파일 | 활성 ID / 브랜치 | 시작 프롬프트 |
|---|---|---|---|---|
| KIC | `b845170c2b81` | [`docs/roles/lead/NEXT_TASK.md`](https://github.com/hibi89/hibi89-kic-proofinvest/blob/lead/kic/docs/roles/lead/NEXT_TASK.md) | **`KIC-R-001` READY** / `feature/research` | [시작 문서](https://github.com/hibi89/hibi89-kic-proofinvest/blob/lead/kic/docs/roles/lead/WORKER_CHAT_START_PROMPT.md) |
| PayPal | `b8d12259307e` | [`docs/dispatch/ACTIVE_TASK.md`](https://github.com/hibi89/hibi89-paypal-ai-hackathon/blob/lead/paypal/docs/dispatch/ACTIVE_TASK.md) | **`PPL-001` READY** / `feature/quote-payment` | [시작 문서](https://github.com/hibi89/hibi89-paypal-ai-hackathon/blob/lead/paypal/docs/dispatch/WORKER_CHAT_PROMPT.md) |
| UGREEN | `3f193407b036` | [`docs/dispatcher/CURRENT_TASK.md`](https://github.com/hibi89/hibi89-ugreen-nas-hackathon/blob/lead/ugreen/docs/dispatcher/CURRENT_TASK.md) | **`UGR-001` READY** / `feature/missing-files` | [시작 문서](https://github.com/hibi89/hibi89-ugreen-nas-hackathon/blob/lead/ugreen/docs/WORKER_START_HERE.md) |

## 점검 항목
- 세 대회 모두 총괄·기능 담당자 별도 브랜치, 단일 활성 READY, 작업자 결과의 feature 브랜치별 `TO_*_LEAD.md`, 총괄 REVIEW/MESSAGE_REVIEW, 후속 대기 큐/검수 게이트 존재.
- 각 대회의 기능 브랜치 3개 메시지함을 최신 원격에서 확인: **활성 과제 실제 시작/종료 영수증 없음**. 따라서 현재 READY는 **대기/준비 완료**이지 기능 구현 성공이나 Sandbox/NAS 실호출 완료 아님.
- KIC: `NEXT_TASK` → `tasks/KIC-R-001.md`; 연구 근거 정규화·오프라인 테스트 6개 이상. 이후 Verification/Risk는 총괄 검수 전 실행 금지.
- PayPal: `ACTIVE_TASK` → PPL-001 공식 Sandbox 기술 적합성/설계 A/B 비교·v0 계약. 아직 Sandbox 인증 실증 미확인.
- UGREEN: `CURRENT_TASK` → UGR-001 공식 Kit/UGOS CLI 지원 능력 표, `feature/missing-files`에만 기록. 실제 NAS 실행 미확인.
- 세 운영 규칙 모두 새로운 채팅방 복원, task ID 및 대상 branch 확인, 역할 전환 전 SHA·검수, 비용 신규 현금 0원·비밀정보 보호 등 정의.
- GitHub 문서 프로토콜과 실제 API 권한 보호/강제 브랜치 보호는 **별개**. 단일 작업자 고정 규칙은 소프트 정책이며, 한 채팅에서 두 작업이 실제 동시에 실행되지 않도록 자동 강제하는 mutex 구현은 없다.

## 발견한 문서 차이
1. **과거 13개 프롬프트는 새로운 7개 채팅 운영에 부적합**. [현행 7개 새 채팅 프롬프트](../CHAT_TRANSITION_PROMPTS_7.md)로 대체. 13개 원본은 역사 자료로 보존하고 경고 표시.
2. **UGREEN 조기 제출 목표:** 이전 전체 공시 `11/14` vs 최신 전담 [UGREEN 실행계획](https://github.com/hibi89/hibi89-ugreen-nas-hackathon/blob/lead/ugreen/docs/UGREEN_EXECUTION_PLAN_20261024.md) `11/10`. 전체 총괄은 **UGREEN 11/10 = 대회 총괄의 더 빠른 목표, 11/14 = 기존 전체 버퍼 점검일**로 분리 기록. 공식 마감 11/16 16:45 KST 불변.
3. KIC/PayPal/UGREEN 내부 역할 문서의 일부 '3명 개별 채팅' 설명·구 HEAD/일정은 **최신 단일 지시/운영 규정이 우선**. 오래된 기록을 실제 현재 실행 상태로 읽지 않는다.
4. KIC는 10/27~28 개발 목표를 잡았으나 `KIC-R-001` READY로 사전 발행했다. 사용자 호출 시 오프라인 승인 범위만 실행 가능, 공통 스키마 동결/실 API는 별도 승인. 일정 제안과 실제 착수는 분리.
5. KIC/PayPal/UGREEN 기능 개발은 팀과 채팅 별개 상태. 단 한 명의 실제 사용자가 3개의 Devpost/DAKER 최종 제출 조작·증빙을 책임지는 점은 변함없다.

## 다음 실제 검수 게이트
1. 사용자가 KIC/PayPal/UGREEN 범용 작업자 채팅을 각 하나씩 연다.
2. 각 작업자에게 **현행 lead 지시 문서** 확인 후 첫 READY 1건만 실행 지시.
3. 작업 종료 보고와 소스/테스트/원격 HEAD를 대회 총괄이 검수한다. 정상 수락이면 lead가 NEXT/ACTIVE/CURRENT_TASK에 다른 task ID/target feature 브랜치를 발행한다.
4. **같은 범용 작업자 채팅**이 신규 대상 브랜치로 실제 전환하여 두 번째 과제를 실행/보고.
5. 이 **작업 종료 → 총괄 검수 → 기능 브랜치 전환**까지 한 사이클 성공해야 비로소 운영 실행 검증 완료라 한다. 현재는 설계·브랜치·문서 검수 완료 단계.

## 보안/작업 범위
- 본 통합 검수는 GitHub 원격 ref·문서·역할 메시지함 대조. 제품 소스 수정·실 Sandbox/NAS/OpenDART 호출·채팅 자동 호출·Devpost 제출·권한 변경 **없음**.
- 총괄/기능 담당의 HEAD는 바뀔 수 있으므로 위 SHA는 실사 당시 값. 다음 실제 작업에서는 항상 해당 lead 원격 HEAD를 새로 조회한다.
