# GitHub Trending 예약 리서치·브랜치별 누적 기록 정책

> 2026-11-13 KST 사용자 직접 지시로 기존 `새 브랜치 금지/모든 보고 kmong-productization에 저장` 규칙을 변경했다. **동일 저장소의 일간·주간 전용 브랜치만 신규 생성.** 월간은 기존 총괄 브랜치를 유지한다.

| 구분 | 자동화 | 일정 (Asia/Seoul) | 정본 브랜치 | 정본 기록 |
|---|---|---|---|---|
| 일간 TOP20 | `Automation_019a9e37b9b08191b6064cc37facab22` | 매일 10:00 | `github-trending-daily` | `docs/github-trending/YYYY-MM/DAILY.md` |
| 주간 TOP30 | `Automation_b505a8e8b1d88191997b8e5654e7e51a` | 월요일 10:30 | `github-trending-weekly` | `docs/github-trending/YYYY-MM/WEEKLY.md` |
| 월간 TOP30 | `Automation_94cd8969ddd081918467dc02bd0a92d3` | 매월 1일 11:00 | `kmong-productization` | `docs/github-trending/YYYY-MM/MONTHLY.md` · `MONTHLY_INDEX.md` |

## 데이터 흐름
1. 해당 기간 공식 `github.com/trending?since=daily|weekly|monthly`를 조회하고 표시된 실제 순위를 보존한다. 부족한 순위·스타 증가·README·LICENSE·최근 커밋은 미확인 표시한다. 대체 집계는 공식 순위와 섞지 않는다.
2. 저장소명/URL·기능·사례·인기 근거, 라이선스·상업 재배포 제약, 지난 보고 대비 변화, hibi89 기존 제품 연계와 **독립** 크몽 상품 TOP3(고객/납품물/추정 가격·개발기간/난이도/차별화/검증)를 구분하여 작성한다.
3. **쓰기 분리:** 일간 자동화는 일간 브랜치만, 주간 자동화는 주간 브랜치만, 월간 자동화는 총괄 브랜치만 수정한다. 주간은 일간 브랜치를 읽어 비교하며, 월간은 일간·주간 브랜치를 읽어 종합한다. **Git 브랜치 자동 병합은 하지 않는다.**
4. 각 예약 실행은 해당 정본 기록의 최신 blob SHA를 먼저 조회하고 run key(`DAILY-YYYY-MM-DD` / `WEEKLY-YYYY-MM-DD` / `MONTHLY-YYYY-MM`) 중복을 확인한다. 중복이면 별도 중복 추가하지 않고 필요한 근거 보완만 안전하게 수정한다. 충돌 재조회 후 1회 재시도한다.
5. 실제 commit SHA와 원격 파일 readback을 확인해 기록한다. GitHub 연결·권한·중복·충돌 문제로 기록하지 못하면 `GITHUB_SYNC_PENDING` 및 원인을 보고한다. **예약 프롬프트만으로 미래 자동 저장이 검증되었다고 주장하지 않는다.**
6. 월간 총괄 문서의 `DAILY.md`, `WEEKLY.md`는 2026-11-13 이전 자료의 **역사적 스냅샷**이다. 해당 위치에 새로운 일간·주간 보고를 추가하면 안 된다. 각 전용 브랜치 정본만 새 자료를 보관한다.

## 보안·장애 복구
- 저장소는 Public이므로 비공개 제품 코드·고객 데이터·토큰·개인정보·전략상 민감 정보를 기록하지 않는다. 다른 제품 코드·완성률·배포·권한·CI 변경 금지.
- 외부 유료 API·새 GitHub Actions workflow·토큰 발급·권한 확대를 자동으로 수행하지 않는다. 추가 자동화 인프라가 필요하면 사전 승인을 받는다.
- 미검증 인용·상품 가격·기간은 제안으로 표시한다. 상품 판매 전 라이선스·실행 환경·품질·권리를 다시 확인한다.
- 이력 복구: 각 브랜치 이전 commit을 확인해 개별 문서만 복구하며 force push나 브랜치 삭제를 하지 않는다.

## 수익화 후보·조사 저장소 누적 보존 (2026-11-13 추가)
- 이전 조사에서 정리한 30개 후보는 `docs/github-trending/MONETIZATION_IDEAS_MASTER.md`, 언급된 69개 저장소는 `RESEARCH_HISTORY_INDEX.md`에 중복 제거해 기록했다. 이전 보고의 사실/라이선스/랭킹을 새 검증 없이 확정하지 않는다.
- 일간/주간 예약은 **매 실행마다** 각자의 브랜치 내 `PRODUCT_IDEAS.md`에 기존 항목과 중복되지 않는 상품화 후보 및 각 후보의 원본 repo, 조사일, 고객, 납품물, 추정 가격/기간, 라이선스 미확인 여부, 위험/다음 검증을 누적한다. 동일 브랜치의 `RESEARCH_HISTORY_INDEX.md`에 신규 조사 프로젝트·URL·조사일·검증 등급을 중복 없이 기록한다.
- 월간 예약은 일간·주간 브랜치를 **읽기 전용** 조회해 `kmong-productization`의 `MONETIZATION_IDEAS_MASTER.md`, `PRODUCT_IDEAS.md`, `RESEARCH_HISTORY_INDEX.md`를 통합·갱신한다. 출처·기존 ID·이전 평가를 보존하고, 재추천은 새 근거가 있을 때만 추가. 날짜별 보고 파일은 별도 보존.
- 장기 마스터의 중앙 정본은 `kmong-productization`. 일간·주간 브랜치의 동일 명칭 `MONETIZATION_IDEAS_MASTER.md`는 **2026-11-13 기준 스냅샷**이며 일별 최신 중앙 동기화가 아니다. 주간/일간의 신규 후보는 `PRODUCT_IDEAS.md`를 확인한다.
- 자동화 편집은 기존 기록 덮어쓰기 전 최신 blob SHA 확인·동일 repo/상품 ID 중복 제거·GitHub 원격 readback 검증. 실패 시 `GITHUB_SYNC_PENDING`. 자동화 성공을 실제 실행 전 확정하지 않는다.
