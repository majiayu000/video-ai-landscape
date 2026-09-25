#!/usr/bin/env python3
"""Render the public skills research summary into site/docs/."""

from html import escape
from pathlib import Path

import markdown


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "docs" / "skills-research-public-2026-09-25.md"
DOCS = ROOT / "site" / "docs"
OUTPUT = DOCS / "skills-construction-2026-09-25.html"
TEMPLATE = DOCS / "higgsfield-skill-anatomy-2026-09-24.html"
TITLE = "视频生成 Agent Skills · 研究摘要"


def main() -> None:
    template = TEMPLATE.read_text()
    before_main, rest = template.split('<main class="md">', 1)
    _, after_main = rest.split("</main>", 1)
    before_main = before_main.replace(
        "<title>Higgsfield Skills 完整解剖</title>",
        f"<title>{escape(TITLE)}</title>",
    ).replace(
        "higgsfield-skill-anatomy-2026-09-24.md",
        TITLE,
    )
    body = markdown.markdown(
        SOURCE.read_text(),
        extensions=["tables", "fenced_code", "sane_lists"],
    )
    OUTPUT.write_text(before_main + '<main class="md">' + body + "</main>" + after_main)

if __name__ == "__main__":
    main()
