# GitHub Trending 예약 보고 → 해총 누적 기록 운영 규칙

- 대상: `hibi89/hackathon-command-center-2026`의 기존 `kmong-productization` 브랜치. **새 브랜치·새 저장소·CI·토큰·배포·권한 변경 금지.**
- 일간: 매일 10:00 KST, 공식 `https://github.com/trending?since=daily` TOP20. 월별 `YYYY-MM/DAILY.md`에 날짜별 append.
- 주간: 월요일 10:30 KST, 공식 `?since=weekly` TOP30. 월별 `WEEKLY.md`에 날짜별 append.
- 월간: 매월 1일 11:00 KST, 공식 `?since=monthly` TOP30. 해당 월 요약 `MONTHLY.md` 작성·갱신, `MONTHLY_INDEX.md` 목차 갱신.
- 매회 공식 순위와 별 증가량, 조회 시각, README/라이선스/최근 활동, 기존 프로젝트 접목, 독립 수익화 TOP3(고객·납품물·추정 가격·난이도·기간·권리·차별화·검증)를 사실/제안으로 구분.
- 공식 페이지가 차단되거나 항목이 부족하면 **미확인** 기록. 대체 집계는 공식 순위로 위장하지 않는다.
- 예약 실행에서 GitHub 쓰기 권한·연결 환경이 없으면 채팅 보고만 생성하고 `GITHUB_SYNC_PENDING`을 명시한다. 자동 저장 성공을 주장하지 않는다.
- GitHub 업데이트는 최신 blob SHA를 먼저 읽고 해당 날짜만 추가. 중복 실행은 동일 날짜·기준시간 식별자로 idempotent 처리. 충돌 시 재조회 후 1회만 안전 재시도, 실패하면 중단.
- Public 저장소이므로 비공개 고객 정보, 개인 데이터, 비공개 소스, 토큰, 경쟁 전략의 민감 세부내용을 게시하지 않는다. 무단 외부 데이터 전송·유료 API·제품 코드 수정 없음.
- STATUS/HANDOFF에 자동화 구성·성공/실패·마지막 검증 시각을 남기되 단순 매일 보고로 불필요한 문서 커밋을 반복하지 않는다.
