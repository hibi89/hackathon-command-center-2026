# GitHub Trending Weekly — 전용 브랜치 운영

- **정본 브랜치:** `github-trending-weekly` (저장소 `hibi89/hackathon-command-center-2026`)
- **예약:** 월요일 10:30 Asia/Seoul, 자동화 `Automation_b505a8e8b1d88191997b8e5654e7e51a`
- **추가할 파일:** `docs/github-trending/YYYY-MM/WEEKLY.md`; 신규 월이면 파일을 생성한다.
- **원본 보존:** 2026-11-09 대체집계 기반 TOP30은 **공식 순위 미확인 과거 보고**로 계속 구분한다.
- **실행 절차:** 공식 `https://github.com/trending?since=weekly` 확인 → TOP30 순서와 증가량/미확인 기록 → README·LICENSE·최근 활동 확인 → 최신 일간 정본 `github-trending-daily`를 **읽기 전용** 조회해 지난 7일 변화·신규 의미 분석 → 기존 hibi89 연계, 독립 크몽 수익화 TOP3 평가 → 대상 브랜치의 최신 blob SHA 조회 → 동일 `WEEKLY-YYYY-MM-DD` 중복 확인 → 해당 날짜 분석만 append → 원격 커밋 SHA 검증.
- **차단·충돌:** 공식 리스트 부족 또는 접근 불가 시 미확인. SHA 충돌은 재조회 후 안전 재시도 1회. 기록 실패 시 `GITHUB_SYNC_PENDING`으로 명시.
- **아이디어 누적:** 이 브랜치의 `docs/github-trending/PRODUCT_IDEAS.md`만 갱신. 일간/월간 브랜치 무단 변경 금지.
- **보안:** Public repo. 비공개 소스·고객 데이터·토큰·PII 금지. 무단 코드·CI·배포·권한·유료 API 변경 금지.
- **월간 연결:** 월간 예약은 이 브랜치를 **읽기 전용**으로 조회해 `kmong-productization`에 월간 통합본 작성. 병합 불필요.
- **복구:** 브랜치 Git 이력 이용. 기존 `kmong-productization`/main 불변.
