"""Fail-closed zero-cost budget/burst gate for a read-only GitHub App observer.

This gate never touches source repositories or central observation JSON.
A deferred workflow job is NOT a successful snapshot sync. A valid allow
decision authorizes only the existing observer; its own checks still apply.
"""
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

BOT_ACTOR = "kmong-hub-dispatcher[bot]"
CORE_RESERVE = 450  # conservative floor for the 35-repo/80-ref/29-product scan
BURST_WINDOW_SECONDS = 1800
RUNS_ENDPOINT = ("/repos/hibi89/hackathon-command-center-2026/"
                 "actions/workflows/kmong-hub-sync.yml/runs"
                 "?event=workflow_dispatch&per_page=100")


class GuardError(RuntimeError):
    pass


def utc_epoch(value):
    if not isinstance(value, str):
        raise GuardError("missing workflow run timestamp")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise GuardError("invalid workflow run timestamp") from exc
    if parsed.tzinfo is None:
        raise GuardError("workflow run timestamp has no timezone")
    return int(parsed.timestamp())


def core_budget(payload):
    if not isinstance(payload, dict):
        raise GuardError("invalid rate limit response")
    core = payload.get("resources", {}).get("core")
    if not isinstance(core, dict):
        raise GuardError("missing core rate budget")
    remaining, reset = core.get("remaining"), core.get("reset")
    if type(remaining) is not int or remaining < 0 or type(reset) is not int or reset <= 0:
        raise GuardError("invalid primary rate budget data")
    return remaining, reset


def bot_is_first_eligible_run(payload, current_run_id):
    if not isinstance(payload, dict) or not isinstance(payload.get("workflow_runs"), list):
        raise GuardError("invalid workflow run list")
    if not str(current_run_id).isdigit():
        raise GuardError("invalid current workflow run id")
    runs = payload["workflow_runs"]
    own = next((r for r in runs if isinstance(r, dict) and r.get("id") == int(current_run_id)), None)
    if own is None or own.get("event") != "workflow_dispatch":
        raise GuardError("bot dispatch was not found among the latest 100 runs")
    if own.get("actor", {}).get("login") != BOT_ACTOR:
        raise GuardError("unexpected bot dispatch actor")
    own_bucket = utc_epoch(own.get("created_at")) // BURST_WINDOW_SECONDS
    for prior in runs:
        if (not isinstance(prior, dict) or prior.get("event") != "workflow_dispatch"
                or prior.get("actor", {}).get("login") != BOT_ACTOR
                or prior.get("conclusion") == "cancelled"
                or type(prior.get("id")) is not int
                or prior["id"] >= int(current_run_id)):
            continue
        if utc_epoch(prior.get("created_at")) // BURST_WINDOW_SECONDS == own_bucket:
            return False
    # If 100 runs filled the API page within one bucket, do not assert uniqueness.
    if len(runs) == 100 and utc_epoch(runs[-1].get("created_at")) // BURST_WINDOW_SECONDS >= own_bucket:
        return False
    return True


def decide(remaining, event, actor, run_id=None, runs=None):
    if type(remaining) is not int or remaining < 0:
        raise GuardError("invalid remaining budget")
    if remaining < CORE_RESERVE:
        return "DEFERRED_PRIMARY_BUDGET"
    if event == "workflow_dispatch" and actor == BOT_ACTOR:
        if runs is None or not bot_is_first_eligible_run(runs, run_id):
            return "DEFERRED_BOT_BURST"
    return "RUN"


def github_read(path, token):
    if not token or not path.startswith("/") or "://" in path:
        raise GuardError("invalid preflight GitHub request")
    req = Request(
        "https://api.github.com" + path,
        headers={"Authorization": "Bearer " + token,
                 "Accept": "application/vnd.github+json",
                 "X-GitHub-Api-Version": "2022-11-28",
                 "User-Agent": "kmong-hub-safe-scan-gate"},
    )
    try:
        with urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except HTTPError as exc:
        raise GuardError(f"GitHub preflight HTTP {exc.code}; full scan not started") from None
    except (URLError, TimeoutError, UnicodeError, ValueError):
        raise GuardError("GitHub preflight read failed; full scan not started") from None


def publish(reason, remaining, reset):
    flag = "true" if reason == "RUN" else "false"
    output_path = os.environ.get("GITHUB_OUTPUT")
    if not output_path:
        raise GuardError("GITHUB_OUTPUT required to safely gate the next step")
    with open(output_path, "a", encoding="utf-8") as f:
        f.write("run_sync=" + flag + "\n")
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        reset_iso = datetime.fromtimestamp(reset, timezone.utc).isoformat()
        with open(summary_path, "a", encoding="utf-8") as f:
            f.write("### Kmong source App scan preflight\n")
            f.write(f"- Verdict: **{reason}** (NOT a sync outcome)\n")
            f.write(f"- Primary core remaining: {remaining}; reserve floor: {CORE_RESERVE}; reported reset: {reset_iso}\n")
            f.write("- When deferred: source scan **NOT_STARTED**; hub snapshot **UNCHANGED**; official scores **UNCHANGED**.\n")
            f.write("- When allowed: the separate scan step must still pass to claim UPDATED/NO_CHANGE.\n")
    print("KMONG PREFLIGHT:", reason, "remaining:", remaining, "reserve:", CORE_RESERVE)


def main():
    token = os.getenv("KMONG_SOURCE_APP_TOKEN")
    if not token:
        raise GuardError("source App token unavailable")
    # GitHub documents that GET /rate_limit does not spend the primary rate budget.
    remaining, reset = core_budget(github_read("/rate_limit", token))
    event, actor = os.getenv("GITHUB_EVENT_NAME", ""), os.getenv("GITHUB_ACTOR", "")
    runs = None
    if remaining >= CORE_RESERVE and event == "workflow_dispatch" and actor == BOT_ACTOR:
        runs = github_read(RUNS_ENDPOINT, token)
    result = decide(remaining, event, actor, os.getenv("GITHUB_RUN_ID"), runs)
    publish(result, remaining, reset)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (GuardError, OSError, OverflowError) as exc:
        print("KMONG PREFLIGHT BLOCKED:", str(exc), file=sys.stderr)
        sys.exit(1)
