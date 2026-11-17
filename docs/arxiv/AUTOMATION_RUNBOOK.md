# arXiv 예약 연구 → 해총 GitHub 자동 누적 runbook

**예약 ID:** `Automation_94cd8969ddd081918467dc02bd0a92d3`  
**대상 repo/branch:** `hibi89/hackathon-command-center-2026@kmong-productization` (다른 branch/main/Production 금지)  
**예약 주기:** 화요일·금요일 11:30 KST (`Asia/Seoul`)  
**실행 도구:** 예약 ChatGPT의 공개 웹 조사 + 연결된 GitHub 커넥터 `fetch_file` / `create_file` / `update_file` / branch `fetch`  
**코드·GitHub Actions 신규 workflow 없음.** GitHub Actions `schedule`은 기본 브랜치에서 실행되므로, 이 작업에서 기본 브랜치·CI·권한을 바꾸지 않고 기존 ChatGPT 예약으로 조사/저장을 지시한다.

## 1. 실행시 반드시 수행하는 원자적 단계
1. arXiv 공식 `cs.AI/recent`, `cs.SE`, `cs.DB`, `cs.CL` 등을 공개 조회. 최신 발표 공지일(announced)과 원문 제출일(submitted), 저자 주장/자체 재현 여부 구분.
2. **원격 브랜치 HEAD**와 다음 파일의 최신 `sha`/본문을 먼저 읽는다: `docs/arxiv/YYYY-MM/RESEARCH.md`, `docs/arxiv/RESEARCH_HISTORY_INDEX.md`, `docs/arxiv/PRODUCT_IDEAS.md`.
3. `ARXIV-YYYY-MM-DD` 섹션 및 같은 날짜 예약 run_id 존재 시 결과가 같은지 검사. **중복 실행은 문서 중복 생성 금지**. 신규 논문은 arXiv ID 기준 인덱스 중복을 필터링. 연구 초록·코드/라이선스·기존 프로젝트/상품 후보와 연결하여 사실/분석/제안 구분.
4. 이미 존재하는 파일은 `fetch_file`의 **현재 blob SHA**를 사용해 `update_file`로 기존 내용 전체를 보존하면서 새 섹션/행만 append. 존재하지 않는 월별 파일은 `create_file`. 동시 수정 충돌 시 **새 SHA/내용 재조회 후 1회 재시도**; force push/파일 초기화 금지.
5. 신규 `PRODUCT_IDEAS.md` 항목은 기존 `KMONG-SVC-01..19` 및 원장 기존 후보와 고객 문제를 비교해 **같은 고객 목적은 EXTENSION**, 새로운 고객 문제일 때만 고유 후보 ID 부여. 최초 발견일과 이전 이력 보존.
6. 순차 커밋 후 각각 `fetch_file` 원격 readback, branch HEAD, 최종 `arXiv ID` 및 run_id 개수/기존 내용 보존, 변경 내용·SHA 검증. 변경 없으면 불필요한 커밋 금지.
7. 성공한 파일별 원격 URL, commit SHA, 이번에 추가한 논문 수·후보 수, 실패/미검증 항목을 보고. **일부 저장 성공과 전체 성공은 반드시 구분**.

## 2. 실패·중복·권한 처리
- GitHub 커넥터 미제공/접근거부/재연결 필요/409/422 충돌/호출 실패/원격 readback 불일치: `GITHUB_SYNC_PENDING` + 차단 사유 + 저장하지 못한 내용을 결과 메시지에 남긴다. GitHub 반영 성공 주장 금지.
- 일부 파일만 갱신되었으면 각 파일의 실제 SHA와 나머지 `GITHUB_SYNC_PENDING`을 분리. 복구 시 run_id/ID 조회 후 **미반영분만** 이어 쓴다.
- 중복 run_id가 이미 모두 기록되고 새 유의미한 논문이 없으면 `NO_NEW_RELEVANT`를 보고하고 내용/상태가 같은 불필요한 Git commit을 만들지 않는다.
- 코드/Actions/CI/본체/배포/main merge/권한/비밀/고객 자료/유료 API는 별도 사용자 GO 전 변경·호출 금지. 예약 실행이 상업 승인을 대체하지 않는다.

## 3. 증거 수준과 알려진 제약
- **2026-11-17 수동 연결 테스트:** 14편의 arXiv 조사 보고서를 ChatGPT가 GitHub Contents API로 작성해 remote readback 일치를 확인. 다음 이력/상품/README 파일 역시 각각 remote readback 확인 후 완료 보고.
- **예약 자동 E2E:** 기존 예약 재설정·미래 실행에서 GitHub 도구 사용과 결과 저장 성공 여부는 **2026-11-20 첫 예약 실 실행 이후** 해당 예약 실행 로그 + 실제 GitHub commit/readback으로만 확정한다. 현재 상태 **`SCHEDULED_END_TO_END_NOT_VERIFIED`**.
- 예약 실행 시 GitHub 연결 권한 또는 사용 가능한 도구 범위가 수동 채팅과 다를 수 있다. 저장 불가 시 `GITHUB_SYNC_PENDING`; 사용자가 수동으로 옮겨 적을 것을 당연한 성공으로 간주하지 않는다.
- GitHub Actions 독립 스케줄러, 백그라운드 프로세스/서버, 자동 비밀/토큰 생성은 구현하지 않았다.
