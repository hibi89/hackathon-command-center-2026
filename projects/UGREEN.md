# UGREEN NAS AI Hackathon — NAS 프로젝트 파일 관리 Skill (잠정)

- 공식 페이지: https://ugreenhackathon.devpost.com/
- 참가: **2026-10-24 KST Devpost 참가 등록 완료 화면 확인** — `Thanks for registering!` 문구 및 `My hackathon projects`/`Create project` 표시. 백엔드·이메일 별도 확인 전.
- 전담 GitHub: [`hibi89/hibi89-ugreen-nas-hackathon`](https://github.com/hibi89/hibi89-ugreen-nas-hackathon) **2026-10-24 생성·5브랜치 운영 파일 직접 검증** (Public).
- 대회 총괄 브랜치: `lead/ugreen` 및 [상위 해커톤 총괄 보고서](https://github.com/hibi89/hibi89-ugreen-nas-hackathon/blob/lead/ugreen/docs/roles/lead/TO_HACKATHON_LEAD.md) 생성. **별도 AI 채팅 역할 아직 배정 전, SDK·실 NAS 미검증**.

## 후보 기능
1. 프로젝트별 필수 파일 누락 탐지.
2. 중복 및 버전 충돌 탐지(사용자 승인 없는 삭제/이동 금지).
3. 개인정보/민감정보의 로컬 노출 위험 감지(무단 외부 전송 금지).

주제는 미확정. 공식 Uliya Skill 규격·CLI·NAS 권한을 먼저 검토하고 개발가능한 최소 범위를 확정한다. 실제 NAS 테스트 없이 작동을 확언하지 않는다.

## Round 1
- 공식 예선 마감 **2026-11-16 16:45 KST** (11/15 23:45 PST).
- 영어 PDF 500단어 이하(10가지 질문 답변), 1MB 이하.
- 표준 Pre-test Skill ZIP: SKILL.md 중심, 직접 연결된 참고 Markdown만 허용.
- ZIP 압축/해제 10MB 이하, 각 파일 1MB 이하, 100개 이하.
- 별도의 manifest/script/executable/binary 미허용. 보안·라이선스 요건 준수.
- 1차 단계 실제 NAS 실행은 필수가 아님.

## Round 2 (진출 시)
- 현지 날짜 11/21: 최대 30팀 발표/안내 예정.
- 현지 날짜 11/22~28: 팀별 하루 원격 NAS 테스트 배정.
- **2026-12-01 16:45 KST** 최종 Skill ZIP과 3분 이내 공개 YouTube 실행 영상 제출.
- 실제 NAS 실행을 별도로 검증해야 함.

## 체크리스트
- [x] Devpost 참가 등록 후 성공 메시지 및 프로젝트 관리 화면 확인
- [ ] Skill Developer Package 확보·규격/권한 확인
- [ ] 주제 확정과 위험 관리
- [ ] 500단어/1MB 제한 영문 PDF
- [ ] 공식 ZIP 규격·용량·파일 개수 검사
- [ ] 공식 예선 제출 증거
- [ ] (본선 시) NAS 실작동·영상 재현 검증

내부 목표: 10/24~26 등록·규격 검토, 11/06~09 패키지 초안, 11/13~15 제출 검증.

## 2026-10-24 KST — 참가 확인 근거·다음 단계
- 사용자 스크린샷에서 UGREEN Hackathon의 `Thanks for registering!` 배너를 직접 확인. **참가 등록 완료**, **작품 생성·실제 제출은 아직 시작 전**.
- 사용자 등록 시 관심 트랙은 `Automate Your Workflow`로 선택. 이 선택은 추후 Skill 아이디어 최종 확정을 의미하지 않음.
- 다음 작업: 공식 UGREEN Skill Developer Package 확보/규격 조사 → 주제 A/B안 평가와 사용자 승인 → 500단어 이내 영문 PDF와 유효한 `SKILL.md` 중심 ZIP 제작.
- 실제 NAS 실행은 예선 필수가 아님. 본선 진출 시 원격 장비 테스트 후 검증.

## 2026-10-24 KST — 공식 Finalists 선발 규모
- [공식 UGREEN Rules](https://ugreenhackathon.devpost.com/rules)에 예선 상위 **최대 30개 프로젝트**가 Finalists로 선발된다고 명시됨.
- 본선은 11/21 PT 이메일 통지, 11/22~28 PT 중 지정 1일 무료 원격 NAS 테스트, 12/01 16:45 KST 최종 ZIP/영상 제출, 최종 **5개 수상작**(1·2·3위 각 1개 + Most Creative 2개).
- 현재는 Devpost 참가 등록 화면만 확인. **예선 PDF·ZIP 제출/본선 진출/수상은 모두 미발생**.

### UGREEN — 2026-10-24 GitHub 5개 브랜치 운영 구조 검증
- 저장소: [`hibi89/hibi89-ugreen-nas-hackathon`](https://github.com/hibi89/hibi89-ugreen-nas-hackathon) (Public); `main` HEAD `33e8ccf0226f6b108b6922f478004562cd3d53bf`, `lead/ugreen` HEAD `8566f0c70d04d459ad71d088d58e59156387d0f4`.
- `feature/missing-files` HEAD `fec871916e14aa6d56d8964cad912f2b253aa825`
- `feature/version-conflicts` HEAD `48ef0bbda3f347b43533ffab4642511444b1dac5`
- `feature/privacy` HEAD `b4a6dd098d06c41ea3f59ffe79494fa1e0a13d34`
- 총괄 고정 상위 보고: [`lead/ugreen/docs/roles/lead/TO_HACKATHON_LEAD.md`](https://github.com/hibi89/hibi89-ugreen-nas-hackathon/blob/lead/ugreen/docs/roles/lead/TO_HACKATHON_LEAD.md).
- **검증**: GitHub 5/5 브랜치와 각각 필수 운영·인수인계·메시지 문서 전수 확인. **코드/CI/실 API/배포/최종 제출은 없음.** 제품 주제·기능은 사용자 최종 승인 전 잠정. 대회별 AI 총괄 채팅방은 아직 생성됐다는 증거 없음.
