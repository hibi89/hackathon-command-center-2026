# PayPal — 통합 해커톤 총괄의 일별 작업시간 감독 기준 (2026-10-24)

**정본은 PayPal 총괄 `lead/paypal`의 [18일 날짜별 실행계획](https://github.com/hibi89/hibi89-paypal-ai-hackathon/blob/lead/paypal/docs/DAILY_CAPACITY_PLAN_20261024.md)**. 이 상황실 문서는 원본 18개 행을 복제하지 않는다. 상위 총괄이 사용자의 요구대로 같은 GitHub 시간표를 보고 일정 충돌·실현 가능성을 검수하기 위한 진입점이다.

## 확인한 근거 (2026-10-24 KST)
- PayPal 본 저장소: `hibi89/hibi89-paypal-ai-hackathon`, 브랜치 `lead/paypal`, 직접 확인한 기준 원격 HEAD `fe74448a419d75d622db4b8c1a9a5a2e6d75a36e`. 이후 **새 원격 SHA 재조회 필수**.
- 2026-10-25~11-11 (18일) 예상 **82시간**, 지연/오류/재시도 포함 안전 확보시간 **164시간**. 하루 평균 PayPal만 **9.1시간** 필요. 10/24에 완료된 PPL-001 코드 이관 및 합성 테스트 작업은 기간 견적에 중복 산입하지 않는다.
- 매일 4시간 PayPal 가용이면 72시간(순작업 대비 10h 부족, 안전 확보 대비 92h 부족), 6시간이면 108시간(안전 확보 대비 56h 부족). **세 대회를 병행하면서 '하루 목표 완료가 널널하고 안전'하다고 판단할 증거는 없다**. 상태 **HIGH RISK**.
- CI [PayPal 40061919949](https://github.com/hibi89/hibi89-paypal-ai-hackathon/actions/runs/40061919949) success는 오프라인 Node 순수 계약 테스트. 실 Sandbox OAuth/Orders·AI API/호스팅·Browser E2E/Devpost 제출을 입증하지 않는다.

## 통합 총괄이 매 점검에서 할 일
1. `lead/paypal` 최신 HEAD와 [원본 시간표](https://github.com/hibi89/hibi89-paypal-ai-hackathon/blob/lead/paypal/docs/DAILY_CAPACITY_PLAN_20261024.md)의 오늘 날짜·목표 1개·예상/안전시간·완료 증거·실측/이월을 직접 확인한다.
2. [PayPal 총괄 최신 보고](https://github.com/hibi89/hibi89-paypal-ai-hackathon/blob/lead/paypal/docs/roles/lead/TO_HACKATHON_LEAD.md) 및 `STATUS.md`, `HANDOFF.md`, `docs/roles/lead/LEAD_ACTIVE_WORK.md`와 실제 코드/CI를 대조. 숫자·기간·게이트가 바뀌었으면 상황실에 출처·새 SHA와 함께 갱신한다.
3. KIC 11/12 10:00과 PayPal 11/13 05:00 공식 제출 간 **19시간 충돌**, PayPal 내부 11/11 목표 및 UGREEN 11/16 16:45까지 고려해 리소스 충돌 평가. 예비시간을 대회 간 중복으로 확보했다고 가정하지 않는다.
4. 하루 실제 가용시간이 예상보다 부족하거나 1.5~2배 이상 지연되면 (a) 실제 측정/미측정 분리 (b) 이월 작업·Sandbox/무료 모델 인증 블로커 공개 (c) 남은 날 재배치 (d) 사용자에게 범위/품질/일정 위험과 안전한 대안 제시. **사용자 승인 없이 기능 축소·유료/Live 전환·공식 마감 연장 금지.**
5. 작업 완료는 오프라인/CI, 실 Sandbox, 브라우저, Production, Devpost 제출 영수증을 별개로 판정. 채팅 없이 자동 동기화되는 것이 아니다.

## 운영 분리
- PayPal 총괄은 자기 `lead/paypal` 저장소에서 직접 개발·테스트하고 원본 일별 표를 최신화한다.
- 통합 총괄은 이 상황실 `main`의 일정·위험·링크·인수인계만 갱신한다. 다른 대회 소스·기능 브랜치를 변경하지 않는다.
- 이번 문서는 사용자의 **"GitHub에 등록해서 두 총괄이 같이 보게"**라는 명시적 요청에 따라 연결한 것. 새 코드 개발·PayPal 실제 계정 테스트·Devpost 제출로 보고하지 않는다.
