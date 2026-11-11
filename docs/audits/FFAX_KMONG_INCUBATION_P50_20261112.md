# FFAX 크몽 제품화 후보 — 50/100 개발 마일스톤 (2026-11-12 KST)

**분류:** 별도 개발 후보 / **기존 활성 16종 집계 미포함**. 현재 16종 목록은 `KMONG_16_CURRENT_20261111.md` 기준 원문 유지.

## 목적
FRONTEND FOUNDRY AX: 프론트엔드 자동 생성·시각 편집·브라우저 검수와 향후 기존 제품의 안전한 Git 통합 도구. 고객용 상용 프로그램으로 분류하기 전에 내부 제품 3종에서 재사용·효율을 검증한다. AI와 디자인 시스템을 합쳐 품질 향상/재작업 절감 가능성을 측정한다.

## 정확한 제품 원본
- Private: [`hibi89/frontend-foundry-ax`](https://github.com/hibi89/frontend-foundry-ax/tree/feature/ffax-workbench-p50-20261112)
- Branch: `feature/ffax-workbench-p50-20261112`
- Tested functional commit: [`e2d9355577e20cbe9d70d80f8bbb9a4263f2de08`](https://github.com/hibi89/frontend-foundry-ax/commit/e2d9355577e20cbe9d70d80f8bbb9a4263f2de08)
- Product docs HEAD: [`833804a076a3daf79a46773a34bb3b0db5cc2712`](https://github.com/hibi89/frontend-foundry-ax/commit/833804a076a3daf79a46773a34bb3b0db5cc2712)
- Main baseline: `191289d19f7eb6203a2a6beb5e8efbcf10bc844d` **미변경**
- [FFAX 원본 완성률 AC 표](https://github.com/hibi89/frontend-foundry-ax/blob/feature/ffax-workbench-p50-20261112/docs/ACCEPTANCE_MATRIX.md)
- [P50 검증 리포트](https://github.com/hibi89/frontend-foundry-ax/blob/feature/ffax-workbench-p50-20261112/docs/FFAX_P50_ENGINEERING_EVIDENCE_20261112.md)
- README에는 사용자 승인 콘셉트 WebP 포함, 원본 PNG와 구분.

## 개발 현황
기능: 자연어 입력의 **규칙 기반** 구조화 브리프/12개 시나리오, 서로 다른 디자인 2안, 13 UI 컴포넌트, 3개 테마, 마우스 컴포넌트 선택·순서·속성 변경·Undo/Redo, 로컬 참조 이미지 권한 확인→두 색상/레이아웃 대안→명시 승인, TSX 소스 초안 다운로드, UI 375/768/1440px 자체 QA.

**점수:** AC02 8 + AC03 12 + AC05 6 + AC06 12 + AC08 12 = **50/100점 잠정 엔지니어링 개발 범위**. 이 값은 정해진 100점 매트릭스 내부 게이트이며 실제 고객 납품·상품 출시에 대한 50% 확률이나 최종 승인 의미가 아니다. 나머지 AC01 8/AC04 14/AC07 12/AC09 6/AC10 5/AC11 3/AC12 2 = 50점, 미통과.

**검증:** Linux Node22.16 `npm test` 24 PASS, Chromium headless `set_content` 같은 JS/CSS/HTML 실제 조작 30 PASS, Node localhost GET200; Console/외부 Network 오류 0, overflow 오류 주입 탐지→복원 PASS. Chromium URL navigation은 실행환경 정책 `ERR_BLOCKED_BY_ADMINISTRATOR`로 불가. Playwright 실제 hosted URL·Windows Chrome/Edge·React runtime typecheck/build·실제 LLM 호출·기존 앱 API 계약 회귀·CI·Production 미검증. **RELEASE HOLD**.

## 다음 단계
1. 개발 브랜치 유지. 2종 샘플 React 앱을 승인된 데이터만으로 준비, 기존 정상 라우트/인증/API 회귀 우선.
2. 모델 어댑터/토큰/API 비용 상한과 외부 소스 전송은 사용자 사전 승인 후 추진.
3. 실제 React/TS build+렌더, GitHub read-only import, 안전한 diff/PR+복구, axe 및 Windows/실제 브라우저 URL 검증.
4. 내부 WORKNOVA/RAG/DBVORA 적용 시 **원본 브랜치·데이터·API 변경 금지**, 개별 승인 및 백업.
5. 상품화 범위 확정 전까지 기존 크몽16종과 합산 금지. 별도 신규 등록·분모 변경이 필요하면 사용자 승인 후.

## 크몽 본대장
2026-11-12 KST HEAD 기준 기존 활성16종 표기 총 **1254%p / 평균78.375% / 85이상8·미만8**, 별도 후보 FFAX 50점은 **분모/합계에서 제외**. SOVIA 다른 작업방 85 잠정 vs 표 75 불일치는 본 작업에서 임의 변경하지 않음.

## 보안·배포·인수인계
중앙 레포 **Public**에는 비공개 FFAX 코드·이미지 내부 바이너리·토큰·고객 데이터 없음. 상세 소스는 private FFAX에만 보존. No Vercel/Production/paid API, 판매 불가. 정상 기능이 있는 다른 제품 저장소 변경 없음. 다음 채팅에서 제품 HANDOFF→STATUS→AGENTS→REQUIREMENTS→ACCEPTANCE_MATRIX→실제 코드 순으로 확인하고 출시 게이트 통과 전 50점 이상의 추정치를 올리지 말 것.
