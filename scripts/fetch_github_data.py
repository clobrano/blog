#!/usr/bin/env python3
"""Fetch GitHub repo metadata and README for each project in projects.txt.

Creates/updates content/projects/<repo>/index.md with frontmatter + README body.
Set GITHUB_TOKEN env var to avoid rate limiting (60 req/hr unauthenticated).

Usage:
    python3 scripts/fetch_github_data.py
"""

import base64
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent
PROJECTS_FILE = SCRIPT_DIR / "projects.txt"
CONTENT_DIR = REPO_ROOT / "content" / "projects"

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")


def github_request(url: str) -> dict:
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    if GITHUB_TOKEN:
        req.add_header("Authorization", f"Bearer {GITHUB_TOKEN}")
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        print(f"  ERROR {e.code} fetching {url}: {e.reason}", file=sys.stderr)
        return {}


def fetch_readme(owner: str, repo: str) -> str:
    data = github_request(f"https://api.github.com/repos/{owner}/{repo}/readme")
    if not data or "content" not in data:
        return ""
    raw = base64.b64decode(data["content"]).decode("utf-8", errors="replace")
    # download_url: "https://raw.githubusercontent.com/{owner}/{repo}/{branch}/README.md"
    download_url = data.get("download_url", "")
    base_raw = download_url.rsplit("/", 1)[0] if download_url else f"https://raw.githubusercontent.com/{owner}/{repo}/main"
    # html_url: "https://github.com/{owner}/{repo}/blob/{branch}/README.md"
    html_url = data.get("html_url", "")
    base_blob = html_url.rsplit("/", 1)[0] if html_url else f"https://github.com/{owner}/{repo}/blob/main"

    def fix_img(m):
        alt, src = m.group(1), m.group(2)
        if src.startswith("http"):
            return m.group(0)
        return f"![{alt}]({base_raw}/{src.lstrip('/')})"

    def fix_link(m):
        text, href = m.group(1), m.group(2)
        if href.startswith("http") or href.startswith("#"):
            return m.group(0)
        return f"[{text}]({base_blob}/{href.lstrip('/')})"

    raw = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", fix_img, raw)
    raw = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", fix_link, raw)
    return raw


def write_project_page(owner: str, repo: str, meta: dict, readme: str):
    dest = CONTENT_DIR / repo
    dest.mkdir(parents=True, exist_ok=True)

    topics = meta.get("topics") or []
    topics_yaml = "\n".join(f'  - "{t}"' for t in topics)

    pushed_at = meta.get("pushed_at") or meta.get("updated_at") or ""
    if pushed_at:
        # Normalize to Hugo-compatible date
        try:
            pushed_at = datetime.strptime(pushed_at, "%Y-%m-%dT%H:%M:%SZ").strftime(
                "%Y-%m-%dT%H:%M:%SZ"
            )
        except ValueError:
            pass

    frontmatter = f"""\
---
title: "{meta.get('name', repo)}"
description: "{(meta.get('description') or '').replace('"', "'")}"
date: "{pushed_at}"
github_url: "{meta.get('html_url', '')}"
stars: {meta.get('stargazers_count', 0)}
forks: {meta.get('forks_count', 0)}
language: "{meta.get('language') or ''}"
topics:
{topics_yaml if topics_yaml else '  []'}
---
"""

    page = dest / "index.md"
    page.write_text(frontmatter + "\n" + readme, encoding="utf-8")
    print(f"  written {page.relative_to(REPO_ROOT)}")


def load_repos() -> list[tuple[str, str]]:
    repos = []
    for line in PROJECTS_FILE.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split("/")
        if len(parts) != 2:
            print(f"  SKIP malformed line: {line}", file=sys.stderr)
            continue
        repos.append((parts[0], parts[1]))
    return repos


def main():
    if not GITHUB_TOKEN:
        print("Warning: GITHUB_TOKEN not set — rate limit is 60 req/hr", file=sys.stderr)

    repos = load_repos()
    if not repos:
        print("No repos found in projects.txt", file=sys.stderr)
        sys.exit(1)

    for owner, repo in repos:
        print(f"Fetching {owner}/{repo}...")
        meta = github_request(f"https://api.github.com/repos/{owner}/{repo}")
        if not meta:
            print(f"  SKIP — could not fetch metadata")
            continue
        readme = fetch_readme(owner, repo)
        if not readme:
            print(f"  Warning: no README found")
        write_project_page(owner, repo, meta, readme)

    print("Done.")


if __name__ == "__main__":
    main()
