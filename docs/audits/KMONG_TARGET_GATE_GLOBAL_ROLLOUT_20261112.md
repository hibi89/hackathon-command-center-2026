# GitHub 전체 저장소 크몽 [작업중] 목표 달성 게이트 공지 전파 검수 — 2026-11-12 KST

## 최신 사용자 확정 정책
- **크몽 제품/후보 작업 착수:** 중앙 `docs/audits/KMONG_16_CURRENT_20261111.md`에 제품명 옆 `**[작업중]**` 표시·커밋, 해당 단계의 확정 완성률 목표·검증 기준을 제품 상태 기록에 명시.
- **목표 미달:** 일시정지·중단·보류·채팅 종료·다른 프로젝트로 전환·담당자 변경 시에도 표식을 **삭제하지 않음**. 종전 '전환·중단 시 제거' 지침은 최신 정책으로 폐기.
- **검증된 목표 달성:** 코드/테스트 SHA, PASS/FAIL/SKIP와 남은 미검증 범위를 확인한 후에만 해당 제품 담당자가 자기 표식을 제거·커밋. 목표 하향/변경으로 표식 제거 시 소유자 명시적 승인 필요.
- 표식은 미달성 **목표 추적 상태**이지 실시간 실행 증거·판매 승인 아님. 중앙 표 자동 갱신 없음, 담당자 직접 커밋. 실패 시 `KMONG_HUB_SYNC_PENDING`. 크몽 대상이 아닌 제품/프로젝트는 이 표식의 대상이 아님.

## 원격 범위·검증
- 연결된 GitHub 소유자 `hibi89`의 `list_repositories(owner=hibi89,page_size=100)` 결과: **총 33개 저장소**, 비아카이브. 모든 저장소 기본 브랜치 `main`에 조건부 공통 고지 삽입 완료.
- **33/33** 기본 브랜치 `AGENTS.md` 원격 재조회 식별자 `KMONG_WORK_TARGET_GATE_20261112` PASS.
- 기존 제품 담당/대회 총괄 및 중앙의 주요 **24개 추가 브랜치**에 동일 정책 반영 후 재조회 **24/24 PASS** (중앙 `kmong-productization`은 `AGENTS.md`의 중간 섹션에 위치하여 전체 파일로 검증).
- 총 검증 범위 **57/57 브랜치-파일**, 오류 0. 구형 브랜치/사용 중이지 않은 기타 브랜치 모두에 반영했다고 주장하지 않음. 원격 수정 전후 문서는 Git 이력으로 복구 가능.
- `EAI@main`, `work-hell-dungeon@main`에는 없던 `AGENTS.md`를 새로 생성. 다른 저장소·브랜치의 AGENTS는 기존 내용을 보존하고 운영 공지만 추가 또는 교체.
- 이 변경에서 **실제 상품 개발·퍼센트·CI·Production·판매 승인/배포·비밀·권한 변경 없음**. 공지는 향후 작업자 실행 지침이며 자동 동기화 아님.

## 33개 기본 브랜치 (`main`)
1. `hibi89/AI_AutoML_Analyst@main`
2. `hibi89/Bid_Owl@main`
3. `hibi89/self-hosted-n8n-reliability-lab@main`
4. `hibi89/ohora-nail-intelligence-v4@main`
5. `hibi89/ohora-trend-catcher@main`
6. `hibi89/web-rea-studio@main`
7. `hibi89/NAON2-Character-Studio@main`
8. `hibi89/gongbaek-sanggwon@main`
9. `hibi89/project-book@main`
10. `hibi89/astra_web_catcher@main`
11. `hibi89/fable5.1_web_catcher@main`
12. `hibi89/astra_pdf_redesigner@main`
13. `hibi89/ohora-trend-catcher-classic@main`
14. `hibi89/ohora-trend-analyzer@main`
15. `hibi89/hibi89-kic-proofinvest@main`
16. `hibi89/hackathon-command-center-2026@main`
17. `hibi89/hibi89-paypal-ai-hackathon@main`
18. `hibi89/hibi89-ugreen-nas-hackathon@main`
19. `hibi89/SMAX@main`
20. `hibi89/REA_Web@main`
21. `hibi89/SOVIA_sovereign@main`
22. `hibi89/RAG_STUDIO@main`
23. `hibi89/ai-code-checker@main`
24. `hibi89/DBVORA@main`
25. `hibi89/Freelancer@main`
26. `hibi89/HAE@main`
27. `hibi89/AX_MART@main`
28. `hibi89/EAI@main`
29. `hibi89/work-hell-dungeon@main`
30. `hibi89/candle_scraper@main`
31. `hibi89/frontend-foundry-ax@main`
32. `hibi89/prep@main`
33. `hibi89/factory-ax-ecosystem@main`

## 24개 추가 주요 브랜치
1. `hibi89/candle_scraper@feature/coin-pattern-p85-forward-eval-20261112`
2. `hibi89/candle_scraper@feature/kmong-collector-p95-delivery-integrity-20261112`
3. `hibi89/HAE@feature/axflow-mvp`
4. `hibi89/HAE@feature/rea-app-kmong-owner-delivery-20261112`
5. `hibi89/HAE@feature/lightning-azent`
6. `hibi89/HAE@feature/la-p17-audit-evidence-20261112`
7. `hibi89/ai-code-checker@feature/retail-private-candidate-20261112`
8. `hibi89/SMAX@feature/prep-self-owner-mapping-p8`
9. `hibi89/REA_Web@feature/lite-owner-delivery-p95-20261112`
10. `hibi89/SOVIA_sovereign@feature/kmong-la-review-p2-20261112`
11. `hibi89/AI_AutoML_Analyst@feature/kmong-p6e50-owner-delivery-20261112`
12. `hibi89/DBVORA@feature/p0-db-map`
13. `hibi89/RAG_STUDIO@feature/p546-rag-prep-mapping`
14. `hibi89/astra_pdf_redesigner@feature/astra-p71-pdf-source-parity-20261112`
15. `hibi89/EAI@feature/kmong-eai-85-p31-20261112`
16. `hibi89/AX_MART@feature/cube-owner-preflight-p85-20261112`
17. `hibi89/AX_MART@feature/pc-care-p15-p18-85-20261112`
18. `hibi89/prep@feature/core-extraction`
19. `hibi89/frontend-foundry-ax@feature/ffax-workbench-p85-20261112`
20. `hibi89/factory-ax-ecosystem@feature/data-verify`
21. `hibi89/hibi89-kic-proofinvest@lead/kic`
22. `hibi89/hibi89-paypal-ai-hackathon@lead/paypal`
23. `hibi89/hibi89-ugreen-nas-hackathon@lead/ugreen`
24. `hibi89/hackathon-command-center-2026@kmong-productization`

## 중앙 정책 위치
- [AGENTS](../../AGENTS.md): 전체 정책, 목표 달성 전 표식 유지.
- [KMONG_PRODUCTIZATION](../../KMONG_PRODUCTIZATION.md): 크몽 공통 공지.
- [최종완성률 및 후보 상태표](KMONG_16_CURRENT_20261111.md): 최신 표기/삭제 게이트.
- [동기화 프로토콜](KMONG_COMPLETION_SYNC_PROTOCOL_20261111.md): 종료 증거 및 실패 기록.

## 차기 검증
- 새 채팅/작업자가 자신의 **실제 작업 브랜치** `AGENTS.md`를 먼저 읽어 이 규칙 적용.
- 브랜치 생성·전환 시 정책이 포함됐는지 확인; 없는 오래된 브랜치라면 안전하게 고지 추가.
- 각 `[작업중]`이 목표 미달 기록과 일치하는지 별도 감사. **현재 다른 채팅이 실행 중이라는 의미로 해석하지 않음**.
