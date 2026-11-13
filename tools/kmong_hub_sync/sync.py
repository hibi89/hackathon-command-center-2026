#!/usr/bin/env python3
"""Read-only GitHub App evidence collection; sole write target is the central observation JSON.

No official completion scoring, private file contents, code execution or source-repo writes.
"""
import base64
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "tools/final_blueprint_gate/canonical_pins.json"
ROSTER = ROOT / "tools/kmong_hub_sync/source_repositories.json"
HUB_REPO = "hibi89/hackathon-command-center-2026"
HUB_BRANCH = "kmong-productization"
INDEX_PATH = "data/final_blueprint_product_index_20261113.json"
SNAPSHOT_PATH = "data/kmong_hub_auto_observations.json"
SHA40 = re.compile(r"^[0-9a-f]{40}$")
REPO_RE = re.compile(r"^hibi89/[A-Za-z0-9_.-]+$", re.I)
REF_RE = re.compile(r"^[A-Za-z0-9._/-]+$")
PIN_MODES = {"observe", "enforce"}


def safe_ref(ref):
    return (isinstance(ref, str) and bool(REF_RE.fullmatch(ref))
            and not ref.startswith(("/", "-")) and not ref.endswith("/")
            and all(part not in {"", ".", ".."} for part in ref.split("/")))


def validate_registry(roster, registry):
    repos = roster.get("repositories") if isinstance(roster, dict) else None
    pins = registry.get("pins") if isinstance(registry, dict) else None
    missing = registry.get("not_pinned_main") if isinstance(registry, dict) else None
    if not isinstance(repos, list) or not isinstance(pins, list) or not isinstance(missing, list):
        raise ValueError("roster and pin registry must contain arrays")
    if roster.get("schema_version") != 1 or registry.get("schema_version") != 1:
        raise ValueError("unsupported schema")
    if len(repos) != 35 or len(pins) != 31 or len(missing) != 4:
        raise ValueError("35-repository / 31-pin / 4-unpinned inventory changed; review before sync")
    names, branches = set(), set()
    for entry in repos:
        name = entry.get("repository")
        if not isinstance(name, str) or not REPO_RE.fullmatch(name) or name.lower() in names:
            raise ValueError("invalid or duplicate repository")
        names.add(name.lower())
        work = entry.get("branches")
        if not isinstance(work, list):
            raise ValueError("branches must be a list")
        for branch in work:
            if not safe_ref(branch) or branch == "main" or (name.lower(), branch) in branches:
                raise ValueError("unsafe or duplicate work branch")
            branches.add((name.lower(), branch))
    if len(branches) != 35:
        raise ValueError("expected 35 explicitly tracked work branches")
    pinned = set()
    for pin in pins:
        name, ref, path, blob = (pin.get(k) for k in ("repository", "ref", "path", "git_blob_sha"))
        if not isinstance(name, str) or name.lower() not in names or name.lower() in pinned:
            raise ValueError("invalid or duplicate pin repository")
        pinned.add(name.lower())
        if not safe_ref(ref) or not isinstance(path, str) or not path or path.startswith("/") or ".." in path.split("/"):
            raise ValueError("invalid pin ref/path")
        if not isinstance(blob, str) or not SHA40.fullmatch(blob) or pin.get("mode") not in PIN_MODES:
            raise ValueError("invalid pin digest/mode")
    unpinned = set()
    for name in missing:
        if not isinstance(name, str) or name.lower() not in names or name.lower() in unpinned:
            raise ValueError("invalid unpinned repository")
        unpinned.add(name.lower())
    if pinned & unpinned or pinned | unpinned != names:
        raise ValueError("pin inventory does not cover exact repository roster")
    return repos, {p["repository"].lower(): p for p in pins}


def load_registry():
    roster = json.loads(ROSTER.read_text(encoding="utf-8"))
    pins = json.loads(REGISTRY.read_text(encoding="utf-8"))
    repos, mapped = validate_registry(roster, pins)
    return sorted(repos, key=lambda x: x["repository"].lower()), mapped


def decode_contents(obj):
    if not isinstance(obj, dict) or obj.get("type") != "file" or obj.get("encoding") != "base64":
        raise ValueError("GitHub contents API did not return a plain file")
    text = base64.b64decode(obj["content"], validate=False).decode("utf-8")
    return json.loads(text)


class GitHubAPI:
    def get(self, path, token, allow_404=False):
        return self._request("GET", path, token, None, allow_404)

    def put(self, path, token, data):
        return self._request("PUT", path, token, data, False)

    def _request(self, method, path, token, payload, allow_404):
        if not token or not path.startswith("/") or "://" in path:
            raise RuntimeError("invalid token or GitHub endpoint")
        body = json.dumps(payload, separators=(",", ":")).encode() if payload is not None else None
        req = Request("https://api.github.com" + path, data=body, method=method,
                      headers={"Authorization": "Bearer " + token,
                               "Accept": "application/vnd.github+json",
                               "X-GitHub-Api-Version": "2022-11-28",
                               "Content-Type": "application/json",
                               "User-Agent": "kmong-hub-source-observer"})
        for attempt in range(2):
            try:
                with urlopen(req, timeout=20) as resp:
                    return json.loads(resp.read().decode("utf-8"))
            except HTTPError as exc:
                if allow_404 and exc.code == 404:
                    return None
                if exc.code in {429, 502, 503, 504} and attempt == 0:
                    time.sleep(1)
                    continue
                raise RuntimeError(f"GitHub {method} returned HTTP {exc.code}; no source/hub write accepted") from None
            except (URLError, TimeoutError) as exc:
                if attempt == 0:
                    time.sleep(1)
                    continue
                raise RuntimeError("GitHub API network error; no source/hub write accepted") from exc
        raise RuntimeError("API retry exhausted")


class Observer:
    def __init__(self, api, token):
        self.api, self.token = api, token
        self.refs = {}
        self.runs = {}

    def api_get(self, path, allow_404=False):
        return self.api.get(path, self.token, allow_404=allow_404)

    def check_installation(self, expected_names):
        obj = self.api_get("/installation/repositories?per_page=100")
        installed = {r["full_name"].lower() for r in obj.get("repositories", []) if isinstance(r, dict)}
        if obj.get("total_count") != len(installed) or installed != {x.lower() for x in expected_names}:
            raise RuntimeError("App installation token is not scoped to exactly 35 approved repositories")
        return len(installed)

    def head(self, repo, branch, missing_ok=False):
        key = (repo, branch)
        if key not in self.refs:
            obj = self.api_get(f"/repos/{repo}/git/ref/heads/{quote(branch, safe='/')}",
                               allow_404=missing_ok)
            sha = obj.get("object", {}).get("sha") if obj else None
            if obj and (not isinstance(sha, str) or not SHA40.fullmatch(sha)):
                raise RuntimeError("invalid Git ref object")
            self.refs[key] = {"status": "PRESENT" if sha else "MISSING", "sha": sha}
        result = self.refs[key]
        if result["status"] == "MISSING" and not missing_ok:
            raise RuntimeError("configured repository main or blueprint ref not accessible")
        return result

    def workflow_run(self, repo, branch, head_sha):
        key = (repo, branch)
        if key not in self.runs:
            data = self.api_get(
                f"/repos/{repo}/actions/workflows/final-blueprint-gate.yml/runs"
                f"?branch={quote(branch, safe='')}&per_page=1", allow_404=True)
            if data is None:
                result = {"status": "WORKFLOW_NOT_AVAILABLE"}
            else:
                runs = data.get("workflow_runs", [])
                if not isinstance(runs, list):
                    raise RuntimeError("invalid Actions run list")
                if runs:
                    run = runs[0]
                    sha = run.get("head_sha")
                    run_id = run.get("id")
                    if not isinstance(sha, str) or not SHA40.fullmatch(sha) or type(run_id) is not int:
                        raise RuntimeError("invalid workflow run metadata")
                    result = {"status": "LATEST_RUN", "run_id": run_id,
                              "head_sha": sha, "conclusion": run.get("conclusion"),
                              "workflow_status": run.get("status"),
                              "matches_current_head": bool(head_sha and sha == head_sha)}
                else:
                    result = {"status": "NO_RUN"}
            self.runs[key] = result
        return self.runs[key]

    def branch_status(self, repo, branch, required=False):
        head = self.head(repo, branch, missing_ok=not required)
        if head["sha"] is None:
            return {"branch": branch, "status": "MISSING"}
        return {"branch": branch, "status": "PRESENT", "head_sha": head["sha"],
                "gate": self.workflow_run(repo, branch, head["sha"])}

    def blueprint(self, repo, pin):
        if pin is None:
            return {"status": "NOT_CONFIGURED"}
        ref, path = pin["ref"], pin["path"]
        head = self.head(repo, ref, missing_ok=True)
        meta = {"ref": ref, "path": path, "mode": pin["mode"],
                "expected_git_blob_sha": pin["git_blob_sha"], "head_sha": head["sha"],
                "owner_approval_verified": False}
        if not head["sha"]:
            return {**meta, "status": "MISSING_REF"}
        obj = self.api_get(f"/repos/{repo}/contents/{quote(path, safe='/')}?ref={quote(ref, safe='')}",
                           allow_404=True)
        if obj is None or obj.get("type") != "file":
            return {**meta, "status": "MISSING_FILE"}
        observed = obj.get("sha")
        if not isinstance(observed, str) or not SHA40.fullmatch(observed):
            raise RuntimeError("invalid canonical Git blob metadata")
        return {**meta, "observed_git_blob_sha": observed,
                "status": "MATCHED" if observed == pin["git_blob_sha"] else
                ("DRIFT_DETECTED" if pin["mode"] == "enforce" else "DRIFT_REVIEW_REQUIRED")}


def collect_snapshot(observer, roster, pins, index):
    products = index.get("records") if isinstance(index, dict) else None
    if not isinstance(products, list) or len(products) != 29:
        raise ValueError("central 29-product index must be independently reviewable")
    ids = [p.get("record_id") for p in products]
    if len(set(ids)) != 29:
        raise ValueError("duplicate product ID")
    names = [r["repository"] for r in roster]
    observer.check_installation(names)
    rows = []
    for entry in roster:
        name = entry["repository"]
        main = observer.branch_status(name, "main", required=True)
        branches = [observer.branch_status(name, b) for b in entry["branches"]]
        rows.append({"repository": name, "main": main, "work_branches": branches,
                     "canonical": observer.blueprint(name, pins.get(name.lower()))})
    allowed = {n.lower() for n in names}
    linked = []
    for p in products:
        name, branch = p.get("repository"), p.get("tracked_branch")
        out = {"record_id": p["record_id"], "repository": name,
               "tracked_branch": branch, "status": "NOT_LINKED"}
        if isinstance(name, str) and name.lower() in allowed and safe_ref(branch):
            ref = observer.branch_status(name, branch)
            out["status"] = ref["status"]
            if ref["status"] == "PRESENT":
                out["head_sha"] = ref["head_sha"]
                out["gate"] = ref["gate"]
        linked.append(out)
    issues = [r["repository"] for r in rows if r["canonical"]["status"] in
              {"DRIFT_DETECTED", "MISSING_REF", "MISSING_FILE"}
              and r["canonical"].get("mode") == "enforce"]
    return {"schema_version": 1, "generated_by": "kmong-hub-sync",
            "policy": "OWNER-FINAL-BLUEPRINT-100",
            "scope": "GitHub ref, Actions and blueprint fingerprint observations only",
            "no_official_score_authorization": True,
            "summary": {"repository_count": len(rows),
                        "tracked_branch_count": len(rows) + sum(len(r["work_branches"]) for r in rows),
                        "product_links": len(linked),
                        "canonical_matched": sum(r["canonical"]["status"] == "MATCHED" for r in rows),
                        "canonical_not_configured": sum(r["canonical"]["status"] == "NOT_CONFIGURED" for r in rows),
                        "blocking_fingerprint_issues": len(issues)},
            "blocking_repositories": issues,
            "repositories": rows, "products": linked}


def hub_path(path, branch=None):
    suffix = "?ref=" + quote(branch, safe="") if branch else ""
    return f"/repos/{HUB_REPO}/contents/{path}{suffix}"


def reconcile_hub(api, token, snapshot, dry_run):
    if not token:
        raise RuntimeError("central GITHUB_TOKEN is missing")
    path = hub_path(SNAPSHOT_PATH)
    existing = api.get(hub_path(SNAPSHOT_PATH, HUB_BRANCH), token, allow_404=True)
    if existing is not None:
        current = decode_contents(existing)
        if not isinstance(current, dict) or current.get("generated_by") != "kmong-hub-sync":
            raise RuntimeError("destination is not a managed evidence snapshot; refuse overwrite")
        if current == snapshot:
            return {"result": "NO_CHANGE", "commit": None}
    if dry_run:
        return {"result": "DRY_RUN", "commit": None}
    raw = json.dumps(snapshot, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    put = {"message": "chore(kmong): refresh read-only GitHub evidence snapshot [skip ci]",
           "branch": HUB_BRANCH, "content": base64.b64encode(raw.encode()).decode()}
    if existing is not None:
        put["sha"] = existing["sha"]  # optimistic concurrency; never force overwrite
    response = api.put(path, token, put)
    commit = response.get("commit", {}).get("sha")
    if not isinstance(commit, str) or not SHA40.fullmatch(commit):
        raise RuntimeError("GitHub did not confirm a commit SHA")
    checked = api.get(hub_path(SNAPSHOT_PATH, HUB_BRANCH), token)
    if decode_contents(checked) != snapshot:
        raise RuntimeError("remote snapshot content did not match the committed observation")
    return {"result": "UPDATED", "commit": commit}


def determine_dry_run(event_name, manual_input):
    """Scheduled trusted runs may write; manual runs default to safe read-only."""
    if event_name == "schedule":
        return False
    if event_name == "workflow_dispatch":
        return str(manual_input).lower() != "false"
    return True


def run():
    roster, pins = load_registry()
    source_token = os.getenv("KMONG_SOURCE_APP_TOKEN")
    hub_token = os.getenv("KMONG_HUB_TOKEN")
    if not source_token or not hub_token or source_token == hub_token:
        raise RuntimeError("independent read-only GitHub App and central GITHUB_TOKEN required")
    api = GitHubAPI()
    index = decode_contents(api.get(hub_path(INDEX_PATH, HUB_BRANCH), hub_token))
    observer = Observer(api, source_token)
    snapshot = collect_snapshot(observer, roster, pins, index)
    dry_run = determine_dry_run(os.getenv("GITHUB_EVENT_NAME", ""),
                                os.getenv("KMONG_SYNC_DRY_RUN", ""))
    result = reconcile_hub(api, hub_token, snapshot, dry_run)
    summary = snapshot["summary"]
    print("KMONG HUB SYNC:", result["result"], "repositories:", summary["repository_count"],
          "tracked branches:", summary["tracked_branch_count"],
          "product links:", summary["product_links"],
          "fingerprint alerts:", summary["blocking_fingerprint_issues"],
          "official scores: UNMODIFIED")
    if result["commit"]:
        print("Hub commit:", result["commit"])
    if os.getenv("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as f:
            f.write("### Read-only Kmong evidence sync\n")
            f.write(f"- Outcome: **{result['result']}**\n")
            f.write(f"- Repositories: {summary['repository_count']} / tracked refs: {summary['tracked_branch_count']}\n")
            f.write(f"- Product links: {summary['product_links']} / fingerprint alerts: {summary['blocking_fingerprint_issues']}\n")
            f.write("- Official completion and registered-product history: **unchanged**\n")
    if summary["blocking_fingerprint_issues"]:
        raise RuntimeError("enforced canonical fingerprint drift detected; official scores unchanged")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(run())
    except (RuntimeError, ValueError, OSError, KeyError, TypeError) as exc:
        print("KMONG HUB SYNC BLOCKED:", str(exc), file=sys.stderr)
        sys.exit(1)
