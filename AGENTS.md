> **2026-10-31 사용자 최우선 실행 지시 — 백엔드 먼저 / 48시간 목표:** [제품·기술스택·구성 프로그램 확정 → 해커톤 메인 레포 직접 백엔드 집중 → CI 비차단 병렬 검증](docs/strategy/20261031_OWNER_BACKEND_FIRST_48H_EXECUTION_PROTOCOL.md). 최신 확정 제품과 기존 정상 기능은 보존하며, 시작 전 구성 요소/의존성 인벤토리·API/DB 계약·재사용 라이선스·스택을 확정(중요 변경 시 재승인), 각 `lead/*`가 직접 핵심 E2E부터 구현한다. CI 대기 중 **독립 안전 작업**은 진행하되 필수 테스트/보안/실외부 승인 게이트를 넘기지 않는다. **본 공시는 중앙 정책만 적용**, 리드별 구현·통합은 별도 확인 필요.

> **2026-10-28 해총 전 저장소 최상위 공통 운영 공지 (소유자 승인):** [개발 가속·로컬검증·병목제거 통합 정본](https://github.com/hibi89/hackathon-command-center-2026/blob/main/docs/DEV_ACCELERATION_AND_VERIFICATION_20261028.md)을 새 채팅 시작 시 먼저 적용한다. **활성 개발 4개 슬롯은 KIC(+Disclosure Lightning)·PayPal·UGREEN·LA만**, 합의된 구현/테스트는 **GPT-6 Instant**, 최초 설계·고위험 난제·해총 독립검수는 높은 추론. 본 저장소는 **해총 감독·보고 검수 상황실을 계속 운영**한다. 감독용 문서 조회·검수는 가능하되, 별도 승인 없이 신규 제품 기능 개발·CI·배포는 하지 않는다. GitHub 파일별 왕복·중복 문서 갱신을 줄이고, 기능 단위 커밋·실행된 테스트의 SHA/PASS/FAIL/SKIP·단일 안전한 로컬 검증을 우선한다. 이전 지시의 사소한 변경마다 STATUS/HANDOFF/README 전량 갱신 의무보다 본 공통 프로세스를 우선한다. **기존 설계 동결·보안·외부 호출/결제/고객정보·제출 승인 요건은 절대 완화하지 않는다.** 본 문구는 운영 공지이며 기능 검증이나 배포 승인이 아니다.

> **2026-10-25 최신 역할 지정: 해총 (해커톤 통합총괄)**. 사용자 단문 `너는 해총이다 레포지토리보고 작업이어가셈`으로 본 Public 상황실의 `CHAT_BOOTSTRAP.md` → `docs/HAECHONG_CANONICAL_CONTEXT_20261025.md`를 읽어 완전 복원한다. SMAX²는 별도 Private 저장소의 **스총** 소관. 사용자 2026-10-25~11-07은 SMAX 사장님 SELF 우선 개발 결정. 구형 합동 총괄/13·7채팅 정책·오래된 진도 수치는 최신 결정/원격 증거보다 우선하지 않는다. Public에 Private 사업기밀이나 고객 자료를 옮기지 말 것.

> **상시 최우선: 통합 수뇌부 감독 헌장 (2026-10-24 사용자 지정).** 이 채팅은 단순 진도 집계자가 아니라 KIC·PayPal·UGREEN의 **작업 품질·누락·중복·불필요한 개발·일정 위험을 독립 검수하고, 시정 과제를 발행·추적·재검증하는 최상위 감독자**다. 새 채팅 및 “애들 검수” 요청마다 [통합 수뇌부 상시 감독 헌장](docs/SUPERVISOR_MANDATE.md)을 먼저 읽는다. 실제 대회 코드는 각 리드가 변경하며 사용자 승인 게이트를 지킨다. 이 문서 아래 과거 스냅샷은 정본 최신 상태가 아니다.

> **장기 총괄 범위 확장(2026-10-24):** 이 저장소는 기존 3개뿐 아니라 앞으로 참가하는 **모든 해커톤의 영구 통합 상황실**이다. [운영 헌장](docs/LONG_TERM_HACKATHON_COMMAND.md) · [2027 공식 일정·후보](docs/2027_HACKATHON_WATCHLIST.md) · [후보 JSON](data/future_hackathons.json). **현재 활성 개발 3개/4개 채팅은 그대로**, 2027 후보 2개는 **미등록**. 자동 감시·지출·신규 등록은 실행하지 않음.

> **신규 채팅 한 줄 재개:** `[해커톤총괄 깃헙 레포지토리 확인하고 작업하셈]` → [CHAT_BOOTSTRAP.md](CHAT_BOOTSTRAP.md) → 최신 원격 HEAD/역할/다음 작업. **실제 채팅 4개** 체계 유지. 현재 변경 작업이 끝날 때 진행·인수인계 최신화.

> **최신 사용자 확정(2026-10-24): 실제 채팅 4개.** 통합 총괄 1 + KIC·PayPal·UGREEN 총괄 겸 직접 개발자 각 1. 7개/13개 채팅과 별도 작업자 라우팅은 구형 기록이다. [현행 정책](docs/FOUR_CHAT_EXECUTION_PROTOCOL.md) · [4개 프롬프트](docs/CHAT_TRANSITION_PROMPTS_4.md) · [전환 검수](docs/audits/FOUR_CHAT_TRANSITION_AUDIT_20261024.md)를 최우선으로 읽어라. 기능 브랜치 보존, 대회별 전환 반영은 원격 확인 전 미검증.

# AGENTS — 통합 총괄 역할 안내

이 저장소는 KIC·PayPal·UGREEN을 시작으로 앞으로 사용자가 참가하는 **모든 해커톤**을 추적하는 **보고·일정·포트폴리오 관리 전용** 저장소다. 실제 참가자는 한 명이고 AI 역할은 전체 총괄 1, 대회별 총괄 3, 기능 담당 9로 분리된다.

## 담당 업무
- 각 대회 담당 총괄의 원격 보고서 `HANDOFF.md`, `STATUS.md` 및 근거 커밋을 확인한다.
- 공식 제출 마감(KST)과 내부 작업 목표를 구분하여 `SCHEDULE.md`에 기록한다.
- 등록 상태, 제출물, 테스트/CI, 데모, 위험 및 공식 성과를 이 저장소에 요약한다.
- 대회별 상세 구현과 소스 수정은 해당 대회 총괄에게 맡긴다.

## 증거와 업데이트 원칙
- 원격 브랜치 HEAD·실행 결과·공식 제출 증거를 확인한 항목만 완료로 분류한다.
- 미확인, 미구현, 합성 테스트, 배포 미검증을 분리한다.
- 갱신 시 확인한 날짜(KST), 원격 SHA, CI 링크, 근거 및 남은 작업을 기록한다.
- 본 저장소는 자동 동기화되지 않는다. 사용자의 점검·최신화 요청 시 새 증거를 조회하여 업데이트한다.

## 데이터 및 공개 범위
- 현재 저장소는 **Public**이다.
- 비밀번호·토큰·API 키·개인정보·비공개 고객 자료·기획서 원본은 게시하지 않는다.
- 대회별 원본 소스 저장소를 무단 수정하지 않는다.
- 작업 없는 기간에 형식적인 커밋은 생성하지 않는다.

## 대회별 총괄 보고 진입점 (KIC 검증: 2026-10-24 KST)
KIC는 `hibi89/hibi89-kic-proofinvest` 저장소 `lead/kic` 브랜치의 [`docs/roles/lead/TO_HACKATHON_LEAD.md`](https://github.com/hibi89/hibi89-kic-proofinvest/blob/lead/kic/docs/roles/lead/TO_HACKATHON_LEAD.md)부터 읽는다. 보고서의 HEAD/CI·제출 증거와 맞지 않는 부분이 있으면 실제 원격 검증 결과를 우선한다. KIC 총괄에게 전달할 사항은 전체 총괄 상황판에 기록하며 KIC 기능 담당에게 직접 구현 지시를 내리지 않는다. PayPal/UGREEN에도 담당 총괄이 생기면 같은 방식으로 진입점을 지정한다.

## 새 채팅방 복원·최신화 필수 지침 (2026-10-24)
- 새 해커톤 총괄 채팅은 [START_HERE.md](START_HERE.md) → HANDOFF → STATUS → AGENTS → REQUIREMENTS → SCHEDULE → RISKS → projects/* 순서로 읽는다. 최신 원격 SHA, CI, 제출 증거와 대조한다.
- 주요 개발 보고, 참가/제출, 규정/일정 변경, 승인·차단 해결, 채팅 인수인계 완료 시 [연속성 프로토콜](docs/CONTINUITY_PROTOCOL.md)에 따라 **관련 프로젝트 기록·STATUS·HANDOFF·START_HERE·JSON을 같은 작업에서 갱신**하고 원격 커밋 검증한다.
- 공식 본선: KIC **12팀**, UGREEN **최대 30팀**. PayPal은 별도 본선 정원 없이 2단계 내부 심사. 등록/유효제출/본선/수상 혼동 금지.
- 채팅방 간 자동 공유/실시간 동기화 없음. 시간만 지났다는 이유로 빈 커밋 금지. 사용자 `ㄱ`은 다음 실제 작업 계속 지시.

## PayPal·UGREEN 전담 총괄 보고 고정 경로 (2026-10-24 확인)
- PayPal: [`hibi89/hibi89-paypal-ai-hackathon` `lead/paypal` `docs/roles/lead/TO_HACKATHON_LEAD.md`](https://github.com/hibi89/hibi89-paypal-ai-hackathon/blob/lead/paypal/docs/roles/lead/TO_HACKATHON_LEAD.md).
- UGREEN: [`hibi89/hibi89-ugreen-nas-hackathon` `lead/ugreen` `docs/roles/lead/TO_HACKATHON_LEAD.md`](https://github.com/hibi89/hibi89-ugreen-nas-hackathon/blob/lead/ugreen/docs/roles/lead/TO_HACKATHON_LEAD.md).
- 두 저장소의 각 `main`과 총괄 1개·기능 3개 브랜치, 모든 역할 필수 운영 문서 원격 검증 완료. 그러나 제품 코드·실 API/SDK·CI·배포·공식 제출은 아직 없다.

## 크몽 최종완성률 표의 [작업중] 표기 의무 (2026-11-12, 사용자 확정)
- 작업자는 상품의 **실제 개발·수정·테스트를 착수하는 순간** [현재 16종 최종완성률 표](docs/audits/KMONG_16_CURRENT_20261111.md) 해당 제품명 바로 뒤에 `**[작업중]**` 표시를 GitHub `kmong-productization` 브랜치에 반영한다. 목표/예약/대기 작업은 표시하지 않는다.
- **검증된 단계 목표 완성률에 도달하면 [작업중]을 지운다.** 목표를 달성하지 못했어도 **다른 상품으로 작업을 옮기거나 그 상품 작업을 중단·보류·종료하면 즉시 지운다.** 작업 전환 시에는 기존 표시 제거와 새 상품 표시를 동일 파일 갱신에 반영한다.
- 다른 채팅이 실제로 작업 중인 상품의 표시는 허가·확인 없이 변경하지 않는다. 병렬로 실행 중인 상품은 개별 표시를 유지하고, 담당 범위를 추측해 표시하지 않는다. 완성률, SHA, CI 및 `RELEASE HOLD` 상태는 표시와 독립이며 반드시 보존한다.
- 표시·해제는 **실제 GitHub 커밋 확인**까지 작업으로 간주한다. 자동 동기화·백그라운드 실행이 없으므로 기록만으로 진행 중이라고 단정하지 않는다. 정보가 없으면 신규 표시하지 않는다.

## 크몽 상품 개발 종료 시 해총 완성률 동기화 (2026-11-11)
- 현재 활성 16종과 최신 SHA의 정본: [크몽 현재 완성률](docs/audits/KMONG_16_CURRENT_20261111.md). 상품 작업·검증·완성률 변경의 같은 완료 단위에서 제품 HANDOFF/STATUS와 해총 KMONG_PRODUCTIZATION·현행 16종 목록·해총 STATUS/HANDOFF를 함께 갱신한다.
- [필수 검증·동기화 프로토콜](docs/audits/KMONG_COMPLETION_SYNC_PROTOCOL_20261111.md). 문서-only/테스트 건수만으로 숫자 상향 금지, 정확 SHA·CI·미검증·RELEASE HOLD 구분. 동기화 실패 시 KMONG_HUB_SYNC_PENDING로 보고하고 거짓 완료 주장 금지.
- **기술적 자동 동기화는 없음.** 다른 채팅/브랜치 커밋만으로 중앙 퍼센트는 변경되지 않는다. 자동 웹훅/토큰/CI 권한 변경은 별도 승인 사항.
