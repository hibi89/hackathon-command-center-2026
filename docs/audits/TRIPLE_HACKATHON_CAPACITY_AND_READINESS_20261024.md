# 2026 해커톤 3개 교차 부하 및 출품 위험 분석 — 2026-10-24 15:34 KST
> 통합 총괄의 원본 계획/원격 상태 스냅샷. 원래 일정표 18일 합계는 **잔여 작업시간이 아님**. 자동 백그라운드 감시 아님.

## 검증된 원본 HEAD/Actions
- KIC: [HEAD d44151bea0f3](https://github.com/hibi89/hibi89-kic-proofinvest/commit/d44151bea0f36768059a7687f2aaf7397d0d47cb) · [CI 40068991917 success](https://github.com/hibi89/hibi89-kic-proofinvest/actions/runs/40068991917) · 테스트 82건
- PayPal: [HEAD 17b804eb93d2](https://github.com/hibi89/hibi89-paypal-ai-hackathon/commit/17b804eb93d2d36f94a2813b6c002769fdd5b9c2) · [CI 40070199115 success](https://github.com/hibi89/hibi89-paypal-ai-hackathon/actions/runs/40070199115) · 테스트 131건
- UGREEN: [HEAD b4660d1a72c7](https://github.com/hibi89/hibi89-ugreen-nas-hackathon/commit/b4660d1a72c74b1c75f7c53530979929dfd1be04) · [CI 40069333573 success](https://github.com/hibi89/hibi89-ugreen-nas-hackathon/actions/runs/40069333573) · 테스트 116건

| 대회 | 선행 개발 실증 | 다음 READY | 외부 차단 |
|---|---|---|---|
| KIC | 11/01 Risk verified-only 안전 산술·결측·0분모·음수자본 처리 100% (82/82 offline PASS) | 11/03 기획서 PDF 1~4쪽 초안 0%; 기본 1.5h+예비 3.5h(5h) | DAKER 10/25 권한·공식 양식 35% (접근 후 기본 1h+예비 2h), DART 원문 10/30 90% (접근 후 0.5h+1h). 실 OpenDART API/제출 미검증. |
| PayPal | D01·D02·D05·D06·D07 각 오프라인 100%, D04 80%, D03 0%, Node 131 PASS + 실제 로컬 Chromium E2E CI 통과 | D08 계약·납품·검수 인증 서버 API 0%; 기본 4h+안전 확보 8h | D03 PayPal 실제 Sandbox·AI 접근 0% (접근 후 기본 3h+안전 8h), D04 실제 AI 20% 잔여(예상 2h/안전 4h). 실 결제·배포·Devpost 미검증. |
| UGREEN | 10/24 오프라인 산출물 100%, G2/G3b/G3c/G4/G5·G6 Markdown Skill 후보 선행 완료, 합성 116 PASS | 10/25 G1 공식 SDK CLI·Expert Agent·validator 지원 명세 0%; 기본 1.5h+예비 1.5h(3h) | Uliya Tool 내부 명령/등록 Agent·실 NAS·PII 내용 검사·공식 validator 미검증. 공식 Round 1에 실 NAS 시연 자체는 필수가 아님. |

## 10/25~11/11 원래 18일간 계획된 작업시간 교차표
- KIC: `docs/roles/lead/DAILY_CAPACITY_PLAN_20261024.md` (lead/kic)
- PayPal: `docs/DAILY_CAPACITY_PLAN_20261024.md` (lead/paypal)
- UGREEN: `docs/UGREEN_DAILY_EFFORT_PLAN_20261024.md` (lead/ugreen)
- 원본 세 표를 같은 KST 날짜로 합산함. KIC/UGREEN의 보수 확보시간 = 기본 + 별도 예비, PayPal 보수 확보시간 = 일별 안전 확보.

| KST 날짜 | KIC 기본 | PayPal 기본 | UGREEN 기본 | 기본 합계 | 보수 확보 합계 |
|---|---:|---:|---:|---:|---:|
| 10/25 | 1h | 4h | 1.5h | 6.5h | 15h |
| 10/26 | 1.5h | 5h | 1.5h | 8h | 17h |
| 10/27 | 1.5h | 3h | 2h | 6.5h | 16h |
| 10/28 | 1.5h | 4h | 2h | 7.5h | 16h |
| 10/29 | 1.5h | 5h | 2h | 8.5h | 18h |
| 10/30 | 1.5h | 5h | 2h | 8.5h | 17h |
| 10/31 | 1.5h | 4h | 2h | 7.5h | 17h |
| 11/01 | 1.5h | 4h | 2h | 7.5h | 17h |
| 11/02 | 1.5h | 5h | 2h | 8.5h | 17h |
| 11/03 | 1.5h | 3h | 2h | 6.5h | 15h |
| 11/04 | 1.5h | 5h | 2h | 8.5h | 18h |
| 11/05 | 2h | 5h | 2h | 9h | 17h |
| 11/06 | 1.5h | 6h | 2h | 9.5h | 19h |
| 11/07 | 1.5h | 4h | 2h | 7.5h | 19h |
| 11/08 | 1h | 6h | 2h | 9h | 20h |
| 11/09 | 1h | 5h | 1.5h | 7.5h | 17h |
| 11/10 | 1h | 6h | 1h | 8h | 17.5h |
| 11/11 | 0h | 3h | 0.5h | 3.5h | 12h |
| **합계** | — | — | — | **138h** | **304.5h** |

- 원안 일평균 기본 **7.67h**, 보수 확보 **16.92h**. 기본 8h 초과 날짜 **7일**, 보수 확보 12h 초과 날짜 **17일**.
- 원안 기본 최고 **11/06 9.5h**, 보수 확보 최고 **11/08 20h**. 11/10 기본 8h/보수 17.5h; 11/11 기본 3.5h/보수 12h.
- 시나리오: 하루 6h × 18일 = 108h이면 원안 기본에 30h 부족. 하루 8h × 18일 = 144h이면 원안 기본 대비 6h 여유, 보수 확보 대비 160.5h 부족. **사용자의 실제 하루 가용시간이나 일한 시간 측정 아님.**
- **중요**: KIC의 10/26~29·10/31·11/01~02 업무, PayPal D01/D02/D05/D06/D07, UGREEN G2~G6 오프라인 범위 상당수는 **10/24 조기 검증 완료**. 따라서 위 원안 숫자에서 완료분을 빼지 않고 138h를 '남은 작업시간'이라고 부르면 오류다. 반대로 외부 계정/양식/SDK 접근 및 배포·접수 위험이 미산정이므로 남은 새 총합/완료 ETA는 확정할 수 없다.
- 모든 소요 **실측 NOT_MEASURED**, 외부 접근 대기시간 **UNKNOWN**. 안전 확보는 예비 용량이지 반드시 소비할 개발 시간이 아니다.

## 우선순위 / 제출 게이트
1. **KIC P0**: 팀 빌딩 참여 상태라면 팀장의 '팀으로 전환'과 실제 최종 제출권한 확인, **주최 PPTX 공식 원본** 확보. 멈추지 말고 근거 중심 PDF 1~4쪽 초안 선행; 11/06 사실검증, 11/08 동결, **11/10 내부 조기 제출**, 공식 **11/12 10:00 KST**. 접수 후 11/12~19 참가팀 상호평가 최소 투표 조건 재확인.
2. **PayPal P0**: D08 신뢰 가능한 서버측 인증/소유자·검수자 구분과 오류·이력 보호 구현은 READY. **실 Sandbox/무료 AI 접근 D03**은 별도 BLOCKED P0; 오프라인 결제 성공을 실제 PayPal 출품 적합성으로 주장 금지. 11/08 호스팅, 11/09 실 브라우저, 11/10 영상, 11/11 내부 제출, 공식 **11/13 05:00 KST** 유지.
3. **UGREEN P0**: 공식 Kit 내부 문서·정확한 CLI/Expert Agent 계약을 승인된 공식 경로로 확인; 사전 개발한 G6 Markdown Skill 후보는 **정적 초안**으로 유지. Round 1은 실 NAS 실행 증거 요구되지 않지만 **공식 Uliya Skill 표준/지원 도구**는 충족해야 함. 영문 제안 PDF/제한 ZIP 동시 준비. 11/10 조건부 조기 제출, 차단 시 11/14 예비일, 공식 **11/16 16:45 KST**.
4. **통합 정책**: 4채팅/대회 총괄 직접 개발, 선행 순서 유연화·차단 별도 기록·신규 지출 0원·실 개인정보/결제/계정 변경/원본 수정 사전 승인 유지. **실제 접수 영수증** 없는 상태를 제출 완료로 표시하지 않는다.

## 외부 규정 확인 (2026-10-24)
- [KIC 공식](https://daker.ai/public/hackathons/kic-ai-agent-competition): 10쪽 이하 공식 양식 PDF, 팀 빌딩 참여자는 팀 전환·팀장 제출, 11/12 10:00 마감.
- [PayPal Rules](https://paypalaihackathon.devpost.com/rules): 11/12 12:00 PST = 11/13 05:00 KST.
- [UGREEN Rules](https://ugreenhackathon.devpost.com/rules): 11/15 23:45 PST = 11/16 16:45 KST, Round 1 NAS 런타임 증거 불필요.

**다음 통합 점검:** 실제 새 SHA·CI/일일 원장을 다시 읽고, 선행 완료를 중복 계산하지 않고 변동만 반영. 
