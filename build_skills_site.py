#!/usr/bin/env python3
"""Render every markdown doc from the 7 cloned vendor skill repos into site/skills/.

Usage: uv run --with markdown python build_skills_site.py
"""
import html as htmllib
import re
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "site" / "skills"

REPOS = {
    "higgsfield-skills": ("higgsfield-ai/skills", "Higgsfield 官方 Skills"),
    "runwayml-skills": ("runwayml/skills", "Runway 官方 Skills"),
    "runway-mcp-plugin": ("runwayml/runway-mcp-plugin", "Runway MCP 插件"),
    "atlascloud-skills": ("AtlasCloudAI/atlas-cloud-skills", "AtlasCloud 官方 Skills"),
    "fal-community-skills": ("fal-ai-community/skills", "fal 社区 Skills"),
    "elevenlabs-plugin": ("elevenlabs/plugin", "ElevenLabs 插件"),
    "anthropics-skills": ("anthropics/skills", "Anthropic 官方参照"),
}

md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists"])

CSS = """
  :root { color-scheme: light; --page:#f9f9f7; --surface:#fcfcfb; --ink:#0b0b0b;
    --ink2:#52514e; --muted:#898781; --grid:#e1e0d9; --border:rgba(11,11,11,.10);
    --accent:#2a78d6; --code-bg:rgba(11,11,11,.05); }
  :root:where(:not([data-theme="light"])) { @media (prefers-color-scheme: dark) {
    color-scheme: dark; --page:#0d0d0d; --surface:#1a1a19; --ink:#fff; --ink2:#c3c2b7;
    --grid:#2c2c2a; --border:rgba(255,255,255,.10); --accent:#3987e5; --code-bg:rgba(255,255,255,.07); } }
  :root[data-theme="dark"] { color-scheme: dark; --page:#0d0d0d; --surface:#1a1a19;
    --ink:#fff; --ink2:#c3c2b7; --grid:#2c2c2a; --border:rgba(255,255,255,.10);
    --accent:#3987e5; --code-bg:rgba(255,255,255,.07); }
  * { box-sizing:border-box; }
  body { margin:0; background:var(--page); color:var(--ink); line-height:1.7; font-size:15px;
    font-family:system-ui,-apple-system,"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif; }
  .topbar { position:sticky; top:0; z-index:10; display:flex; gap:16px; align-items:center;
    padding:10px 24px; background:color-mix(in srgb, var(--page) 88%, transparent);
    backdrop-filter:blur(8px); border-bottom:1px solid var(--grid); font-size:13px; }
  .topbar a { color:var(--ink2); text-decoration:none; } .topbar a:hover { color:var(--accent); }
  .topbar .crumb { color:var(--muted); }
  .topbar button { margin-left:auto; border:1px solid var(--border); background:var(--surface);
    color:var(--ink2); border-radius:8px; padding:5px 11px; font-size:12.5px; cursor:pointer; }
  main { max-width:880px; margin:0 auto; padding:36px 24px 90px; }
  .meta { background:var(--surface); border:1px solid var(--border); border-radius:12px;
    padding:16px 20px; margin-bottom:28px; font-size:13.5px; }
  .meta .m-name { font-weight:700; font-size:15px; margin-bottom:4px; }
  .meta .m-tag { display:inline-block; font-size:11px; color:var(--accent); border:1px solid
    color-mix(in srgb, var(--accent) 35%, transparent); border-radius:999px; padding:1px 9px; margin-left:8px; vertical-align:2px; }
  .meta .m-desc { color:var(--ink2); white-space:pre-line; }
  .meta .m-src { margin-top:8px; font-size:12px; color:var(--muted); }
  .meta .m-src a { color:var(--muted); }
  .md h1 { font-size:26px; line-height:1.3; margin:10px 0 16px; }
  .md h2 { font-size:19px; margin:34px 0 10px; padding-bottom:6px; border-bottom:1px solid var(--grid); }
  .md h3 { font-size:16px; margin:24px 0 8px; }
  .md p, .md li { color:var(--ink); }
  .md a { color:var(--accent); }
  .md code { font-family:ui-monospace,"SF Mono",Menlo,Consolas,monospace; font-size:12.5px;
    background:var(--code-bg); padding:1.5px 6px; border-radius:5px; }
  .md pre { background:var(--surface); border:1px solid var(--border); border-radius:10px;
    padding:14px 16px; overflow-x:auto; line-height:1.55; }
  .md pre code { background:none; padding:0; font-size:12.5px; white-space:pre; }
  .md blockquote { margin:14px 0; padding:2px 18px; border-left:3px solid var(--accent);
    background:var(--surface); border-radius:0 10px 10px 0; color:var(--ink2); }
  .md table { border-collapse:collapse; width:100%; font-size:13.5px; margin:14px 0; display:block; overflow-x:auto; }
  .md th, .md td { border:1px solid var(--grid); padding:7px 12px; text-align:left; vertical-align:top; }
  .md th { background:var(--code-bg); font-size:12px; }
  .md hr { border:none; border-top:1px solid var(--grid); margin:30px 0; }
  .md img { max-width:100%; }
  h2.list-head { font-size:17px; margin:30px 0 12px; border:none; }
  .filelist { list-style:none; padding:0; margin:0; }
  .filelist li { background:var(--surface); border:1px solid var(--border); border-radius:10px;
    padding:13px 17px; margin-bottom:8px; }
  .filelist a { color:var(--accent); text-decoration:none; font-weight:600; font-size:14px; }
  .filelist a:hover { text-decoration:underline; }
  .filelist .d { display:block; color:var(--ink2); font-size:12.5px; margin-top:3px; }
  .filelist .plain a { color:var(--ink2); font-weight:500; }
  .cards { display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:12px; }
  .card { background:var(--surface); border:1px solid var(--border); border-radius:12px; padding:18px 20px; }
  .card h3 { margin:0 0 2px; font-size:15px; }
  .card .gh { font-size:12px; color:var(--muted); margin-bottom:8px; }
  .card .gh a { color:var(--muted); }
  .card p { font-size:13px; color:var(--ink2); margin:0 0 10px; }
  .card a.go { display:inline-block; font-size:13px; color:var(--accent); text-decoration:none; font-weight:600; }
  footer { max-width:880px; margin:0 auto; padding:0 24px 60px; font-size:12px; color:var(--muted); }
"""

JS = "function t(){const r=document.documentElement;const d=r.dataset.theme==='dark'||(!r.dataset.theme&&matchMedia('(prefers-color-scheme: dark)').matches);r.dataset.theme=d?'light':'dark';}"


def page(title, crumb_repo, body, meta="", crumb_file=""):
    crumb = f'<a href="/">← 对比报告</a><span class="crumb">/</span><a href="/skills/">技能库</a>'
    if crumb_repo:
        crumb += f'<span class="crumb">/</span><a href="/skills/{crumb_repo}/">{crumb_repo}</a>'
    if crumb_file:
        crumb += f'<span class="crumb">/</span><span class="crumb">{crumb_file}</span>'
    return f"""<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{htmllib.escape(title)}</title><style>{CSS}</style></head>
<body><nav class="topbar">{crumb}<button onclick="t()">🌓</button></nav>
<main>{meta}{body}</main>
<footer>AI 视频厂商 CLI / Skill / MCP 全景对比 · 技能库 · <a href="/" style="color:var(--muted)">返回报告</a></footer>
<script>{JS}</script></body></html>"""


def split_fm(text):
    if text.startswith("---"):
        m = re.match(r"^---\s*\n(.*?)\n---\s*\n?", text, re.S)
        if m:
            return m.group(1), text[m.end():]
    return "", text


def fm_field(fm, key):
    """Extract a (possibly multiline) scalar/block field from YAML frontmatter."""
    m = re.search(rf"^{key}:\s*(.+?)?(?=\n[\w-]+:|\Z)", fm + "\n\x00", re.S | re.M)
    if not m:
        return ""
    val = (m.group(1) or "").strip()
    if val in ("|", ">", "|-", ">-", "|+", ">+"):
        rest = fm[m.end():]
        rest = rest.split("\n\x00")[0]
        lines = [ln.strip() for ln in rest.splitlines() if ln.strip() and not re.match(r"^[\w-]+:", ln)]
        val = " ".join(lines)
    else:
        val = val.strip("\"'")
    return re.sub(r"\s+", " ", val).strip()


def render_md(text):
    fm, body = split_fm(text)
    md.reset()
    html_out = md.convert(body)
    html_out = re.sub(r'(href=")(?!https?://|#)([^"]*?)\.md(#[^"]*)?"',
                      lambda m: f'{m.group(1)}{m.group(2)}.html{m.group(3) or ""}"', html_out)
    return fm, html_out


def meta_card(name, version, desc, repo, relpath):
    slug = REPOS[repo][0]
    gh = f"https://github.com/{slug}/blob/main/{relpath}"
    ver = f'<span class="m-tag">v{htmllib.escape(version)}</span>' if version else ""
    desc_html = f'<div class="m-desc">{htmllib.escape(desc)}</div>' if desc else ""
    return (f'<div class="meta"><div class="m-name">{htmllib.escape(name or Path(relpath).stem)}{ver}</div>'
            f'{desc_html}<div class="m-src">源文件：<a href="{gh}" target="_blank" rel="noopener">{slug}/{relpath}</a></div></div>')


def write(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def build():
    if OUT.exists():
        shutil.rmtree(OUT)
    stats = {}
    for repo, (slug, label) in REPOS.items():
        repo_dir = ROOT / repo
        skill_entries, plain_entries = [], []
        for f in sorted(repo_dir.rglob("*.md")):
            rel = f.relative_to(repo_dir).as_posix()
            if ".git" in f.parts:
                continue
            raw = f.read_text(encoding="utf-8", errors="replace")
            fm, body_html = render_md(raw)
            name, desc, version = fm_field(fm, "name"), fm_field(fm, "description"), fm_field(fm, "version")
            title = name or f.stem
            meta = meta_card(name, version, desc, repo, rel) if name else ""
            out_rel = Path(rel).with_suffix(".html")
            write(OUT / repo / out_rel, page(f"{title} · {label}", repo, body_html, meta, crumb_file=rel))
            if f.name == "SKILL.md":
                skill_entries.append((rel, out_rel.as_posix(), name or f.stem, desc))
            else:
                plain_entries.append((rel, out_rel.as_posix(), title))
        # per-repo index
        has_root_index = (repo_dir / "index.md").exists()
        idx_name = "overview.html" if has_root_index else "index.html"
        items = "".join(
            f'<li><a href="/skills/{repo}/{out}">{htmllib.escape(name)}</a>'
            f'<span class="d">{htmllib.escape(desc[:220])}{"…" if len(desc) > 220 else ""}</span></li>'
            for rel, out, name, desc in skill_entries)
        plains = "".join(
            f'<li class="plain"><a href="/skills/{repo}/{out}">{htmllib.escape(name)}</a>'
            f'<span class="d">{rel}</span></li>'
            for rel, out, name in plain_entries)
        body = (f"<h1>{htmllib.escape(label)}</h1>"
                f'<p style="color:var(--ink2)">{len(skill_entries)} 个 SKILL.md · {len(plain_entries)} 篇参考文档 · '
                f'<a href="https://github.com/{slug}" target="_blank" rel="noopener">GitHub: {slug}</a></p>'
                f"<h2 class='list-head'>技能（SKILL.md）</h2><ul class='filelist'>{items}</ul>")
        if plains:
            body += f"<h2 class='list-head'>参考与说明文档</h2><ul class='filelist'>{plains}</ul>"
        write(OUT / repo / idx_name, page(f"{label} · 技能列表", repo, body))
        stats[repo] = (label, slug, len(skill_entries), len(plain_entries), idx_name)

    # global index
    cards = "".join(
        f'<div class="card"><h3>{htmllib.escape(label)}</h3>'
        f'<div class="gh"><a href="https://github.com/{slug}" target="_blank" rel="noopener">{slug}</a></div>'
        f'<p>{n_skill} 个技能 · {n_doc} 篇参考文档</p>'
        f'<a class="go" href="/skills/{repo}/{idx}">浏览 →</a></div>'
        for repo, (label, slug, n_skill, n_doc, idx) in stats.items())
    body = ("<h1>技能库 · 7 个官方仓库 · 466 篇文档</h1>"
            "<p style=\"color:var(--ink2)\">本地克隆的官方技能仓库全量渲染版，配套"
            "<a href=\"/\">《AI 视频厂商 CLI / Skill / MCP 全景对比》报告</a>阅读。</p>"
            f"<div class='cards'>{cards}</div>")
    write(OUT / "index.html", page("技能库 · 视频厂商官方 Skills", "", body))
    total_s = sum(s[2] for s in stats.values()); total_d = sum(s[3] for s in stats.values())
    print(f"OK: {total_s} SKILL.md + {total_d} docs -> {OUT}")


if __name__ == "__main__":
    build()
