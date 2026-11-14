# CITEVAULT AX — 최종설계 P85 추가 실검증 (2026-11-14 KST)

## [2026-11-14 KST] 최신: 사용자 Windows 부분 실증+질문 중심 UI · 455PASS

- 기능 SHA [`62fe69bd9f78f5a9a2c49f53b5f227053503a4f1`](https://github.com/hibi89/Freelancer/commit/62fe69bd9f78f5a9a2c49f53b5f227053503a4f1), STATUS/HANDOFF/24항 수용표 SHA [`9a822c85923902bfce68b2c027cf5d85168816bd`](https://github.com/hibi89/Freelancer/commit/9a822c85923902bfce68b2c027cf5d85168816bd).
- [정확 SHA Actions #43536006934](https://github.com/hibi89/Freelancer/actions/runs/43536006934) **8/8 SUCCESS, 455 executed PASS /0FAIL /0SKIP** (Ubuntu/Windows 중복 포함). P70 31, 원본 RAG upstream35+bridge36, OS별 vault/UI/ACL+대화 131·합성100 harness1·backup12, native31×2, real Chrome1, Windows portable ZIP2.
- **REQ16 제품 기능:** 사용자 제시한 복잡 UX 단순화: 로그인→질문→출처 검색 중심, 문서 범위·SQL 검토·관리자 화면은 기본 접힘, 기존 API·접근권한·CSP 유지. Ubuntu 실제 Chrome과 양 OS 신규 UI 계약 검증.
- **REQ19 부분 실기기 증거:** 사용자가 이번 채팅에 올린 Windows QA 콘솔 `PASS`, 기존 정본 SHA `62663721`의 synthetic operator 로그인, 문서/컬렉션 1개, `SEARCH_ONLY` 및 `policy line1` 근거 인용 스크린샷 확인. 실제 Win10/11 버전, 새 UI SHA 현장 실행, 상용 설치/고객자료/실백업·리커버리 및 종료 후 파일 제거는 미검증. 임시 비밀번호/로컬 사용자 경로가 화면에 있어 **공개 GitHub에 스크린샷 복사 금지**.
- 회귀 장애: 초기 사용자 친화형 UI 문구가 이전 운영자 QA 기대 문자열과 달라 #43535664826 실패, Chrome 임시 프로필 ENOTEMPTY; #43535827150 Chrome 10초 startup timeout. 기존 문자열을 유지하고 cleanup/bounded 30초 시작 및 stderr 진단 수정, 최신 8/8 PASS. 정확 경계 외 타상품·고객 원본·배포 설정 변경 0.
- [상세 기술·증거](https://github.com/hibi89/Freelancer/blob/product/rag-enterprise-knowledge/docs/P85_SIMPLE_UI_OWNER_WINDOWS_20261114.md). **공식 24항 전체 최종완성률 UNASSESSED; 목표85% 미인증; CITEVAULT AX [작업중] / RELEASE HOLD / SALE NO-GO**. 실제 기업 IdP·원본 사용권/승인된 PREP-SMAX signed AX producer·실 Korean model+license+Gold100·물리 Win10/11 운영 설치/고객·법무 인수 필요.
- 중앙 원장 대형 `KMONG_16_CURRENT_20261111.md`의 CITEVAULT 표시는 현재도 `[작업중]`. 본 project audit와 제품 HANDOFF/STATUS가 최신 SHA 근거이며 다른 상품 이력/등록완료는 수정하지 않음. 공유 Freelancer PUBLIC의 여러 브랜치/Git 역사 공개 위험·secret 전수감사 미완.


## [2026-11-14 09:10 KST] 이번 최신 최종설계 REQ24+REQ19 — 8/8 CI · 447 PASS

- 제품 기능 SHA [`f2979aa50156b4f5c3d80f4d23a1b2ec336f0040`](https://github.com/hibi89/Freelancer/commit/f2979aa50156b4f5c3d80f4d23a1b2ec336f0040), 제품 10항 HANDOFF/STATUS/24요건 수용표 문서 HEAD [`62663721a4576f597e1b7cde5025760271428cda`](https://github.com/hibi89/Freelancer/commit/62663721a4576f597e1b7cde5025760271428cda).
- [정확 소스 GitHub Actions #43531986943](https://github.com/hibi89/Freelancer/actions/runs/43531986943) **Ubuntu+Windows+실 Chromium·portable QA 총 8/8 JOB SUCCESS, 447 test executions PASS /0 FAIL /0 SKIP** (Linux/Windows 중복 실행 포함), [정책 gate #43531987256](https://github.com/hibi89/Freelancer/actions/runs/43531987256) SUCCESS(최종 고객 85% 인증 아님).
- **REQ24 실기능:** 서버 memory-only 5분 TTL/64 스레드, SHA256 bearer/문서 version/source SHA 결속, 후속질문 전 현재 tenant/group/project/clearance ACL+원문 재검증, 권한 철회/문서폐기/버전교체/위변조/만료/로그아웃 시 이전 맥락 무효화; API/UI 후속 질문·실 Chrome 클릭 테스트. 양 OS 신규12PASS, 생성형 한국어 모델 미설치로 answer=null·외부전송0.
- **REQ19 내부 Windows portable QA:** GitHub Windows Server2022에서 Windows용 Node22+소스/NOTICE·manifest 12파일 합성 번들 작성, Python stdlib ZIP CRC+파일별 SHA roundtrip→압축 해제된 실제 Node 실행으로 운영자 셀프테스트 성공 **2PASS**, ZIP 33,208,926 bytes / sha256 `6dc2c15b1525780c2b1889635a9f94a18cfb987df10530ffe23f916392ea71a2`. CI 임시 데이터·임시 ZIP이며 고객에게 배포하지 않음. 실제 Win10/11 설치/Node 재배포 라이선스/상용 릴리스는 미검증.
- **Stop & Pivot 증거:** 과거 ZIP PowerShell 방식 2회 #43531311927/#43531472046 FAIL(압축 풀어도 실행 파일 없는 layout) → 해당 방법 중단 후 Python zipfile 로컬+hosted PASS. #43531831668 Chrome 프로필 삭제 `ENOTEMPTY` teardown 충돌은 안전한 종료 대기·임시 파일 정리 재시도로 수정, 최신 정확 소스 8/8 CI PASS.
- **최종24항 전체 공식 완성률 UNASSESSED / 사용자 목표85% 미달성·미검증, CITEVAULT AX [작업중] / RELEASE HOLD / SALE NO-GO**. 실제 기업 직원 IdP, 고객 소유권·정식 authoritative signed PREP/SMAX AX 발급, 라이선스 검증된 실 Korean model, 물리 Windows10/11·고객 Gold100·보안/법무/owner 인수 필요. 합성 447PASS를 최종 판매/85%로 환산 금지.
- [제품 상세 인수인계/검증](https://github.com/hibi89/Freelancer/blob/product/rag-enterprise-knowledge/docs/P85_CONVERSATION_PORTABLE_20261114.md). 공유 `Freelancer` 전체 PUBLIC, 타상품 브랜치/과거 Git 이력 공개·민감정보 전수 감사 미실시. 다른 제품 및 고객 원본·계정/비용·Production 불변.
- **중앙 집계 주의:** 큰 `KMONG_16_CURRENT_20261111.md` 본문(164KB)은 이번에 무단 대용량 재작성하지 않고, CITEVAULT 최신 증거는 이 단일 프로젝트 감사 파일과 제품 HEAD를 정본으로 한다. 중앙 표의 과거 421PASS 등은 과거 SHA에 대한 기록으로만 해석.


## [2026-11-14 KST] 최신: Chromium 실제 브라우저+권한대시보드 CI 421 PASS

- 제품 정본 `hibi89/Freelancer@product/rag-enterprise-knowledge`, 기능 SHA [`49918ad4d0de23b8bc462830fa0789e93ebd7936`](https://github.com/hibi89/Freelancer/commit/49918ad4d0de23b8bc462830fa0789e93ebd7936), 제품 문서/수용표 HEAD [`119410fce937a8edfc073518f255a8e937a2db95`](https://github.com/hibi89/Freelancer/commit/119410fce937a8edfc073518f255a8e937a2db95).
- [GitHub Actions #43529432977](https://github.com/hibi89/Freelancer/actions/runs/43529432977) exact-SHA **7/7 SUCCESS, 421 executions PASS /0 FAIL /0 SKIP** (Windows/Linux 중복 테스트 포함). 신규 ACL library8PASS/OS, 실제 Chrome browser1PASS.
- 사용자의 **실제 UI 기능**: 최신 권한을 확인한 `GET /v1/library`, 조직·그룹·프로젝트·등급·문서 active 필터링; 허용 문서 KPI/컬렉션 차트·문서 선택·로그아웃 데이터 제거. 같은 브랜치의 원본 RAG/SQL/PDF-DOCX/Ed25519 합성 경로·Windows native 기존 기능 회귀 통과.
- 실 Chromium Ubuntu hosted: 로그인→허용 문서 대시보드→원문 선택·권한 있는 검색→390px 모바일 무가로 오버플로→로그아웃, Chrome JS runtime 오류0/외부 HTTP 요청0, PNG 스크린샷 SHA `dacfed126a5c6763bd6117e0645ac0b4f3cb532b1bbb573d163151570fa46a65`. 테스트 로컬 Chrome은 조직정책 `ERR_BLOCKED_BY_ADMINISTRATOR`로 blocked, **hosted actual Chrome PASS**. 브라우저 Windows10/11 물리환경과 고객 자료 인수는 미검증.
- [제품 상세 검증·REQ16 수용표](https://github.com/hibi89/Freelancer/blob/product/rag-enterprise-knowledge/docs/P85_CHROMIUM_DASHBOARD_ACCEPTANCE_20261114.md). REQ16 합성 UI 범위 실제 검증 강화됐지만 24항 전체 최종설계 공식률 **UNASSESSED, 85% 미인증, CITEVAULT AX [작업중]·RELEASE HOLD/SALE NO-GO**.
- 미완: 고객 실직원 IdP·문서 이용권/서명 승인 PREP/SMAX producer/AX, licensed Korean model, 물리 Win10/11/customer Gold100·보안/라이선스/법무 최종수용, 사용자 확정 가중치. 공개 Freelancer 전체 브랜치/이력 노출 위험은 그대로, 타제품·원본/고객자료·비용·Production 변경 없음.
- **해총의 이전 398/404PASS 증거는 과거 정확 SHA의 이력이며 본 421PASS가 최신**. 다른 모든 제품 최종률/등록완료·[작업중] 이력·판매정책 불변.


## [2026-11-14 KST 추가] CITEVAULT P85 SQLite catalog consistency 정확 SHA 검증 — 404 PASS

- 기능 `hibi89/Freelancer@product/rag-enterprise-knowledge` [`d32f530e2425da0129a4eb2e9a4a7aef6708dab8`](https://github.com/hibi89/Freelancer/commit/d32f530e2425da0129a4eb2e9a4a7aef6708dab8), STATUS/HANDOFF/24항 수용표 [`aca47c3b5bef32c98ed7a3ac09a0a6ac56a4fe46`](https://github.com/hibi89/Freelancer/commit/aca47c3b5bef32c98ed7a3ac09a0a6ac56a4fe46).
- [hosted GitHub Actions #43527372030](https://github.com/hibi89/Freelancer/actions/runs/43527372030) exact functional SHA **6/6 SUCCESS, 404 test executions PASS/0FAIL/0SKIP**, Ubuntu+Windows 합산(반복 포함). 기존 398 대비 snapshot/integrity 추가 부정3테스트×2OS = 404.
- 실기능: SQLite `header/users/docs/audit` 스키마·generation·count 확인, active 문서 메타데이터의 `tenant/id/version/native_kind/SHA256`를 staged 파일 SHA와 결속. (1) 원본 변조 snapshot 거부, (2) SQLite+manifest 재해시 위조된 catalog 거부, (3) header-only DB restore 거부. Linux/Windows 신규 backup suite 각 **12/12 PASS**.
- [정본 404 증거](https://github.com/hibi89/Freelancer/blob/product/rag-enterprise-knowledge/docs/P85_SNAPSHOT_CATALOG_INTEGRITY_20261114.md). 실제 고객 백업·민감 데이터·승인된 원본 PREP/SMAX와 외부 API는 사용 안 함.
- 공식 **전체 24항 최종설계 완성률 UNASSESSED / 85% 미인증**, `CITEVAULT AX [작업중]`, `RELEASE HOLD/SALE NO-GO`. 기업 실제 IdP, 고객 자료 권리+authoritative signed AX producer, 실제 라이선스 검증 Korean model, 실 Win10/11 고객 설치·Gold100/운영 법적 보안/확정 가중치 미완. 합성 CI 성공≠최종 85%.
- 공유 `Freelancer` 저장소 PUBLIC과 전 브랜치/이력 노출 위험 전수 점검 미수행. 다른 모든 크몽 제품 점수·상태·등록이력·Production 불변.


- 제품 기능 SHA: `hibi89/Freelancer@product/rag-enterprise-knowledge` / `0cf969fb2908cca985f4655d2c713ad7e030d168`.
- 제품 STATUS/HANDOFF/24항 추적표 문서 SHA: `fca436f5cc6f58f10f7e41fa8810f1e39d86b1f7`.
- [실제 hosted CI 43525453183](https://github.com/hibi89/Freelancer/actions/runs/43525453183): Ubuntu24.04+Windows2022 **6/6 SUCCESS, 398 test executions PASS/0FAIL/0SKIP** (플랫폼 간 중복 포함).
- [최종설계 정책 gate 43525845785](https://github.com/hibi89/Freelancer/actions/runs/43525845785): SUCCESS (최종 제품 85% 수용 인증이 아님).
- 신규 기능: 명시적 수동 오프라인 SQLite+문서 SHA256 manifest 백업, create-only 복구, 무단 덮어쓰기/변조·symlink/hardlink/경로 탈출·추가 파일 거부. 양 OS 각 **9 PASS**. 서비스 중지·SQLite 닫고 실행하며 운영형 무중단 고객 백업 아님.
- 합성 한국어 질의100회/OS: 근거 검색20, 근거 부족20, 상충20, 무권한 조회20, 혼합권한 요청 거부20. p95 Ubuntu **0.328ms**, Windows **1.001ms**, 작은 합성 코퍼스 기준. Harness는 OS별 1개 Node 테스트로 집계. **고객 승인 Gold100·실 한국어 모델·대용량 성능과 무관**.
- 이전 검증: 정확 pinned 원본 RAG upstream35PASS + CITEVAULT bridge36PASS. 양 OS Windows DOCX UTF8/SQLite EBUSY 해결 상태 유지.
- [백업 증거](https://github.com/hibi89/Freelancer/blob/product/rag-enterprise-knowledge/docs/P85_OFFLINE_SNAPSHOT_20261114.md) · [합성100 증거](https://github.com/hibi89/Freelancer/blob/product/rag-enterprise-knowledge/docs/P85_SYNTHETIC100_EVIDENCE_20261114.md).
- **전체 24항 최종완성률 UNASSESSED / 목표85% 미인증 / CITEVAULT AX [작업중] / RELEASE HOLD / SALE NO-GO**. 실제 고객 임직원 IdP·원본 사용권·승인된 signed PREP/SMAX→AX producer, 실제 Korean pretrained local model, 물리 Win10/11 설치, 고객 Gold100/법무·안전 인수/확정 가중치 미검증.
- 사용자에 의한 `hibi89/Freelancer` 전체 Public 변경으로 타제품 모든 브랜치/기록 공개 위험. 보안 이력 전수 검사 미완, 고객 자료·토큰 커밋 금지. assistant가 공개 설정/Production·비용·다른 상품 원장을 변경한 것은 아님.
- 중앙 기존 CITEVAULT 행에 과거 선실패/378PASS가 있어도 **본 문서와 제품 HEAD의 최신 398PASS 증거가 우선**한다. 다른 모든 제품 수치·마커·판매 등록완료 이력 불변.
