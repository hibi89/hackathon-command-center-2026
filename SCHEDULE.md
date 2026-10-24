> **PayPal '본선' 공식 규정 정정 및 후속 시간표 (2026-10-24):** PayPal은 별도 추가 개발 본선이 아닌 Stage One 적합성 pass/fail → Stage Two 기존 출품작 심사. [심사·접근·수상 대응 원본표](https://github.com/hibi89/hibi89-paypal-ai-hackathon/blob/lead/paypal/docs/POST_SUBMISSION_JUDGING_PLAN_20261024.md) **11회 점검, 순작업 예상 8h / 보수 확보 16h** (11/13~12/22 전후). **출품 전 82h/164h 개발표는 그대로**; 실 Sandbox/배포/제출 미검증. [공식 규정](https://paypalaihackathon.devpost.com/rules) 참조.

> **PayPal 일별 시간표 — 상위 총괄 필독 (2026-10-24 KST):** [PayPal 원본 18일 계획](https://github.com/hibi89/hibi89-paypal-ai-hackathon/blob/lead/paypal/docs/DAILY_CAPACITY_PLAN_20261024.md) · [상황실 감독 메모](docs/PAYPAL_DAILY_CAPACITY_OVERSIGHT_20261024.md). **예상 82시간 / 지연 포함 권장 확보 164시간**, PayPal 단독 매일 평균 약 9.1시간 필요. **KIC·UGREEN 병행 시 11/11 조기 제출 HIGH RISK**. 시간표/코드/CI의 진실은 PayPal `lead/paypal` 최신 HEAD로 재확인. 실 Sandbox·AI API/Production/Devpost 접수 미검증.

> **UGREEN 일별 투입시간 및 제출 위험 (2026-10-24 KST)**: [날짜별 보수적 계획·예비·완료기준](https://github.com/hibi89/hibi89-ugreen-nas-hackathon/blob/lead/ugreen/docs/UGREEN_DAILY_EFFORT_PLAN_20261024.md) / [실측 기록](https://github.com/hibi89/hibi89-ugreen-nas-hackathon/blob/lead/ugreen/docs/roles/lead/WORK_TIME_LOG.md) / [대회 총괄→상위 총괄 보고](https://github.com/hibi89/hibi89-ugreen-nas-hackathon/blob/lead/ugreen/docs/roles/lead/TO_HACKATHON_LEAD.md). UGREEN만 계획 **34.25h**, 별도 예비 **26.75h**, 모두 쓰면 **최대 61h**. 하루 상한 평일 보통 3h·주말 4h; KIC(11/12)·PayPal(11/13) 공식 마감일 UGREEN 신규 개발 0h. 11/10 조기 제출은 **SDK 접근 차단으로 조건부**, 11/14 대체 게이트, 공식 11/16 16:45 KST. **다른 두 대회 소요시간·외부 SDK 대기시간은 합산되지 않았으므로 3개 대회 전체의 안전성은 별도 재계산 필요.** 하루 상한 초과는 완료로 주장하지 않고 이월·재산정.

> **KIC 일별 작업시간 통합 열람 (2026-10-24 13:29:50 KST)**: [원본 60일 시간표](https://github.com/hibi89/hibi89-kic-proofinvest/blob/lead/kic/docs/roles/lead/DAILY_CAPACITY_PLAN_20261024.md) · [통합 총괄 검수 기준](docs/KIC_DAILY_CAPACITY_OVERSIGHT_20261024.md). 원본 `lead/kic`는 KIC 총괄이 매 작업 주요 변경 시 최신화한다. 상위 총괄은 매 점검 시 **당일 작업·예비시간·이월·제출위험**을 반드시 확인한다. 과거 채팅/스냅샷 SHA보다 최신 브랜치가 우선한다. (본 공시는 새 제품 구현/제출 증거가 아님.)

# SCHEDULE — 공식 일정 및 내부 운영 목표

**기준일: 2026-10-24 KST**. 모든 시각은 **대한민국 표준시(KST, UTC+09:00)**. `공식`과 `내부` 일정을 혼동하지 말 것. Devpost에 기재된 11월 PST는 KST보다 17시간 느리며, 미국 11월은 서머타임 종료 후 PST(UTC-8) 기준.

## 공식 일정 (검증된 것만)

| KST 날짜/시각 | 대회 | 이벤트 | 유형 | 원문·근거 |
|---|---|---|---|---|
| **11/12 (목) 10:00** | KIC | 예선 PDF 제출 마감 | 공식 | [DAKER](https://daker.ai/public/hackathons/kic-ai-agent-competition) |
| **11/13 (금) 05:00** | PayPal | 완성작 Devpost 제출 마감 | 공식 | [Devpost: 11/12 12:00 PST](https://paypalaihackathon.devpost.com/) |
| **11/16 (월) 16:45** | UGREEN | Round 1 PDF + ZIP 제출 마감 | 공식 | [Devpost: 11/15 23:45 PST](https://ugreenhackathon.devpost.com/) |
| 11/12~19 (날짜 범위) | KIC | 참가자 상호 평가 | 공식 | [DAKER](https://daker.ai/public/hackathons/kic-ai-agent-competition) |
| **11/21 (현지 날짜, 시각 미기재)** | UGREEN | 본선 진출 최대 30팀 발표/초청 이메일 | 공식 | [Devpost](https://ugreenhackathon.devpost.com/) |
| 11/22~28 (현지 일정) | UGREEN | 본선 팀별 배정된 하루 원격 NAS 테스트 | 공식 | [Devpost](https://ugreenhackathon.devpost.com/) |
| **12/01 (화) 16:45** | UGREEN | 본선 최종 Skill ZIP + 3분 이내 영상 제출 | 공식 | [Devpost: 11/30 23:45 PST](https://ugreenhackathon.devpost.com/) |
| 12/02 07:00 ~ 12/16 01:00 | PayPal | 심사 기간 | 공식 | [Devpost 날짜표](https://paypalaihackathon.devpost.com/details/dates) |
| **12/03 (목), 시각 미기재** | KIC | 예선 결과 발표 | 공식 | [DAKER](https://daker.ai/public/hackathons/kic-ai-agent-competition) |
| **12/22 (화) 02:00 (Dates 기준)** | PayPal | 수상자 발표 예정. **Rules는 07:00으로 상충** | 시각 재확인 필요 | [Dates](https://paypalaihackathon.devpost.com/details/dates) / [Rules](https://paypalaihackathon.devpost.com/rules) |
| **12/22 (화) 10:00** | KIC | 본선 데모 URL/코드/PDF 마감 | 공식 | [DAKER](https://daker.ai/public/hackathons/kic-ai-agent-competition) |
| **12/29 (화), 시각 미기재** | KIC | 본선 온라인 발표 예정 | 공식·예정 | [DAKER](https://daker.ai/public/hackathons/kic-ai-agent-competition) |
| **2027/01/11 (월), 시각 미기재** | KIC | 최종 결과 발표 예정 | 공식·예정 | [DAKER](https://daker.ai/public/hackathons/kic-ai-agent-competition) |

## 내부 운영 목표 — 공식 마감이 아님

| 내부 목표(KST) | 대상 | 해야 할 일 |
|---|---|---|
| 10/24~26 | PayPal·UGREEN | **참가 등록 완료 화면 확인(10/24)**. 후속: 기술 규정·실행 가능성 확인 및 각 총괄 개발 준비 |
| 10/27~31 | PayPal | 최소 AI+PayPal Sandbox 흐름 작동 검증, 저장소/라이선스 설정 |
| 10/27~11/05 | KIC | 예선 PDF 품질·참고자료·팀 전환 상태 확인 (실코드 확대는 우선순위 낮음) |
| 11/01~05 | PayPal | 제품 통합/오류 처리/브라우저 시연과 영상 구조 |
| 11/06~09 | KIC·UGREEN | KIC PDF 최종 검수, UGREEN 예선 ZIP 구조 검사 |
| **11/10** | KIC | 조기 제출 목표 |
| **11/11~12** | PayPal | 완성작 조기 제출 목표 및 KIC 접수 확인 |
| **11/13~15** | UGREEN | 최종 패키지 구조/단어수/용량 검사 후 조기 제출 |

## 자원 충돌 원칙
- **KIC 11/12 10시 → PayPal 11/13 05시** 간격은 **19시간**에 불과함. KIC는 **11/10 조기 제출**이 운영상 중요.
- PayPal은 작동 프로그램·코드·영상까지 요구되어 11/13까지의 개발 병목이 가장 클 수 있음.
- UGREEN은 비교적 늦지만 **허용 SDK/패키지 구조**를 먼저 확인하지 않으면 제출 무효 위험.
- 시간 위험이 큰 작업부터 처리하되, 기존 대회 총괄에게 영향이 가는 개발 범위 변경은 사용자 승인.

**시간대/일정 변경 가능성**: 공식 페이지를 업데이트 요청 시 재확인. UGREEN 진출 발표/원격 테스트의 현지 날짜를 임의로 KST 자정 기준 확정하지 않는다.
## 2026-10-24 KST 진행 현황 메모
- PayPal·UGREEN의 참가 등록 직후 화면 확인 완료. 공식 **프로젝트/작품 제출 마감일은 변하지 않음**.
- UGREEN `Create project`는 아직 실행되지 않았고 Round 1 PDF/ZIP은 **미제출**. KIC는 팀 전환/최종 제출 확인 필요.

## 본선 진출 일정의 뜻 — 2026-10-24 공식 검증
- KIC: **12팀 본선** 12/03 발표 → 12/22 본선 MVP/PDF 마감 → **6팀 수상**. 11/12~19 상호평가 참여 조건·최소 투표 횟수는 최신 운영진 안내를 확인할 것.
- PayPal: **별도 Finalists 선정 인원/발표 없음**. Stage One pass/fail, Stage Two 본심사는 동일 제출작 심사 순서. 정식 작품 제출 **11/13 05:00**을 최우선 마감으로 유지.
- UGREEN: **최대 30팀 본선**. 11/21 **미국 PT 기준** 이메일 안내, 팀별 NAS 테스트 일정 통지. 최종 5개 수상작.
- PayPal 수상 발표 시각 공식 공고 상충: Dates는 **12/21 09:00 PST = 12/22 02:00 KST**, Rules는 **12/21 14:00 PST = 12/22 07:00 KST**. 날짜만 확정적으로 관리하고 시각은 근접 시 재검증.

## 2026-10-24 KST — 모든 역할 브랜치에 공시 완료
- [KIC lead 일정표](https://github.com/hibi89/hibi89-kic-proofinvest/blob/lead/kic/docs/COMPETITION_SCHEDULE.md), [PayPal lead 일정표](https://github.com/hibi89/hibi89-paypal-ai-hackathon/blob/lead/paypal/docs/COMPETITION_SCHEDULE.md), [UGREEN lead 일정표](https://github.com/hibi89/hibi89-ugreen-nas-hackathon/blob/lead/ugreen/docs/COMPETITION_SCHEDULE.md).
- 3개 저장소 × 5개 브랜치 = **15개 브랜치 모두 공시 파일과 README 링크 경로 확인**. 공식 행사/마감과 내부 목표를 각 담당자가 자체 문서에서 직접 확인 가능.
- 내부 조기 제출 목표: **KIC 11/10**, **PayPal 11/11**, **UGREEN 11/14**. 계획 날짜는 제출 확인서가 아니며, 공식 마감은 변하지 않았다.
- 전체 총괄의 충돌 대응: KIC/PAYPAL 마감 19시간 차이, PayPal 조기 제출 실패 시 KIC 예선 기획서 작업 방해 금지. 사용자 실제 플랫폼 제출 조작이 필요하면 적시에 요청.

## 2026-10-24 — 각 대회 총괄 최신 순차 일정 교차 검수
- KIC [총괄 마스터 일정](https://github.com/hibi89/hibi89-kic-proofinvest/blob/lead/kic/docs/roles/lead/KIC_MASTER_SCHEDULE_20261024.md): **11/10 조기 제출**. 10/27~28 Research → 10/29~11/01 Verification → 11/02~03 Risk → 11/04 lead 통합 (모두 내부 계획, 실제 개발 착수는 별개).
- PayPal [총괄 실행계획](https://github.com/hibi89/hibi89-paypal-ai-hackathon/blob/lead/paypal/docs/PAYPAL_EXECUTION_PLAN_20261024.md): **11/11 조기 제출**. 10/26~30 quote-payment → 10/31~11/02 delivery → 11/03~06 subscriptions → 11/07~09 통합.
- UGREEN [총괄 실행계획](https://github.com/hibi89/hibi89-ugreen-nas-hackathon/blob/lead/ugreen/docs/UGREEN_EXECUTION_PLAN_20261024.md): **11/10 조기 제출 목표**, 기존 전체 상황실 11/14는 **예비 일정 점검일**. 10/24~26 SDK → 10/27 계약 → 10/28~29 missing-files → 10/30~31 version-conflicts → 11/01~02 privacy → 11/03~05 통합 → 11/07~09 PDF/ZIP 검증. 공식 마감 11/16 16:45 KST 불변.
- 세 대회 동시 진행 / 대회 안에서 범용 작업자 1명이 기능을 차례로 처리. 날짜가 되었단 이유로 단일 READY 지시를 자동 전환하지 않음.

## 2026-10-24 KST — 신규 사용자 결정: 4개 채팅 직접개발 체제
- 3개 대회 총괄이 직접 개발/테스트/커밋/검수·제출 준비까지 책임. 실제 채팅은 **통합 1 + 대회 총괄 3 = 4개**로 축소. 별도 작업자 채팅 및 채팅 간 작업 인수 폐지. 기능별 브랜치와 코드·이전 작업 이력은 유지.
- [4개 채팅 현행 정책](docs/FOUR_CHAT_EXECUTION_PROTOCOL.md), [4개 시작 프롬프트](docs/CHAT_TRANSITION_PROMPTS_4.md), [전환 확인](docs/audits/FOUR_CHAT_TRANSITION_AUDIT_20261024.md) 참조. 이전 7개/13개 운영 기록보다 본 최신 결정을 우선.
- 전환 직전 PayPal PPL-001 feature READY_FOR_REVIEW, 합성 테스트 11 PASS(작업자 보고), Sandbox 실 API BLOCKED_BY_ACCESS. 해당 대회 총괄이 직접 최신 HEAD 및 코드/검수 보고를 확인 후 **중복 구현하지 않고 인계**할 것.
- KIC/PayPal/UGREEN 소유 저장소를 이 통합 총괄은 수정하지 않는다. 사용자가 대회별 총괄에 개편을 지시했으나 **그 저장소에 실제 반영됐는지는 별도 GitHub 검수 대기**. 제품 배포·공식 제출 상태 변경 주장 없음.
