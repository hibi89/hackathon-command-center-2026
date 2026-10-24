# PayPal AI Hackathon 2026 — 공식 대회정보·출품 게이트·자료 링크

> **통합 총괄 상시 참조 / 2026-10-24 KST 공식 페이지 재검증.** 사용자 제공 Devpost 화면 6장과 대회 공식 Rules / FAQs / Resources 및 Devpost 도움말 교차 검증. 이 문서는 공개 대회 규정에 대한 간략 브리프이며 **참가자의 실제 계정·등록·제출·API 실행 성공을 증명하는 문서가 아니다.** 규정 변경 시 반드시 공식 URL 재확인.

## 1. 대회 개요와 일정
- 대회명: **PayPal AI Hackathon — Build what's next with PayPal and AI**.
- 대회 홈페이지: https://paypalaihackathon.devpost.com/
- 공식 규정: https://paypalaihackathon.devpost.com/rules
- 자료: https://paypalaihackathon.devpost.com/resources
- FAQ: https://paypalaihackathon.devpost.com/details/faqs
- 업데이트: https://paypalaihackathon.devpost.com/updates
- 참가/작품 접수: Devpost의 **Join hackathon → Start project / Enter a submission → 작성 → Submit project**. 포트폴리오 기존 작품 불러오기와 신규 출품은 별개.
- 접수 기간: **2026-10-01 09:15 PT부터 2026-11-12 12:00 PST**; 한국 최종 마감 **2026-11-13 05:00 KST**. 팀 내부 목표 **11/11 KST**는 공식 마감이 아님.
- 공식 심사 기간: **2026-12-01 ~ 12-15 (미국 Pacific Time)**. 결과 발표 예정 **2026-12-21경 미국 Pacific Time**. 실제 발표 공지는 추후 공식 확인.
- 상금(공식 규정 §8): Grand Prize **1위 $12,000, 2위 $8,000, 3위 $5,000**. Honorable Mention(혁신성·영향력·데모 등) 각 **$5,000**; Sponsor Prize는 후원사·조건별 별도. **상금·입상·본선 진출 확정 사실 없음.**
- 공식 선발 구조: §6의 **Stage One 적합성 pass/fail → Stage Two 심사**. **별도 '본선 N명' 선발 정원이나 독립 본선 진출 수상 이력으로 자동 전환하는 규칙 없음**.

## 2. 참가 자격과 계정
- 성년 개인·팀·조직 참가 가능, 혼자 참가 가능, 최대 팀원 수 제한 없음(FAQ). 등록·작품 제출은 구별.
- 공식 규정의 제외지역 예시에 **북한** 포함, **대한민국은 명시적 제외 목록에 없음**. 다만 개인별 거주·관련 법률·이해상충 요건과 PayPal Developer 가입 국가 지원 여부는 별도 확인 필요. **참가 자격 승인 확정이라는 뜻이 아님.**
- 무료 PayPal Sandbox 접근은 https://developer.paypal.com/ 에서 확인. 개발자 Dashboard의 **Sandbox REST app + Business(판매자) + Personal(구매자)** 계정/권한을 구분. FAQ에 따르면 국가/전화번호 때문에 가입 불가능하면 대회 PayPal Discord에 문의.
- 상금과 Sponsor Prize 자격은 별도 약관/도구 요건에 영향받을 수 있음. 후원사 AI 도구 사용 자체는 필수 **아님**(어떤 AI 모델/플랫폼도 가능).

## 3. 출품 필수요건 — 완료 증빙 체크
| 공식 필수 게이트 | 실제 해야 할 것 | 2026-10-24 PayPal 담당 상태 |
|---|---|---|
| **실 PayPal + AI** | **무료 PayPal Sandbox 개발자 플랫폼과 실제 작동하는 AI 도구**가 한 제품에서 통합 작동; PayPal 연동이 핵심 | **BLOCKED / NOT_TESTED**: 로컬 mock·API 준비 코드만 |
| 작동하는 앱 | 실제 기능·설명·영상이 일치하며 심사위원이 실행·상호작용 가능 | 오프라인 localhost 합성 데모만 CI 검증 |
| 공개 오픈소스 소스 | 공개 GitHub 등 + 빌드·설치·실행 완전한 안내 + 저장소 루트 **LICENSE**(About 노출 확인) | `lead/paypal`에 MIT LICENSE와 영어 초안 존재, **최종 공개/기본 브랜치/권한 미검증** |
| 배포 또는 로컬 실행 | **외부 호스팅 필수 아님**. 심사위원이 직접 실제 PayPal+AI 실행 가능하도록 가이드 완비 또는 공개 동작 URL | 실 계정·심사 재현 아직 미검증 |
| 영상 | **공개 YouTube 실동작 데모**; 규정 표현은 3분 미만 권고, 심사위원은 3분 이후 시청 의무 없음 | 영어 스토리보드 DRAFT만, **NOT_FILMED** |
| 제출 설명 | 기능과 제품 가치·기술·AI 설명, **영문** 또는 번역 포함, 제3자 저작권·상표 권리 준수 | 영문 초안 존재, 최종 작성/검수 전 |
| 심사 접근 | 무료로 별 제한 없이 심사 종료까지(미국 PT **12/15**) 테스트 가능, 접근이 필요하면 안전한 별도 방법·안내 | 심사 계정/보안·공개 URL/로컬 실제 재현 **NOT_TESTED** |
| 실제 제출 | Devpost 모든 필수 필드 입력 후 **Submit project**, 화면의 **Submitted** 상태/영수증 링크 확인 | **NOT_SUBMITTED** |
- 외부 계정·개발자 권한·API 자격 증명이 필요해도 **공개 저장소·채팅에 Client Secret, 접근 토큰, 구매자 비밀번호, 실제 카드/고객정보 올리지 않음**. 안전한 별도 재현 경로를 설계할 것.
- 정적 프로토타입·모의 PayPal/AI만으로 Stage One을 통과한다고 주장하지 않는다.

## 4. 심사 및 전략적 우선순위
- **Stage One:** 대회 테마와 필수 PayPal API/SDK 사용 적합성 **pass/fail**.
- **Stage Two:** 다섯 항목 **동일 비중**: (1) 기술 구현 (2) 디자인 (3) 영향력 (4) 혁신성/아이디어 (5) 발표/영상.
- 가장 큰 합격 병목은 **실 PayPal Sandbox + 실 AI 결과가 한 워크플로에서 검증되는가**이다. 모의 테스트 개수 또는 Cloudflare 배포 자체가 공식 통합 증빙을 대체하지 않는다.
- 호스팅은 선택이며, 실동작 데모와 심사 재현 가능성 기준으로 0원 로컬/호스팅 선택. 무단 유료 API·Live 결제·공개 배포·최종 Submit 금지.

## 5. 공식 개발 링크/녹화 영상
| 우선 | 자료 | 출처 |
|---|---|---|
| P0 | 공식 규정/Submission requirements | https://paypalaihackathon.devpost.com/rules |
| P0 | 공식 FAQ(팀·국가·Sponsor) | https://paypalaihackathon.devpost.com/details/faqs |
| P0 | Sandbox 시작 가이드(공식 PayPal 개발팀) | https://github.com/paypaldev/getting-started-with-paypal-sandbox |
| P0 | PayPal 개발자 Dashboard | https://developer.paypal.com/dashboard/ |
| P0 | 10월 6일 **Start building with PayPal** 공식 녹화 | https://www.youtube.com/watch?v=FFJfCW9z3Do |
| P1 | 대회 공식 Resources/가이드 통합 | https://paypalaihackathon.devpost.com/resources |
| P1 | PayPal AI Toolkit 코드/에이전트 개발 자료 | https://github.com/paypal/AI-Toolkit |
| P1 | PayPal REST API 공식 소개 | https://developer.paypal.com/api/get-started/ |
| P1 | Postman API 탐색 가이드 | https://developer.paypal.com/api/rest/postman/ |
| P1 | Devpost 새 프로젝트 vs 기존 포트폴리오/제출 상태 | https://help.devpost.com/article/122-how-to-enter-a-submission |

**사용자 스크린샷의 빈 기존 프로젝트 화면:** `Submit an existing project / You haven't added any projects to your portfolio yet`는 **기존 포트폴리오 프로젝트 없음**을 의미한다. 참가 실패가 아니다. 신규 제출은 **Start project**, 마지막 **Submit project** 클릭 후 **Submitted** 상태 확인. Draft ≠ Submitted.

## 6. 통합 총괄이 매번 확인할 사항
1. 프로젝트 리드: https://github.com/hibi89/hibi89-paypal-ai-hackathon/tree/lead/paypal
2. 본문 공식 링크 상세 검증 원본: https://github.com/hibi89/hibi89-paypal-ai-hackathon/blob/lead/paypal/docs/audits/PPL_OFFICIAL_DEVPOST_LINK_AUDIT_20261024.md
3. 리드→수뇌부 답신: https://github.com/hibi89/hibi89-paypal-ai-hackathon/blob/lead/paypal/docs/roles/lead/TO_HACKATHON_LEAD.md
4. 실제 정본 18일 원장: https://github.com/hibi89/hibi89-paypal-ai-hackathon/blob/lead/paypal/data/paypal_daily_progress.json 및 그 **최신 HEAD의 CI**를 따로 확인. 본 문서의 진도는 10/24 스냅샷이다.
5. 이번 검수 기준 담당 HEAD: `dec853b55cd3324a7d1dc98359af424cca948517`; Actions [#40089356119](https://github.com/hibi89/hibi89-paypal-ai-hackathon/actions/runs/40089356119) **259/259 Node + 로컬 Chromium PASS**. **실 PayPal/AI, 영상, Devpost 제출은 전부 미검증/미제출**.
6. 원장 18일: **DONE12 / PARTIAL2 / BLOCKED1 / NOT_STARTED3**. D03 **0% BLOCKED**(실 계정·OAuth·AI), D04 **80% PARTIAL**(실 AI 누락), D15 **20% PARTIAL**(호스팅), D16–18 **0%**. D15 예정 남은 기본 5h·안전 포함 10h, 실투입시간 NOT_MEASURED.
7. **P0 시정**: 실 Sandbox Business/Personal + 실제 OAuth/Order/approval/capture GET 증빙, 진짜 무료 AI 응답과 결합, 무료 심사 재현성. **P1**: 영어 제출 설명·3분 미만 영상·공개 소스/루트 MIT 노출·Devpost Submitted 영수증. **P2**: 추가 합성 D1 확장 및 과거 SHA 정리.
8. 개인 계정 로그인·API 호출·실 결제·유료 구독·비밀키 취급·공식 제출은 **사용자 별도 승인**. 단순 문서 공시나 `ㄱ`은 외부 금융/공개 제출 승인 아님.

## 7. 보존·공시 규칙
- 본 파일은 **중앙 상황실의 공식 대회정보 진입점**으로 계속 유지하고, 최신 공식 Rules가 우선한다. 대회별 리드가 원본 코드·진도·CI를 관리하고, 중앙은 독립 시정·감사한다.
- 새 통합 총괄 채팅에서는 **이 파일을 `CHAT_BOOTSTRAP.md`·`START_HERE.md`에서 먼저 열어 P0 누락/불필요 작업을 판정**한다. 링크 기록만으로 메시지가 자동 전파되거나 리드가 실제 실행하는 것은 아니다.
- 기록일 2026-10-24 KST; 출처: [Rules](https://paypalaihackathon.devpost.com/rules) §1·§3·§4·§6·§8, [FAQ](https://paypalaihackathon.devpost.com/details/faqs), [Resources](https://paypalaihackathon.devpost.com/resources), [Devpost Help](https://help.devpost.com/article/122-how-to-enter-a-submission).
