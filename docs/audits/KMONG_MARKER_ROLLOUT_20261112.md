# 크몽 상품 작업중 표기 규칙 전파 검증 — 2026-11-12 KST

## 사용자 지시와 적용 범위
실제 제품 작업을 시작하면 중앙 `docs/audits/KMONG_16_CURRENT_20261111.md`의 해당 상품 이름 뒤에 `**[작업중]**`을 기입하고 GitHub에 커밋한다. 검증된 단계 목표 완료·중단·보류·작업 종료·제품 전환 시 자신의 표식을 삭제하고 커밋까지 확인한다. 다른 채팅의 표식은 임의 수정하지 않는다. 자동 동기화가 아니므로 담당자 실행 및 GitHub 쓰기 권한이 필요하다. 중앙 쓰기 실패는 `KMONG_HUB_SYNC_PENDING`.

대상: 크몽 활성 16종 및 후보 PREP/FFAX/Factory AX를 담당하는 **15개 제품 저장소의 현재 확인된 21개 주요 개발 브랜치**. 과거/비활성 브랜치와 크몽 비대상 저장소 전체에 소급 반영했다는 주장은 하지 않는다.

## 반영된 제품 필수 파일
모두 `AGENTS.md` 최상단에 `KMONG_WORK_IN_PROGRESS_20261112` 공통 필수 지침을 삽입했다. 새 채팅 또는 `ㄱ` 재개에도 읽도록 지정했고, 기존 파일 내용을 보존했다.

| 저장소 | 반영 브랜치 | 확인된 정책 커밋 |
|---|---|---|
| hibi89/candle_scraper | main | `3ea35af637c2` |
| hibi89/candle_scraper | feature/coin-pattern-p85-forward-eval-20261112 | `fc42b1075f27` |
| hibi89/HAE | feature/axflow-mvp | `75dfc0e1ad92` |
| hibi89/HAE | feature/rea-app-kmong-owner-delivery-20261112 | `b5958fe7de89` |
| hibi89/HAE | feature/lightning-azent | `52a568bc92fe` |
| hibi89/HAE | feature/la-p17-audit-evidence-20261112 | `ed9f42696a29` |
| hibi89/ai-code-checker | feature/retail-private-candidate-20261112 | `9011bc95584f` |
| hibi89/SMAX | feature/prep-self-owner-mapping-p8 | `2014afbe7413` |
| hibi89/REA_Web | feature/lite-owner-delivery-p95-20261112 | `308ed853998e` |
| hibi89/SOVIA_sovereign | feature/kmong-la-review-p2-20261112 | `9b415ea7b3ca` |
| hibi89/AI_AutoML_Analyst | feature/kmong-p6e50-owner-delivery-20261112 | `5e0cb17a6b3d` |
| hibi89/DBVORA | feature/p0-db-map | `b26848f64c9c` |
| hibi89/RAG_STUDIO | feature/p546-rag-prep-mapping | `033f206097b6` |
| hibi89/astra_pdf_redesigner | feature/astra-p71-pdf-source-parity-20261112 | `dc69f7e7ddbb` |
| hibi89/EAI | feature/kmong-eai-85-p31-20261112 | `60c9fcb877d9` |
| hibi89/AX_MART | feature/cube-owner-preflight-p85-20261112 | `4152d49fb787` |
| hibi89/AX_MART | feature/pc-care-p15-p18-85-20261112 | `eb8a64617d35` |
| hibi89/prep | main | `2bc8a47b65ff` |
| hibi89/prep | feature/core-extraction | `62b8a6a172d` |
| hibi89/frontend-foundry-ax | feature/ffax-workbench-p85-20261112 | `69fb334491eb` |
| hibi89/factory-ax-ecosystem | feature/data-verify | `b896e2140179` |

## 검증과 미검증
- **21/21 원격 AGENTS 파일 재조회 PASS**: 각 브랜치 첫 5줄에 공통 식별자 존재. 실패 0.
- GitHub 커밋 API 2개 표본 점검: author/committer `hibi89` 일치.
- 중앙 상황실 `AGENTS.md`에 전체 의무 명시. 완성률 정본 하단에 후보 3종 별도 상태 표 추가; 활성16종 통계/완성률 숫자는 변경하지 않음.
- **제품 코드·테스트·배포/Production 변경 없음**. 이 작업은 문서 운영 정책만 수정했다. 기존 개발 결과가 자동 동기화되거나 현재 실제 실행 중이라고 검증한 것은 아니다.
- 후속 각 담당자는 시작/종료 이벤트마다 중앙 파일의 최신 HEAD 조회→자기 제품 상태만 수정→커밋 확인해야 한다.
