# BID AX API 응답 계약·보안 감사 / 전수 설계 R01–R29 수용 상태

**기준 2026-11-14 KST.** Product private `hibi89/Freelancer@product/bid-ax-public-procurement`, latest verified HEAD `fbac278dd21f48cea13a8f2f491585f053e630b9`. 원천 CANDIDATE-10 / Kmong SKU 후보 KMONG-SVC-18. **제품 85% 목표, 최종완성률 UNASSESSED, [작업중], 출시 HOLD / 미등록**.

## 실제 개발·검증

- 온비드 결과 목록/상세와 나라장터의 고객 공통키를 이용하는 수동 전송기에, 공식 JSON 응답 격리본을 **키 없이 로컬 검사**하는 `bidax/response_audit.py` 추가. 계정 키 문자열은 미수신·미저장/전송0. `api_gateway.py`는 JSON/URL 인코딩 인증키 반사와 민감 필드명 차단, 별도 canonical JSON SHA256(전자서명 아님) 추가. `api-inspect`는 응답/페이지/총건수/중복 JSON/변조/원문 미상 시 REVIEW_HOLD로 전환하고 영구 원장 자동 가져오기 금지.
- Linux Python3.13.5 전체 회귀 **201 PASS/0 FAIL/0 SKIP** (기존188 + 신규13), compileall PASS, `.pyz` 오프라인 명령 smoke PASS. GitHub 기능/테스트/문서 6개 실제 내용 대조 일치; Github blueprint gate 43514650785 SUCCESS(파이썬/Windows CI 아님).
- 정확 SHA 검증 범위 = 코드/로컬 모의·합성. 실 API 호출/상용권리/실 Windows/독립 사람100/10·실 고객 인수 **0/미검증**.

## 85%까지 남은 핵심 수용 항목 (코드와 고객 외부증거 분리)

| 영역 | 현재 | 차단/다음 단계 |
|---|---|---|
| R01–R04 나라장터 API·첨부 | 수동 게이트/7일 오프라인 스테이징 | 사용자 본인 키 현장 실 응답·목록/상세 원문·7일 페이지/첨부 재현 |
| R05–R15 원장·자격/보고·알림 | 다수 로컬 합성 테스트·PDF | 실제 공고·전문가 검토·권한/상시 재가동·실첨부 PDF |
| R16–R18 Windows/보안/설치 | Linux Tk/zipapp, 백업 | Python3.11/Windows10·11/실 EXE·ACL/설치/제거 복구 |
| R19–R21 실증·권리·고객 | 미수용 | 실공고100/인간10·이용허락/법률·고객 파일럿·출시 승인 |
| R22–R26 온비드 | 로컬 정규화/원장·계획·응답 구조 감사 | 15157220 공식 오퍼레이션 경로 확인·15157252/54 실제 응답·증분/계약 검증 |
| R27–R29 법원/통합 | 적법 자료 동의 기반 PDF/TXT 미리보기/3모듈 로컬 격리 | 고객 실제 보유권·문서 위험·Windows/계약 수용 |

**수치판정:** 사용자 지시 R01–R29 **전체 최종설계 100% 기준 고정**, 별도 신규 가중치 승인 요구 금지. 현 단계에서는 각 조건의 실수용 근거 부족으로 공식 최종률 UNASSESSED. 유닛테스트 건수나 내적 P85 목표를 숫자로 승격하지 말 것. 이전 이력 보존, 다른 후보·작업중·등록완료/29→19 제품 분류 변경 없음.

## 다음 작업 및 개입

1. 코드는 인증키 저장 없이 1페이지 API 응답 격리와 원문 구조 점검 준비. 사용자 PC에서 명시적 동의/본인 승인 키로 실제 1페이지 호출 후 원문 필드·권리 확인 필요. **키/원문을 GitHub나 채팅으로 공유하지 않는다.**
2. 실제 원문 파서·페이지/중단복구·첨부/오류 검증, OS·고객/법률·지원/상용 조건을 개별 검증.
3. 최종 85% 독립 수용 근거 전까지 [작업중]/RELEASE HOLD/미등록 그대로.

근거: https://www.data.go.kr/data/15129394/openapi.do ; https://www.data.go.kr/data/15157220/openapi.do ; https://www.data.go.kr/data/15157252/openapi.do ; https://www.data.go.kr/data/15157254/openapi.do .
