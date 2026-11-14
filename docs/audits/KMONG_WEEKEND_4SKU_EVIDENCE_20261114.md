# 2026-11-14 주말 4개 크몽 SKU — 정확 SHA / 기능 CI / 출시 보류 증거

**점검 시점:** 2026-11-14 13:30 KST (조회 중 원천 브랜치가 추가 갱신될 수 있음)

**검증 방법:** 중앙 [19서비스 카탈로그](../../data/kmong_service_catalog_20261113.json), [29원천 공식 인덱스](../../data/final_blueprint_product_index_current.json), 4개 GitHub product tracked HEAD, 해당 브랜치의 GitHub Actions `head_sha`/run status와 각 제품 `HANDOFF.md` 최상단 교차 확인. 이 자료는 운영 참고용 독립 감사이며 원천 제품 코드를 변경하지 않는다.

## 요약

| 서비스 / 사용자 고객 문제 | 제품 인덱스 기록 | 2026-11-14 관찰 source HEAD | 기능 검증 근거 | 출시 상태 |
|---|---|---|---|---|
| `KMONG-SVC-01` 데이터 웹보고서 | `ACTIVE-05` DATA2WEB, **공식 72/100** | `hibi89/data2web_studio@feature/final-blueprint-p85-evidence-20261113` `d5c09f07d6e0d7173c6e9babb8bb0765a019ab85` | [Windows/Linux/Browser CI #43556540886](https://github.com/hibi89/data2web_studio/actions/runs/43556540886) **4/4 jobs SUCCESS, run source SHA=d5c09f07**; [CodeQL #43556540904](https://github.com/hibi89/data2web_studio/actions/runs/43556540904) SUCCESS. 프로그램 테스트는 합성·공개 runner이며 구매자 실기기 증거 아님 | 미등록 / RELEASE HOLD |
| `KMONG-SVC-08` DB 구조 진단 | `ACTIVE-11` DBVORA, **공식 UNASSESSED** | `hibi89/DBVORA@feature/p0-db-map` `13773f2086edb89f78bd247ac7b228cb045b78bb` (문서-only HEAD) | [source `fdbf9ed34b932d220220fd1b13abb616389a37ea` CI #43555133875](https://github.com/hibi89/DBVORA/actions/runs/43555133875) **Windows/Linux 2/2 SUCCESS**, source `HANDOFF.md` 보고 Ubuntu688 PASS, Windows687 PASS/1 POSIX-only SKIP. `13773f20` 최종설계 게이트 [#43555506564](https://github.com/hibi89/DBVORA/actions/runs/43555506564) SUCCESS | 미등록 / RELEASE HOLD |
| `KMONG-SVC-09` PDF 재디자인 | `ACTIVE-13` Astra PDF, **공식 UNASSESSED** | `hibi89/astra_pdf_redesigner@feature/astra-p71-pdf-source-parity-20261112` `2c01f15b244d8159cf5ab119d19b82aae7cb2269` (문서-only HEAD) | [source `2213e8e50759836b8c24bfbe7b037536a8fd995a` Linux #43553461990](https://github.com/hibi89/astra_pdf_redesigner/actions/runs/43553461990) **2/2 SUCCESS**, [Windows #43553462026](https://github.com/hibi89/astra_pdf_redesigner/actions/runs/43553462026) **SUCCESS**, final blueprint gate [#43553462320](https://github.com/hibi89/astra_pdf_redesigner/actions/runs/43553462320) SUCCESS | 미등록 / RELEASE HOLD |
| `KMONG-SVC-10` React UI 제작 | `CANDIDATE-03` FFAX, **공식 UNASSESSED** | `hibi89/frontend-foundry-ax@feature/ffax-workbench-p85-20261112` `bdbbf0bbd2d8dcf1f53ac513e44522a47214a342` | 과거 [source `abe82e806f30c7949684cc1f03ea0d497cd25561` #43553254119](https://github.com/hibi89/frontend-foundry-ax/actions/runs/43553254119) **4/4 SUCCESS**, 128/128 PASS/OS. **현재 코드 `bdbbf0bb` run [#43556707423](https://github.com/hibi89/frontend-foundry-ax/actions/runs/43556707423)는 점검 시 2 jobs SUCCESS + 1 in progress, 총괄 SUCCESS 미확인**. 직전 `5eb8dbdf` [#43556549527](https://github.com/hibi89/frontend-foundry-ax/actions/runs/43556549527) FAILURE 후 수정됨. 실패한 버전은 출시 근거로 사용 금지 | 미등록 / RELEASE HOLD |

## 독립 상용 출시 / BASE 준비 관문 — 기존 확정 제품 최종설계 점수와 다름

| SKU | 현재 기술 증거로 충족 가능한 부분 | 반드시 별도 확인해야 하는 남은 관문 | 사용자 개입 시점 |
|---|---|---|---|
| `01` | 오프라인 HTML/ZIP/수령 확인 및 GUI/브라우저 합성 Windows·Linux 검증, 판매 설명 KIT 준비 이력 | **R23/R30** 독립 외부 구매자 실 OS/브라우저 7항, **R29** 독립 보안감사, **R21/R33** 저작권·고객 입력/결과물 권리, 실제 크몽 게시 사용자 수용 | 13:00 통합 사용자 요청 이력 재사용; 외출 중 새 PC 작업 요청 금지 |
| `08` | SQLite/선택형 로컬 PG 읽기전용·CAS zlib·synthetic backup/restore, cross-OS CI | 실 Windows10/11 사용자 테스트, 물리전원차단/복원·실 고객 DB 별도 승인, NOTICE/오픈소스권리/가격·지원/환불/상용 심사 | 동일 통합 요청 재사용, 비밀/고객DB 전송 금지 |
| `09` | PDF 원본 보존 경계·편집/검수·Electron Windows 설치/NSIS CI·오프라인 이력 | 승인된 원본 PDF **5–10개** 전후 품질/글꼴 확인, STEP6 실제 권리 검증/검색 결과, STEP7 OCR/한국어 로컬 모델 실동작·사용권, SKU 라이선스 발급·실 Windows 인수 | 동일 통합 요청 재사용; 모델·개인키/폰트 유료/무단 다운로드 금지 |
| `10` | 13종 React19 TSX, 컴파일/서버렌더, Chromium3/axe 합성 QA, 최신 재수정 후 CI 확인 대기 | 실제 허가 로컬 Qwen 12프롬프트 중 **≥10 독립 타입검사+SSR 성공**, 사용자 Windows GUI/키보드 7항, 고객 GitHub/라이선스·판매 GO | 동일 통합 요청 재사용; 합성12/12를 실 Qwen 12/12로 표현 금지 |

**설계 선택:** (A) 네 제품의 잠정 80~95% 등 숫자를 복제해 SKU 준비율로 환산하는 방법은 빠르지만 오인·중복·무허가 출시 위험으로 **미채택**. (B) 정본 제품별 기능 CI의 정확 SHA와 *고객/권리/사용자 GO*를 구분하고 미검증을 남기는 **증거 중심 SKU별 HOLD 기록을 채택**. 추가 비용·외부 데이터 전송·권한 확대 0.

## 증거 제약·절차

- 29원천→19서비스 중 정확히 해당 4개 서비스의 연결은 [중앙 상품 무결성 CI #43556719142](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43556719142) **20/20 PASS**. GitHub 데이터와 출력 레코드가 일치하는 메타데이터 시험일 뿐 서비스 완성도 증명은 아님.
- 중앙 수집은 [실전 GitHub App bot RUN #43554677541](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43554677541) 35repo/80refs/29상품 `UPDATED` PASS. 해당 원장은 수집 시점의 HEAD이고 원천 개발자들이 계속 커밋하므로 이후 diff는 단순 drift일 수 있다. **새로운 GitHub 작업 완료가 중앙 최종완성률에 자동 환산되지 않는다.**
- 19개 `listing_status=미등록`, `verified_registered_count=0`이며, 게시 URL/일자/이력 기록은 실제 크몽에서 확인된 뒤에만 변경. `BASE_COMMERCIAL_READY`/소유자 `GO` 네 건 모두 증거 없음. 이 표가 물리 테스트, 서명된 상용권리 또는 플랫폼 등록을 수행했다는 뜻은 아니다.
- 보류 항목 재질문 방지: **2026-11-14 13:00 KST 통합 소유자 요청**이 각 제품 기록에 이미 반영됐으며 중복 요구하지 않는다. 외출 후 PC 작업은 그 요청에서 처리한다.
- 최종 검증은 최신 `HANDOFF.md` → `STATUS.md` → 실제 source/CI → 정확 SHA → 임시 판매 KIT/실고객 인수의 순서로 반복하고, 실제 판매 GO 전 사용권/고객 정보/원본 보호 검증을 완료한다.

**기록 범위:** 공통 카탈로그·인덱스·product `HANDOFF.md` / GitHub branch HEAD / Actions jobs read-only 확인, 주문/결제/원본 변경 없음. 점검 시점 이후 새 커밋·CI 종료가 있을 수 있으므로 외부 게시 전에 다시 확인.

## FFAX_POST_RUN_43556707423 — 2026-11-14 13:31+ KST subsequent exact-source verification

FFAX source `bdbbf0bbd2d8dcf1f53ac513e44522a47214a342` [run #43556707423](https://github.com/hibi89/frontend-foundry-ax/actions/runs/43556707423) **completed SUCCESS**, four jobs `windows-native`, `offline-node`, `browser-qa`, `package-owner-review` **4/4 SUCCESS**. Windows-native **138/138 pass, 0 fail**, Linux offline-node **138/138 pass, 0 fail**. Served Chromium 375×768×1440px (3 viewports, no overflow, 13 nodes) PASS. Review ZIP artifact ID `14098043598`, Chromium evidence ZIP artifact ID `14098617661` (temporary GitHub artifacts, content bytes/hash not separately verified in this audit).

Logs disclose `actualProviderCalls: 0`; the synthetic fixture result `12 passed/0 failed` is **not a real local Qwen inference trial**. AC04 owner-installed local Qwen12 (≥10 genuine independently typechecked+SSR passes), AC09 physical UI7, commercial owner GO still pending. The earlier top-row `in_progress` was accurate **at the 13:30 snapshot**, then resolved SUCCESS at 04:30:44Z. No source code or official completion/SALE HOLD state changed by this supplemental audit.

With this update, all four weekend SKU projects have grounded functional CI **SUCCESS** evidence for the named source commits; none has proven independent full-commercial-acceptance `BASE_COMMERCIAL_READY`.
