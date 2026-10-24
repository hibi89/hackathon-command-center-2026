# PayPal AI Hackathon — AI 프리랜서 계약·결제 Agent (잠정)

- 공식 페이지: https://paypalaihackathon.devpost.com/
- 공식 일정: https://paypalaihackathon.devpost.com/details/dates
- 참가: **Devpost 참가 등록 완료로 판단(2026-10-24 KST)** — Register 이후 대회 내 `My hackathon projects` 화면과 `Create project` 버튼 스크린샷 확인. 참가 확인 메일 및 서버 기록은 별도 미검증.
- 전담 GitHub: [`hibi89/hibi89-paypal-ai-hackathon`](https://github.com/hibi89/hibi89-paypal-ai-hackathon) **2026-10-24 생성·5브랜치 운영 파일 직접 검증** (Public).
- 대회 총괄 브랜치: `lead/paypal` 및 [상위 해커톤 총괄 보고서](https://github.com/hibi89/hibi89-paypal-ai-hackathon/blob/lead/paypal/docs/roles/lead/TO_HACKATHON_LEAD.md) 생성. **별도 AI 채팅 역할 아직 배정 전, 코드·실 API·배포 미착수**.

## 잠정 통합 기능
1. 고객 요구 분석 후 견적/작업 범위를 만들고 승인된 PayPal Sandbox 결제로 연결.
2. 해외 프로젝트의 단계·납품·결제 상태 추적.
3. 반복 결제 실패 또는 청구 예외 파악과 해결 안내.

주제는 미확정. 담당 총괄이 PayPal 공식 API/기술 적합성·시간·차별성을 조사하고 2가지 이상 설계안을 비교해 사용자 승인 후 확정한다. 초기 범위는 Sandbox이며 실제 결제는 하지 않는다.

## 제출 요구
- **공식 마감 2026-11-13 05:00 KST** (11/12 12:00 PST).
- AI와 PayPal 기술이 실제 핵심인 작동 가능한 프로그램.
- 공개 오픈소스 저장소와 저장소 루트 라이선스, 설치 및 실행 안내.
- 호스팅된 데모 또는 심사위원이 실행 가능한 명확한 설명.
- 3분 미만의 공개 YouTube 시연 영상(실행 장면).
- AI 개발 방식·사용한 PayPal 기술·제품 소개.

## 진행 체크리스트
- [x] 참가 등록 직후 참가자 화면 확인 (프로젝트 생성·최종 제출과 구분)
- [ ] 주제·실제 API 사용 가능성 검증
- [ ] PayPal Sandbox 최소 결제 흐름
- [ ] 세 기능 중 실제 작동 범위 결정 및 구현
- [ ] 공개 소스·LICENSE·재현 안내
- [ ] 브라우저 검증·안전성 확인
- [ ] 시연 영상·Devpost 제출 영수증

내부 목표: 10/24~26 참가/기술 조사; 10/27~31 Sandbox 최소 흐름; 11/01~05 통합 검증; 11/11~12 최종 제출.
공식 결과는 심사 후 별도 기록한다.

## 2026-10-24 등록 증거
등록 절차 화면 → `Register` 실행 → Devpost PayPal AI Hackathon 내 `My hackathon projects` 페이지 진입. 아직 프로젝트가 없어 `Create project`가 나타남. **참가 등록과 작품 최종 제출은 별개의 단계**. 계정 식별정보/개인정보를 공개 GitHub에 업로드하지 않음.

## 2026-10-24 — 공식 규정/기술 검토 추가
- 전체 총괄이 **Overview, Rules, Resources, FAQs, Schedule, Updates 및 PayPal Sandbox 공식 안내**를 직접 읽어 필수 요건과 미검증 항목을 분리했다.
- [공식 규정·심사·기술·설계 A/B 비교 보고서](../docs/research/PAYPAL_OFFICIAL_REVIEW_20261024.md)를 참조한다. **PayPal + AI 모두 핵심 기능**이어야 하고 Sandbox 실제 흐름 검증이 최우선.
- 심사는 내부 적합성 pass/fail 이후 동일 비중 다섯 기준(기술/디자인/효용/혁신/발표). 별도 본선 참가자 제출일은 없다.
- 기존 3기능 아이템은 **잠정 유지**. 사용자 승인 전 축소/확정하지 않는다. 총괄 권고는 결제 코어를 우선 실제 검증하고 추가 모듈을 순차 구현하는 B안.
- 참가 자체는 확인되었으나 **PayPal Developer 계정 실제 로그인·Sandbox API·Devpost 작품 생성·공개 코드·영상·최종 제출은 미검증/미완료**.
- PayPal은 한국 실계정의 Developer/Sandbox 접근 가능 여부를 사전 확인해야 한다(FAQs는 국가별 가입 불가 가능성을 명시).

## 2026-10-24 KST — 본선 선발 인원 질의 최종 확인
- [PayPal 공식 규정 §6](https://paypalaihackathon.devpost.com/rules)에서 **별도의 공식 본선 진출 정원/발표 규정은 발견되지 않음**.
- `Stage One` 테마/기술 적합성 **pass/fail** → 통과작 대상 `Stage Two`의 5개 동등 비중 심사. 외부 대회처럼 '12팀 본선' 등 숫자가 있는 방식이 아님.
- 현재 목표는 **실제 작동 PayPal + AI 프로그램 완성·공개 코드·영상·Devpost 유효 제출** 후 공식 수상 가능성 확보. 등록/출품/수상 성과는 구분한다.
- PayPal 전담 총괄 저장소·Sandbox 접근 확인은 여전히 시작 전이며 기존 잠정 3기능은 사용자 확정 전이다.

### PayPal — 2026-10-24 GitHub 5개 브랜치 운영 구조 검증
- 저장소: [`hibi89/hibi89-paypal-ai-hackathon`](https://github.com/hibi89/hibi89-paypal-ai-hackathon) (Public); `main` HEAD `d66757b8d73daa3158897db078430c4cc91a3847`, `lead/paypal` HEAD `f921c483b5785bf8a1f9fd70da8cd983599669c3`.
- `feature/quote-payment` HEAD `cafdb0a2b2e497944872adc34fb5bb507b9d1d78`
- `feature/delivery` HEAD `f7336d2746c415938d0325b19798752ba3c4fb4a`
- `feature/subscriptions` HEAD `8ad5897be995e654d95bffef4f2d03e0691cef33`
- 총괄 고정 상위 보고: [`lead/paypal/docs/roles/lead/TO_HACKATHON_LEAD.md`](https://github.com/hibi89/hibi89-paypal-ai-hackathon/blob/lead/paypal/docs/roles/lead/TO_HACKATHON_LEAD.md).
- **검증**: GitHub 5/5 브랜치와 각각 필수 운영·인수인계·메시지 문서 전수 확인. **코드/CI/실 API/배포/최종 제출은 없음.** 제품 주제·기능은 사용자 최종 승인 전 잠정. 대회별 AI 총괄 채팅방은 아직 생성됐다는 증거 없음.

## 2026-10-24 KST — 구조/일정 재검증 반영
- [역할별 공식 일정 공시](https://github.com/hibi89/hibi89-paypal-ai-hackathon/blob/lead/paypal/docs/COMPETITION_SCHEDULE.md) 존재; 5/5 브랜치가 동일한 전체 일정표를 보유하며 README에 링크가 있음.
- 관측 HEAD: `main b58533ac7e632706a95d807de5ced6497b5e46b0`, `lead/paypal 62efc0293af5aef6ddd43480f3349f7dba728646`. 세 feature별 최신 SHA는 [통합 검수 보고서](../docs/audits/REPOSITORY_AUDIT_20261024.md) 참고.
- 주제·참가/기능·실 API·실서비스·최종 제출의 기존 상태 **변경 없음**. 문서 링크·검증 개선만 완료.

## 2026-10-24 — PayPal 총괄 기능별 자체 일정 업데이트
- [lead/paypal 일정 5절](https://github.com/hibi89/hibi89-paypal-ai-hackathon/blob/lead/paypal/docs/COMPETITION_SCHEDULE.md)에 10/24~26 Sandbox 접근·주제/범위 검증, quote-payment 10/27~11/01, delivery 10/29~11/04, subscriptions 10/30~11/05, 통합 11/06~09, 내부 조기 제출 11/11 권고 기록.
- 조회 HEAD `a7fb08d141f40455606816bbc15520a0f925134d`; **사용자 승인 전 일정 초안**, API/코드/Devpost 제출 성공 아님.

## 2026-10-24 KST — 최신 단일 작업자 라우터 확인
- [PayPal v4 실행계획](https://github.com/hibi89/hibi89-paypal-ai-hackathon/blob/lead/paypal/docs/PAYPAL_EXECUTION_PLAN_20261024.md): 신규 현금 지출 0원/3개 기능을 하나의 출품으로 통합/대회 내 1명씩 순차 진행; 내부 11/11 제출 목표. 구형 병렬 계획은 폐기.
- 최초 [PPL-001](https://github.com/hibi89/hibi89-paypal-ai-hackathon/blob/lead/paypal/docs/dispatch/ACTIVE_TASK.md): READY, `feature/quote-payment`; 실제 Sandbox 적합성·설계 A/B·v0 계약 검증이 첫 관문. 후속 feature 임의 착수 금지.
- 세 feature 최신 HEAD: `e5b70e0376628dc9e6237d69234f56648c849ca8`, `77dc5327b69432d3f64a320dea8a1ae0c2f427ce`, `9d77f9029d9dfb571f14f5d10289f97015ba6f4f`. 각각 가장 최근 변경 파일은 `AGENTS.md`이고 PPL-001 실행 보고는 없음. Sandbox/API/제품 코드/실제 제출 미검증.


## [2026-10-24 KST] 4개 채팅 체계 완료 — PAYPAL 총괄 직접 개발
- 별도 기능 작업자 채팅 폐기. `lead/paypal`가 직접 소스 개발·테스트·자체 검수·통합을 담당하며, 유일한 현재 작업 포인터는 `docs/roles/lead/LEAD_ACTIVE_WORK.md`. 기존 feature 브랜치는 작업 증거를 포함해 원본 보존. 이전 작업 지시서의 READY/IN_PROGRESS는 역사 상태이며 신규 실행권 없음.
- 최신 확인 총괄 SHA: `3fc1d9e9ac017d50c73492fb550c30f88c4f7fa2`. PayPal 오프라인 Node 11 PASS는 작업자 보고이며 실제 Sandbox 인증/결제 호출 미검증. 공식 제출 영수증 미확인.
