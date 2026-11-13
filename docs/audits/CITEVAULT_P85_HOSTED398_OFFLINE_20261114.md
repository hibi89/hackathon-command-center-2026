# CITEVAULT AX — 최종설계 P85 추가 실검증 (2026-11-14 KST)

- 제품 기능 SHA: `hibi89/Freelancer@product/rag-enterprise-knowledge` / `0cf969fb2908cca985f4655d2c713ad7e030d168`.
- 제품 STATUS/HANDOFF/24항 추적표 문서 SHA: `fca436f5cc6f58f10f7e41fa8810f1e39d86b1f7`.
- [실제 hosted CI 43525453183](https://github.com/hibi89/Freelancer/actions/runs/43525453183): Ubuntu24.04+Windows2022 **6/6 SUCCESS, 398 test executions PASS/0FAIL/0SKIP** (플랫폼 간 중복 포함).
- [최종설계 정책 gate 43525845785](https://github.com/hibi89/Freelancer/actions/runs/43525845785): SUCCESS (최종 제품 85% 수용 인증이 아님).
- 신규 기능: 명시적 수동 오프라인 SQLite+문서 SHA256 manifest 백업, create-only 복구, 무단 덮어쓰기/변조·symlink/hardlink/경로 탈출·추가 파일 거부. 양 OS 각 **9 PASS**. 서비스 중지·SQLite 닫고 실행하며 운영형 무중단 고객 백업 아님.
- 합성 한국어 질의100회/OS: 근거 검색20, 근거 부족20, 상충20, 무권한 조회20, 혼합권한 요청 거부20. p95 Ubuntu **0.328ms**, Windows **1.001ms**, 작은 합성 코퍼스 기준. Harness는 OS별 1개 Node 테스트로 집계. **고객 승인 Gold100·실 한국어 모델·대용량 성능과 무관**.
- 이전 검증: 정확 pinned 원본 RAG upstream35PASS + CITEVAULT bridge36PASS. 양 OS Windows DOCX UTF8/SQLite EBUSY 해결 상태 유지.
- [백업 증거](https://github.com/hibi89/Freelancer/blob/product/rag-enterprise-knowledge/docs/P85_OFFLINE_SNAPSHOT_20261114.md) · [합성100 증거](https://github.com/hibi89/Freelancer/blob/product/rag-enterprise-knowledge/docs/P85_SYNTHETIC100_EVIDENCE_20261114.md).
- **전체 24항 최종완성률 UNASSESSED / 목표85% 미인증 / CITEVAULT AX [작업중] / RELEASE HOLD / SALE NO-GO**. 실제 고객 임직원 IdP·원본 사용권·승인된 signed PREP/SMAX→AX producer, 실제 Korean pretrained local model, 물리 Win10/11 설치, 고객 Gold100/법무·안전 인수/확정 가중치 미검증.
- 사용자에 의한 `hibi89/Freelancer` 전체 Public 변경으로 타제품 모든 브랜치/기록 공개 위험. 보안 이력 전수 검사 미완, 고객 자료·토큰 커밋 금지. assistant가 공개 설정/Production·비용·다른 상품 원장을 변경한 것은 아님.
- 중앙 기존 CITEVAULT 행에 과거 선실패/378PASS가 있어도 **본 문서와 제품 HEAD의 최신 398PASS 증거가 우선**한다. 다른 모든 제품 수치·마커·판매 등록완료 이력 불변.
