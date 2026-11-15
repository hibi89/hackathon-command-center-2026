#!/usr/bin/env python3
"""Offline guard: incubating WebOps ideas cannot silently become sellable SKUs.

This complements the existing permanent 29-source/19-service listing gate.
No network, repository mutation, registration, or completion-rate calculation.
"""
import json
from pathlib import Path
import sys
from validate import CATALOG, IntegrityError, require

ROOT = Path(__file__).resolve().parents[2]
INTAKE = ROOT / "data/kmong_webops_product_intake_20261115.json"
INTAKE_PATH = "data/kmong_webops_product_intake_20261115.json"
DECISION = "KMONG-TREND-3IN1-20261115"
EXTENSION_IDS = {"KMONG-SVC-07", "KMONG-SVC-14"}
CANDIDATE = "KMONG-CAND-UPTIME-01"


def validate_webops(catalog, intake):
    """Verify reference integrity and sale hold, without changing source data."""
    require(isinstance(catalog, dict) and isinstance(intake, dict),
            "catalog and incubation registry must be JSON objects")
    services = catalog.get("ranked_services")
    require(isinstance(services, list) and len(services) == 19,
            "original 19 service slots must remain")
    ids = [item.get("service_id") for item in services if isinstance(item, dict)]
    require(ids == [f"KMONG-SVC-{n:02d}" for n in range(1, 20)],
            "original service IDs/order must be preserved")
    require(type(catalog.get("source_product_count")) is int and
            catalog["source_product_count"] == 29,
            "original 29 source inventory must remain")
    require(type(catalog.get("recommended_listing_count")) is int and
            catalog["recommended_listing_count"] == 19,
            "original 19-listing count must remain")
    # The existing 19 BASE listings may be legitimately published later.
    # Their registration history is validated by validate.py; this gate only
    # forbids promoting the independent UPTIME OPS incubation record.

    ref = catalog.get("trending_product_intake_20261115")
    require(isinstance(ref, dict) and
            ref.get("decision_id") == DECISION and
            ref.get("record_type") == "PENDING_PRODUCT_BUILD_ONLY" and
            ref.get("intake_registry") == INTAKE_PATH and
            ref.get("new_candidate_id") == CANDIDATE and
            ref.get("candidate_status") == "NOT_BUILT_NOT_REGISTERED_RELEASE_HOLD" and
            ref.get("commercial_ready") is False and
            ref.get("publish_authorized") is False and
            ref.get("official_product_completion_changed") is False,
            "catalog intake reference is missing or prematurely released")

    require(intake.get("schema_version") == 1 and
            intake.get("decision_id") == DECISION and
            intake.get("record_type") == "INCUBATION_ONLY_NOT_REGISTERED" and
            intake.get("canonical_source_catalog") ==
            "data/kmong_service_catalog_20261113.json" and
            type(intake.get("canonical_existing_service_count")) is int and
            intake["canonical_existing_service_count"] == 19 and
            type(intake.get("canonical_existing_source_count")) is int and
            intake["canonical_existing_source_count"] == 29,
            "incubation registry changed its approved source/catalog contract")

    extensions = intake.get("extensions")
    require(isinstance(extensions, list) and len(extensions) == 2,
            "exactly two existing-service extensions expected")
    ext_ids = [row.get("service_id") for row in extensions if isinstance(row, dict)]
    require(len(ext_ids) == 2 and set(ext_ids) == EXTENSION_IDS and
            len(set(ext_ids)) == 2 and all(sid in ids for sid in ext_ids),
            "extension missing, duplicated or assigned to an unknown SKU")
    for row in extensions:
        require(row.get("decision") == "FOLD_AS_UNVERIFIED_EXTENSION" and
                row.get("listing_status") == "미등록" and
                row.get("commercial_ready") is False,
                "unverified extension must not be sold as approved")

    candidates = intake.get("new_candidates")
    require(isinstance(candidates, list) and len(candidates) == 1 and
            isinstance(candidates[0], dict),
            "exactly one new development candidate expected")
    candidate = candidates[0]
    require(candidate.get("candidate_id") == CANDIDATE and
            candidate["candidate_id"] not in ids and
            candidate.get("product_name") == "UPTIME OPS" and
            candidate.get("decision") == "NEW_CANDIDATE_NOT_EXISTING_SERVICE" and
            candidate.get("development_status") == "NOT_BUILT" and
            candidate.get("listing_status") == "미등록" and
            candidate.get("kmong_listing_url") is None and
            candidate.get("published_at_kst") is None and
            candidate.get("listing_history") == [] and
            candidate.get("commercial_ready") is False and
            candidate.get("release_hold") is True,
            "UPTIME OPS candidate has an unapproved launch or identity change")

    bundle = intake.get("bundle")
    require(isinstance(bundle, dict) and
            bundle.get("name") == "WebOps QA 360" and
            bundle.get("status") == "DRAFT_ONLY_NOT_NEW_SKU" and
            isinstance(bundle.get("components"), list) and
            len(bundle["components"]) == 3 and
            set(bundle["components"]) == EXTENSION_IDS | {CANDIDATE} and
            bundle.get("not_for_sale_until_all_components_ready") is True,
            "WebOps bundle must remain an unsellable combination, not a fourth SKU")
    require(intake.get("third_party_license_text_verified_in_this_run") is False and
            intake.get("third_party_code_copied") is False and
            intake.get("source_repo_mutations") is False and
            type(intake.get("kmong_registered_count_change")) is int and
            intake["kmong_registered_count_change"] == 0 and
            intake.get("verified_sale_approval") is False,
            "unverified external rights or launch claims must not be promoted")
    return {"extensions": len(extensions), "candidates": len(candidates),
            "existing_listings": len(services), "published_from_intake": 0}


def main():
    try:
        catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
        intake = json.loads(INTAKE.read_text(encoding="utf-8"))
        summary = validate_webops(catalog, intake)
    except (IntegrityError, OSError, TypeError, ValueError, KeyError) as exc:
        print("KMONG_WEBOPS_INTAKE: FAIL:", exc, file=sys.stderr)
        return 1
    print("KMONG_WEBOPS_INTAKE: PASS "
          f"listings={summary['existing_listings']} "
          f"extensions={summary['extensions']} "
          f"candidates={summary['candidates']} "
          "registered_change=0 sale_approval=false release_hold=true")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
