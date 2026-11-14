# BID AX 온비드 후속 페이지 로컬 수집기 — 무료/266→276 CI 감사

**2026-11-14 KST** · hibi89/Freelancer @ product/bid-ax-public-procurement · 기능 [`3008bfd440aafe57e264ad4a0485d517f8819634`](https://github.com/hibi89/Freelancer/commit/3008bfd440aafe57e264ad4a0485d517f8819634) · 제품 문서 [`6e644ce44c3e026882f9daf2dae7fd245a768658`](https://github.com/hibi89/Freelancer/commit/6e644ce44c3e026882f9daf2dae7fd245a768658).

1. 사용자 승인: **유료 비용 없는** 개발·검증·GitHub 반영은 진행 허용. 최종설계 R01–R29 29개 전체 불변, 별도 100점 가중치 재승인 요구 금지.
2. 구현/선택: 고객 키/원문 클라우드 수집·자동 정규화(A)보다 **고객 PC의 검증된 첫 JSON을 근거로 하는 소량·중단복구·실키 메모리 보유(B)** 채택. `onbid-continue`는 오프라인 계획 후 명시적 동의/--live가 있을 때만 공식 15157252 요청, max25(기본4)/시도예산 24(사용자 조정)·재시도0, 신규 파일 create-only/SQLite SHA·UUID 조회조건 검증, 저장됐지만 중단된 격리 파일의 무재호출 재사용. 기존 원문·키/타상품/법원문건 불변.
3. 테스트: [Actions #43540224552](https://github.com/hibi89/Freelancer/actions/runs/43540224552) **5/5 SUCCESS**: Ubuntu Python3.11/3.13 각276 PASS, Windows3.11 276 tests/0FAIL/1 POSIX SKIP, Windows CLI·GUI 비출시 EXE 스모크. 신규 오프라인 synthetic 테스트 10. 최초 synthetic reference total21 vs cached page total11로 1 ERROR→reference11로 정정 후 CI 성공; 운영 오류 아님.
4. 실데이터/차단: 첫 온비드 실 API 15157252 page1 10건·provider totalCount186 **보고만**. 나머지18페이지와 나라장터/온비드 타 API 3종 실제 응답·원문 필드·상용 API/파일 권리·실 공고100/독립 인간검토10·구매자 Win10/11 설치/파일럿 **미검증**. 15157220 오퍼레이션 경로 미확정이라 호출 계속 차단.
5. 판정: **최종완성률 공식 UNASSESSED, 사용자 목표85% 미입증, [작업중], RELEASE HOLD, 크몽 미등록.** 테스트 통과가 실제 고객 수용률 아님. CANDIDATE-10/KMONG-SVC-18, 기존 29원천/19서비스·등록 이력·타제품·BID OWL 무변경.
6. 실행/인수: 고객 Windows 로컬 `py -3.11 -m bidax.cli --db .\\local-onbid-pages\\stage.db onbid-continue UUID FIRST_JSON --out-dir .\\local-onbid-pages --consent`로 dry-run 후 요청 시에만 `--live --max-new-pages 4 --daily-limit 24`, 키 로컬 프롬프트. 실제 18페이지 본인 PC 호출이 끝나면 186 실원문/자격 별도 검증. [제품 실행 가이드](https://github.com/hibi89/Freelancer/blob/product/bid-ax-public-procurement/docs/BID_AX_ONBID_FREE_CONTINUATION_20261114.md).
