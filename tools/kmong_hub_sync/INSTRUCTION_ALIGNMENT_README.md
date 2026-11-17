# 해총 개인지침 충돌 감시 — Read-only Advisory (운영 기능 + PR #5 보강)

**목표:** 기존 중앙 GitHub App 동기화가 실행될 때마다 해총 정책 정본이 변경됐는지 확인하고, 사용자가 **별도로 제공한 최소 구조화 규칙 사본**이 있다면 ChatGPT·Codex 규칙 충돌과 수정 권고를 Actions Summary로 보고한다.

## 핵심 제약

- GitHub App은 ChatGPT 계정의 개인지침이나 Codex 계정·로컬의 전역 지침을 **직접 읽을 수 없다**.
- 개인지침 원문, 비밀·토큰, 고객자료, `.env`를 공개 저장소에 올리거나 Actions 로그로 출력하지 않는다.
- 지침 사본이 없으면 `NOT_VERIFIED_NO_SNAPSHOT`, **절대 자동 일치 판정하지 않는다**.
- 사본이 있어도 사용자가 신고한 규칙 상태일 뿐, 계정에 실제 적용된 사실을 독립적으로 증명하지 못한다.
- 정책 원문 SHA가 기준과 다르면 `CHANGED_REVIEW_REQUIRED`, 원문을 읽지 못하면 `UNAVAILABLE`로 보고한다.
- 충돌 권고는 `instruction_alignment_rules.json`에 공개된 고정 문구만 사용한다. 사용자가 넣은 규칙 값, 원문, 알 수 없는 입력값은 로그에 출력하지 않는다.
- GitHub App 권한·비밀·Production·수집 원장·계정 지침은 **수정하지 않는다**. 이 기능은 알림/권고 전용이다.

## 입력과 검사

- 정책 정본: `kmong-productization/docs/strategy/OWNER_DEV_EXECUTION_CANONICAL_20261116.md`
- 기준 Git blob SHA: `866cebf588d6fa1f7a51ac61878ac60eaafe0b26` (V2.1·병목 §0C 포함)
- 규칙: P0 설계 담당, P1 구현 담당, P2 검증 담당, P3 Astra FE 실제 구현, P4 최종 재검증, P1 브라우저 후행, 병목 재설계, 완성률, 임무 잠금, 소유자 사전 승인 등 10개.
- 실행: `python3 -B tools/kmong_hub_sync/instruction_drift.py --summary "$GITHUB_STEP_SUMMARY"`
- 기존 `kmong-hub-sync.yml`의 완료/연기 결과 **뒤에서** 별도 읽기 전용 단계로 **main에 통합(PR #4)**되어 있으며, 2026-11-17 Actions #44020977616에서 운영 실행까지 확인했다. 기존 동기화의 권한·출처·동작을 변경하지 않는다.
- GitHub Actions 사용자 알림은 계정 설정에 따라 다르므로 **Summary/annotation 생성만 보장**한다. Issue 생성·외부 메시지 전송·계정 지침 자동 수정을 하지 않는다.
- 선택적 자동 비교 입력: 소유자가 별도 승인 후, **원문이 아닌 비민감 규칙 ID/값 JSON만** GitHub Actions secret `HAECHONG_INSTRUCTION_RULE_SNAPSHOT_JSON`으로 직접 등록하면 해당 워크플로 단계만 런타임에 읽는다. 현재 secret 생성·값 등록은 **NOT_RUN**. secret이 없으면 두 지침 모두 `NOT_VERIFIED_NO_SNAPSHOT`.
- 자동 비교는 최신 정책 blob SHA와 레지스트리 핀이 일치할 때만 수행한다. 원격 정책 변경/조회 실패 시 `NOT_EVALUATED_POLICY_UNCURRENT`로 방어한다. 이 권고 스텝의 입력 오류가 기존 Collector 성공을 FAIL로 바꾸지 않도록 `continue-on-error`를 사용한다.

## 선택적 구조화 사본

사용자가 실제 현재 지침을 검토해 **비밀이 없는 규칙 ID/값만 추려** 로컬에서 임시 JSON을 제공할 때 다음과 같이 비교한다. 원문 자체를 올리지 않는다.

```json
{"schema_version": 1, "profiles": {
  "chatgpt": {"rules": {"P2_VALIDATION_OWNER": "codex_sol_max"}},
  "codex": {"rules": {"P2_VALIDATION_OWNER": "legacy_owner"}}
}}
```

`--snapshot /private/local/path.json`은 선택 인수다. 일부 규칙만 제공하면 `INCOMPLETE_SNAPSHOT`, 불일치 규칙은 `DECLARED_CONFLICT`, 값 일치는 `SNAPSHOT_RULES_MATCH`로 표기한다. 어느 상태에서도 실제 계정 설정이 확인됐다고 주장하지 않는다.

## 현재 알려진 지침 이력 주의

기존 `docs/strategy/CHATGPT_CODEX_CUSTOM_INSTRUCTIONS_USER_ACTION_20261116.md`에는 예전 V2 담당 구분이 남아 있다. 현재 해총 V2.1과의 **문서 차이**이며 실제 계정 지침이 여전히 구형이라는 증거는 아니다. 사용자가 계정 지침을 확인한 뒤 수동 교체해야 한다.

## 추가된 검토 자동화 (PR #5 — main 미병합)

1. **입력 안전성:** 지나치게 깊은 JSON은 원문 출력 없이 안전 오류 처리하고, 선택한 로컬 사본 파일은 32 KiB 상한보다 1바이트까지만 읽어 크기 초과를 차단한다. 구조화된 JSON은 정규화된 짧은 규칙 ID/값만 허용한다. JSON 객체의 중복 키(중첩 포함)는 마지막 값으로 덮어쓰지 않고 거부한다. 공개 레지스트리의 예상하지 못한 최상위/규칙 필드와 제어문자도 실패 처리한다. 원문/자유서술·예상하지 못한 키·배열·중복 규칙·잘못된 SHA·줄바꿈을 허용하지 않으며, 민감한 사본 입력값을 출력하지 않는다. 스냅샷은 GitHub Actions secret을 사용하는 **선택 기능**으로만 남는다.
2. **정본 범위 보호:** V2.1의 공개 규칙 10개 ID를 한 개라도 제거·대체하거나 규칙의 `policy_anchor`를 삭제하고도 일치 판정하는 상황을 차단한다. `policy_path`는 현재 정책 파일과 정확히 일치해야 하며, 정책/규칙 개정은 코드 검토와 SHA 업데이트를 동반한다.
3. **소유자 체크리스트:** 규칙 사본이 없거나 일부만 있으면 Actions Summary에 미확인 규칙 ID와 공개 정본의 기대 지침/기대 값을 표시한다. 출력된 기대값을 실제 계정에서 확인하지 않고 그대로 복사해 넣는 것은 검증이 아니다. 조회 불가 상태를 절대 PASS로 표시하지 않는다.
3. **정본 변경 후보 분류:** 현재 정책 Git blob SHA 기준으로 10개 공개 규칙의 `policy_anchor`가 모두 존재하는지 확인한다. SHA가 변경되면 `CHANGED_REVIEW_REQUIRED`, 앵커가 사라진 규칙 ID는 `potential_rule_review_ids`로 우선 표시한다. **앵커가 남아 있어도 의미상 변경 가능하므로 모든 규칙의 최종 수동 검토는 필요하다.** 고정 SHA와 문구가 모순될 때 `RULE_ANCHOR_MISMATCH`로 안전하게 검사를 멈춘다.
4. **Actions 알림:** 선언된 충돌은 warning, 사본 누락은 notice, 입력 오류는 별도 summary 및 warning. 기존 collector 기능 성공을 보조 알림 실패로 FAIL 처리하지 않으며, 알림을 계정에 푸시하거나 수정하지 않는다.
5. **필수 권한:** 승인 없이 repo secrets, GitHub App 권한·설정, 운영 도메인·Vercel, Production, main 병합을 변경하지 않는다.

## 운영/병합 증거

- 기본 read-only 감시기: [PR #4](https://github.com/hibi89/hackathon-command-center-2026/pull/4) **main 병합 및 Actions 실제 운영 확인**. 운영 run [#44020977616](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/44020977616)에서 collector UPDATED 35 repos/80 branches/29 products, instruction policy `CURRENT`, ChatGPT/Codex `NOT_VERIFIED_NO_SNAPSHOT`.
- 위 입력 방어, 세부 규칙 체크리스트, 정책 앵커 분류 등의 개선은 [PR #5](https://github.com/hibi89/hackathon-command-center-2026/pull/5) 브랜치 `feature/haechong-instruction-advisory-visibility-20261117`에서만 구현됐다. **사용자 GO 전 main 병합 금지.** main에 미반영된 기능을 실제 운영 완료로 표현하지 않는다.
- 매회 동기화가 원격 계정 지침을 읽는 기능은 없다. 실제 비교하려면 소유자가 직접 확인한 **비민감 규칙 사본**을 적법한 비공개 경로로 제공해야 한다.
- 실서명 Webhook HTTP200 Ping, 새로운 Production SHA/브라우저 테스트는 이 권고 개선 PR의 대상이 아니다. 과거 별도 E2E 증거와 혼동하지 않는다.

## 로컬·CI 검증

```sh
python3 -B -m unittest discover -s tools/kmong_hub_sync -p 'test_*.py' -v
python3 -B tools/kmong_hub_sync/instruction_drift.py --summary /tmp/instruction-advisory.md
```

둘째 명령은 정본을 **읽기만** 하며 외부 계정 지침은 조회하지 않는다. secret이 없으면 `NOT_VERIFIED_NO_SNAPSHOT`을 결과로 남긴다. 원격 응답 접근 실패 시 `UNAVAILABLE`로 보고하고, 가짜 사본/가짜 PASS를 만들지 않는다.

기존 HMAC 비밀, GitHub App 설치, Vercel Production, 원장 자동 수집 및 상용 등록 승인은 변경하지 않는다.
