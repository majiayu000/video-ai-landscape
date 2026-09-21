#!/usr/bin/env python3
"""Generate the appendix section (all SKILL.md, grouped by repo) into index.html.

Usage: uv run --with markdown python gen_appendix.py
"""
import html as htmllib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INDEX = ROOT / "index.html"

REPOS = {
    "higgsfield-skills": "Higgsfield 官方",
    "runwayml-skills": "Runway 官方",
    "runway-mcp-plugin": "Runway MCP 插件",
    "atlascloud-skills": "AtlasCloud 官方",
    "fal-community-skills": "fal 社区",
    "elevenlabs-plugin": "ElevenLabs 插件",
    "anthropics-skills": "Anthropic 官方参照",
}


def split_fm(text):
    if text.startswith("---"):
        m = re.match(r"^---\s*\n(.*?)\n---\s*\n?", text, re.S)
        if m:
            return m.group(1), text[m.end():]
    return "", text


def fm_field(fm, key):
    m = re.search(rf"^{key}:\s*(.+?)?(?=\n[\w-]+:|\Z)", fm + "\n\x00", re.S | re.M)
    if not m:
        return ""
    val = (m.group(1) or "").strip()
    if val in ("|", ">", "|-", ">-", "|+", ">+"):
        rest = fm[m.end():].split("\n\x00")[0]
        lines = [ln.strip() for ln in rest.splitlines() if ln.strip() and not re.match(r"^[\w-]+:", ln)]
        val = " ".join(lines)
    else:
        val = val.strip("\"'")
    return re.sub(r"\s+", " ", val).strip()


def build_section():
    total = 0
    parts = ['<section id="appendix">',
             '  <h2><span class="no">A</span>附录 · 技能全清单</h2>',
             '  <p class="section-sub">7 个仓库里全部 <b>103 个 SKILL.md</b>，按厂商分组，点名称直达在线渲染页。</p>']
    for repo, label in REPOS.items():
        rows = []
        for f in sorted((ROOT / repo).rglob("SKILL.md")):
            if ".git" in f.parts:
                continue
            fm, _ = split_fm(f.read_text(encoding="utf-8", errors="replace"))
            name, desc = fm_field(fm, "name"), fm_field(fm, "description")
            rel = f.relative_to(ROOT / repo).as_posix()
            url = f"skills/{repo}/{Path(rel).with_suffix('.html').as_posix()}"
            disp = htmllib.escape(name or Path(rel).parent.name)
            if len(desc) > 100:
                desc = desc[:100] + "…"
            path_sub = htmllib.escape(rel)
            rows.append(f'<tr><td><code><a class="code-link" href="{url}">{disp}</a></code>'
                        f'<span class="sub">{path_sub}</span></td>'
                        f'<td>{htmllib.escape(desc)}</td></tr>')
        total += len(rows)
        parts.append(f'  <h3>{htmllib.escape(label)} <span style="color:var(--muted);font-weight:400;font-size:13px">· {len(rows)} 个</span></h3>')
        parts.append('  <div class="tbl-scroll"><table>')
        parts.append('  <tr><th>技能</th><th>描述</th></tr>\n  ' + "\n  ".join(rows))
        parts.append('  </table></div>')
    parts.append("</section>")
    assert total == 103, f"expected 103 SKILL.md, got {total}"
    return "\n".join(parts)


def main():
    section = build_section()
    html_text = INDEX.read_text(encoding="utf-8")
    assert html_text.count("<footer>") == 1, "expected exactly one <footer>"
    # idempotent: strip a previously generated appendix before inserting
    html_text = re.sub(r'<section id="appendix">.*?</section>\n*', "", html_text, flags=re.S)
    INDEX.write_text(html_text.replace("<footer>", section + "\n\n<footer>"), encoding="utf-8")
    print(f"OK: appendix with 103 skills inserted into {INDEX}")


if __name__ == "__main__":
    main()
