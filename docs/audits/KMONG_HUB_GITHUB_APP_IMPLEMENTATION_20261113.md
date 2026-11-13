## 2026-11-13 후속 안전성 검증 (실 인증 이전)
- 현행 코드 main@b8667cd27e92001e39ad21f4c71fde6f034bbd62: 예약 실행의 최초 관찰 원장 생성 차단. 최초 수동 dry_run=true 검증 후 수동 dry_run=false 원장 초기화가 선행되어야 예약 갱신 가능. 설치 가이드 보완 main@8c012e9296aaba186417d2d5523ae6ccd87bc5b1.
- [단위 회귀 CI #43357835854](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43357835854) **24/24 PASS** (예약 최초 생성 금지·초기화 후 예약 갱신 2건 추가), [공통 게이트 #43357835850](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43357835850) **SUCCESS**.
- 미완료/미검증: 전용 GitHub App 생성 및 35개 지정 저장소 설치, Actions 변수·Secret 등록, 설치 토큰, 실제 35/70/31/29 조회, 최초 중앙 원장 commit/readback, NO_CHANGE와 일일 스케줄 검증. data/kmong_hub_auto_observations.json 원격 조회 404 (미생성).
- 공식률 29/29 UNASSESSED, 과거 85·95 수치, 19 서비스, 작업중·사용자 개입 필요·RELEASE HOLD 보존. 제품 소스/권한/인증/고객 데이터/Vercel 변경 없음. 사용자 계정 설정 후 실제 Actions 결과로 최종 확인.

# Github App 기반 중앙 증거 자동 동기화 — 구현 및 실제 인증 상태
**2026-11-13 KST · 중앙 코드 `main@e28781d0af0904894251c48ab20a0360915a0671` · Hub 기록 기준 `32a1cb1cd35f7b2fd342797e739821f8438e6f69`**

## 범위와 보안 결정
- **A안 채택:** 35개 원본 저장소/70 추적 브랜치에 *읽기 전용* 전용 GitHub App 설치 토큰(`Contents: read`, `Actions: read`), 해총 중앙 저장소의 GitHub Actions `GITHUB_TOKEN contents: write`는 **중앙 저장소에만 쓰기**. 동일 토큰 재사용·원본 저장소 쓰기 금지.
- 비교 B안: 만료/교체/개인 계정 토큰 수명관리 부담이 있는 fine-grained PAT 단독 교차 권한보다 전용 GitHub App을 우선. 별도 서버 구축도 배제(운영·추가 비용 감소). <https://github.com/actions/create-github-app-token/blob/main/README.md>의 v3 권한·대상 저장소 scope 방식 사용.
- 자동화 트리거는 `workflow_dispatch`와 매일 11:10 KST `schedule`뿐, `KMONG_SYNC_ENABLED=true` 설정 전에는 스케줄 잡 비활성. 수동 최초 `dry_run=true`가 기본. `schedule`은 독립 테스트된 write mode이며 커밋 실제 변경이 있을 때만.
- **정확히 35개 GitHub App 설치 범위**가 아니면 수집 자체 중단. `source_repositories.json`에 main 35+기존 문서상 주요 작업브랜치35(정확히 총70), 중앙 원장의 상품 `tracked_branch` 29개도 읽기 전용 관측. 기존 31 pin의 Git blob SHA 변동 검사.
- 인증 성공 시에만 `kmong-productization/data/kmong_hub_auto_observations.json` **새 전용 파일 1개**를 idempotent 조건부로 갱신. 기존 공식 29 상품원장, 19개 SKU 등록이력, 상품 상태, 요구사항 100점 가중치/공식률·`STATUS/HANDOFF`는 자동 쓰기하지 않는다.
- 변경 없음 → `NO_CHANGE`(무커밋); dry-run → `DRY_RUN`; 타인이 소유한 JSON·권한 오류·source 35 미달·optimistic SHA write 충돌·원격 readback 불일치 → **BLOCKED**. 기존 이력 강제 수정 금지.

## GitHub에서 직접 확인한 구현·실행 결과
| 대상 | 실제 근거 | 결과 |
|---|---|---|
| 중앙 읽기/쓰기 분리 엔진 | [`tools/kmong_hub_sync/sync.py`](https://github.com/hibi89/hackathon-command-center-2026/blob/main/tools/kmong_hub_sync/sync.py) + [35+35 roster](https://github.com/hibi89/hackathon-command-center-2026/blob/main/tools/kmong_hub_sync/source_repositories.json) | GitHub 커밋 완료, **앱 인증 실환경 호출은 미실행** |
| 테스트 | [Actions #43352459675](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43352459675), 코드 정확 SHA `e28781d0af0904894251c48ab20a0360915a0671` | **22/22 PASS**; read scope/fingerprint/NO_CHANGE/dry-run/SHA guard/readback tests 포함 |
| 기존 자동검증과 충돌 | [Actions #43352459689](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43352459689), 동일 SHA | 공통 gate SUCCESS, `UNASSESSED` 유지 |
| Author/Committer | [최신 GitHub commit](https://github.com/hibi89/hackathon-command-center-2026/commit/e28781d0af0904894251c48ab20a0360915a0671) | GitHub 계정 `hibi89`과 연결된 작성자·커미터 확인, 서명 검증은 미설정 |
| 실제 App 원격 스캔 | 현재 전용 App Client ID, 개인키 및 Actions 등록값 미확인 | **미검증/활성화 대기** |
| 자동 Hub commit & schedule | 사용자 UI 설정 후 수동 read-only 검증→정상일 때 write | **미실행**; 성공·완료 주장 금지 |

## 외부 사용자 필수 작업과 최소 승인 범위
- 사용자는 App 설치·비밀키/변수 등록과 시험 실행에 필요한 권한을 승인했으나, ChatGPT GitHub 커넥터에는 GitHub App 생성/Private Key 발급/Actions Secrets·Variables 기록 액션이 없음. **승인 표현만으로 GitHub Actions 자격증명이 만들어지지 않음.**
- 실제 GitHub UI 절차: [중앙 설치 가이드](https://github.com/hibi89/hackathon-command-center-2026/blob/main/docs/strategy/KMONG_HUB_GITHUB_APP_SETUP_20261113.md).
  1. 개인 GitHub 앱 생성, `Contents: Read-only`, `Actions: Read-only`; `hibi89`의 35개 정확 저장소에만 설치.
  2. 중앙 repo Actions Variable `KMONG_SYNC_APP_CLIENT_ID` 저장; Secret `KMONG_SYNC_APP_PRIVATE_KEY`에 GitHub 발급 PEM 전체 내용 저장(채팅 전송 금지).
  3. Variable `KMONG_SYNC_ENABLED=true` 설정 후 Actions에서 `dry_run=true` 성공 확인, 그 다음 `dry_run=false` 수동 시범 운전.
- 정상 이후 GitHub Actions 매일 11:10 KST 일일 상태 갱신, 다른 레포 쓰기·배포·설정 확대 없음.

## 완료 기준과 남은 기술/범위
- 코드 설계·로컬 모의 네트워크 22 regression/기존 shared CI PASS는 **완료**.
- 실제 GitHub App installation token mint + 35 repo live metadata access, 70 ref 조회, 31 pin, 상품29, 첫 hub commit/remote readback, 두 번째 NO_CHANGE, schedule은 **전부 미검증/권한 준비 대기**.
- 다른 네 repo 최종설계 정본 미확인, 22 observe 항목 사용자 확정 최종설계 승인 근거 미확인, HAE/LA 합성 CI는 실제 고객 전체 기능 E2E 대체 아님. 제품 공식률 **29/29 UNASSESSED**, 고객 시스템과 Production **미적용**.
- 자동 동기화가 시작되더라도 새 파일에 GitHub SHA·CI·지문 **관찰** 결과만 저장하고 공식 완성률을 계산하거나 변경하지 않는다. 요구사항 전체 승인·실제품 검증은 별도 절차.

## 검증 시점
2026-11-13 KST GitHub 원격 커밋 SHA/Actions job logs, code+unit-test 검토. App credential/secret 환경은 읽기권한 도구가 없어 **미확인** 상태.
