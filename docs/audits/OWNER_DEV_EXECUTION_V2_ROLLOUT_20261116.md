# OWNER-DEV-EXECUTION-V2 전 저장소/브랜치 적용 감사
2026-11-16 KST | 원장: [79개 반영 커밋/80개 기준 참조](../../data/owner_dev_execution_v2_rollout_20261116.json)

## 소유자 지시와 채택 설계
- 최초 최종설계·작업 큐: **웹 GPT-6 Sol High**, 실제 백엔드/프론트엔드 주력 구현: **웹 GPT-6 Sol Instant**.
- 구현 100% 후보 후 전체 CI·통합·실사용 검증/수정. 고위험 DB·보안·권한·원본·외부 요청의 필수 국소 안전검사는 후행하지 않음. 필수 Actions/브랜치 보호 무단 해제 금지.
- Codex GPT-6.1 Sol Max 기술/보안과 Astra Max 디자인/UX 독립 검수 → 웹 Sol High 최종 통합 → 소유자 출시 GO 후 Codex Luna Extra High 등록.
- 제품 전체 최종설계 공식률은 기존 승인된 REQ 가중치+실검증 기준. 구현 후보 100%가 공식 100%나 판매 완료가 아니며 RELEASE HOLD 유지.

## 적용 범위·증거 강도
- GitHub 사용자 연결 계정으로 **35개 저장소**를 직접 목록 조회함. 중앙 기존 관찰 원장에 35 repo/80 refs(기본 main 35 + 추적 작업 브랜치45)가 기록되어 있음. 2026-11-15 동기화 시점의 원장임을 감안하여 최신 작업 브랜치도 별도 발견·적용.
- 그 80개 중 **79개 ref에서 `AGENTS.md` 최상단에 V2 정책/범위 게이트를 추가하고 GitHub write API가 커밋 SHA를 반환**. 기본 34개+추적 작업 45개. 커밋별 `repo/branch/SHA` 전체는 JSON 원장. **이 숫자는 실제 CI나 전체 79 HEAD 재조회/브라우저 테스트 완료 건수가 아니라 쓰기 영수증**임.
- 중앙 운영 브랜치 `kmong-productization`는 새 정본, `CHAT_BOOTSTRAP.md`, `AGENTS.md`, 앞선 프로토콜 4개 `SUPERSEDED` 배너, 사용자 글로벌 설정 수정안 및 본 감사와 등록부를 직접 변경. 중앙 `main`은 기존 GitHub App/Vercel 중앙 자동화의 원래 runtime/ref라 **수정 보류(OWNER_APPROVAL_REQUIRED)**.
- 관찰 원장 이후 추가된 `data2web_studio@work/high-data2web-security-r06-r29-20261115` / `@work/codex-data2web-to100-20261115`, `astra_pdf_redesigner@integration/astra-final-blueprint-100-20261115`, `Freelancer@tools/ax-dev-factory-local`는 본 80개 외에 별도로 V2 역할 게이트/필요한 최신 HANDOFF 시작 문구를 반영. `astra_pdf_redesigner@integration/astra-commercial-core`도 기존 80개에 포함되어 적용.
- 우선 핸드오프 교정 8개: DATA2WEB p85/High/Codex 3, Astra integration/P71 2, DBVORA P0, FFAX feature, AX Dev Factory tool. 기존 HANDOFF 길고 방대한 시행착오 로그는 삭제하지 않고 최상단 `HANDOFF-STARTUP-V2`로 **AGENTS→정확 HEAD→현재 ROLE→STATUS/실 소스**를 먼저 확인하도록 안내. 내용 중 구형 모델 위임은 역사/이전 지시로 취급.
- 해커톤 `lead/kic`, `lead/paypal`, `lead/ugreen` 및 3개 대회 main에는 `HACKATHON-SCOPE-GUARD`, 개인 로컬 AX Dev Factory에는 `AXDEV-EXCEPTION`, 과거/비활성 main에는 `INACTIVE-SCOPE-GUARD`를 명시. 크몽 작업 순서를 대회 제출/도구 안전 게이트에 강제로 적용하지 않음.
- 기능·테스트·배포·CI 워크플로 설정·GitHub App/Vercel 구성/계정·토큰·서드파티 자료·원래 상품 등록 이력·공식점수 **변경하지 않음**. 별도 GitHub push로 기존 Actions가 자동 시작되었을 가능성은 있으나 이 감사에선 최신 실행 결과를 전부 검증하지 않음.

## 왜 역사 삭제보다 역할 게이트를 택했나
**A. 오래된 문장들을 저장소별로 무작정 일괄 삭제/전체 HANDOFF 재작성:** 구형 요구·고객 권리/보안·대회 제출 결정·실패 복구 증거 소실 및 원본 드리프트 위험, CI/충돌 증가.
**B. 기존 Git History와 증거는 보존, 상단 `OWNER-DEV-EXECUTION-V2` 정책을 확정해 명시적인 범위·모델 역할 및 문서 권위 우선순위를 재정의:** 안전/비용/유지보수 면에서 채택. 과거 단계 문구는 역사이며 앞으로 실행할 절차가 아니라고 명시하여 효력상 충돌 제거.

## 읽기·역할 라우팅 수정
1. 현재 **채팅의 담당 임무 및 repo/branch** 확정. 해총 중앙 `ㄱ`은 GitHub App 90→100 임무 잠금만, 제품 `ㄱ`은 지정한 제품/브랜치만; 타 제품으로 몰래 전환 불가.
2. **최신 AGENTS V2** 및 정확 GitHub HEAD를 우선 확인. `HANDOFF → STATUS → REQUIREMENTS → 승인된 최종설계 → 실제 소스/테스트 → Instant 작업 큐`를 자료로 읽는다. HANDOFF의 새 이력이 AGENTS나 사용자 확정 최종설계를 덮어쓰지 못함.
3. High가 최초 설계/REQ 작업 큐를 고정하지 않았다면 Instant가 임의 설계를 재창조하거나 공수를 추정해 공식률을 바꾸지 않음. High 작업 완료 후 Instant는 READY 여러 작업을 연속 구현. 고위험 설계변경·개선 없는 2회 실패→High HOLD, 독립 Ready 계속.
4. 공식 검증률/구현률/상용 준비/실제 게시 상태 분리. 각 중요 작업 후 STATUS/HANDOFF 갱신, SHA/PASS/FAIL/SKIP/NOT_RUN 및 단순한 다음 작업 참조만 남긴다.

## GitHub 샘플 독립 재확인
- 새 중앙 정본/원장과 DATA2WEB 최근 High·Astra 최근 통합 HANDOFF·AX Dev Factory·KIC lead/SMAX main·비활성 OHORA main의 **최상단 문구 원격 readback** PASS.
- 커밋 샘플 4건 중앙 rollout `24fbe22f9852006975dfcae132c93869b59f2132`, DATA2WEB `09dacdcacf970536f4faaf026cbc869a7f0668a3`, AX Dev Factory `e4cf2a968da3b58772227829e146ec63b4ecac5f`, OHORA `640d28a4bfb97459c7d2dc7790e6907eff0b4a56`: GitHub commit SHA 및 author/committer `hibi89` readback 일치.
- **미실행/미검증:** 전 79개 ref에 대한 자동 end-to-end 읽기/테스트, 기존 CI 최신 결과, 모델 GUI 실제 선택 가능 여부, Codex 글로벌/ChatGPT 글로벌 사용자지침, Production/고객 실제 사용. '79/79 기능 정상'이라고 주장 금지.

## 소유자에게 요청해야 하는 두 가지
1. **글로벌 사용자지침은 GitHub 연결만으로 수정 불가.** [복사 가능한 교체 문구](../strategy/CHATGPT_CODEX_CUSTOM_INSTRUCTIONS_USER_ACTION_20261116.md)를 ChatGPT 웹 개인화 사용자지침과 Codex 전역 지침에 직접 반영해야 함. 변경 전 사용자 설정 백업; 수정 후 간단한 모델 역할 복원 테스트.
2. **해총 중앙 `main` (기존 GitHub App/Actions/Vercel 관련 원본)의 AGENTS/bootstrap 동기화 승인**은 실 운영 설정/자동배포 영향이 확인되기 전 보류. 중앙 `kmong-productization`에서 정책 정본 유지 가능. owner가 main 문서-only 정책 전파 및 관련 자동 동작을 승인하면 기존 정상 커밋과 배포 SHA를 먼저 확인한 뒤 안전하게 진행.

## 판정
중앙 공통 정책 작성/범위 이탈 방지/79개 tracked branch `AGENTS` 쓰기 커밋: **APPLIED WITH WRITE RECEIPTS**.
중앙 main: **OWNER_APPROVAL_REQUIRED / NOT_APPLIED**.
웹·Codex 계정 글로벌 사용자지침: **OWNER_ACTION_REQUIRED / NOT_VERIFIED**.
실제품 BE/FE 구현100%, CI, 독립검수, 구매자 인수, 크몽 실제 등록: **NOT_APPLICABLE/NOT_RUN**.
