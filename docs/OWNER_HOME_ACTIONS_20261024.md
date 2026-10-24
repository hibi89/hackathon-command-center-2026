# 귀가 후 사용자 확인·전달 목록 — 2026-10-24 KST

> **가장 먼저 볼 자료.** 3개 해커톤 통합 총괄이 2026-10-24 KST 원격 저장소/CI/검수 브랜치를 직접 조회해 선정. **지금 모바일에서는 로컬 작업 불필요.** 계정 정보·비밀키·PDF 본문·실고객 자료를 GitHub/채팅에 보내지 않음. 스크린샷은 이름·이메일·전화번호·계정번호·토큰·경로를 가린 후 **상태만** 전달. 이 문서는 본인만 가능한 확인의 메모이며 실행/승인/공식 제출 영수증이 아님.

## 0. 귀가하면 처리할 순서 (꼭 필요한 것만)

| 우선 | 대회 | 본인이 집에서 확인하거나 건넬 것 | 전달 방식/완료 기준 | 하지 말 것 |
|---|---|---|---|---|
| **1 / P0** | **KIC** | [DAKER KIC 페이지](https://daker.ai/public/hackathons/kic-ai-agent-competition)에 **본인 로그인**. (a) 참가 완료/1인 팀 여부, (b) 휴대폰 본인확인 필요 여부, (c) **최종 예선 단일 PDF 업로드·제출 화면에서 참가자/팀장 제출권한과 버튼 활성상태**, (d) 허용 형식·쪽수·마감 표시 확인 | **최종 제출 버튼을 누르기 전** 상태만 말해주거나 민감정보 가린 화면 제공. 작전실 '해커톤 동기화' 등 기존 출품 데이터 덮어쓰기 기능을 누르지 말 것. 정식 제출은 별도 승인. PDF는 [Private Library 동결 후보](https://github.com/hibi89/hibi89-kic-proofinvest/blob/lead/kic/docs/KIC_FROZEN_PDF_SUBMISSION_PREFLIGHT_20261024.md) 기록상 이미 별도 보관; 같은 PDF를 반복 업로드할 필요 없음 | SMS/OTP·쿠키·비밀번호 전달, 팀전환·임의 공개·제출 클릭 금지 |
| **2 / P0** | **PayPal** | [PayPal Developer Dashboard](https://developer.paypal.com/dashboard/)에 본인 로그인. **Sandbox REST 앱 존재 여부**와 [Sandbox Accounts](https://developer.paypal.com/sandbox-testing/accounts)의 **Business 판매자 + Personal 구매자** 계정이 있는지만 확인. 계정이 없거나 로그인 불가한지도 상태 보고 | 예: `Sandbox 앱 있음/없음, Business 있음/없음, Personal 있음/없음, API 키 접근 가능 여부(값 불필요)`. 가린 화면 선택; 키·ID도 전송 불필요. 계정 개설/권한 변경은 본인이 별도 판단 | Client Secret, 토큰, 계정 이메일·구매자 비밀번호 등 복사·전달 금지. Live/실결제 금지 |
| **3 / P0** | **PayPal AI** | [Google AI Studio](https://aistudio.google.com/)의 본인 프로젝트에서 **실제로 사용 가능한 무료 모델·Free Tier 제공 여부 및 결제연동 상태**를 눈으로 확인. Gemini API Key가 존재하는지만 파악 | `무료 호출 가능 여부 / 모델 이름 / 청구·유료 활성화 여부 / 키 존재 여부`만 전달. **무료 실호출 1회**를 허용할지는 한도·데이터 흐름/요청 내용을 본 뒤 별도 승인. 미지원·불확실하면 차단 유지 | 키 자체 전송·유료 청구 연결·실고객 프로젝트 입력 금지 |
| **4 / P1** | **UGREEN** | 기존 생성 ZIP **재제공 불필요**. [공식 Creator 기반 수정본 리뷰 브랜치](https://github.com/hibi89/hibi89-ugreen-nas-hackathon/tree/review/ugreen-official-creator)에 이미 P1 보완 커밋 `7af2cb7`, [변경 보고](https://github.com/hibi89/hibi89-ugreen-nas-hackathon/blob/review/ugreen-official-creator/docs/submission/G20_P1_CHANGE_REPORT.md) 및 `static-pass 0/0/0` 체크 JSON 있음. **UGREEN 리드가 검수 후 제출 ZIP/PDF를 새로 만들면** 최종 내용·AI/제3자 사용 고지·제출 트랙 등을 직접 확인하고 정확한 산출물에 대해 명시 승인할 준비 | 귀가 즉시 필요한 파일 재업로드 **0건**. 집에서 UGREEN 설치나 NAS 구매할 필요 없음(예선). 리드가 리뷰 SHA/권리/ZIP/PDF를 확인한 뒤 정확한 제출 후보 최종 승인만 요청 | 옛 4-Markdown 초안 ZIP 또는 3파일 검수용 ZIP을 Devpost에 그대로 제출하거나 무단 SkillHub 업로드하지 말 것 |
| **5 / P1** | **제출 단계 (추후)** | PayPal Devpost **영문 설명·공개 GitHub LICENSE·실동작 YouTube <3분·재현 접근**, UGREEN 영문 10문항 PDF/Skill-only ZIP, KIC 동결 10쪽 PDF·DAKER 제출/상호평가를 단계별로 확인 | 실제 공식 `Submitted` 상태/영수증 확보 후에만 접수 완료로 기록. 각 최종 제출은 개별 명시 승인받아 진행 | 오늘 계정 확인만으로 제출 완료 처리 금지 |

## 1. 집에서 읽을 가치가 높은 공식 자료 (선택)

긴 설명을 모두 읽을 필요는 없으며, 각 대회에서 본인이 승인해야 할 정확한 부분만 확인한다.

- **KIC:** [DAKER 대회/제출화면](https://daker.ai/public/hackathons/kic-ai-agent-competition), [동결 PDF 사전검사와 제출 안내](https://github.com/hibi89/hibi89-kic-proofinvest/blob/lead/kic/docs/KIC_FROZEN_PDF_SUBMISSION_PREFLIGHT_20261024.md). DAKER 공식 마감 **11/12 10:00 KST**; 내부 목표 11/10. 제출 이후 **11/12~19 상호평가 참여**가 예정되어 있으므로 별도 확인.
- **PayPal:** [Rules](https://paypalaihackathon.devpost.com/rules), [공식 FAQ](https://paypalaihackathon.devpost.com/details/faqs), [Devpost 링크 검수](https://github.com/hibi89/hibi89-paypal-ai-hackathon/blob/lead/paypal/docs/audits/PPL_OFFICIAL_DEVPOST_LINK_AUDIT_20261024.md), [실계정 한 번만 검증 가이드](https://github.com/hibi89/hibi89-paypal-ai-hackathon/blob/lead/paypal/docs/technical/PPL_P0_OWNER_ONE_SHOT_REAL_API_PROBE_20261024.md). 마감 **11/13 05:00 KST**. 무료 로컬 데모는 허용 가능하나 **실 PayPal+실 AI 없이 모의 데모로 제출하면 적격성 위험**.
- **UGREEN:** [Rules](https://ugreenhackathon.devpost.com/rules), [Official Starter Kit](https://ai.ugreen.com/pages/hackathon-starter-kit), [P1 수정내역](https://github.com/hibi89/hibi89-ugreen-nas-hackathon/blob/review/ugreen-official-creator/docs/submission/G20_P1_CHANGE_REPORT.md). Round1 **11/16 16:45 KST**. **본선 진출 전 실 NAS나 NAS 영상 필요 없음**.

## 2. 이미 있는 자료 — 다시 요청하지 않음

- KIC 비공개 후보 PDF/PPTX는 과거 Private Library에 6개 보관됨(수정 전 크기·SHA 확인; 접근 불가면 사용자에게 반복 제출 요청하기 전에 저장 위치 확인). 단일 동결 PDF 후보 513,113B SHA-256 `0bdbbf04f374a7ccb39cd15e1aa700a006514278b094d32bb05ac7db610e034e`는 **원장상 검수된 값**, 10/24 새 로컬 프리플라이트 미실행.
- UGREEN 사용자가 업로드한 `ProjectReady_OFFICIAL_REVIEW.zip`은 [G20 원본 비교 검수](https://github.com/hibi89/hibi89-ugreen-nas-hackathon/blob/lead/ugreen/docs/submission/G20_UPLOADED_REVIEW_ZIP_INDEPENDENT_AUDIT_20261024.md) 완료. 새 수정본은 이미 [리뷰 브랜치 `7af2cb7`](https://github.com/hibi89/hibi89-ugreen-nas-hackathon/tree/review/ugreen-official-creator)에 존재하며 **이번 검사에서 HEAD 확인됨**. `lead/ugreen`에 아직 승격되지 않았고 최종 PDF/ZIP·실 Agent/권리/최종 승인 미완료.
- PayPal 소스에는 단발 실 API 탐침 스크립트와 영속 AI 예약 잠금이 존재하지만, 실 개인 계정/무료 모델/실 Provider 사용 기록은 **아직 없음**. 위 계정 상태 확인이 반복 모의 코딩보다 우선.

## 3. 총괄이 집에서 받은 보고로 수행할 후속 조치

1. **KIC:** 제출권한이 보이면 업로드 가능한 실제 화면을 정본 PDF 해시와 대조하고, 최종 제출과 상호평가 일정을 별도 승인·영수증으로 관리. 안 되면 인증/권한·지원 경로만 정리하고 BLOCKED 유지.
2. **PayPal:** Business/Personal Sandbox와 Gemini Free Tier 모두 가능할 때에만 추가 승인 요청 → 비밀값은 소유자 비공개 환경에 둔 채 합성 데이터로 범위 제한한 **실 API 일회성 검증**, 이후 실제 Orders/승인/GET/Capture 통합과 영상·심사 접근 검증. 무료 정책/국가 지원이 불가하면 실패 사유 보존하고 공식 FAQ 지원 경로 검토.
3. **UGREEN:** `review/ugreen-official-creator@7af2cb7`을 `lead/ugreen`에 **임의 병합하지 않고** 리드가 새 Skill 코드·정적 결과를 읽어 검수, 원본 복구 보장 후 승인된 후보로 새 영문 PDF Q8/ZIP·권리 표시·SHA/CI를 다시 검사; 참가자 최종 확인 후 Devpost 제출.
4. **세 대회 모두:** 로그인/가입·실 API·승인·정식 제출은 사용자 명시적 허락이 없으면 진행하지 않음. 실제 증거는 각각의 대회 리드 브랜치에 남기고 수뇌부가 재검증.

**현재 제출 영수증:** KIC 0 / PayPal 0 / UGREEN 0 (GitHub/대화에서 확인된 범위; 사용자의 비공개 Devpost 변경은 조회하지 않음).
