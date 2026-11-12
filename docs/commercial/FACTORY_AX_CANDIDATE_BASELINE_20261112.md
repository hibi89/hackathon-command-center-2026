> **2026-11-12 KST — Factory AX VERIFY W1 70% 잠정 엔지니어링 최신화:** Private [Factory 기능 커밋 c324158c](https://github.com/hibi89/factory-ax-ecosystem/commit/c324158c54753516aafba5f2aad85a09b277061a) 최신 기능 HEAD 직접 검증. 기존 W1-50 원본 보존 + 발주→생산(1:N·재작업)→검사(PASS/FAIL/REVIEW)→출하(분할·반품) 연결, 품목/LOT·단위·Decimal·시간창·날짜별 누적/동일일 시각 불명 보류, 원본 SHA+행 근거, 안전 오프라인 공급자 정책 **DRAFT** 화면 구현. Linux Python3.13.5 합성 **87/87 PASS, 0 FAIL/0 SKIP** + compileall + CSV4종 CLI OK, Chromium 주입 화면 3 PASS/JS오류0/요청0; Windows 직접 file://는 브라우저 정책 차단으로 NOT VERIFIED. 기능 소스 Git blob `d223747b600958c142f80ac7563c0fb2c4dcbf4a`/reconcile `50087c130b96a6f47451c5dd062dd027d9a7cc60`/테스트 `734e4e1932a2ea67f21e88b38e2a97c238c06765` 로컬 파일 정확 일치. **첫 제품 VERIFY 70% 잠정**, 전체 Factory AX Ecosystem **UNASSESSED**, Windows/실고객/CI/원천 PREP·EAI golden/라이선스/출시 **미검증 RELEASE HOLD**. 기존 크몽 활성 **16종 1369%p/평균85.5625%/16종 모두85% 이상** 수치·분모 불변, 신규 후보 별도. [범위/증거](https://github.com/hibi89/factory-ax-ecosystem/blob/feature/data-verify/docs/VERIFY_70_EVIDENCE_20261112.md).

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
| **Factory AX VERIFY 최종 상품 완성률** | **70% 잠정 엔지니어링(W1 보수적 대사 범위)** | 승인형 CSV/제한 XLSX + 발주→생산→검사→출하 1:N/부분/LOT/반품·재작업·기간 대사, SHA/행 근거, source-minimal 보고. 원천 PREP/EAI 동등성·고객 Windows·상용인수 미검증. |
| **신규 Factory AX 기능 구현/실행 검증** | **GitHub 새 코어·87 합성 PASS** | Linux 로컬 87 PASS/0 FAIL, 실제 4종 합성 CLI OK, Chromium 동일 HTML 주입 3 PASS/외부요청0. 정확 Git blob 3개/현재 기능 HEAD 검증. GitHub Actions·Windows file://는 미검증. |
| **첫 개발 목표** | **W1-70 잠정 도달** | W1 50 기준 기능 유지 + 제조업 독립 합성 oracle 20+ 케이스와 보수적 날짜별 누적/단위·LOT·검사/출하, 오프라인 공급자 정책 DRAFT UI. 실제 사용·설치/보안·실고객 인수 기준은 W1-85 이후 게이트. |
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
