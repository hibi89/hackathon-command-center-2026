"""Explicit single-shot CLI. No implicit polling or external network."""
import argparse
import sys
from datetime import datetime, timezone
from .core import GuardError, History, head_probe, load_targets


def main(argv=None):
    ap = argparse.ArgumentParser(description="UPTIME OPS consent-gated local preview")
    ap.add_argument("--config", required=True, help="local explicit allowlist JSON")
    ap.add_argument("--db", help="local SQLite evidence file")
    ap.add_argument("--target", help="one authorized target ID")
    ap.add_argument("--live", action="store_true", help="explicitly allow one real HEAD")
    ap.add_argument("--export-csv", help="write a NEW CSV file (no overwrite)")
    args = ap.parse_args(argv)
    try:
        targets = load_targets(args.config)
        if args.live:
            if not args.db or not args.target:
                raise GuardError("--live requires --target and --db")
            selected = next((t for t in targets if t.target_id == args.target), None)
            if selected is None:
                raise GuardError("unknown, unapproved target ID")
            result = head_probe(selected)
            db = History(args.db)
            try:
                events = db.record(selected, result, datetime.now(timezone.utc))
                if args.export_csv:
                    db.export_csv(args.export_csv)
            finally:
                db.close()
            print("UPTIME_OPS: " + result.state + " " + result.detail +
                  " events=" + ",".join(events))
            return 0 if result.state == "UP" else 2
        if args.export_csv:
            if not args.db:
                raise GuardError("CSV export requires --db")
            db = History(args.db)
            try:
                db.export_csv(args.export_csv)
            finally:
                db.close()
        print("UPTIME_OPS: CONFIG_VALIDATED_NO_NETWORK targets=" + str(len(targets)))
        return 0
    except (GuardError, OSError, ValueError) as exc:
        print("UPTIME_OPS: REFUSED: " + str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
