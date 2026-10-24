> **상위 감독 감사 필수 (2026-10-24):** [수뇌부 헌장](SUPERVISOR_MANDATE.md)을 우선 적용한다. 보고 취합만으로 끝내지 않고 **실제 구현과 목표의 적합성, 누락된 필수 작업, 중복·낭비, 제출 병목**을 독립 판정하고 `data/supervisor_findings.json`에 시정 작업·담당·증거·재검수 상태를 기록한다. 리드의 자기평가를 그대로 승인하지 않는다.

# 대회 총괄 → 전체 총괄 보고 규약

세 대회는 실제 참가자 1명과 별개 AI 역할로 운영한다. 각 대회 총괄은 자기 저장소의 최신 STATUS/HANDOFF 및 검증 근거를 관리한다. 전체 총괄은 읽고 이 통합 관리 저장소를 업데이트한다. 채팅방 간 자동 전달을 가정하지 않는다.

## 보고 필수 항목
1. 확인 시각(KST), 대회명, 담당 총괄 브랜치
2. 저장소 URL, 브랜치, 원격 HEAD SHA
3. 참가 등록, 공식 제출, 본선/수상 증거
4. 세 기능의 구현·미구현·미검증 상태
5. 테스트 명령, PASS/FAIL 수, CI 실행 링크
6. 데모/Production URL과 브라우저·API 검증 범위
7. 공식 마감(KST), 남은 제출물과 우선순위
8. 장애 원인·시도/실패 근거·대안·결정 요청
9. 비용·권한·보안·범위 변경 등 승인 항목
10. 보고서 작성시각, 기준 커밋, 다음 작업

## 통합 총괄 책임
변경 대상: README.md, STATUS.md, SCHEDULE.md, RISKS.md, projects/*.md, HANDOFF.md, data/checkpoints.json.
각 대회 실제 코드와 기능별 브랜치는 대회 총괄이 담당한다.

## 근거 우선순위
공식 제출 증거·실행 결과 → 원격 SHA 및 CI → 대회별 최신 HANDOFF/STATUS → 과거 채팅 설명.
서로 다르면 확인한 사실과 미확인 사항을 구분한다. 새 자료를 확인하지 않은 날짜에 자동 최신이라고 주장하지 않는다.

## KIC 전용 확정 라우팅 (2026-10-24 KST)
- 수신 브랜치: `hibi89/hibi89-kic-proofinvest` → `lead/kic`.
- 전체 총괄이 가장 먼저 읽을 KIC 단일 보고 진입점: [`docs/roles/lead/TO_HACKATHON_LEAD.md`](https://github.com/hibi89/hibi89-kic-proofinvest/blob/lead/kic/docs/roles/lead/TO_HACKATHON_LEAD.md).
- KIC 기능 담당자별 메시지는 `feature/{research,verification,risk}`의 `docs/roles/<role>/TO_KIC_LEAD.md`로 모이며, KIC 총괄만 각 원격 HEAD를 검토해 `lead/kic/docs/roles/lead/MESSAGE_REVIEW.md`에 처리 기록을 남긴다.
- 전체 총괄은 KIC 메시지함을 직접 수정하지 않고 총괄 공식 보고의 상태·차단·일정 위험을 반영한다. 각 대회 보고서는 최신 작성 시각과 원격 SHA를 비교하며 자동 동기화되는 것으로 간주하지 않는다.


## 현행 2026-10-24 KST — 4개 채팅 및 직접 개발 보고
- 각 대회 총괄이 개발자를 겸하므로 **작업자 메시지 중계 단계는 폐지**. 중앙은 대회별 lead 브랜치의 `docs/roles/lead/LEAD_ACTIVE_WORK.md`, `STATUS.md`, `HANDOFF.md`, `TO_HACKATHON_LEAD.md`와 실제 원격 SHA/테스트/공식 제출 증거만 확인.
- 기존 feature 브랜치는 이전 실행 증거이며 새 소스는 lead에서 직접 변경. 테스트 자체 검수·CI 및 Production/제출 여부를 구분하여 기록. 작업자용 과거 디스패처는 현재 실행 지시 아님.

## 2026-10-24 KST — PayPal 매 작업 종료 일차 100%·남은 시간 보고 고정
- 사용자 명시 지시: PayPal 개발 총괄은 매 실제 작업을 마칠 때마다 **그날 계획된 검증 완료 기준을 100%로 보고 진행 X%/100%, 남은 예상 Y시간, 남은 안전 확보 Z시간, 실측/미계측, 미완료·이월·증거**를 보고한다. [정식 규약](https://github.com/hibi89/hibi89-paypal-ai-hackathon/blob/lead/paypal/docs/DAILY_PROGRESS_REPORTING.md) / [PayPal 최신 공식 JSON 원장](https://github.com/hibi89/hibi89-paypal-ai-hackathon/blob/lead/paypal/data/paypal_daily_progress.json).
- **원장 현재 기록:** PPL-D01 100%/100%, 남은 예상 0h/안전 0h (quote API 오프라인 부분만 완료); 현재 활성 **PPL-D02 0%/100%, 남은 예상 5h/안전 9h** (영속 DB·CAS·중복 점유/재시작 검증 미착수). 실측 시간 NOT_MEASURED. **전체 3기능/Devpost 완성률을 뜻하지 않는다.**
- 진행률은 증거가 검증된 체크 항목 가중치 합계이며 실제 시간 소모로 증가하지 않는다. 블로커나 예상시간 초과 때 남은 시간과 이월을 재산정하고 과소견적 하지 않는다. 최근 PayPal 정책/테스트 커밋 `b0557a82a6f9a552e5749b0c41bd8d0074cae4dc`; GitHub Actions run 40064258097의 완료 여부는 확인 후 별도 판정. 이전 오프라인 34개 회귀 테스트 CI 성공은 검증됨.
- 상위 총괄은 [PayPal LEAD_ACTIVE_WORK](https://github.com/hibi89/hibi89-paypal-ai-hackathon/blob/lead/paypal/docs/roles/lead/LEAD_ACTIVE_WORK.md)와 [상위 공식 보고](https://github.com/hibi89/hibi89-paypal-ai-hackathon/blob/lead/paypal/docs/roles/lead/TO_HACKATHON_LEAD.md)에서 가장 최근의 X%·Y/Z시간·TESTED/NOT_TESTED·원격 SHA를 직접 확인해 상황실 일정/위험을 조정한다. 각 대회 원본 변경 시 자동 동기화되지 않음.
