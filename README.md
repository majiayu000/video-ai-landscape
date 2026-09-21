# AI 视频厂商 CLI / Skill / MCP 全景对比

16 家视频生成厂商的 agent 接入面（CLI / Agent Skills / MCP）调研报告 + 本地技能库镜像 + 在线阅读站点。

- **线上报告**: https://video-vendor-skills.pages.dev
- **技能库（466 篇在线渲染）**: https://video-vendor-skills.pages.dev/skills/

## 结构

```
index.html            # 主报告（11 节 + 附录：103 个 SKILL.md 全清单）
site/                 # 部署目录 = index.html + skills/（build 脚本渲染产物，474 页）
build_skills_site.py  # 把 7 个仓库的全部 .md 渲染为 site/skills/*.html
gen_appendix.py       # 从 7 个仓库提取 103 个 SKILL.md，生成主报告附录章节
setup.sh              # 按 pinned SHA 重建 7 个厂商仓库的调研快照（不入库，见 .gitignore）
```

## 重建流程

```bash
./setup.sh                                            # 1. 克隆 7 个仓库（固定 SHA）
uv run --with markdown python build_skills_site.py    # 2. 渲染技能库 → site/skills/
uv run --with markdown python gen_appendix.py         # 3. 生成附录 → index.html
```

## 部署（Cloudflare Pages 直传）

```bash
cp index.html site/
~/.bun/bin/wrangler pages deploy site --project-name=video-vendor-skills --branch=main --commit-dirty=true
```

## 快照信息

调研日期 2026-09-21。7 个仓库的克隆 SHA 固定在 `setup.sh`，厂商后续更新不影响本报告的可复现性。
