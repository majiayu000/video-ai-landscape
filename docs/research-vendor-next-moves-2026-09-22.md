# 前瞻调研 · 主要厂商近 90 天布局与空位（2026-09-22）

> 方法：5 路 schema 约束 agent 真实网络调研（fal / AtlasCloud / Higgsfield+Runway / 第二梯队 / 开发者需求侧）。
> 规则：以 2026-09-22 为"现在"，只看近 90 天动作 + 未来信号；gaps 为核心产出。
> 原始结构化输出：workflow run wf_30803c52-a09。

---


## fal（含 genmedia-labs 归属鉴定）

近 90 天 fal 的重心完全不在开发者 CLI/skills 面：他们发布了首个第一方视频模型 H3 Max（8-27，主打"5 秒视频 3 秒内出片"）、上线第二个 MCP——Platform MCP（8-17，15 个只读运维调试工具，让 agent 操作你的 fal 账号）、连发 serverless 可观测性/计费/重试更新，同时招聘向企业销售/解决方案/定价运营/基建倾斜。任务中最关键的问题是 genmedia-labs/skills 的归属：经源码级比对确认它不是 fal 的阵地——单人仓库（kalvinrv，2026-08-12 建、仅 3 commits），33 个技能全部调用 runcomfy CLI、357 个 UTM 链接指向 runcomfy.com、零处提到 fal 端点，这是 RunComfy 的 skills.sh 营销阵地（3.8M 安装）；而 fal 官方的 fal-ai-community/skills 仅 8.8K 安装且 2026-05-13 后停更。最大空位：fal 把"agent 优先"的精力全部收进自家围墙（fal Agent Early Access + 只覆盖自家 1000+ 模型的 Run MCP），跨供应商的 contract-first 统一契约层、成本感知路由、多供应商 job 编排完全没人做——这正是独立开发者 CLI 的切入位。

### 近 90 天时间线

- **2026-06-01 ~ 06-17** — serverless 运营能力密集上线：Analytics 扩 14 个指标、Per-Condition Retry 配置、Capacity 页、Usage API、Usage & Billing 改版、Docker 免改直部署（Direct Server Mode）（https://fal.ai/docs/changelog）
- **2026-06-24** — 招聘 Machine Learning Engineer, Reliability（Remote-APAC），此后 90 天新增 17 个岗位（https://jobs.ashbyhq.com/fal-ai）
- **2026-07-02 ~ 09-11** — 企业化招聘潮：Strategic Account Lead、Senior/Staff Core Product Systems、Compute Operations、Senior Solutions Architect、Network/K8s Infra、Solutions Marketer、Deal Desk & Pricing Ops、Community/Growth Marketer（https://jobs.ashbyhq.com/fal-ai）
- **2026-07-08** — 技术博客发 dSpark 1000 tok/s、16x 吞吐基建文（Ideogram v4 prompt expander），同日 changelog 上线 App-Level Retry Configuration（https://blog.fal.ai/how-we-achieved-1000-tok-s-and-16x-throughput-with-dspark-for-ideogram-v4-prompt-expander/）
- **2026-07-13** — 发《Serving sub-second Ideogram v4 without quality loss》等 3 篇，继续推理速度叙事（https://blog.fal.ai/serving-sub-second-ideogram-v4-without-quality-loss/）
- **2026-08-03 ~ 08-04** — fal deploy 支持部署消息与注解（CLI+SDK+API）；Runner 遥测新增 GPU Utilization 图表（https://fal.ai/docs/changelog）
- **2026-08-17** — 上线 Platform MCP Server（api.fal.ai/v1/mcp/platform）：15 个工具、11 个 serverless 调试工具 + 4 个发现网关，只读/无状态/免费；配套发布 Serverless Observability REST API 族（https://fal.ai/docs/changelog）
- **2026-08-27** — 发布首个第一方模型 H3 Max：fal Research 对 MiniMax H3 做后训练+推理优化，明确进入'平台+自研模型'双轨（https://blog.fal.ai/introducing-h3-max-by-fal/）
- **2026-09-09** — 新增 Community Growth、Growth Marketer 两个市场岗；创意侧 9-11 加 Creative Producer、9-17 加 Creative Technologist（营销团队用自家 agent 产出内容）（https://jobs.ashbyhq.com/fal-ai）
- **2026-09-14** — WebSocket 端点计费头（x-fal-billable-units）；9-09 Dashboard Playground 支持多端点切换——changelog 近 90 天全部是 serverless/平台向，无一条 CLI/agent/skills 更新（https://fal.ai/docs/changelog）
- **2026-09-17** — 发《H3 Max: Built with fal Inference and Training》：5 秒视频 3 秒内生成，人称偏好评测对 12 个领先视频模型三项第一（Artificial Analysis、Design Arena 独立基准亦第一）（https://blog.fal.ai/h3-max-built-with-fal-inference-and-training/）
- **2026-06-22 ~ 09-21（窗口内持续）** — 开源面仅 3 个仓库有推送：fal 主仓库（SDK 发布至 fal_v1.81.0、fal_client_v1.0.3）、fal-js、flashpack（高吞吐 tensor 加载）；genmedia CLI 与社区 skills 仓库零提交（https://github.com/orgs/fal-ai/repositories）

### Roadmap 信号

- **平台重心转向'agentic 运维'：官方明示 Platform MCP 让 assistant 替你走完调试路径（'why did my last request fail?'），并配套发布可观测性 REST API 族——下一步大概率继续把 serverless 全生命周期交给 agent**（置信：官方明示；https://fal.ai/docs/changelog）
- **fal Agent 是下一个主推产品：文档树已包含 projects/memory、custom skills、connectors、sandbox、training、video-sequences、video-understanding、plan-cards、spending-caps 全套，目前 Early Access、按月 credit 订阅（credits 跨产品通用、先于按量扣费、月末滚动）——正式 GA 与定价放开是最近可期的动作**（置信：官方明示；https://fal.ai/docs/documentation/agent/access-and-pricing）
- **'平台+自研模型'双轨确立：H3 Max 之后 fal Research 会继续出后训练模型（此前 4 月已发布 PATINA PBR 材质模型，基于 FLUX.2 klein），速度优先的模型品牌大概率扩展到图像/音频**（置信：官方明示；https://blog.fal.ai/introducing-h3-max-by-fal/）
- **企业销售规模化：90 天内新增 Strategic Account Lead、Solutions Architect、Deal Desk & Pricing Ops、Enterprise AM、Solutions Marketer 等 7+ 个 GTM 岗，叠加 2025-12 $140M Series D（Sequoia/Kleiner/NVIDIA）与 5 月 AWS 合作——正朝企业平台方向走**（置信：多源交叉；https://jobs.ashbyhq.com/fal-ai）
- **开发者 CLI/skills 通道被战略性降级：genmedia CLI（fal 员工 ilker@fal.ai 维护的 npm 包）停在 2026-03 beta、repo 停在 5-29；fal-ai-community/skills 停更 4 个月；changelog 与招聘里零 CLI/devtools 投入——他们把'agent 优先'的希望折叠进了 fal Agent 与 MCP，而非开发者终端工具**（置信：多源交叉；https://github.com/fal-ai-community/genmedia-cli）
- **fal Agent v2 或在内部酝酿：fal.ai 站点的 Next.js 路由清单中出现 /agent-v2、/agent-access 路由（当前 404 未发布）**（置信：推断；https://fal.ai/agent-v2）
- **changelog 已从主站迁移：fal.ai/changelog 返回 404，产品更新统一收进 docs.fal.ai/docs/changelog——文档站成为开发者信息的唯一正式出口**（置信：多源交叉；https://fal.ai/docs/changelog）

### 做得好的

- 双 MCP 战略是目前厂商里最完整的 agentic 面：Run MCP（mcp.fal.ai，9 工具，搜索/定价/运行/链式调用 1000+ 模型）+ Platform MCP（8-17 上线，15 个只读工具让 agent 调试'我的请求为什么失败'）——把'用 agent 造东西'和'用 agent 运维'分开做，且 Platform MCP 只读的设计是聪明的安全姿态
- 自研模型节奏快、叙事聚焦：H3 Max 走'后训练+推理协同优化'路线，主打极致速度（5s 视频 <3s），并引用第三方基准（Artificial Analysis、Design Arena）背书，而不是自说自话
- fal Agent 把开放格式吃进来：自定义 skills 直接兼容 agentskills.io 的 SKILL.md 格式、支持从 GitHub URL 安装——降低了生态迁移成本，也说明他们认可 skills 开放标准
- 对 AI 原生开发者体验很敏感：docs 提供 /docs/llms.txt 完整索引、llms 风格文档、状态页、透明的产品 changelog（近 90 天 15+ 条高频更新）
- 企业化护城河在加深：serverless 可观测性 API 族（events/revisions/runners history）、按条件的重试预算、机秒计费与 Reserve/Burst 分档、容量页——这些都是冲着大客户长期负载去的
- 技术内容营销质量高且密集（dSpark、MXFP8 quantizer、Triton inline ASM、epilogue fusion），既是招聘漏斗也是推理能力的信任状

### 空位与切入姿势

- **没有官方'跑任意模型'的一等 CLI：fal 官方 CLI 面向 serverless 应用部署（apps/deploy/runners/scale，附带 queue/run 子命令）；真正 agent-first 的 genmedia CLI 挂在社区组织、npm 停在 2026-03 的 0.1.2-beta，近 90 天零维护，而竞品 RunComfy 已发布打磨完整的 runcomfy CLI 并配上 skills 矩阵**
  - 证据：npm genmedia 0.1.2-beta（maintainer ilker@fal.ai）最后发布 2026-03-06；fal-ai-community/genmedia-cli 最后 push 2026-05-29；docs.fal.ai 的 CLI 章节全部是部署类命令
  - 切入：独立开发者做 contract-first 多供应商 CLI：一份统一 job 契约（submit/poll/cancel/artifact）映射 fal、Runway、Replicate、RunComfy、AtlasCloud 等后端，提供 dry-run 成本预估、幂等重放、SHA256 内容寻址产物缓存——这正是四种厂商哲学（CLI 即运行时/UX 剧本/脚本即技能/技能即文档）之上的公共层，厂商自己永远只会覆盖自家目录
- **skills 分发通道拱手让人：fal 官方社区 skills 在 skills.sh 仅 8.8K 总安装（头部 fal-image-edit 919），仓库 2026-05-13 停更；而 RunComfy 借 genmedia-labs 匿名组织拿下 3.8M 安装（video-edit 单技能 598.7K），fal 在这个新兴分发渠道近乎缺席**
  - 证据：skills.sh/genmedia-labs/skills（33 技能、3.8M 安装、357 个 runcomfy UTM 链接）vs skills.sh/fal-ai-community/skills（31 技能、8.8K 安装）；genmedia-labs 仓库零 fal 端点引用
  - 切入：以'多供应商路由'为差异点抢占 skills.sh：发布 vendor-neutral 的 model-routing、cost-aware 视频生成、跨厂商 fallback 技能（fal 的技能只懂 fal 目录，RunComfy 的只懂自家）；技能内嵌成本对比表与真实基准，蹭 skills.sh 的安装分发红利，质量对打 RunComfy 的 SEO 式铺量
- **成本可观测与预算控制在视频管线场景缺位：fal 的成本工具（get_pricing、Usage API、spending caps）全是单账号单产品视角，没有跨供应商的成本账本；视频迭代烧钱快，用户在 agent 对话里花钱无感**
  - 证据：Platform MCP 只读调试工具覆盖 spend 查询但仅限 fal 自家；Run MCP 的 get_pricing 只回答 fal 目录内价格；docs 无任何跨产品预算/成本聚合层
  - 切入：CLI 内置 per-generation 成本账本：每次生成的预估/实际花费、按 vendor/model 汇总、预算熔断（超阈值自动降级到便宜模型）、月度账单导出——对自由职业者和中小工作室是即买点
- **多镜头/角色一致性的开放编排层缺失：fal Agent 里有 video-sequences、characters/smart entities、资产库，但全部锁在 Early Access 的围墙 agent 内；公开 API 侧 workflows 只能编排 fal 自己的模型，无法把 Kling 的动作戏、Veo 的 B-roll、Seedance 的风格化镜头放进同一条时间线**
  - 证据：docs.fal.ai/documentation/agent/tools/video-sequences 等均为 Agent 产品页；fal.ai/docs/platform-apis/v1/workflows 仅编排 fal 生态内模型；官网 footer 的 Workflows/Playgrounds 亦为站内产品
  - 切入：把'剧本级'多镜头管线做成代码：开放的 shot list 契约（角色/场景/镜头语言/一致性约束）+ 每个镜头可指定不同 vendor/model + 失败镜头单点重跑；对标 Higgsfield 的 UX 剧本但以库/CLI 形态开放，而非封闭 App
- **跨供应商运行分析无人做：fal 8-17 刚为自家 serverless 补齐 events/revisions/runners-history 可观测性 API，但仅覆盖 fal；用户同时用多家供应商时没有统一的成功率/延迟/成本面板**
  - 证据：docs/changelog 8-17 条目明确这些 API 是为 Platform MCP 服务的自家观测；fal 无任何跨厂商遥测产品
  - 切入：轻量 analytics sidecar：CLI 埋点输出结构化运行日志（vendor、model、排队时长、端到端延迟、成本、失败原因分类），本地 SQLite + 一条命令出周报——先做开源攒口碑，再挂 SaaS
- **官方 MCP 面迭代放缓、工具数原地踏步：Run MCP 自 3-19 上线以来仍是 9 个工具，无批量作业、无管线原语、无 webhooks 集成；复杂多步任务全靠 assistant 自行循环 submit/check**
  - 证据：fal.ai/mcp 页面与 3-19 发布文对照：工具清单完全一致（search_models/get_model_schema/get_pricing/search_docs/run_model/submit_job/check_job/upload_file/recommend_model）
  - 切入：做 MCP 之上的'批处理/pipeline 中间件'：批量队列（N 个 prompt × M 个模型矩阵跑批）、结果自动验收（视觉模型打分）、失败自动换模型重试——独立开发者不必等 fal 自己做

### 未解问题

- fal Agent 何时 GA、credit 定价多少、是否会开放 skills 市场并给创作者分成（文档只有 Early Access 说明，具体 tier 价格页未公开拉取到）
- genmedia CLI 会不会复活并入官方 CLI，还是被 fal Agent 彻底替代后弃坑——决定独立 CLI 的窗口期长度
- fal 是否会正面回应 skills.sh 通道（8.8K vs RunComfy 3.8M 安装的悬殊），例如推官方 skills 合集或给 skills.sh 生态投资源
- /agent-v2 路由的真实含义与发布时间（仅从 Next.js 路由清单推断，无官方说明）
- H3 Max 的 API 定价与' Anbieter 独占期'安排，以及 H3 Max Director 这类演示应用是否会产品化
- fal.ai 主站 /changelog 被下线迁往 docs 的原因——是信息架构调整还是产品运营收缩的信号

### 来源

- [fal Product Changelog（docs，近 90 天全部平台更新）](https://fal.ai/docs/changelog)
- [fal MCP Server 产品页（Run MCP，9 工具）](https://fal.ai/mcp)
- [fal MCP Server 发布文（2026-03-19）](https://blog.fal.ai/connect-your-ai-to-1-000-models-with-the-fal-mcp-server/)
- [fal Agent 文档：Access and pricing（Early Access + credit tiers）](https://fal.ai/docs/documentation/agent/access-and-pricing)
- [fal Agent 文档：Custom skills（兼容 agentskills.io 格式）](https://fal.ai/docs/documentation/agent/skills/custom-skills)
- [fal Agent 产品页](https://fal.ai/agent)
- [Introducing H3 Max by fal（2026-08-27）](https://blog.fal.ai/introducing-h3-max-by-fal/)
- [H3 Max: Built with fal Inference and Training（2026-09-17）](https://blog.fal.ai/h3-max-built-with-fal-inference-and-training/)
- [skills.sh：genmedia-labs/skills（RunComfy 阵地，3.8M 安装）](https://skills.sh/genmedia-labs/skills)
- [genmedia-labs/skills 仓库（单人、3 commits、runcomfy CLI）](https://github.com/genmedia-labs/skills)
- [genmedia-labs video-edit SKILL.md（全文指向 runcomfy.com）](https://github.com/genmedia-labs/skills/blob/main/video-edit/SKILL.md)
- [skills.sh：fal-ai-community/skills（8.8K 安装）](https://skills.sh/fal-ai-community/skills)
- [fal-ai-community/skills 仓库（2026-05-13 停更，提交者为 fal 员工）](https://github.com/fal-ai-community/skills)
- [fal-ai-community/genmedia-cli（Agent-first CLI，2026-05-29 停更）](https://github.com/fal-ai-community/genmedia-cli)
- [npm genmedia 包（0.1.2-beta，maintainer ilker@fal.ai，2026-03-06）](https://www.npmjs.com/package/genmedia)
- [fal 招聘板（Ashby，31 个岗位含发布日期）](https://jobs.ashbyhq.com/fal-ai)
- [fal Careers 页（80 人、SF、产品线全景）](https://fal.ai/careers)
- [fal-ai GitHub org（近 90 天仅 3 仓库有推送）](https://github.com/orgs/fal-ai/repositories)
- [fal/fal releases（fal_v1.81.0、fal_client_v1.0.3 等）](https://github.com/fal-ai/fal/releases)
- [blog.fal.ai 全量博文 sitemap（121 篇含日期）](https://blog.fal.ai/sitemap-posts.xml)
- [dSpark 1000 tok/s 基建文（2026-07-08）](https://blog.fal.ai/how-we-achieved-1000-tok-s-and-16x-throughput-with-dspark-for-ideogram-v4-prompt-expander/)
- [Our Series D: Scaling fal（2025-12-09，$140M，背景轨迹）](https://blog.fal.ai/our-series-d-scaling-fal/)
- [docs.fal.ai sitemap（agent/skills/workflows/mcp 全文档树）](https://docs.fal.ai/sitemap.xml)

---

## AtlasCloud

AtlasCloud 近 90 天的重心很清晰：模型目录自动化扩张（52 天从 386 个同步到 450 个，约 2-3 次/周的自动 commit）+ 渠道从"装 skill"升级为"Codex 插件 + OAuth 免 API key 分发"（9 月上旬拆出独立插件仓库并上架商店元数据），平台侧则补账务与协议基建（分时定价、按模型披露 OpenAI/Anthropic/Gemini 协议、key 轮换）。"技能即文档"路线没有重构：主 SKILL.md 仍是 574 行一行未减（还硬编码"300+ models"而实际已是 450，文档漂移已出现），膨胀被转移到卫星层——两个中英双语子 skill（语言路由模式）、22 篇 library 玩法库、Codex 插件拆仓。作为后进聚合云，他们押注的是模型广度 + 价格（68% off + 分时定价）+ "更少护栏的 full-capability pipeline"（README 原文营销）+ 分发渠道密度。最大空位在契约层以下：全栈都是给人/agent 读的 Markdown，没有机器可读的 per-model 参数契约、没有统一任务生命周期（视频仍靠轮询，Webhook 仅音频）、没有任何 eval/回归基建、450 个模型没有路由/比价原语——这四块正好是 contract-first CLI 可以整体吃掉的地层。

### 近 90 天时间线

- **2026-06-26** — 用户在 skills 仓库提交 issue #2（用 skill 经 Gemini Omni Flash 剪辑视频出问题），至今 open、0 条回复——社区响应债的直接证据（https://github.com/AtlasCloudAI/atlas-cloud-skills/issues/2）
- **2026-07（changelog 月份条目）** — 平台上线分时定价（高峰/低谷）、按 key/成员/模型的支出统计 CSV、音频任务 Webhook（视频没有）、最多 5 个团队（https://www.atlascloud.ai/docs/changelog）
- **2026-07-31** — 博客预告 Seedance 2.5（30 秒原生视频、50 参考图、灵活剪辑）；同日发 Yapper 客户案例（https://atlascloud.ai/blog）
- **2026-08-06** — 把 awesome-seedance-2.5 仓库里的两个技能收编为主仓库子 skill：seedance-2-5-skill + universal-video-prompt-skill，references 全套中英双语镜像并内置'语言路由'（中文请求先读 workflow.zh-CN.md，代码/模型 ID 不翻译）（https://github.com/AtlasCloudAI/atlas-cloud-skills/commits/main）
- **2026-08-11 / 08-12** — 新增 Atlas 3D 生成 skill（9 月 8 日又暂时移除）；6 天内修复'API key 默认出现在命令行'的安全问题（#5）；description 修剪到 Agent Skills 1024 字符上限（#4）（https://github.com/AtlasCloudAI/atlas-cloud-skills/issues/5）
- **2026-08-18** — 三个 issue/PR 同日把 Kling 4.0 与 Wan 3.0 刷成'当前模型'并对照 live 目录刷新全部模型版本；README 声明模型列表由 .github/scripts/update-models-readme.mjs 自动生成、禁止手改（https://github.com/AtlasCloudAI/atlas-cloud-skills/issues/8）
- **2026-08（changelog 月份条目）** — API key 一次性完整显示+可轮换；按模型披露支持的协议（Chat Completions / Responses / Anthropic Messages / Gemini）；多模态 LLM 支持音频输入；使用历史才开始显示错误详情和原始响应体（https://www.atlascloud.ai/docs/changelog）
- **2026-08-14** — 创建 awesome-minimax-h3（H3 生态聚合：权重/LoRA/ComfyUI 节点/工作流）和 dsh-media-gen（DeepSeek Harness 里规划媒体工作流）——生态卡位 + 新 harness 适配（https://github.com/AtlasCloudAI/awesome-minimax-h3）
- **2026-09-04 至 09-18** — CLI 结束暑期沉寂（v0.1.16 后停了近 3 个月），14 天连发 9 个版本至 v0.1.25，仍在 v0.1.x 未到 1.0（https://github.com/AtlasCloudAI/cli/releases）
- **2026-09-08 / 09-09** — skill 打包为 Codex 插件上架（品牌图标+商店元数据）；先试集体改名当日 revert，最终把插件拆到独立仓库 atlas-cloud-plugin——OAuth 一次浏览器登录、免 API key、计费走用户自己的 Atlas 账号（https://github.com/AtlasCloudAI/atlas-cloud-plugin）
- **2026-09-11** — mcp-server 开出两个内部中文 issue：#11 请求用 GitHub Actions 构建发布镜像、#12 自曝 combo/oauth-exchange 分支与 main 已分叉且生产镜像从分支构建（均 0 回复）；同日批量刷新全部 awesome-* prompt 仓库（https://github.com/AtlasCloudAI/mcp-server/issues）
- **2026-09-14** — 为 Codex 插件补中文安装指南（面向 0.4.2 升级路径）——中文内容按需打补丁，仍无系统性中文文档（https://github.com/AtlasCloudAI/atlas-cloud-plugin）
- **2026-09-18** — 企业案例博客：Lindy 在 Atlas Cloud 上把 agent 推理成本降 90%——营销重心偏向 agent/编码推理市场（对应首页 Coding Plan 入口）（https://atlascloud.ai/blog）
- **2026-09-21** — 目录自动同步达 450 个模型（视频 200/图像 130/LLM 73/音频 13/3D 10，52 天净增 64）；comfyui、mcp-server、cli、skills 四仓库同日 push；博客一天发 6+ 篇开发者向 SEO 文（API 测试、'successful failures'、竞品替代等）（https://github.com/AtlasCloudAI/atlas-cloud-skills/commits/main）

### Roadmap 信号

- **渠道战升级为平台级分发：Codex 插件 + OAuth 免 key（浏览器登录授权、计费到用户账号），大概率会复制到 Claude Desktop/Cursor 等宿主——'装 skill'变'装渠道'**（置信：官方明示；https://github.com/AtlasCloudAI/atlas-cloud-plugin）
- **模型目录扩张会继续且保持自动化：'Day-0 SOTA Access'是首页主标语，目录同步已成 2-3 次/周的制度化 commit，模型数从 386 涨到 450 未减速**（置信：官方明示；https://github.com/AtlasCloudAI/atlas-cloud-skills/commits/main）
- **多协议兼容（每模型披露 Chat Completions / Responses / Anthropic Messages / Gemini）将作为聚合层护城河继续加深——8 月刚上的披露机制是前置动作**（置信：官方明示；https://www.atlascloud.ai/docs/changelog）
- **向 agent/编码推理市场倾斜：Coding Plan 入口 + Lindy'推理成本降 90%'案例 + 09-21 一天 6 篇开发者 SEO 文，营销预算正在从创作者教程转向开发者获客**（置信：多源交叉；https://atlascloud.ai/blog）
- **垂直 demo 应用试水（marketing/edu/collage/explainer 四个 studio 仓库 7 月集中创建）是在测 API 上游哪些场景值得做产品化**（置信：官方明示；https://github.com/AtlasCloudAI/atlas-marketing-studio）
- **'更少护栏的 full-capability pipeline'作为对大厂内容限制的套利卖点会继续（README 原文营销'unrestricted / fewer guardrails'）——差异化明确但合规与支付通道风险自负**（置信：官方明示；https://github.com/AtlasCloudAI/atlas-cloud-skills）
- **按旗舰模型逐个复制专属子 skill（目前只有 Seedance 有，Kling 4.0 / Wan 3.0 / Veo 未跟）——大概率每个爆款模型一个 skill 目录**（置信：推断；https://github.com/AtlasCloudAI/atlas-cloud-skills）
- **在观望 agent skills 生态的索引/注册表方向：08-19 fork 了 jwynia/agent-skills 后零动作，说明在看 skill 分发标准化但未下注**（置信：推断；https://github.com/AtlasCloudTeam/agent-skills）

### 做得好的

- 模型目录自动化纪律：README/SKILL.md 的模型列表由脚本从 live 目录生成（ATLAS-MODELS:START 标记 + update-models-readme.mjs，注释明确'禁止手改'），450 个模型基本零手工漂移——把'模型目录'当数据管道而非文档，值得直接学
- 分发矩阵广度是四家之最：同一套 skill/API 同时铺 Codex 插件、Claude Code、Gemini CLI、ComfyUI 节点、n8n、Dify、OpenClaw、lobe-chat——聚合云把渠道密度当护城河
- 子 skill 的'语言路由'双语模式可直接借用：英文请求读 en 文件、中文请求先读 workflow.zh-CN.md，模型 ID/JSON 键/命令强制不翻译——低成本实现双语而不必翻译主文件
- 内容获客闭环：awesome-seedance-2.5-prompts-skills（200 星，比主仓库 32 星还热）每个 prompt 都附真实生成的预览，垂直 studio（营销/教育/拼贴/解说）做 API 上游的需求探针——GitHub 流量 + SEO 双引擎
- 旗舰模型补票速度快：Seedance 2.5 从预告（07-31）到上线+专属 skill 收编（08-06）8 天内完成；发现 key 上命令行的安全问题后 6 天修复
- 协议面铺得宽：同一个模型同时兼容 OpenAI/Anthropic/Gemini 三家 SDK 协议并按模型披露，加上 x-api-key 头、Responses API——'任何现成 SDK 都能直连'是聚合层的真实粘性

### 空位与切入姿势

- **全栈没有机器可读契约层——'技能即文档'止步于人/agent 读的 Markdown**
  - 证据：仓库无任何 JSON Schema 或测试 fixture；atlascloud.json 只是 6.5KB 的 OpenAPI 骨架；参数契约只存在于按模型的 UI 文档（changelog 2026-07 '仅显示各模型实际支持的采样参数'）和 SKILL.md 表格里；目录同步的产出是 Markdown 列表而非数据文件；文档漂移已经发生——SKILL.md description 和 README 徽章仍写'300+ models'，实际已是 450
  - 切入：用他们免鉴权的 GET /api/v1/models 端点（SKILL.md 里明确标注无需鉴权）做契约生成器：per-model 参数 schema+价格+模态，输出可校验的 JSON Schema 并提供 contract diff/verify——在'52 天加 64 个模型'的漂移环境里，contract-first CLI 正好占住他们没做的这一层
- **视频任务生命周期无统一抽象：视频仍靠轮询，Webhook 只给了音频**
  - 证据：changelog 2026-07 仅'音频任务支持 Webhook 回调'；SKILL.md 端点表里视频只有 GET /prediction/{id} 轮询；无取消、幂等键、断点恢复的任何 API 或文档
  - 切入：CLI 内建跨厂商统一 job runtime：submit/poll/webhook 自适应切换、幂等提交、本地队列、失败重试与恢复——对 AtlasCloud、fal、官方 API 用同一套任务语义，这是聚合层之上他们没做、聚合层之下做不了的夹层
- **零 eval/回归基建：skill 与模型升级全在裸奔**
  - 证据：atlas-cloud-skills 近 90 天 58 个 commit 全是文档/目录同步/插件操作，无一个测试或 eval 文件；对比 Higgsfield 有 evals、fal 有 index.json+SHA256 锁定；200 星 prompt 库的'真实预览'是一次性产物，无回归语义；Seedance 2.5 八天补票式的更新没有任何质量验证痕迹
  - 切入：做跨厂商 golden-prompt 回归套件（固定 prompt 集 → 成本/延迟/结构化输出校验），发布为开源 CI action——他们每次模型升级都是验证空窗，这个基建可以同时卖给多家厂商和聚合云
- **失败语义与可观测性欠账，连他们自己都在拿这个痛点写博客获客**
  - 证据：09-21 博客《Stop Shipping 'Successful' Failures》和《AI Tools for API Testing》把聚合 API 的失败问题当营销素材；平台侧 2026-08 才加'错误详情+原始响应体'显示；mcp-server issue #12 自曝生产镜像从与 main 分叉的分支构建（infra 成熟度信号）
  - 切入：统一错误分类学（各供应商错误映射为稳定 errno）+ 请求重放日志 + 成本/延迟遥测，CLI 提供 --explain-failure——把他们的博客痛点做成产品
- **450 个模型零路由/比价原语，选择负担全压给开发者**
  - 证据：官网主打'up to 68% off'和分时定价（changelog 2026-07），但 API 与 skill 层没有任何'按成本/延迟/质量选模型'的路由端点或工具；对比 fal 的 run "<prompt>" 智能路由——Atlas 卖的是目录广度，不是决策辅助
  - 切入：meta-router CLI：--cheapest/--fastest/--best 路由 flag，数据源就用 Atlas 与 fal 的公开目录和价格端点做跨厂商实时比价，甚至跨 Atlas/fal/官方 API 做统一路由——他们的价格优势反而可以被你变成路由优势
- **双语是补丁不是体系：中文只出现在边缘层**
  - 证据：主 SKILL.md、README、官网首页全英文（对主 skill 目录 grep 中文字符为空）；中文仅存在于两个子 skill 的 zh-CN 镜像、插件中文安装指南、以及 mcp-server 内部中文 issue（团队工作语言是中文）；官网 20 语言本地化是 2025-12 的站点级动作，开发者文档无中文
  - 切入：做中文一等开发者体验：中文文档+中文 prompt 契约模板（对接 Seedance/Wan/Kling/Hailuo 的中文 prompt 习惯），这是英文外壳的中国团队反而没占住的位置；他们的微信/支付宝收款和'no VPN'话术说明需求存在，但供给只在营销层
- **社区响应与治理债：issue 即黑洞**
  - 证据：skills 仓库 issue #2（Gemini Omni Flash 视频编辑问题）开了 88 天 0 回复；mcp-server 7 个 open issue 里 5 个 0 评论；无 careers 页、无公开路线图——后进聚合云的信任积累还没开始
  - 切入：独立开发者用'48 小时响应 + changelog 纪律'做信任差异化；或者反过来做 AtlasCloud 生态的积极维护者/集成者（他们的 agent 工具层星数远低于 prompt 库，说明需求真实但供给粗糙），吃他们引来的流量

### 未解问题

- Coding Plan（agent 推理）与视频生成 API 的收入/战略权重各占多少？Lindy 案例是 LLM 推理成本优化，视频在叙事里是否已被降级为品类之一
- mcp-server 的 CI 债如何收口：#11（Actions 构建镜像）与 #12（生产镜像从分叉分支构建）是否有内部排期，还是继续从分支构建生产
- 主 SKILL.md 的 574 行是计划瘦身重构，还是接受'主文件冻结+卫星膨胀'的现状？'300+'硬编码何时修
- 是否会出现系统性中文开发者文档与 CLI 中文文案（内部协作已用中文，但产品面全是英文优先）
- 'unrestricted / fewer guardrails'定位的支付通道与合规风险（Stripe/卡组织对内容类目政策）是否会迫使其收缩，收缩后这批需求流向哪里
- Kling 4.0 / Wan 3.0 / Veo 是否会各复制一个 Seedance 式专属子 skill，还是收敛为统一模型配置——影响子 skill 模式的可维护性判断
- 对 Agent Skills 生态规范（skill 索引、版本锁定、签名）的官方立场：fork jwynia/agent-skills 后零动作，是观望还是放弃

### 来源

- [Atlas Cloud 官网首页（模型目录/定位/Coding Plan/MCP & CLI）](https://atlascloud.ai)
- [Atlas Cloud 官方博客索引（Seedance 2.5 预告、Lindy 案例、09-21 批量开发者文）](https://atlascloud.ai/blog)
- [Atlas Cloud 官方 Changelog（分时定价/多协议披露/Webhook/3D 等按月记录）](https://www.atlascloud.ai/docs/changelog)
- [Atlas Cloud 开发者文档（MCP Server / CLI / Skills 章节与语言切换器）](https://www.atlascloud.ai/docs)
- [AtlasCloudAI/atlas-cloud-skills（commit 活动/issue/仓库结构）](https://github.com/AtlasCloudAI/atlas-cloud-skills)
- [atlas-cloud-skills issue #2（Gemini Omni Flash 编辑问题，88 天未响应）](https://github.com/AtlasCloudAI/atlas-cloud-skills/issues/2)
- [atlas-cloud-skills issue #5（API key 命令行泄露修复）](https://github.com/AtlasCloudAI/atlas-cloud-skills/issues/5)
- [AtlasCloudAI/atlas-cloud-plugin（Codex 插件：OAuth 免 key、中文安装指南）](https://github.com/AtlasCloudAI/atlas-cloud-plugin)
- [AtlasCloudAI/mcp-server（open issues 含 CI/分支分叉内部问题）](https://github.com/AtlasCloudAI/mcp-server/issues)
- [AtlasCloudAI/cli（v0.1.10→v0.1.25 release 记录）](https://github.com/AtlasCloudAI/cli/releases)
- [AtlasCloudAI/awesome-seedance-2.5-prompts-skills（200 星 prompt+skill 库）](https://github.com/AtlasCloudAI/awesome-seedance-2.5-prompts-skills)
- [AtlasCloudAI/atlas-marketing-studio（垂直应用试水代表）](https://github.com/AtlasCloudAI/atlas-marketing-studio)
- [AtlasCloudTeam/agent-skills（fork 自 jwynia/agent-skills，生态观望信号）](https://github.com/AtlasCloudTeam/agent-skills)

---

## Higgsfield + Runway

90 天窗口内两家走向明显分化：Higgsfield 的"UX 剧本"技能路线仍在加码（higgsfield-ai/skills 7/8–9/11 高频迭代出 websites/game/brandkit/explainer/Ad Multiplier 一整套"应用工厂"技能，MCP 以免 API key 方式铺进 ChatGPT/GPT-6 Astra/Claude/Cursor 等 7+ 客户端），但重心已从 CLI 转向 ChatGPT 分发和无代码 app，计费"坑"没修反而更碎（credits、All Unlimited、Bonus Seconds、MCP 专属 credits、console API 五套面并存，官方 9 月连发两篇解释文）；CLI 仓库 8 月零提交、release 多为 docs 空转，进入维护态。Runway 则把 Developer Platform 做成明示主线：8/28 skills 仓库重构让 runway-dev-* 成为唯一集成路径、MCP 服务器 7 月连获远程 HTTP/模型目录/媒体预览更新、API changelog 90 天 15+ 次上新（Model Router→容量回退→路由历史三连击、Task Cost API、ACEScg/ProRes 专业交付），同时招聘 Founding DX Lead 与 Dev Platform 产品/设计岗，域名迁 runway.com 并向企业（SSO/审计/Team Plan）、Adobe 插件和日本市场扩张。最大空位在"契约层"：Runway 无官方 CLI 且开源 MCP 只有 9 个工具、高频弃用无迁移工具；Higgsfield 技能无版本化、计费无编程化查询接口；两家都没有确定性评测基准和产物契约——这正是一个契约优先多厂商 CLI 的立足点。

### 近 90 天时间线

- **2026-07-02** — Runway 上线 Agent Skills：一条命令生成广告 campaign、商业片等；7/8 开放 Custom Agent Skills（用户可自建并共享技能）——技能路线写入产品主 changelog（https://runway.com/changelog）
- **2026-07-04** — Higgsfield Unlimited Models Marketplace 扩展至 Team/Scale（按席位购买、不可转让）——计费面继续增项（https://higgsfield.ai/changelog）
- **2026-07-07** — Higgsfield Apps 发布：无代码生成完整 generative app，可经 MCP 从 Claude/Cursor 构建；同日 App Contest 明确'第三方 API 接入生成取消参赛资格'，说明 API 与平台双轨（https://higgsfield.ai/changelog）
- **2026-07-08** — Higgsfield skills 仓库进入高频迭代期：higgsfield-websites 技能持续重构（动画默认、deploy-first、反 slop、hermes 同步），7/16 新增浏览器游戏技能与 CLI video explainer 技能（https://github.com/higgsfield-ai/skills/commits/main/）
- **2026-07-13** — Higgsfield After Effects 插件接入 Supercomputer 与 MCP（bridge.higgsfield.ai/mcp），agent 可直接操作合成/图层/关键帧（https://higgsfield.ai/changelog）
- **2026-07-16** — Runway 开源 MCP 服务器两天两更：新增远程 HTTP 传输、模型目录与按工具覆盖、内联媒体预览、MCP_TOOL_TIMEOUT 配置（https://github.com/runwayml/runway-api-mcp-server/commits/main/）
- **2026-07-20** — Higgsfield 上线 All Unlimited 通行证（图像/视频/音频顶级模型一张通行证、共享并发、一次一任务）（https://higgsfield.ai/changelog）
- **2026-07-23** — Runway 发布 Model Router API：configId 保存路由配置、成本/延迟/质量偏好、允许/拒绝列表、每模态 credit 上限、dryRun；7/30 追加并发达上限时自动回退次优模型，7/30 同日上线 Task Cost API（响应内含每任务 credit 成本）（https://docs.dev.runwayml.com/api-details/api_changelog/）
- **2026-07-28** — Runway 新增企业端点：org usage 与 audit_logs API（https://docs.dev.runwayml.com/api-details/api_changelog/）
- **2026-08-03** — Runway Model Router 路由历史上线：记录每次路由决策及原因，可经公开 API 获取——'多模型调度层'三周内三连击（https://runway.com/changelog）
- **2026-08-03** — Higgsfield skills 新增 Brandkit 与 YouTube Thumbnail 技能；8/7 将 game-generation 并入 higgsfield-websites（游戏定为第三种产品类型）（https://github.com/higgsfield-ai/skills/commits/main/）
- **2026-08-05** — Runway 开启第三方模型高频聚合：90 天内陆续上新 Hailuo 3.0、Grok Imagine、WAN 3.0、Seedance 2.5、MiniMax H3 Max、GPT Image 2.5 等 15+ 次模型更新（https://docs.dev.runwayml.com/api-details/api_changelog/）
- **2026-08-14** — Higgsfield Seedance 2.5 推出 Bonus Seconds：按秒计费的独立池、不扣 credits、30 天有效——计费体系再添一层（https://higgsfield.ai/changelog）
- **2026-08-17** — Runway org 入库 runway-api-mcp-server 与 avatars-sdk-react（代号 GWM-1）（https://github.com/orgs/runwayml/repositories）
- **2026-08-19** — Higgsfield for Enterprise：SOC 2 与 SSO、无限席位、按团队分配 credits（https://higgsfield.ai/changelog）
- **2026-08-20** — Runway MCP 支持工作流：agent 可列出/编辑/运行 Workflows；同日 Ruby SDR→HDR 调色模型覆盖 Tool Mode、Workflows 与 Runway Dev（https://runway.com/changelog）
- **2026-08-22** — Higgsfield Grok Bot 进 MCP：新用户验卡得 3 天试用 + 100 个 MCP 专属 credits，未取消自动续为月付 Plus——'MCP 专属 credits'与平台 credits 并存（https://higgsfield.ai/changelog）
- **2026-08-26** — Higgsfield Supercomputer 免费模型 Ox Alpha 被证实为智谱 GLM-5.3 Flash 并转为消耗 credits；8/27 MCP 调用故障修复（https://higgsfield.ai/changelog）
- **2026-08-28** — Runway skills 仓库同日三个 commit（#19/#20/#21）：新增 MCP-aware Dev Platform 集成技能，并将 runway-dev-*（models/model-routers/characters/recipes/workflows）定为唯一集成路径（https://github.com/runwayml/skills/commits/main/）
- **2026-08-31** — Runway 专业交付格式连续上线：ACEScg OpenEXR 序列（8/31）、video_to_hdr 支持 alpha 通道（9/11）、帧率增强（9/17）——瞄准专业制片管线（https://docs.dev.runwayml.com/api-details/api_changelog/）
- **2026-09-07** — Higgsfield MCP 登陆 GPT-6 Astra 并发布 Games 2.0（changelog 9/4 已先上线 GPT-6 Astra 与 3D Jutsu）——分发重心转向 ChatGPT 生态（https://higgsfield.ai/blog）
- **2026-09-10** — Higgsfield 连发《Why Your AI Video Credits Run Out Faster Than You Expect》（9/10）与《Credits vs Unlimited Plans》（9/15）——官方下场解释计费混乱（https://higgsfield.ai/blog）
- **2026-09-11** — Higgsfield skills 默认模型统一切到 GPT Image 2.5 / Seedance 2.5（直接改 main，无版本号）；同日 higgsfield-ai/cli 最后一次功能性 commit 也只是 docs 模型默认值更新，8 月该仓库零提交（https://github.com/higgsfield-ai/skills/commits/main/）
- **2026-09-16** — Higgsfield 首波 API 公开推送：同日发布《Meet the Higgsfield API》《How To Generate AI Videos Straight From the Higgsfield API》《Inside Higgsfield #2: Supercomputer》三篇（https://higgsfield.ai/blog）
- **2026-09-04** — Runway 上线自助 Team Plan（每席位 6,900 credits 共享池、最多 9 人）；9/8 发布 Runway Plugins for Adobe（Premiere/After Effects 面板）；9/4 sdk-python/sdk-node 更新；9/10 入库 runway-characters-meet（https://runway.com/changelog）
- **2026-09-22（窗口内持续）** — Runway 招聘确认 Dev Platform 主线：Founding Developer Experience Lead、Dev Platform 产品总监/资深 PM/资深产品设计师、MTS Backend API、EM API，另有 Robotics Engineer (Research) 与 GM Japan（https://runway.com/careers）

### Roadmap 信号

- **Runway 把 Developer Platform 确立为公司下一主线：在招 Founding Developer Experience Lead（founding 级）、Dev Platform 产品总监 + 资深 PM + 资深产品设计师、MTS Backend API、EM API——一个子系统同时招齐 DX、产品、设计、工程四条线**（置信：官方明示；https://runway.com/careers）
- **Runway 技能路线收敛到 Dev MCP 优先：8/28 三个 commit 把 runway-dev-* 定为唯一集成路径并标注 MCP-aware，未来 skills 生态将围绕 Dev Platform MCP 而非裸 REST 教程展开**（置信：官方明示；https://github.com/runwayml/skills/commits/main/）
- **Runway 正在把自己建成'多模型调度层'：Model Router（7/23）→ 容量自动回退（7/30）→ 路由历史 API（8/3）三周三连击，下一步大概率是路由策略市场/跨厂商路由（已聚合 7+ 第三方模型）**（置信：官方明示；https://docs.dev.runwayml.com/api-details/api_changelog/）
- **Runway 向企业+国际化扩张：SSO 默认化、配置告警、Team Plan 自助化、GM Japan + Founding Deployment Lead Japan 在招、域名迁移 runway.com**（置信：官方明示；https://runway.com/changelog）
- **Runway 在角色/虚拟人/实体方向埋点：avatars-sdk-react（代号 GWM-1）8/17 入库、runway-characters-meet 9/10 入库、Robotics Engineer (Research) 在招、Runway Studios 创意岗位扩张——可能孵化独立角色产品线**（置信：推断；https://github.com/orgs/runwayml/repositories）
- **Higgsfield 分发押注 ChatGPT/GPT-6 Astra：MCP 上 GPT-6 Astra（9/7）、ChatGPT 内直接生成视频（8/14）、Grok Bot 常驻（8/22）、3D Jutsu 捆绑 GPT-6 Astra（9/4）——多篇文章与 changelog 交叉印证'宿主 agent 承载 UI'路线**（置信：多源交叉；https://higgsfield.ai/blog）
- **Higgsfield 产品重心从'视频效果'转向'应用工厂'：websites/game/explainer/brandkit/Apps/3D Jutsu 连续落地，Supercomputer 升级为中枢（Projects 共享工作区 8/23、GPT-6 Astra 多步工作流 9/4）**（置信：多源交叉；https://higgsfield.ai/changelog）
- **Higgsfield 开始公开经营 API 招牌：9/16 同日三篇 API 文章（产品介绍+教程+基建幕后），console.higgsfield.ai 以'50+ 模型一个 API'独立售卖——API 会成为下一阶段的显性产品线**（置信：多源交叉；https://higgsfield.ai/blog）
- **Higgsfield 计费短期不会收敛反而继续增项：9/3 Scale 无限模型、8/14 Bonus Seconds、8/22 MCP 专属 credits、8/26 免费模型转收费——每个新面都是独立池，碎片化是产品策略而非过渡态**（置信：官方明示；https://higgsfield.ai/changelog）
- **Higgsfield CLI 进入维护态：8 月零提交、9 月仅 docs 默认值更新、v1.1.19–v1.1.24 多个 release 指向同一 commit（docs 空转），核心人力已转向 skills 与 ChatGPT 分发**（置信：推断；https://github.com/higgsfield-ai/cli/commits/main/）

### 做得好的

- Higgsfield 技能迭代速度惊人：两个月内从 websites 到 game、brandkit、YouTube thumbnail、Ad Multiplier 铺出完整'应用工厂'技能矩阵（skills 仓库 1.1k stars、89 commits），且每个技能都对应可展示的成品而非 API 文档
- Higgsfield MCP 零门槛分发：mcp.higgsfield.ai/mcp 免 API key 直连，覆盖 ChatGPT/Claude Code/Cursor/Grok Bot/OpenClaw/Hermes 等 7+ 客户端，把分发做成了默认动作；Adobe AE、Blender、DaVinci 三套创意工具桥接也全部走 MCP
- Higgsfield 用营销闭环养技能：$1M 电影节、$100k App Contest、Create in Public credits 资助，让技能产出有真实受众和传播素材
- Runway 把成本做成 API 一等公民：Task Cost API（7/30）在响应里直接返回每任务 credit 成本（运行中估算+完成时终值），Model Router 路由历史可 API 拉取审计——这是两家唯一把'可预测成本'产品化的
- Runway skills 仓库工程化最规范：runway-dev-* 家族结构清晰（models/routers/characters/recipes/workflows），8/28 敢于做破坏性收敛（'唯一集成路径'），MIT 许可 + 双安装通道（npx skills add / claude plugin marketplace）
- Runway API 聚合节奏行业最快：90 天 15+ 次模型上新，第三方模型（Seedance/WAN/Hailuo/Grok/GPT Image）全部经统一 API 暴露，同时保住 HDR/ACEScg/ProRes 专业交付差异化
- Runway 企业端点补齐迅速：org usage、audit_logs（7/28）、SSO 默认化与配置告警（8/24）、Team Plan 自助化（9/4），从创作者工具向组织采购平滑过渡

### 空位与切入姿势

- **Runway 没有官方 CLI**
  - 证据：runwayml org 下 63 个仓库全是 SDK/MCP/skills/演示，无 CLI 仓库；skills 的用法是让 agent 读 SKILL.md 后自行拼 REST 调用，Model Router configId、Task Cost、路由历史这些 API 一等公民没有任何命令行入口
  - 切入：做契约优先的 Runway CLI：`router create/dry-run/apply`、`task cost --history`、`routes export`，把 Model Router 配置文件化（JSON 契约进 git）、成本报表命令化；也可给 runwayml/skills 提 PR 补 CLI 层借官方流量
- **Runway 开源 MCP 只有 9 个工具，远窄于其真实能力面**
  - 证据：runway-api-mcp-server 仅 listModels/generateVideo/generateImage/upscaleVideo/editVideo/generateAudio/getTask/cancelTask/getOrg；Recipes、Workflows、Model Router 管理都不在其中（Workflows 只进了产品内闭源 Agent MCP，见 8/20 changelog），且 24 commits 无 release、无语义版本
  - 切入：独立维护超集 MCP/CLI：Recipe 执行器、Router 配置管理、routing-history 拉取做成本/质量报表——官方 9 工具与文档能力面之间的差集就是产品定义
- **Runway 高频上新+弃用但零迁移工具**
  - 证据：90 天内 Gen-3 Alpha Turbo/Gen-4 Aleph 弃用（7/30）、默认模型反复切换、15+ 模型上新；docs 只有按日流水 changelog，无弃用 RSS/webhook、无参数兼容矩阵、无 codemod——依赖它的自动化管线每次都要人工扫 changelog
  - 切入：做跨厂商模型目录 diff 与弃用告警服务：定期快照各厂商模型目录（模型/参数/价格/弃用状态），机器可读 diff + webhook 通知 + 旧→新参数映射建议，直接嵌入用户 CLI 的 CI 流程
- **Higgsfield 技能无版本化、无机器可读契约**
  - 证据：higgsfield-ai/skills 89 个 commit 直接改 main 的 SKILL.md，无 semver、无 CHANGELOG；9/11 一次 commit 把全库默认模型切到 GPT Image 2.5/Seedance 2.5，`npx skills add higgsfield-ai/skills` 拉的是漂移中的 main 头——技能产出不可复现
  - 切入：做技能注册表 + 版本锁：fork 官方技能集并打语义版本与参数 schema（类似 package-lock），提供'锁定版技能集'供 CI 消费；对漂移出 diff 报告。这与'契约优先'定位天然同构
- **Higgsfield 计费碎片化且无编程化查询接口**
  - 证据：90 天 changelog 中计费类条目 12+ 条：All Unlimited（7/20）、存储按 1GB=2.5 credits（7/8）、Bonus Seconds 独立池（8/14）、MCP 专属 credits + 自动转付费 Plus（8/22）、免费模型 GLM 转收费（8/26）、Scale 无限（9/3）；/cli 页宣称'同一 credit 体系'但 MCP 又有专属 credits；无公开 balance/usage API，官方需连发两篇博文（9/10、9/15）向用户解释
  - 切入：做统一计费聚合器：一个本地 ledger/CLI 子命令，把订阅 credits、Bonus Seconds、MCP credits、console API 余额汇总查询、用量预警和成本归因（哪个 agent 会话烧掉了多少）——多厂商 CLI 的天然模块，Higgsfield 自身不会做（暴露内部池不利营销）
- **Higgsfield 订阅与 console API 双轨依旧，且互相对立**
  - 证据：console.higgsfield.ai 独立售卖'50+ 模型一个 API、最优价格'；官方 changelog 无任何 API 条目；7/7 App Contest 明文'经第三方 API 接入生成取消参赛资格'，说明 API 用户与平台用户是两个世界；9/16 才发第一波 API 教程
  - 切入：做双轨路由与实测对比：同一 prompt/参数在订阅 credits（MCP/CLI）与 console API 两条轨上跑成本/延迟/质量实测并发布对比数据，CLI 里做 `--track subscription|api` 自动选便宜轨——帮开发者把'坑'变成可计算的决策
- **两家都没有确定性评测与回归基准**
  - 证据：Runway/Higgsfield 的 changelog 与博客全是能力宣传：无公开 eval 集、无 seed 复现说明、无参数稳定性承诺、无模型间横向基准；Higgsfield skills 的'质量'靠 anti-slop 提示词约定，Runway 靠 recipes 人工经验
  - 切入：建跨厂商提示词回归集：固定 prompt+seed+参数定期跑分，发布横向对比报告（成本/时长/一致性），以 CLI 插件形式让用户在自家场景上跑私有基准——评测是厂商不便自证、第三方最有话语权的空位
- **两家技能层都缺 agent 输入校验与产物契约**
  - 证据：Runway skills 要求预充值 $10 + 环境变量即用，无输入 schema 校验层；Higgsfield 技能直接产出网站/游戏成品但无产物 manifest（部署 URL、资产清单、成本记录均不落盘）——agent 管线断点恢复和审计无从做起
  - 切入：把 JSON contract 层做成两家 skills 之上的公共包装器：统一输入校验、产物 manifest、断点恢复与重放——这正是把已有工程实践（agent 输入/恢复/产物契约硬化）产品化为跨厂商中间层

### 未解问题

- Higgsfield《Higgsfield Unlimited MCP》（7/28 博文）的具体权益边界（覆盖哪些模型、是否限速、与 All Unlimited 的关系）未能验证——目标 URL 404，真实 slug 未知
- runway-characters-meet 仓库的实际用途（是新角色产品 GWM-1 的落地页还是开源工具）未读取内容，角色方向信号目前仅靠入库时间与 avatars-sdk-react 代号推断
- Higgsfield console API 与订阅 credits 是否完全隔离、有无互通额度或促销，未从一手定价文档确认（pricing 页 JS 渲染抓不到）
- Runway skills 安装要求的 '$10 prepay' 是最低充值还是月费、RUNWAYML_API_SECRET 与平台订阅 credits 的关系未验证
- Higgsfield CLI 8 月零提交是团队人力转移还是单纯稳定期，无法从外部仓库证据区分；若为前者，CLI 生态位可能被官方进一步边缘化
- Runway 开源 MCP（runway-api-mcp-server）与闭源产品内 Agent MCP 的功能边界（Workflows 仅在后者）未来是否会收敛，无官方表态

### 来源

- [Runway API Changelog（docs.dev.runwayml.com）](https://docs.dev.runwayml.com/api-details/api_changelog/)
- [Runway 产品 Changelog](https://runway.com/changelog)
- [runwayml/skills 仓库（runway-dev-* 技能族）](https://github.com/runwayml/skills)
- [runwayml/skills 提交历史（8/28 唯一路径重构）](https://github.com/runwayml/skills/commits/main/)
- [runwayml/runway-api-mcp-server（9 工具 MCP）](https://github.com/runwayml/runway-api-mcp-server)
- [runwayml org 仓库列表（63 仓库）](https://github.com/orgs/runwayml/repositories)
- [Runway Careers（Founding DX Lead、Dev Platform、Robotics、Japan）](https://runway.com/careers)
- [Higgsfield 产品 Changelog（计费/MCP/CLI 条目）](https://higgsfield.ai/changelog)
- [higgsfield-ai/cli 仓库](https://github.com/higgsfield-ai/cli)
- [higgsfield-ai/cli 提交历史（8 月空窗）](https://github.com/higgsfield-ai/cli/commits/main/)
- [higgsfield-ai/cli Releases（v1.1.17–v1.1.26）](https://github.com/higgsfield-ai/cli/releases)
- [higgsfield-ai/skills 仓库（应用工厂技能矩阵）](https://github.com/higgsfield-ai/skills)
- [higgsfield-ai/skills 提交历史（7/8–9/11）](https://github.com/higgsfield-ai/skills/commits/main/)
- [Higgsfield MCP 页（免 API key、7+ 客户端、FAQ 计费）](https://higgsfield.ai/mcp)
- [Higgsfield CLI 页（'same credit system' 表述、35 技能）](https://higgsfield.ai/cli)
- [Higgsfield Blog（9/16 API 三连发、9/10 与 9/15 计费解释文、9/7 GPT-6 Astra）](https://higgsfield.ai/blog)

---

## 第二梯队（Pika / MiniMax / Vidu / Kling / Luma / ElevenLabs）

90 天内六家分成三个梯队：MiniMax 与 ElevenLabs 已建成官方全栈 agent 面（MCP+CLI+skills，且 ElevenLabs 完成“本地 MCP→托管 MCP、REST 示例→CLI”的架构切换）；可灵与 Vidu 是最关键的刚入场者——可灵 6/15 才建 skills 仓、8 月 10 天内连发 Claude/Cursor/WorkBuddy 三端官方 plugin 并上线托管 MCP（klingai.com/mcp，官方优先推荐 CLI），Vidu 7 月推出 OpenClaw 系官方 Vidu Agent 并高频维护 vidu-skills（但官方 vidu-mcp 已停更 15 个月）；Luma 停在 API+官方 CLI 层（CLI 默认分支自 6/9 停更），其“Luma Skills”是产品内工作流而非可安装 agent 技能，全站无 MCP；Pika 转型 API Club 聚合门户（OpenAPI 3.1+llms.txt+/agent 提示词页），无任何协议级集成。统一 CLI 的下一步方向：provider 适配器优先对准“官方 API 强、agent 面空白”的 Luma Agents API 与国际版 Kling API。最大空位：可灵的 agent 集成被锁在中国消费者会员生态（klingai.com 中文+会员计费），国际开发者门户 kling.ai/document-api 零 agent 集成；且全行业没有跨厂商统一契约——成本预估仅 Vidu 一家实现，这正是 contract-first 多厂商 CLI 的入口。

### 近 90 天时间线

- **2026-06-24** — Vidu：官方 vidu-cli 与 vidu-skills 同日更新至 v1.4.15（TTS/唇同步/字幕能力）；vidu-cli 为 npm 分发的官方命令行（https://github.com/shengshu-ai/vidu-skills）
- **2026-07-02** — Vidu：同日创建 vidu-s-api（Vidu-S 实时交互数字人 API 的集成指南与技能）与 openclaw-vidu-s（OpenClaw 集成）；官方 Vidu Agent（自称首个基于 OpenClaw 的营销 agent，由 Vidu Q3 驱动）于 vidu.com/vidu-claw 上线（https://github.com/shengshu-ai/vidu-s-api）
- **2026-07-07** — 可灵：kling-cli 消费者技能升级 v0.1.3（响应字段统一 camelCase）；该 skills 仓 6/15 才创建（自述“kling-skills 分发镜像仓”），90 天内持续演进（https://github.com/klingai-tech/skills）
- **2026-07-10** — Luma：docs.lumalabs.ai 更新 Dream Machine API→Luma Agents API 迁移通知；新文档站（docs.agents.lumalabs.ai）提供 llms.txt 与每页 .md，含 Ray3.2/uni-1 路由与 video_edit/reframe 端点，但无任何 MCP/skills 章节（https://docs.lumalabs.ai）
- **2026-08-05 至 08-14** — 可灵：10 天内连发三个官方 plugin 仓——cursor-plugin（08-05）、workbuddy-plugin（08-06）、claude-plugin（08-13），完成 Claude/Cursor/WorkBuddy 三端覆盖（https://github.com/klingai-tech/claude-plugin）
- **2026-08-06** — Luma：官方上架第三方模型“MiniMax H3 Available Now”与“Seedance 2.5: Now Live in Luma”，平台转向模型聚合/路由（https://lumalabs.ai/news）
- **2026-08-15** — MiniMax：开源视频模型 MiniMax-H3（原生立体声、2K/15s、开源权重），仓库自带 9 个技能（含 Prompt Writing Skill），后续发布 awesome-minimax-h3-integration 生态列表（09-17）（https://github.com/MiniMax-AI/MiniMax-H3）
- **2026-08-20** — ElevenLabs：归档本地 elevenlabs-mcp，切换到托管 MCP（https://api.elevenlabs.io/v1/mcp，OAuth 授权），README 明示本地版由托管版取代（https://github.com/elevenlabs/elevenlabs-mcp）
- **2026-08-25** — ElevenLabs：官方 skills 仓库将全部 REST 示例改为 CLI 调用（提交信息：“The ElevenLabs CLI just shipped”）；随后 09-01 增加 npm 安装选项、09-07 增加 Cursor 托管 MCP connector 配置、09-09 再从 changelog 同步技能（https://github.com/elevenlabs/skills）
- **2026-08-21 至 09-19** — MiniMax：mmx-cli 五个版本（v1.0.22→v1.0.26）：08-31 自动安装缺失的 coding agents、09-02 检测 Codex runtime、09-19 新增语音转写 asr-1.0；CLI 本身可用 npx skills add MiniMax-AI/cli 作为 agent 技能安装，支持双区 API（https://github.com/MiniMax-AI/cli）
- **2026-09-10** — 可灵：kling-cli skill v0.2.0，新增主体库与动作控制（对齐 3.0 系模型能力）；09-11 workbuddy-plugin 跟进更新（https://github.com/klingai-tech/skills）
- **2026-09-14 至 09-20** — Vidu：vidu-s-api（09-14）、openclaw-vidu-s（09-15）、vidu-skills（09-18，更新 vidu.cn/vidu.com 双区 token 文档）、Vidu-S 主仓（09-20）密集推送（https://github.com/shengshu-ai/vidu-skills）
- **2026-09-18** — ElevenLabs：skills 仓库最后一次推送（90 天内第 5 次从 changelog 自动同步，最后一次同步 09-07 changelog）（https://github.com/elevenlabs/skills）
- **2026-09-20** — Pika：官网主推 API Club 聚合门户（dev.pika.art：固定目录、provider 托管、REST+OpenAPI 3.1+llms.txt+/agent onboarding 提示词页、micro-USD 预付费报价、无免费层），全站无 MCP/CLI/skills；同日 api-evangelist 档案更新确认其主域无第一方生成 API（https://dev.pika.art）
- **2026-09-21** — MiniMax：开源终端编码 agent minimax-code（约 1.7k stars），agent 战略从“被 agent 调用”扩展到“自带 agent 运行时”（https://github.com/MiniMax-AI/minimax-code）
- **90 天内（负证据）** — Luma：官方 luma-agents-cli 默认分支最后 commit 停在 2026-06-09（v0.3.0），窗口内零动作；旧官方 luma-api-mcp 停更于 2025-04 且指向已废弃 API；官方 MCP/可安装 skills 均不存在（https://github.com/lumalabs/luma-agents-cli）
- **90 天内（负证据）** — Vidu：官方 vidu-mcp 停更于 2025-06-26，未覆盖 Q3/Vidu S 新能力；可灵国际站 kling.ai/document-api（Kling 3.0 Omni/Turbo、Motion Control、Virtual Try-On）全站无 MCP/CLI/skills 入口，agent 集成仅存在于 klingai.com 中国消费者站（https://github.com/shengshu-ai/vidu-mcp）

### Roadmap 信号

- **可灵 agent 生态将加速扩张：klingai-tech org 6-9 月连续创建 4 个仓库，9/10 的 skill v0.2.0 刚加入“主体库与动作控制”（与 3.0 系模型能力同步），commit 节奏跟随模型发布；下一步大概率覆盖 3.0 Omni 全部能力并补国际版**（置信：官方明示；https://github.com/klingai-tech/skills）
- **MiniMax 走向“自带 agent 运行时”：mmx-cli 七周五个版本（自动安装 coding agents、检测 Codex runtime）+开源 minimax-code+H3 仓库自带 9 技能，从被调用方进化为运行时提供方**（置信：官方明示；https://github.com/MiniMax-AI/cli）
- **托管 MCP（OAuth、零本地配置）取代本地 stdio MCP 成为默认：ElevenLabs 8/20 归档本地 MCP 切换 api.elevenlabs.io/v1/mcp；可灵直接以托管端点 klingai.com/mcp+提示词分发；MiniMax 亦有官方 MCP 双实现**（置信：多源交叉；https://github.com/elevenlabs/elevenlabs-mcp）
- **Luma 平台化聚合第三方模型（8/6 上架 MiniMax H3 与 Seedance 2.5），向模型路由演进；但官方对 MCP/agent skills 零表态，agent 面短期大概率继续缺位**（置信：推断；https://lumalabs.ai/news）
- **Vidu 押注 OpenClaw 生态而非 MCP：vidu-claw 官方营销 agent+openclaw-vidu-s+skills 均只提 Vidu Agent/OpenClaw/Claude Code，官方 vidu-mcp 一年未动——出现中国厂商“OpenClaw 优先”路线**（置信：推断；https://www.vidu.com/vidu-claw）
- **Pika 以 agent 友好文档替代协议集成：llms.txt+/agent onboarding 面向 coding agent 的 API 消费，但目录固定、provider 托管、无自有算力出口，短期不会出现第一方模型专用 agent 工具**（置信：推断；https://dev.pika.art）

### 做得好的

- MiniMax 全栈样本：官方 MCP（Python+JS 双实现，7 个工具含 generate_video）、mmx-cli 明确“为 AI agent 构建”（npm 分发、npx skills add 安装、双区 api.minimax.io/api.minimaxi.com、自动检测 Codex/Claude 等运行时）、开源 H3 仓库自带 9 个技能——把 fal 式“CLI 即运行时”推到极致
- ElevenLabs 工程纪律：每 5-10 天把 changelog 自动同步进 skills 仓；托管 MCP+OAuth 消灭本地配置；CLI 定位“Agents as Code”（agent 配置文件化+全 API 子命令）；skills 仓内置 evals
- 可灵消费者 agent 化打法：一句中文提示词让任意 agent 自动配置托管 MCP（klingai.com/mcp）并完成授权；npx skills add 一行分发（声明支持 40+ agent）；三端 plugin+电商/短剧/门店三场景视频教程
- Vidu skills 实用性最强：提交前成本估算（cost estimation）、配额/积分查询、vidu.cn/vidu.com 双区 token 文档、同一技能适配 Vidu Agent/OpenClaw/Claude Code 三运行时
- Luma 文档对机器最友好：llms.txt+每页 .md+Python/TS/Go 三语言 SDK+官方 Go CLI；Agents API 的 uni-1 统一路由与 video_edit/reframe 端点设计值得契约层借鉴
- Pika 的 agent 友好文档：公开 OpenAPI 3.1 规范+免鉴权实时报价目录（micro-USD 计价）+专门的 /agent onboarding 提示词页

### 空位与切入姿势

- **Luma Agents API 无官方 MCP、无可安装 agent skill，官方 CLI 停更超过 3 个月**
  - 证据：docs.agents.lumalabs.ai（2026-07-10 更新版）全站无 MCP/skills 章节；github.com/lumalabs/luma-agents-cli 默认分支最后 commit 2026-06-09（v0.3.0）；官方 luma-api-mcp 停更于 2025-04 且指向已废弃的旧 Dream Machine API
  - 切入：独立维护 luma-agents-mcp：封装 Ray3.2 生成+video_edit/reframe/uni-1 路由（异步轮询+presigned 下载语义清晰），并按 agentskills.io 规范发布可 npx skills add 安装的技能，正好补上 MiniMax-MCP/vidu-mcp 在 Luma 的空位；CLI 维护真空可由 fork+补 release 占位
- **可灵 agent 集成只覆盖中国消费者会员生态，国际开发者 API 门户零 agent 面**
  - 证据：klingai.com/app/mcp 为中文页面、FAQ 围绕会员计费与充值，托管端点 https://klingai.com/mcp 面向消费者账号；而国际门户 kling.ai/document-api（Kling 3.0 Omni/Turbo、Motion Control、Virtual Try-On 完整 REST 文档）全站无 MCP/CLI/skills；GitHub 上 klingai-tech 四仓均为中文消费者侧，国际版 key 用户无任何 agent 工具
  - 切入：为国际版 API（kling.ai key 体系）做双语 skill+MCP：复刻 vidu-skills 的双区模式（vidu.cn/vidu.com 各自 token），第一批占位国际版 Kling agent 集成；官方中文 kling-cli 不认国际 key，两端用户都缺工具
- **Vidu 官方 MCP 停更 15 个月，Q3（16s 音视频）与 Vidu S（实时交互）新能力无 MCP 覆盖**
  - 证据：github.com/shengshu-ai/vidu-mcp pushed_at 2025-06-26；同期 vidu-skills（2026-09-18）、vidu-s-api（09-14）、openclaw-vidu-s（09-15）高度活跃，说明官方资源押在 skills/OpenClaw 侧，协议层被放弃
  - 切入：社区 vidu-mcp 复活：直接包一层官方维护的 npm vidu-cli 为 MCP server，自动继承其能力表（含独家成本估算），零 API 维护成本补上官方不做的协议层
- **Pika 无第一方生成 API 出口，自有模型（Pika 2.5、Soundtrack/Music/SFX）只能经聚合门户或 fal 访问，且无任何协议级 agent 集成**
  - 证据：dev.pika.art 自述“The catalog is fixed and provider-hosted”、无免费层；pika.art 全站无 MCP/CLI/skills；api-evangelist/pika-labs（2026-09-20 更新）确认主域无第一方 REST API，历史上经由 fal.ai 等聚合器
  - 切入：在统一 CLI 中把 Pika API Club 做成一个 provider 适配器——它公开 OpenAPI 3.1+llms.txt+免鉴权实时报价目录，contract 可自动生成，是六家中接入成本最低的多模型聚合源；顺带覆盖其目录里的 Seedance 2.5/Wan 3.0/H3 等第三方模型
- **全行业无跨厂商统一视频生成契约；提交前成本预估仅 Vidu 一家实现**
  - 证据：六家异步语义各异：Luma 任务+presigned URL、MiniMax /v2/video_generation+/query 轮询、Pika job+签名 webhook+micro-USD 报价、可灵消费者 MCP 与开发者 API 双体系、Vidu 双区 base URL；各官方 CLI/MCP 均只封装自家，无一家做跨厂商抽象
  - 切入：用户在建的 contract-first 多厂商 CLI 就是空位本身：以 Vidu cost estimation 与 Pika micro-USD 报价为参照，实现“提交前跨厂商报价+统一任务/轮询/下载契约”，再用单个 skill（npx skills add）同时分发到 40+ agent——任何官方单厂商技能都做不到这一点
- **可灵官方 skills 仓库只是极简分发镜像，“能装但没教”**
  - 证据：github.com/klingai-tech/skills README 全文仅一行安装命令（npx skills add klingai-tech/skills），自述“分发镜像仓”；官方配套只有 3 个场景视频教程，无文本工作流、无最佳实践库
  - 切入：第三方深度工作流技能库：分镜/多镜头一致性/主体库批量/动作控制组合玩法，补官方镜像仓之上的方法论层——这是“技能即文档”（AtlasCloud 式）哲学尚未被任何视频厂商占据的位子
- **ElevenLabs 式“changelog→skills 自动同步”纪律在视频厂商中零复制**
  - 证据：elevenlabs/skills 90 天内 5 次以“Update skills from changelog”为名的同步提交；而 Kling 3.0 Omni、MiniMax H3、Vidu Q3 等新模型能力均未同步进各自技能（可灵 skill v0.2.0 仅到主体库/动作控制，H3 未进 MiniMax-MCP 的 generate_video 工具清单）
  - 切入：对独立 CLI 项目本身：建立“厂商 changelog→provider 契约→skill 再生成”自动化管道作为差异化卖点——新模型发布一处更新、多厂商技能同时生效，这是 Sixty 四家官方都没做的元能力

### 未解问题

- klingai.com/mcp 托管端点的工具清单、鉴权细节与计费口径（会员积分还是 API 费用）未公开文档化——页面仅提供提示词与 FAQ
- 可灵国际版（kling.ai）是否会获得与 klingai.com/app/mcp 同等的 agent 入口；klingai-tech 四仓均面向中文消费者侧
- MiniMax mmx-cli 的 video generate 当前支持的模型清单：H3/H3-Max 是否已进入 CLI 与官方 MCP 的工具参数（官方 MCP 文档仍写 Hailuo-02）
- Luma Agents API 的 GA 时间线与是否有 MCP/可安装技能计划（官方新闻与文档零表态）
- shengshu-ai/vidu-mcp 会被复活，还是被 vidu-cli+skills 路线正式取代
- Pika API Club 的上线日期与其自有模型（Pika 2.5）是否经此出口——页面无任何日期信息
- 可灵 skills 仓自述“分发镜像仓”，其上游原始仓库（kling-skills）位置不明，难以追踪真实发版节奏

### 来源

- [MiniMax-AI/MiniMax-MCP（官方 MCP，7 工具含 generate_video）](https://github.com/MiniMax-AI/MiniMax-MCP)
- [MiniMax-AI/cli（mmx-cli，为 AI agent 构建的官方 CLI，可作技能安装）](https://github.com/MiniMax-AI/cli)
- [MiniMax-AI/MiniMax-H3（开源视频模型，自带 9 技能）](https://github.com/MiniMax-AI/MiniMax-H3)
- [MiniMax 平台视频生成文档（H3/H3-Max 异步 API，llms.txt）](https://platform.minimax.io/docs/guides/video-generation)
- [elevenlabs/elevenlabs-mcp（已归档，README 指向托管 MCP）](https://github.com/elevenlabs/elevenlabs-mcp)
- [elevenlabs/skills（官方技能仓，changelog 同步记录）](https://github.com/elevenlabs/skills)
- [elevenlabs/cli（Agents as Code 官方 CLI）](https://github.com/elevenlabs/cli)
- [可灵官方 MCP/CLI/Skill 入口页（托管端点 klingai.com/mcp，npx skills add klingai-tech/skills）](https://klingai.com/app/mcp)
- [klingai-tech/skills（可灵官方技能分发镜像仓，v0.2.0 于 09-10）](https://github.com/klingai-tech/skills)
- [klingai-tech/claude-plugin（可灵官方 Claude 插件，08-13 创建）](https://github.com/klingai-tech/claude-plugin)
- [kling.ai 国际开发者门户（Kling 3.0 Omni/Turbo API，无 agent 集成）](https://kling.ai/document-api/guides/get-started/overview)
- [shengshu-ai/vidu-skills（Vidu 官方技能，含成本估算与双区文档）](https://github.com/shengshu-ai/vidu-skills)
- [shengshu-ai/vidu-mcp（Vidu 官方 MCP，2025-06 后停更）](https://github.com/shengshu-ai/vidu-mcp)
- [Vidu Agent（基于 OpenClaw 的官方营销 Agent）](https://www.vidu.com/vidu-claw)
- [docs.agents.lumalabs.ai（Luma Agents API 文档，无 MCP/skills）](https://docs.agents.lumalabs.ai)
- [lumalabs/luma-agents-cli（官方 CLI，2026-06-09 后停更）](https://github.com/lumalabs/luma-agents-cli)
- [Luma 新闻页（Ray3.2、Luma Skills、MiniMax H3 上架时间线）](https://lumalabs.ai/news)
- [Luma Skills 公告（产品内工作流技能，2026-06-16）](https://lumalabs.ai/news/luma-skills)
- [dev.pika.art（Pika API Club 聚合门户：OpenAPI 3.1+llms.txt+/agent onboarding）](https://dev.pika.art)
- [api-evangelist/pika-labs（第三方 API 面档案：主域无第一方 REST API）](https://github.com/api-evangelist/pika-labs)

---

## 开发者需求侧（90 天社区信号）

近 90 天开发者吐槽呈三条主线：一是 fal 的计费/账户信任黑洞——同一个"余额充足仍自动锁号"bug 三个月内至少 7 个 issue（充值即锁、工单无人回、一笔 10,272 秒误计费直接变成 $40,500 并吞掉充值），且官方修 SDK 代码很快、对计费集群却零处理；二是 Higgsfield 的 agent 集成质量欠账——MCP OAuth 对 Claude Code 等客户端断了 5 周（官方两次宣称修复、用户 9/19 仍在复现）、MCP 生成工具广告不透明 schema、官方 skills 过不了 Codex 校验；三是结构性痛点"同模型跨厂商价差 5-10 倍 + 提交无幂等"——已有创业者连发两次 Show HN 做 VideoRouter，还有开发者想在 Higgsfield CLI 上造预算管控系统却连"一次调用是否恰好一个计费任务"都问不到。厂商侧动向是 Runway 把 Dev MCP 收敛为唯一集成路径并上线 Model Routers/自动计费，MiniMax 和 Luma 冲进 CLI/多语言 SDK 战场。最大空位：所有厂商都缺"计费可信层"（预算硬上限、幂等提交、账单对账、误计费防护）——这是吐槽最密、已有开发者被迫自建、而厂商因利益冲突结构性不会做的一层，独立开发者可以用一个本地"预算闸门 + 任务对账"CLI 切入。

### 近 90 天时间线

- **2026-08-13** — MiniMax 生态信号：MiniMax-AI/awesome-minimax-h3-integration 创建（376★），社区开始围绕 H3 开源权重自发攒集成资料（https://github.com/MiniMax-AI/awesome-minimax-h3-integration）
- **2026-08-14** — Higgsfield Python SDK：upload_file() S3 上传 100% 失败（缺 x-amz-tagging 头），与 CLI #65 同根因（https://github.com/higgsfield-ai/higgsfield-client/issues/2）
- **2026-08-15** — fal #1147：确认充值 $10 后账户仍被锁 Exhausted balance，自述与更早的 #914/#922 同根因，只能发帖求人工解锁（至今 open）（https://github.com/fal-ai/fal/issues/1147）
- **2026-08-17 ~ 2026-09-19** — Higgsfield CLI MCP OAuth 断裂集群（#67/#68/#70/#75/#76）：RFC 9207 issuer 不匹配导致 Claude Code/Codex 全部无法完成 MCP 认证；#68 积 7 条评论、多人跨 5 周复现——官方 9/3 称已修复，9/5、9/13、9/19 用户仍在复现（https://github.com/higgsfield-ai/cli/issues/68）
- **2026-08-24 ~ 2026-08-25** — Higgsfield CLI 整个 website 命令面返回 Session expired（#71/#72），marketplace 内部 x-api-key 被拒（https://github.com/higgsfield-ai/cli/issues/71）
- **2026-08-27** — Higgsfield 官方 changelog 承认当日 Higgsfield MCP 调用大面积失败并修复——官方亲自确认了 agent 集成面的脆弱（https://higgsfield.ai/changelog）
- **2026-08-28** — Runway 官方 skills 仓库重构：'make Dev Platform skills sole integration path'（#19/#20），把托管 Dev MCP（dev.runwayml.com/mcp）定为唯一 agent 集成路径（https://github.com/runwayml/skills）
- **2026-08-31 ~ 2026-09-04** — Higgsfield changelog 密集上新：MiniMax H3 Max（768p 换速度）、Gemini Omni 1.1 Flash、Genjutsu 对象替换、Scale 档'无限模型'（首购后仅 7 天无限）——模型路由面持续扩张（https://higgsfield.ai/changelog）
- **2026-09-03 ~ 2026-09-04** — Runway sdk-python 发 5.20.0：新增模型、图像选项与 audit-log actions（Stainless 生成式 SDK 持续演进）（https://github.com/runwayml/sdk-python）
- **2026-09-04** — Higgsfield CLI #80：官方 skills 无法通过当前 Codex 的 frontmatter 校验——官方 skill 质量跟不上客户端演进（https://github.com/higgsfield-ai/cli/issues/80）
- **2026-09-05 ~ 2026-09-21** — fal 锁号集群爆发期：#1162（充值后锁）、#1163（余额 $110.83 仍锁、扣费照走）、#1168（$47.40 余额被锁、客服无回应）、#1172（Solana USDC 到账不入账）、#1183（新号首充即锁，工单一周无人回）——同一 bug 五周内至少 4 个新 issue（https://github.com/fal-ai/fal/issues/1163）
- **2026-09-09** — fal-js #238：queue.submit() 无视 retry.maxRetries=0、传输错误后重放提交 POST——重复生成/重复扣费风险的精确报告，12 天 0 官方回复（https://github.com/fal-ai/fal-js/issues/238）
- **2026-09-10 ~ 2026-09-14** — runwayml 四个仓库（sdk-python/sdk-node/skills）被同一用户 30+ 条无分诊 issue 淹没，其中两条正文直接贴出明文 API key（sdk-node #205/#222），官方零分诊、零回复（https://github.com/runwayml/sdk-node/issues/222）
- **2026-09-11** — VideoRouter 首次 Show HN：'同一底层视频模型在不同 provider 价差 5-10 倍'，做统一 API 按price/availability 路由——供给侧创业者对'价格不透明'的真金白银投票（https://news.ycombinator.com/item?id=49667080）
- **2026-09-16 ~ 2026-09-17** — VideoRouter 换文案再发（'OpenRouter for video and image generation APIs'）；同日 HN 用户追问 Seedance 2.5 的 reference images/角色一致性是否可用、无人能答；fal #1175：80 秒视频被记 10,272s 执行时长、误扣 $40,500 并锁号吞掉 $100 自动充值（https://news.ycombinator.com/item?id=49733974）
- **2026-09-19 ~ 2026-09-21** — Higgsfield CLI #91：开发者自建'生成审批+预算管控系统'，被迫开 issue 公开求计费语义（一次调用=几个计费任务？有无幂等键？）；#93：MCP generate_video 广告空 schema、校验却要求嵌套 params，schema 驱动客户端 100% 失败；fal #1183 新号首充即锁；MiniMax CLI #249 中文开发者求配额 API 返回小数（当前整数百分比把 2.8% 显示成 3%）（https://github.com/higgsfield-ai/cli/issues/91）

### Roadmap 信号

- **Runway 把托管 Dev MCP（dev.runwayml.com/mcp）定为唯一 agent 集成路径，skills 只负责教接入；配套文档新增 Model Routers（模型路由 API 化）与 Usage & Billing / Autobilling / Usage tiers 章节**（置信：官方明示；https://github.com/runwayml/skills）
- **Runway 产品与 ARR 双线扩张（9/8 HN 帖 'Runway Reaches 200M ARR'），集成面从生成向工具调用/虚拟形象/会议摄像头延伸（Tool calling、Custom Voices、Avatars SDK）**（置信：多源交叉；https://docs.dev.runwayml.com/）
- **Higgsfield 持续加码'聚合路由'定位：changelog 近 90 天密集接入第三方旗舰模型（MiniMax H3 Max、Gemini Omni 1.1 Flash、Recraft V4、GPT-6 Astra），导航常驻 MCP API 与 ChatGPT Plugin 入口**（置信：官方明示；https://higgsfield.ai/changelog）
- **MiniMax 全面转向 agent 终端分发：官方 CLI 高频发版、官方插件注册表、H3 开源权重带动 8/13 新建的 376★ 社区集成库——它在复制 fal 的'CLI 即运行时'路线并用开源权重补内容面**（置信：多源交叉；https://github.com/MiniMax-AI/cli）
- **Luma 新开 Agents 产品线并一次补齐四语言 SDK（含 Go），从 Dream Machine SDK 切换重心**（置信：官方明示；https://github.com/lumalabs/luma-agents-cli）
- **fal 处于资本扩张期（HN 8/16 评论：估值 $8b、流量不及 OpenRouter 却更高估值；8/29 评论指其单日 $4,000 赞助渲染），但计费信任问题集群全部挂起未动**（置信：多源交叉；https://news.ycombinator.com/item?id=49324121）
- **Higgsfield 5.6k★ '核心仓库开源'（HN 9/17 有人发帖质疑动机）更像 GitHub 品牌运营：仓库 created 2018、描述是 GPU 训练框架，与视频生成核心无关**（置信：推断；https://news.ycombinator.com/item?id=49744855）

### 做得好的

- Runway：文档即接口的标杆——docs.dev.runwayml.com 每页自带 'Copy for LLM / View as Markdown / Open in Claude / Connect to Cursor'，Dev MCP 是 Get Started 一等公民；8/28 果断把 skills 收敛为 Dev Platform 单一集成路径，主动消灭碎片化
- Runway：SDK 工程化成熟——Stainless 生成的 sdk-python/sdk-node 持续发版（9/3-9/4 发 5.20.0：新模型+audit-log actions），另有 openapi 仓库对外开放规格
- fal：代码层响应极快——#1146 的 multipart 上传 bug（8/14 报）9/16 修复（#1170）、#1165 端口冲突（9/10 报）9/21 修复（#1166），还给 CLI 加了 backup domains（9/18）提升弱网可用性
- Higgsfield：agent 全家桶铺货速度罕见——CLI（569★）+ skills（1087★）+ JS/Python 双 SDK + cursor-plugin + Homebrew tap 全在近两周内有 push，且官方 changelog 连 MCP 故障都公开披露
- MiniMax：终端+开源组合拳——MiniMax-AI/cli（2168★，2026-03 创建、9/19 仍在 push）配官方插件注册表 MiniMax-Code-Plugins 和社区 awesome 库，中文 issue 区有真实维护者响应（#254 附提交关闭）
- Luma：9/17 同日 push luma-agents-cli 与 ts/python/go 三个 SDK 仓库，Go 官方 SDK 在视频厂商中少见
- 厂商集体在把'能被 agent 调用'当作一级发布物（CLI/MCP/skills/插件注册表），说明独立开发者做兼容层/对齐层的时机窗口正开着

### 空位与切入姿势

- **计费可信层整体缺位（最大空位）：没有任何厂商提供预算硬上限、自助解锁、误计费防护与账单对账**
  - 证据：fal 同一根因的锁号 issue 横跨 3 个月至少 7 条（#914/#922/#1147/#1162/#1163/#1168/#1183），充值即锁、客服一周不回、$40,500 误计费直接吞充值（#1175）；需求强度最强：同一 bug 五周内 4 个新 issue，用户除了公开求人工解锁毫无手段
  - 切入：做本地'预算闸门'sidecar/CLI 插件：per-job 成本预估、硬性花费上限（超限熔断）、本地账本逐条核对执行时长↔扣费（#1175 那种 10,272s→$40,500 在本地立即拦截）、月度对账单导出。先支持 fal（痛点最深），再扩 Higgsfield/MiniMax
- **提交无幂等、任务语义不透明：厂商都没回答'一次调用是否恰好一个计费任务、超时后是否重试'**
  - 证据：fal-js #238：queue.submit 无视 maxRetries=0、传输错误后重放 POST（重复扣费风险，官方 12 天未回）；Higgsfield CLI #91：开发者为给公司造审批+预算管控系统，被迫在 issue 区问幂等键与计费语义——需求强度的直接证据是有人已经动手自建这层
  - 切入：跨厂商 job orchestrator：统一任务表、幂等提交键、webhook 事件归一、断点恢复、失败重试策略显式化，定位'视频生成的轻量任务层'，CLI 优先、可被 CI/agent 调用
- **agent 集成质量无对齐层：官方 MCP/skills 在真实客户端里大规模不可用，且无人做跨客户端一致性验证**
  - 证据：Higgsfield MCP OAuth 对 Claude Code 断 5 周（#67/#68/#75/#76，官方称修复后 9/19 仍复现）；MCP generate_video 广告空 schema 导致 schema 驱动客户端 100% 失败（#93）；官方 skills 过不了 Codex 校验（#80）；Windows 路径引号 bug（#83）；安装脚本不校验和（#69/#73）。Runway 侧则是 SDK 仓库 30+ issue 零分诊、明文 key 无人处理
  - 切入：维护一套在 Claude Code/Codex/Cursor 三端实测过的视频生成 MCP + skills 套件，公开 conformance 测试矩阵和认证结果——把 Higgsfield 自己的'evals 哲学'反过来评测所有厂商的 agent 面；顺带吃下 OAuth/Windows 这类脏活的信任红利
- **价格不透明、路由不可控：同一模型在不同渠道价差 5-10 倍，且开发者无法知道扣费怎么算出来的**
  - 证据：VideoRouter 创始人 9/11 与 9/16 两度 Show HN 主打'同模型价差 5-10 倍'；Higgsfield 的'unlimited'档藏着'首购后仅 7 天无限'条款，CLI #91 的作者连'能否自动走免费额度'都要开 issue 问
  - 切入：不做全量代理（撞巨头），做'路由回执+账单审计'：每次生成记录价格快照与计费依据，生成可审计的对账报告；可与预算闸门合并为同一产品的差异化能力
- **一致性控制停留在消费端，API/CLI 侧没有角色一致性工作流**
  - 证据：9/16 HN 用户追问 Seedance 2.5 的 reference images/角色设定表是否真正可用、无人能答；Higgsfield 9/1 上的消费端 Genjutsu（对象替换+30 参考图）反证需求真实；第三方 seedance-skill（Claude Code skill，4 月创建）已攒 104★ 证明分发渠道存在
  - 切入：做 character-sheet→多镜头一致性的 skill/工作流模板（参考图管理、种子与参数复现、跨镜头身份锁定），以 Claude Code skills 形式发布，蹭 Runway/Higgsfield skills 生态的分发位
- **SDK 语言矩阵缺口：头部视频厂商里 Kling 官方 GitHub 近乎空壳，多数厂商只有 JS/Python**
  - 证据：kling-ai 组织仅有 .github 一个仓库且 2025-03 后无任何 push；Luma 直到 9/17 才补 Go；fal 官方只有 JS/Python/Swift（React Native 只是示例仓库）
  - 切入：给无 SDK 厂商做 OpenAPI→多语言（Go/Rust/Kotlin）生成与类型契约发布——对标 Runway 用 Stainless 的做法把它带给缺位厂商；也可并入统一 CLI 作为底层库
- **配额/用量可观测性粗糙：积分余量、重置时间、扣费明细的粒度都不够开发者用**
  - 证据：MiniMax CLI #248/#249（中文开发者）：配额 API 只回整数百分比（2.8% 显示成 3%）、求小数与重置倒计时，官方 API 端点 /v1/token_plan/remains 精度不足；Runway SDK issues 里全是无上下文的裸错误（PermissionDeniedError 等）
  - 切入：跨厂商用量仪表盘/费用告警 CLI（进度条级配额、按模型/项目的成本归集），作为预算闸门产品的轻量入口；单独做太薄，建议并入第一条

### 未解问题

- Reddit 三个版（r/aivideo、r/StableDiffusion、r/LocalLLaMA）原帖本轮未能采样：WebSearch 会话额度（200/200）已耗尽，reddit.com 直接抓取返回 'Prove your humanity' 人机验证墙——需求强度评估目前主要锚定 GitHub issues 与 HN，Reddit 侧吐槽浓度待补测
- 即刻与知乎无法程序化访问；V2EX 近 90 天相关帖多为 0 回复的作品/推广帖（含中转站送码帖，如 v2ex.com/t/1242388），中文开发者真实痛点浓度可能被低估——MiniMax CLI 中文 issue 区（#249/#259 等）是唯一已验证的中文一手吐槽源
- fal 此前调研记录的'社区 skills 仓库'（run "<prompt>" 智能路由、index.json+SHA256）本次在 GitHub fal-ai 组织下未能重新定位（组织内无 skills/agent/route 相关仓库），是否改名、转私有或内置于 CLI 待确认
- Higgsfield 5.6k★ '核心开源仓库'（created 2018，描述为 GPU 训练框架）的真实开放范围、与视频生成核心的关系、开源动作背后的运营目的
- VideoRouter 的真实采用与留存数据（HN 仅 1-2 条评论，两次发帖间隔 5 天，创始人供给端认定需求但需求侧验证缺失）
- Runway 'Model Routers' 与 Autobilling/Usage tiers 的具体 API 语义与计费规则（本轮只核对了文档目录结构，未逐页核对）

### 来源

- [fal-ai/fal #1183：新账号首充即被锁（2026-09-21）](https://github.com/fal-ai/fal/issues/1183)
- [fal-ai/fal #1175：80 秒视频被记 10,272s、误扣 $40,500 并锁号（2026-09-17）](https://github.com/fal-ai/fal/issues/1175)
- [fal-ai/fal #1163：余额 $110.83 仍被锁、扣费照走（2026-09-08）](https://github.com/fal-ai/fal/issues/1163)
- [fal-ai/fal #1147：充值后锁号，同 #914/#922 根因（2026-08-15）](https://github.com/fal-ai/fal/issues/1147)
- [fal-js #238：queue.submit 无视 maxRetries=0 重复提交（2026-09-09）](https://github.com/fal-ai/fal-js/issues/238)
- [Higgsfield CLI #68：MCP OAuth RFC 9207 断裂，5 周多人复现](https://github.com/higgsfield-ai/cli/issues/68)
- [Higgsfield CLI #93：MCP 生成工具广告空 schema（2026-09-20）](https://github.com/higgsfield-ai/cli/issues/93)
- [Higgsfield CLI #91：预算管控系统开发者公开求计费语义（2026-09-19）](https://github.com/higgsfield-ai/cli/issues/91)
- [Higgsfield CLI #80：官方 skills 过不了 Codex 校验（2026-09-04）](https://github.com/higgsfield-ai/cli/issues/80)
- [runwayml/skills：8/28 重构为 Dev Platform 唯一集成路径](https://github.com/runwayml/skills)
- [Runway Dev 文档：Dev MCP、Model Routers、Usage & Billing/Autobilling](https://docs.dev.runwayml.com/)
- [runwayml SDK 仓库 issue 分诊缺位与明文 key 泄露（2026-09-14）](https://github.com/runwayml/sdk-node/issues/222)
- [VideoRouter Show HN：同模型跨厂商价差 5-10 倍（2026-09-11）](https://news.ycombinator.com/item?id=49667080)
- [VideoRouter 再发：OpenRouter for video and image generation（2026-09-16）](https://news.ycombinator.com/item?id=49733974)
- [MiniMax CLI #249：配额百分比精度不足（中文开发者，2026-08-31）](https://github.com/MiniMax-AI/cli/issues/249)
- [Higgsfield 官方 Changelog：MCP 故障公告与模型路由扩张（2026-08~09）](https://higgsfield.ai/changelog)
- [MiniMax-AI/cli：官方多模态 CLI（2168★，2026-09-19 仍在 push）](https://github.com/MiniMax-AI/cli)
- [lumalabs/luma-agents-cli 与四语言 SDK（2026-09-17 同日 push）](https://github.com/lumalabs/luma-agents-cli)
- [HN：fal 估值 $8b 与 OpenRouter 对比讨论（2026-08-16）](https://news.ycombinator.com/item?id=49324121)
- [HN：Seedance 2.5 角色一致性（reference images/char sheets）无人能答（2026-09-16）](https://news.ycombinator.com/item?id=49734117)

---
