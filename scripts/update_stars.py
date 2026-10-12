#!/usr/bin/env python3

from __future__ import annotations

import json
import os
import tempfile
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen


USERNAME = "qhy991"
ASSET = Path(__file__).resolve().parents[1] / "assets" / "total-stars.svg"


@dataclass(frozen=True)
class Stars:
    total: int
    repository_count: int


def fetch_total_stars() -> Stars:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "qhy991-profile-stars",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    total = 0
    repository_count = 0
    page = 1
    while True:
        url = (
            f"https://api.github.com/users/{USERNAME}/repos"
            f"?type=owner&per_page=100&sort=full_name&direction=asc&page={page}"
        )
        with urlopen(Request(url, headers=headers), timeout=30) as response:
            repositories = json.load(response)
        if not isinstance(repositories, list) or len(repositories) > 100:
            raise ValueError(f"Invalid repository page {page}")
        for repository in repositories:
            if not isinstance(repository, dict):
                raise ValueError(f"Invalid repository on page {page}")
            owner = repository.get("owner")
            private = repository.get("private")
            if (
                not isinstance(owner, dict)
                or not isinstance(owner.get("login"), str)
                or not isinstance(private, bool)
            ):
                raise ValueError(f"Invalid repository visibility or owner on page {page}")
            if private or owner["login"].casefold() != USERNAME.casefold():
                continue
            stars = repository.get("stargazers_count")
            if type(stars) is not int or stars < 0:
                raise ValueError(f"Invalid star count on page {page}")
            total += stars
            repository_count += 1
        if len(repositories) < 100:
            return Stars(total, repository_count)
        page += 1


def render_svg(stars: Stars, checked: date) -> str:
    total = f"{stars.total:,}"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="420" height="100" viewBox="0 0 420 100" role="img" aria-labelledby="title desc">
  <title id="title">{total} total stars across {stars.repository_count} public repositories owned by {USERNAME}. Checked {checked.isoformat()} UTC.</title>
  <desc id="desc">Includes forks and archived repositories. Refreshed daily from the GitHub API.</desc>
  <rect x="0.5" y="0.5" width="419" height="99" rx="12" fill="#0d1117" stroke="#30363d"/>
  <g font-family="-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif">
    <text x="20" y="25" fill="#8b949e" font-size="13">Total stars</text>
    <text x="20" y="62" fill="#58a6ff" font-size="32" font-weight="700">{total}</text>
    <text x="20" y="84" fill="#8b949e" font-size="11">{stars.repository_count} public repos · Checked {checked.isoformat()} UTC</text>
  </g>
</svg>
'''


def update_asset(path: Path, svg: str) -> bool:
    if path.exists() and path.read_text(encoding="utf-8") == svg:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=path.parent, delete=False
        ) as temporary:
            temporary_path = Path(temporary.name)
            temporary.write(svg)
        temporary_path.chmod(0o644)
        temporary_path.replace(path)
    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)
    return True


def refresh(path: Path = ASSET, checked: date | None = None) -> Stars:
    stars = fetch_total_stars()
    checked = checked or datetime.now(timezone.utc).date()
    changed = update_asset(path, render_svg(stars, checked))
    print(f"{stars.total:,} stars across {stars.repository_count} public repositories; asset changed: {changed}")
    return stars


if __name__ == "__main__":
    refresh()
