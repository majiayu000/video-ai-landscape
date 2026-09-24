#!/usr/bin/env python3
"""Render research docs from docs/ into site/docs/ for the report site.

Reuses the CSS/page template from build_skills_site.py.

Usage: uv run --with markdown python gen_docs.py
"""
import html as htmllib
import shutil
from pathlib import Path

from build_skills_site import CSS, JS, render_md, write

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "site" / "docs"

# 公开调研文档白名单（内部战略/执行文档不上站）: (文件名, 展示标题)
DOCS = [
    ("higgsfield-skill-anatomy-2026-09-24.md", "Higgsfield Skills 完整解剖"),
    ("higgsfield-ecosystem-assessment-2026-09-24.md", "Higgsfield 生态与效果评估"),
    ("higgsfield-prompt-enhancer-finding-2026-09-24.md", "PromptEnhancer：CLI 效果依赖调研"),
    ("research-deep-dive-2-2026-09-22.md", "深度调研 · 第二轮"),
    ("research-ecosystem-expansion-2026-09-22.md", "生态扩展调研"),
    ("research-round3-2026-09-22.md", "调研 · 第三轮"),
    ("research-round4-strategy-2026-09-23.md", "调研 · 第四轮：厂商策略"),
    ("research-vendor-next-moves-2026-09-22.md", "厂商下一步动作研判"),
]


def doc_page(title, crumb_file, body):
    crumb = (f'<a href="/">← 全景报告</a><span class="crumb">/</span>'
             f'<a href="/docs/">研究文档</a>'
             f'<span class="crumb">/</span><span class="crumb">{htmllib.escape(crumb_file)}</span>')
    return f"""<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{htmllib.escape(title)}</title><style>{CSS}</style></head>
<body><nav class="topbar">{crumb}<button onclick="t()">🌓</button></nav>
<main class="md">{body}</main>
<footer>AI 视频厂商 CLI / Skill / MCP 全景对比 · 研究文档 · <a href="/" style="color:var(--muted)">返回报告</a></footer>
<script>{JS}</script></body></html>"""


def build():
    if OUT.exists():
        shutil.rmtree(OUT)
    items = []
    for fname, title in DOCS:
        src = ROOT / "docs" / fname
        if not src.exists():
            print(f"SKIP (missing): {fname}")
            continue
        _, body_html = render_md(src.read_text(encoding="utf-8"))
        slug = fname.removesuffix(".md")
        write(OUT / f"{slug}.html", doc_page(title, fname, body_html))
        date = slug.rsplit("-", 1)[-1] if slug[-8:].replace("-", "").isdigit() else ""
        items.append((slug, title, date, fname))
        print(f"OK: {fname} -> /docs/{slug}.html")

    cards = "".join(
        f'<div class="card" style="flex:1 1 280px;border:1px solid var(--border);border-radius:12px;'
        f'padding:16px 18px;background:var(--surface)">'
        f'<h4 style="margin:0 0 6px;font-size:14.5px"><a href="{slug}.html" style="color:var(--ink);text-decoration:none">'
        f'{htmllib.escape(title)}</a></h4>'
        f'<div style="font-size:12px;color:var(--muted)">{date} · docs/{fname}</div></div>'
        for slug, title, date, fname in items)
    intro = ('<div class="meta"><div class="m-name">研究文档</div>'
             '<div class="m-desc">全景报告之外的过程性调研与厂商拆解：调研轮次记录、'
             'Higgsfield 技能解剖与生态评估、PromptEnhancer 服务端依赖发现等。'
             '内部战略与执行文档不在本站公开。</div></div>')
    write(OUT / "index.html", doc_page("研究文档 · 视频厂商调研", "", intro + f'<div class="cards" style="display:flex;flex-wrap:wrap;gap:14px">{cards}</div>'))
    print(f"OK: {len(items)} docs + index -> {OUT}")


if __name__ == "__main__":
    build()
