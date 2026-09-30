#!/usr/bin/env python3
"""Render the public skills research summary into site/docs/."""

from html import escape
from pathlib import Path
import re

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
    before_main = re.sub(r'<meta\b[^>]*(?:name="(?:description|twitter:[^"]*)"|property="og:[^"]*")[^>]*>\s*', '', before_main)
    before_main = re.sub(r'<link\b[^>]*rel="canonical"[^>]*>\s*', '', before_main)
    head = """<meta name="description" content="视频生成 Agent Skills 的结构、执行契约、参考层、验证与恢复机制研究摘要，保留来源和结论边界。">
<link rel="canonical" href="https://video-vendor-skills.pages.dev/docs/skills-construction-2026-09-25.html">
<meta property="og:type" content="website">
<meta property="og:title" content="视频生成 Agent Skills · 研究摘要">
<meta property="og:description" content="视频生成 Agent Skills 的结构、执行契约、参考层、验证与恢复机制研究摘要，保留来源和结论边界。">
<meta property="og:url" content="https://video-vendor-skills.pages.dev/docs/skills-construction-2026-09-25.html">
<meta property="og:image" content="https://video-vendor-skills.pages.dev/social-card.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="AI 视频厂商 CLI / Skill / MCP · 报告首页预览">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="视频生成 Agent Skills · 研究摘要">
<meta name="twitter:description" content="视频生成 Agent Skills 的结构、执行契约、参考层、验证与恢复机制研究摘要，保留来源和结论边界。">
<meta name="twitter:image" content="https://video-vendor-skills.pages.dev/social-card.png">"""
    before_main = before_main.replace("</head>", head + "</head>", 1)
    body = markdown.markdown(
        SOURCE.read_text(),
        extensions=["tables", "fenced_code", "sane_lists"],
    )
    OUTPUT.write_text(before_main + '<main class="md">' + body + "</main>" + after_main)

if __name__ == "__main__":
    main()
