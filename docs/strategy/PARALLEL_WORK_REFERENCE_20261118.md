# 해총 병렬 개발 레퍼런스 — SWU-CPAA/WE와 A/B/C 멀티 작업자 (2026-11-18 KST)

> **문서 종류: 참고 실행 패턴 / 신규 강제 정책 아님.** 상위 정본은 [OWNER_DEV_EXECUTION_CANONICAL_20261116.md §0J·§0I](OWNER_DEV_EXECUTION_CANONICAL_20261116.md) 및 [GPT6_HIGH_STANDARD_WORK_UNIT_20261117.md §0E·§0D·§0C](GPT6_HIGH_STANDARD_WORK_UNIT_20261117.md)이다. 사용자 현재 지시, 프로젝트 최종설계·고유 안전/승인 규칙, 중앙 정책, 실제 코드/HEAD의 우선순위를 보존한다. 본 문서 자체는 제품 코드 변경, 멀티 에이전트 자동 실행, main/Production GO를 의미하지 않는다.

## 1. 세 종류의 '병렬'을 분리

| 방식 | 실제 실행 주체 | 필요 조건 | 기본 판단 |
|---|---|---|---|
| **단일 웹 GPT의 SWU-WE** | 웹 GPT **한 명**이 1회 \`ㄱ\`에서 독립/위상정렬 1~6 SWU를 순차 구현. 도구 조회·국소 검사만 지원 시 병렬 | 최신 HEAD·실제 READY·비충돌 경로 | **기본 방식**. 모델 추론/코드 생성은 직렬이며 작업자가 3명으로 복제되지 않음 |
| **동일 저장소의 다중 작업자** | 실제로 분리된 GPT/Codex/Work 세션·작업환경 | 동일 기준 commit SHA, 서로 다른 브랜치, 고정 API 계약, 중복 없는 allowed_paths, 통합자 1명 | 충돌/인계비용을 초과하는 경과시간 절감 예상 시 |
| **A/B/C 별도 저장소의 다중 작업자** | 독립 세션 A(정본·통합), B/C(분리 모듈) | A 최종설계·계약 **고정 SHA** + B/C 각각의 기준 SHA, 정확히 일치하는 계약 파일 해시, 명시적 소스 복사 허용목록, 소유자 1명 | 저장소별 격리·독립 코드 개발이 실제 필요할 때만 |

**서로 다른 저장소는 같은 Git commit SHA를 갖는다는 전제를 세울 수 없다.** 다중 저장소에서는 A의 설계/계약 버전을 공통 기준으로 고정하고 각 저장소의 HEAD, 파일 SHA256, 최종 통합 HEAD를 따로 추적한다. 단일 저장소 병렬에서만 '동일 출발 SHA'가 문자 그대로 동일하다.

## 2. 병렬 선택 전 승인·선정 게이트

1. 최신 원격 \`repo/branch/HEAD\` → \`AGENTS.md\` → \`HANDOFF.md\` → \`STATUS.md\` → REQ/최종설계 → 실제 소스/큐를 확인한다. 완료 후보는 코드 근거로만 판정한다.
2. SWU-CPAA로 의존 DAG, 임계경로, 후속 차단 수, S/C/I/D/U, 외부 GO/보안 HOLD, 작업 경로 충돌, 실제 작업자·모델 가용성 및 총 소요시간을 평가한다.
3. 병렬을 택하려면 **실제 동시 작업자 존재**, 공통 계약·설계 기준, 소유 영역·허용경로, 통합 책임자, 기준 SHA와 인수 수용조건을 먼저 고정한다. 절감 시간이 추가 호출/한도·검토·복사/충돌·재검증 비용보다 불확실하거나 작으면 단일 GPT SWU-WE/순차 실행으로 돌아간다.
4. 외부/고객 원본·비밀·권한·DB 위험·유료·실서비스·main/Production·출시/삭제는 기존 별도 승인 게이트를 유지한다. 새 저장소는 사용자 기존 PUBLIC-only 원칙을 따르지만 **고객 소스·비밀·비공개 설계는 공개하지 않는다**.
5. 대화에서 \`ㄱ\`만 여러 번 입력했다고 다른 실제 GPT 세션이 자동 생성되거나 백그라운드에서 병렬 실행되는 것은 아니다. 각 작업자는 **실제 시작/실행/커밋 증거**를 남겨야 한다. ChatGPT Work는 브라우저/실서비스 조작 환경이며 Codex Sol Max 모델과 동의어가 아니다.

## 3. 모듈·계약·큐 분리 표준

- **A / 설계자·통합자:** 승인된 30 REQ 등 제품별 전체 기능·수용조건과 고정 계약의 유일한 정본. 자신의 core/CLI/GUI 및 최종 통합 브랜치를 관리. B/C 계약 변경은 A가 검토하고 사용자 GO가 필요한 변경은 별도 요청한다.
- **B / 독립 코드 모듈:** A가 정의한 입력·출력·실패 계약을 그대로 구현. A/C 영역이나 공통 설정을 변경하지 않는다.
- **C / 다른 독립 모듈:** A 계약의 데이터 구조만 받아 구현; B 구현 코드나 A의 내부 코드를 직접 import하여 결합하지 않는다.
- 각 SWU 레코드에는 \`SWU-ID, REQ-ID, owner, depends_on, allowed_paths, acceptance, source SHA, status, test evidence, retry counts\`를 유지한다. 설계·Mock·문서·테스트 개수는 P1 기능 구현 건수로 가산하지 않는다.
- B/C는 \`AGENTS/HANDOFF/STATUS/REQUIREMENTS\`, \`WORKER_SCOPE\`, \`CONTRACT\`, \`assigned_swu_queue\`로 자기 일감을 이해한다. **A 최종설계는 참조 링크와 정확한 고정 SHA로 조회**하며 전체 설계 복제가 필수는 아니다. 단 최신 중앙 정책 HEAD와 사용자 지시를 회차마다 확인한다.
- API/JSON 스키마의 required 필드, 타입, 함수 시그니처, 예외/오류, 정렬, 경로·SHA provenance를 고정한다. 계약 변경 필요 시 \`CONTRACT_CHANGE_REQUEST\`를 A에 올리고 A 승인·버전 갱신·각 작업자 반영 후에만 구현한다.

## 4. 실행·인수인계·통합 순서

1. **P0 고정:** A가 최종설계·고유 보안 규칙·REQ 전체·계약 V1·SWU DAG·소유 경로·통합자·브랜치를 확정하고 B/C에 공통 설계 SHA 및 정확한 계약을 배포한다.
2. **각자 P1:** A/B/C의 별도 실제 작업자 채팅이 자신의 \`ㄱ\`으로 독립 READY를 코딩한다. 각 작업은 실제 caller→callee→상태/출력·핵심 실패 경로, 최소 syntax/type/smoke, 개별 원격 커밋 SHA로 \`IMPLEMENTED_UNVERIFIED\` 후보를 판정한다. 필수 안전검사/기존 CI는 우회하지 않는다.
3. **작업자 인계:** B/C는 \`repo@branch@commit_sha\`, SWU/REQ, 변경된 허용 파일 목록과 각 SHA256, 국소 PASS/FAIL/NOT_RUN, 남은 코드 간극·계약 변경 요청·차단 증거를 HANDOFF에 기록한다.
4. **A 선별 통합:** 원본 B/C 브랜치·Git 이력 보존 후 **허용된 모듈/테스트 경로만** A의 integration 브랜치로 복사한다. 서로 다른 repository의 branch를 동일 SHA로 가정하거나 공통 \`AGENTS/HANDOFF/STATUS/pyproject\`를 덮어쓰지 않는다. 복사 전후 파일 해시 및 기준 SHA를 기록한다.
5. **A 통합 최소 검사:** 스키마·타입·버전, import, 정상/핵심 오류 경로, 입력/출력, provenance, 충돌·누락 경계를 확인하고 A 통합 HEAD와 소스별 SHA를 기록한다. 통합 불일치 시 수정 담당 SWU를 재배정하되 원본/이력·계약을 임의 훼손하지 않는다.
6. **P2 별도 검증:** 승인된 담당자가 전체 CI/기능/보안/통합/브라우저/실기기·복구/회귀를 수행하고 결함 수정·재검증 후 독립 기술·보안/UX 감사 및 High 최종 인수. **자가 국소 검사는 독립 검수가 아니다.** P1 \`IMPLEMENTED_UNVERIFIED\`와 P2 \`VERIFIED\` 분리.
7. **종료:** B/C 저장소 및 백업·이력은 보존. 삭제/가시성 변경/main 병합/Production/상용 공개는 사용자 별도 GO 없이는 하지 않는다.

실질 무진전은 SWU별 초기 2회 → \`ISOLATED_REDESIGN_PENDING\` 격리 → 다른 방법 2회 → 총 4회면 \`SOLMAX_BATCH_PENDING\`. 고위험·필수 임계차단은 0회부터 실제 제품 작업자가 근거를 갖춰 전문 지원 요청 가능. 다른 안전 READY는 계속한다.

## 5. 실례 — REQ Evidence Auditor A/B/C (구현 완료 사례가 아닌 *설계·분리 사례*)

- **A (정본):** [\`hibi89/REQ-Evidence-Auditor-A-\`](https://github.com/hibi89/REQ-Evidence-Auditor-A-) · [설계 \`e58e14ee4ef84dfc226d657cfe45b1d40cfb9ba9\`](https://github.com/hibi89/REQ-Evidence-Auditor-A-/tree/e58e14ee4ef84dfc226d657cfe45b1d40cfb9ba9) · [최종설계](https://github.com/hibi89/REQ-Evidence-Auditor-A-/blob/e58e14ee4ef84dfc226d657cfe45b1d40cfb9ba9/docs/FINAL_BLUEPRINT.md) · [SWU DAG](https://github.com/hibi89/REQ-Evidence-Auditor-A-/blob/e58e14ee4ef84dfc226d657cfe45b1d40cfb9ba9/docs/SWU_DAG.md) · [통합 Runbook](https://github.com/hibi89/REQ-Evidence-Auditor-A-/blob/e58e14ee4ef84dfc226d657cfe45b1d40cfb9ba9/docs/INTEGRATION_RUNBOOK.md). 30 REQ, 계획 SWU 17(A7/B5/C5); A는 \`src/reqea/**\`와 \`tests/a/**\`, 공통 docs/package·integrator. 최종 제품은 A만.
- **B (정적 코드 인덱스):** [\`hibi89/REQ-Evidence-Auditor-B-\`](https://github.com/hibi89/REQ-Evidence-Auditor-B-) · \`feature/reqea-b-codegraph-p1-20261118@8f40de5cc6265917c457f279469f4e2d064d0a10\` · [작업 범위](https://github.com/hibi89/REQ-Evidence-Auditor-B-/blob/8f40de5cc6265917c457f279469f4e2d064d0a10/docs/WORKER_SCOPE.md). \`B-01..05\`, \`src/reqea_codegraph/**\`, \`tests/b/**\`; API \`build_code_index(root, options) -> dict\`.
- **C (증거 매칭·리포트):** [\`hibi89/REQ-Evidence-Auditor-C-\`](https://github.com/hibi89/REQ-Evidence-Auditor-C-) · \`feature/reqea-c-evidence-p1-20261118@b5d6b4eaabc95340cfa1ac6cdd80201bfc122773\` · [작업 범위](https://github.com/hibi89/REQ-Evidence-Auditor-C-/blob/b5d6b4eaabc95340cfa1ac6cdd80201bfc122773/docs/WORKER_SCOPE.md). \`C-01..05\`, \`src/reqea_evidence/**\`, \`tests/c/**\`; API \`evaluate(manifest, code_index, options) -> dict\` / \`render_html(audit) -> str\`.
- **공통 계약:** \`reqea.v1\`의 [A 계약 정본](https://github.com/hibi89/REQ-Evidence-Auditor-A-/blob/e58e14ee4ef84dfc226d657cfe45b1d40cfb9ba9/docs/CONTRACT_V1.md). 실제 확인된 A/B/C 계약 Git blob SHA 모두 \`b39d8307662206472f2165b4bce3c0e10e2b62b6\`. B/C는 A 고정 설계 SHA를 직접 참조하므로 설계 변경 시 **자동 동기화되지 않음**; 변경 관리는 A가 책임진다.
- **SWU DAG:** 첫 독립 READY는 A-01/02/03, B-01, C-01. B-05/C-04 완성 이후 A-04 통합, A-05 CLI, A-06 GUI, A-07 Actions로 의존 연결. A 통합 브랜치 \`integration/reqea-p1-20261118\`에서만 합친다.
- **관찰 시점 상태:** 위 고정 SHA의 P0 설계·작업 분리 기록이며 기능 P1 \`NOT_STARTED\`, P2 \`NOT_RUN\`, 공식 구현/검증률 \`UNASSESSED\`. 이 문서는 **세 실제 모델의 동시 코딩/완료·속도 향상 증거가 아니다**. 초기 계획 17 SWU/30 REQ는 다른 프로젝트의 분모로 복사하지 않는다.
- **구별:** Provisioner 실증용 \`hibi89/Test-A\`, \`Test-B\`, \`Test-C\` 3개는 단순 공개 저장소 자동 생성·표준 초기화 성공 사례이며 **REQ Evidence Auditor A/B/C와 다른 저장소**다.

## 6. 작업 시작/최종 인수 체크리스트

- [ ] 제품 임무와 최종설계/REQ 정본 1개 지정, 안전·사전 승인 분리
- [ ] 워커 각각의 실존 repo/branch/HEAD·역할·allowed_paths·SWU/REQ·의존 DAG 확정
- [ ] 공통 계약 버전·파일 SHA와 소스 SHA들 별도 보존; 호환되지 않으면 HOLD
- [ ] 실제 각 작업자 세션 실행 여부와 SWU별 코드/국소 검사/커밋 증거 확인
- [ ] 통합자만 선별 소스 복사/커밋; 공통 파일·원본 덮어쓰기 금지
- [ ] 전체 P1 구현 후보와 P2 검증 수용조건을 분리, 숫자 무근거면 \`UNASSESSED\`
- [ ] 속도 효과는 같은 난도·조건의 실측이 없으면 \`SPEED_EFFECT=UNMEASURED\`; 토큰/작업자 호출·대기·충돌·통합·P2 재작업 비용도 포함
- [ ] 중앙 문서 게시만으로 개별 제품 repo에 반영됐다고 주장하지 않음 (\`NOT_PROPAGATED\`)

**기본 결론:** 독립 다중 작업자 병렬은 '세 저장소를 만들었다'로 성립하지 않는다. 계약·의존·수정 경로·책임·실제 작업자·SHA 인수와 통합 근거가 마련되고 총 P1 완료시간 절감이 예상될 때만 선택한다.
