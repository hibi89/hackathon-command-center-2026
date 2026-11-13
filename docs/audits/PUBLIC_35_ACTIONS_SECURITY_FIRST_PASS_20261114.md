# 2026-11-14 KST — 전 저장소 PUBLIC 전환 후 Actions 및 공개 보안 1·2차 감사

- **책임:** 해총 / `hibi89/hackathon-command-center-2026@main`
- **상태:** `ACTIONS_RUNNING_SAMPLED / METADATA_SCAN_DONE / HISTORY_AND_SECRET_AUDIT_PENDING`
- **실행:** 연결 GitHub API 읽기 전용. 사용자 공개 전환 이후 이 감사에서 **코드·설정·권한·비밀키·배포·상품 상태 수정 0건**. 본 문서/STATUS/HANDOFF만 갱신.
- **공식 참고:** [GitHub 공개 전환의 영향](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility), [GitHub Actions 요금](https://docs.github.com/en/billing/concepts/product-billing/github-actions).

## 1. 전체 PUBLIC 상태와 분모

- 사용자 CLI `gh repo edit --visibility public`: 이전 PRIVATE 17개를 17/17 PUBLIC으로 변경, 0 실패.
- 연결 GitHub `list_repositories(owner=hibi89)` 원격 대조: **35개 전체 PUBLIC, PRIVATE 0**.
- 35/35는 중앙 관측 레지스트리의 35개 기준이며, 계정의 다른 소유·조직 계정이나 이후 생성되는 저장소까지 영구 보증하지 않음.

## 2. 공개 이후 GitHub Actions 실제 실행 확인

| 저장소 | 정확한 run | 상태 | 근거 범위 |
|---|---|---|---|
| [Freelancer](https://github.com/hibi89/Freelancer) | [#43523875124](https://github.com/hibi89/Freelancer/actions/runs/43523875124) (2026-11-13 23:01:07 UTC) | **SUCCESS / 1 job 성공** | 최종설계 Gate, checkout 및 증거 검증 Step 성공. 실제 제품 전체 최종완성률 승인과 무관 |
| [data2web_studio](https://github.com/hibi89/data2web_studio) | [#43523342553](https://github.com/hibi89/data2web_studio/actions/runs/43523342553) (22:56:51 UTC) | **SUCCESS / 4 jobs 성공** | Windows browser, Linux browser, Ubuntu Python, Windows Python; 실제 Chrome/Edge·Tk 검증 Step 성공. 합성/hosted 환경 |
| [data2web_studio](https://github.com/hibi89/data2web_studio) | [#43523343218](https://github.com/hibi89/data2web_studio/actions/runs/43523343218) | **SUCCESS / 1 job 성공** | 최종설계 Gate, 공식 제품률 자동 승인 아님 |
| [해총 hub](https://github.com/hibi89/hackathon-command-center-2026) | [#43523793011](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43523793011) (23:00:31 UTC) | **SUCCESS / 1 job 성공** | App 설치 토큰 생성·registry unit 검사·읽기 수집 및 스냅샷 갱신 실행 |
| [UGREEN](https://github.com/hibi89/hibi89-ugreen-nas-hackathon) | [#43522003442](https://github.com/hibi89/hibi89-ugreen-nas-hackathon/actions/runs/43522003442) (22:46:35 UTC) | **SUCCESS / 2 jobs** | 기존 공개 저장소의 Linux/Windows 검증 증거. 17개 신규 공개 전환에 따른 복구 증거로 계산하지 않음 |

- 전환 이전/전환 중 `Freelancer` [#43519727755](https://github.com/hibi89/Freelancer/actions/runs/43519727755), `data2web_studio` [#43520778342](https://github.com/hibi89/data2web_studio/actions/runs/43520778342) 등 `failure` run은 있었으나 정확한 실패 원인과 GitHub Billing 청구 차단 내역은 이 감사에서 **미확인**. 신규 run 성공은 실제 runner 가동 증거이며 **계정 결제 한도 표시가 해제되었다는 증명은 아님**.
- 모든 35개 저장소에서 동일 시점 새 run을 수행·성공 확인하지 않았다. 일부 저장소는 workflows 자체가 없거나 오래된 run만 확인됨.
- PUBLIC 저장소의 표준 GitHub-hosted runner 실행은 공식 정책상 무료. larger runners, Actions storage, 사용자 계정의 과금 제약은 별도 점검. 추가 비용 지출은 승인되지 않았고 실행하지 않았다.

## 3. 해총 GitHub App 관측 확인

- 중앙 [sync #43523793011](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43523793011) `SUCCESS`, 실제 `sync` job의 **8개 Step 모두 SUCCESS**.
- `kmong-productization/data/kmong_hub_auto_observations.json` 원격 재조회(확인 당시 브랜치 HEAD `64e824e22c79450bae8695ece15c972dbf24fdf2`): **35 repositories / 80 refs / 29 products linked / 29 present / 0 missing / 0 unlinked / fingerprint alert 0**.
- 이는 관측+원장 갱신 결과다. Vercel Production SHA 및 외부 실제 신규 Webhook E2E는 이전대로 미검증이다.

## 4. 파일경로 기반 공개 보안 감사 — 80 refs

- **기본 브랜치 `main` 35개**의 Git tree 전체 파일명 조회; 각 tree `truncated=false`.
- **추적 작업 브랜치 45개**는 중앙 최신 관측 JSON의 `work_branches[].head_sha`와 Git tree 조회로 일괄 검사; 각 tree `truncated=false`. 관측 SHA 이후 변경된 ref와 **레지스트리 밖 브랜치**는 이 범위에 포함되지 않는다.
- 검사 규칙: `.env` 계열(단 `.env.example` 제외), `.pem`/`.p12`/`.pfx`/`.p8`/`.key`, `id_rsa`/`id_ed25519`, `credentials.json`/`secret.json`, `.ssh`/`.aws` 등 전형적인 민감 파일 *이름*.
- **이 패턴과 일치하는 파일 경로 0건**. 하지만 **파일 내용의 하드코딩 토큰, 테스트 fixture 속 실제 키, 과거 커밋/기타 refs, PR, 릴리스/Actions 로그/아티팩트, LFS, Wiki, 서브모듈**은 이 검사만으로 탐지 불가. `no secrets` 결론을 내리지 않는다.
- GitHub Code Search `user:hibi89` 대상으로 `.env`/`credentials.json`/`AKIA` 3개 조회 결과 `total=0`이었지만 `incomplete_results=true`로 확인되어 **유효한 무검출 증거로 인정하지 않음**.
- GitHub `secret-scanning/alerts` API는 연결 GitHub 조회 도구에서 **지원하지 않는 URL(400)**로 거절되어 실제 경고 수/해결상태 **미검증**.

### 공개 원본 재검토 후보 (내용 무열람)

| 저장소/참조 | 경로(파일명 메타데이터) | 크기 또는 범위 | 판정 |
|---|---|---|---|
| `gongbaek-sanggwon@main` | `판매자료/크몽_최종등록_20261017/KMONG_840642_FINAL_CORRECTED_247_20261017.zip` | 1,061,871 bytes | 판매용 ZIP, 고객 데이터·재배포권·개인정보 검토 **필요**, 실제 내용 미열람 |
| `gongbaek-sanggwon@main` | `설계/05_ABC_분류_작업표.csv` | 152,947 bytes | 상업용 데이터인지 확인 필요, 실제 내용 미열람 |
| `HAE@feature/axflow-mvp` | `apps/ax-flow/HAE-Windows-offline.zip` | 패키지 파일 존재 | 배포 바이너리/내부 자료 혼입 여부 확인 필요, 실제 내용 미열람 |
| `ai-code-checker@main` 및 추적 브랜치 | `assets/pilot-safe.zip`, `assets/pilot-vulnerable.zip` | 검사 시제품 아카이브 | 이름상 테스트용이나 실제 데이터 배제 증명은 아직 없음 |

## 5. 브랜치 보호·공개 설정 영향

- 17개 신규 공개 저장소 전체의 `GET /repos/{owner}/{repo}/rulesets` 읽기 성공: **반환된 Ruleset 목록 0/17**. 해당 API의 리스트에 보이는 Ruleset이 없었다는 의미이며 저장소 전체가 아무 보호도 없다는 의미가 아님.
- 별도 `branches/main/protection` 조회는 `Freelancer`, `data2web_studio` 두 저장소에서 **403 Resource not accessible by integration**. Branch Protection 유무는 **미검증**.
- GitHub 공식 문서에 따르면 private→public 변환 시 **모든 Push Ruleset이 비활성화**되며 **기존 Actions 이력/로그도 모두 공개**된다. 기존 정책 재확인 및 필요 시 재활성화는 사용자 사전 승인 대상으로 보류.

## 6. 실행하지 않은 사항과 다음 우선순위

- `P0` **보안 위험:** 과거 Git 이력·레지스트리 외 브랜치·과거 Actions 로그/아티팩트/릴리스·LFS의 키/고객정보 및 재배포권 전수 감사. GitHub 네이티브 Secret Scanning 경고 화면은 계정 관리자 접근으로 확인. 실제 토큰 발견 시 원문을 보고서에 옮기지 않고 소유자에게 회전/폐기를 요청한다.
- `P1` **운영 보호:** 17개 repo Ruleset/Branch Protection 현행 정책 계정 화면 대조, 필수 체크/PR 승인·보안 변경은 사용자 별도 승인을 받은 뒤에만 조치.
- `P1` **Actions:** 이후 새 SHA에서 다시 실행된 표준 runner 성공/FAIL의 원인을 저장소별 검증, 35개 모두 성공했다고 전수 인정 금지. Billing 한도 표시는 GitHub 사용자 계정 Billing UI 직접 확인 필요.
- `P2` **App 운영:** Source Auditor/Dispatcher 실수집·중복/취소·일일 cron과 Vercel Webhook 별도 확인. 개인키·토큰·Vercel/도메인/설치권한을 자동 변경하지 않는다.
- 제품 공식 최종완성률은 사용자 승인 최종설계 100점 기준 그대로 **29/29 UNASSESSED**, 과거 잠정 수치·`[작업중]`·`RELEASE HOLD`·등록완료 기록 전부 보존.

**미구현/미검증을 분리한 본 감사는 전량 읽기 조회의 결과이며, 사용자의 Public 전환 결정을 되돌리거나 판매·권한/보안을 임의 변경하지 않았다.**
