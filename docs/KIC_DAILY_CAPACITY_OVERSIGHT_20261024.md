# 통합 총괄 열람 — KIC 날짜별 보수적 작업시간과 이월 기준
> 2026-10-24 13:29:50 KST 사용자 명시 요청으로 상황실에 KIC 날짜별 계획의 **공식 열람 경로**를 등록. KIC 원본은 `hibi89/hibi89-kic-proofinvest@lead/kic`에 있고, 이 문서는 감독용 색인이다. 원본 수정 권한/제품 개발은 KIC 총괄이 가진다.

## 검증한 권위 원본
- **[KIC 60일 날짜별 보수적 작업시간표](https://github.com/hibi89/hibi89-kic-proofinvest/blob/lead/kic/docs/roles/lead/DAILY_CAPACITY_PLAN_20261024.md)** — 2026-10-24~12-22 KST, `docs/roles/lead/DAILY_CAPACITY_PLAN_20261024.md`; 확인한 커밋 [`4b285a2`](https://github.com/hibi89/hibi89-kic-proofinvest/commit/4b285a2334fa4c443a8199ed5bf08b115e90f5b0).
- **[KIC 총괄 당일 단일 작업 포인터](https://github.com/hibi89/hibi89-kic-proofinvest/blob/lead/kic/docs/roles/lead/LEAD_ACTIVE_WORK.md)** — 작업 미완료/다음 실행.
- **[KIC 공식 마스터 일정](https://github.com/hibi89/hibi89-kic-proofinvest/blob/lead/kic/docs/roles/lead/KIC_MASTER_SCHEDULE_20261024.md)** — 사용자 승인된 공식/내부 마감.
- **[KIC 상위 총괄 보고](https://github.com/hibi89/hibi89-kic-proofinvest/blob/lead/kic/docs/roles/lead/TO_HACKATHON_LEAD.md)** — CI·현재 상태·차단·사용자 승인 이슈.

## 예선 전 시간 배정 검수
- **10/24~11/12(20일): 기본 예상 25h + 검수/오류 예비 65h = 총 상한 90h**. 대부분 하루 한 핵심 산출물을 기본 1~2h·복구 예비 2~3.5h·상한 3~5h로 배정.
- **11/13~12/03(21일): 기본 17h + 예비 43h = 상한 60h.** 상호평가 의무 및 다른 해커톤 제출 충돌 고려.
- **12/04~12/22(19일, 본선 진출 시에만): 기본 17.5h + 예비 57.5h = 상한 75h.** 12/03 선발 결과·접근 권한/결함에 따라 재산정 필수.
- **11/08 PDF 동결 → 11/10 조기 접수 → 11/11 접수 오류 전용 예비일 → 11/12 10:00 KST 공식 예선 마감**. 그 전에 DAKER 제출권한과 공식 10쪽 이내 PDF 템플릿 확인이 우선.
- **정량 착각 금지**: 90h는 20일 동안 반드시 일할 시간/완료 예측이 아니라 기본 + 실패 대응용 여유의 합. 실제 소요 미계측. 사용자가 과거 4h 예상→8~20h 지연을 겪어 작은 작업 단위·넉넉한 복구 시간을 요청했다.

## 통합 총괄의 매번 실사 절차
1. KIC `lead/kic` 최신 HEAD를 다시 조회. 이 색인의 `4b285a2`는 확인 당시 스냅샷일 뿐 **고정된 최신 SHA가 아니다**. KIC 원본 URL은 브랜치를 가리키므로 다음 수정이 반영된다.
2. 원본 시간표의 **당일 작업·기본 예상·복구 시간·최대 배정·완료 게이트**, 실측 원장과 `LEAD_ACTIVE_WORK`, `STATUS/HANDOFF`를 함께 열람.
3. 실제 계획 대비 초과, 누적 이월, 차단, PDF/DAKER 제출 위험을 검토한다. 같은 장애 2회 또는 일 상한 초과면 다음 날짜로 분할·이월, 기본 예상의 2배 초과면 다음 3일 재산정 여부 확인. 코드나 품질을 몰래 축소해 일정 준수로 표시하지 않는다.
4. 통합 총괄의 `STATUS/HANDOFF/SCHEDULE`에는 **진행 상황/의존성과 일정 충돌만** 기록하고 KIC 원본 일정·작업 코드는 KIC 총괄이 관리한다. 주요 실사 시 새 HEAD와 근거를 갱신하되 형식적인 빈 커밋은 피한다. 사용자 승인 없이 예선 공식 마감·0원 예산/범위 정책을 변경하지 않는다.
5. 실 테스트 성공, 실 API/브라우저 운영, 공식 접수는 각각 별도 근거로 판정한다. 일정표가 게시됐다는 사실은 제품 완성/제출 증거가 아니다.

**자동 실시간 동기화가 아니라 양쪽 채팅이 같은 GitHub 원본을 요청 시 읽는 구조.** 위 원본 문서의 60일치 날짜별 세부 내용은 이곳에 복제하지 않아 오래된 이중 시간표를 만들지 않는다.

## 2026-10-24 13:53:35 KST — KIC 일일 진척률 100% 기준과 잔여시간 상위 총괄 연결
- 사용자 지시: **매 실제 작업 종료 또는 BLOCKED 시점**에 KIC 1일 핵심 목표를 100점 가중 검증 게이트로 평가해 완료율 및 잔여 예상시간을 공개. [현행 KIC 단일 실적판](https://github.com/hibi89/hibi89-kic-proofinvest/blob/lead/kic/docs/roles/lead/DAILY_PROGRESS.md) / [점수 계산·시간 산정 프로토콜](https://github.com/hibi89/hibi89-kic-proofinvest/blob/lead/kic/docs/roles/lead/DAILY_PROGRESS_PROTOCOL.md).
- 현재 근거 스냅샷(2026-10-24): **당일 원 계획(60일 시간표 공시) 100/100=100%, 잔여 0h**, 별도 Research 인수/CI 26 PASS는 **선행 작업**으로 분리. 10/25 DAKER 권한·공식 양식·초안 계획 **0/100=0%**, 남은 기본 **1h + 오류/검수 예비 3h = 초기 최대 4h**. **실제 작업시간 미계측**. 이 수치는 **계획상 잔여 예상**이지 완료 보증/프로젝트 전체 완성률이 아님.
- 사용자에게는 각 작업 종료 시 `오늘 XX%/100% · 남은 순작업 Xh + 오류예비 Yh = 상한 Zh · 미완료/차단 · 실제 투입(또는 미계측) · SHA/CI`를 보고하도록 KIC `LEAD_FULLSTACK_PROTOCOL.md`에 등록. 상위 통합 총괄도 매 번 `lead/kic`의 **실제 최신 HEAD**를 재조회하여 종료 수치의 최신성을 검증한다.
- KIC 커밋 `c4fc1e54a95b71839959fcc7e410d6ccb5621e75`에서 원본 실적판·지침 확인 가능(상황실 스냅샷, 매번 ref 갱신 확인). 별도 worker 채팅 사용하지 않으며 KIC 계획/코드/공식 제출은 본 상황실이 임의 변경하지 않는다.

**감독 우선순위**: 공식 접수·DAKER 팀 전환 미확인, 일일 수치 100%와 프로젝트 완료/예선 통과를 혼동하지 않는다. 실제 투입 미계측은 0시간이 아니다.
