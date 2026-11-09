# SMAX² 45→50% 제품 진척 검증 요약 — 2026-11-10 KST

**범위:** `hibi89/SMAX@preprocessing` 개발 SHA `3190da505efcd55e7e83a1eabe994fbd8c9e5718`, 상태 문서 HEAD `3830cb276f560d58e8181ba384d9cbe64815737c`; 해총 `kmong-productization`의 크몽 활성 16종 상품 집계. 소유자의 목표인 SMAX² 최종상품 **50% 잠정**을 개발 기능 범위로 재평가. 전체 Native/Windows/판매 검수와 분리.

## 새 기능과 추정 배점

| 기능 | 기여 | 실제 동작·검증 범위 |
|---|---:|---|
| P5 다중 원본 SAFE batch | +2%p | 명시 소스 1–8개, SHA256 중복·혼합 주기 거부, 하나라도 HOLD 시 금액 전체 숨김, BigInt 합산. GitHub 실제 함수 V8 17 PASS/0 FAIL; 실제 P3/P4/P5 소스+진짜 SHA-256의 합성 CSV 2개 집계 순합 275.00. |
| P6 로컬 HTML owner-review | +1%p | 브라우저 전달용 무JavaScript/무CDN CSP 격리, 고객별 원문·개별 거래값 미포함, 위조·잘못된 금액 거부. 실제 렌더러 V8 14 PASS/0 FAIL. |
| P7 사용자가 열 선택할 수 있는 안내 | +2%p | 한국어·영어 날짜·채널·금액 후보 및 동점/누락 `AMBIGUOUS_MAPPING_REVIEW`, 자동 매핑·승인 금지. GitHub 소스/테스트 blob SHA와 Node22 스테이징 파일 SHA 일치: Native Node 28 PASS/0 FAIL (18 라이브러리, 10 CLI with CSV parser + reader test double); 원본 실제 CSV parser 연결 V8 9 PASS. |
| 합계 | **+5%p** | 전체 상품 잠정 **45→50%**, release QA 별개 |

## 검증 등급·실패 근거

- **Source-verified native:** P7 라이브러리 `self-column-suggest.mjs` blob `842264614544a0651edc9abc82a8201e229e591c`, CLI `self-column-suggest-cli.mjs` blob `2aca23c81698f841168b4f2792ff29413bc13c65`; 해당 테스트 2개 blob `fdc2e3814e417d17b38d8ab142537bfa2476a9a0`, `6f3d9c6c2982079d27f88018bd7ffeab884908df`. 네 파일 모두 실제 GitHub SHA와 Native Node22 로컬 `git hash-object` 일치. `node --test` **28/28 PASS** (CSV parser/reader stubbed in CLI tests, exact P7 source).
- **V8 source integration:** P5 17/17; P6 14/14; P7 원본 `site/csv-transform.mjs` 파서+P7 CLI 9/9; P3 기존 Generic/SELF 독립 SHA256 원본 V8 14/14. P3→P4→P5 실제 원본 소스/정확 SHA256를 연결하여 정상2 CSV 300.00 -25.00=275.00, SHA 검증/검토 보류/중복 차단 포함 **9 PASS**, 나머지 1은 검증 하네스에 `structuredClone` 없어 미실행(실패 제품 기능으로 오인 금지).
- **Pending:** GitHub Actions on `preprocessing` branch 조회 0건, 전체 Native 원본 저장소 `npm run test:preprocessing` 미실행, 새 P5 17/P6 15/P7 CLI10 Native 원본 통합 검증 전체 미실행. 실제 Windows Edge/Chrome 프론트엔드 SELF 승인 UI 및 고객·납품/라이선스/결제 실사 미검증. **RELEASE HOLD**.
- 처음 P7 V8 14시도 중 부분 한국어 alias 4자 부재 이슈는 4자 이상 부분일치로 수정, 실제 U+200D 아닌 리터럴 테스트 하네스 이슈는 실제 Unicode Native 검사로 재현/통과. 재검증 P7 V8 14 PASS, Native 28 PASS. 실패 데이터를 지우지 않고 소스 기준 SHA로 구분.
- `main` SHA `264bd5342cd0702a472697d9fa47968fca7f990e`, `frontend` SHA `52e8a54f676a015e9fbee58def89e1cb84656d72` 보존. 사용자 데이터, 비밀, API 비용, GitHub Actions 권한, 배포 설정/도메인 변경 없음.

## 현행 16종 집계와 다음 순서

업데이트 뒤 총 완성률 포인트 **995**, 단순 평균 **995/16 = 62.1875%** (표시 62.2%); 미만 50% **AXMART³ CUBE 45% 한 개**, 50% 정확히 4개(SMAX², EAI, 코인 패턴 분석기, AXMART PC CARE), 초과 50% 11개. 이 평균은 *16개 상품 단순 산술 평균*, 규모·매출·기술 난도 가중치 없음.

다음 우선순위: SMAX² 정확 GitHub 전체 `npm run test:preprocessing` native regression → P3~P7 실제 OS 파일/CLI 통합 → Windows/SELF frontend UI 승인 E2E → 상용 권리/고객 설치/판매; 최종 사용자가 해야 할 현장 작업은 마지막에 묶어서 안내. 비용·외부 데이터 전송·권한/보안 변경·원본 수정/배포는 별도 승인 후에만.
