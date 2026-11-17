# 해총 GitHub App 중앙 자동화 — 사용자 GO main 병합 및 Production 격차 인계 (2026-11-17 KST)

> 본 파일은 크기가 큰 기존 `HANDOFF.md` 원본을 보존하면서, 현재 해총 임무의 실제 배포·검증 상태를 별도 인계하기 위한 기록입니다. GitHub App→HMAC Webhook→**기존** Vercel→GitHub Actions→중앙 원장 외 프로젝트를 다루지 않습니다.

## 1. 임무·확정 설계·사용자 승인
- 2026-11-17 KST 사용자가 “ㄱ 승인한다이기야 ㄱ”으로 직전 대기 중인 GitHub main 통합 및 기존 Production 반영·검증을 승인함.
- GitHub App read-only source / hub-only Actions write dispatch / HMAC / quota gate / hourly reconciliation / 원장 official score 불변 구조 유지. 유료·타 프로젝트 연동·Secret/권한/도메인 변경 승인으로 확대하지 않음.

## 2. 완료된 실제 코드 및 버전
- 통합 단일 SHA `b9e9f0fb17a3ffb9b233591a4721b536badb6b84`: PR #5 지침 정책 4개 파일 + PR #6 Webhook/Collector 5개 파일. 출처 9개 경로가 서로 겹치지 않음.
- [PR #7](https://github.com/hibi89/hackathon-command-center-2026/pull/7) main에 실제 병합: `e9a2b7e7afc3ebfc677b95730c214bcd9b732ceb` (검증된 통합 SHA와 Git tree `e81478647128f3ebb4d402d9f1bfcaf5ca6d5507` 동일). PR #6은 통합의 조상으로 GitHub 자동 MERGED 표시; PR #5는 이력 보존하며 별도 병합 없이 CLOSED/SUPERSEDED.
- 새 코드: 중복 GitHub Actions 이력 누락/비정상/비정렬 방어·비싼 중복 재수집 차단, owner instruction 공개 정책 rules exact-ID/anchor/path 방어, JSON 입력 안전/크기 한계.

## 3. 실제 실행 검증 PASS/FAIL/NOT_RUN
- main [Webhook tests #44033439548](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/44033439548): Node **81/81 PASS**, Python **132/132 PASS**, 추가 익명 Production GET probe 실시.
- main [observer #44033439587](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/44033439587): Python **132/132 PASS**; 정책 `CURRENT`, 계정 지침 `NOT_VERIFIED_NO_SNAPSHOT`.
- [blueprint evidence #44033439750](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/44033439750): PASS.
- [bot dispatch #44033438274](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/44033438274): preflight **RUN**, Collector **UPDATED**, 35 repos / 80 tracked refs / 29 products / unlinked0 / fingerprint0 / official scores UNMODIFIED, 원장 `c81e5effe60d2ef8debf9d5abf108428b6696e72`.
- [bot dispatch #44033444369](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/44033444369): **DEFERRED_BOT_BURST** (중복 full scan 생략). GitHub Actions “success”는 두 번째 sync가 이루어진 증거가 아님.
- Production 새 source SHA parity: **FAIL / READY_SHA_NOT_MATCHED** (HTTP 200 `ready` 만 검증), Production에서 새로운 HMAC Ping200 및 signed redelivery–Actions–ledger E2E는 **NOT_RUN**.

## 4. 진행·대기·차단
- GitHub main 반영 및 코드 안전 테스트 **완료**. 운영 collector 새 main에서 **RUN/UPDATED** 실증.
- **Vercel Production 현재 소스:** `5542fb5bf13cba5f30a374afc423b875790ff58c` (main `e9a2b7e7...`와 불일치); 동기화 코드의 기존 Production 반영 여부는 미적용/미검증. Vercel 권한 장애가 실제 Production 업데이트 차단.
- 공식 전체 구현완료율·검증완료율: 분모와 승인된 수용 매트릭스 미확정으로 `UNASSESSED`. RELEASE HOLD.

## 5. 오류·시도·원인·대안
- 연결된 Vercel API에서 기존 project ID `prj_veZOkRkhMEMEA6h7PiEIl3IKcthn` 404, 프로젝트명 `kmong-hub-event-bridge` 404, 기존 프로젝트 배포 목록 403, 프로덕션 도메인 배포 조회 404. 현재 연결로 조회되는 프로젝트는 **다른** `project08-executive`뿐. 오류 계층: **Vercel 계정/team/프로젝트 접근**. 기존 Production HTTP 200은 독립 GitHub Actions read-only GET로 관측되어 장애와 별도.
- 원인 후보: 다른 Vercel 소유자 계정/team 컨텍스트 또는 권한 제한. 현재 증거로 정확 원인 단정 불가.
- 개선 대안: 사용자 소유 Vercel 세션/올바른 팀 권한이 있는 **기존** 프로젝트에서 배포 연결 확인 및 사용자 승인 범위 내 안전 배포. 교체 Vercel 프로젝트 생성·권한 확대·임의 Secret 복사·타 프로젝트 연결 금지.
- 잘못된 같은 계정 404/403을 반복 호출하지 않고 STOP. 새 배포가 이루어졌다는 주장은 금지.

## 6. GitHub 정본·브랜치
- repo `hibi89/hackathon-command-center-2026`; main `e9a2b7e7afc3ebfc677b95730c214bcd9b732ceb`; feature #5 `b60715c8...`, feature #6 `bd148fb0...`, 통합 #7 `b9e9f0fb...`.
- 운영 `kmong-productization`은 main과 별개이며 자동 수집 bot이 원장만 갱신함. 임무 보호 첫 두 줄 유지.

## 7. 기존 Production URL·환경 경계
- `https://kmong-hub-event-bridge.vercel.app/api/webhook` — GET HTTP 200, `source_sha=5542fb5bf13cba5f30a374afc423b875790ff58c`, 검사 verdict `READY_SHA_NOT_MATCHED`.
- 기존 프로젝트만 사용, GitHub 연동 Root Directory 및 build ignore 설정 임의 변경 금지. `Ready`는 새 기능/동일 SHA의 근거가 아님.
- 별도 사용자 승인 범위가 존재해도 실제 Vercel 권한이 없어 새 Production 배포 **미실행**.

## 8. 원본·백업·Secrets
- 원장 blob `b05dfeb239ff12bf7374b07b4788f4af0ba96302` readback; JSON summary: `repository_count=35`, `tracked_branch_count=80`, `product_refs_unlinked=0`, `blocking_fingerprint_issues=0`.
- 환경변수·서명키·고객정보·원본·DB 변경 없음. 이전 Production의 실제 SHA 보존, 롤백/복구 경로로 기존 Git SHA 참고. GitHub PR/history 삭제 금지.

## 9. 다음 READY / 완료기준 / 사용자 선택
- 올바른 Vercel 소유자 세션에서 기존 프로젝트 ID/team/Production deployment 확인 → **현재 main SHA와 연결된 정확한 배포 후보**를 검증, 기존 Production 반영 → 익명 GET SHA 비교 + 서명된 Ping / 미서명 401 / 비허용 이벤트 202 / 서명 push 202 및 bot Actions/ledger readback.
- 배포/신규 서명 E2E가 완료되지 않았다면 `NOT_RUN`; 단순 GitHub commit/Actions success를 실서비스 최종 PASS로 환산 금지.
- 유료 서비스/새 Vercel 프로젝트/Secret/권한 변경·보호 우회는 이번 GO 포함하지 않음.

## 10. 갱신 시점 및 검증 기준
- 2026-11-17 KST; main 코드 기준 SHA `e9a2b7e7afc3ebfc677b95730c214bcd9b732ceb`; 위 Actions 및 원장 readback. 작성 당시 Production source SHA mismatch가 정확히 확인됐으며, 이후 자동 배포가 일어났는지는 이 파일 자체로 판정하지 않는다.

## 11. 신규 채팅 재확인: 연결 계정 범위·추가 Collector·Owner 단일 작업 (2026-11-17 KST)

### A. 이번 회차의 최신 읽기 증거
- `main@e9a2b7e7afc3ebfc677b95730c214bcd9b732ceb` 변동 없음. `kmong-productization@28281a00eba554e81a4ba49db9de9082412f6b8f` 확인 시점 기준. 운영 브랜치의 새 커밋은 `data/kmong_hub_auto_observations.json`만 변경함. BOT 원장 커밋과 Production 배포는 별개이다.
- 기존 CI run [#44033439548](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/44033439548) job log: Node 81 PASS, Python 132 PASS. 정확 main SHA 일치. 같은 job의 Production GET probe는 HTTP 200 / `READY_SHA_NOT_MATCHED` / `source_sha=5542fb5bf13cba5f30a374afc423b875790ff58c` (2026-11-17 06:44 UTC). **이 시각 이후 Production 동일성을 재검증하지 못했으므로 현재 SHA라고 단정하지 않는다.**
- 후속 BOT [#44036352165](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/44036352165) (`main@e9a2b7e7...`, 07:08 UTC): 실제 sync job log **`KMONG HUB SYNC: UPDATED`**, repositories 35, tracked branches 80, products 29, linked 29, unlinked 0, fingerprint alerts 0, official scores UNMODIFIED. 따라서 기존 `DEFERRED_BOT_BURST`과 구분되는 **추가 실제 수집** 증거 확보. 단, 이 수집이 최신 Vercel 런타임에서 서명 검증되어 이어진 단일 Delivery였는지는 별도 E2E 상관관계 미확립.
- GitHub `main` commit combined status에 Vercel `success` 1건 및 `Deployment has completed` 확인. [배포 상태 대상](https://vercel.com/hibi89/kmong-hub-event-bridge/4avFGgsA9c8Znb3vanPKvwB5FtJs). **GitHub 커밋의 Vercel success는 Production 도메인에 같은 SHA가 배정되었다는 증거가 아니다.**
- 구형 Production 관측 SHA `5542fb5...` 대비 `main@e9a2b7e...`은 GitHub compare 기준 21 commits ahead / 0 behind. diff에는 `services/kmong-event-bridge/lib/receiver.js`, `tools/kmong_hub_sync/quota_guard.py` 등 실제 런타임·수집 보안 변경이 포함되어 동일 Production 검증의 중요성이 높음.

### B. 실패한 Vercel 접근 재분류
- 연결 Vercel `list_teams`: `hibi89` (`team_oDTHTX6ht90nzgUWxnpzZxhU`) 단 1개 노출; Git-linked project 목록 공란, `kmong-hub-event-bridge` name 검색 결과 0.
- 정확 team ID를 명시한 기존 project ID 및 프로젝트명 `get_project`도 각각 404, GitHub status 대상 deployment ID 조회도 404. Vercel deployment URL fetch 역시 `lookup_deployment 404`. 현재 연결의 프로젝트 선택/권한 또는 소유 세션 문제를 배제할 수 없음; 프로젝트 삭제의 증거는 아님. 같은 404 재시도는 HOLD.
- 외부 실행 환경은 Production endpoint DNS를 확인하지 못했으나, 독립 GitHub Actions CI runner GET 200 기록은 보존됨. **현재 서비스 장애 또는 최신 Production 동작에 대한 단정 금지.**

### C. 사용자 조작 1회 묶음 및 다음 안전한 READY
1. 사용자 소유 Vercel 브라우저 세션에서 **기존** [Vercel project/deployment](https://vercel.com/hibi89/kmong-hub-event-bridge/4avFGgsA9c8Znb3vanPKvwB5FtJs)를 열어 계정·team·project access를 확인한다. 열린 프로젝트에서 team/project ID, GitHub 연결 repo, Production branch, Root Directory, Ignore Build 설정, Production deployment ID·source SHA를 읽는다. 연결된 ChatGPT Vercel 앱의 기존 팀/프로젝트 접근 승인 여부도 확인한다. **토큰·HMAC secret·.env 원문은 전달하거나 출력하지 않는다.**
2. 기존 프로젝트 접근 및 이전 정상 Production 복구 후보를 확인하면 사용자 기존 GO 범위에서 **같은 프로젝트**를 최신 검증 main SHA로 배포하고 실제 Production hostname 매핑을 확인한다. 새 프로젝트/도메인/권한/환경변수 변경·우회 배포는 별도 GO 전 금지.
3. 동일 Production endpoint에서 GET `source_sha` 일치, 미서명·잘못 서명 401, 비허용 이벤트 202, 유효 서명 Ping 200, 허용된 실제 GitHub Delivery → Actions 실행 ID → UPDATED/NO_CHANGE와 원장 readback을 동일 delivery ID로 상관 검증한다. 실제 서명 원문/토큰은 수집·기록하지 않는다.
4. 성공·실패를 실제 deployment ID, SHA, run URL, 수용조건 PASS/FAIL/SKIP/NOT_RUN으로 기록하고 독립 정상 동작/회귀 증거를 확정한다.

### D. 상태 경계
- GitHub 통합 + 회귀 CI + 다회 실제 Collector UPDATED: **PASS**.
- 현재 연결에서 기존 Vercel 프로젝트 접근: **BLOCKED (404)**.
- 신규 main Production SHA parity: **NOT_VERIFIED_AFTER_LAST_GET** (마지막 06:44 UTC GET은 **FAIL / READY_SHA_NOT_MATCHED**).
- 신규 main HMAC 서명 Ping 및 배포 후 전체 E2E: **NOT_RUN**.
- 공식 전체 구현/검증 가중치 분모: **UNASSESSED**. 출시/운영 최종 인수: **HOLD**.
- 이번 회차는 읽기 검증과 본 감사 기록만 수행. Production, GitHub main, Secrets, HMAC, 설치 권한, 원장 스키마, 다른 프로젝트 설정은 변경하지 않음.
