> **[OWNER-DEV-EXECUTION-V2 OVERRIDE | 2026-11-16]** [최신 사용자 확정 실행·모델 분담·부트스트랩 정본](OWNER_DEV_EXECUTION_CANONICAL_20261116.md): **웹 Sol High 최초설계/큐 → 웹 Sol Instant BE/FE 구현100% 후보 → 후행 전체 CI/수정 → Codex Sol Max+Astra Max 독립 검수 → 웹 Sol High 최종 인수 → OWNER GO 후 Codex Luna Extra High 등록.** 아래 문서의 기존 상충하는 모델 역할·중간 검수 시점·4개 슬롯 제한·매회 전체 CI 등은 **역사/이전 정책**으로 보존하며 더 이상 현행 일반 실행 지침으로 사용하지 않는다. 안전/기밀/권리/원본·상용 승인 조건은 유효.
> **[OWNER-P1-BROWSER-DEFERRAL-20261117 | NEWER OVERRIDE]** [중앙 V2.1 §0B](OWNER_DEV_EXECUTION_CANONICAL_20261116.md): P1 구현완료율에는 실제 브라우저/Playwright E2E·화면 클릭/시각·반응형/a11y·로그인 검증을 포함하지 않는다. BE/FE 코드/연결·REQ/정확 SHA와 필수 문법/타입·국소·고위험 안전 검사로 구현 후보 판단. 외출 중 승인·OTP/브라우저 검증은 `DEFERRED_TO_P2`, 차단 작업 격리 후 독립 READY 계속. 실 브라우저/UX/전체 CI·회귀는 P2에 일괄. 기존 필수 CI·보안·권한 GO 불변.

# High 설계 → Instant 고속 구현 → High 최종 인수 (2026-11-16)
> 사용자 신규 운영 선택 / 정책: KMONG-HIGH-TO-INSTANT-V1 / `hibi89/hackathon-command-center-2026@kmong-productization`.
> 이 문서는 [6단계 구현·CI·독립검수·등록 정본](KMONG_SOL_HIGH_IMPLEMENT_FIRST_QA_LAST_PROTOCOL_20261116.md)의 **구현 담당 역할 세분화**다. 기존 최종설계·확정 요구/가중치, 해총 GitHub App 주 임무 잠금과 제품별 원본·브랜치·상태·RELEASE HOLD 모두 보존.
> 2026년 12월의 정확한 모델 사용량/과금 정책과 계정별 접근 권한은 실제 적용 시 다시 확인한다. 정책이 달라도 실행 가능한 역할분리로 설계한다.

## 1. 역할과 권한 고정
| 구간 | 책임 | 모델/환경 |
|---|---|---|
| 최초 설계 (필수) | 사용자 최종 요구 정본 고정, A/B 설계 비교, 백엔드·프론트엔드·DB/API·보안·비용·장애복구·출고 게이트 설계, 구현 가능한 REQ 티켓 100% 분해 | **웹 GPT-6 Sol High** |
| 주력 구현 | 하위 티켓 읽기, 소스 수정·동작 점검, 커밋 SHA, 작업 상태 전환, 독립 티켓 연속 실행 | **웹 GPT-6 Sol Instant** |
| 설계 이탈/고위험 | 변경 요구·설계 충돌·DB 파괴/인증 변경·반복 실패·구조 결정이 필요한 경우만 처리 | **웹 GPT-6 Sol High** |
| 구현 100% 후보 후 | 전체 CI·빌드·E2E·실기기/브라우저·보안검증; 결함 최소 수정 | 우선 Instant, 고위험·반복 실패는 High |
| 독립검수 | 코드/보안/최종설계: Codex GPT-6.1 Sol Max; UI/UX: Astra Max (사용 가능하면) | Codex / 지정 GPT 모델 |
| 인수·출시 | 정확 SHA의 변경 검증/최종설계 전체·상용/권리/외부승인 게이트는 High; 사용자 GO 후 크몽 등록 보조는 Codex Luna Extra High | High → Codex |

## 2. 최초 설계 완료 산출물 — High 책임
개별 제품의 현재 **소스 저장소와 해당 담당 브랜치에** 아래 구조를 보존 또는 연결한다. 파일명이 이미 있으면 새 동명이인 문서로 중복 생성하지 않고 정본을 확장한다.
- `docs/FINAL_BLUEPRINT.md` 또는 기존 승인 설계: 사용자 확정 요구 전체/기술 제약/비목표, 2개 이상 설계 대안 성능·비용·유지보수 비교, 선택 근거, API/DB/FE 아키텍처·트리거/데이터 흐름/권한·실패 복구.
- `docs/INSTANT_TASK_QUEUE.json`: 각 `task_id`, `req_ids`, `depends_on`, `source_paths`, `change_type`, `implementation_acceptance`, `minimal_safety_checks`, `risk`, `status`, `blocker`, `evidence_sha`를 정의. 이미 원장 있으면 기존 원장/REQ를 그대로 링크하여 중복 원장을 만들지 않는다. 전체 설계 누락 0을 확인한다.
- `docs/INSTANT_RUNBOOK.md`: 매 `ㄱ`에서 실행할 다음 작업 선정, 브랜치·원본/백업, 명령, 커밋·검증·재시도·HOLD·인수인계 절차와 고위험 Escalation 조건.
- `docs/ACCEPTANCE_MATRIX.md` 또는 기존 scorecard: 요구 ID→승인 가중치(있는 경우)→코드·테스트·정확 SHA→구현/실행/실장비/권리/상용 항목을 별도 기록.
- **High가 최초 설계의 맨 마지막에 Instant가 바로 수행할 3~10개의 독립 작업 묶음을 선택하고, 각 작업의 입력·수정 가능 경로·명확한 종료 조건을 제공**한다. 설계 승인 전 요구 축소/기술 스택 갈아엎기 금지.

## 3. Instant 실행 프로토콜
1. `HANDOFF → STATUS → AGENTS → REQUIREMENTS → 확정 최종설계 → 실제 소스 → RUNBOOK → TASK_QUEUE`에서 **변경된 부분만** 재확인. 시작 시 branch/HEAD와 다른 작업자 PR/소유 파일을 확인한다.
2. 의존성이 충족되고 외부 승인/고객 원본/권한 변화가 필요 없는 **READY 티켓 중 고객 가치·잔여 공수 대비 가장 큰 구현 기능**부터 고른다. 같은 파일을 동시 수정하거나 승인 없는 main/배포를 건드리지 않는다.
3. 1회 호출에서 가능한 **여러 연관 티켓**을 실제 코딩·커밋. 한 티켓 끝났다고 인위적으로 중단하지 않는다. 문서 작성·CI 대기만으로 실진척을 주장하지 않는다.
4. P1 구현 중 전체 CI의 매회 반복 대기는 피한다. 문법·타입·변경 국소 스모크, 데이터 손실/보안·인증/권한·외부 통신 등 고위험 변경의 필수 즉시 검사, 기존 자동 CI·보호 규칙은 유지한다. 워크플로/브랜치 보호 설정은 무단으로 바꾸지 않는다.
5. 미실행 테스트는 `NOT_RUN`; 코드가 존재하면 `IMPLEMENTED_UNVERIFIED` 또는 `IMPLEMENTED_SMOKE_PASS`; 최종설계 조건 실제 검증 전에는 `VERIFIED`로 승격하지 않는다. 구현 100% 후보와 공식 최종설계 검증 100%를 구분한다.
6. 위험한 설계변경, 원본 데이터 손상 가능성, API 비밀/외부비용, 필요한 도구 접근 불가, 같은 원인 개선 없는 2회 실패 시 해당 티켓을 `HOLD_HIGH_REVIEW` 또는 `BLOCKED_EXTERNAL`로 격리한다. 독립 READY 작업이 남았으면 이어간다. 무의미한 같은 실패 반복 금지.
7. 모든 회차 보고: `repo/branch/HEAD | 구현 티켓 완료 수/전체 | 구현률(근거·분모 유효 시) | 공식 검증률/UNASSESSED | 바뀐 파일/실제 기능 | PASS/FAIL/SKIP/NOT_RUN | 다음 READY/차단`. High 호출은 필수 판단 문제로 제한한다.

## 4. 상태 모델과 간단 진척 계산
- `READY → IN_PROGRESS → IMPLEMENTED_UNVERIFIED → VERIFIED`; 차단은 `HOLD_HIGH_REVIEW / BLOCKED_EXTERNAL / OWNER_ACTION_REQUIRED`.
- `IMPLEMENTATION_SCOPE_PROGRESS`: **정본 전체의 백엔드/프론트엔드 구현 요구** 중 완료된 구현 패키지의 승인된 작업 가중치 기준 비율. 임의 `1%p`를 찍거나 작은 파일 수정으로 가산 금지; 가중치/전체 요구 매핑 불충분하면 숫자 대신 `x/y 패키지 완료` 표시.
- `OFFICIAL_FINAL_BLUEPRINT_COMPLETION`: 기존 `OWNER-FINAL-BLUEPRINT-100` 규칙에 따라 **실제 검증된** 수용 항목의 승인 가중치로만 계산. 공식 미산정은 `UNASSESSED` 유지.
- CI 전이라도 구현 결과를 볼 수 있게 `완료 REQ, 경로, SHA, 현재 최소 검증`을 따로 보고한다. 사용자 개입 최소화와 진척 증거 양립.

## 5. 첫 시범 운용의 선정 기준·중단 조건
- 기존 19개 SKU 중 **최신 작업 브랜치와 실제 코드가 확인되고, 외부 감사·법률·고객장비 승인 없이도 남은 구현이 존재하는 제품**을 고른다.
- 병렬 Codex/High 소유 파일과 충돌하는 저장소를 첫 시범으로 선정하지 않는다. 먼저 정확 repo/branch/최신 HANDOFF를 재확인한다.
- 1회 High 설계 결과로 10개 안팎의 테스트 가능한 소규모 티켓을 만들고 Instant 3~5회 실제 실행의 `코드 커밋·완료 티켓·재작업/실패·검증근거`를 측정. 성능 향상 폭·사용량 절감은 **실측 후** 판단한다.
- 후보 점검: `KMONG-SVC-01 DATA2WEB`은 2026-11-15 기준 R29 제품 검증기 통합 등 기술잔여가 있지만 2개 소유 PR과 외부 R07/R21/R25/R26/R29 승인 블로커가 있어 파일 충돌과 공식률 72점 정체 가능성 주의. `KMONG-SVC-08 DBVORA` main/develop 문서가 2026-10-26 초기 상태이므로 직전 채팅의 높은 진척치를 검증 없이 재사용하지 않음. 둘 중 실제 최신 코드·비충돌 READY 작업이 확인되는 쪽을 선정.
- 첫 시범은 다른 제품 코드/브랜치·CI·보안설정·점수·출시상태를 자동 수정하지 않는다. 제품별 선택·설계/개발은 해당 원본의 최신 승인·브랜치·실행 근거로 이어간다.

## 6. 다음 채팅에서 바로 사용할 두 명령
**High 설계 명령:** “해총 최신 `KMONG-HIGH-TO-INSTANT-V1`에 따라 이 제품 repo/branch의 최종설계·현재 소스와 실제 잔여 공수를 확인하고, 전체 요구를 손실 없이 작업 큐와 수용 기준으로 쪼개라. 실행 가능한 첫 3~10개의 고립된 Instant 배치를 준비하고 정확 SHA까지 GitHub에 기록해라. 원본/공식률 무단 변경 금지.”

**Instant 개발 명령:** “해당 제품 저장소의 HANDOFF/STATUS/AGENTS/최종설계와 `INSTANT_RUNBOOK` 및 `INSTANT_TASK_QUEUE`를 읽고 READY 작업을 가능한 만큼 연속 구현하라. 구현 중 매번 전체 CI 대기하지 말되 위험검사는 수행, GitHub 커밋과 전후 구현 진척 증거를 남기고, 외부 차단은 격리한 채 다음 독립 작업으로 이동하라. 결함 2회 실패 시 High로 넘겨라.”
