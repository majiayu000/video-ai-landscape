# AI 视频厂商 CLI / Skill / MCP 全景对比

16 家视频生成厂商的 agent 接入面（CLI / Agent Skills / MCP）调研报告 + 本地技能库镜像 + 在线阅读站点。

- **线上报告**: https://video-vendor-skills.pages.dev
- **技能库（466 篇在线渲染）**: https://video-vendor-skills.pages.dev/skills/
- **研究文档**: https://video-vendor-skills.pages.dev/docs/
- **Higgsfield CLI 运行时流程图（2026-10-13）**: [打开独立 HTML](site/research/higgsfield-cli-flow/index.html#overview) · 9 条流程、66 条命令中文说明、105 个模型与 22 个 workflow 参数快照
- **视频技能研究摘要**: https://video-vendor-skills.pages.dev/docs/skills-construction-2026-09-25.html

## 按任务阅读

[接入选择与恢复阅读路线](https://video-vendor-skills.pages.dev/docs/skills-construction-2026-09-25)解释 CLI / Skill / MCP 的入口差别，连接 Runway、Higgsfield、fal community 与 Atlas 的现有技能快照及当前上游资料，并区分等待超时、缺少文件与受理未知。本站提供调研材料，不提供新的统一生成或恢复服务。

材料与镜像的版本固定在 `setup.sh`；查看当前能力时请回到各厂商上游。报告断链和来源错误可在[项目 Issues](https://github.com/majiayu000/video-ai-landscape/issues)提供公开证据，账号和计费问题走相应厂商支持。

## 结构

```
index.html            # 主报告（11 节 + 附录：103 个 SKILL.md 全清单）
site/                 # 部署目录 = index.html + skills/ + docs/ + report/ + research/
docs/skills-research-public-2026-09-25.md  # 可公开的技能研究摘要
build_research_summary_page.py  # 将研究摘要渲染为 site/docs/ 页面
build_skills_site.py  # 把 7 个仓库的全部 .md 渲染为 site/skills/*.html
gen_appendix.py       # 从 7 个仓库提取 103 个 SKILL.md，生成主报告附录章节
setup.sh              # 按 pinned SHA 重建 7 个厂商仓库的调研快照（不入库，见 .gitignore）
```

## 重建流程

```bash
./setup.sh                                            # 1. 克隆 7 个仓库（固定 SHA）
uv run --with markdown python build_skills_site.py    # 2. 渲染技能库 → site/skills/
uv run --with markdown python gen_appendix.py         # 3. 生成附录 → index.html
uv run --with markdown python build_research_summary_page.py  # 4. 渲染研究摘要 → site/docs/
cp index.html site/
```

## Higgsfield CLI 运行时流程图

[`site/research/higgsfield-cli-flow/index.html`](site/research/higgsfield-cli-flow/index.html#overview) 是独立静态专题，默认打开总览；下载 HTML 后也可离线浏览。点击节点可查看对应命令与依据，支持命令搜索、参数检索、缩放、SVG 导出与打印。原始帮助、Skill 摘录、参数契约和覆盖矩阵内嵌在页面中，可在证据弹窗下载，无需本机文件或外部服务。

这是 2026-10-13 的 CLI v1.1.26 / Skills 0.13.0 快照，并非实时能力目录；写操作未逐条实跑。旧视频示例保留原始 prompt 与 enhanced_prompt，公开版隐去了任务 ID、账号标识及成品链接。此专题单独存放在 `site/research/`，重建技能库或文档不会删除它；`gen_docs.py` 保留研究文档首页的入口。

GitHub 中的 HTML 以源码展示；下载后用浏览器打开。部署 `site/` 后访问 `/research/higgsfield-cli-flow/#overview`。设计参考：[Claude Code 运行时流程图](https://blog.silencestar.com/posts/claude-code-agent-internals/#runtime)。

## 部署（Cloudflare Pages 直传）

部署目录必须保留顶层 `site/404.html`，让不存在的地址返回 404；缺少该文件时，Pages 会将错误路径回退到首页。首页和附录的站内链接使用 `/docs/`、`/skills/` 等根路径，避免嵌套路径下重复拼接。

```bash
cp index.html site/
~/.bun/bin/wrangler pages deploy site --project-name=video-vendor-skills --branch=main --commit-dirty=true
```

## 全文搜索

技能库首页与报告附录带搜索框，基于 [pagefind](https://pagefind.app/) 静态索引。重建站点后跑一次：

```bash
npx -y pagefind --site site
```

## 自动更新（CI）

`.github/workflows/refresh.yml` 每周一检查 7 个厂商仓库上游是否有新提交：有则把 `setup.sh` 的 pinned SHA 前移、重建站点、自动提交；若配置了 `CLOUDFLARE_API_TOKEN` + `CLOUDFLARE_ACCOUNT_ID` 两个 Actions secret 还会自动部署。可在 Actions 页手动触发（可勾选强制重建）。

## 快照信息

调研日期 2026-09-21。7 个仓库的克隆 SHA 固定在 `setup.sh`，厂商后续更新不影响本报告的可复现性。

厂商商业对比，以及阿特拉斯技能、命令行、MCP 的做法，写在 [`docs/atlas-ecosystem-plan.md`](docs/atlas-ecosystem-plan.md)。
