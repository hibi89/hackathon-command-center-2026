> [2026-11-14 공통 키 API 연결기 최신화] 사용자 4개 무료 API 신청 완료·인증키 동일. 제품 SHA e3ffb4fa1a6c20f640746f990cef5f0f9e88f8b3, 실 키/HTTP 없이 mock 188/188 PASS, 고정 호스트·비밀 누출/중복 차단·수동 원문 격리. 15157220 경로 미확인으로 라이브 차단. 최종 R01–29 85% 미입증/UNASSESSED, [작업중]/HOLD, 별도 가중치 승인 요청하지 않음. [중앙 상세](BID_AX_SHARED_KEY_API_GATEWAY_20261114.md).

# BID AX — R01–R29 최종완성률 85% 목표 실검증 경과 (2026-11-14 KST)

## 범위 · 근거
- 최종설계: 나라장터 입찰 + 온비드 공매(공식 무료 API 대상) + 고객 적법 확보 법원경매 문서 로컬 분석, 기존 21+추가 8 = 29개, 사용자 정본 변경 없음.
- 제품: Private hibi89/Freelancer@product/bid-ax-public-procurement, 최신 SHA `04d5b5e563be70ff32b08e49ea46c6e3f37693e9`, 기능 커밋 `8aa19f3aa4873ff17ecc188a097bd1c59f146a7b`. 정확 원격 소스 `bidax/{portfolio,cli,desktop}.py`, `tests/{test_portfolio_watchlist,test_portable}.py` 모두 Git blob **5/5 로컬 sha와 일치**.
- 로컬: Linux Python3.13.5 `python -Werror::ResourceWarning -m unittest discover -s tests -q` **167 PASS/0 FAIL/0 SKIP**; compileall PASS, Tk8.6 Xvfb smoke PASS, zipapp subprocess 이용한 합성 공고/온비드→통합 보고→관심 상태 감사 PASS.
- 핵심 변화: R26 가격/유찰/유형 필터·관심/해제·UUID 멱등·원문 버전변경 다시 검토; R29 G2B/ONBID/COURT namespace 격리 요약, 타 SQLite DB 자동 변경 금지; 기존 입찰/공매/법원 기능 보존.
- 상세 전수표: https://github.com/hibi89/Freelancer/blob/product/bid-ax-public-procurement/docs/BID_AX_FULL_BLUEPRINT_29_ACCEPTANCE_20261114.md

## 최종완성률
- 사용자 승인 전 R01–R29 **100점 가중치 제안**을 문서로 제시했을 뿐 공식 배점 미승인. 현 단계에서 임의 85% 부여 금지.
- 공식 `UNASSESSED`, 사용자 목표 `85% [작업중]` 계속, `RELEASE HOLD`, 크몽 미등록. 167개 테스트/167 통과는 **로컬 기술 검증**이지 최종설계 85점이 아니다.
- 실 나라장터/온비드 인증키·응답·첨부/100실공고·인간검토10, 실제 Windows10/11 EXE/고객 수용·API권리/상용약관 미검증. Private GitHub Actions Python OS 매트릭스는 과금/승인 문제로 수동 실행하지 않음. 기존 blueprint-only Actions SUCCESS는 Python/Windows 기능 CI 아님.

## 사용자 개입과 다음 개발
- 독립 개발 가능: 동의 받은 고객 PC 기준 데이터 격리·감사/오류복구·로컬 GUI/보안 테스트, 무료 API의 정적 계약 검토, 법원 오프라인 자료 검토 보조.
- 사용자 승인/환경 필요: 본인 공공데이터포털 무료 API 활용신청·실호출 권한, R01–R29 최종 100점 배점 확인, 고객 소유 Windows 실장비/원문/권리/최종 판매 승인. 키/개인자료를 채팅이나 GitHub에 공유하지 않는다.
- 외부 API 호출·유료 CI·고객 원본 업로드·판매 게시/배포·환경변수/기존 저장소 보호설정 변경은 하지 않음.
- 기존 원천29종, 판매후보19, 다른 상품 상태와 등록완료 이력·BID OWL 제외정책 그대로 유지.
