# GitHub Trending Daily — 전용 브랜치 운영

- **정본 브랜치:** `github-trending-daily` (저장소 `hibi89/hackathon-command-center-2026`)
- **예약:** 매일 10:00 Asia/Seoul, 자동화 `Automation_019a9e37b9b08191b6064cc37facab22`
- **추가할 파일:** `docs/github-trending/YYYY-MM/DAILY.md`; 신규 월이면 파일을 생성한다.
- **원본 보존:** 2026-11의 기존 11/06~12 내용은 당시 ChatGPT 보고의 **미재검증 요약**으로 남긴다.
- **실행 절차:** 공식 `https://github.com/trending?since=daily` 확인 → 표시 순위 최대 20위 및 미확인 슬롯 기록 → README·LICENSE·최근 커밋 확인 → hibi89 연계 및 독립 크몽 TOP3(가격·기간은 추정) 작성 → 최신 branch/path/blob SHA 조회 → 동일 `DAILY-YYYY-MM-DD` 섹션 유무 확인 → 새 기록만 append/commit → 원격 재조회로 기록과 SHA 확인.
- **충돌/재실행:** 동일 날짜에 여러 번 실행되면 동일 run key의 중복 삽입 금지. 내용 보완은 근거와 수정시각을 붙여 동일 섹션 내 수정. SHA 충돌 시 최신 원본 재조회 후 1회 재시도.
- **아이디어 누적:** 이 브랜치의 `docs/github-trending/PRODUCT_IDEAS.md`만 갱신. 주간·월간 브랜치는 쓰지 않는다.
- **보고:** GitHub 커밋 SHA·저장 경로·미확인 또는 `GITHUB_SYNC_PENDING`을 명시. 자동화 프롬프트 변경만으로 미래 GitHub 쓰기를 보증하지 않는다.
- **보안:** Public repo. 비공개 소스·고객 데이터·토큰·PII·기획상 민감한 내용 금지. 무단 코드·CI·배포·권한·유료 API 변경 금지.
- **월간 연결:** 월간 예약은 이 브랜치를 **읽기 전용**으로 조회해 `kmong-productization`에 월간 통합본을 작성한다. 병합 불필요.
- **복구:** 브랜치 Git 이력으로 이전 정본 복원. 기존 `kmong-productization`/main 원본 보존.
