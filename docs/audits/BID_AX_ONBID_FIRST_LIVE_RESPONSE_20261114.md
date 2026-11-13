# BID AX 사용자 PC 첫 온비드 실제 응답 — 보안 진단 후속 (2026-11-14 KST)

## 사용자 직접 확인된 사실

- Windows PowerShell/Python3.11에서 온비드 `onbid_result_list` API 15157252를 **1회 `--live` 호출**하여 `local/result_001.json` 저장. 사용자 콘솔 출력: 15,930바이트, 호출 횟수1, `QUARANTINED_UNVERIFIED_OFFICIAL_MAPPING`.
- 저장된 파일을 오프라인 `api-inspect`한 결과 `CANONICAL_RESPONSE_SHA256_MATCH`·`REVIEW_HOLD`·`UNRECOGNIZED_ENVELOPE`. 따라서 **응답 수신과 로컬 검증만 확인**, 실제 온비드 공매 목록 성공/인증키 권한/공식 응답 필드/법적 상용권은 아직 확인하지 못함.
- 사용자 API 키나 실제 JSON 파일은 담당자에게 전달되지 않았으며 정부 API를 추가로 호출하지 않음. 해당 값·실개인정보·원문은 GitHub/크몽 원장에 기록하지 않음.

## 실제 개발·수용

- 제품 코드: `hibi89/Freelancer@product/bid-ax-public-procurement` **`e650fdbe65de25885bef0e6a4eb758c6bd4a1afa`**.
- 기존 검사기는 `response.header/body` 형식만 인정. 이를 근거 없이 성공으로 완화하지 않고, 로컬 SHA/서비스·요청 검증 후 **고정된 공개 필드명·자료형/코드범주만 출력**하는 `bidax/response_shape.py`, `api-shape` 및 단일 `BID_AX_API_SHAPE_DIAG.py`를 추가함.
- Linux Python3.13.5 기존 201 + 신규 7 = **208 PASS /0 FAIL**, 컴파일/3.11 문법 AST PASS, 62파일 ZIP SHA 일치. **실 Windows 진단기 실행 자체와 실 JSON 구조 확인은 아직 NOT_RUN**. 자동 레코드 수용·법적 자격승인/자동 경매 또는 입찰 금지.

## 형이 해야 할 일 (추가 키/API 요청 없음)

기존 로컬 `BID_AX` 폴더에 위 단일 파일을 넣고 `py -3.11 .\\BID_AX_API_SHAPE_DIAG.py` 실행 후 `OFFLINE_SCHEMA_ONLY` 결과 텍스트만 전달. 로컬 `result_001.json` 및 키·고객자료는 외부 업로드 금지.

## 완성률·상태

- 최종설계 29요구 R01–R29 고정; 별도 가중치 승인 다시 요구하지 않음. 85% 전체 달성은 **미입증**. **공식 UNASSESSED, [작업중] 유지, RELEASE HOLD/크몽 미등록**.
- 실제 입찰/온비드 원문·100 실공고/10 인간검토·실 Win10/11 서명 EXE·권리/상용·고객 수용 항목 별도 미검증. 다른 상품·BID OWL·크몽 역사적 목록 변경 없음.
