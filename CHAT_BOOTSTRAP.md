> **상시 최우선: 통합 수뇌부 감독 헌장 (2026-10-24 사용자 지정).** 이 채팅은 단순 진도 집계자가 아니라 KIC·PayPal·UGREEN의 **작업 품질·누락·중복·불필요한 개발·일정 위험을 독립 검수하고, 시정 과제를 발행·추적·재검증하는 최상위 감독자**다. 새 채팅 및 “애들 검수” 요청마다 [통합 수뇌부 상시 감독 헌장](docs/SUPERVISOR_MANDATE.md)을 먼저 읽는다. 실제 대회 코드는 각 리드가 변경하며 사용자 승인 게이트를 지킨다. 이 문서 아래 과거 스냅샷은 정본 최신 상태가 아니다.

> **현행 승인(2026-10-24): 작업 순서 최적화 허용.** 당일 목표 검증 완료 후 선행 개발 또는 날짜 건너뛰기 가능. **의존성·BLOCKED·실제 증거·달력일 100% 분리** 필수. [상위 규약](docs/WORK_ORDER_FLEX_POLICY_20261024.md). 기존 2026 일정표·0원 예산·4채팅 유지.

> **장기 총괄 범위 확장(2026-10-24):** 이 저장소는 기존 3개뿐 아니라 앞으로 참가하는 **모든 해커톤의 영구 통합 상황실**이다. [운영 헌장](docs/LONG_TERM_HACKATHON_COMMAND.md) · [2027 공식 일정·후보](docs/2027_HACKATHON_WATCHLIST.md) · [후보 JSON](data/future_hackathons.json). **현재 활성 개발 3개/4개 채팅은 그대로**, 2027 후보 2개는 **미등록**. 자동 감시·지출·신규 등록은 실행하지 않음.

> **PayPal '본선' 공식 규정 정정 및 후속 시간표 (2026-10-24):** PayPal은 별도 추가 개발 본선이 아닌 Stage One 적합성 pass/fail → Stage Two 기존 출품작 심사. [심사·접근·수상 대응 원본표](https://github.com/hibi89/hibi89-paypal-ai-hackathon/blob/lead/paypal/docs/POST_SUBMISSION_JUDGING_PLAN_20261024.md) **11회 점검, 순작업 예상 8h / 보수 확보 16h** (11/13~12/22 전후). **출품 전 82h/164h 개발표는 그대로**; 실 Sandbox/배포/제출 미검증. [공식 규정](https://paypalaihackathon.devpost.com/rules) 참조.

> **PayPal 일별 시간표 — 상위 총괄 필독 (2026-10-24 KST):** [PayPal 원본 18일 계획](https://github.com/hibi89/hibi89-paypal-ai-hackathon/blob/lead/paypal/docs/DAILY_CAPACITY_PLAN_20261024.md) · [상황실 감독 메모](docs/PAYPAL_DAILY_CAPACITY_OVERSIGHT_20261024.md). **예상 82시간 / 지연 포함 권장 확보 164시간**, PayPal 단독 매일 평균 약 9.1시간 필요. **KIC·UGREEN 병행 시 11/11 조기 제출 HIGH RISK**. 시간표/코드/CI의 진실은 PayPal `lead/paypal` 최신 HEAD로 재확인. 실 Sandbox·AI API/Production/Devpost 접수 미검증.

# 해커톤 통합 총괄 — 새 채팅 한 줄로 이어가기

**고정 호출 문구:** `[해커톤총괄 깃헙 레포지토리 확인하고 작업하셈]`

**원격 진입점:** https://github.com/hibi89/hackathon-command-center-2026/blob/main/CHAT_BOOTSTRAP.md  
**저장소:** `hibi89/hackathon-command-center-2026` · **브랜치:** `main`

## 호출 시 즉시 수행
1. GitHub 연결을 이용해 본 저장소의 **원격 최신 `main` HEAD SHA**를 조회하고 본 문서 → `START_HERE.md` → `HANDOFF.md` → `STATUS.md` → `docs/FOUR_CHAT_EXECUTION_PROTOCOL.md` → `SCHEDULE.md` → `RISKS.md` → `data/checkpoints.json` 순서로 복원한다.
2. 사용자가 해당 채팅의 대회(KIC/PayPal/UGREEN)를 명시했거나 이전 확정 역할이 있으면 **그 대회 총괄 겸 개발자**로 실행한다. 대회 지정이 없는 새 채팅에 **이 문구만** 있다면 통합 총괄로 시작한다. 동일한 글자만으로 신규 채팅이 어느 대회의 총괄인지를 구별하는 것은 불가능하므로 임의 대회로 코드를 수정하지 않는다.
3. 기존 활성 3개 대회 `lead/*`의 원격 HEAD 및 `TO_HACKATHON_LEAD.md`와 `LEAD_ACTIVE_WORK.md`를 확인한다. 대회 총괄이라면 자기 저장소의 `lead/*/CHAT_BOOTSTRAP.md`를 읽고 현재 작업을 **직접 개발·테스트·검수·커밋**한다. 통합 총괄이라면 일정·차단·제출·개발 증거 검수 및 상황실 동기화를 실제 수행한다.
4. 구형 7/13개 채팅·작업자 `NEXT_TASK`/`ACTIVE_TASK`/`CURRENT_TASK`는 역사를 보존하되 **실행권이 없다**. 각 리드 `LEAD_ACTIVE_WORK.md`가 현재 우선순위다. 완료 보고·실제 HEAD·코드가 다르면 최신 실증으로 판단하고 기존 정상 기능/기록을 보존한다.
5. 권한·실결제·개인정보 외부 전송·유료 서비스·품질/범위 축소·원본 덮어쓰기는 기존 사용자 승인 게이트를 지킨다. 실제 테스트/실 API/Production/공식 제출은 별도 증거 없이 완료 처리하지 않는다.

## 단 하나의 진입 테이블

| 채팅 역할 | 정확한 저장소 | 확인 브랜치 | 실행 기준 |
|---|---|---|---|
| 통합 총괄 | `hibi89/hackathon-command-center-2026` | `main` | `START_HERE.md → HANDOFF.md → STATUS.md → data/checkpoints.json` |
| KIC 총괄·개발 | `hibi89/hibi89-kic-proofinvest` | `lead/kic` | `docs/roles/lead/LEAD_ACTIVE_WORK.md` |
| PayPal 총괄·개발 | `hibi89/hibi89-paypal-ai-hackathon` | `lead/paypal` | `docs/roles/lead/LEAD_ACTIVE_WORK.md` |
| UGREEN 총괄·개발 | `hibi89/hibi89-ugreen-nas-hackathon` | `lead/ugreen` | `docs/roles/lead/LEAD_ACTIVE_WORK.md` |

**현재 고정 마감(KST)**: KIC 내부 11/10·공식 11/12 10:00 / PayPal 내부 11/11·공식 11/13 05:00 / UGREEN 내부 11/10·공식 11/16 16:45. 현재 제출 상태는 최신 원격 증거/플랫폼 영수증 재검증.

## 항구적인 갱신 계약
- 대회 총괄의 **주요 개발·검수·상태 변경/채팅 이관 종료**: 자기 `LEAD_ACTIVE_WORK.md`, `STATUS.md`, `HANDOFF.md`, `TO_HACKATHON_LEAD.md`와 필요한 소스·테스트 결과를 **그 작업에서** 실제 GitHub에 갱신하고 원격 SHA 확인. 본 `CHAT_BOOTSTRAP.md`는 진입 경로/역할/규칙이 바뀌는 경우에만 수정한다. 동적 작업 ID/SHA를 고정 공시 파일에 박제하지 않는다.
- 통합 총괄의 **주요 감독·변경/채팅 이관 종료**: `STATUS.md`, `HANDOFF.md`, `START_HERE.md`, `data/checkpoints.json` 및 필요하면 `SCHEDULE.md`/`RISKS.md`/`CHAT_BOOTSTRAP.md`를 갱신하고 GitHub `main` HEAD 확인.
- 시간 경과만으로 자동 동기화되거나 백그라운드에서 다른 채팅이 실행되는 것은 아니다. 매번 새 채팅에서 원격 상태를 직접 읽는다. 소스가 없거나 GitHub 접근 불가면 성공이라 하지 않고 제약을 보고한다. 단순 질의/무변경 시 형식적 커밋 금지.

**한 줄 요약:** 사용자 문구 → GitHub 실제 최신 상태 복원 → 역할에 맞는 미완료 실작업 → 증거 검증 → 저장소 인수인계 커밋.

## 2026-10-24 13:29:50 KST — KIC 일별 시간표 공유 진입점
- 새 통합 총괄 채팅은 [KIC 60일 원본 시간표](https://github.com/hibi89/hibi89-kic-proofinvest/blob/lead/kic/docs/roles/lead/DAILY_CAPACITY_PLAN_20261024.md) 및 [통합 감독 규칙](docs/KIC_DAILY_CAPACITY_OVERSIGHT_20261024.md)을 KIC 현재 과제와 함께 열람한다. KIC 자체 총괄 채팅도 동일 원본을 사용한다. 상한·예비·실측·이월을 분리하며 자동 최신화라는 주장은 하지 않는다.

## 2026-10-24 13:53:35 KST — KIC 일일 진척률 100% 기준과 잔여시간 상위 총괄 연결
- 사용자 지시: **매 실제 작업 종료 또는 BLOCKED 시점**에 KIC 1일 핵심 목표를 100점 가중 검증 게이트로 평가해 완료율 및 잔여 예상시간을 공개. [현행 KIC 단일 실적판](https://github.com/hibi89/hibi89-kic-proofinvest/blob/lead/kic/docs/roles/lead/DAILY_PROGRESS.md) / [점수 계산·시간 산정 프로토콜](https://github.com/hibi89/hibi89-kic-proofinvest/blob/lead/kic/docs/roles/lead/DAILY_PROGRESS_PROTOCOL.md).
- 현재 근거 스냅샷(2026-10-24): **당일 원 계획(60일 시간표 공시) 100/100=100%, 잔여 0h**, 별도 Research 인수/CI 26 PASS는 **선행 작업**으로 분리. 10/25 DAKER 권한·공식 양식·초안 계획 **0/100=0%**, 남은 기본 **1h + 오류/검수 예비 3h = 초기 최대 4h**. **실제 작업시간 미계측**. 이 수치는 **계획상 잔여 예상**이지 완료 보증/프로젝트 전체 완성률이 아님.
- 사용자에게는 각 작업 종료 시 `오늘 XX%/100% · 남은 순작업 Xh + 오류예비 Yh = 상한 Zh · 미완료/차단 · 실제 투입(또는 미계측) · SHA/CI`를 보고하도록 KIC `LEAD_FULLSTACK_PROTOCOL.md`에 등록. 상위 통합 총괄도 매 번 `lead/kic`의 **실제 최신 HEAD**를 재조회하여 종료 수치의 최신성을 검증한다.
- KIC 커밋 `c4fc1e54a95b71839959fcc7e410d6ccb5621e75`에서 원본 실적판·지침 확인 가능(상황실 스냅샷, 매번 ref 갱신 확인). 별도 worker 채팅 사용하지 않으며 KIC 계획/코드/공식 제출은 본 상황실이 임의 변경하지 않는다.

## 2026-10-24 KST — PayPal 매 작업 종료 일차 100%·남은 시간 보고 고정
- 사용자 명시 지시: PayPal 개발 총괄은 매 실제 작업을 마칠 때마다 **그날 계획된 검증 완료 기준을 100%로 보고 진행 X%/100%, 남은 예상 Y시간, 남은 안전 확보 Z시간, 실측/미계측, 미완료·이월·증거**를 보고한다. [정식 규약](https://github.com/hibi89/hibi89-paypal-ai-hackathon/blob/lead/paypal/docs/DAILY_PROGRESS_REPORTING.md) / [PayPal 최신 공식 JSON 원장](https://github.com/hibi89/hibi89-paypal-ai-hackathon/blob/lead/paypal/data/paypal_daily_progress.json).
- **원장 현재 기록:** PPL-D01 100%/100%, 남은 예상 0h/안전 0h (quote API 오프라인 부분만 완료); 현재 활성 **PPL-D02 0%/100%, 남은 예상 5h/안전 9h** (영속 DB·CAS·중복 점유/재시작 검증 미착수). 실측 시간 NOT_MEASURED. **전체 3기능/Devpost 완성률을 뜻하지 않는다.**
- 진행률은 증거가 검증된 체크 항목 가중치 합계이며 실제 시간 소모로 증가하지 않는다. 블로커나 예상시간 초과 때 남은 시간과 이월을 재산정하고 과소견적 하지 않는다. 최근 PayPal 정책/테스트 커밋 `b0557a82a6f9a552e5749b0c41bd8d0074cae4dc`; GitHub Actions run 40064258097의 완료 여부는 확인 후 별도 판정. 이전 오프라인 34개 회귀 테스트 CI 성공은 검증됨.
- 상위 총괄은 [PayPal LEAD_ACTIVE_WORK](https://github.com/hibi89/hibi89-paypal-ai-hackathon/blob/lead/paypal/docs/roles/lead/LEAD_ACTIVE_WORK.md)와 [상위 공식 보고](https://github.com/hibi89/hibi89-paypal-ai-hackathon/blob/lead/paypal/docs/roles/lead/TO_HACKATHON_LEAD.md)에서 가장 최근의 X%·Y/Z시간·TESTED/NOT_TESTED·원격 SHA를 직접 확인해 상황실 일정/위험을 조정한다. 각 대회 원본 변경 시 자동 동기화되지 않음.
