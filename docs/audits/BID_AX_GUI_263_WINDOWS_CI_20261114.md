# BID AX GUI 다중페이지·Windows 263테스트 CI 중앙 감사

2026-11-14 KST · 제품 `hibi89/Freelancer@product/bid-ax-public-procurement`

- **정확 검증 기능 SHA:** [`1ae85fcb4cc58d3bdd3f52d37c243b99f1f4e4f4`](https://github.com/hibi89/Freelancer/commit/1ae85fcb4cc58d3bdd3f52d37c243b99f1f4e4f4); 문서 HEAD [`721f1ba1f464eec65e5cbf79f5127529e4819a4b`](https://github.com/hibi89/Freelancer/commit/721f1ba1f464eec65e5cbf79f5127529e4819a4b). 중앙 판매 후보 `CANDIDATE-10`/서비스 `KMONG-SVC-18` 유지. 최종설계 전체 R01–R29 변경 없음.
- **변경:** Tk GUI에서 사용자가 사전 보유·격리한 Onbid `15157252` JSON 여러 개를 한 번에 선택하여 명시 동의 후 UUID 로컬 SQLite 경로/SHA/건수 증빙 등록. 중간 실패 시 이미 기록한 유효 페이지를 같은 배치에서 다시 조회·재개. GUI 15개 버튼을 5열로 재배치. 실 HTTP·자동 원장 승격·실자격/낙찰판정·API 키 저장 없음.
- **CI:** [GitHub Actions #43538216227](https://github.com/hibi89/Freelancer/actions/runs/43538216227) **5/5 SUCCESS**(Ubuntu3.11 263 PASS; Ubuntu3.13 263 PASS; Windows3.11 **263 tests, 0 FAIL, 1 POSIX-only SKIP**; Windows CLI folder EXE smoke PASS; Tk 창 초기화+비출시 unsigned Windows GUI onedir PE build PASS). Windows 현장 GUI EXE 조작·설치/SmartScreen/서명은 **미검증**.
- **오류와 실제 해결:** 중간 [CI #43537874647](https://github.com/hibi89/Freelancer/actions/runs/43537874647) Windows 260 테스트 중 임시 SQLite 연결 `with sqlite3.connect`가 파일 핸들을 닫지 않아 WinError32 ERROR1; `contextlib.closing` 후 최종 run에서 PASS. 불필요한 빈 커밋·유료 재배포 없음.
- **데이터/상용 게이트:** 기존 사용자 실 온비드 첫 페이지 10/10(업스트림 totalCount186)만. **나머지18페이지·나라장터 및 다른 온비드 상세/공고 API·원문 필드·공고100/독립 사람10·고객 Windows·상업 사용권 미검증.** 상품 공식 85% 미입증, **UNASSESSED/[작업중]/RELEASE HOLD/크몽 미등록**, 기존 원천29/서비스19/등록완료/다른 제품·BID OWL 모두 불변.
- **원본·보안:** API key, 사용자 raw JSON, 고객 DB 공유/변경 없음. GitHub 제품 repo 현재 public임을 메타데이터로 확인했으므로 키·데이터 비업로드 원칙 필수.
- **제품 근거:** [GUI/CI 기록](https://github.com/hibi89/Freelancer/blob/product/bid-ax-public-procurement/docs/BID_AX_GUI_ONBID_CHECKPOINT_CI_20261114.md) 및 [전수 최종설계 수용 표](https://github.com/hibi89/Freelancer/blob/product/bid-ax-public-procurement/docs/FINAL_R01_R29_EVIDENCE_GATE_20261114.md).
