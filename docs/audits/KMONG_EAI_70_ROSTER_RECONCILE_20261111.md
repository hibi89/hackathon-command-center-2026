# 크몽 16종 최신화 — EAI 70%와 ASTRA 70% 동시 반영 (2026-11-11 KST)

## 변경 근거
- EAI: `hibi89/EAI@feature/local-first-mvp` 실제 기능+테스트 SHA `8cdad74a256d3e132870dfd28a875dd4425ffa77`; [GitHub Actions #42960081154](https://github.com/hibi89/EAI/actions/runs/42960081154) **582/582 PASS, 0 FAIL/0 SKIP**, Python3.11 Ubuntu, compileall CLI smoke. 문서 SHA `379d0c7a77e9a422e7c7cc1c3e11d8318510dda9`; [P23–P30 상세 및 영역별 50+20 가중치](https://github.com/hibi89/EAI/blob/feature/local-first-mvp/docs/P23_P30_MILESTONE_70_20261111.md). **최종설계 대비 70% 잠정**이고 실 Windows/Qwen/고객/상용 출시 미검증.
- ASTRA: `hibi89/astra_pdf_redesigner@feature/astra-p52-to-p70-20261111`, 실제 기능 SHA `dab6e365f5c9d57e285eaf71cb840ecc41513c6e`; [Chrome/Edge CI #42957762014](https://github.com/hibi89/astra_pdf_redesigner/actions/runs/42957762014), [Windows NSIS CI #42957762000](https://github.com/hibi89/astra_pdf_redesigner/actions/runs/42957762000), 검증 결과 상세는 기존 크몽 문서 하단 ASTRA 70% 추록 참고. 이 18pp는 별도 채팅에서 달성했으나 기존 요약 표의 52%가 역사적으로 남아 있어 이번에 정합화. 실제 구매자 출고·STEP6·PRO/BUSINESS는 HOLD.

## 활설 상품 16종 현재 추정

| 대상 | 동기화 전 기준 | 동기화 후 | 변화 |
|---|---:|---:|---:|
| EAI | 50% | **70% 잠정** | +20pp |
| ASTRA PDF Redesigner | 52% | **70% 잠정** | +18pp |
| 그 외 14종 | 변동 없음 | 변동 없음 | 0pp |
| **16종 합계** | **1085pp** | **1123pp** | **+38pp** |
| **16종 산술평균** | **67.8125%** | **70.1875%** | **+2.375pp** |
| **70% 미만** | 4종 | **2종** | PC CARE 50, AXMART³ CUBE 50 |

EAI 개발 완성률은 가중 범위 기반 기술총괄 **잠정 추정**이지 제품 실사용·판매 가능 상태에 대한 검증값이 아니다. 실제 로컬 Qwen 접속을 하지 않았고 fake localhost만 사용. 무단 업로드·권한/비용·배포·고객 원본 변경 없음. 다른 14종의 수치는 최신 표 기준 그대로 보존, 과거 추록을 소급 수정하지 않는다. 테스트 없는 상향 금지.

## 이어가기
- `HANDOFF.md` → `STATUS.md` → `AGENTS.md` → `REQUIREMENTS.md`(있을 때) → `KMONG_PRODUCTIZATION.md` → 각 제품 브랜치 검증
- 70% 미만: AXMART PC CARE, AXMART³ CUBE 각 50%. 다른 채팅과의 브랜치 충돌 여부 확인 후 담당 제품에서 개발.
- EAI 70→100 경로: 실제 Windows + real local Ollama/Qwen, 라이선스, UI/납품, customer-like workload/보안 성능 검증 이후에만 추가 가산.
