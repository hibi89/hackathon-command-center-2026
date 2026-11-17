#!/usr/bin/env python3
"""Accept exactly one newly added request in a push by the owner."""
import os
import re
import subprocess
import sys
from pathlib import Path

PREFIX = "requests/repo_provisioner/"


def eligible(path):
    return (
        path.startswith(PREFIX)
        and re.fullmatch(r"[a-z0-9][a-z0-9-]{3,79}\.json", path[len(PREFIX):]) is not None
        and Path(path).is_file()
        and not Path(path).is_symlink()
    )


def get_new_request(before, after, actor):
    if actor != "hibi89":
        raise ValueError("only an owner-attributed push can provision repositories")
    if not re.fullmatch(r"[0-9a-f]{40}", before) or not re.fullmatch(r"[0-9a-f]{40}", after):
        raise ValueError("invalid before/head SHA")
    r = subprocess.run(["git", "diff", "--name-status", before, after,
                        "--", PREFIX], capture_output=True, text=True, check=True)
    changes = [line.split("\t") for line in r.stdout.splitlines()]
    if len(changes) != 1 or len(changes[0]) != 2 or changes[0][0] != "A":
        raise ValueError("exactly one NEW JSON request is required; modifications ignored")
    path = changes[0][1]
    if not eligible(path):
        raise ValueError("invalid request path")
    return path


if __name__ == "__main__":
    try:
        path = get_new_request(os.environ["GITHUB_BEFORE"], os.environ["GITHUB_SHA"],
                               os.environ["GITHUB_ACTOR"])
        with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as f:
            f.write("request=" + path + "\n")
        print("Accepted one new request: " + path)
    except (KeyError, ValueError, subprocess.CalledProcessError) as e:
        print("REQUEST_REJECTED: " + str(e), file=sys.stderr)
        raise SystemExit(2)
