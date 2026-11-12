> **2026-11-12 KST — Factory W1 VERIFY 경로 보안 개선, 82% 유지:** Private [Factory SHA `10b068b77cfc`](https://github.com/hibi89/factory-ax-ecosystem/commit/10b068b77cfc204c90de49b41736b851dc778c51)에서 출력/보고서 검증/승인 spec/백업·복원 경로의 **전체 상위 폴더**에 대해 심볼릭 링크·Windows reparse 지점을 `lstat`으로 거부하도록 변경하고 부정 테스트 6개 추가. Linux Python3.13 독립 테스트 파일 6개(15+24+4+4+29+54) **130 PASS/0 FAIL/0 SKIP**, `compileall` 및 독립 unsigned `.pyz` 합성 4역할→검수→백업→복원→검증 PASS, Linux 실 Tk/Xvfb GUI PASS. 전체 통합 1회 실행은 명령 제한으로 결과 확정 불가였으며 **분리된 130개 완료 실행만 PASS로 계수**. 실제 Windows NTFS/junction/ACL/PowerShell/GUI 및 Actions(0회) 미검증, 수동 실행+계정 예산 확인이 필요. 파일 안전성 체크는 race-free 보증이 아닌 사전점검. **VERIFY 82% 잠정 / 85 미달, Factory 생태계 전체 미산정, RELEASE HOLD**, 기존 크몽 활성16종 평균·분모 변동 없음. [검증·인수 문서](https://github.com/hibi89/factory-ax-ecosystem/blob/feature/data-verify/docs/VERIFY_82_PATH_ANCESTOR_QA_20261112.md).

> **2026-11-12 KST — Factory W1 VERIFY JSON 형식 오류 안전 차단 보강, 82% 유지:** [Factory 기능/인수인계 SHA 7ac39e80](https://github.com/hibi89/factory-ax-ecosystem/commit/7ac39e8009e3c2312e1f2b616ec66f0d1d237794) 원격 반영. 입력 승인 명세 `[]`, 보고 결과/영수증·백업 메타의 비객체/숫자 형식이 Python 추적 예외로 새어 나가지 않도록 `BLOCKED`·종료3 처리 강화. CLI 부정 4건 포함 **Linux Python3.13.5 전체 124 PASS/0 FAIL/0 SKIP**, 구문 검사 및 .pyz 패키지 무결성 PASS. 초기 실행 래퍼 시간 제한 후 별도 상세 테스트 로그 `Ran 124 tests in 34.928s / OK` 확인. GitHub Actions 수동-only 등록 완료됐지만 **실행 0건**, Windows 실기기·GitHub hosted Windows CI·Actions 요금/남은 무료 잔액·실고객/라이선스 **미검증**. 최초 W1 VERIFY **82% 잠정 유지, 85% 미달 / 전체 Factory Ecosystem 미산정 / RELEASE HOLD**. 기존 크몽 활성16종 및 평균/분모 변경 없음. [증거 문서](https://github.com/hibi89/factory-ax-ecosystem/blob/feature/data-verify/docs/VERIFY_82_MALFORMED_FAILCLOSED_20261112.md).

> **2026-11-12 KST — Factory VERIFY 수동 Windows/Linux CI 등록 승인 반영, 82% 유지:** 사용자 승인하에 [Factory `main` 등록/인수인계 SHA a94a36b0](https://github.com/hibi89/factory-ax-ecosystem/commit/a94a36b0547fb34e8a7ef2216024e9f9b390ef64) 와 [`feature/data-verify` 검증/인수인계 SHA 001e9f2f](https://github.com/hibi89/factory-ax-ecosystem/commit/001e9f2f5c3c14a4904cfda90c64aa8835a13d6c) 원격 반영. `.github/workflows/verify-owner-qa.yml`은 `workflow_dispatch` 전용, 읽기 권한만 허용, feature 브랜치 이외 작업 스킵, 작업당 12분 제한 및 동시 실행 취소. 기본 `main`에 **실행 파일 등록만** 했으며 제품 기능 코드는 병합하지 않음. 로컬 Python3.13.5 **120 PASS / 0 FAIL / 0 SKIP**, compileall, 워크플로 정적 형식 검증 PASS. GitHub Actions 실행 기록 **0건** 확인, 계정 잔여 사용량·과금 제한·Windows 실행 **미확인**. 연결된 GitHub 도구에서 계정 청구 사용량 조회·워크플로 dispatch 기능 제공되지 않아 무단 유료/보안 변경 없이 정지. 사용자는 GitHub `Settings → Billing & Licensing`에서 잔여 포함 사용량과 `Budgets and alerts` 지출 중단을 확인한 뒤 Actions 화면에서 **Branch `feature/data-verify`** 지정해 수동 실행해야 함. **VERIFY 82% 잠정 / 85% 미충족 / Factory 생태계 전체 미산정 / RELEASE HOLD**. 기존 활성 크몽16종 총점·분모·평균은 불변.

> **2026-11-12 KST — Factory AX VERIFY 백업 경합 방어 개선, 82% 잠정 유지:** [Factory 기능 SHA 0c3f1cb9](https://github.com/hibi89/factory-ax-ecosystem/commit/0c3f1cb9d610ae90a7d1f132a985e7636becfca1). 검증 완료된 5개 보고서 파일을 ZIP으로 읽는 도중 소스가 바뀌어도 백업 성공으로 오판하던 TOCTOU 위험 보강. 백업 시작 시 영수증 SHA와 개별 파일·원본 매니페스트를 독립 재검사, ZIP 완료 후 원본 재검증, 실패시 본인 생성 임시 아카이브만 정리. Linux3.13.5 **120/120 PASS, 0 FAIL/0 SKIP**(동시 변경 회귀 2건 신규), compileall·재현 .pyz/manifest·실 Linux Xvfb/Tk GUI PASS. 원본 소스/기존 main 보호. **Windows 실제 CMD/NTFS/Defender, Actions CI 0회, 고객 권리 미검증**, GitHub 수동 workflow 기본 브랜치 등록/사설 러너 과금 승인 필요. **VERIFY 82% 잠정 / 85 미달 / RELEASE HOLD**, Factory 전체 UNASSESSED, 크몽 활성16종 평균85.5625% 유지. [검증 근거](https://github.com/hibi89/factory-ax-ecosystem/blob/feature/data-verify/docs/VERIFY_82_BACKUP_CAPTURE_QA_20261112.md).

> **2026-11-12 KST — Factory AX VERIFY 85 목표 후속 Windows 종료코드 안전성 수정, 82% 잠정 유지:** [Factory 코드 커밋 f687b4af](https://github.com/hibi89/factory-ax-ecosystem/commit/f687b4affb0f973534734965d98d3d3b70dfd91c). Windows CMD `%errorlevel%`이 괄호 블록에서 조기 치환되어 BLOCKED=3을 성공=0으로 오판할 위험 제거; `goto use_python` 분기 및 별도 `exit /b %errorlevel%` 도입. 정적 회귀 테스트 추가, 실제 Windows CMD가 오류3과 기존 SHA 불변을 보장하는 수동 CI·PowerShell 검증 시나리오 준비. Linux Python3.13.5 전체 **118/118 PASS, 0 FAIL/0 SKIP**, 컴파일·재현 패키지·실제 Tk/Xvfb 합성 GUI PASS. **GitHub Actions 0회** 및 실제 Windows·NTFS·Defender **미검증**; GitHub 공식 요구상 `workflow_dispatch`는 기본 브랜치에 워크플로 파일이 있어야 수동 실행 가능하지만 현재 기능 브랜치에만 있음. 남은 GitHub Actions 잔여 무료 사용량/지출 한도 미확인, 따라서 메인 브랜치 변경·요금 발생 가능한 CI 실행은 무단 수행 안 함. **VERIFY 82% 잠정, 85% 미달 / Factory 전체 미산정 / RELEASE HOLD**, 활성 크몽16종 평균85.5625%와 분모 불변. [상세 근거](https://github.com/hibi89/factory-ax-ecosystem/blob/feature/data-verify/docs/VERIFY_82_WINDOWS_LAUNCHER_QA_20261112.md).

> **2026-11-12 KST — Factory AX VERIFY W1 85 목표 QA 후속, 82% 유지:** [기능 SHA eca3222e5588](https://github.com/hibi89/factory-ax-ecosystem/commit/eca3222e5588aac41c3fbf700192cd4d707d1323), [인수인계 SHA 84ed826aeba5](https://github.com/hibi89/factory-ax-ecosystem/commit/84ed826aeba5a9b438e91d865a546e67fb7014df). 기존 70% 제조 대사 및 W1-82 오프라인 납품 코어 보존. 백업 생성 중 다른 프로세스의 ZIP 삭제 가능 경합 수정·두 회귀 테스트 추가, 진짜 Linux Xvfb Tk 화면에서 GUI 합성 OK/중복 BLOCKED 버튼 2회 및 취소 경로 안전 PASS, Windows 원클릭 합성 점검 PowerShell 스크립트와 수동-only Ubuntu/Windows CI 절차 보강. Linux Python3.13.5 **117 PASS/0 FAIL/0 SKIP**, compileall·합성 4파일→보고→백업/복구→검증·패키지 무결성 PASS. **실 Windows/NTFS/PS5.1/Defender, GitHub Actions CI(0회), 고객·라이선스 여전히 미검증**. 따라서 **VERIFY 82% 잠정, 85% 미달 / RELEASE HOLD**; Factory 전체 미산정, 기존 활성16종 1369%p·평균85.5625%·16/16≥85 수치·분모 불변. [추가 근거](https://github.com/hibi89/factory-ax-ecosystem/blob/feature/data-verify/docs/VERIFY_82_QA_NATIVE_GATES_20261112.md).

> **2026-11-12 KST — Factory AX VERIFY W1 85% 목표 개발, 실제 82% 잠정 / 85 인수 미충족:** Private [기능 SHA 06a64f9c84ae](https://github.com/hibi89/factory-ax-ecosystem/commit/06a64f9c84aef37661423ec6dde49c2c12359b65) 원격 13파일 반영 확인. 기존 70% 발주→생산→검사→출하 대사 보존. 독립 Python 오프라인 후보에 원본 SHA 재검사, 신규 보고 폴더/완료 표식, SHA 영수증/독립검증, 수동 백업·복구, Tkinter GUI 코드, 재현 가능한 .pyz 및 Windows CMD QA 후보, 권리 인벤토리 추가. Linux 합성 **115 PASS / 0 FAIL / 0 SKIP**, compileall/패키지 E2E/백업·변조 검증 PASS. 실제 Windows GUI/NTFS/한글경로/Defender·호스티드 GitHub CI·실고객·라이선스 인증은 **미검증**. CI 워크플로는 수동 실행 전용이며 실행하지 않음. 따라서 **VERIFY 82% 잠정(70→82), 85% NOT ACHIEVED / RELEASE HOLD**. Factory AX Ecosystem 전체 UNASSESSED, W2~W4 미구현, 크몽 활성 16종 개별 점수·평균·분모 불변. [근거/남은 인수조건](https://github.com/hibi89/factory-ax-ecosystem/blob/feature/data-verify/docs/VERIFY_85_OWNER_CANDIDATE_20261112.md).  > **2026-11-12 KST — Factory AX VERIFY W1 70% 잠정 엔지니어링 최신화:** Private [Factory 기능 커밋 c324158c](https://github.com/hibi89/factory-ax-ecosystem/commit/c324158c54753516aafba5f2aad85a09b277061a) 최신 기능 HEAD 직접 검증. 기존 W1-50 원본 보존 + 발주→생산(1:N·재작업)→검사(PASS/FAIL/REVIEW)→출하(분할·반품) 연결, 품목/LOT·단위·Decimal·시간창·날짜별 누적/동일일 시각 불명 보류, 원본 SHA+행 근거, 안전 오프라인 공급자 정책 **DRAFT** 화면 구현. Linux Python3.13.5 합성 **87/87 PASS, 0 FAIL/0 SKIP** + compileall + CSV4종 CLI OK, Chromium 주입 화면 3 PASS/JS오류0/요청0; Windows 직접 file://는 브라우저 정책 차단으로 NOT VERIFIED. 기능 소스 Git blob `d223747b600958c142f80ac7563c0fb2c4dcbf4a`/reconcile `50087c130b96a6f47451c5dd062dd027d9a7cc60`/테스트 `734e4e1932a2ea67f21e88b38e2a97c238c06765` 로컬 파일 정확 일치. **첫 제품 VERIFY 70% 잠정**, 전체 Factory AX Ecosystem **UNASSESSED**, Windows/실고객/CI/원천 PREP·EAI golden/라이선스/출시 **미검증 RELEASE HOLD**. 기존 크몽 활성 **16종 1369%p/평균85.5625%/16종 모두85% 이상** 수치·분모 불변, 신규 후보 별도. [범위/증거](https://github.com/hibi89/factory-ax-ecosystem/blob/feature/data-verify/docs/VERIFY_70_EVIDENCE_20261112.md).

> **2026-11-12 KST — Factory AX VERIFY W1 50% 잠정 엔지니어링 달성 (신규 크몽 육성 후보, 활성16종 외):** 원본 Private [feature/data-verify 기능 커밋](https://github.com/hibi89/factory-ax-ecosystem/commit/8007f82af7d07ec5d8938144038d4b419fa334dd) `8007f82af7d07ec5d8938144038d4b419fa334dd` GitHub 원격 HEAD 재확인, source Blob `dc4be03b682679211d16aed7c3efd6ac45c41f82`·tests `30e014751b2e8c7511d4493d3fde31749ed51d94` 테스트한 로컬 파일과 **정확히 일치**. 새 Python3.11 stdlib 비공개 로컬 코어: 발주·생산·검사·출하 4 승인형 CSV/제한 XLSX, profile·source SHA·행 근거, 누락·중복·단위/Decimal·주문참조·QC 5종 품질검사, OK/REVIEW_REQUIRED/BLOCKED, 새 전용 한국어 HTML/CSV/JSON 보고. Linux 합성 **54 PASS/0 FAIL/0 SKIP**, 컴파일 및 실 CSV4종 CLI OK, 원본 불변, 오염/변조/경로 거부 증거. **첫 상품 VERIFY의 50% 개발 단계만 잠정 인정**, PREP/EAI 원천 동등성·1:N/반품·Windows/실사용 고객·실 Excel·CI/상용 승인 **미검증**; **Factory AX Ecosystem 전체 완성률 UNASSESSED**, RELEASE HOLD. **기존 활성 크몽16종 합계 1369%p/평균85.5625%/16종 85% 이상 전부 불변**, FFAX/PREP/기타 육성 후보와 별도. [제품 검증 문서](https://github.com/hibi89/factory-ax-ecosystem/blob/feature/data-verify/docs/VERIFY_50_EVIDENCE_20261112.md).

# Factory AX Ecosystem — 크몽 상품화 신규 후보 / 최종 완성률 등록
> 2026-11-12 KST · 담당 Factory AX 총괄 · 기존 활성 16종에 합산하지 않는 **독립 육성 후보** · RELEASE HOLD

## 식별 / 검증 기준
- 비공개 신규 원천 저장소: [hibi89/factory-ax-ecosystem](https://github.com/hibi89/factory-ax-ecosystem), `main` 기준 커밋 `29b9653ccbc4bcd36a190f9e9d78954bcc4dae76`.
- 새 저장소 29개 설계·운영·보안·인수인계 문서와 10개 브랜치 확인. **문서와 브랜치가 제품 개발·검수 완료 증거는 아님.**
- 첫 제품: **Factory AX VERIFY**. 장기 사업: **Factory AX Ecosystem**. 이 둘의 분모와 100% 정의를 구분한다.

## 완성률 정본
| 평가 대상 | 2026-11-12 현재 | 목표와 이유 |
|---|---|---|
| **Factory AX VERIFY 최종 상품 완성률** | **82% 잠정 엔지니어링 (85 목표 미달)** | 기존 4단계 대사 유지, 수동 백업·복구, 신규 보고서/무결성 영수증, 로컬 Tkinter GUI 소스, .pyz/Windows CMD QA 후보. 실제 Windows·CI 미검증. |
| **신규 Factory AX 기능 구현/실행 검증** | **GitHub QA 코드 + Linux 합성 117 PASS** | Python3.13.5 117 PASS/0 FAIL/0 SKIP, compileall, 독립 .pyz 합성 CLI·백업·변조 거부 PASS. Windows/호스티드 CI/실고객/라이선스 미검증. |
| **첫 개발 목표** | **W1 82% 잠정 / 85% 미달** | Windows 실행 GUI·패키지, NTFS 보안·한글경로/복구·GitHub clean CI 및 사용 인수시험 필요. RELEASE HOLD. |
| **Factory AX Ecosystem 장기 최종 완성률** | **UNASSESSED (정식 미산정)** | W1→W4 완성, HAE·LA·보안 Guard·RAG·NAS/FILE·PC CARE·Code QA·Console 통합 및 고객 납품 검증이 최종 100% 범위. |
| 출고 상태 | **RELEASE HOLD** | 제품 코드·납품 설치·고객 성과·보안·권리·상용 판매 미검증. |

## 상품화 사업 모델
- 중소 제조업체에 **표준 제품 + 제한된 고객 맞춤 설정/설치/검수/인수**를 공급하는 납품형. 일반 고객에게 SMAX² SELF 프로그램의 직접 구축을 요구하지 않는다.
- **W1 진입:** 발주·생산·검사·출하의 CSV/XLSX 대사, 수량·LOT·키·누락·중복·부분 출하 규칙과 근거 보고. SMAX² 전체 플랫폼이 아닌 PREP의 데이터 계약/검증된 기술과 EAI 기능을 독립 검토 후 재사용.
- **W2 확장:** 승인된 사내 매뉴얼 검색과 NAS/SMB 파일 읽기 전용 검수.
- **W3 최종 비전:** HAE + Lightning Azent로 허가된 범위의 사내 AX 워크플로, 독립 정책 Guard 집행·SOVIA 감사·실행 기록·복구.
- **W4 보안/IT:** 일반 업무용 Windows PC CARE 수동/승인된 정기 읽기 검사, Code Checker 허가 코드 정적검수, 통합 관리자 콘솔. PLC/SCADA/OT 직접 제어·무인 수리 금지.
- 필수 클라우드/API 월 구독 0원은 **설계 목표**이며 실제 총운영비 0원·보안 100% 보장 아님.
- 가격 가설 (아직 유료 고객/원가·수요 검증 전): BASIC 249,000원 / 구축형 STANDARD 990,000원 / PRO 290만~500만 원.

## 크몽 전체 장부 보호
- 기존 활성 **16종의 상태/점수·합계·평균·분모는 그대로 유지**. 해총 최근 검증 기록 기준 16종 모두 **85% 이상 잠정 엔지니어링**, 합계 1369%p/평균 85.5625%.
- Factory AX는 아직 **1개 신규 별도 후보**. W2/3/4 모듈을 별도 3개 유료 상품으로 중복 추가하지 않음.
- 기존 PREP/FFAX/BID AX/FlowPilot Universal/WORKNOVA Desk 및 다른 기술 후보와 분리. 중복 계산·다른 프로젝트 점수 대입 금지.
- 현시점 해총 연동은 수동 문서 기록이며 Factory 원본과 자동 동기화되지 않음.

## 다음 작업
1. Factory `feature/data-verify` 에서 최종 설계 문서/원천 소스와 권리·버전 확인.
2. 제조업 4종 합성 입력/독립 정답 oracle와 PREP 호환 계약을 실제 코드·테스트로 구현.
3. EAI 및 PREP 권리·동등성 검증 후 순차적으로 소스 SHA·테스트 PASS/FAIL/SKIP·실 Windows·보안·출시 위험을 분리 기록.
4. 실제 VERIFY 개발 진척을 **인수 조건 검증 후** 70→85→95→100 단계별로 갱신. 장기 생태계 전체 진척도 별도 산정.
5. 신규 상용 공개·코드 원본 복사/변경·실고객 자료 반출·외부 API·유료 CI·권한 보안 변경은 별도 승인 전 금지.

## 근거
- [Factory AX 최종 설계도](https://github.com/hibi89/factory-ax-ecosystem/blob/main/docs/PRODUCT_BLUEPRINT.md) (Private)
- [Factory AX 100% 인수 매트릭스](https://github.com/hibi89/factory-ax-ecosystem/blob/main/docs/ACCEPTANCE_MATRIX.md) (Private)
- [Factory AX 인수인계](https://github.com/hibi89/factory-ax-ecosystem/blob/main/HANDOFF.md) (Private)
- 신규 Factory 제품 코드·테스트는 별도 Private 기능 브랜치에서 새로 구현하고 SHA로 검증; **Production·고객 설치·사용권·출시 승인 없음**.
