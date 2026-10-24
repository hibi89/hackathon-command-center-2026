# PayPal AI Hackathon — AI 프리랜서 계약·결제 Agent (잠정)

- 공식 페이지: https://paypalaihackathon.devpost.com/
- 공식 일정: https://paypalaihackathon.devpost.com/details/dates
- 참가: **Devpost 참가 등록 완료로 판단(2026-10-24 KST)** — Register 이후 대회 내 `My hackathon projects` 화면과 `Create project` 버튼 스크린샷 확인. 참가 확인 메일 및 서버 기록은 별도 미검증.
- 전담 GitHub: 미생성(연결 계정 조회 시점)
- 대회 총괄: AI 역할 운영 예정, 개발 착수 미확인

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
