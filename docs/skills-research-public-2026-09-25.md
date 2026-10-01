# 视频生成 Agent Skills：研究摘要

> 调研快照：2026-09-24。安装量、价格和产品能力会变化，请以厂商当前文档为准。

## 研究范围

本次研究比较了视频生成厂商的 CLI、Agent Skills 和 MCP 接入方式，并阅读了七个公开技能仓库的文档。技能原文可在[在线技能库](/skills/)中查看。

## 可复用的发现

- 成熟的技能仓库通常把简短的执行指令放在 `SKILL.md`，把模型参数、故障排查和示例放在按需读取的参考文件中。
- 技能描述应说明适用场景、与其他技能的配合方式，以及不适用的边界。版本、引用文件和基本格式可以通过自动检查保持一致。
- 长时间运行的生成任务需要明确区分提交成功、仍在处理、超时和失败；成本与产物有效期也应在调用前后清楚呈现。
- 提示词增强的实现因技能而异。部分图像工作流依赖服务端模板；调研时所见的视频生成路径主要由技能引导 Agent 直接编写提示词。这个结论仅适用于所检查的版本。

## 想接入视频生成，先选哪条阅读路线？

CLI 是命令行调用入口，Skill 是 Agent 在适用任务时读取的执行说明，MCP 则把工具暴露给支持协议的宿主。厂商可能同时提供三种入口，不能只看到仓库里有 `SKILL.md` 就认定已经安装了 CLI 或接通了账户。Higgsfield 的[当前官方接入说明](https://higgsfield.ai/creator-hub/help-center/integrations/how-do-i-access-higgsfield-via-cli)分别说明 CLI/Skills 与 MCP；具体安装、认证和能力仍按各厂商现行文档执行。

| 你现在要解决的事 | 从本站哪里开始 | 接着核对什么 |
|---|---|---|
| 为 coding agent 找视频技能 | [技能库总索引](/skills/)，按厂商或关键词检索 | 打开 `SKILL.md` 与它引用的 reference；确认适用任务、依赖与授权步骤 |
| 了解 Runway 的 Agent 接入 | [Runway 技能快照](/skills/runwayml-skills/) | 对照 [runwayml/skills 当前仓库](https://github.com/runwayml/skills)，以现行配置与账户可用性为准 |
| 了解 Higgsfield 的技能结构 | [Higgsfield 完整解剖](higgsfield-skill-anatomy-2026-09-24)与[技能镜像](/skills/higgsfield-skills/) | 区分执行说明、参数参考和服务端依赖，不把提示词层当作全部运行逻辑 |
| 找 fal 的相关生成技能 | [fal community 技能快照](/skills/fal-community-skills/) | 查看 [fal-ai-community/skills 当前仓库](https://github.com/fal-ai-community/skills)；保留 community 的来源身份 |
| 学 Atlas 的提交、续查与文件验收 | [Atlas 技能快照](/skills/atlascloud-skills/)与[独立中文教程](https://majiayu000.github.io/atlas-tutorials/) | 从教程的来源版本开始；没有真实账户测试的示例不作为模型效果证据 |

这几条路线提供可读材料和来源选择，不是厂商质量、价格或成功率排名。需要跨厂商业务比较时，回到[全景报告](/)，同时核对报告日期和当前官方说明。

## 已经提交了任务，超时或没有文件怎么办？

先区分提交、远程处理与本地保存。已有任务 ID 时，回到对应厂商技能的查询/等待说明，核对原任务；不要因本地等待超时就自动重新生成。远程显示完成但本地没有文件时，核对输出 URL、下载结果与文件格式；再次提交不是下载修复。连 ID 都没有时，保留原回执和发生时间，按厂商提供的历史或支持渠道确认是否受理，仍未知就明确写未知。

本站没有统一的跨厂商恢复命令，也不能证明服务端幂等或硬预算已经存在。请分别阅读原技能的状态语义、计费边界、输出有效期与失败处理。把某个厂商的命令复制到另一家，可能产生新任务或根本无法查询。

## 镜像、当前版本与反馈

此页的研究结论仍冻结在 2026-09-24；上面的任务入口补充于 2026-10-01。镜像版本固定在[公开 setup.sh](https://github.com/majiayu000/video-ai-landscape/blob/main/setup.sh)，可复现报告所读的材料，但不保证是上游最新状态。原始仓库、许可证与署名仍归各自权利人；本站不授予第三方素材或技能的新许可。

报告来源错误或断链可向[本项目 Issues](https://github.com/majiayu000/video-ai-landscape/issues)提供页面地址、厂商、快照版本与公开来源。产品安装、付款或账号问题应走厂商自身支持入口，不提交密钥、账户回执或客户素材。

## 进一步阅读

- [Higgsfield 技能结构与执行方式](higgsfield-skill-anatomy-2026-09-24)
- [Higgsfield 生态与效果评估](higgsfield-ecosystem-assessment-2026-09-24)
- [PromptEnhancer 调用路径调查](higgsfield-prompt-enhancer-finding-2026-09-24)
