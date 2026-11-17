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
