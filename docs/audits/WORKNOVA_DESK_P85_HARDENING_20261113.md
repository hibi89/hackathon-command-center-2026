# WORKNOVA Desk P85 추가 하드닝 — 해총 중앙 증빙 (2026-11-13 KST)

* 정본: Private `hibi89/Freelancer@product/worknova-desk-local`, 정확 소스/문서 HEAD [affb062c6251bc5ff253a8d855c7672298afe39d](https://github.com/hibi89/Freelancer/commit/affb062c6251bc5ff253a8d855c7672298afe39d); 선행 `7fdea1bf0d031fcd4d500d2f3b31d59a49e99124`.
* 요청: 사용자 최종85% 목표. **공식 최종설계 100% 승인 가중치 및 WD01..14 전 항목 수용 증거 미비, UNASSESSED**. 목표 미달, `[작업중]` 유지. `RELEASE HOLD` / 실제 크몽 미등록, 출시 승인 없음.
* 신규: 오프라인 SHA 체크포인트(기본 여섯 테이블 레코드 실제 해시/감사 헤드/카운트), 사용자 지정 별도 보호 SHA 검증, 변조·중복·가짜 무결성 차단. 포터블 v2 정확 열 개 소스 파일 ZIP/설치/시작 전 해시·경로 검증. Python 필수, 미서명·EXE 아님. 기본 원화/VAT·인간승인·계약·단계·수금·한국어 문서·GUI는 그대로.
* 구조 선택: hosted/cloud notarization은 외부 비용·송신·권한 부담; 사용자가 분리 보관하는 오프라인 체크포인트는 월 서버비 없음. 동일 공격자가 DB·체크포인트·제시 SHA를 모두 제어하면 변조 방지 불가능. 개인정보 평문은 체크포인트에 저장하지 않음.
* 실제 독립 Linux Python3.13.5 `PYTHONPATH=. python -m unittest discover -s tests -q` 68 PASS/0 FAIL/0 SKIP(기존52+신규16); `xvfb-run -a python tests/gui_smoke_xvfb.py` GUI PASS; `compileall` PASS; ZIP 새 폴더 해제 후 별도 검증 PASS. 정확 Git blobs 14/14 체크. 기능 코드 SHA와 문서 SHA 동일 커밋.
* Windows10/11 실제 PowerShell 설치/업그레이드/롤백/제거, Windows Python3.11·Tk·Word/PDF 인쇄, 고객 10사례, 폰트·상용 권리, Windows/호스티드 제품 CI, OS DB 접근통제/암호화, 서명 EXE·Production 전부 NOT RUN/미검증. GitHub 기존 정책-only gate는 제품 Windows QA 아님.
* 복구: 이전 P85 Git SHA로 코드 checkout 가능, 고객 SQLite 파일/마이그레이션 덮어쓰기 금지. 다른 프로젝트의 진도·등록이력·PayPal 원형 불변. 상세 근거 Private `Freelancer/docs/P85_HARDENING_20261113.md`.
* 다음: 사용자 계정/파일 권한·실 Windows 설치/복구, 한국어 문서 권리, 인수 고객 테스트 및 승인된 WD01..14 100점 분모 확보 후에만 공식 85% 판정.
