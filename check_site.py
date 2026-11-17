#!/usr/bin/env python3
"""Check the static publish directory and, optionally, the deployed research route."""

import argparse
import sys
from pathlib import Path
from urllib.parse import urljoin
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent
RESEARCH_ROUTE = "research/higgsfield-cli-flow/"
RESEARCH_TITLE = "<title>Higgsfield CLI · 运行时流程版</title>"


def check_research_page(html):
    if RESEARCH_TITLE not in html or 'id="flowview"' not in html:
        raise ValueError("Expected the Higgsfield CLI flow page, including its diagram")


def check_site(directory):
    for name in ("index.html", "404.html", "docs/index.html", "skills/index.html"):
        if not (directory / name).is_file():
            raise ValueError(f"Missing publish artifact: {name}")
    docs = (directory / "docs/index.html").read_text(encoding="utf-8")
    if f'href="../{RESEARCH_ROUTE}#overview"' not in docs:
        raise ValueError("The research index does not link to the Higgsfield overview")
    check_research_page((directory / RESEARCH_ROUTE / "index.html").read_text(encoding="utf-8"))


def check_live(origin):
    url = urljoin(origin.rstrip("/") + "/", RESEARCH_ROUTE)
    request = Request(url, headers={"Cache-Control": "no-cache", "User-Agent": "video-ai-landscape publish check"})
    with urlopen(request, timeout=20) as response:
        if response.status != 200:
            raise ValueError(f"Expected HTTP 200, got {response.status}: {url}")
        if response.headers.get_content_type() != "text/html":
            raise ValueError(f"Expected HTML at {url}")
        check_research_page(response.read().decode("utf-8"))
    print(f"Public research page verified: {url}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", type=Path, default=ROOT / "site", help="Static publish directory")
    parser.add_argument("--live", metavar="ORIGIN", help="Also verify the public research page")
    args = parser.parse_args()
    try:
        check_site(args.site)
        print(f"Publish artifacts verified: {args.site}")
        if args.live:
            check_live(args.live)
    except (OSError, ValueError) as error:
        print(error, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
