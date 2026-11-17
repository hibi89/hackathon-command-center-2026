#!/usr/bin/env python3
"""Create up to three PRIVATE repos from a validated owner request, then bootstrap policy.
Dry run by default. No deletion, rename, visibility changes or file overwrites.
"""
import argparse
import base64
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

OWNER = "hibi89"
CENTRAL = "hibi89/hackathon-command-center-2026"
NAME = re.compile(r"^[A-Za-z][A-Za-z0-9._-]{0,69}$")
REQ_ID = re.compile(r"^[a-z0-9][a-z0-9-]{3,79}$")
SHA = re.compile(r"^[0-9a-f]{40}$")
KEYS = {"schema_version", "request_id", "owner", "names", "project", "private", "approval"}


class ProvisionError(Exception):
    pass


def validate(req):
    if not isinstance(req, dict) or set(req) != KEYS or type(req["schema_version"]) is not int or req["schema_version"] != 1:
        raise ProvisionError("invalid request schema")
    if req["owner"] != OWNER or req["private"] is not True or type(req["private"]) is not bool:
        raise ProvisionError("only hibi89 PRIVATE repositories are permitted")
    if req["approval"] != "owner-requested-create-and-bootstrap-only":
        raise ProvisionError("owner approval marker missing")
    if not isinstance(req["request_id"], str) or not REQ_ID.fullmatch(req["request_id"]):
        raise ProvisionError("invalid request_id")
    if not isinstance(req["project"], str) or not 1 <= len(req["project"]) <= 90 or any(ord(c) < 32 or ord(c) == 127 for c in req["project"]):
        raise ProvisionError("invalid project name")
    names = req["names"]
    if not isinstance(names, list) or not 1 <= len(names) <= 3:
        raise ProvisionError("only 1..3 names per request")
    if any(not isinstance(n, str) or not NAME.fullmatch(n) or n.lower().endswith(".git") for n in names):
        raise ProvisionError("invalid repo name")
    if len(set(n.lower() for n in names)) != len(names):
        raise ProvisionError("duplicate name")
    return req


def documents(req, name, policy_sha):
    if not SHA.fullmatch(policy_sha):
        raise ProvisionError("exact central policy SHA required")
    base = "https://github.com/" + CENTRAL + "/blob/" + policy_sha + "/docs/strategy/"
    prov = dict(schema_version=1, request_id=req["request_id"],
                repository=OWNER + "/" + name, project=req["project"],
                policy_repo=CENTRAL, policy_branch="kmong-productization",
                policy_sha=policy_sha, product_implementation="NOT_STARTED",
                product_verification="UNASSESSED")
    agents = f"""# AGENTS — {name}

Project: {req["project"]}. Independent work area for parallel implementation.
Policy authority: {CENTRAL} at exact SHA {policy_sha}.
Central execution: {base}OWNER_DEV_EXECUTION_CANONICAL_20261116.md (§0J)
SWU standard: {base}GPT6_HIGH_STANDARD_WORK_UNIT_20261117.md (§0E)

## Mission and precedence
Latest user instructions and approved final blueprint/safety rules outrank project task notes. Refresh canonical remote HEAD before work. Initial bootstrapping does NOT authorize implementation scope or claim that a product is built.

## P1 development
Use SWU-CPAA for critical-path and dependency-aware READY selection and SWU-WE for 1..6 actual independent functional SWUs per chat turn when safe. Implement real caller-to-callee BE/FE/API/DB/CLI and core failure paths; preserve REQ/SWU IDs, allowed paths and interface contracts. Multiple independent GPT chats require distinct areas, one integration owner, shared base SHA and no conflicting writes.

On actual no-progress failure: two attempts -> ISOLATED_REDESIGN_PENDING, redesigned two further attempts -> SOLMAX_BATCH_PENDING. Essential high-risk blockage may request expertise earlier. Documentation/CI polling do not count as implementation. P1 syntax/type/smoke and urgent safety gates remain; P2 full CI, integration, security, browser, recovery and independent audit are NOT automatically done.

## Safety
No paid calls, customer data export, privilege expansion, secrets, destructive database writes, force push, main merge, Production, domain, commercial release or deletion without explicit owner approval. Protect original code, backup and history. Unrun checks must be NOT_RUN; unknown implementation or verification rate must be UNASSESSED. Exact branch/SHA and paths are required for progress reporting.
"""
    handoff = f"""# HANDOFF — {name}

State: P0_BOOTSTRAPPED. Product code: NOT_STARTED. P2: NOT_RUN.
Request: {req["request_id"]}. Central pinned policy SHA: {policy_sha}.
Assigned SWUs/REQs: UNASSIGNED. Allowed paths: UNASSIGNED.
Next: import owner-approved final blueprint, allocate independent module scope, fix API contracts and actual acceptance tests. No product implementation was performed by this bootstrap.
"""
    status = f"""# STATUS — {name}

Bootstrap documents exist. P1 implementation: NOT_STARTED / UNASSESSED.
P2 verification: NOT_RUN / UNASSESSED. Production and commercial GO: HOLD.
Request: {req["request_id"]}; pinned canonical SHA: {policy_sha}.
"""
    requirements = f"""# REQUIREMENTS — {name}

Product-specific requirements, SWUs and acceptance conditions: UNASSESSED.
This is a placeholder, NOT authorization to reduce or invent product scope.
Before implementation import the approved blueprint and assign REQ IDs, module contracts, dependencies and allowed paths.
"""
    return {
        ".haechong-provisioner.json": json.dumps(prov, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        "AGENTS.md": agents, "HANDOFF.md": handoff,
        "STATUS.md": status, "REQUIREMENTS.md": requirements,
    }


class GitHub:
    def __init__(self, token):
        if not token or any(c.isspace() for c in token):
            raise ProvisionError("dedicated provisioner token is missing")
        self.token = token

    def api(self, method, path, body=None):
        req = urllib.request.Request(
            "https://api.github.com" + path, method=method,
            data=json.dumps(body).encode() if body is not None else None,
            headers={"Accept": "application/vnd.github+json",
                     "Content-Type": "application/json",
                     "X-GitHub-Api-Version": "2026-03-10",
                     "Authorization": "Bearer " + self.token,
                     "User-Agent": "haechong-repo-provisioner/1"})
        try:
            with urllib.request.urlopen(req, timeout=20) as r:
                payload = r.read(200000)
                return r.status, json.loads(payload) if payload else {}
        except urllib.error.HTTPError as e:
            if method == "GET" and e.code == 404:
                return 404, None
            raise ProvisionError(f"GitHub API {method} {path}: HTTP {e.code}") from None
        except urllib.error.URLError:
            raise ProvisionError("GitHub network failure") from None


def put_new(client, name, branch, filename, data):
    path = f"/repos/{OWNER}/{urllib.parse.quote(name)}/contents/{filename}"
    status, _ = client.api("GET", path)
    if status == 200:
        return "PRESERVED"
    status, _ = client.api("PUT", path, {
        "message": "docs(bootstrap): add " + filename,
        "content": base64.b64encode(data.encode()).decode(),
        "branch": branch,
    })
    if status not in (200, 201):
        raise ProvisionError("bootstrap write failed: " + filename)
    return "CREATED"


def create_one(client, req, name, policy_sha):
    path = f"/repos/{OWNER}/{urllib.parse.quote(name)}"
    files = documents(req, name, policy_sha)
    status, current = client.api("GET", path)
    created = status == 404
    if created:
        _, current = client.api("POST", "/user/repos", {
            "name": name, "private": True, "auto_init": True,
            "description": req["project"] + " — independent Haechong P1 work area"})
        if current.get("full_name", "").lower() != f"{OWNER}/{name}".lower() or current.get("private") is not True:
            raise ProvisionError("unexpected create response; inspect manually")
    else:
        if current.get("private") is not True:
            raise ProvisionError("existing repo must remain untouched: " + name)
        markpath = path + "/contents/.haechong-provisioner.json"
        s, marker = client.api("GET", markpath)
        if s != 200:
            raise ProvisionError("existing repo not owned by this request: " + name)
        try:
            prior = json.loads(base64.b64decode(marker["content"]).decode())
        except (ValueError, KeyError, UnicodeError):
            raise ProvisionError("unreadable existing provenance: " + name) from None
        if prior != json.loads(files[".haechong-provisioner.json"]):
            raise ProvisionError("provenance conflict: " + name)
    branch = current.get("default_branch") or "main"
    if not re.fullmatch(r"[A-Za-z0-9._/-]{1,100}", branch):
        raise ProvisionError("invalid GitHub default branch")
    # Marker first makes partial failures resumable. Never overwrite any file.
    for filename, content in files.items():
        put_new(client, name, branch, filename, content)
    return {"repository": OWNER + "/" + name,
            "url": f"https://github.com/{OWNER}/{name}",
            "result": "CREATED" if created else "RESUMED"}


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("--request", required=True)
    p.add_argument("--policy-sha", required=True)
    p.add_argument("--execute", action="store_true")
    p.add_argument("--confirm", default="")
    args = p.parse_args(argv)
    try:
        reqfile = Path(args.request)
        if not reqfile.is_file() or reqfile.suffix != ".json":
            raise ProvisionError("JSON request file is required")
        req = validate(json.loads(reqfile.read_text(encoding="utf-8")))
        documents(req, req["names"][0], args.policy_sha)
        if not args.execute:
            print(json.dumps({"result": "DRY_RUN", "writes": False, "names": req["names"]},
                             ensure_ascii=False))
            return 0
        if args.confirm != req["request_id"] or os.getenv("HAECHONG_PROVISIONER_ENABLE") != "YES_CREATE_PRIVATE_REPOS":
            raise ProvisionError("execution requires explicit matching confirmation and enabled gate")
        client = GitHub(os.getenv("GH_REPO_PROVISIONER_TOKEN"))
        completed = 0
        for name in req["names"]:
            try:
                print(json.dumps(create_one(client, req, name, args.policy_sha)), flush=True)
                completed += 1
            except ProvisionError as e:
                raise ProvisionError(f"PARTIAL completed={completed}; stopped at {name}: {e}") from None
        print(json.dumps({"result": "CREATED_OR_RESUMED", "count": completed}))
        return 0
    except (ProvisionError, OSError, ValueError) as e:
        print("PROVISIONER_ERROR: " + str(e), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
