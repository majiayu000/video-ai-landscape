#!/usr/bin/env python3
"""Render docs/REPORT-*.md into a styled single-page report site.

Usage: uv run --with markdown python build_report_site.py
Outputs: site/report/index.html (and a copy at REPORT.html for local reading).
"""
import re
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent
SRC = sorted((ROOT / "docs").glob("REPORT-*.md"))[-1]  # latest report by name
OUT_SITE = ROOT / "site" / "report" / "index.html"
OUT_ROOT = ROOT / "REPORT.html"

md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists"])
body = md.convert(SRC.read_text())

# Assign stable ids to h1/h2 (python-markdown slugify drops CJK) and collect TOC.
count = 0
toc = []  # (level, id, text)
def tag_heading(m):
    global count
    count += 1
    level, inner = m.group(1), m.group(2)
    text = re.sub(r"<[^>]+>", "", inner)
    hid = f"sec-{count}"
    toc.append((int(level), hid, text))
    return f'<h{level} id="{hid}">{inner}</h{level}>'

body = re.sub(r"<h([12])>(.*?)</h\1>", tag_heading, body, flags=re.S)

toc_html_items = []
for level, hid, text in toc:
    cls = "lv1" if level == 1 else "lv2"
    toc_html_items.append(f'<a class="{cls}" href="#{hid}">{text}</a>')
toc_html = "\n".join(toc_html_items)

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
  html { scroll-behavior:smooth; scroll-padding-top:64px; }
  body { margin:0; background:var(--page); color:var(--ink); line-height:1.75; font-size:15px;
    font-family:system-ui,-apple-system,"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif; }
  .topbar { position:sticky; top:0; z-index:20; display:flex; gap:16px; align-items:center;
    padding:10px 24px; background:color-mix(in srgb, var(--page) 88%, transparent);
    backdrop-filter:blur(8px); border-bottom:1px solid var(--grid); font-size:13px; }
  .topbar a { color:var(--ink2); text-decoration:none; } .topbar a:hover { color:var(--accent); }
  .topbar .crumb { color:var(--muted); }
  .topbar .title { font-weight:700; color:var(--ink); }
  .topbar button { margin-left:auto; border:1px solid var(--border); background:var(--surface);
    color:var(--ink2); border-radius:8px; padding:5px 11px; font-size:12.5px; cursor:pointer; }
  .layout { display:flex; max-width:1200px; margin:0 auto; gap:32px; padding:0 24px; align-items:flex-start; }
  nav.toc { position:sticky; top:64px; width:250px; flex:none; max-height:calc(100vh - 88px);
    overflow-y:auto; padding:28px 0 40px; font-size:13px; }
  nav.toc .toc-head { font-size:11px; letter-spacing:.12em; color:var(--muted);
    text-transform:uppercase; margin-bottom:10px; }
  nav.toc a { display:block; color:var(--ink2); text-decoration:none; padding:4px 10px;
    border-left:2px solid transparent; border-radius:0 8px 8px 0; line-height:1.5; }
  nav.toc a.lv1 { font-weight:700; color:var(--ink); margin-top:8px; }
  nav.toc a.lv2 { padding-left:22px; font-size:12.5px; color:var(--ink2); }
  nav.toc a:hover { color:var(--accent); background:var(--surface); }
  nav.toc a.active { border-left-color:var(--accent); color:var(--accent); background:var(--surface); }
  main { flex:1; min-width:0; max-width:880px; padding:32px 0 90px; }
  .hero { background:var(--surface); border:1px solid var(--border); border-radius:12px;
    padding:18px 22px; margin-bottom:30px; font-size:13.5px; color:var(--ink2); }
  .hero b { color:var(--ink); }
  .md h1 { font-size:27px; line-height:1.3; margin:52px 0 16px; padding-top:8px; }
  .md h1:first-child { margin-top:4px; }
  .md h2 { font-size:20px; margin:38px 0 12px; padding-bottom:6px; border-bottom:1px solid var(--grid); }
  .md h3 { font-size:16.5px; margin:26px 0 8px; }
  .md a { color:var(--accent); }
  .md code { font-family:ui-monospace,"SF Mono",Menlo,Consolas,monospace; font-size:12.5px;
    background:var(--code-bg); padding:1.5px 6px; border-radius:5px; }
  .md pre { background:var(--surface); border:1px solid var(--border); border-radius:10px;
    padding:14px 16px; overflow-x:auto; line-height:1.55; }
  .md pre code { background:none; padding:0; font-size:12.5px; white-space:pre; }
  .md blockquote { margin:14px 0; padding:2px 18px; border-left:3px solid var(--accent);
    background:var(--surface); border-radius:0 10px 10px 0; color:var(--ink2); }
  .md table { border-collapse:collapse; width:100%; font-size:13.5px; margin:14px 0; display:block; overflow-x:auto; }
  .md th, .md td { border:1px solid var(--grid); padding:8px 12px; text-align:left; vertical-align:top; }
  .md th { background:var(--code-bg); font-size:12px; white-space:nowrap; }
  .md tbody tr:nth-child(even) { background:color-mix(in srgb, var(--surface) 60%, transparent); }
  .md hr { border:none; border-top:1px solid var(--grid); margin:34px 0; }
  .md ul { padding-left:1.3em; } .md li { margin:3px 0; }
  #top-btn { position:fixed; right:22px; bottom:22px; z-index:30; display:none; width:38px; height:38px;
    border-radius:10px; border:1px solid var(--border); background:var(--surface); color:var(--ink2);
    font-size:16px; cursor:pointer; }
  #top-btn:hover { color:var(--accent); }
  footer { max-width:880px; margin:0 auto; padding:0 24px 60px; font-size:12px; color:var(--muted); }
  @media (max-width: 900px) { nav.toc { display:none; } }
  @media print {
    .topbar, nav.toc, #top-btn { display:none !important; }
    body { font-size:11pt; background:#fff; color:#000; }
    .layout { display:block; padding:0; max-width:100%; }
    main { padding:0; max-width:100%; }
    .md h1, .md h2 { page-break-after:avoid; } .md table, .md pre { page-break-inside:avoid; }
  }
"""

JS = """
function t(){const r=document.documentElement;const d=r.dataset.theme==='dark'||(!r.dataset.theme&&matchMedia('(prefers-color-scheme: dark)').matches);r.dataset.theme=d?'light':'dark';}
const btn=document.getElementById('top-btn');
addEventListener('scroll',()=>{btn.style.display=scrollY>600?'block':'none';},{passive:true});
btn.onclick=()=>scrollTo({top:0,behavior:'smooth'});
// scroll-spy: highlight current section in TOC
const links=[...document.querySelectorAll('nav.toc a')];
const targets=links.map(a=>document.getElementById(a.getAttribute('href').slice(1))).filter(Boolean);
const io=new IntersectionObserver(es=>{es.forEach(e=>{if(e.isIntersecting){
  links.forEach(l=>l.classList.toggle('active',l.getAttribute('href')==='#'+e.target.id));}});},
  {rootMargin:'-64px 0px -70% 0px'});
targets.forEach(el=>io.observe(el));
"""

page = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>视频 AI 生态全域调研与战略 · 完整报告</title>
<style>{CSS}</style>
</head>
<body>
<header class="topbar">
  <a href="/">← 对比报告</a><span class="crumb">/</span>
  <span class="title">完整报告</span>
  <button onclick="t()">🌗 主题</button>
</header>
<div class="layout">
  <nav class="toc">
    <div class="toc-head">目录</div>
    {toc_html}
  </nav>
  <main>
    <div class="hero">
      <b>35 路 schema 约束真实网络调研（4 轮）+ 35 个历史案例提炼 33 条定律</b>。<br>
      配套：机器可读数据 <code>data/</code>（价格 34 条 / 能力矩阵 13 条，as_of 2026-09-22）·
      逐路原始发现 <code>docs/research-*.md</code> × 5。<br>
      置信度：官方源 &gt; 多源交叉 &gt; 单一来源 &gt; 推断；商业数字未经审计。
    </div>
    <div class="md">
{body}
    </div>
  </main>
</div>
<footer>生成于 2026-09-23 · 方法论与来源声明见报告第七部分 · 窗口判断行动前 24h 需一手复核</footer>
<button id="top-btn" title="回到顶部">↑</button>
<script>{JS}</script>
</body>
</html>"""

OUT_SITE.parent.mkdir(parents=True, exist_ok=True)
OUT_SITE.write_text(page)
OUT_ROOT.write_text(page)
print(f"source: {SRC.name}")
print(f"toc entries: {len(toc)}")
print(f"written: {OUT_SITE} ({OUT_SITE.stat().st_size} bytes)")
print(f"written: {OUT_ROOT} ({OUT_ROOT.stat().st_size} bytes)")
