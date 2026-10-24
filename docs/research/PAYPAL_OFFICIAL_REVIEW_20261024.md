# PayPal AI Hackathon — 공식 규정·기술·제출 검증 보고서
> 조사 시점: 2026-10-24 KST | 전체 총괄 작성 | **기술 구현 및 실계정 접속은 실시하지 않음** | 주제 미확정

## 1. 공식 자료
- Overview: https://paypalaihackathon.devpost.com/
- Official Rules (충돌 시 우선): https://paypalaihackathon.devpost.com/rules
- Resources: https://paypalaihackathon.devpost.com/resources
- FAQs: https://paypalaihackathon.devpost.com/details/faqs
- Schedule: https://paypalaihackathon.devpost.com/details/dates
- Updates: https://paypalaihackathon.devpost.com/updates
- PayPal 공식 Sandbox 안내: https://github.com/paypaldev/getting-started-with-paypal-sandbox

## 2. 참가 및 일정
- 1인 참가 허용. 대한민국은 규정에서 명시된 제외 국가에 포함되지 않으나 개인별 자격은 공식 규정 충족을 전제로 한다.
- 사용자가 Devpost 참가 신청을 마치고 `My hackathon projects` 화면을 제공함. 작품 생성 및 최종 제출은 **아직 미완료**.
- 제출: **2026-11-13 05:00 KST**, Devpost 현지 **2026-11-12 12:00 PST**.
- 일정표상 심사: 2026-12-02 07:00 ~ 12-16 01:00 KST, 결과 발표 2026-12-22 02:00 KST 예정. 상세 공식 Rules와 Schedule에 결과 발표 시각 차이가 존재하므로 정확한 발표 시각은 추후 재확인.
- 참가 무료. PayPal Sandbox 무료. 개인의 PayPal Developer 계정 생성·API 사용 가능 여부는 **실계정으로 미확인**; 국가·전화번호 사유로 회원가입이 불가하면 FAQ에 따라 공식 Discord 문의.

## 3. 핵심 개발·제출 조건 (필수)
1. PayPal 개발 플랫폼과 AI 모델·도구를 **모두 실질적으로 사용**하는 앱/Agent. PayPal은 중심적인 역할이어야 함. 임의의 후원사 도구는 선택.
2. 실질적으로 작동하는 데모. 심사위원이 재현 가능한 설치·실행 지침 또는 호스팅 데모 URL 중 하나. 정적 시안·동작하지 않는 화면 불인정.
3. 영어 텍스트 설명(또는 영문 번역), 사용 AI 도구·역할·핵심 흐름 설명.
4. 공개 오픈소스 GitHub/GitLab/Bitbucket 저장소 및 첫 화면에 인식 가능한 LICENSE, 전부 실행에 필요한 소스·자산·재현 지침.
5. **3분 미만**, 실제 작동 과정을 보이는 **공개 YouTube** 영상 링크. 저작권/상표 자료 권리 확인.
6. 기존 프로젝트를 재사용할 경우 대회기간(2026-10-01 이후) **유의미한 새 구현**을 입증.
7. 모든 제출물 영어 또는 번역 제공, 제3자 API/라이선스·개인정보·지식재산권 준수.
8. 무료로 심사 기간 동안 재현 가능한 상태 유지. API 키·Sandbox Secret·테스트 비밀번호를 Public GitHub에 직접 올리지 않음; 데모 접근은 보안 승인된 별도 방법/가이드 사용.

## 4. 심사 방식
- **Stage One**: 테마 적합성·필수 API/SDK의 합리적 사용 여부 pass/fail.
- **Stage Two**: (동일 비중) **기술 구현, 디자인/완성도, 잠재적 영향, 혁신성, 발표**.
- 이 Stage One/Two는 **심사 내부 단계**이며 KIC/UGREEN처럼 분리된 예선/본선 제출 일정은 아님.
- 특별상으로 Most Creative, Most Impactful, Best Demo Delivery, Best Use of PayPal + AI, Best Use of Agentic Commerce 등이 있음.
- 현금 상금 총액은 공식 사이트의 개요/배너에 표기 불일치($67,500 cash/$67,500+ prizes vs 소개문 $69,750)가 있어 시점별 공고 재확인; 전략 결정에 사용하지 않음.

## 5. 실제 API/운영을 위한 사전 검증 (미실행)
- Sandbox 무료 구매자(Personal)·판매자(Business) 계정, 테스트 Client ID·Secret 생성 가능 여부.
- 가능하면 Orders v2의 `create -> buyer approve -> capture` 흐름과 중복·거부 처리 확인. 실제 결제/Live 자격증명 사용하지 않음.
- PayPal Checkout / Orders / Invoicing / Subscriptions / Webhooks의 계정·국가·API 지원 범위 각각 분리 검토.
- PayPal AI Toolkit / Agent Toolkit / MCP 문서 제공 확인. 설치 가능성 및 실제 작동은 검증 전.
- 인증 비밀은 서버 환경변수/비공개 설정, 공개 커밋 금지. 사용자 동의 없는 결제 실행 금지.

## 6. 잠정 제품 설계 2안 비교 (아직 확정·개발 착수 아님)
| 평가 | A: 세 기능 동시 완성 | B: 단일 결제 코어 우선, 단계 확장 |
|---|---|---|
| 흐름 | 견적/결제 + 납품 단계 + 구독 실패를 병렬 구현 | 견적 AI -> 고객 승인 -> Sandbox 주문/결제 -> 상태 표시를 실제 끝까지 검증. 납품·구독은 독립 확장 |
| 구현 속도 | 느림, 3개 API 계약·UI/상태 통합 부담 | 빠름, 한 개의 일관된 작동 흐름 |
| 외부 API/안전 | Invoicing/Orders/Subscriptions/Webhooks 조합 복잡 | Orders/Sandbox 중심, 검증 가능성 높음 |
| 심사 기준 적합성 | 기능 수 많아도 미완성 시 감점 위험 | End-to-end 기술/디자인/영상 증명 용이 |
| 장기 상품성 | 넓은 기능, 유지보수 부담 큼 | 제품화 시 모듈식 확장 가능 |

**전체 총괄 제안:** 기한 및 유효 제출 위험을 고려하면 **B를 우선 검증하고 A의 3기능 최종 비전은 유지**한다. 단, 이는 전체 총괄의 *비교 의견*일 뿐 주제·범위 변경 승인 아님. PayPal 전담 총괄이 API 실현성/기술 선택/보안·비용을 분석한 뒤 사용자에게 대안과 승인 요청.

## 7. 전체 총괄의 다음 점검
- PayPal 담당 총괄과 기능별 작업 브랜치 아직 없음; 기존 KIC 저장소는 변경하지 않음.
- 참가 완료 / Devpost 프로젝트 미생성 / SDK 실검증 미완료 / 구현 0 / 영상 미완료 / **공식 최종 제출 미완료**.
- 우선순위: 담당 총괄 지정 -> PayPal Developer Sandbox 로그인·계정 가능 여부 -> 제품 2안 검수/승인 -> 하나의 결제 코어 구현/실검증 -> 공개 저장소/LiCENSE/영상/Devpost 제출.
- 실제 DEVPOST 프로젝트 생성·공개·범위 변경/Live 결제 실행은 사용자 의사결정 및 별도 확인.

상태 변경은 각 대회 총괄의 원격 보고가 생기면 그 문서와 GitHub SHA·CI·실제 데모 증거를 대조하여 갱신한다. 본 문서는 2026-10-24의 조사 스냅샷이며 자동 갱신되지 않는다.
