# Freelancer 신규 브랜치 → 크몽 최종완성률 등록 원장 (2026-11-13 KST)

**목적:** Freelancer `product/*` 브랜치가 생성되면 최종완성률을 산정하지 못했더라도 누락 없이 중앙 크몽 원장에 등록한다. 기존 29개 원천제품/19개 판매 서비스·등록 이력은 삭제하거나 덮어쓰지 않는다. 이 원장은 신규 제품의 별도 보조 등록부이며 판매 게시글 수를 뜻하지 않는다.

| 제품 | Freelancer 브랜치 | 공식 최종완성률 | 등록/출시 | 근거 |
|---|---|---|---|---|
| AZENTFLOW AX | `product/hae-la-automation` | UNASSESSED | 기존 HAE·LA 통합 서비스에 연결, HOLD | 기존 기업형 조합 |
| CITEVAULT AX | `product/rag-enterprise-knowledge` | UNASSESSED | 기존 RAG 서비스에 연결, HOLD | 기존 기업형 조합 |
| SITECRAFT AX | `product/rea-website-rebuild` | UNASSESSED | 기존 REA_Web 서비스에 연결, HOLD | 기존 기업형 조합 |
| PROOFQA AX | `product/proofqa-ax-delivery-audit` | UNASSESSED | 기존 코드 품질감사 서비스에 연결, HOLD | 기존 기업형 조합 |
| ONTOINSIGHT AX | `product/ontoinsight-ax-data-analytics` | UNASSESSED | 기존 데이터 AI 분석 서비스에 연결, HOLD | 기존 기업형 조합 |
| ECHOHOME | `product/echohome-pawtalk-local-ai` | UNASSESSED | 미등록·HOLD | 가족 동의 음성대화 설계, 앱 미검증 |
| PAWTALK | `product/echohome-pawtalk-local-ai` | UNASSESSED | 미등록·HOLD | 반려동물 놀이형 음성대화 설계, 앱 미검증 |
| MYRADIO AI | `product/myradio-ai-dj` | UNASSESSED | 미등록·HOLD | 오프라인 WAV 시제품, 실 Windows/상용권리 미검증 |
| AXNODE | `product/axnode-sector-runtime` | UNASSESSED | 미등록·HOLD | 사용자 A안 독자 바이너리 `.axnode` 최종설계 R01~R29, 별도 로컬 POC 19 PASS; GitHub 브랜치에 실행 소스/CI 미반영, 원격/3GB/Windows 미검증 |

**브랜치 수 8개 / 제품 9개.** ECHOHOME과 PAWTALK는 같은 브랜치를 사용하므로 브랜치 1개=상품 1개로 가정하지 않는다. 모든 행은 현재 확인된 GitHub 브랜치와 Freelancer `main/docs/PRODUCT_INDEX.md`·`HANDOFF.md`를 기준으로 등록했다. 등록완료는 실제 크몽 게시 증거가 있을 때만 기록한다.

## 앞으로의 자동 등록 규칙 (정책 확정, 무인 실행은 미구현)

1. `Freelancer`에 `product/*` 브랜치 생성 이벤트가 오면 브랜치명을 중앙 등록 후보로 감지한다. 기존 브랜치도 정기 재대조하여 이벤트 누락을 복구한다.
2. 해당 브랜치의 `docs/FINAL_BLUEPRINT.md`, `REQUIREMENTS.md`, `STATUS.md`를 읽어 **상품 ID와 브랜치의 1:N 관계**를 식별한다. 자료가 없으면 브랜치만 `UNASSESSED / 설계 확인 대기`로 등록하고 상품 수를 임의 추정하지 않는다.
3. 기존 원장과 안정적인 `repo+branch+product_id` 키로 중복 검사한다. 같은 상품의 새 커밋은 기존 행을 갱신하되 등록완료·작업중·HOLD·과거 검증 증거는 보존한다.
4. 최종 설계도 100% 기준의 요구별 소스·정확 SHA 검증·승인 가중치가 없으면 공식 완성률은 **UNASSESSED**. 기존 내부 85/95% 숫자 복사 금지.
5. GitHub API 쓰기 권한을 가진 전용 토큰/앱을 최소 권한으로 설정하고, 단일 작성자·동시 실행 직렬화·충돌 시 최신 HEAD 재조회·중복 방지·실패 알림·감사 로그를 적용한다.
6. 실제 자동 등록은 이벤트 워크플로/인증·교차 비공개 저장소 읽기·중앙 브랜치 쓰기 권한과 종단 테스트를 갖춘 뒤에만 `ACTIVE`로 판정한다. 현재 `NOT_CONFIGURED / NOT_TESTED`이며 자동화 성공으로 표시하지 않는다.

기존 해총 중앙 29종과 19개 게시 후보의 분류는 변경하지 않았다. 신규 소비자형 3종은 판매 후보 분류 검토 전에도 이 등록부에서 영구 추적한다.

## 2026-11-13 신규 연구 제품 AXNODE 등록

- 신규 안정 ID: `Freelancer/product/axnode-sector-runtime/AXNODE`. [전용 최종설계](https://github.com/hibi89/Freelancer/blob/product/axnode-sector-runtime/docs/FINAL_BLUEPRINT.md)와 R01~R29 요구 ID를 공식 전체 설계의 분모 후보로 등록. 사용자 세부 가중치/실험 검증 전 공식 수치 **UNASSESSED**, 크몽 **미등록**, 출시 **HOLD**.
- 2026-11-13 로컬 POC에 대해 5섹터·852-byte CSV 분석 / Python unittest **19 PASS/0 FAIL/0 SKIP**를 재확인. 이 성공은 로컬 샌드박스 시험이며 GitHub 브랜치의 코드 CI나 고객 Windows/3GB/원격 Actions/HAE-LA 상용 동작 증거가 아니다. 시제품 코드는 로컬 ZIP 별도 산출물이고 이 브랜치에는 설계/인수인계 문서가 등록됨.
- 이 제품은 **기존 29개 원천제품 / 19개 판매 서비스와 별도 신규 후보**다. 앞서 추가된 소비자형 3종과 합하면 중앙 추적 제품은 **33개 (29+3+1)**, Freelancer `product/*`는 **8개 브랜치, 9개 제품**이다. 기존 상품 등록완료/마커/진도/출시 상태, 원본 29→19 매핑 불변.
- 이 원장 반영은 담당자 수행 동기화이며 GitHub Webhook/GitHub Actions 무인 신규 브랜치 등록 기능이 실제 활성화된 것이 아님.
