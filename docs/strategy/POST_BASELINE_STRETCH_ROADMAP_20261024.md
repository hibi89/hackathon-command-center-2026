# 해커톤 3개 조기완료 후 추가개발 전략 — 총괄 참조용 (2026-10-24)

> **보존 목적:** KIC·PayPal·UGREEN의 기존 예정 작업을 일찍 마쳤을 때 무엇을 보강할지, 다음 총괄 채팅이나 감사에서 즉시 재사용하기 위한 의사결정 원본.
>
> **상태:** **조건부 전략 초안 / 사용자에게 설명 및 기록 요청받음 / 실제 개발 착수 지시 아님.** 이 파일이 생겼다는 이유만으로 세 대회 담당자의 현재 P0 업무·제출 마감·작업 원장을 수정하지 않는다. 신규 기능 착수 여부는 당시 최신 HEAD, 진도, 차단요인, 남은 일정과 사용자 승인 범위를 재검토해 결정한다.

## 0. 30초 총괄 요약

| 프로젝트 | 조기완료 시 가장 먼저 강화할 한 가지 | 강력한 심사 시연 장면 | 뒤로 미룰 것 | 실사용 상품화 방향 |
|---|---|---|---|---|
| **KIC** | **근거 추적형 투자 리서치 Agent** | 위험 수치 클릭 → DART 원문·계산·분모 확인 → 근거 부족하면 계산 보류 | 금융 지표 수 늘리기, 동결 PDF 디자인 반복 | 출처 검증 가능 기업 리서치·보고서 솔루션 |
| **PayPal** | **AI 견적 → 인간 최종승인 → Sandbox 결제 → 영수증** | 견적 변경 발견 시 결제 중지·금액 재승인, 중복 결제 차단 | 모의 D1·추가 구독 및 무리한 클라우드 확장 | 프리랜서 견적·청구·결제 SaaS |
| **UGREEN** | **NAS 프로젝트 인수인계 변경 감지** | 전회 대비 파일 누락·변경·최종본 후보 충돌을 증거로 비교하고 담당자 행동 제시 | 공식 SDK 정적 검색 반복, 합성 테스트 개수만 증가 | 납품 폴더·버전·누락 자동 검수 도구 |

**공통 원칙:** 세 프로젝트 모두 기능 3~5개를 늘리기보다 **심사위원이 체감하는 차별화 기능 1개**를 선택한다. 기능 완료에는 실제 경로의 시연·재현성·실패 대응 증거가 필요하다. 오프라인/합성 성공을 실제 외부 시스템 인증으로 바꾸어 쓰지 않는다.

## 1. 착수 게이트와 단계

1. **P0 제출 적격성 최우선.** KIC의 실제 DAKER 제출권한, PayPal의 실 PayPal Sandbox + 실 AI 호출, UGREEN의 공식 UGOS Skill Creation Tool 실제 생성 증거·사용자 저작권/제출 승인 해결. P0 작업은 차단된 채 새 기능 확장만 반복하지 않는다.
2. **P1 추가 차별화는 '조기 완료 + 마감 보호'일 때만.** 공식 제출 준비, 참가자 승인, 남은 필수 일정과 충돌하지 않고 독립 수행 가능한 경우 1개만 개발한다. UGREEN은 예선용 네 개 Markdown ZIP 제한을 깨는 소스/바이너리를 제출 패키지에 추가하지 않는다.
3. **P2 데모·심사 품질.** 실제 화면·로그·위험 경계가 보이는 60~150초 시연, 짧은 영문 소개, 아키텍처 1장, 실행 README, 실제 CI/외부 호출 증거, 알려진 한계와 사용권 문서. PayPal은 공식 영상 규정 별도로 준수한다.
4. **본선 대비 전환.** KIC는 진출 시 실제 동작 Agent+출처 재현, UGREEN은 제한된 공식 NAS 접근 시간을 위해 오류 복구·검증 순서 미리 준비, PayPal은 심사위원 재현성을 중점 점검한다.
5. **과잉 개발 종료 기준.** 신규 기능이 P0 실증/접수 확률을 떨어뜨리거나 현재 대표 시연을 더 명확히 만들지 못하면 보류. 반복 정적 조사·임의 유료 서비스·무단 배포·무단 제출 금지.

## 2. 총괄이 나중에 재개할 때 체크할 것

- 실제 GitHub **최신 원격 HEAD와 정본 진행표**를 먼저 읽고 이 문서의 2026-10-24 수치를 당일 수치로 재사용하지 말 것.
- **KIC:** 실제 원문 출처 1건 이상 인증됐는가? DAKER 제출권한 확인/예선 PDF 동결이 지켜지는가? 클릭해서 근거를 좇는 사용자 시나리오가 구현 가능한가?
- **PayPal:** 판매자·구매자 별도 Sandbox와 무료 AI 모델의 실 호출 증거가 존재하는가? AI가 승인된 금액을 변경시키지 않는가? 결제 불확실·중복 호출 시 안전한가?
- **UGREEN:** 공식 Creator가 실제 Skill을 생성했는가? 사용자 승인/저작권/AI 고지가 확보됐는가? 전회 비교를 지원하는 정식 NAS Agent/권한 근거가 있는가? 근거 없으면 기존 오프라인 비교 데모만 유지할 것.
- **기록 형식:** 선택한 P1 1건에만 목표·대체안·제출 리스크·예상 작업범위·합격기준·실측 테스트·승인 필요사항을 남긴다. 정식 시정 지시는 각 대회 `docs/FROM_HACKATHON_COMMAND.md`의 별도 ACTIVE 지시로 내릴 때만 효력이 있다.

---

## 상세 근거 및 구현 수용 기준 (영문 기록)

# Three-hackathon stretch roadmap — after eligibility and stable base (2026-10-24 KST)

**Decision type:** conditional engineering strategy drafted by integrated chief in response to user asking what to build if the three projects finish ahead of schedule. **This document is NOT a new ACTIVE order to leads, not permission to bypass existing P0 owner-account gates, not authorization for paid services, official submission, or confidential data publication.** Lead `docs/FROM_HACKATHON_COMMAND.md` ACTIVE/P0 always outranks stretch goals.

**Primary outcomes:** (1) eligibility and actual submission proof, (2) scoring-relevant standout moment, (3) reproducible public portfolio demonstrator. Plan dates are KST; calendar progress % is NOT software maturity.

## Keep the gates first
- **KIC**: authenticated DAKER individual/team-leader/submit-button authority; exact entrant-approved <=10-page official-template PDF. Current day ledger **28 DONE/3 BLOCKED/29 NOT_STARTED** on `lead/kic@6e0a896b19154b41a1197b7420f2cb43e7d53a70`. Official Round 1 is **proposal PDF**, not mandatory production deploy. Round 1 deadline **2026-11-12 10:00 KST**; finals only if selected (Dec 3 results; Dec 22 prototype/demo/README/PDF).
- **PayPal**: authorized genuinely working PayPal Sandbox OAuth/Orders+buyer/capture evidence and actual AI response; user-safe judge reproduction + publicly visible <3-minute video + public OSS LICENSE. Current **12 DONE/2 PARTIAL/1 BLOCKED/3 NOT_STARTED** on `lead/paypal@ae90cabddbab8444ef0a49fa8538b651108d2960`. Deadlines **2026-11-13 05:00 KST**; public hosted URL optional only if judge can actually run build following README; synthetic demos alone ineligible.
- **UGREEN**: evidence that participant actually used the *official UGOS Skill Creation Tool* to CREATE the initial Skill in supported assistant, compare actual generated Markdown, review rights/dataflow/AI disclosures and submit exact PDF+ZIP with receipt. Current **2 DONE/12 PARTIAL/3 BLOCKED/7 NOT_STARTED** on `lead/ugreen@cb29c2f4197ff9edd2f89c96d6da2d8c44384845`. Round 1 deadline **2026-11-16 16:45 KST**; no live NAS/video required in Round1. Finalists have separate assigned single-day NAS remote access Nov 22–28 PT and Round2 deadline Nov 30 23:45 PT (Dec 1 16:45 KST).

## Rank-one conditional stretch per contest

### KIC — evidence-traceable investment research Agent
**Why:** round-one PDF evaluates problem, business usefulness, agent design, sources and MVP feasibility. Real usefulness, source truth, and explainability differentiate from a generic RAG chatbot. Build as a finalist preparation / demonstration branch, keeping submitted frozen preliminary PDF intact.

- **Core showcase:** one realistic public permitted company-and-period question, Research → primary-source Verification → Risk verdict (or UNKNOWN) → 1-page cited report. Every figure and claim is linked to original issuer/source date/report code, unit, calculation, timestamp and verification status. An unavailable source must remain `NOT_VERIFIED`; never upgrade synthetic fixtures into real source evidence.
- **Differentiating moment:** click one red-flag metric → inspect source and denominator; discover missing/mismatched filing → system *withholds* ratio and explains why, instead of hallucinating a risk rating. Compare at most 2–3 truly verified peers and one historical period if original permissible facts are available.
- **Acceptance:** reproducible recorded 3-case demo: valid matched facts, mismatched sources, denominator invalid; at least one authorized real DART filing trace confirmed before labeling anything LIVE. Offline synthetic acceptable as openly labeled fallback, not official verified evidence.
- **Avoid:** more investment-factor counts, PDF cosmetic loops or LLM orchestration complexity ahead of actual DAKER submission permission.

### PayPal — single compelling AI-to-payment transaction with human safeguards
**Why:** judging equally weighs PayPal+AI depth, end-user design, impact, novelty and presentation. Stage-one minimum is a genuinely functional AI+PayPal integration.

- **Core showcase:** client brief → actual AI drafts bounded scope/milestone quote → seller reviews/edits & explicitly approves exact price/currency → real PayPal Sandbox buyer approval → server-side retrieval/capture confirmation → receipt/milestone state visible. Keep event chain reproducible with two safe sandbox roles.
- **Differentiating moment:** AI warns about a changed scope/invoice or incorrect amount before any payment. The operator sees exact approved amount and a "request approval again" path; payment is held rather than guessed. No autonomous real-money payment/escrow/regulated custody claim.
- **Acceptance:** one allowed real Sandbox transaction and one genuine AI-generation receipt (secret-redacted), end-to-end demo with wrong-merchant, mismatched-amount, duplicate webhook, interrupted request tests; use verified idempotency for uncertain outcomes. A <3-minute YouTube video shows actual on-device operation; README allows judge to execute or interact. Availability of reviewer sandbox account must be handled by the entrant under provider rules without public credential leakage.
- **Avoid:** more fake D1, subscription, production hosting and peripheral integrations before real Provider gate. Optional stretch *after* base: tiny conversion dashboard or frictionless buyer-view only if demo remains coherent.

### UGREEN — NAS-local ProjectReady delta and provenance review
**Why:** Round1 scored equally on user value, differentiation, technical quality and **NAS-specific fit**. "List missing files" alone is easily compared to a generic AI folder tool; repeat-run evidence with safe version/permission decisions makes it distinctive.

- **Core showcase:** owner-authorized NAS folder and explicit checklist → source-backed PRESENT / MISSING (only complete scans) / NOT_CHECKED / VERSION_REVIEW report → compare a second run with prior authorized snapshot → "newly missing / changed / ambiguous versions / unchanged" digest and precise owner next steps. No file reads outside scope, and no secret path echo.
- **Differentiating moment:** a supposed final file disappears or there are two possible final versions; instead of quietly selecting the newest or declaring READY, agent flags the change and asks human to choose. Unavailable Agent permissions remain NOT_CHECKED, never fake a verified absence.
- **Acceptance:** official UGOS Creator output and later (if finalist) actual registered NAS agent path/complete-listing evidence; 5 reproducible synthetic scenarios for Round1 explanation (already exist, reuse), explicit safe I/O, handling a missing permission and truncated listing. Stronger NAS Fit: cite actual approved NAS file/knowledge capabilities, show local persisted historical evidence only if supported by real permissions/SDK. Round1 submission ZIP remains Markdown-only as per rules; don't insert scripts/JSON/bin.
- **Avoid:** repeated static SDK spelunking, unapproved live NAS scan, cloud data exfiltration, adding executable to 4-file entry, claiming simulated 211 passes prove official NAS compatibility.

## Shared portfolio release layer — after contest-specific submission gates
One short English product summary, a 60–150-second labeled honest walkthrough for each, one architecture/decision diagram, reproduction README, CI evidence, threat/limitations section, synthetic-data fallback clearly differentiated from real provider validation, and links to contest receipts or state NOT_SUBMITTED. Release only assets with validated rights. Keep contest originality and third-party license disclosures separate. No extra premium integrations solely for sponsor-prize eligibility unless user opts in.

## Priority/stop decision rule
1. **P0 external proof before expansion**: if access blocked, prepare only one concise owner action checklist and deterministic safe test harness. Do not spend successive work units on mock replacements.
2. **P1 one scoring-relevant differentiator per contest** only when initial product and exact release path are verified or a genuinely independent task cannot endanger deadline.
3. **P2 polish** user journey/video/reproducible docs; keep max scope bounded.
4. No feature counts or elapsed-hour percentages manufactured from dates. Any additional release or account/paid/third-party action requires entrant permission and a fresh compliance check.
5. Supervisor may suggest/stretch backlog in command center; child lead starts work only after current active priorities and user approval conditions, preserving latest lead schedules. Avoid altering original 60/18/24 day DONE statuses based solely on plan.

## Official evaluation sources
- KIC [official DAKER call](https://daker.ai/public/hackathons/kic-ai-agent-competition): preliminary PDF, 10-page limit, later finals with executable demo and agent.
- PayPal [Devpost Rules](https://paypalaihackathon.devpost.com/rules): stage 1 viability + genuine PayPal Developer Platform and AI, 5 equally weighted criteria, functional repo/test build and public YouTube under 3 minutes.
- UGREEN [Devpost Rules](https://ugreenhackathon.devpost.com/rules): official Creator requirement, Round1 PDF/ZIP and no NAS runtime, four equally weighted criteria; finalist-only NAS remote test and Round2 submission.
