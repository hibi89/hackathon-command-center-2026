# 해총 GitHub App × AI Code Checker 자동 코드검수 확장 최종설계 (승인된 미래 개발안)

- **설계 등록:** 2026-11-14 KST
- **상태:** `DESIGN_ONLY / IMPLEMENTATION_NOT_STARTED / RELEASE_HOLD`
- **소유자·총괄:** 사용자 / 해총. 제품 소스 수정은 각 담당 저장소·담당 브랜치에서 수행한다.
- **중앙 기준:** `hibi89/hackathon-command-center-2026@main`; 크몽 상품 상태 단일 정본은 추후 `kmong-productization`에서 설계·검증 후 확립
- **기존 자산:** 중앙 Source Auditor GitHub App(35 repos/80 refs), Dispatcher App(중앙 Actions만 쓰기), `kmong-hub-sync.yml`, 중앙 `data/kmong_hub_auto_observations.json`(관측만), `hibi89/ai-code-checker` 오프라인 v2
- **코드체커 최신 확인 참고:** `hibi89/ai-code-checker@main 37a360da884d1c372a3df76e71d180d57ffcf9c5` (설계 조회 기준; 생산용 배포/검증된 핀은 구현 시 별도 확정)
- **제약:** 추가 유료 결제 0원, 신규 유료 서비스·외부 AI API 기본 금지, 원본·판매/등록이력·기존 기능 보존, 소스나 개인정보의 외부 전송·권한 변경·Production 배포는 각각 별도 사전 승인

## 1. 사업 목적과 완료 정의

AI 담당자들이 각 GitHub 브랜치에 Push/PR을 올린 뒤 중앙 총괄은 **정확한 변경 SHA**를 기준으로 코드 정적 검수·보안·테스트·최종설계 추적·중복·상태충돌을 수집한다. 결과는 `PASS / FAIL / REVIEW / PARTIAL / NOT_RUN`으로 분리하고 근거와 한계를 제시한다. 자동 점수화, 자동 병합, 무단 수정, 공개 검수 결과에 비공개 원본 코드 삽입은 금지한다.

현재 구현된 것은 **35개 저장소·80개 추적 refs·29개 제품 링크의 읽기 관측과 중앙 스냅샷 갱신**이다. GitHub App → Code Checker 자동검수, 각 소스의 PR 체크, 자동 충돌 수정, 원장 상태 동기화는 아직 **미구현**이다. 기존 Vercel Production SHA/신규 Webhook 실연동도 **미검증**이다.

Code Checker 오프라인 v2는 `offline_core.py` 등으로 **코드 실행·Gemini·네트워크 호출 없는** 제한 정적 검사를 지원한다. README 기준 파일 200개/각 1 MiB/총 8 MiB 제한, Python AST 지원·타 언어는 제한 일반 규칙이며 `complete`는 분석 범위 처리 완료일 뿐 취약점 없음 보장이 아니다. Gemini v1(유료·전송 동의 별도)은 **비활성**으로 유지한다.

## 2. 설계 대안 비교 (무과금 전제)

| 항목 | A. 각 소스 저장소 내 신뢰된 Actions에서 검수, 중앙에는 요약만 | B. 중앙 Actions가 App으로 비공개 코드 읽어서 일괄 검수 |
|---|---|---|
| private 소스 유통 | 원 저장소의 격리 CI 외부로 원본 코드를 복제하지 않음 | 중앙 runner에 원본 소스가 복제됨 |
| 기존 권한 | 소스별 기본 `contents:read`의 제한 실행 가능; 중앙은 기존 Actions 읽기 | 기존 source App의 read 범위는 활용 가능하나 별도 cross-repo 원본 취급 |
| 설정/관리 | 최초 각 저장소 CI 템플릿 설치·버전 핀·회귀검증 필요 | 중앙 구현 집중, 소스별 준비는 줄어듦 |
| Action minutes | 소스별 사용, private 저장소 무료 할당량 주의 | 중앙 public 표준 runner를 활용할 여지; 소스 취급 위험·API 비용 증가 |
| 장애 경계 | 소스별 실패 격리·결과 재시도 용이 | 중앙 장애가 전체 검수를 막음 |
| 품질 통제 | 검사기와 이벤트 버전 고정, 소스별 허용 범위 | 35개 저장소의 언어/규모별 누락 관리 필요 |
| **선택** | **A 권고: 무유료·최소 권한·개인정보 보호 우선** | B 보류: private 소스 중앙 수집·권한 검토/승인 필요 |

장기적으로는 A의 경량 스캔 + 기존 중앙 App 관측을 결합한다. Code Checker가 모든 언어/취약점을 해결한다고 가정하지 않는다. 저장소별 GitHub Actions 사용량이 무료 한도에 접근하면 **자동 중지/검사 배치·빈도 축소 후 사용자에게 알림**하고, 과금 결제는 자동 승인하지 않는다. Public/Private Actions 무료 조건·실제 계정 과금 설정은 구현 전 다시 확인한다.

## 3. 권장 데이터 흐름과 트리거

```text
담당 AI -> 기존 repo/브랜치 commit 또는 PR
    -> 소스 repo 신뢰된 GitHub Actions (읽기 전용 checkout, 정확한 SHA 고정)
    -> pin된 오프라인 AI Code Checker 정적 스캔
    -> 대상별 커버리지 + 검수 결과 (비밀/코드 원문 제외)
    -> 소스 repo의 run/artifact/결과 로그
    -> 기존 Source Auditor App (repo/actions 읽기; 검증된 run만)
    -> 해총 중앙 관측 원장 (repo, ref, head SHA, run ID, checker SHA, 결과/시간/한계)
    -> 상태·설계 충돌 비교/알림/작업 담당자 반환 (첫 단계는 읽기·수동 검토)
```

1. **검수 트리거:** `pull_request`와 허용된 `push`만. 승인된 저장소/브랜치·최근 변경 파일 확인 후 표준 러너에서 경량 검사. 원본 `workflow_run`/브랜치 HMAC 식별을 무조건 신뢰하지 않고 run ID·head SHA·결과를 GitHub API로 재확인한다.
2. **스코프 확정:** `repository_full_name + base_sha + head_sha + checker_version + config_digest`의 고유 키. 같은 키는 중복 수집/중복 재실행 금지. `main`과 제품 feature는 분리 표시.
3. **입력 처리:** 기본 `offline_core`의 safe ZIP/파일/폴더 기능을 재사용하되 `.env`, 키, 토큰, 고객파일은 수집하지 않음. 대용량/미지원 언어/파일 제외는 `PARTIAL`로 표기. 어떤 소스파일도 CI 요약에 본문으로 쓰지 않는다.
4. **검증 단계:** ① Python AST/제한 정적 룰과 미지원 파일 ② 확정 테스트 명령·결과 로그 (별도 승인 후 신뢰 브랜치에서만 실행) ③ REQUIREMENTS/설계 ID→증거 SHA 매핑 ④ 보호 원본/회귀 변화·license NOTICE·보안·API 비용/권한 점검.
5. **중앙 저장:** 공개 허브에는 SHA, 파일 경로·규칙 ID·건수 같은 최소 메타데이터만 남긴다. private 코드 조각·스택트레이스 내 민감값·전체 검사 보고서/로그는 복사하지 않음. 상세 보고서는 원 저장소 접근 정책하에 보관.
6. **담당자 재작업:** 최초에는 검수 실패의 **읽기 전용 경고/작업 후보**만 생성한다. PR 코멘트/Checks 기록/담당자 통지 자동화는 추가 권한·사용자 승인 후 별도 단계.
7. **출시 Gate:** FAIL 또는 PARTIAL/NOT_RUN·미승인 최종설계·실고객/라이선스/보안 미검증은 출시 승인으로 오판하지 않는다. 내부 정적 검사 PASS만으로 최종완성률 85/95/100%를 인정하지 않는다.

## 4. 보안·공급망 및 격리

- **기본 권한:** 소스 repo의 `GITHUB_TOKEN: contents:read`; `persist-credentials: false`, 네트워크 egress/재사용 토큰 최소화. 검수 작업에서 소스 App 개인키·Dispatcher 개인키·Webhook secret 미주입.
- **검사기 신뢰:** 공개 Code Checker `main` 최신 코드를 무핀으로 내려받지 말고 review된 전체 SHA로 pin. GitHub Actions 자체도 검증된 정확 SHA pin을 권장한다. 설치형 추가 패키지/외부 API 기본 금지.
- **신뢰 경계:** 외부 PR/포크 코드는 임의 코드 실행·쉘 설치·테스트 스크립트 자동 실행 금지. 정적 분석 입력은 데이터로 취급; 최초 워크플로/검사기 실행은 **기본 브랜치의 신뢰된 정의**만 사용한다. 비신뢰 파일을 checkout할 때 symlink/서브모듈/대용량·path traversal/zip bomb 대응 필요.
- **프라이버시:** 보안 경고에 비밀 토큰 값 노출 금지. Public 중앙 레포에는 private 소스 경로조차 민감할 경우 해시 또는 비식별 규칙 코드로 대체. 민감정보 원문을 제3자 SaaS/LLM에 보내는 기능 미활성.
- **기존 App:** Source Auditor 읽기 전용·Dispatcher 중앙 Actions 쓰기 전용 유지. `checks:write`, `pull-requests:write` 등 권한 확대를 **이번 설계에서 수행하지 않음**. 자동 병합/배포/강제 push 금지.
- **비용:** 결제 0원 우선. Private Actions 사용량/실패 반복/동시성 폭증 감시. 매일 모든 변경을 무조건 재스캔하지 말고 SHA 기반 증분/주기적 재대조로 제한.

## 5. 최종설계/크몽 단일 원장과 연계

- 29개 원천 제품(`record_id`)과 19개 묶음 판매 서비스(`service_id`) 매핑 분리. 신규 제품·Freelancer 공유 브랜치를 1:1로 단정 금지.
- `[작업중]`, `[사용자 개입 필요]`, `검증 대기`, `RELEASE HOLD`, `등록완료`는 독립 상태 필드로 유지. **`[작업중]`는 실제 실시간 AI 실행 증거가 아님**.
- 판매 상품 `등록완료`는 실제 크몽 등록 링크/증거가 있을 때만 기록하며 영구 보존. 신규 코드 Push만으로 상태 해제·달성률 승인·등록완료 자동 표기 금지.
- 현존 `docs/audits/KMONG_16_CURRENT_20261111.md`, Freelancer 보조 등록부, STATUS/HANDOFF 문구 상충은 `제품ID+repo+branch+명시적 상태이벤트` **단일 정본** 도입 후 자동 파생 뷰로 정리하는 것이 선결 조건. 초기 데이터 이관은 수동 대조·스냅샷 백업·등록완료 보호 검증 후 사용자 승인.
- 공식 최종완성률은 원 사용자 확정 **최종설계 전체 100점 분모**, 요구 ID·기능 SHA·실시험·승인된 가중치로만 산정. 현재 29종 공식 UNASSESSED 이력을 임의 재산정하지 않는다.

## 6. 예외·실패 복구·중복 실행

- 검수 입력 미지원·서브모듈/용량 초과: `PARTIAL`, 검출 코드에 부정확한 보안 완료 표시 금지.
- GitHub API 403/429/5xx·Actions 취소·실행 시간 초과: `NOT_RUN/RETRY_PENDING`으로 기록, rate-limit 헤더 및 무료 CI 한도에 맞춘 제한된 재시도, 누락 run은 일일 read-only 보정 조회.
- 동일 SHA 재푸시/중복 webhook: idempotency key로 merge해 단일 결과 유지. 새로운 검사기 버전/구성 변경은 새 키로 검사하되 이전 결과는 이력 보존.
- 악성/변조 보고: GitHub run API에 있는 `repo+run_id+head_sha+workflow path+conclusion`과 소스 run의 서명/권한 범위를 재조회, 일치하지 않으면 `REVIEW` 및 자동 PASS 금지.
- 2회 반복 무진전 장애는 Stop & Pivot: 재현 최소 입력·원인 증거 기록 → (A) 저장소 내 오프라인 수동 검사 (B) 안전한 코드체커 CLI 아티팩트 (C) 설계 재검토 비교. 무료 정책 위반이면 중지.
- DB는 초기 불필요. 순환 관측 JSON을 쓰더라도 원본 등록이력과 달성 상태는 분리하며, 다중 담당자 덮어쓰기 충돌 시 compare-and-swap/원본 SHA를 사용해 fail closed한다.

## 7. 단계별 구현 순서와 승인 Gate

| 단계 | 산출물 / 증거 | 실행 조건 |
|---|---|---|
| **P0 (다음 작업)** | AI Code Checker 오프라인 CLI/exit-code/JSON 보고 포맷/출처 검수, 중앙 29제품 상태 단일 정본 구조 설계, 무료 quota 확인, 코드체커 테스트 | 외부 전송·새 권한·유료 API 없는 읽기 검토 |
| **P1** | 소스 repo 1개에서 신뢰된 워크플로 시범: 정확 SHA 정적 검사, PASS/FAIL/PARTIAL/NOT_RUN·파일 수·룰 ID만 출력, 부정 입력 테스트 | 원본 소스/설치/Actions 정책·사용자 승인 후 |
| **P2** | App의 기존 `actions:read`로 허용된 run 메타데이터 수집, 중앙 repo에 **메타데이터 전용** 비파괴 관측, 중복·누락 보정 테스트 | private run/아티팩트 내용 전송 여부 별도 승인 |
| **P3** | 선택된 저장소만 단계적으로 확대, 변경부·주기 보정·무료 CI 예산·경고·상태 충돌 감시, 기존 제품 원장과 안전 분리 | 실제 비용·API quota/보안·권한 증거 검증 |
| **P4** | 선택적 PR Checks·보호 규칙·담당자 자동 재작업·상용 Gate 연동 | Checks/PR 쓰기·브랜치 보호·배포/보안 변경은 **별도 명시 승인 필수** |

### 시범 필수 수용 시험

1. 신뢰된 branch의 정상 파일: Code Checker run과 SHA/설정/version 기록·결과 정확.
2. 악성 ZIP 경로탈출·symlink·고객 비밀파일: 차단/마스킹; 허브에 비밀값/원문 0.
3. 지원되지 않은 JS/TS·초과 파일: `PARTIAL`이지 자동 `PASS` 아님.
4. 동일 SHA 2회 webhook: 결과 1건, 변경된 head SHA는 재검토.
5. CI cancelled/403/timeout: `NOT_RUN` 또는 `REVIEW`; 성공 위조 불가.
6. Source Auditor의 비공개 읽기 권한/Dispatcher 중앙-only 권한 동일, 소스 repo·kmong 원장 원본 변경 0.
7. 29개 제품 ID·19개 서비스 ID와 등록완료/작업중/승인 가중치 보존.
8. 허가 없는 Vercel 새 프로젝트/Prod 배포·외부 AI/LLM 호출·결제 0.
9. 호스팅되는 결과 파일·UI·보안 경계에 민감정보가 남지 않는지 별도 검증.
10. GitHub Actions 결과 `run_id, head_sha, job, tests pass/fail/skip`·정확 repo SHA를 독립 재조회하여 증명.

## 8. 운영 인수인계

- **지금까지 완료:** 본 설계 문서의 GitHub 등록만. 기존 GitHub 중앙 observer 실행 검증 SHA `9400e1a6383a9a6bd85091ffb31165a0bc3160f9`, hub snapshot `29912c1605d3a6ab8ef5732ed6599b8fd8c7bcd7`, 관련 17 Node/27 Python 성공은 **기존 자동 수집 엔진**의 증거이며 Code Checker 연동 성공을 의미하지 않는다.
- **현재 미구현:** 소스 CI Code Checker 실행, App 중앙 검수 수집, 자동 상태 정본/충돌 방지, Checks 쓰기/PR 게이트, 고객/Production 검증.
- **보류:** Webhook/Vercel 생산 SHA 및 실신규브랜치 이벤트 미검증, 첫 scheduled job 기록 별도 확인 필요. 체크 실패를 서비스 장애로 단정하지 않는다.
- **예상 테스트 명령:** `python3 -B -m unittest discover -s tools/kmong_hub_sync -p 'test_*.py' -v`; Code Checker는 정확한 구현 버전에서 `python offline_core.py <approved-test-fixture>` 및 신뢰된 테스트만.
- **다음 담당자:** 이 문서 → 중앙 `HANDOFF.md`/`STATUS.md`/`AGENTS.md`/`REQUIREMENTS.md` → AI Code Checker `CODE_CHECKER_RESUME.md`/`HANDOFF.md`/`STATUS.md`/실소스 → 갱신된 repo/CI SHA → 비용·권한·원본·시험 범위 재점검.
- **수정 금지/승인사항:** 비밀키/토큰/환경변수·App 설치 권한·Vercel Production·판매등록·원본 코드·기존 점수/이력. 변경은 사용자 명시 승인 이후 별도 작업.
