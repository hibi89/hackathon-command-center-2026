# REA_Web 원래 목적 복구 / DATA2WEB Studio 독립 분리 — 2026-11-12 KST

## 소유자 최종 결정
- 기존 `hibi89/REA_Web` = **웹사이트 분석·재구축**: 허가된 사이트 관찰, Fable5.1 분석, Astra P4 증거·기능 명세, 인간 승인, 고객 소유 데이터로 새 웹앱 재구축·검증.
- 신규 Private `hibi89/data2web_studio` = **표형 파일 → 로컬 독립 웹앱**: CSV·flat JSON 현행 Lite 기능을 독립 이관하고, Excel XLSX·TSV를 추가한다.
- 두 제품은 동일한 최종완성률을 공유할 수 없다. 데이터 기반 웹앱 생성은 REA_Web 본래 전 제품이 아니라 REA Pro의 일부이자 DATA2WEB의 기능 원본.

## 정확한 GitHub 정본
### REA_Web 원제품
- [원래 README](https://github.com/hibi89/REA_Web/blob/main/README.md), [최종 설계](https://github.com/hibi89/REA_Web/blob/main/docs/ORIGINAL_FINAL_DESIGN.md), [요구사항](https://github.com/hibi89/REA_Web/blob/main/REQUIREMENTS.md).
- [신규 개발 브랜치](https://github.com/hibi89/REA_Web/tree/feature/website-analysis-rebuild), 기존 Pro 부모 `feature/d27-windows-python-discovery@97b6e5cab7b8ffb4e1ee7f5e593021f4dac2598d`, 기존 `feature/orchestrator@46060b46`, Fable `import/fable51-bbe72c0@7e6f273b`, Astra partial `import/astra-p4-b3166b6@f044b66e`.
- 초기 역사 기능: CSV→FastAPI/SQLite 웹앱 + Fable 결과를 선택적 Astra 검토 보고서로 넣는 합성 CI 55 PASS; **원래 사이트 URL→Fable→Astra→사람 승인→새 웹앱 E2E 미검증**.
- **정식 최종상품률 UNASSESSED**; 원제품 필수 사이트 종단 수용증거 0건. 문서/기존 Pro source 존재만으로 95% 산정 금지. 배포/고객/권리 RELEASE HOLD.

### DATA2WEB Studio
- [신규 Private 저장소](https://github.com/hibi89/data2web_studio), [최종설계](https://github.com/hibi89/data2web_studio/blob/main/docs/FINAL_DESIGN.md), [요구사항](https://github.com/hibi89/data2web_studio/blob/main/REQUIREMENTS.md).
- 브랜치 `feature/lite-independent-migration`(CSV·JSON 원본 계약 동등성), `feature/xlsx-tsv-import`(안전 XLSX/TSV 파서); 현재 **문서·브랜치 초기화**, 독립 소스/테스트 미이관.
- **정식 최종상품률 UNASSESSED**; 신규 저장소 독립 실행 검증 0%, 첫 개발 단계 P50 후보. 과거 좁은 범위 Lite `hibi89/REA_Web@feature/lite-owner-delivery-p95-20261112` 기술95% 잠정은 **역사 근거**, 새 범위 최종율로 계산하지 않음.
- 기능 이관·licensing/NOTICE·실 Windows/고객 승인·상용 출시 RELEASE HOLD.

## 크몽 중앙 통계 처리
- 기존 활성 16개 상품에서 `REA_Web` 단일 구버전 95% 행을 **DATA2WEB Studio(미산정)**로 정정하고 원래 `REA_Web — 웹사이트 분석·재구축(미산정)`를 독립 행 추가해 **활성 제품 식별자 17개**로 관리한다.
- 신규 정본은 **15개 수치 표기/2개 미산정**. 이전 활성16종 평균·합계 및 Lite P95 포함 산식은 과거 기록으로 보존하고 현재 17개 전체의 숫자 평균으로 재사용하지 않는다. 타15개 점수·작업중 표식 보존.
- 분리 문서·브랜치 구성은 제품 구현 완성률 증거가 아니다. 사용자 새 목표를 임의로 95/100로 지정하지 않는다. 상업 승인 금지.
- 크몽 작업 표식 정책은 그대로: 실제 단계 개발 착수시 목표와 함께 [작업중]을 남기고 검증된 목표 달성 전 제거 금지. 이번 구분 정리는 설계/등록 작업이고, 향후 마이그레이션 E2E는 아직 시작하지 않았다.

## 다음 과제
1. DATA2WEB: 기존 Lite SHA·LICENSE와 기능 골든 비교 후 독립 CSV/JSON/HTML/ZIP 구현 및 Windows+Linux E2E 완료 시 첫 P50 검증; 다음 XLSX·TSV.
2. REA_Web: 기존 Pro/Fable/Astra 계약을 실제 소스 기준 비교하고, 허가된 로컬 웹 fixture의 관찰→Astra REVIEW/HOLD→Pro 앱 생성→Chromium E2E 신규 구현; 그때 P50 평가.
3. 실고객 원본/실사이트 접근/상업적 사용권/판매 GO는 사용자 승인 별도. 원본 데이터, Git 이력, 기존 배포·권한·API 키 변경 없음.

## 인계·검증
- 상태: **설계 및 브랜치 정렬**. 새로운 제품 코드 테스트 **NOT RUN**, 원본 GitHub 소스/기존 테스트 역사적 자료만 확인.
- GitHub 중앙 상태는 별도 최신 커밋 `STATUS.md`/`HANDOFF.md` 및 상품 표 참조.
- 갱신: 2026-11-12 KST.
