# 2026-11-13 KST — 크몽 Freelancer 5종 + 별도 후보 4종, 총 9종 최종완성률 정본

**정본:** `hibi89/hackathon-command-center-2026@kmong-productization`의 후보 관리 참고 문서. 최초 설계 전체를 100% 기준으로 하며, **코드/검증 없이 숫자 완성률을 추측하지 않는다.**
**핵심 규칙:** (a) 제품 내 기존 엔진 진척 ≠ 신규 조합 상품 완성률; (b) 로컬 P85 기능검증 ≠ 정식 hosted CI 게이트 수용; (c) W1 부분 85% ≠ Factory AX 전체 85%; (d) `UNASSESSED`는 0% 또는 100%가 아님.
**이번 작업:** GitHub 원본 문서/HEAD/파일 트리 및 확인 가능한 Actions API 조회. **코드·테스트 신규 실행 0, CI 신규 사용 0, 고객/Production 0.**

## A. 5개 신규 브랜드 기업용 상품 — 모두 설계 완료, 최종상품률 미산정

| 상품명(내부 브랜드) | Freelancer 기획 브랜치(정확 HEAD) | 기반 기술·원본 기술의 과거 상태 | **신규 결합 상품 최종완성률** | 출고 |
|---|---|---|---|---|
| **AZENTFLOW AX** | `hibi89/Freelancer@product/hae-la-automation` `a578aee2300ae053bafe5cdaf1dd8e23385ff47b` | HAE+Lightning Azent+DBVORA; HAE 내부 85% 잠정, 전체 Python CI 2 FAIL/패키지 parity 미해결 | **UNASSESSED** (기업 패키지/고객 통합 기능·테스트 미실행) | HOLD |
| **CITEVAULT AX** | `hibi89/Freelancer@product/rag-enterprise-knowledge` `acf4936670bf1205f648d0dff5ca7e48b62fa83a` | RAG Studio+SMAX²/PREP+SQL/검색; RAG 원본 엔지니어링 95% 잠정 | **UNASSESSED** (기업 IAM/실 데이터·모델/납품 확장 미실행) | HOLD |
| **SITECRAFT AX [작업중]** | `Freelancer@product/rea-website-rebuild` docs `6e94d0066cbc80e91fed28b3358b36fc76235515`; `REA_Web@feature/sitecraft-ax-p85-20261113` code `a3f31c4c676fb28c2ddded052f9cd0a0942370ad` docs `a59d5279325e35c0fc65e81c36c7f74e21cbb0b9` | 독립 P85 합성 3사이트×desktop/mobile×3연속동작 실 Chromium 18전이 + Astra observed/digest→Fable static→Pro 새 앱 브라우저 비교; PNG48 RGB차이24, atomic 생성/보안 거부; [CI #43382914205](https://github.com/hibi89/REA_Web/actions/runs/43382914205) Ubuntu·Windows 각 116PASS/0FAIL/1WARN 2/2 SUCCESS | **공식 UNASSESSED** (P85 합성 기술 게이트 ≠ 사용자 전체 최종설계 공식 85%, 실제 고객 승인/권리/운영 인수 미실행) | RELEASE HOLD |
| **PROOFQA AX** | `hibi89/Freelancer@product/proofqa-ax-delivery-audit` `54b718f5d5520fae912d1fcc2e70a87ebd8f173c` | AI Code Checker 기존 기술 P95 잠정+Graphify+agent-browser+Cloudflare 감사 방법론 | **UNASSESSED** (신규 외부 기술 통합·독립 보안/브라우저 검증 0회) | HOLD |
| **ONTOINSIGHT AX** | `hibi89/Freelancer@product/ontoinsight-ax-data-analytics` `afda6eac0802d50cbcd44eb0b99d3daeffbf0922` | AI AutoML Analyst 기존 P95 잠정+NVIDIA Auto Ontology **개념**+선택 PREP/SMAX² | **UNASSESSED** (새 Excel·다중 파일·온톨로지/ML 누수 검증 0회) | HOLD |

- 다섯 상품의 확정된 기술/기능·출고 범위·100% 달성 기준은 각 `Freelancer` 브랜치 `docs/FINAL_BLUEPRINT.md`와 `docs/ACCEPTANCE_AND_ROADMAP.md`를 따름. [기획 허브 색인](https://github.com/hibi89/Freelancer/blob/main/docs/PRODUCT_INDEX.md).
- 이 5개는 **기존 HAE/RAG/REA/Code Checker/AutoML 개별 완성률 표의 중복 행으로 세지 않는다.** 신규 패키지의 개발률은 원본 대비 실제 통합 범위/고객 검증 evidence가 확보될 때 재산정.
- 내부 상품명은 상표/동명·도메인 권리 검토 전 대외 상품 등록 명칭 확정 아님.

## B. 스크린샷에서 지정한 4개 별도 프로젝트 — 최신 GitHub 재평가

| 프로젝트 | 정본 저장소 / 현재 브랜치 HEAD | 확인된 증거 / 경계 | **최종상품 완성률** | 독립 단계·출시 |
|---|---|---|---|---|
| **DATA2WEB Studio** | `hibi89/data2web_studio@main 01c9cfe0a6b4631d5546237997d407e53b35e2cd` / `feature/lite-independent-migration 1eb76e75070215fa7060bf6a2639e6838725163d` / `feature/xlsx-tsv-import db749750b65c4a3ebaf50b70ce5e1ace1af689c2` | 각 7~8개 blob **전부 문서**; 독립 source/CLI/테스트 없음. 구 REA Lite CSV/JSON 95%는 다른 코드/범위. 최종 R01–R33 신상품 전체에 승계 불가 | **UNASSESSED** | 독립 실행 코드 검증 **0%**, P50 미착수 / HOLD |
| **PREP** | `hibi89/prep@feature/core-extraction b8a637e824fc5b1ac63d31aaf188e9821039b49d`; 정확 기능 검증 SHA `a4c71258851af4b0d8540202f36c84c1438ad9e6` | Native Linux Node22.16 `npm test` **150/150 PASS**, no-network **150/150 PASS**, pack/check/SDK·CLI/HTML·receipt/오프라인 설치 성공(원본 문서 기준). 독립 PREP 방식 사용자 승인, SMAX 완전동등성 P85에서 제외. **GitHub-hosted CI 실행 0건** (Actions branch run query 0). Windows/소비자 P95·출시 P100 미완 | **UNASSESSED (정식 P85 보류)** | **P85 엔지니어링 로컬 완료**, CI/상용 미검증 / HOLD |
| **FFAX** | `hibi89/frontend-foundry-ax@feature/ffax-workbench-p85-20261112 35548e453dfaaf73042f61693beb3ebe28e75b4a`; 실제 기능 검증 `a76a962037b41d474699845378c2656e439f66f1` | `docs/ACCEPTANCE_MATRIX.md`의 AC01·02·03·05·06·07·08·10·11 합계 **78/100**. Node 105/105, Chromium 주입 30/30, 복구 9/9(원본 문서). AC04 live AI(14), AC09 공식 접근성/UX(6), AC12 CI(2) 미달. 현재 브랜치 Hosted run 0 | **78% 잠정** | P85 미달(목표 유지) / HOLD |
| **Factory AX (전체 생태계)** | `hibi89/factory-ax-ecosystem@feature/data-verify f9577bbc4c798534b36ed1243e122453b5e4a4a9`; Green CI 기능 SHA `b70a059175389bf53d87f8c90dc4f5bbe6a97986` | [Actions #43178583600](https://github.com/hibi89/factory-ax-ecosystem/actions/runs/43178583600) **완료 SUCCESS**, Windows Server2025·Ubuntu 각 **138 PASS/0 FAIL/0 SKIP**+합성 ZIP/CMD/Tk. **W1 CORE+VERIFY만 내부 85% 잠정**; W2 RAG/FILE, W3 HAE+LA/Guard, W4 엔드포인트/콘솔 통합 미구현. 실 구매자 Windows·권리/공급사 데이터 미검증 | **전체 UNASSESSED** | **W1만 85% 잠정**, 제품 P100·출시 미달 / HOLD |

### 근거 문서
- [DATA2WEB 설계](https://github.com/hibi89/data2web_studio/blob/main/docs/FINAL_DESIGN.md), [원래 제품과 분리 감사](REA_WEB_DATA2WEB_PRODUCT_SPLIT_20261112.md).
- [PREP P85 게이트 감사](https://github.com/hibi89/prep/blob/feature/core-extraction/docs/P85_GATE_AUDIT_20261112.md), [PREP STATUS](https://github.com/hibi89/prep/blob/feature/core-extraction/STATUS.md).
- [FFAX 100점 수용표](https://github.com/hibi89/frontend-foundry-ax/blob/feature/ffax-workbench-p85-20261112/docs/ACCEPTANCE_MATRIX.md), [로컬 증빙](https://github.com/hibi89/frontend-foundry-ax/blob/feature/ffax-workbench-p85-20261112/docs/FFAX_P85_LOCAL_PROJECT_RESTORE_20261112.md).
- [Factory W1 85% exact CI 증거](https://github.com/hibi89/factory-ax-ecosystem/blob/feature/data-verify/docs/VERIFY_85_CI_ACCEPTANCE_20261112.md), [전체 인수표](https://github.com/hibi89/factory-ax-ecosystem/blob/main/docs/ACCEPTANCE_MATRIX.md).

## C. 중앙 해총과 진척 집계 규칙

1. **본 9종은 `Freelancer` 패키지 5건과 독립 후보 4건의 묶음 정리다.** `DATA2WEB Studio`는 현행 17개 활성상품 표에도 이미 존재하므로 새 활성 행을 **중복 생성하지 않는다**. PREP/FFAX/Factory AX는 활성 17개 외 별도 후보 유지.
2. 기존 활성 제품 목록·수치·집계, KUODRA/REA/Astra 등의 `[작업중]` 및 `[사용자 개입 필요]` 표시를 변경하지 않는다. 5개 신규 기획 상품에 개발 착수 전 `[작업중]`을 가짜로 붙이지 않으며 각 신규 상품은 설계 완료·통합 개발 미착수로 표시한다.
3. **FFAX는 기존 사용자 목표 P85 미달 상태**(78%). 기존 `[작업중]` 표시의 유지/등록은 담당 원본 개발 정책에 따르며, 이 문서에서는 `P85 GOAL OPEN` 상태를 명시한다. 중단·채팅 종료를 이유로 목표 해제하지 않는다.
4. PREP의 85 로컬 기능검증은 숫자 최종상품 85 확정이 아니고 GitHub-hosted CI가 정본 수용 요구이므로 `UNASSESSED` 유지. 사용자 유료 runner 승인 없이 workflow dispatch 없음.
5. Factory AX는 **W1 85%**와 전체 **UNASSESSED**을 분리한다. 85%를 전체 진행률로 기재/평균 집계 금지.
6. SOURCE HEAD와 exact-tested commit SHA를 구분하며 매 갱신 최신 `HANDOFF→STATUS→AGENTS→REQUIREMENTS→실 소스` 순으로 비교한다.
7. 모든 프로젝트 **RELEASE HOLD / SALE NO-GO**. 상용 출고 기준: 실 고객 사용권·라이선스/NOTICE·배포물·실 Windows/브라우저·법적/과금·사람 인수 검증과 소유자 승인.
8. 이 갱신의 행위는 **GitHub 문서 동기화만**: 신규 기능·파일 이관·테스트 실행·배포·외부 AI/고객자료 전송·권한/계정/환경변수 변경 0회. 기존 HEAD를 복구 지점으로 기록한다.

## D. 다음 작업 우선순위(별도 사용자 개발 지시 시)
1. **DATA2WEB:** independent CSV/flatJSON→HTML/ZIP 실제 GitHub 소스·test, 첫 P50 증명 → XLSX/TSV 연결.
2. **PREP:** 사용자가 사전 승인하는 1회 GitHub-hosted CI의 exact SHA 실행·로그/결론으로 공식 P85 승인 여부 결정, 이후 Win/독립 소비자 P95.
3. **FFAX:** AC04 실제 승인형 AI React 생성, AC09 axe/UX 검증, AC12 GitHub-hosted CI의 남은 증거 채우기. 78→85 승격은 100점 수용표 충족 후.
4. **Factory:** W1 실제 Windows10/11/NTFS/권리·고객 검증 뒤 P95; 전체 플랫폼은 W2→W3→W4 실제 원본 제품·권한 통합을 개별 수락해야 최종완성률 산정.
5. **Freelancer 5종:** 각 상품 `FINAL_BLUEPRINT.md` 전체 요구/서브패키지 통합·고객형 기능·권리·CI·납품을 순서대로 실제 구현/재검수한 뒤 새로운 완성률 기록.

## E. 재현 범위/확인 시점
- 확인일: **2026-11-13 KST**. GitHub 저장소 공개 설정/브랜치 HEAD/원본 STATUS·HANDOFF·요구/최종설계·폴더 트리 직접 조회, Factory CI 단일 실행 REST 결과 확인 및 PREP/FFAX 해당 브랜치 CI 0건 확인.
- 기존 원본 문서의 테스트 수는 **과거 실행 증거**이며, 본 감사에서 신규 소프트웨어 테스트·제품 브라우저/Windows 실기기/고객데이터 실제 동작은 실행하지 않았다.
- 본 감사 추가는 `kmong-productization` **문서 전용 커밋**으로 수행. 최종 commit SHA·GitHub ref 일치는 저장 후 별도 재조회 확인.
