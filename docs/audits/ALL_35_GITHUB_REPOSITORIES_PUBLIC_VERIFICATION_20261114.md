# GitHub 35개 저장소 전부 공개 전환 검증 — 2026-11-14 KST

- **범위:** `hibi89` 계정에 연결된 중앙 관측 대상 35개 GitHub 저장소
- **사용자 직접 실행:** Windows GitHub CLI `gh repo edit <owner/name> --visibility public --accept-visibility-change-consequences` 일괄 작업. 사용자 출력 `공개 확인 17 / 17`, `확인 필요 0`; `gh repo list hibi89 --visibility private --limit 100` 결과 0개
- **독립 원격 검증:** 연결된 GitHub `list_repositories(owner=hibi89, page_size=100)` 반환 **전체 35개, PUBLIC 35, PRIVATE 0**. 공개 변경을 이 AI가 직접 실행한 것은 아님
- **이전:** PUBLIC 18 / PRIVATE 17 (전환 전 GitHub 조회); **이후:** PUBLIC 35 / PRIVATE 0 (전환 후 GitHub 조회)
- **시행 승인:** 사용자가 전체 공개를 명시 지시했고 실제 PC CLI에서 실행. GitHub 원격 설정 외에 중앙 제품 코드/브랜치/비밀/등록 이력/평가 가중치 변경 없음
- **비용:** 공개 저장소 **표준 GitHub-hosted runner는 무료**. larger runner와 스토리지, 계정별 과금/차단 정책은 별도. 공식 문서 `https://docs.github.com/en/billing/concepts/product-billing/github-actions` 확인, 해당 계정 과금 화면·한도 자동 해제 여부 **미검증**
- **보안:** PUBLIC 전환으로 과거 Git history/전체 브랜치 및 GitHub Actions 로그의 공개 위험, 외부 포크 가능, push ruleset 비활성화 영향. 공식 `https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility` 참조. `.env`·고객 개인정보·실제 토큰의 현재/과거 커밋과 로그 전수 감사 **미수행**; 원문·비밀 값을 이 문서에 기록하지 않음
- **실 Actions 상태:** 현재 새 공개 설정에서 모든 35개 repo의 업무용 CI를 종단 재실행한 것은 아님. 이전 시간대 수집된 중앙 `Kmong hub cross-repository evidence sync` #43520792229 `success` (`2026-11-13T22:37:28Z`). `Freelancer` final-blueprint #43519727755 `failure`, `data2web_studio` #43520778342 `failure`(모두 공개 전환 완료 로그보다 전 시점의 실행 기록으로 추정, 전환 후 작동 여부의 증거 아님). Failed job은 존재하지만 로그의 원인/과금 차단 여부는 이 감사에서 미판정. **Actions 한도 문제가 해결됐다고 확정하지 않음**
- **저장소 원장:** 기존 29개 제품·19개 후보 SKU·35 repos/80 refs 중앙 수집 설정 유지. 외부 공개를 곧 제품 판매 승인/100점 최종완성률 승인으로 보지 않는다

## 후속 점검

1. **시크릿/개인정보/저작권 최우선:** 비공개 출처 데이터·키·.env·로그·과거 Git 이력, 공개 전환 후 push ruleset 및 공개 download artifact 감사. 발견 시 해당 키는 폐기·재발급하고 해당 저장소 보안 조치를 별도 승인받아 실행한다.
2. **GitHub Actions:** 전환 후 새 정확 SHA에 대한 표준 runner CI를 1개 이상 확인하고 job 할당 여부 및 실패 원인(과금 제한/워크플로 YAML/실제 테스트)을 구분한다. 실패 과거 기록을 해결 성공으로 오판하지 않는다.
3. **해총 관리:** Source Auditor App/Dispatcher App의 설치·권한/Receiver Webhook와 `kmong-productization` 29개 원장·80 refs 실수집을 별도 검증한다. Vercel Production은 종전처럼 미검증.
4. **비용/정책:** 추가 유료 결제·상업적 재배포 라이선스 변경·자동 의존성 다운로드 등을 사전 승인 없이 수행하지 않는다.

**검증 범위:** GitHub 메타데이터 35/35와 이전 Actions 메타데이터, 공식 문서. 실제 저장소 내용 전수비밀 감사/전환 후 CI/실 GitHub App Webhook/Vercel Production은 **미검증**. 중앙 상태 문서 업데이트는 **문서 작업**이지 코드 수정·배포·개별 상품 상태 변경이 아니다.
