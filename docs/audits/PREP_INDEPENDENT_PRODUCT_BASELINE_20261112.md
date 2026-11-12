# PREP 독립 제품 — 크몽 상품화 후보 및 최종완성률 기준 (2026-11-12 KST)

## 최신 판정
| 항목 | 값 | 구분 |
|---|---|---|
| 제품 | PREP — Universal Data Preparation Engine | 별도 독립 제품 |
| 저장소 | [hibi89/prep](https://github.com/hibi89/prep), `main` / `develop` / `feature/core-extraction` | GitHub 조회 |
| 확인한 문서 기준 SHA | `1b5d2be9ddd289aa03b95809e8fc95afc85fb8a3` | 문서-only HEAD |
| 최종 설계 | [REQUIREMENTS.md](https://github.com/hibi89/prep/blob/main/REQUIREMENTS.md) R01–R12, [최종 제품 설계](https://github.com/hibi89/prep/blob/main/docs/FINAL_PRODUCT_BLUEPRINT.md), [검수 기준](https://github.com/hibi89/prep/blob/main/docs/ACCEPTANCE_MATRIX.md) | 문서화됨 · 소유자 최종 검수 대기 |
| **독립 저장소의 구현 및 실행 검증 달성률** | **0% (검증 근거 기준)** | 해당 저장소에 실행 가능한 제품 소스 이관 및 테스트 증거 없음 |
| **정식 최종상품 개발 완성률** | **미산정 (UNASSESSED)** | 기능별 R01–R12 구현/실행 증거 및 제품 평가 필요 |
| 상용화 | RELEASE HOLD | 패키지/Windows/실사용/권리/배포 검증 없음 |
| 공개 상태 | Public (현재 보안 차단) | 기존 비공개 소스 이관 금지. 가시성 변경은 사용자 사전 승인 |
| 크몽 집계 | **기존 활성16종 외 별도 육성 후보** | 활성16종 분모/합계/평균/순위 변경 없음 |

## 수치 기준 설명
- 0%는 독립 PREP 저장소에서 **검증된 실행 가능한 제품 기능의 확보 정도**를 가리킨다. 설계 완료 비율이나 최종 제품 전체의 정확한 개발 진도 추정값이 아니다.
- 정식 '최종상품 완성률'은 해당 저장소 `STATUS.md`와 `HANDOFF.md`에 적힌 대로 **미산정**이다. 아직 독립 제품에 대한 근거 기반 점수 산정이 불가능하다.
- 역사적 `hibi89/SMAX@preprocessing`의 **SMAX²+PREP+SELF 상품 범위 점수 50%**는 PREP 독립제품 점수로 복사하지 않는다. 해총 현행 SMAX² 상품 85% 잠정도 PREP 점수로 복사하지 않는다.
- 향후 실제 전처리 기능을 안전하게 이관하고, 골든/회귀/Windows/실사용/어댑터 검증 증거를 확인한 이후에만 독립 PREP 상품의 진도를 재평가한다.
- 작업 없는 기획 문서 추가나 브랜치 생성만으로 50%로 올리지 않는다.

## 2026-11-12 KST 조회 근거 및 차단 사항
- PREP `STATUS.md`: final product design DOCUMENTED / OWNER REVIEW; independent runtime NOT MIGRATED; full test NOT RUN; CI NOT CONFIGURED; production HOLD; standalone completion NOT SCORED.
- PREP `HANDOFF.md`: Public repo와 기존 Private 원본 간 보안 불일치로 소스 이관 차단.
- PREP `REQUIREMENTS.md`: 50/70/85/95/100은 **장래 합격 기준**이지 현재 달성 수치 아님.
- 기술 스택: Node.js 20+ ECMAScript Modules 계획; 오프라인 결정론적 CSV/JSON 검증, 인간 검토, 원본 SHA-256, 독립 CLI/SDK는 **목표 기능**.
- 현재 독립 repo에서 `npm test`, Windows E2E, CI, 실제 고객 검증은 수행되지 않았다. PASS/FAIL/SKIP를 만들지 않는다.

## 다음 우선순위
1. 사용자의 사전 동의 아래 PREP 공개 상태를 Private으로 전환하거나, 비공개 원본을 복사하지 않는 별도 공개 개발을 선택.
2. 원본 `hibi89/SMAX`의 재사용 가능한 소스, 테스트, 의존성 및 원본 SHA를 안전하게 인벤토리하고 백업/롤백 확보.
3. 명시된 PREP 코어만 독립 추출하고 SMAX 전용 업무 의존성 제거.
4. 정확 SHA 연결 회귀/보안 테스트와 Node/Windows 검증.
5. 승인된 소비자 앱 최소 1곳에서 버전 고정 연동 성공 후 상품 완성률 정식 평가.

**원본 보존:** PREP, SMAX, 타 상품 코드/권한/보안/배포 변경 없음. 이 문서는 해총 보고만 최신화한다. 기존 활성16종 현재값과 과거 이력은 그대로 유지.

**갱신:** 2026-11-12 KST. 근거: 연결된 GitHub 메타데이터 및 PREP 프로젝트 문서 확인. 허브 최종 커밋 SHA는 이 파일을 포함한 쓰기 후 별도 확인.
