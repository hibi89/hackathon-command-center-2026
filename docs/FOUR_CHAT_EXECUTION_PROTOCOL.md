# 현행 운영 — 4개 AI 채팅, 총괄이 직접 개발

> **2026-10-24 KST 사용자가 최종 확정.** 기존 7개 채팅(총괄+별도 작업자)과 13개 역할별 별도 채팅 구조는 폐기한다. 원본 기능 브랜치/기존 코드/작업 이력은 보존.

## 1. AI 채팅은 단 네 개
- 통합 총괄: `hibi89/hackathon-command-center-2026@main`. 세 대회의 일정·품질·비용·위험·공식 제출 증거를 감독하며 대회 코드는 수정하지 않음.
- KIC 총괄 겸 직접 개발자: `hibi89/hibi89-kic-proofinvest@lead/kic`. Research/Verification/Risk 기능 구현·테스트·커밋·자체 검수·통합·제출 준비.
- PayPal 총괄 겸 직접 개발자: `hibi89/hibi89-paypal-ai-hackathon@lead/paypal`. quote-payment/delivery/subscriptions 구현·테스트·커밋·자체 검수·통합·제출 준비.
- UGREEN 총괄 겸 직접 개발자: `hibi89/hibi89-ugreen-nas-hackathon@lead/ugreen`. missing-files/version-conflicts/privacy 개발·테스트·커밋·자체 검수·통합·제출 준비.

**3개 대회는 동시 진행한다. 대회 안에서는 한 채팅이 직접 우선순위별 일을 수행한다.** 추가 기능별 AI 채팅도, 순환 작업자 채팅도, 채팅 간 작업 의뢰/인수도 없다.

## 2. 각 대회 총괄의 실행 절차
1. 매 작업 시작 시 `lead/*` 최신 원격 HEAD 및 HANDOFF/STATUS/AGENTS/REQUIREMENTS/실제 소스·테스트를 읽는다. 과거 단일 작업자용 NEXT_TASK/ACTIVE_TASK/CURRENT_TASK는 미완료 작업·중복 방지의 **이력/참고**로 조회하되 별도 작업자 채팅 호출을 요구하지 않는다.
2. 현재 feature의 기존 코드/커밋/테스트/TO_*_LEAD 보고를 확인해 이미 완성한 작업·검수 대기 작업을 중복 실행하지 않는다. READY/IN_PROGRESS/검수 대기와 BLOCKED를 현재 실상에 맞게 정리한다.
3. 해당 대회 총괄이 **기존 적절한 feature 브랜치**에서 직접 코드/테스트·검증/커밋을 실행한다. 코드 삭제·강제 덮어쓰기·임의 force push 금지. 역할 간 계약·합성/실 API·실배포 구분. 기능 변경 뒤 같은 feature의 STATUS/HANDOFF/테스트 증거를 정리한다.
4. 본인 `lead/*`에 최신 지시/결정/통합 검수/STATUS/HANDOFF 및 `docs/roles/lead/TO_HACKATHON_LEAD.md`를 갱신하고, 필요시 PR·CI·병합 증거를 남긴다. GitHub Author/Committer와 원격 HEAD, Production SHA를 구분 검증한다.
5. 사용자 `ㄱ` = **현재 승인된 다음 실제 작업 실행**. 계획서만 작성하거나 다른 작업자 채팅으로 넘기지 않는다. 마감·품질·비용 조건을 임의 축소·변경하지 않는다.

## 3. 과거 파일과 새 채팅
- [현행 4채팅 프롬프트](CHAT_TRANSITION_PROMPTS_4.md)만 새로운 채팅 재개에 사용. 과거 7채팅 프롬프트/13채팅 프롬프트 및 역할 메시지함·디스패치 파일은 **감사/인수인계 이력**이므로 삭제하지 않는다.
- 세 대회의 `lead/*` 문서 정비는 각 총괄 책임. **상황실에 이 정책을 커밋한 사실 = 각 대회 전환 성공이 아니다.** 리드 저장소 최신 HEAD/보고/기능 실행 증거를 직접 읽은 다음 완료 판정한다.
- KIC 내부 11/10(공식 11/12 10:00 KST), PayPal 내부 11/11(공식 11/13 05:00), UGREEN 내부 11/10(공식 11/16 16:45) 목표 유지. 신규 현금 지출 0원·계정 권한/실 API/외부 데이터 전송/원본 변경은 기존 사용자 사전 승인 정책 준수.
- 공개 GitHub에 비밀, `.env`, 개인정보, 제출 원본 무단 공개 금지. GitHub 문서 변경만으로 자동 채팅 실행·CI 성공·API/서비스·공식 제출을 주장하지 않는다.

## 4. 완료 검증 게이트
- 세 대회 리드의 HANDOFF·STATUS·실행 지시가 '총괄 직접 개발' 체제로 **실제로 원격 반영**됐는지.
- 기존 진행/검수 대기 과제의 커밋·기능·테스트·실 API 결과를 총괄이 직접 인수했는지.
- 총괄 혼자 feature 구현→테스트→커밋→자체 검수→다음 작업까지 최소 한 사이클 확인.
- 공식 제출/실배포는 별도 화면·로그·영수증으로 검증.
