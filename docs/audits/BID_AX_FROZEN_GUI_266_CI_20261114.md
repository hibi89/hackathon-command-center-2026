# BID AX — Windows frozen GUI 실기동 266 테스트 CI 중앙 최신 감사

2026-11-14 KST · `hibi89/Freelancer@product/bid-ax-public-procurement` · 코드 [`1ec540634671ff85b080e034cd37564e54fc8e1e`](https://github.com/hibi89/Freelancer/commit/1ec540634671ff85b080e034cd37564e54fc8e1e), 문서 [`cb0434ef6a61af80e96b2f5c2d9a0aa512983280`](https://github.com/hibi89/Freelancer/commit/cb0434ef6a61af80e96b2f5c2d9a0aa512983280).

- **고객 PC 개입 없이 개발:** 기존 온비드 격리 JSON의 GUI 다중 선택·동의/UUID 증빙·중단복구(기능 SHA `1ae85fcb4cc5`) 보존. 신규 `--selftest-gui` 모드는 임시 디렉터리에서 GUI 시작/0.7초 후 정상 종료, 실제 고객 DB 기본 경로 호출 없음. GitHub Windows runner에서 unsigned frozen EXE 프로세스를 실제 실행하고 30초 시간 제한·ExitCode0 확인.
- **검증:** [Actions #43538851029](https://github.com/hibi89/Freelancer/actions/runs/43538851029) **5/5 SUCCESS**: Ubuntu3.11/3.13 각각 266 PASS, Windows3.11 **266 tests, 0 FAIL, 1 POSIX-only SKIP**, Windows CLI EXE 무HTTP smoke, Tk 창 생성/종료, unsigned GUI onedir PE 생성 및 **frozen GUI 실행/종료** PASS. 앞 단계 [263 테스트 CI](https://github.com/hibi89/Freelancer/actions/runs/43538216227)보다 실제 GUI 실행 증거 확대. 고객 Windows10/11 설치·업무 시나리오·서명·SmartScreen/ACL은 **미검증**.
- **실 API/상용:** 고객 소유 온비드15157252 최초 한 페이지 10/10(기관 `totalCount=186` 보고)만 검증, 뒤18페이지/나라장터 및 온비드 나머지 API/인증·실공고100·독립사람10/상업 원문권리·고객인수 미완. 신규 정부 HTTP 호출·고객키 업로드·원본 수정 0. 상업 크몽 등록 없음.
- **정식 최종완성률:** R01–R29 100% 전체 고정, 공식 **UNASSESSED**, 85% 미입증, `[작업중]`, RELEASE HOLD. CANDIDATE-10/KMONG-SVC-18, 원천29/서비스19/등록완료 이력/제외 BID OWL/타제품 보존.
- **제품 근거:** [Windows GUI 실기동 상세](https://github.com/hibi89/Freelancer/blob/product/bid-ax-public-procurement/docs/BID_AX_FROZEN_GUI_SMOKE_20261114.md). 기존 [255→263 GUI 감사](BID_AX_GUI_263_WINDOWS_CI_20261114.md)는 중간 이력.
