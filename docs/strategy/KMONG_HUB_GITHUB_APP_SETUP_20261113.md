# GitHub App 기반 해총 자동 증거 동기화 — 보안 설치·운영 안내

> 기준 2026-11-13 KST · **안전한 코드 설치와 실제 App 연결은 별개**. 사용자 확정 전체 최종설계 100점 기준 보존, 공식률 자동 승격 없음.

## 1. 확정 아키텍처

| 계층 | 계정/토큰 | 권한 | 역할 |
|---|---|---|---|
| 35 소스 저장소 | 별도 전용 GitHub App 설치 토큰 | `Contents: Read-only`, `Actions: Read-only`; Metadata 자동 read | 35 main + 35 지정 브랜치 + 29 상품 관련 브랜치의 SHA/CI/정본 지문만 읽기 |
| 중앙 관리 저장소 | 워크플로 내장 `GITHUB_TOKEN` | 이 저장소에만 `Contents: Write` | `kmong-productization/data/kmong_hub_auto_observations.json` 파일만 갱신 |
| 기존 70 caller | 변경 없음, `Contents: Read` | 저장소별 read-only | 기존 지문/manifest gate 유지 |

- 전용 App 액세스 토큰은 GitHub가 자동 발급하는 단기 설치 토큰이며, Actions 종료 후 폐기된다. App 키는 GitHub Actions Secret으로만 관리한다.
- 워크플로는 **오직** `workflow_dispatch`와 하루 1회 스케줄(11:10 KST)에서 실행한다. 외부 PR/포크 이벤트로 App 키가 노출되지 않게 한다.
- GitHub Actions `vars.KMONG_SYNC_ENABLED=true`를 등록하기 전에는 정기/수동 Sync Job이 **SKIPPED**. 등록 후 첫 실행은 `dry_run=true`로 확인.
- GitHub App에 권한 확장, 고객 원문·코드·최종설계 본문 외부 업로드, 강제 푸시, GitHub Secrets 파일 저장, 제품 Deploy 등은 필요 없음.

## 2. 사용자 GitHub 웹 UI에서 수행해야 할 계정 단계

1. [GitHub 개발자 설정](https://github.com/settings/apps) → **New GitHub App**. 이름 예: `kmong-hub-source-auditor`; Homepage URL은 중앙 [GitHub 저장소](https://github.com/hibi89/hackathon-command-center-2026); Webhook은 **Active 해제**. 저장소 권한은 **Contents Read-only**, **Actions Read-only**만. Metadata Read는 기본. 조직/계정 관리·워크플로 수정·쓰기 권한 전부 없음.
2. GitHub App 등록 후 **Client ID** 값을 확인하고 **Generate a private key**로 PEM 파일 생성. PEM의 실제 내용은 채팅이나 GitHub 코드에 올리지 말 것.
3. 만든 App의 **Install App** → `hibi89` → **Only select repositories**로 설치. 선택 대상은 [35개 고정 목록](../../tools/kmong_hub_sync/source_repositories.json)의 `repositories[].repository`. 기존 ChatGPT GitHub 커넥터 설치는 이 자동화 App 키를 대신하지 못함.
4. 중앙 저장소 [Actions Variables](https://github.com/hibi89/hackathon-command-center-2026/settings/variables/actions)에 변수 `KMONG_SYNC_APP_CLIENT_ID` = 위 Client ID 생성.
5. 중앙 저장소 [Actions Secrets](https://github.com/hibi89/hackathon-command-center-2026/settings/secrets/actions)에 `KMONG_SYNC_APP_PRIVATE_KEY` = GitHub가 다운로드한 PEM 파일의 **전체 내용** 등록.
6. 테스트 준비 후 중앙 Actions Variables에 `KMONG_SYNC_ENABLED` = `true` 등록. [Actions](https://github.com/hibi89/hackathon-command-center-2026/actions) → `Kmong hub cross-repository evidence sync` → `Run workflow` → 먼저 `dry_run=true` 실행하여 35개 접근/70 참조·31 지문·29 제품 연결 확인. 정상 후 `dry_run=false` 수동 실행; 이후 일정 자동 실행.

**개인 계정 설정과 PEM Secret 등록은 현재 ChatGPT GitHub 도구로 불가.** 위 6단계 완료 후 '했다'만 알려주면 계정 자체로부터 비밀키를 받지 않고 CI 결과를 확인할 수 있다.

## 3. 실행·실패·복구

- 실행 Python: `tools/kmong_hub_sync/sync.py`, 표준 라이브러리, API endpoint는 `api.github.com`만, `READ App` 토큰과 `HUB WRITE` 토큰 분리.
- App 토큰의 `/installation/repositories`가 **정확히 35개**를 가리키지 않으면 전체 중단. 다른 1개/전체 계정 액세스로 자동 축소·확장하지 않음.
- 소스 코드는 읽지 않고 Git 브랜치 HEAD, Actions run ID/SHA/conclusion 및 원본 문서의 **blob SHA만** 저장. HAE/LA 합성 테스트 PASS와 최종상품 완성을 구분.
- 원장 갱신은 독립 파일 `data/kmong_hub_auto_observations.json` 하나에만 허용. `data/final_blueprint_product_index_20261113.json`, 19개 SKU 등록 이력, `STATUS.md`, `HANDOFF.md`, 과거 P85/P95 및 공식 `UNASSESSED`는 자동 쓰기 금지.
- 새 증거와 기존 스냅샷이 동일하면 `NO_CHANGE`로 커밋 없음. `dry_run`은 `DRY_RUN`으로 커밋 없음.
- API/권한 실패, 중복 repo, 불일치 원장, GitHub optimistic `sha` 충돌에서는 강제 덮어쓰기 금지. 오류를 Actions에 남기고 다음 실행 전 원인 조사.
- 소스 지문 변경이 발견되면 그 사실을 **관찰 원장에 기록**하고 강제 핀의 경우 job도 실패 처리한다. 최종설계 기준 지문을 임의 최신으로 바꾸거나 공식률을 승격하지 않는다.
- Auth 오류는 GitHub App 설치 대상·Repository permissions/Secrets·Actions 허용부터 확인. 중앙 쓰기 403이면 기존 branch protection/Actions `GITHUB_TOKEN` 정책과 충돌했을 가능성이 있으므로 **우회하지 않고 승인받아 설정 변경**. `Ready`/CI PASS만으로 고객 기능 수용 선언 금지.
- 새 중앙 Snapshot 경로를 삭제/변경하려면 기존 JSON와 커밋 SHA를 확인하고 별도 승인. 과거 Snapshot은 Git 이력으로 복구.
- 원래 35 main + 35 작업 브랜치 목록을 [roster JSON](../../tools/kmong_hub_sync/source_repositories.json)에서 확인. App의 설치 저장소나 새 대상 변경은 사용자 승인 필요.

## 4. 점검·완료 기준

1. 권한 없는 테스트에서 단위 테스트 PASS.
2. GitHub App을 설정한 실제 `dry_run=true`에서 `/installation/repositories` 35개와 GitHub API 70 참조·31 지문·29 제품 매핑 조회 PASS.
3. `dry_run=false`에서 원장 **새 커밋 → 원격 readback 완전 일치** 실증, 동일 상태 재실행은 `NO_CHANGE`.
4. 1일 스케줄 재실행과 API 실패·SHA 충돌·모니터링 증거 확인.
5. 29개 공식 완성률은 별도 owner-approved 100점 rubric과 실제 고객 E2E 확인 전 계속 `UNASSESSED`.

**배포/고객서비스/Vercel:** 해당 없음. 실제 App 연결·일정 성공 이전에는 `KMONG_HUB_SYNC_CREDENTIALS_PENDING` / `검증 대기`로 기록.
