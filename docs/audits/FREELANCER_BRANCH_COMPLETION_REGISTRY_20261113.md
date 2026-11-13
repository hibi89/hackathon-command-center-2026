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

**브랜치 수 7개 / 제품 8개.** ECHOHOME과 PAWTALK는 같은 브랜치를 사용하므로 브랜치 1개=상품 1개로 가정하지 않는다. 모든 행은 현재 확인된 GitHub 브랜치와 Freelancer `main/docs/PRODUCT_INDEX.md`·`HANDOFF.md`를 기준으로 등록했다. 등록완료는 실제 크몽 게시 증거가 있을 때만 기록한다.

## 앞으로의 자동 등록 규칙 (정책 확정, 무인 실행은 미구현)

1. `Freelancer`에 `product/*` 브랜치 생성 이벤트가 오면 브랜치명을 중앙 등록 후보로 감지한다. 기존 브랜치도 정기 재대조하여 이벤트 누락을 복구한다.
2. 해당 브랜치의 `docs/FINAL_BLUEPRINT.md`, `REQUIREMENTS.md`, `STATUS.md`를 읽어 **상품 ID와 브랜치의 1:N 관계**를 식별한다. 자료가 없으면 브랜치만 `UNASSESSED / 설계 확인 대기`로 등록하고 상품 수를 임의 추정하지 않는다.
3. 기존 원장과 안정적인 `repo+branch+product_id` 키로 중복 검사한다. 같은 상품의 새 커밋은 기존 행을 갱신하되 등록완료·작업중·HOLD·과거 검증 증거는 보존한다.
4. 최종 설계도 100% 기준의 요구별 소스·정확 SHA 검증·승인 가중치가 없으면 공식 완성률은 **UNASSESSED**. 기존 내부 85/95% 숫자 복사 금지.
5. GitHub API 쓰기 권한을 가진 전용 토큰/앱을 최소 권한으로 설정하고, 단일 작성자·동시 실행 직렬화·충돌 시 최신 HEAD 재조회·중복 방지·실패 알림·감사 로그를 적용한다.
6. 실제 자동 등록은 이벤트 워크플로/인증·교차 비공개 저장소 읽기·중앙 브랜치 쓰기 권한과 종단 테스트를 갖춘 뒤에만 `ACTIVE`로 판정한다. 현재 `NOT_CONFIGURED / NOT_TESTED`이며 자동화 성공으로 표시하지 않는다.

기존 해총 중앙 29종과 19개 게시 후보의 분류는 변경하지 않았다. 신규 소비자형 3종은 판매 후보 분류 검토 전에도 이 등록부에서 영구 추적한다.
