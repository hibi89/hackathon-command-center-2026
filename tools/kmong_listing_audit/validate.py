#!/usr/bin/env python3
"""Zero-network, read-only integrity gate for 29 source products and 19 Kmong listings.

Keep product repository branches and official completion separate from listing state.
The lone confirmed naming alias is intentional, not a fuzzy string match.
"""
from collections import Counter
from datetime import date
from pathlib import Path
import json
import re
import sys
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[2]
CATALOG = ROOT / "data/kmong_service_catalog_20261113.json"
INDEX = ROOT / "data/final_blueprint_product_index_current.json"
ALIASES = {"Factory AX 전체": "Factory AX"}
LISTING_STATES = {"미등록", "심사중", "등록완료", "판매중지", "비공개", "게시삭제"}


class IntegrityError(ValueError):
    pass


def require(ok, message):
    if not ok:
        raise IntegrityError(message)


def canonical_source(name):
    require(isinstance(name, str) and bool(name.strip()), "missing source product")
    return ALIASES.get(name, name)


def valid_kmong_url(value):
    """Accept explicit official Kmong HTTPS URLs, never external redirects/hosts."""
    if not isinstance(value, str) or value != value.strip():
        return False
    parts = urlsplit(value)
    return (parts.scheme == "https" and
            parts.netloc.lower() in {"kmong.com", "www.kmong.com"} and
            parts.path not in {"", "/"})


def valid_publication_date(value):
    """KST calendar date in a canonical YYYY-MM-DD representation."""
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return False
    try:
        return date.fromisoformat(value).isoformat() == value
    except ValueError:
        return False


def registration_events(history):
    """Validate history shape; proof fields are necessary, not independent authenticity."""
    events = []
    for event in history:
        require(isinstance(event, dict), "listing history must contain event objects")
        name = event.get("event", event.get("status"))
        if name != "등록완료":
            continue
        require(valid_kmong_url(event.get("kmong_listing_url")) and
                valid_publication_date(event.get("published_at_kst")) and
                isinstance(event.get("evidence"), str) and
                bool(event["evidence"].strip()),
                "registered history needs official URL, KST date and evidence reference")
        events.append(event)
    return events


def validate(catalog, index):
    """Return stable trace rows; never infer approval or mutate either input."""
    require(isinstance(catalog, dict) and isinstance(index, dict), "JSON objects required")
    services, records = catalog.get("ranked_services"), index.get("records")
    internal = catalog.get("internal_platforms")
    require(isinstance(services, list) and len(services) == 19, "expected 19 listings")
    require(isinstance(records, list) and len(records) == 29, "expected 29 source records")
    require(isinstance(internal, list) and len(internal) == 1, "expected 1 internal platform")

    counts = (catalog.get("source_product_count"),
              catalog.get("recommended_listing_count"),
              catalog.get("folded_feature_count"),
              catalog.get("internal_platform_count"))
    require(counts == (29, 19, 9, 1), "catalog counts drifted from owner-approved layout")
    require(catalog.get("operating_unit_key") == "service_id", "SKU identity is not service_id")

    ids = [s.get("service_id") for s in services if isinstance(s, dict)]
    ranks = [s.get("rank") for s in services if isinstance(s, dict)]
    require(len(ids) == 19 and ids == [f"KMONG-SVC-{i:02d}" for i in range(1, 20)],
            "service IDs must remain the approved 19 ranked IDs")
    require(ranks == list(range(1, 20)), "duplicate or reordered ranks")
    require(len({r.get("record_id") for r in records if isinstance(r, dict)}) == 29,
            "duplicate or malformed source record ID")

    by_name = {}
    for r in records:
        require(isinstance(r, dict), "invalid source record")
        name = canonical_source(r.get("product"))
        require(name not in by_name, "ambiguous or duplicate canonical source: " + name)
        require(isinstance(r.get("repository"), str) and r["repository"].startswith("hibi89/"),
                "source repository missing")
        require(isinstance(r.get("tracked_branch"), str) and bool(r["tracked_branch"]),
                "source tracked branch missing")
        by_name[name] = r

    source_memberships = []
    rows = []
    for service in services:
        sources = service.get("source_products")
        require(isinstance(sources, list) and len(sources) >= 1, "listing without source")
        status = service.get("listing_status")
        require(status in LISTING_STATES, "invalid listing state")
        history = service.get("listing_history")
        require(isinstance(history, list), "listing history must be retained as list")
        url, published = service.get("kmong_listing_url"), service.get("published_at_kst")
        registered_events = registration_events(history)
        if status == "미등록":
            require(not registered_events, "previously published listing cannot be reset to unregistered")
            if not history:
                require(url is None and published is None,
                        "unregistered listing has unproven URL or publication date")
        else:
            require(bool(history), "non-unregistered listing lacks lifecycle evidence")
        if status == "등록완료":
            require(bool(registered_events), "registered listing needs a verified-history reference")
            last = registered_events[-1]
            require(valid_kmong_url(url) and valid_publication_date(published) and
                    url == last["kmong_listing_url"] and
                    published == last["published_at_kst"],
                    "registered listing URL/date must match last historical registration")
        elif url is not None or published is not None:
            require(bool(registered_events) and
                    url == registered_events[-1]["kmong_listing_url"] and
                    published == registered_events[-1]["published_at_kst"],
                    "inactive listing URL/date must match last registered event")

        for name in sources:
            name = canonical_source(name)
            source_memberships.append(name)
            require(name in by_name, "listing references unknown source: " + name)
            r = by_name[name]
            rows.append({"record_id": r["record_id"], "product": r["product"],
                         "catalog_source": name, "service_id": service["service_id"],
                         "repository": r["repository"], "tracked_branch": r["tracked_branch"]})

    internal_names = []
    for platform in internal:
        require(isinstance(platform, dict), "invalid internal platform")
        names = platform.get("source_products")
        require(isinstance(names, list) and len(names) == 1, "expected one internal-only source")
        for name in names:
            name = canonical_source(name)
            internal_names.append(name)
            require(name in by_name, "internal platform references unknown source")
            r = by_name[name]
            rows.append({"record_id": r["record_id"], "product": r["product"],
                         "catalog_source": name, "service_id": None,
                         "repository": r["repository"], "tracked_branch": r["tracked_branch"]})

    union = source_memberships + internal_names
    require(len(source_memberships) == 28 and len(internal_names) == 1,
            "expected 28 listing assignments and one internal-only source")
    require(len(union) == 29 and len(set(union)) == 29, "duplicated catalog source assignment")
    require(set(union) == set(by_name), "orphan source or untracked catalog source")
    advertised = catalog.get("source_products_all_29")
    require(isinstance(advertised, list) and len(advertised) == 29,
            "source_products_all_29 missing entries")
    require(Counter(canonical_source(n) for n in advertised) == Counter(union),
            "advertised source inventory differs from listing/internal mapping")
    require(sum(1 for r in rows if r["service_id"] is None) == 1,
            "internal platform incorrectly listed as commercial SKU")

    lifecycle = catalog.get("listing_lifecycle")
    require(isinstance(lifecycle, dict) and lifecycle.get("policy") ==
            "PERMANENT_RETENTION_WITH_EVIDENCE", "permanent posting history policy missing")
    require(lifecycle.get("evidence_required_for_registered") is True,
            "registered listing evidence requirement disabled")
    require(set(lifecycle.get("status_values", [])) == LISTING_STATES,
            "listing state schema changed")
    # Registration is a durable historical fact even if a listing is later hidden,
    # suspended, or removed. Never reduce the tally to currently active listings.
    require(lifecycle.get("verified_registered_count") ==
            sum(bool(registration_events(s["listing_history"])) for s in services),
            "verified registration count must preserve historical completions")

    # Cross-validate official score *summary*, without authorizing a score change.
    summary = index.get("summary", {})
    require(isinstance(summary, dict), "official score summary missing")
    unassessed = sum(r.get("official_final_completion") == "UNASSESSED" for r in records)
    certified = sum(r.get("official_final_completion") == "100%" for r in records)
    require(summary.get("official_unassessed") == unassessed and
            summary.get("official_certified") == certified and
            summary.get("official_partial_scored") == 29 - unassessed - certified,
            "official source score summary mismatch")
    return sorted(rows, key=lambda r: r["record_id"])


def main():
    try:
        catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
        index = json.loads(INDEX.read_text(encoding="utf-8"))
        rows = validate(catalog, index)
    except (IntegrityError, OSError, ValueError, TypeError) as exc:
        print("KMONG_SKU_INTEGRITY: FAIL:", exc, file=sys.stderr)
        return 1
    listed = sum(r["service_id"] is not None for r in rows)
    print(f"KMONG_SKU_INTEGRITY: PASS source_products={len(rows)} "
          f"commercial_sources={listed} internal_only={len(rows)-listed} "
          "listings=19 aliases=1 official_scores=UNMODIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
