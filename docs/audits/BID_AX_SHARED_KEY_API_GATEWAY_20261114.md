# BID AX — 사용자 4개 무료 API 활용신청·공통 인증키 게이트 개발 기록 (2026-11-14 KST)

- 대상: CANDIDATE-10, KMONG-SVC-18. hibi89/Freelancer@product/bid-ax-public-procurement.
- 사용자 확인: 나라장터 입찰공고 15129394·온비드 15157220/15157252/15157254 4개 신청, 같은 계정 일반 인증키가 4개에 동일하게 표시됨. 키 값 자체는 수집/공유/저장/검증하지 않음. 동일 키가 모든 서비스에 접근 허가됐다는 실 API 증거는 아직 없음.
- 기능 SHA [e3ffb4fa1a6c](https://github.com/hibi89/Freelancer/commit/e3ffb4fa1a6c20f640746f990cef5f0f9e88f8b3). 원격 신규 코드/테스트/문서/예시 7/7 Git blob 로컬 해시와 일치.
- 새 api-probe CLI: 기본 credential-free offline 계획; 명시 --live --out 시에만 Windows/PC에서 getpass로 1회 메모리 입력한 키로 HTTPS 고정 서비스에 1페이지 조회 가능. 사용자 키를 채팅/GitHub에 올리지 않음.
- 서비스별 내구 요청한도·오류·추적/중복 JSON 방지, 기존 파일 보존, 위험 원문 로컬 격리. 기존 나라장터·온비드·법원 DB 인수/자격 엔진에 자동 통합하지 않음.
- G2B 물품/용역/공사/외자, 온비드 결과목록/상세는 운영 경로 확인. **15157220 공고물건은 공식 operation 미확인으로 호출 미지원/차단.** 공식 확인 전 작동한다고 주장 금지.
- 로컬 Linux Python3.13.5 전체 **188 PASS/0 FAIL/0 SKIP** (기존 167+신규21). 컴파일/zipapp api-probe 오프라인 실행 PASS, 실 OpenAPI 요청 0/실 Windows10·11/EXE/고객·상용권리 미검증. GitHub blueprint-only Action은 Python 테스트 대체 아님; 과금 가능성 있는 자동/수동 별도 OS CI 요청 없음.
- 공식 최종 설계 R01–R29 (29개) 고정. 사용자는 별도 가중치가 없다고 명시했으므로 추가 배점 승인 요청하지 않는다. 실제 미수용/미검증으로 **공식 최종완성률 UNASSESSED, 목표85% 미입증, [작업중] 및 RELEASE HOLD/크몽 미등록**.

## 남은 사용자 작업 / 개발자 작업

- 사용자: 추가 무료 API 신청 필요 없음. Windows 로컬에 보관한 키는 공유하지 않고 추후 명시 승인 시 소량 실 데이터만 고객 PC에서 직접 호출·상태/필드 검증. 고객 실기기 테스트도 별도 필요.
- AI 개발자: 15157220 오퍼레이션 정확 스펙 확인; 실 API 응답 스키마·페이지 처리/오류 회복·정규화·출처/법적 조건, 100 real notices/10 human, Windows/Python3.11·EXE/고객검증 완료 전 출시 보류.
- 기준 문서: https://github.com/hibi89/Freelancer/blob/product/bid-ax-public-procurement/docs/API_GATEWAY_SHARED_KEY_20261114.md
- 공식 API: https://www.data.go.kr/data/15129394/openapi.do , https://www.data.go.kr/data/15157220/openapi.do , https://www.data.go.kr/data/15157252/openapi.do , https://www.data.go.kr/data/15157254/openapi.do
