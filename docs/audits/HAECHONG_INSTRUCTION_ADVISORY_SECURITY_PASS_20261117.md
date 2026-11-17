# 해총 GitHub App 지침 감시 보강 — 2026-11-17 KST

## 1. 임무와 승인 범위
- 현행 고정 임무: **GitHub App→HMAC Webhook→기존 Vercel→Actions→중앙 원장**. 제품화·새 서비스·Production 변경 아님.
- 사용자 지시: 짧은 상태보고/반복 CI 대기 대신 같은 회차에 독립 작업을 묶어 실코드·수용 검사·커밋·인수인계를 진행.
- 시작할 때 정본 `kmong-productization` 임무 고정(AGENTS/HANDOFF/STATUS), `main@6fdbc1d4ee223e53cd9a6cefa3bf3a8f39d7f437`, PR #5 `open` 검증.
- 기존 자동 동기화의 작동 증거: [Actions #44020977616](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/44020977616) collector UPDATED, 35개 repo/80개 branch/29개 product, 0 unlinked·0 fingerprint alerts; 지침 스냅샷은 두 계정 모두 `NOT_VERIFIED_NO_SNAPSHOT`.

## 2. 실제 코드 구현
- 기능 브랜치: `feature/haechong-instruction-advisory-visibility-20261117`; 후보 HEAD **`6b99987c8341c087b83608ce63b3bf49bc703ab9`**.
- [PR #5](https://github.com/hibi89/hackathon-command-center-2026/pull/5) 4개 파일만 수정: `instruction_drift.py`, `instruction_alignment_rules.json`, `test_instruction_drift.py`, `INSTRUCTION_ALIGNMENT_README.md`.
- 입력 안정성: JSON 최상위/프로필/규칙 형식·길이·정규화 값 검증, 허용되지 않은 자유 입력 차단, 공개 규칙 ID·policy SHA·중복·개행/비정상 anchor 거부. 오류가 나면 원문을 출력하지 않고 권고만 FAIL/CHECK. GitHub Actions collector는 별도 `continue-on-error` 유지.
- 소유자 수정 권고: Snapshot 미제공·일부 누락·선언된 충돌·정본 변경에 따라 Next Action을 분리. 새 Summary에 **실제 계정 설정을 읽은 것이 아닌 공개 정책 기대값**을 체크리스트로 제공.
- 정책 변경 후보: pinned blob `866cebf588d6fa1f7a51ac61878ac60eaafe0b26`과 함께 공개 규칙 10개의 문구 anchor 등록; 사라진 앵커에 대해 우선 재검토 `potential_rule_review_ids` 제시. **앵커가 남아 있어도 의미상 변경은 놓칠 수 있으므로 SHA 변경 시 전수 수동 검토**. 원격 정본/규칙 앵커 불일치 때 계정 일치 검사를 차단.
- CLI/워크플로 회귀: optional secret 없을 때 `NOT_VERIFIED_NO_SNAPSHOT`, 오염 입력을 보낼 때 공개 Summary에 비밀을 출력하지 않고 종료 2. 임의 실제 개인지침 자동 수정 기능 없음.

## 3. 검증/증거
- 초기 103/103 PASS에서 단계별 방어·수동 체크리스트·정본 변경 후보 분류를 추가했다.
- [#44022921634](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/44022921634): 108/108 PASS.
- [#44023088380](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/44023088380): 113/113 PASS.
- [#44023298802](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/44023298802): 118/118 PASS.
- **[#44023492552](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/44023492552): 121/121 PASS** + [Final blueprint gate #44023492689](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/44023492689) PASS.
- 정책 실조회 시 `policy_source_status=CURRENT`, `potential_rule_review_ids=[]`, ChatGPT/Codex 모두 `NOT_VERIFIED_NO_SNAPSHOT` (기대된 안전한 결과).
- PR compare 기준 `main@6fdbc1d4` 앞서 **16개 커밋, 뒤처짐 0, 변경 경로 4개** 확인. 기존 source collector·webhook·Vercel 런타임·workflow·GitHub App 권한 경로 수정 없음.

## 4. 안전·미검증
- **PR #5는 main 미병합**. 테스트 PASS와 실제 운영/상용 기능 활성화는 구분한다.
- 사용자 승인 없는 GitHub App 권한/비밀, Production, 브랜치 보호, main merge, 고객 자료 전송, 비용 발생/서비스 출시 등 변경 없음.
- 사용자의 실제 ChatGPT/Codex 개인지침을 직접 읽을 방법이 없어 자동 충돌 **판정 불가**. 비민감한 규칙 ID/값 사본을 사용자 승인하에 별도 제공한 뒤 재확인 필요. 임의 스냅샷 입력/비밀 전송은 수행하지 않음.
- 새 PR HEAD의 Production 배포/정당 서명 Ping HTTP200, GitHub App 실제 delivery HMAC 인과관계는 이 회차에서 NOT_RUN/NOT_VERIFIED. 과거 성공 이력 재사용 금지.
- P1 제품 구현완료율과 P2 공식 검증완료율은 가중 분모 미확정으로 **UNASSESSED**, 출시 `RELEASE HOLD`.

## 5. 다음 READY와 중단점
1. PR #5 최종 diff/브랜치/검사 결과를 검토한 후 **사용자의 별도 명시 GO**로만 main 병합. 병합 전 기능 추가 구현 가능하지만 무단 main 병합 금지.
2. 병합 후에는 실제 GitHub App→Actions 동기화에서 새 advisory Summary/annotation 표시의 `PASS/NOT_RUN`을 확인한다.
3. 소유자 지침 스냅샷 등록은 별도 사전 승인 필요; 없으면 `NOT_VERIFIED_NO_SNAPSHOT` 유지.
4. HMAC Ping200·현 Production SHA 검증은 정상적인 승인/접근 경로 없으면 분리 HOLD. 동일 실패 방식 두 번 반복하지 않음.

**기준 시점:** 2026-11-17 KST. 증거 기준 main `6fdbc1d4ee223e53cd9a6cefa3bf3a8f39d7f437`, PR #5 `6b99987c8341c087b83608ce63b3bf49bc703ab9`, Actions #44023492552. 본 감사 문서 작성은 제품 코드 진척이나 실제 계정 일치에 가산되지 않는다.
