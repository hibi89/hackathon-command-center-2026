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
