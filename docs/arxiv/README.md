# arXiv 기술·구현·크몽 상품화 레이더

**운영 브랜치:** `hibi89/hackathon-command-center-2026@kmong-productization`  
**수집 예약:** ChatGPT 자동화 `Automation_94cd8969ddd081918467dc02bd0a92d3`, 화·금 11:30 KST (2026-11-17 기준 설정)  
**운영 성격:** 공개 논문 조사·기술 검토·상품화 가설. 사용자 승인 없는 소스/배포/권한/상품 등록 작업 아님.

## 조사 자료
- [월별 최신 연구 원장](2026-11/RESEARCH.md) — 날짜별 `ARXIV-YYYY-MM-DD` 섹션. 해당 날짜 run_id 중복 추가 금지
- [논문 조사 이력](RESEARCH_HISTORY_INDEX.md) — arXiv ID가 영구 중복 방지 키; 새 논문만 누적, 재검토 시 날짜/변경 근거 추가
- [상품 아이디어](PRODUCT_IDEAS.md) — 기존 19 SKU와 중복 제거, 제안→검증→실상품 등록 상태 구분
- [예약·자동 저장 runbook](AUTOMATION_RUNBOOK.md) — GitHub 커넥터의 최신 SHA 조회 → 새 항목만 append/update → 원격 readback

## 안전 및 검증
1. arXiv 논문 공개 = 코드 상업권리 허용이 아니다. 논문/저자 보고, 구현 코드 LICENSE/NOTICE·의존/모델/데이터 권리를 분리 기록한다.
2. 사용자 확정 제품별 `AGENTS.md`·최종설계·원천·크몽 19 SKU/등록 이력은 별도 정본이다. 조사는 제품 변경이나 출시 승인으로 취급하지 않는다.
3. 실제 코드·테스트·CI·배포·GitHub Actions·GitHub App·Production·고객자료/비밀 접근을 조사 예약에서 수행하지 않는다.
4. 저장 권한이 없거나 예약 실행 도구에서 GitHub 커넥터가 제공되지 않으면 **`GITHUB_SYNC_PENDING`**와 이유를 보고한다. GitHub 성공을 추정하지 않는다.
5. 최초 수동 저장 성공과 **예약 실행 성공은 별개**다. 첫 예약 실행 후 실제 자동 커밋 SHA·원격 파일 readback을 확인하기 전에는 `SCHEDULED_END_TO_END_NOT_VERIFIED` 유지.
