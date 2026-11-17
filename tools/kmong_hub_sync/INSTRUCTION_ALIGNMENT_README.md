# 해총 개인지침 충돌 감시 — Read-only Advisory (기능 브랜치)

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
- 기존 `kmong-hub-sync.yml`의 완료/연기 결과 **뒤에서** 별도 읽기 전용 단계로 실행하도록 준비. 기존 동기화의 권한·출처·동작을 변경하지 않는다.
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

## 병합·검증 범위

현재 기능은 `feature/haechong-instruction-alignment-20261117`에 격리되어 있다. **사용자 GO 전 `main` 병합하지 않는다.** 따라서 실제 GitHub App schedule/dispatch에서 자동으로 실행되고 있다고 주장하지 않는다. PR이 병합되고 기존 Actions를 실제 관찰할 때 최초 실동작을 판정한다.

기존 GitHub App HMAC, Vercel Production, 원장 동기화, 출시 및 권한·보안 정책은 모두 불변이다.
