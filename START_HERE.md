# START HERE — 2026 AI 해커톤 통합 총괄 재개 지점

> **2026-10-24 KST 검증된 스냅샷**. 채팅방이 달라져도 이 저장소를 통해 전체 운영을 복원한다. **자동 동기화 아님**. 읽은 날의 현재 `main` HEAD·다른 대회 원격 HEAD를 다시 확인한다.
>
> 저장소: `hibi89/hackathon-command-center-2026` · 기본 브랜치: `main` · 현재 Public · 웹앱/배포 대상 아님.

## 0. 새 채팅 첫 동작 (필수)

당신은 **KIC·PayPal·UGREEN 통합 해커톤 전체 총괄 GPT-6**이다. 실제 참가자는 사용자 **1명**, 최종 결정권자다. 대회별 총괄 3명과 기능 담당 9명은 각자 별도 AI 채팅 역할이며 자동 메시지 공유는 없다.

1. **이 `START_HERE.md` → 루트 `HANDOFF.md` → `STATUS.md` → `AGENTS.md` → `REQUIREMENTS.md` → `SCHEDULE.md` → `RISKS.md` → `projects/*.md` → `data/checkpoints.json`** 읽기.
2. `main`의 실제 원격 **HEAD SHA**와 보고서의 확인 시점을 대조한다. 과거 채팅보다 원격 GitHub와 공식 제출 증거를 우선한다.
3. KIC는 [전용 최신 총괄 보고서](https://github.com/hibi89/hibi89-kic-proofinvest/blob/lead/kic/docs/roles/lead/TO_HACKATHON_LEAD.md)를 **`lead/kic` 브랜치 지정하여** 읽고, 필요하면 CI 및 기능 브랜치 SHA를 확인한다. `main`의 KIC 역할 문서만 보아서는 안 된다.
4. PayPal·UGREEN 총괄 저장소는 **이 스냅샷 기준 미생성**. 생성되었는지 GitHub에서 검색 후 확인한다. 없으면 계획·확정 전제로 실제 제작했다고 말하지 않는다.
5. 이력·최신 상태가 다르면 **그 차이를 보고하고 증거로 수정**한다. 이전 채팅을 못 읽어도 루트 문서와 대회별 공식 소스로 후속 작업 가능하도록 한다.
6. 새 사용자 요청이 `ㄱ`이면 **보류된 다음 실제 작업**을 안전하게 수행하고, 주요 변경 종료 때 [갱신 프로토콜](docs/CONTINUITY_PROTOCOL.md)을 적용한다. 단순 열람 때 형식적인 커밋은 하지 않는다.

## 1. 세 대회 상태 (2026-10-24 KST 스냅샷)

| 대회 | 참가 등록 | 아이템 | 코드/저장소 | 공식 제출 단계 | 공식 본선 규모 |
|---|---|---|---|---|---|
| [KIC](projects/KIC.md) | 자이언츠파크 팀 생성 화면 확인; **'팀으로 전환' 미검증** | **ProofInvest 확정** | [KIC GitHub](https://github.com/hibi89/hibi89-kic-proofinvest), Python 합성 테스트 9 PASS·CI 성공 | **PDF 예선 미제출** | **상위 12팀** (최종 6팀 수상) |
| [PayPal](projects/PAYPAL.md) | Devpost 참가자 `My hackathon projects` 화면 확인 | AI 프리랜서 계약·결제 **잠정** | 전담 저장소 미생성, API/코드 미착수 | 작품 미생성·**미제출** | **정원 지정 없음**, Stage One pass/fail 뒤 Stage Two 본심사 |
| [UGREEN](projects/UGREEN.md) | Devpost `Thanks for registering!` 성공 화면 확인 | NAS 프로젝트 파일 관리 Skill **잠정** | 전담 저장소 미생성, Skill SDK 실검증 전 | Round 1 PDF/ZIP **미제출** | **최대 30팀**, 최종 5개 상 |

**목표 우선순위**: ①유효 제출 ②KIC/UGREEN 본선 또는 공식 입증 성과 ③실제 작동 완성품 ④공개 포트폴리오 ⑤판매 가능 상품화 ⑥수상/상금. **PayPal의 Stage Two를 공식 본선 진출 경력이라고 부르지 않는다.** 참가 등록은 최종 제출/수상과 구분한다.

## 2. 가까운 마감 — 모두 KST

| 마감 | 대회 | 실제로 완료해야 하는 것 |
|---|---|---|
| **2026-11-12 목 10:00** | KIC | 공식 10페이지 이하 PDF 기획서 업로드 + 팀 권한/최종 제출 확인. **내부 조기 제출 11/10** |
| **2026-11-13 금 05:00** | PayPal | 의미 있는 PayPal+AI 앱, 공개 오픈소스 소스·라이선스, 작동 데모/실행 안내, 3분 미만 공개 YouTube, 영어 설명 및 Devpost 제출 |
| **2026-11-16 월 16:45** | UGREEN | 영문 500단어 이하 PDF(1MB 이하) + 공식 Uliya 형식 SKILL.md 중심 ZIP, Devpost Round 1 제출 |

- KIC **11/12~19** 상호평가 후 **12/03** 본선 발표. 투표 참여 조건은 KIC 총괄이 공식 최신 공지 재검증한다.
- UGREEN **11/21 PT** 최대 30팀 본선 통지, **11/22~28 PT** 지정 NAS 원격 테스트, **12/01 16:45 KST** 본선 ZIP+영상 제출.
- PayPal은 분리된 본선 진출 발표 일정 **없음**. 심사 Stage One/Two는 내부 채점 순서다. 수상 결과 발표 12월 하순 예정(공식 Rules와 Dates 시간 차이, 추후 재확인).
- 상세 일정·이력은 [SCHEDULE.md](SCHEDULE.md)에 있다.

## 3. 지휘 체계·코드 소유권

```text
전체 총괄 = 이 저장소만 수정 (진행·일정·위험·인수인계)
├─ KIC 총괄 = hibi89/hibi89-kic-proofinvest @ lead/kic
│  ├─ feature/research
│  ├─ feature/verification
│  └─ feature/risk
├─ PayPal 총괄 = 아직 전담 GitHub/역할 브랜치 없음
│  ├─ 견적·결제 (잠정)
│  ├─ 납품 거래 (잠정)
│  └─ 구독 청구 (잠정)
└─ UGREEN 총괄 = 아직 전담 GitHub/역할 브랜치 없음
   ├─ 파일 누락 (잠정)
   ├─ 중복/버전 (잠정)
   └─ 개인정보 노출 (잠정)
```

**총 13개 AI 역할, 실제 참가자는 사용자 단 1명.** 이 저장소에는 경영 상황판만 유지하고 개발·검수·통합·제출은 각 대회 총괄이 맡는다. 다른 저장소/브랜치를 승인 없이 수정하지 않는다.

## 4. 가장 중요한 미해결 문제·다음 실제 작업

1. **PayPal P0**: 전담 총괄 확보 → PayPal Developer Sandbox 계정 접근 가능 확인 → 두 설계안 비교·승인 → 주문 승인/결제/상태 확인 최소 end-to-end 개발 → 소스·라이선스·영상·Devpost 유효 제출.
2. **KIC P0**: 기존 KIC 총괄에게 예선 PDF·'팀으로 전환'·상호평가 참석 필요 여부를 확인. KIC 개발은 침범하지 않음.
3. **UGREEN P1**: 전담 총괄 및 저장소 → 공식 Skill Developer Package/Uliya CLI/권한 확인 → 아이템 승인 → 영문 PDF 및 규격 ZIP. NAS 하드웨어 구매 불필요.
4. **공통**: 세 대회 마감 충돌 조율, 제출 증빙 수집, 공개 GitHub의 개인/키/비공개 전략 유출 방지. Public 저장소 가시성은 사용자 승인 없이 변경 금지.

## 5. 고정 문서 인덱스 및 최신화 계약

- [HANDOFF.md](HANDOFF.md) — 10개 항목 인수인계. **새 채팅에서 두 번째로 읽기**.
- [STATUS.md](STATUS.md) — 검증된 최근 진행·지표·브랜치 SHA/CI.
- [SCHEDULE.md](SCHEDULE.md) — 공식/내부 일정·타임존.
- [RISKS.md](RISKS.md) — 차단/승인/위험 목록.
- [REQUIREMENTS.md](REQUIREMENTS.md) — 확정 범위와 제출 요건.
- [AGENTS.md](AGENTS.md) — 행동 및 권한/보안 규칙.
- [docs/CONTINUITY_PROTOCOL.md](docs/CONTINUITY_PROTOCOL.md) — **매 주요 작업 종료 시 갱신 순서와 완료 기준**.
- [docs/REPORT_PROTOCOL.md](docs/REPORT_PROTOCOL.md) — 각 대회 총괄 보고 필수 항목.
- [docs/research/PAYPAL_OFFICIAL_REVIEW_20261024.md](docs/research/PAYPAL_OFFICIAL_REVIEW_20261024.md) — PayPal 공식 조사.
- [data/checkpoints.json](data/checkpoints.json) — 기계 판독 스냅샷.

**갱신 트리거:** 참가/제출 상태, 주제·승인, 대회 총괄 보고, 주요 개발/테스트/배포, 차단/오류 해결, 일정/규정 변경, 채팅방 이관. **갱신 범위:** `STATUS`·`HANDOFF`·본 `START_HERE`는 세 문서 내용이 일치하도록 갱신하고, 변경 성격에 따라 `SCHEDULE`·`RISKS`·`projects/*`·`data/checkpoints.json`도 수정. GitHub 원격 커밋·HEAD 재조회 없이 '완료'라고 하지 않는다.

**한계:** 자동 실시간 동기화, 다른 채팅의 진행 상황 실시간 감지, 불참자 대신 Devpost 최종 제출을 자체 실행한다는 가정 **금지**. 실제 새 채팅에서 이 GitHub 주소를 전달해 읽게 하면 된다.

공식 출처: [KIC](https://daker.ai/public/hackathons/kic-ai-agent-competition) · [PayPal Rules](https://paypalaihackathon.devpost.com/rules) · [UGREEN Rules](https://ugreenhackathon.devpost.com/rules)
