# 2026 AI 해커톤 통합 상황실

> 기준: **2026-10-24 KST** | 역할: **전체 총괄(전략·일정·품질 감독)** | 실제 참가자: **1명**  
> 이 저장소는 **프로젝트 코드 저장소가 아닌 운영·보고 전용 저장소**입니다. 이 파일들의 내용은 현재 시점의 스냅샷이며 자동 동기화되지 않습니다.

**원격 저장소 공개 범위: Public (GitHub에서 직접 확인). 비공개 전략·인증·미공개 산출물은 여기에 저장하지 않습니다.**

## 대회별 상황판

| 대회 | 주제 | 참가 | 원격 저장소 | 개발·제출 상태 | 공식 제출 마감(KST) |
|---|---|---|---|---|---|
| [KIC](projects/KIC.md) | **ProofInvest** (확정) | 신청·팀 생성 화면 확인, **팀 전환 미검증** | [hibi89-kic-proofinvest](https://github.com/hibi89/hibi89-kic-proofinvest) | 초기 Python 스타터 + 9개 테스트 보고, GitHub Actions 성공. 기획서 v0.1 존재; **미제출** | **11/12 10:00** |
| [PayPal](projects/PAYPAL.md) | AI 프리랜서 계약·결제 Agent (후보) | **Devpost 참가 등록 후 My hackathon projects 화면 확인** | **미생성(조회 기준)** | 주제 미확정, 구현/시연/제출 미착수 | **11/13 05:00** |
| [UGREEN](projects/UGREEN.md) | NAS 프로젝트 파일 관리 Skill (후보) | **Devpost ‘Thanks for registering!’ 및 My hackathon projects 확인** | **미생성(조회 기준)** | 규격·SDK 적용 미검증, 예선 PDF·ZIP 미착수 | **11/16 16:45** |

**성공의 정의**: 공식 유효 제출 → KIC/UGREEN 본선 진출 등 객관적 성과 → 동작 제품·코드·시연 축적 → 상품화. AI 역할 13개는 작업 분담용이며 실제 팀원은 1명입니다.

## 오늘 기준 가장 중요한 판단

1. **KIC**: 예선에서 중요한 것은 **공식 PDF 10페이지 이내 기획서 제출**. 실제 API·배포는 본선 준비 항목; 합성 테스트를 실데이터 성공으로 간주하지 않음. 팀 전환/제출 버튼 확인이 우선 리스크.
2. **PayPal**: 참가 등록 화면 확인 후 주제 확정 및 PayPal Sandbox **실제 작동**이 선행되어야 함. 공개 오픈소스 코드와 실행 가능한 데모, 3분 미만 공개 YouTube 영상은 공식 제출 요건.
3. **UGREEN**: 참가 등록 확인. 실제 NAS 없이 예선 참가 가능. **500단어 이내 영문 PDF(1MB 이하) + 공식 Uliya 표준의 pre-test Skill ZIP** 필수. Round 1 ZIP에는 별도 실행 파일/스크립트/매니페스트를 넣으면 안 됨.

## 운영 문서

- [STATUS.md](STATUS.md) — 최신 총괄 상태 / GitHub 증거
- [SCHEDULE.md](SCHEDULE.md) — 공식 마감·내부 목표·시간대
- [RISKS.md](RISKS.md) — 교차 일정·제출 차단 항목
- [projects/KIC.md](projects/KIC.md) · [projects/PAYPAL.md](projects/PAYPAL.md) · [projects/UGREEN.md](projects/UGREEN.md) — 대회별 상세 기록
- [AGENTS.md](AGENTS.md) · [REQUIREMENTS.md](REQUIREMENTS.md) — 권한 및 운영 규칙
- [docs/REPORT_PROTOCOL.md](docs/REPORT_PROTOCOL.md) — 각 대회 총괄이 보고서를 남길 때 형식
- [HANDOFF.md](HANDOFF.md) — 전체 총괄 인수인계(10항)
- [data/checkpoints.json](data/checkpoints.json) — 간단한 기계 판독용 상태 데이터

## 대회별 공식 보고 진입점
- **KIC:** [`lead/kic/docs/roles/lead/TO_HACKATHON_LEAD.md`](https://github.com/hibi89/hibi89-kic-proofinvest/blob/lead/kic/docs/roles/lead/TO_HACKATHON_LEAD.md) — 2026-10-24 KST 직접 확인. KIC 총괄 HEAD `f7f5a25d072d` CI 성공.
- PayPal·UGREEN: Devpost 참가 등록 화면 확인, 전담 개발 저장소 미생성. 향후 각 담당 총괄의 보고 경로를 확인하면 등록. 향후 담당 총괄의 보고 경로를 확인하면 등록.

## 한 번의 점검 순서

KIC는 전용 `TO_HACKATHON_LEAD.md` → 담당 총괄 `HANDOFF.md`/`STATUS.md` → 브랜치 SHA/CI → 실제 소스·제출 증거 순으로 확인합니다. 전체 총괄은 대회 간 일정·위험·품질만 조정합니다. 대회별 코드나 브랜치를 대신 수정하지 않습니다.

### 출처
- KIC: https://daker.ai/public/hackathons/kic-ai-agent-competition
- PayPal: https://paypalaihackathon.devpost.com/ 및 https://paypalaihackathon.devpost.com/details/dates
- UGREEN: https://ugreenhackathon.devpost.com/

**주의**: '완료'는 근거로 확인된 사실에만 사용합니다. 본선 선발·수상·실API·배포 결과를 추정하지 않습니다.