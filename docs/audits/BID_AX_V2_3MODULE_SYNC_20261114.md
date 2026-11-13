# BID AX v2 3모듈 원격 동기화 및 최종 85% 재검증 — 2026-11-14 KST

- **상품:** CANDIDATE-10 / KMONG-SVC-18 (기존 중앙 원천29·판매19 포함, 중복 판매 신규 등록 없음).
- **저장소:** PRIVATE `hibi89/Freelancer`, 브랜치 `product/bid-ax-public-procurement`; 기능 SHA `2a9852bcb47a271a4119f67dfcaf8ec35ae2a632`, 최신 문서 `d295a8869689272f14a37864716e69093d5ca351`. 기존 원격 기준 `1b7b2ef0c00162905b4d0f4116933f682311fb0f`.
- **실제 변경:** 오프라인 온비드 JSON 물건/결과 원장, 중복·변조·구버전 거부, 법원경매 고객 PDF/TXT 로컬 동의·해시/위험검토, 3모듈 GUI/CLI. 첫 code commit `0b407a9edc363bf7be565356f4e9f64190b3c5f3` 8/8 파일 원격 일치. 두 번째 `2a9852bcb47a271a4119f67dfcaf8ec35ae2a632` 4/4 원격 일치. 온비드 공식형 15157220/15157252/15157254 **요청 계획만**, API 키 없음, 실 HTTP 수행 없음.
- **로컬 검증:** Linux Python3.13.5 `python -Werror::ResourceWarning -m unittest discover -s tests -q` **136 PASS/0 FAIL/0 SKIP**, Python compileall PASS, 3.11 AST22 PASS(문법만), 비출시 .pyz 실제 `onbid-plan result_detail` PASS. Pyz SHA256 `2fe1de178782e3b3e6698630ca4ffc243503dc0a863953f3d6d223d13f61e0f1`; Python 설치 필요, Windows EXE 아님. Github blueprint-only CI는 Python OS CI 아님. Private Actions 비용 가능성이 있으므로 OS 매트릭스 수동 dispatch **미실행**.
- **안전/상용 차단:** 나라장터·온비드 실제 무료 API 계정/응답/운영트래픽/상업적 첨부 원문 권리 미검증. 실제 입찰공고100건·인간 법률/자격10건/실 고객 Windows·실 PDF 추출/멀웨어 검사/권한·암호화/실 EXE·법률 전문가·실 판매 승인 없음. 법원 API 오픈 제공 예정, 허가되지 않은 자동 크롤링 없음. 데이터/토큰 GitHub 전송 0.
- **최종 100% 분모:** 사용자 확정 **R01–R29 29개**. 신규 R22–R29 **부분 코드 구현**으로 전진했지만, 독립 최종 수용 **0/8**. 기존 R01–R21도 완전 수용·최종 가중치 미확정. 사용자 승인 항목별 100점 가중치 부재 → **공식 최종완성률 UNASSESSED**, 목표 85% **[작업중]**, RELEASE HOLD/크몽 미등록 보존. 136 테스트 수/기술 P85를 최종 %로 환산 금지.
- **원천보존:** 기존 29개/19서비스·과거 상품등록/작업중·BID OWL·다른 Freelancer 제품 및 사용자 DB 원본 수정 없음. Git 히스토리 통해 정상 revert 가능, force push/데이터 덮어쓰기 불가.
- **다음:** (1) 본인 API 활용신청·공식 스키마/상업권/승인 후 실 샘플 수집 (2) 실제 Windows 10/11/Python3.11·EXE/PDF·접근권한/고객 인수 (3) 100실공고/10인간 검토 (4) R01–R29 사용자 승인 100점 가중치 수용 후 공식 재산정. 사용자 사전 승인 없이는 유료 워크플로, 계정/보안 변경, 원문 외부 전송, 상품 출시 금지.

공식 출처: https://www.data.go.kr/data/15157220/openapi.do · https://www.data.go.kr/data/15157252/openapi.do · https://www.data.go.kr/data/15157254/openapi.do · https://www.data.go.kr/data/15129394/openapi.do · https://openapi.scourt.go.kr/kgso202m01.do
