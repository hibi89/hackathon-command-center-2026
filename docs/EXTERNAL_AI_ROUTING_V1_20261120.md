# IAE_dev 외부 AI 라우팅 최종 정책 v1.1 — 2026-11-20 KST

> 사용자 확정 방향: **Hydrogen은 특별한 고난도 사례에만, IAE_dev 내부 하루 20회 상한**, 평상시 외부 AI 지원은 **Gemini 3.5 Flash 계열 우선**. 로컬 AI/검증된 규칙 엔진을 먼저 쓴다.
> 이 문서는 **설계 및 수용 계약**이다. 실제 Google 계정·무료 등급·요청 한도·API 키·호출·과금·원본 전송은 NOT_RUN / ACCOUNT_UNVERIFIED. 모든 외부 AI 기본 OFF, max_spend_usd=0.
> 본 제품 P0: [통합 최종설계](strategy/IAE_DEV_FINAL_BLUEPRINT_V1_20261119.md), [28 REQ·22 SWU·9 P2](strategy/IAE_DEV_IMPLEMENTATION_AND_ACCEPTANCE_V1_20261119.md). 원본 MLA·FFAX·EAI·AXZERO·REQ 정본, F18·Owner 승인, 해총 GitHub App 임무를 변경하지 않는다.

## 1. 모델 현실과 선택

Google 공식 2026-10-08 릴리스 노트에 따르면 `gemini-3.5-flash`는 deprecated, API 요청은 `gemini-3.6-flash`로 자동 연결된다. 사용자가 요청한 **3.5 Flash의 일반 외부 AI 역할을 보존**하되 실제 API 후보는 **`gemini-3.6-flash`**로 검증하고, `gemini-3.8-flash`는 별도 사용자 승인·계정 확인 후 대안으로만 허용한다. *Flash 사용 한도가 넉넉하다*는 경험은 고정된 무료 API 사용량 증거가 아니다.

Hydrogen의 모델 API ID 후보는 `gemini-4-hydrogen`. **20회는 사용자 지정 IAE_dev 내부 보수적 예산**이지 Google 전체 계정/앱/API 공통의 공식 하루 제한이라고 주장하지 않는다. 실제 Google AI Studio API project tier/RPM/TPM/RPD 및 과금 자격은 반드시 확인하며 작은 상한을 따른다. Google 앱 사용량과 API project 사용량은 별개일 수 있고, 다른 프로그램/기기 사용량은 이 로컬 원장만으로 측정 불가.

공식 확인: [Gemini API 변경 기록](https://ai.google.dev/gemini-api/docs/changelog), [모델](https://ai.google.dev/gemini-api/docs/models), [한도](https://ai.google.dev/gemini-api/docs/rate-limits), [가격](https://ai.google.dev/gemini-api/docs/pricing).

## 2. 우선순위와 실제 승인 경로

| 순서 | 경로 | 요청 조건 | 권한 및 실패 |
|---|---|---|---|
| 0 | 기존 검증된 AXZERO capability·캐시·Typed Operator | 실제 artifact 검증, 작업/환경 SHA와 효과 계약 일치 | MLA F18·Owner 준수. AXZERO 미구현이면 OFF |
| 1 | **MLA 로컬 Ollama / Qwen3:4B** + 정적 분석 | 일반 BE/FE 코드 제안, 원인 조사, 로컬 기본 작업 | 무료·오프라인 우선, CPU/RAM/VRAM 한도 |
| 2 | **Gemini Flash 일반 외부 자문** | 로컬 결과 부족 및 공개/합성 비민감 자료로 보조 분석·코드 제안이 실제 유익할 때 | 명시적 사용자 opt-in, 검증된 무료 tier/API 한도/계약, 외부 전송 승인 필요 |
| 3 | **Gemini 4 Hydrogen 특수 자문** | 고난도 P0 모순, 안전·보안 임계 교착, 2+2 격리 이후 재설계 난제, Flash로 해결 안 된 특별 사례 | 추가 **특별 사유와 1회 Owner 승인** 필수, 로컬 내부 20회/rolling24h 상한 |
| 4 | 사용자/승인된 전문 독립 검수 | 비밀·권한·원본·F18 위험·부적합 데이터/모델 한도·실환경 문제 | 해당 SWU HOLD, 독립 READY 진행 |

**Flash 429/503/시간초과 → Hydrogen 자동 승격 절대 금지.** 기본 로컬 안전 대안/재시도 시점 제안·HOLD 우선. Hydrogen은 모델이 잘나온다는 이유로 일반 코딩 루프의 기본 워커가 되지 않는다. AI 응답은 미신뢰 제안이지 코드 실행 승인이나 독립 감사가 아니다.

## 3. Hydrogen 20회 자체 예산·시스템 원장

- 모든 IAE_dev 프로젝트는 **중앙 SQLite WAL one-writer usage ledger**에서 같은 Provider/account-project/model에 대해 중복 차감 없이 집계한다. 다른 앱·계정 이용분은 `EXTERNAL_USAGE_UNKNOWN` 표시.
- **rolling 24h 최대 20건**(사용자 화면 KST, 내부 UTC monotonic/transactional timestamps), 이 중 **긴급용 4건 예약**. 일반 특수 사건은 당일 누적 16건까지 허용, 예약 4건은 별도 긴급 승인만. 예약 포함 총 20초과 불가.
- Hydrogen **한 작업 1회, 동시 호출 1개, 자동 재시도 0회**. send 직전 원자적 `request_id/provider/account_project/model/owner_approval_id/payload_sha/expiry/attempt_state` 예약 → 실제 전송 → 결과/소모량 기록.
- network timeout·모호한 실패·전송 여부 불분명은 보수적으로 `UNKNOWN_CONSUMED`로 집계. 같은 request_id 재시도/중복 소비를 막고, 전송 전 명백한 취소만 반환 허용.
- 공급자 API 실제 한도가 20보다 낮으면 **실제 확인된 더 낮은 한도** 적용. Google의 리셋 시간이 KST라고 가정하지 않는다. 로컬 자체 rolling24h는 추가 보호 상한이다.
- API 비활성·무료 여부 미확인·자격 없는 모델·잔여량 0·예산 불명·계정 미확인 → **OFF/HOLD**, 자동 유료 전환 금지.

## 4. Flash 일반 지원 규칙

- `requested_label=Gemini 3.5 Flash`, `proposed_effective_api_model=gemini-3.6-flash`. 실제 이용 가능한 API model ID/response model ID를 조회해 pin한다. 3.8 Flash/Lite를 조용히 대체하거나 모델 string을 무검증 고정하지 않는다.
- 분당 요청(RPM), 토큰(TPM), 일간(RPD), free tier 및 비용 통제를 **해당 사용자의 프로젝트**에서 읽기 전용으로 확인하기 전 `FLASH_DISABLED`.
- 401/403/404/계정 요금제 오류 → Flash만 OFF, 429 quota → 제한적 백오프 또는 HOLD, 503/timeout → 중복 전송 방지를 우선. 재시도 정책과 소비는 실제 계정 한도를 따로 적용.
- 무료·$0 상한이 검증되지 않으면 호출하지 않는다. Google Search Grounding의 일일/월간 한도를 **Flash 모델 API 호출 RPD와 혼동하지 않는다**.

## 5. 원본 보호, 보안, 비용

- **기본값:** `external_enabled=false`, `hydrogen.enabled=false`, `flash.enabled=false`, `max_spend_usd=0`, `network_egress=deny`. 설계 승인만으로 API 키 등록/외부 호출/비용·출시 GO를 얻지 않는다.
- 사용자가 매번 **공개/저작권 확인된 비민감 자료 또는 합성 입력**의 redaction report, exact payload SHA, 요청 대상/모델, 목적, account tier/잔여 quota·무료 검증 결과를 보고 승인해야 한다.
- 고객/비공개 repo 원본·토큰·`.env`·비밀·개인 이미지/프롬프트·고객 데이터·원본 경로·권리 없는 자료 업로드 금지. 비밀 제거/권리·원본 SHA 입증 실패 → BLOCK.
- 호출 결과는 `UNTRUSTED_PROPOSAL`. 외부 AI에게 shell/파일쓰기/Git push/main/DB/권한/승인 부여 불가. MLA의 Zero-VM/CodeShield/F18/Owner 및 별도 실제 테스트/감사를 통과해야 한다.
- 실제 모델 공급자별 policy/약관·데이터 보존·과금 조건이 바뀌거나 계정 tier 승격 시 실행 전 다시 검증. 자동 결제/과금계정 연결 금지.

## 6. IAE_dev 구현 책임과 계약

**ProviderRequestV1**: `request_id, project_id, source_sha, provider_role, requested_model_id, data_class, owner_approval_id, sanitized_payload_sha, quota_snapshot, free_tier_receipt, max_cost_usd, deadline_ms, attempt_id`.

**ProviderResultV1**: `request_id, actual_response_model_id, status, reason_code, source_sha, response_digest, usage_tokens, cost_usd, duration_ms, consumption_state, untrusted_proposal_ref`.

- **IAE_dev**: `adapters/external_ai/**`, `service/approval/**`, `service/storage/**`, `service/metrics/**`, `app/ui/providers/**`에 provider registry/무료 검증/중앙 원자 ledger/UI/egress 증거. 외부 호출은 권한이 아니라 MLA의 approved-work scope에 종속.
- **MLA**: 실제 작업의 유일한 authoritative Controller·Owner/F18. 모델/어댑터 응답은 권한 없는 조언; MLA source 실행을 대체하지 않는다.
- **EAI**: 비권한 advisor만. EAI 자체 Hydrogen API 호출을 IAE_dev가 자동 활성화하지 않고 그 밖 사용량을 IAE_dev 원장에 포함했다고 주장하지 않는다.
- **AXZERO**: 검증된 정형 업무 무AI 실행의 특화 엔진, **외부 모델 유료/계정·F18 규칙을 우회하는 대체 수단 아님**.
- **UI**: 각 모델 실사용 가능·OFF·429, 요청 사유, 무료 확인, 외부전송 승인 상태, 모델 ID, 사용량(알려진 것만), Hydrogen rolling24h used/critical reserved/remaining, 실행/모델 제안·실제로 검증한 PASS 분리.

## 7. 기존 개발 분모/검증 게이트 유지

본 개정은 **기존 28 REQ·22 P1 SWU·9 P2 게이트의 세부 수용조건 확장**이며 기능을 삭제하거나 분모를 부풀리지 않는다.

- REQ-05/09/10/17/26/27/28: egress owner approval·free tier·provider model migration·실 quota·정확 증거.
- SWU-006/007/018/019/020: provider router capability/MLA 연결, 보안 egress, 원자 usage ledger, provider UI. 추가 API/file scope는 각 SWU allowed_paths에 포함.
- P2-05/06/09: 비밀·401/403·429·무료 실패·20차/21차 호출·긴급 4건·다중 프로세스 충돌·전송불명·재부팅·모델 이관·OFF·Flash 429→Hydrogen 미자동 전환 실제 회귀.
- 최초에는 **전부 mock/synthetic provider**로 검증하되 실제 라이브 API는 사용자 별도 승인 전까지 `NOT_RUN`, synthetic PASS를 라이브/실사용 PASS로 승격 금지.
- **2026-11-30 일정은 목표이지 완료 보증이 아님.** 외부 provider 부재/OFF여도 MLA→FFAX→REQ/Actions 핵심 경로 정상이어야 한다.
