# Kmong product HEAD drift audit — 2026-11-14 12:56 KST

**Source of truth:** `hibi89/hackathon-command-center-2026@kmong-productization/data/kmong_hub_auto_observations.json`, Git blob SHA `17a7d39920e6a44dc6d7c5c59caa8209e28c1e95`.

**Inspection:** 2026-11-14 12:54–12:56 KST. 29/29 individual read-only GitHub branch HEAD lookups succeeded, compared with `products[].head_sha` from the hub's auto-observation JSON. Evidence is a point-in-time comparison only; concurrent product updates may immediately make this report stale.

| Finding | Count |
|---|---:|
| Product references independently checked | 29 |
| Current Git HEAD identical to hub observation | **25** |
| Product HEAD newer/different than the hub observation | **4** |
| Lookup errors or nonexistent branches | **0** |

## Four changed product refs (not proof of failed synchronization)

| Product | ID | Branch | Snapshot SHA | Independently observed live HEAD |
|---|---|---|---|---|
| DATA2WEB | ACTIVE-05 | `hibi89/data2web_studio@feature/final-blueprint-p85-evidence-20261113` | `a3975984dcb7dc1c797e17f1a6de58532f723768` | `69a535eb4da2366f623d1d5e4de7fab1acb785f9` |
| DBVORA | ACTIVE-11 | `hibi89/DBVORA@feature/p0-db-map` | `c9823a3d48c4c8507c8c4c61ca3328d92674b3d4` | `4731046b4a16df50f4241d4ce9d925874ee25640` |
| Astra PDF | ACTIVE-13 | `hibi89/astra_pdf_redesigner@feature/astra-p71-pdf-source-parity-20261112` | `ed363a4f8aa0294114a1ff0ef99c3daff2f846eb` | `2c01f15b244d8159cf5ab119d19b82aae7cb2269` |
| FFAX | CANDIDATE-03 | `hibi89/frontend-foundry-ax@feature/ffax-workbench-p85-20261112` | `d47b70eab287a972772ed7e807f94586a3eae9d7` | `26dadf77c40e0a20c1bced469f8386f19d068876` |

**The other 25 HEAD comparisons matched:** ACTIVE-01, 02, 03, 04, 06, 07, 08, 09, 10, 12, 14, 15, 16, 17; CANDIDATE-01, 02, 04, 05, 06, 07, 08, 09, 10, 11, 12.

## Operational implications and next steps

- The observation snapshot is **not current for four actively changing products** at the time of inspection; an old automated readiness score cannot be represented as a newly certified functional completion percentage. Official score authority remains unchanged: DATA2WEB's historical approved 72/100 only, the other 28 products `UNASSESSED`. Readiness scores are not the final blueprint completion rate, nor product sale clearance.
- Latest proven full collector RUN: [GitHub Actions #43551965261](https://github.com/hibi89/hackathon-command-center-2026/actions/runs/43551965261), 35 repos/80 refs/29 products, `UPDATED`, zero blocking fingerprints. This audit occurred **after** that run and therefore does not imply its historical result was wrong.
- An hourly `23 * * * *` schedule is configured in central `main@f4d8cbe42a4e3dd6db62ba6792c61a1414e0bbc9` and still present in main `80172145`; as of 12:56 KST on 2026-11-14 there were **zero observed `event=schedule` runs**. First post-change schedule slot is 13:23 KST (subject to GitHub delay/drop and existing `KMONG_SYNC_ENABLED`/API quota guard). Do not label the schedule broken before that slot.
- After a natural dispatch or scheduled RUN, compare new `kmong-productization` snapshot to all 29 live HEADs again and distinguish `UPDATED`, `NO_CHANGE`, `DEFERRED / NOT_SYNCED`, `SKIPPED`, and source-side concurrent drift.
- Do not overwrite the generated observation JSON from this audit, raise official percentages, alter source branches, trigger unnecessary paid builds, or claim production 100% from stale metadata.

## Reproducibility

1. Read blob SHA of `kmong-productization/data/kmong_hub_auto_observations.json`.
2. For each of its `products[0..28]`, fetch the exact GitHub `repos/{repository}/branches/{tracked_branch}` resource read-only; compare `commit.sha` with `head_sha`.
3. Use a fresh source snapshot after the next full GitHub Actions RUN and repeat; preserve the old snapshot Git blob and this audit as the point-in-time trail.

**As-of / scope:** 2026-11-14 12:54–12:56 KST. GitHub API connector evidence. 29 successful branch HEAD lookups. No Production POST, no Vercel deployment, no change to original data or rights/policy.
