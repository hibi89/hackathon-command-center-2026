# KIC — ProofInvest (확정)

- 공식 페이지: https://daker.ai/public/hackathons/kic-ai-agent-competition
- 저장소: https://github.com/hibi89/hibi89-kic-proofinvest (Public)
- AI 책임: KIC 총괄, branch lead/kic
- 참가 상태: 자이언츠파크 1인 참가 신청·팀 생성 화면 확인, 최종 팀 전환 미확인
- 조회 기준: 2026-10-24 KST

## 제품
산업·기업 리서치 → 공시·재무정보 교차 검증 → 설명 가능한 위험 신호 탐지 → 출처와 불확실성이 표시된 투자 검토 보고서.

| 기능 | 브랜치 | 개발 상태 |
|---|---|---|
| 산업 리서치 | feature/research | 역할 문서 준비 / 고유 신규 기능 미착수 |
| 금융정보 검증 | feature/verification | 역할 문서 준비 / 실제 OpenDART API 미검증 |
| 위험 신호 탐지 | feature/risk | 역할 문서 준비 / 공통 합성 계산 스타터 존재 |

## 검증한 GitHub 기준
- main: 9d0d454154a7393627a840113ab811a5b91f121a
- lead/kic: f7f5a25d072d7049eddfef1577d8b9c2134b8325
- research: 76f3089212b76b55d6daad9725b989e8586c3752
- verification: 141dbbaf31487806e5d3d01fc92ecc3667e53ca2
- risk: 0e4d2cf6526c44626bb09c4fe6d30b490ad15ad0
- [main GitHub Actions 성공](https://github.com/hibi89/hibi89-kic-proofinvest/actions/runs/40050488506)
- [lead/kic 최신 HEAD GitHub Actions 성공](https://github.com/hibi89/hibi89-kic-proofinvest/actions/runs/40051624837)
- 초기 Python 오프라인 합성 테스트 9건 통과 보고. 실기업 API/통합 Agent/배포/브라우저 미검증.
- 각 기능 담당 메시지함의 신규 차단/의사결정 요청: 조회 시점 0건.
- **최우선 고정 보고서:** [TO_HACKATHON_LEAD.md](https://github.com/hibi89/hibi89-kic-proofinvest/blob/lead/kic/docs/roles/lead/TO_HACKATHON_LEAD.md) (소유 브랜치: `lead/kic`). 상세 검증은 같은 브랜치의 `docs/roles/lead/STATUS.md`, `HANDOFF.md`, `MESSAGE_REVIEW.md`와 실제 HEAD/CI로 대조한다.

## 제출
- 공식 예선 PDF 10페이지 이내: **2026-11-12 10:00 KST**
- 내부 조기 제출 목표: **2026-11-10**
- [x] 참가 신청·1인 팀 생성 화면 확인
- [ ] 최종 '팀으로 전환' 및 제출 권한 확인
- [x] 기획서 PPTX/PDF v0.1 존재 보고(기존 대화 파일, 공개 저장소에 원본 미게시)
- [ ] 공식 양식 최종 PDF 검수 및 공식 제출 증거
- [ ] (본선 선발 시) 12/22 10:00 KST 실제 데모 URL·GitHub 코드·발표 PDF

## 감독 의견
예선 제출의 핵심은 기획서 품질·공식 형식·접수 성공이다. 실 API 개발의 진도와 예선 제출 완료 여부를 혼동하지 않는다.

## 2026-10-24 KST — KIC 총괄 공식 보고 체계 수신
- KIC 총괄이 `lead/kic/docs/roles/lead/TO_HACKATHON_LEAD.md`를 전체 총괄용 **고정 보고 창구**로 신설하고 누적 작업 이력·최신 현황·위험·승인 대기·일정을 기록함.
- GitHub 직접 확인: `lead/kic` HEAD `f7f5a25d072d7049eddfef1577d8b9c2134b8325`; [동일 HEAD 오프라인 CI run 40051624837](https://github.com/hibi89/hibi89-kic-proofinvest/actions/runs/40051624837) **completed/success**. `main` 및 feature 3개 SHA는 위 표와 동일.
- 전체 PR 목록 직접 조회: 0건. 공식 기획서 PDF 제출·팀 전환은 여전히 확인되지 않음.
- **상위 총괄 확인이 필요한 안건:** KIC 예선 PDF 제출 가능성(팀 전환·접수 버튼 포함), 11/12~19 상호평가 일정 확보, 공통 데이터 계약 A안과 실제 OpenDART 호출은 담당 총괄의 사용자 승인 대기.
- 분업: KIC 총괄은 새 지시 전에 세 기능 브랜치의 `TO_KIC_LEAD.md`를 검토하고 `MESSAGE_REVIEW.md`에 기록. 전체 총괄은 KIC 공식 보고서를 읽고 대회 간 일정·위험을 관리하며 기능 구현에는 개입하지 않음.

## 2026-10-24 KST — 성과 기준
- 공식 **예선 상위 12팀 본선**, 최종 **6팀 수상**. 아직 예선 PDF 제출·팀 전환 완료 증거가 없으며 본선 선발·수상 단계는 **미진입**.
- 상호평가 기간 **11/12~19** 사용자 참여 일정 확보가 필요하다. 구체 투표 조건은 KIC 전담 총괄이 주최 최신 공고를 검증한다.

## 2026-10-24 KST — 구조/일정 재검증 반영
- [역할별 공식 일정 공시](https://github.com/hibi89/hibi89-kic-proofinvest/blob/lead/kic/docs/COMPETITION_SCHEDULE.md) 존재; 5/5 브랜치가 동일한 전체 일정표를 보유하며 README에 링크가 있음.
- 관측 HEAD: `main 1300b9b31a5b86792d15ed7a2dce7c24849dbd87`, `lead/kic 25fe5f60642ad022343da68ae01535713436dcf9`. 세 feature별 최신 SHA는 [통합 검수 보고서](../docs/audits/REPOSITORY_AUDIT_20261024.md) 참고.
- 주제·참가/기능·실 API·실서비스·최종 제출의 기존 상태 **변경 없음**. 문서 링크·검증 개선만 완료.

## 2026-10-24 — KIC 총괄 자체 세부 일정 업데이트
- [AUDIT_EXECUTION_PLAN_20261024.md](https://github.com/hibi89/hibi89-kic-proofinvest/blob/lead/kic/docs/roles/lead/AUDIT_EXECUTION_PLAN_20261024.md) 게시 확인. `lead/kic` 조회 HEAD `d081a59c62e5686fac93f9f0ec97e86f79832ccb`.
- 기획서 중심 A안 65~70% / 소규모 구현 30~35%는 **총괄 제안**. 사용자 확정 아님.
- 10/25 기획서 실물 확인·11/10 내부 조기 제출. 개발/실API/DAKER 최종 제출은 미확인.
