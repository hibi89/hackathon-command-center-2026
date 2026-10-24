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
- lead/kic: 3ea8596edbd17cd3dcbbdadf17d9855010d835d9
- research: 76f3089212b76b55d6daad9725b989e8586c3752
- verification: 141dbbaf31487806e5d3d01fc92ecc3667e53ca2
- risk: 0e4d2cf6526c44626bb09c4fe6d30b490ad15ad0
- [main GitHub Actions 성공](https://github.com/hibi89/hibi89-kic-proofinvest/actions/runs/40050488506)
- [lead GitHub Actions 성공](https://github.com/hibi89/hibi89-kic-proofinvest/actions/runs/40050871579)
- 초기 Python 오프라인 합성 테스트 9건 통과 보고. 실기업 API/통합 Agent/배포/브라우저 미검증.
- 각 기능 담당 메시지함의 신규 차단/의사결정 요청: 조회 시점 0건.
- 최신 KIC 총괄 보고: lead/kic/docs/roles/lead/HANDOFF.md, STATUS.md, MESSAGE_REVIEW.md.

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
