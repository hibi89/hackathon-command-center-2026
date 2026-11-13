# BID AX v2 85% 목표 — 로컬 구현 후 코드 GitHub 미반영 (2026-11-13 KST)

- **정본**: hibi89/Freelancer@product/bid-ax-public-procurement, 최종설계 R01–R29 (사용자 확정), CANDIDATE-10, KMONG-SVC-18.
- **실제 개발**: 오프라인 로컬(임시 컨테이너) `bidax/onbid.py`, `bidax/court.py`, CLI·Tk GUI 확장, 합성 예시, 36개 신규 테스트. 온비드 사업자 키/실 JSON은 미검증; 법원 PDF는 비실행 해시만·TXT 키워드 언급만, 법적 권리분석 없음.
- **로컬 시험**: Linux Python3.13.5 기존94+신규36=**130 PASS/0 FAIL/0 SKIP**, compileall, Xvfb/Tk 3모듈 GUI controller, 비출시 Python zipapp 실제 CLI import/report PASS.
- **GitHub 원격**: 소스 기준 직전 `42fa2aaa3e7077721ebfeb10f9bacc09ad109a8b`, 확장 설계 `ab0d92a333a18e01a585a99d6a6b5812ab0c6305`, 최신 제품 문서 `1b7b2ef0c00162905b4d0f4116933f682311fb0f`. **새 기능 코드/테스트 파일은 GitHub 미반영**. 새 문서는 로컬 결과와 대기상태의 기록, GitHub CI SUCCESS나 Windows 인증 아님. 외부 API 호출0, 실제 고객자료0.
- **최종 수용**: R22–29 신규 8개 중 정식 실 API·고객·권리·Windows 요구 충족한 항목 **0/8**. 최종 29개 가중치 총100점 승인 없음 → **공식 final UNASSESSED (85% 달성 미입증)**, 사용자 요구 85% **[작업중] 유지**, RELEASE HOLD/크몽 미등록.
- **다음**: 로컬 원본 ZIP/변경 소스 전체를 기존 제품 브랜치에 정확 코드로 동기화→SHA readback→기존 130테스트 동일 원격 checkout 및 독립 Windows/Linux CI→온비드 승인 공식 데이터·쿼터/계약→법원 고객 문서·malware/PDF 파싱 보안/전문가→Windows/고객 인수·승인 100점 가중치.
- **보존**: 기존 온비드/법원 설계 v2, 원본 나라장터 코드, 제외 BID OWL, 기존 29종 원천/19 판매 SKU 및 다른 제품의 공식률/마커/등록완료 이력 불변.
