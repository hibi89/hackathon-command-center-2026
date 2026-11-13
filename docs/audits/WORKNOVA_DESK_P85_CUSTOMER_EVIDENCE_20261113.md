# WORKNOVA Desk P85 후속 독립 감사 — 고객 수명주기·납품 파일 증빙
기준: 2026-11-13 KST · 기존 P85 하드닝 감사 뒤 이은 작업. **공식 최종완성률 UNASSESSED / P85 최종설계 달성 미확정**. `[작업중]`/RELEASE HOLD/미등록 보존.

## 확인된 원본·실행 근거
- Private `hibi89/Freelancer@product/worknova-desk-local` 기능 및 인수인계 HEAD [`6f24ccea44c120391254922f4b0d0801bfbb6e5f`](https://github.com/hibi89/Freelancer/commit/6f24ccea44c120391254922f4b0d0801bfbb6e5f) (부모 `affb062c6251bc5ff253a8d855c7672298afe39d`). 신규/수정 파일 16개, 주요 코드 Git Blob 6/6 로컬 해시 대조 후 실제 원격 HEAD 재조회.
- Linux Python3.13.5 오프라인 `PYTHONPATH=. python -m unittest discover -s tests -q` **81 PASS/0 FAIL/0 SKIP** (기존68+신규13); Tk8.6/Xvfb 실제 위젯 스크립트형 업무 E2E **2종 PASS**; `compileall` PASS; 포터블 ZIP 빌드/추출/12개 소스 SHA 검증/분리 실행 CLI `init` PASS.
- GitHub 기본 Final blueprint completion evidence gate [#43391481138](https://github.com/hibi89/Freelancer/actions/runs/43391481138) **SUCCESS at 동일 SHA**, 단 **문서/증거 정책 게이트**이므로 제품 Python/Windows CI PASS의 근거 아님.

## 새 기능 (기존 최종설계 WD-01..WD-14 범위 내)
- **WD-01 부분**: 고객 이름 변경에는 이전 이름 일치·명시 승인 필수, 이름/이름 해시 감사 로그에 남기지 않음, 동일 값 중복 변경 무해. 거래 내역이 있는 고객 삭제 차단 및 미사용 고객만 확정 요청 시 삭제. 고객 계약·견적·수금 유지. GUI/CLI 지원. 사용자 입력 actor는 인증된 OS 계정이 아님.
- **WD-06 부분**: DELIVERED 상태의 사용자 지정 실제 로컬 파일을 읽기 전용 SHA256/크기 검증(64MiB 제한, 심볼릭/하드링크·읽는 중 변경 거부), 파일명/경로/내용은 DB에 비저장·외부 전송 없음. 동일 파일 중복 방지, 재검증, CLI/GUI 흐름. 파일 해시만으로 외부 전달이나 구매자 승인 증명 **불가**.
- **WD-08/09/13 부분**: 기존 로컬 감사 해시체인/독립 체크포인트/SQLite v2 및 백업 보존. 포터블 Python 필수 ZIP 12파일 원장 최신화. **서명 EXE·윈도우 설치 성공·암호화 인증**에 해당하지 않음.

## 독립 미검증·중단 조건
- 실 Windows 10/11 (PowerShell 설치·업그레이드·삭제·롤백/Defender/Word PDF 인쇄), 한글 TTF 재배포 권리, 다중사용자 접근 제어/스토리지 암호화, 고객 실제 10건 검수, 법률·세무·상업 라이선스·판매 최종 승인 전부 **미검증/미완**. 무단 유료 CI/배포/PayPal 거래/실고객 데이터 전송 없음.
- 최종설계 사용자 승인 항목별 **100점 가중치 부재**, 전체 요구별 정확 인수검증 미완. 따라서 **정식 85% 달성 주장 불가, 공식 완성률 UNASSESSED**. 기존 68 PASS/하드닝 SHA는 과거 기록으로 보존하고 81 PASS가 같은 목표의 더 넓은 *로컬* 검증임을 구분.
- 출시/판매/Production **HOLD·미적용**, 기존 활성 17종·다른 후보 점수와 각 담당자의 [작업중]/등록완료 표식은 수정하지 않는다.

## 복구 및 다음 작업
- 원본 PayPal 해커톤·Freelancer main/타 브랜치 그대로. 백업·고객 DB/폰트/시크릿 변경 없음. 이전 소스 HEAD `affb062c...`로 코드 롤백 가능하나 마이그레이션된 데이터에 구형 라이터 사용 금지.
- 제품 정본: [WD-01~WD-14 P85 후속 추적](https://github.com/hibi89/Freelancer/blob/product/worknova-desk-local/docs/P85_CUSTOMER_EVIDENCE_20261113.md). 다음은 실제 Windows 설치/원복·실고객 10건·OS 보호·라이선스 확인, 승인 가중치 및 수용 조건 확정 후 공식률 재산정.
