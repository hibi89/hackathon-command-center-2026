# 해커톤 통합 총괄 — 새 채팅 한 줄로 이어가기

**고정 호출 문구:** `[해커톤총괄 깃헙 레포지토리 확인하고 작업하셈]`

**원격 진입점:** https://github.com/hibi89/hackathon-command-center-2026/blob/main/CHAT_BOOTSTRAP.md  
**저장소:** `hibi89/hackathon-command-center-2026` · **브랜치:** `main`

## 호출 시 즉시 수행
1. GitHub 연결을 이용해 본 저장소의 **원격 최신 `main` HEAD SHA**를 조회하고 본 문서 → `START_HERE.md` → `HANDOFF.md` → `STATUS.md` → `docs/FOUR_CHAT_EXECUTION_PROTOCOL.md` → `SCHEDULE.md` → `RISKS.md` → `data/checkpoints.json` 순서로 복원한다.
2. 사용자가 해당 채팅의 대회(KIC/PayPal/UGREEN)를 명시했거나 이전 확정 역할이 있으면 **그 대회 총괄 겸 개발자**로 실행한다. 대회 지정이 없는 새 채팅에 **이 문구만** 있다면 통합 총괄로 시작한다. 동일한 글자만으로 신규 채팅이 어느 대회의 총괄인지를 구별하는 것은 불가능하므로 임의 대회로 코드를 수정하지 않는다.
3. 세 대회 `lead/*`의 원격 HEAD 및 `TO_HACKATHON_LEAD.md`와 `LEAD_ACTIVE_WORK.md`를 확인한다. 대회 총괄이라면 자기 저장소의 `lead/*/CHAT_BOOTSTRAP.md`를 읽고 현재 작업을 **직접 개발·테스트·검수·커밋**한다. 통합 총괄이라면 일정·차단·제출·개발 증거 검수 및 상황실 동기화를 실제 수행한다.
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
