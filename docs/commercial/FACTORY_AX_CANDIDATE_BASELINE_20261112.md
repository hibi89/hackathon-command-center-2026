# Factory AX Ecosystem — 크몽 상품화 신규 후보 / 최종 완성률 등록
> 2026-11-12 KST · 담당 Factory AX 총괄 · 기존 활성 16종에 합산하지 않는 **독립 육성 후보** · RELEASE HOLD

## 식별 / 검증 기준
- 비공개 신규 원천 저장소: [hibi89/factory-ax-ecosystem](https://github.com/hibi89/factory-ax-ecosystem), `main` 기준 커밋 `29b9653ccbc4bcd36a190f9e9d78954bcc4dae76`.
- 새 저장소 29개 설계·운영·보안·인수인계 문서와 10개 브랜치 확인. **문서와 브랜치가 제품 개발·검수 완료 증거는 아님.**
- 첫 제품: **Factory AX VERIFY**. 장기 사업: **Factory AX Ecosystem**. 이 둘의 분모와 100% 정의를 구분한다.

## 완성률 정본
| 평가 대상 | 2026-11-12 현재 | 목표와 이유 |
|---|---|---|
| **Factory AX VERIFY 최종 상품 완성률** | **UNASSESSED (정식 미산정)** | 소스/통합 테스트·실 Windows·제조업 E2E가 없으므로 증거 없는 %를 만들지 않는다. |
| **신규 Factory AX 기능 구현/실행 검증** | **0건 확인** | 합성 데이터·첫 코어 구현과 검증 전. 기존 EAI/SMAX 등 기술 테스트는 Factory 테스트가 아니다. |
| **첫 개발 목표** | **50% 미달** | CORE/PREP 호환 매핑·EAI 검수·4파일 합성 fixture/정답 oracle/원본 SHA·보고서와 실제 자동 테스트 통과 후 기준 평가. |
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
3. EAI와 통합해 순차적으로 소스 SHA·테스트 PASS/FAIL/SKIP·실 Windows·보안·출시 위험을 분리 기록.
4. 실제 VERIFY 개발 진척을 **인수 조건 검증 후** 50→70→85→95→100 단계별로 갱신. 장기 생태계 전체 진척도 별도 산정.
5. 신규 상용 공개·코드 원본 복사/변경·실고객 자료 반출·외부 API·유료 CI·권한 보안 변경은 별도 승인 전 금지.

## 근거
- [Factory AX 최종 설계도](https://github.com/hibi89/factory-ax-ecosystem/blob/main/docs/PRODUCT_BLUEPRINT.md) (Private)
- [Factory AX 100% 인수 매트릭스](https://github.com/hibi89/factory-ax-ecosystem/blob/main/docs/ACCEPTANCE_MATRIX.md) (Private)
- [Factory AX 인수인계](https://github.com/hibi89/factory-ax-ecosystem/blob/main/HANDOFF.md) (Private)
- 이번 중앙 해총 작업은 **후보 등록 문서만**, 신규 코드/Factory 테스트·운영 Production 없음.
