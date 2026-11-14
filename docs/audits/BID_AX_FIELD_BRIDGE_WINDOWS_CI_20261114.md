# BID AX 온비드 첫 10개 필드 진단·Windows CI 4/4 성공

**2026-11-14 KST, 등록되지 않은 후보 KMONG-SVC-18 / CANDIDATE-10.**

- 제품 `hibi89/Freelancer@product/bid-ax-public-procurement`; 기능 `f662ecf23f9dc51bc6aad15cb64a28491950a899`, 문서 `8203cce5a478903a3133dcb8732c482e193cdfaa`.
- 고객 본인 PC 실 공식 온비드 결과목록 15157252 첫 페이지 **10/10**, 총 보고 **186건**, 저장 SHA 일치. 186 전수 수집과 실 항목ID 유효성/나머지18페이지는 미검증. 원문/키/개별 고객 데이터 미전달.
- `bidax/onbid_official_bridge.py`: 고객 로컬 격리패킷의 검증 후 공개 필드 이름별 **존재 건수만** 출력. `onbid-detail-queue --consent`는 유효 물건ID가 모두 존재할 때 15157254 **실행하지 않은** 상세조회 후보만 고객 PC 새 파일에 기록. 키비저장, 자동 API/판정/중복/덮어쓰기 차단.
- **[Actions 43533369896](https://github.com/hibi89/Freelancer/actions/runs/43533369896) completed success 4/4**: Ubuntu3.11 237 PASS, Ubuntu3.13 237 PASS, Windows3.11 237 tests OK skipped=1 (POSIX mode check not applicable to NTFS). Windows PyInstaller onedir **CLI EXE** `--help` 및 Onbid 무네트워크 plan PASS. 소스 기능 HEAD와 CI HEAD 일치.
- 이전 Windows 실패 원인: 코드 페이지 인코딩, ZIP Windows 구분자, POSIX 전용 권한 검사; 별도의 EXE 실행 대기는 Tk GUI 엔트리포인트를 CLI --help로 실행한 잘못된 테스트. CLI 독립 엔트리포인트로 변경하고 성공. 기존 GUI는 보존, Win GUI EXE·고객 설치·SmartScreen/ACL 미확인.
- 여전히 G2B+Onbid 다른3서비스 실계약, 100실공고·인간10검토, 법률/상용권·고객 파일럿/실 설치 미검증. 고정 최종설계 R01–R29의 **공식률 UNASSESSED/85% 미입증**. 상태 `[작업중]`, RELEASE HOLD, 미등록. 사용자 가중치 추가승인 요구 없음.
- 다른 SKU/등록완료 이력, 기존 원천29/판매19와 BID OWL 및 고객 원본 불변.

제품 근거: https://github.com/hibi89/Freelancer/blob/product/bid-ax-public-procurement/docs/ONBID_OFFICIAL_FIELD_BRIDGE_20261114.md
