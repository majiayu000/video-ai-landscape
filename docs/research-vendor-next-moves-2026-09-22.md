# 前瞻调研 · 主要厂商近 90 天布局与空位（2026-09-22）

> 方法：4 路 schema 约束 agent 真实网络调研（fal / AtlasCloud / 第二梯队 / 开发者需求侧；Higgsfield+Runway 路因限流待补跑，其信号已部分由需求侧覆盖）。
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

## 第二梯队（Pika / MiniMax / Vidu / Kling / Luma / ElevenLabs）

近 90 天（2026-06-22～09-22）第二梯队的 agent 集成格局已从"提供 REST API"升级为"直接把产品面开在 agent 里"，且分化成三种打法：Pika 最激进——砍掉旧 Developer API（dk_ key 全部失效），把全部开发者入口迁到托管 MCP（mcp.pika.me，58 个原子工具、OAuth）+ 9 个 /pika:* skills + Claude/Cursor/Codex 三套插件清单；MiniMax 和 Vidu 走"CLI 即技能"——MiniMax 的 mmx-cli（9/19 仍在加 ASR 功能）自带 agent skill、双区端点，Vidu 的 vidu-cli+vidu-skills 支持 npx skills 和 ClawHub 双分发且是唯一做"提交前成本预估"的厂商；Kling 没有统一协议，而是给各个 agent 生态逐个做官方插件（openclaw 9/16、deepseek 8/31、pi 8/19），可灵官方 Skill 挂 ClawHub 但认证仍靠 AK/SK。真正的缺席者是：Luma（有官方 Go CLI 和三语言 SDK 但无 MCP 无 skills，功能开发停在 6 月 v0.3.0）和可灵/海螺的 MCP 层（可灵完全没有，海螺的官方 MCP 视频模型枚举还停在 Hailuo-02，落后于已发布的 H3）。最大的空位不在"有没有接入层"，而在接入层之上的三件事：全行业除 Vidu 外无人做生成前成本报价、除社区项目外无人做生成前校验、除 Pika 外无人把多供应商聚合做进 agent 工具面——这正是 contract-first 多供应商 CLI 可以整体占据的生态位。

### 近 90 天时间线

- **2026-06-24** — Vidu 官方 vidu-skills 发布 v1.4.15（同期 vidu-cli 以 npm+cargo 双分发），skills 支持 npx skills 与 ClawHub 双安装（https://github.com/shengshu-ai/vidu-skills/commits）
- **2026-06-25** — Pika-Labs/Pika-Experiments 推送：官方 agent 原型工作坊（'给 agent 一张脸和一个声音'），并弃用 Pika-Director-Suite（https://github.com/Pika-Labs/Pika-Experiments）
- **2026-07-15** — Pika-Skills 仓库归档：官方宣布旧 Developer API（pika.me/dev，dk_ 密钥）已停用，正在重建面向 PikaStream 1.0 的平台无关访问（https://github.com/Pika-Labs/Pika-Skills）
- **2026-07-20** — Pika-Plugins 同步 20 个漂移 skill（源自第三方 Mellis-Labs marketplace），插件含 58 工具 MCP + 9 skills + Claude 插件三表面（https://github.com/Pika-Labs/Pika-Plugins）
- **2026-07-21** — Vidu 官方 dify-plugins 推送，Dify 生态插件上线（https://github.com/shengshu-ai/dify-plugins）
- **2026-08-03～08-20** — elevenlabs-mcp 连续安全修复（本地文件越权读写）并发布 0.12.2；8/20 README 加弃用声明，指向官方托管 MCP（https://github.com/elevenlabs/elevenlabs-mcp/commits）
- **2026-08-19** — 可灵官方 klingai-dev/pi-plugin 推送，为 pi coding agent 出官方插件（https://github.com/klingai-dev/pi-plugin）
- **2026-08-20** — MiniMax-MCP 迁移 MCP SDK v2 并下线 Music 工具；同日 MiniMax 平台公告：音乐付费 API 对新用户关闭（https://github.com/MiniMax-AI/MiniMax-MCP/commits）
- **2026-08-31** — ElevenLabs 官方 CLI 升级 v1.1.0（命令级归因 User-Agent cmd/<command>）；音乐端点支持 music_v2_5（https://elevenlabs.io/docs/changelog/2026/8/31.md）
- **2026-08-31** — 可灵官方 klingai-dev/deepseek-plugin 推送，为 DeepSeek 生态出官方插件（https://github.com/klingai-dev/deepseek-plugin）
- **2026-09-11** — Vidu 官方新模型仓库 Motus2 推送（https://github.com/shengshu-ai/Motus2）
- **2026-09-14** — ElevenLabs CLI v1.3.0：API 命令加 --intent 元数据，并新增 elevenlabs feedback missing-capability 反馈命令（https://elevenlabs.io/docs/changelog/2026/9/14.md）
- **2026-09-15** — Vidu 官方 openclaw-vidu-s 推送：Vidu S 实时数字人 Avatar + 实时流编辑（风格渲染/换人/换背景/虚拟试穿）接入 OpenClaw（https://github.com/shengshu-ai/openclaw-vidu-s）
- **2026-09-16** — 可灵官方 klingai-dev/openclaw-plugin 推送（配合 ClawHub 上的 Kling AI Skill v1.1.0：意图自动路由 video/image/element）（https://github.com/klingai-dev/openclaw-plugin）
- **2026-09-17** — Luma 四个官方仓库（luma-agents-cli/-go/-python/-typescript）有推送，但最新功能提交停在 6/8 的 v0.3.0（https://github.com/lumalabs/luma-agents-cli）
- **2026-09-18** — vidu-skills 更新中国大陆（vidu.cn）与海外（vidu.com）双区 token 获取指南（https://github.com/shengshu-ai/vidu-skills/commits）
- **2026-09-19** — MiniMax mmx-cli 新增 mmx speech transcribe（asr-1.0，支持 srt/vtt/流式），仓库 2167 stars 持续高频迭代（https://github.com/MiniMax-AI/cli/commits）
- **2026-09-20** — Vidu 官方 Vidu-S 仓库推送（实时数字人/实时视频编辑模型）（https://github.com/shengshu-ai/Vidu-S）

### Roadmap 信号

- **Pika 将发布新的平台无关开发者平台（面向 PikaStream 1.0 及后续模型），官方原话'当新平台就绪时会公布更新的 API 访问、商业条款和迁移指南'——即 Pika 的 REST API 将回归，且以 agent 优先**（置信：官方明示；https://github.com/Pika-Labs/Pika-Skills）
- **ElevenLabs 接入层全面托管化：本地开源 MCP 已加弃用声明（8/20），托管 MCP（api.elevenlabs.io/v1/mcp，OAuth，CIMD，三区域端点）成为唯一官方路径；推断后续工具面会逐步从本地迁移到托管**（置信：多源交叉；https://github.com/elevenlabs/elevenlabs-mcp/commits）
- **Kling 正在多 agent 生态铺设官方插件（openclaw/deepseek/pi 三个仓库 40 天内接连推送）但始终不走 MCP 协议——推断其策略是绑定 ClawHub/OpenClaw 生态而非中立协议，短期不会出官方 MCP**（置信：多源交叉；https://github.com/klingai-dev/openclaw-plugin）
- **MiniMax 官方文档 Tip 明确引导开发者'使用 MiniMax CLI 而非 MCP'，CLI 迭代频率（近 30 天 4+ 次功能提交）远高于 MCP（8/20 后无提交）——接入层重心已从 MCP 转向 CLI+skill 分发**（置信：官方明示；https://platform.minimax.io/docs/guides/mcp-guide.md）
- **MiniMax 与 fal.ai 深度绑定：H3 Max 视频模型由 fal.ai 后训练（官方模型页原话），音乐能力转向 Hugging Face 开源（Music 3.0）——MiniMax 正把分发外包给聚合平台**（置信：官方明示；https://platform.minimax.io）
- **Luma 以'Agents API'命名其生成 API 并铺齐 CLI+三语言 SDK（2026-05-04 同日创建四个仓库），但无 MCP/skills 且功能开发停在 6 月——推断其 agent 策略是借道分销伙伴（fal、Freepik、Krea、Lovart 等 9 家已在合作列表），自有 agent 面投入在收缩**（置信：推断；https://docs.agents.lumalabs.ai）
- **Vidu 战略重心转向实时：Vidu S（实时数字人 Avatar+实时流编辑，9 月连推三仓库）+官方 OpenClaw 集成，传统异步生成接口的 agent 面（vidu-mcp）已 15 个月未更新——推断离线视频生成的接入层投入将集中在 skills 路线**（置信：多源交叉；https://github.com/shengshu-ai/openclaw-vidu-s）

### 做得好的

- Pika 的三表面分发设计：同一个托管 MCP（58 原子工具）+ npx skills（经 vercel-labs/skills 覆盖 50+ agent）+ Claude/Cursor/Codex 原生插件清单，'一次身份、一次授权、一张账单'跨所有 agent——这是目前全行业最完整的 agent 分发矩阵，值得直接对标
- MiniMax 的 CLI 即技能哲学：mmx-cli 一个二进制覆盖 text/image/video/speech/vision/search，README 第一行安装命令就是 npx skills add MiniMax-AI/cli -y -g（为 agent 而非人为优先），且双区端点（api.minimax.io / api.minimaxi.com）无缝切换；官方文档明确建议'用 CLI 代替 MCP 以获得更简单配置'
- Vidu 是唯一做'提交前成本预估'的厂商：vidu-skills 内置 Cost Estimation（video/image/TTS/lip-sync 任务提交前估算积分成本）+ 配额查询工具——把计费透明度做进了 agent 工具面
- ElevenLabs 的工程纪律：每周 changelog 节奏、CLI 有命令级归因和 missing-capability 反馈闭环、托管 MCP 用 OAuth+CIMD（'API 密钥不复制进客户端'）、EU/印度/新加坡区域端点
- Kling 的意图路由设计：官方 Skill 按用户意图自动选择 video/image/element 子命令并路由到对应 API 端点，中国/全球端点自动探测缓存
- 中国厂商的文档 LLM 化：Kling 提供 llms.txt + 每页 .md 版本（'This content is optimized for LLMs'），MiniMax 提供 171 行全量 llms.txt 索引——降低了 agent 抓取门槛

### 空位与切入姿势

- **可灵完全没有官方 MCP server——官方 agent 面只有 ClawHub Skill（AK/SK 认证）和零散的 per-agent 插件；全球流量最大的视频模型在 Claude/Cursor 里没有中立协议入口**
  - 证据：kling.ai/llms.txt 全文 grep 仅命中一个 Skills 页（2026/04/01 更新），无任何 MCP 条目；klingai-dev org 下是 openclaw-plugin/deepseek-plugin/pi-plugin 三个孤立插件而非统一协议实现；官方 Skill 文档写明'暂时无法通过 API Key 访问，预计六月内支持'
  - 切入：为可灵做第三方 MCP/skills 网关：内置中国/全球双区端点探测、AK/SK→OAuth 封装、3.0 Omni 音视频同步参数映射、积分预估——把可灵官方 skill 没做好的认证和计费体验补齐，以 npm 包+托管端点双形态分发
- **MiniMax 官方 MCP 的视频工具严重滞后于 API：generate_video 模型枚举只有 Hailuo-02/T2V-01 系列，不含已发布的 H3/H3 Max；且 8/20 下线 Music 工具后 agent 无法再调用音乐能力**
  - 证据：platform.minimax.io/docs/guides/mcp-guide.md 模型枚举为 [MiniMax-Hailuo-02, T2V-01-Director, ...] 无 H3；同页 Tip 建议改用 CLI；platform.minimax.io 公告 8/20 起音乐付费 API 对新用户关闭
  - 切入：在多供应商 CLI 里以最新 API 契约（含 H3/H3 Max、4-15s、2K）直接封装海螺视频，绕过其官方 MCP 的滞后枚举；音乐空档则路由到其他厂商的音乐 API（如 ElevenLabs music_v2_5）做成跨厂商回退链
- **全行业（除 Vidu 的 skills 和 Pika 的个别参数外）没有厂商在 agent 工具面做'生成前成本报价'；Luma/MiniMax/Vidu API 全部是轮询制且无公开 webhook，agent 每次轮询都烧 token**
  - 证据：Luma 文档明确 Submit→Poll→Download 三步无 webhook；MiniMax MCP 只有 query_video_generation 轮询工具；Vidu skills 是唯一内置 Cost Estimation 的官方集成；社区项目 smart-token-guard（'Stop burning credits on broken AI video'）的存在反证了官方层缺位
  - 切入：把'dry-run 报价 + 统一任务编排'做成 contract-first CLI 的核心卖点：每家厂商维护一份机器可读定价/时长/分辨率合约，生成前返回全供应商比价表，后台代管轮询/webhook，agent 只收最终结果——这是所有厂商都没占的生态位
- **ElevenLabs 接入层托管化后工具面反而收窄：托管 MCP 只覆盖 ElevenAgents 管理+TTS，音乐/音效/语音克隆/视频转音乐（video-to-music）全部不在托管版里，而开源本地版已弃用**
  - 证据：hosted-mcp.md 安全范围原话'OAuth permissions covering ElevenAgents read and write operations and Text to Speech'，未提及 music/sound effects/video；elevenlabs-mcp README 8/20 弃用声明指向托管版
  - 切入：做跨厂商统一本地 MCP/CLI，专门收录'被托管化抛弃'的能力（ElevenLabs 音效/克隆/配乐 + 各家视频），对厌恶把凭据交给托管 OAuth 的专业用户形成差异化
- **Pika 旧 Developer API 用户被整体抛弃：dk_ 密钥全部失效、新平台无时间表、无迁移路径，其 skills 还依赖第三方 Mellis-Labs marketplace 同步（供应链不透明）**
  - 证据：Pika-Skills README：'Existing Developer Keys no longer work, and new keys can no longer be created'、'Future programmatic access details will be announced when the new platform launches'；Pika-Plugins 提交记录显示 skills 源自 Mellis-Labs/pika-creative-plugin-marketplace 自动同步
  - 切入：承接 Pika 出逃用户：提供 pika 风格 skill 语义（podcast/explainer/ugc-ads 三类工作流）但路由到用户自选的模型供应商；同时 Pika MCP 的多供应商聚合参数设计（generate_video 带 kling/veo3/sora/minimax 各自旋钮）证明了该形态有真实需求，可以做得更中立
- **中国厂商的 agent 面在国际一致性上残缺：可灵文档是 JS 渲染 SPA（llms.txt 缓解但 Skill 文档停在 4 月）、认证是 AK/SK 而非行业惯例的 API Key/OAuth、MiniMax MCP 指南完全不提 CN/Global 双区差异、Vidu 同时存在 vidu.cn/.com/.io/.studio 四个域名**
  - 证据：kling.ai/document-api 经 Playwright 渲染才可见正文；kling-skills 页写明 AK/SK 手动导入命令且 API Key 'expected to support within June'；MiniMax mcp-guide.md '未提及任何中国大陆平台与国际平台差异'（仅 mmx-cli README 提及双区）；Vidu 双区端点要靠用户手设 VIDU_BASE_URL
  - 切入：独立开发者做'中国模型国际接入规范层'：统一凭据模型（一处配置自动映射各家中英文平台）、双区端点自动探测、数据出境/合规提示、英文文档与状态页——这是中国厂商自己不会优先做、国际 agent 开发者又最痛的一层
- **没有任何官方集成做'生成前校验'（prompt 合约、关键帧可用性、模型能力矩阵匹配），错误要到任务提交后才发现并扣费**
  - 证据：官方 skills 全部是提交-轮询两段式；唯一做预检的是社区项目 smart-token-guard（'Check every keyframe and clip before you pay for the next render'）；Luma 文档承认 legacy API 误路由问题（HDR 请求误发 Ray 3 的 FAQ）说明参数路由确实易错
  - 切入：在 CLI 合约层内置静态校验：分辨率/时长/关键帧数/模型能力矩阵在提交前对账，错误零成本拦截——把 Higgsfield 的 evals 思路从模型层下沉到接入层

### 未解问题

- 可灵是否会在 2026 下半年推出官方 MCP 或统一 CLI？其官方 Skill 承诺的'API Key 认证六月内支持'是否已兑现（文档页停留在 4 月，未见更新声明）
- Pika 新开发者平台（PikaStream 1.0）的发布时间、商业条款和是否保留托管 MCP 三表面并存
- ElevenLabs 托管 MCP 是否会扩容到 music/sound effects/voice clone/video-to-music，还是这些能力永久留在被弃用的本地版
- Luma 'Agents API' 的命名是否预示真正的 agent 编排能力（多步骤、工具调用），还是纯营销改名；CLI 0.3.0 之后是否还有投入
- MiniMax Video Agent（模板化视频任务）API 何时进入 MCP/skills 层，与通用 generate_video 的割裂是否是长期设计
- Vidu 的 shengshu-ai/vidu-mcp 无弃用声明但 15 个月未更新，官方是否已默认由 vidu-skills 取代
- Pika MCP 内的 sora_edit 工具在第三方模型（Sora）上的商业授权模式是否可持续（2026 年 9 月 Sora 生态变动后）

### 来源

- [Luma Agents API 官方文档（Ray3.2/uni-1.1、CLI/SDK、无 MCP）](https://docs.agents.lumalabs.ai)
- [Luma API 产品页（Ray3.2 能力与定价、合作伙伴列表）](https://lumalabs.ai/api)
- [lumalabs/luma-agents-cli（官方 CLI，v0.3.0 停于 2026-06-08）](https://github.com/lumalabs/luma-agents-cli)
- [MiniMax-AI/MiniMax-MCP（官方 MCP，2026-08-20 迁移 SDK v2 并下线 Music 工具）](https://github.com/MiniMax-AI/MiniMax-MCP)
- [MiniMax-AI/cli（官方 mmx-cli，2026-09-19 新增 speech transcribe）](https://github.com/MiniMax-AI/cli)
- [MiniMax 官方 MCP 指南（视频模型枚举滞后、建议改用 CLI）](https://platform.minimax.io/docs/guides/mcp-guide.md)
- [MiniMax 平台文档总索引（H3/H3 Max、音乐 API 关停公告、Video Agent API）](https://platform.minimax.io/docs/llms.txt)
- [elevenlabs/elevenlabs-mcp（官方 MCP，2026-08-20 加弃用声明转向托管版）](https://github.com/elevenlabs/elevenlabs-mcp)
- [ElevenLabs Hosted MCP server 官方文档（OAuth/CIMD、仅 Agents+TTS 范围）](https://elevenlabs.io/docs/eleven-agents/operate/hosted-mcp.md)
- [ElevenLabs CLI 官方文档（voice agents as code）](https://elevenlabs.io/docs/eleven-agents/operate/cli.md)
- [ElevenLabs Changelog 2026-09-14（CLI v1.3.0、music_v2_5）](https://elevenlabs.io/docs/changelog/2026/9/14.md)
- [ElevenLabs Changelog 2026-08-31（CLI v1.1.0、music v2.5）](https://elevenlabs.io/docs/changelog/2026/8/31.md)
- [Kling AI 官方 Skill 文档（ClawHub v1.1.0、AK/SK 认证、意图路由）](https://kling.ai/document-api/api/get-started/kling-skills)
- [kling.ai llms.txt（模型演进到 3.0 Omni、海外收入 70%）](https://kling.ai/llms.txt)
- [klingai-dev/openclaw-plugin（可灵官方 OpenClaw 插件，2026-09-16）](https://github.com/klingai-dev/openclaw-plugin)
- [shengshu-ai/vidu-skills（官方 Agent Skill，成本预估/双区 token，2026-09-18 更新）](https://github.com/shengshu-ai/vidu-skills)
- [shengshu-ai/vidu-cli（官方 CLI，npm+cargo 双分发）](https://github.com/shengshu-ai/vidu-cli)
- [shengshu-ai/vidu-mcp（官方 MCP，2025-06-26 后停止更新）](https://github.com/shengshu-ai/vidu-mcp)
- [shengshu-ai/openclaw-vidu-s（Vidu S 实时数字人/流编辑的 OpenClaw 集成）](https://github.com/shengshu-ai/openclaw-vidu-s)
- [Pika-Labs/Pika-Plugins（官方 Claude 插件：58 工具托管 MCP + 9 skills 三表面）](https://github.com/Pika-Labs/Pika-Plugins)
- [Pika-Labs/Pika-Skills（官方宣布旧 Developer API 停用、PikaStream 1.0 新平台在建）](https://github.com/Pika-Labs/Pika-Skills)
- [Pika-Labs/Pika-Experiments（官方 agent 原型工作坊）](https://github.com/Pika-Labs/Pika-Experiments)

---

## 开发者需求侧（90 天社区信号）

近 90 天（2026-06-22 至 09-22）的开发者侧声音呈现清晰格局：fal 生态是"计费信任重灾区"（锁号 bug 连环 11+ 条 issue、执行时长计费故障、USDC 入账丢失，且官方在 GitHub 上几乎 0 回复）；Runway 把 skills 战略性升级为"Dev Platform 唯一集成路径"（8-28 官方 commit 明示 MCP-aware 方向）；Higgsfield 消费端 UX 强但开发者集成面缺失，9-21 一天内有 3+ 个第三方 CLI/ComfyUI 集成冒出，其 MCP 被抱怨幻觉。最关键的需求验证来自 9-16 上线的 VideoRouter（"OpenRouter for video"）：同一视频模型在不同供应商间价差 5-10 倍，路由/比价层已被独立开发者验证为真需求。对正在自研 contract-first 多供应商 CLI 的读者，最大空位是：厂商都没把"计费可信、任务生命周期、幂等重试"做成一等契约——webhook 验签、断点恢复、预算护栏全靠集成者自己造轮子，这正是 contract-first CLI 的用武之地。

### 近 90 天时间线

- **2026-06-26** — fal issue #1094：付费成功后账号立即被锁，开启 90 天内连环'锁号'投诉潮（#1072/#1108/#1112/#1147/#1162/#1163/#1168 等，多数 0 官方回复，用户互相交叉引用同一 unlock bug）（https://github.com/fal-ai/fal/issues/1094）
- **2026-07-13** — fal issue #1112：正余额仍显示'Exhausted balance'锁号，确认与 #489/#922 同一自动解锁 bug——问题已持续多个季度（https://github.com/fal-ai/fal/issues/1112）
- **2026-08-14** — fal issue #1146：fal_client 同步 MultipartUpload.save 从第二个分片起上传空字节——数据静默损坏类 bug（https://github.com/fal-ai/fal/issues/1146）
- **2026-08-22** — HN 用户 echelon 公开批评 Higgsfield'unethical'并列举 dark patterns 文章（同日讨论串中也有人指出其定位 UGC 创作者、开发者被忽视）（https://news.ycombinator.com/item?id=49401031）
- **2026-08-24** — Replicate replicate-javascript issue #382：'CRITICAL BILLING BUG: Infrastructure Deadlock on Disabled Deployment'——计费/部署状态机死锁（https://github.com/replicate/replicate-javascript/issues/382）
- **2026-08-27** — 社区项目 Videoai PR #12：把 fal queue 句柄持久化到磁盘、拆分 submit/poll 以支持重启恢复——集成者自造长任务生命周期管理（https://github.com/FarrukhGulomov/Videoai/pull/12）
- **2026-08-28** — Runway 官方 skills 仓库三连 commit：'add MCP-aware Dev Platform integration skills'、'make Dev Platform skills sole integration path'——skills 成为官方钦定集成路径（https://github.com/runwayml/skills）
- **2026-08-29** — corsair issue #1369：向社区项目请求 fal 队列提交+queue status+webhook 支持——再次证明长任务等待体验要靠第三方补（https://github.com/corsairdev/corsair/issues/1369）
- **2026-08-31** — fal 发布 H3 Max（自训练 MiniMax 变体，'5 秒视频不到 3 秒生成'），HN 帖'Faster than real-time video generation'——fal 从聚合器转向自有模型变体（https://news.ycombinator.com/item?id=49505580）
- **2026-09-09** — fal-js issue #238：queue.submit 无视 retry.maxRetries:0 并重放传输失败的 POST——用户明确要求'文档化服务端幂等保证'，暴露提交无幂等键（https://github.com/fal-ai/fal-js/issues/238）
- **2026-09-11** — VideoRouter 作者在'Save 80% for video generations'帖中阐述：同一模型各供应商 $/秒价差巨大，需按价格/可用性自动路由，首批支持 Atlascloud/Fal/Replicate/WaveSpeed（https://news.ycombinator.com/item?id=49667081）
- **2026-09-14** — HN 用户 bmau5：使用 Higgsfield MCP 与 Figma 直连集成时'反复遇到产品尺寸等幻觉'——厂商 agent 集成质量问题被点名；同日 fal #1168 又一条正余额锁号投诉（https://news.ycombinator.com/item?id=49705458）
- **2026-09-16** — VideoRouter 正式上 HN：'prices can differ by 5-10× depending on the provider'——统一视频模型路由层作为品类被公开验证（https://news.ycombinator.com/item?id=49733974）
- **2026-09-17** — 三件事同日：fal #1175 投诉 80 秒视频被按 10,272 秒执行时长计费（ alleged $40,500）；V2EX 帖 '接入了 Seedance 系列模型——效果是真的好，贵也是真的贵'；社区项目 Komamotion PR 演示需自行实现 fal JWKS/ED25519 与 Replicate Svix webhook 验签（https://github.com/fal-ai/fal/issues/1175）
- **2026-09-18** — V2EX 帖'商汤悄悄更新的这几个 skills 还挺好用的'：SenseNova-Skills 用 Motion HTML 串图片+Seedance 视频——中文厂商也在卷 agent skills；fal #1172：$70 USDC Solana 充值最终确认但未入账（https://www.v2ex.com/t/1243083）
- **2026-09-19** — V2EX 帖'libTV 本地开源平替：画布+剪辑一体，任何 MCP Agent 都能全程操控'（29 个 MCP 工具），回复中追问'有没有比 wan3 便宜的视频模型 API'——成本敏感+MCP 化工作流是中文开发者当前热点（https://www.v2ex.com/t/1243225）
- **2026-09-21** — Higgsfield 第三方集成同日爆发：HiggsfieldAPI-CLI（Python CLI 管理图片/视频生成）、ComfyUI-Higgsfield（目录驱动 API 集成）、nk-studio（local-first API studio）——官方开发者工具缺位，社区自己上（https://github.com/rk-research/HiggsfieldAPI-CLI）

### Roadmap 信号

- **Runway 将把 Dev Platform skills 作为唯一官方集成路径持续投入（8-28 一天三个 commit：MCP-aware skills → 设为 sole integration path），未来第三方直接调 API 的玩法会被引导收敛到 skills/MCP 通道**（置信：官方明示；https://github.com/runwayml/skills）
- **fal 正从'聚合器'转向'自有模型变体'：8-27 发布自训练 H3 Max、9-17 发推理 deep-dive，'faster than real-time'成为其视频侧主打叙事；这会挤压纯比价路由层的模型同质化空间**（置信：官方明示；https://blog.fal.ai/h3-max-built-with-fal-inference-and-training/）
- **'OpenRouter for video'成为被验证的品类：VideoRouter 9-11/9-16 两次发帖，首批即接入 Atlascloud/Fal/Replicate/WaveSpeed；HN 同期讨论提及 fal 估值 $8B、Stripe 收购 OpenRouter $7B+——通用模型路由被资本确认后，视频垂类路由是被看好的下位替代**（置信：多源交叉；https://news.ycombinator.com/item?id=49733974）
- **Higgsfield 开发者生态将被动补课：9-21 同日 3+ 个第三方 CLI/ComfyUI 集成出现，说明其 API 有需求但官方工具缺位；若继续只服务 UGC 创作者，开发者侧会被聚合器和第三方 CLI 接管**（置信：推断；https://github.com/rk-research/HiggsfieldAPI-CLI）
- **中文厂商入场 agent skills（商汤 SenseNova-Skills 串图片+Seedance 视频成页）+ 中文社区 MCP 化视频工作流兴起（libTV 29 个 MCP 工具），中文市场的'skill+MCP 工作流'窗口正在打开**（置信：多源交叉；https://www.v2ex.com/t/1243083）

### 做得好的

- fal：推理性能工程一流——H3 Max 宣称 5 秒视频 3 秒内生成并登顶人类偏好评测（9-17 官方 deep-dive），加上此前的 sub-second Ideogram、FlashPack 加载技术；对开发者最有价值的资产是其'工程透明'博客文化，deep-dive 本身就是获客渠道
- Runway：集成战略最清晰——8-28 官方 commit 把 Dev Platform skills 定为'唯一集成路径'并做了 MCP-aware 改造，skills 仓库同时分发 Claude/Cursor 双 marketplace，等于官方下场做 agent 生态
- Higgsfield：消费端增长机器——HN 讨论承认'Higgsfield 和字节证明了后进者能赢'；其 UX 剧本（CLI+规则+模型路由树+evals）在四家架构哲学里对 agent 最友好；社区一天内冒出 3+ 第三方集成说明 API 需求真实存在
- AtlasCloud：已被 VideoRouter 列入首批支持供应商（与 Fal/Replicate/WaveSpeed 并列）——说明其 API 在聚合生态里被当作一等公民；中英双语+嵌入式 API 参考的 skill 形态在中文市场是差异化
- Replicate：Cog 生态（自托管模型容器化）和 Svix webhook 验签等基础设施细节被社区项目反向引用为范本（Komamotion PR 同时实现 fal JWKS 与 Replicate Svix）

### 空位与切入姿势

- **计费可信层：没有任何厂商把'成本可预估、账单可对账、异常可护栏'做成契约。fal 90 天内 11+ 条'正余额仍锁号'连环 bug 且 GitHub 上基本 0 回复，#1175 声称 80 秒视频按 10,272 秒计费，#1172 USDC 入账丢失；Replicate 有'部署禁用仍计费死锁'；HN 用户抱怨 fal preflight 成本检查'极不可靠，预期与实际成本差数量级'**
  - 证据：https://github.com/fal-ai/fal/issues/1175 、https://github.com/replicate/replicate-javascript/issues/382 、https://github.com/fal-ai/fal/issues/1163
  - 切入：在 contract-first CLI 里内置：每 run 预算护栏（spend guard，超限熔断）、本地账本与供应商账单自动对账、提交幂等键、执行时长/计费时长偏差告警。这些全是多供应商场景的公约数，单厂商永远不会替你做。吐槽密度极高（90 天 15+ 条 issue），但第三方付费意愿属中等——适合作为 CLI 的信任卖点而非独立收费点
- **长任务生命周期契约缺失：webhook 验签（fal JWKS/ED25519、Replicate Svix）、断点恢复（queue 句柄持久化）、submit/poll 拆分、重试语义，全部由集成者在各项目里重复造轮子**
  - 证据：Komamotion PR 自实现两家验签（https://github.com/nexulys/Komamotion/pull/2）；Videoai PR 持久化 fal queue 句柄支持重启恢复（https://github.com/FarrukhGulomov/Videoai/pull/12）；corsair issue 请求 queue status+webhook（https://github.com/corsairdev/corsair/issues/1369）；fal-js #238 证明连 retry:maxRetries:0 都不生效、且无法确认服务端是否幂等去重
  - 切入：把'任务句柄'抽象为多供应商统一契约：本地持久化 job id→崩溃恢复、统一 webhook 验签库、统一超时/退避/幂等策略、'提交失败后不知道任务是否已创建'的显式 unresolved 状态机。动手迹象极强（至少 4 个独立项目在 90 天内自造），是 CLI 最硬的差异化模块
- **统一路由/比价层刚被验证但远未成熟：同一视频模型在不同供应商间价差 5-10 倍，开发者需手动选商、手动因价格切换；fal/Higgsfield/Replicate 各自只推自家，无人提供中立比价**
  - 证据：VideoRouter 作者原话'prices can differ by 5–10× depending on the provider'，并追问规模化用户如何选商（https://news.ycombinator.com/item?id=49667081）；V2EX 回复追问'比 wan3 便宜的视频模型 API'（https://www.v2ex.com/t/1243225）；HN 用户在 Seedance 2.5 讨论中说'愿意为更多控制和更低成本接受画质小损'（https://hn.algolia.com/api/v1/search_by_date?query=fal.ai&tags=comment）
  - 切入：两个姿势：(a) 在 CLI 内做 provider-agnostic 路由策略 + 开源价格表数据文件（社区可 PR，天然传播）；(b) 做'开源/本地优先的 VideoRouter'——先发者 franklin_yao 的产品刚上线（HN 1 分 1 评）、闭源且托管，开源+可自托管+不抽成是清晰差异位。付费意愿已被直接验证（'Save 80%'是卖点）
- **一致性与可控性没有契约化：厂商把'角色一致性/镜头控制'当消费端功能卖点，API 侧开发者只能各显神通；社区产品反过来把'稳定可控角色'当核心卖点营销**
  - 证据：V2EX'全链路 AI 短剧工具'强调'稳定、可控的角色'（https://www.v2ex.com/t/1242811）；fal 官方博客亲自写 3D-to-AI 'total control' 管线教程——等于承认 API 不内置可控性（https://blog.fal.ai/from-clay-3d-render-to-a-real-action-short-a-3d-to-ai-pipeline-with-total-control/）；Higgsfield MCP 被抱怨产品尺寸幻觉（https://news.ycombinator.com/item?id=49705458）
  - 切入：把一致性做成跨供应商原语：reference 图+seed+角色描述的标准化契约、同一 prompt 多供应商并跑的 eval 对比报告、一致性回归测试集。这是读者此前调研确认四家都未契约化的点，且中文短剧/电商场景付费意愿最明确
- **agent skill/MCP 生态质量参差且无质检：Higgsfield MCP 幻觉被点名；Runway skills 仓库被同一账号 25 条 spam issue 淹没无人清理、且 8-28 一次性破坏性重构集成路径；AtlasCloud 公共 agent-skills 仓库自 2 月底停更 7 个月**
  - 证据：runwayml/sdk-python issues 全是 iid7oom21 刷屏、0 官方清理（https://github.com/runwayml/sdk-python/issues/272）；bmau5 的 MCP 幻觉抱怨（https://news.ycombinator.com/item?id=49705458）；AtlasCloudTeam/agent-skills 最后 commit 2026-02-24（https://github.com/AtlasCloudTeam/agent-skills/commits）
  - 切入：做'第三方 skill 质检与兼容层'：带 evals、SHA256 完整性校验、版本化破坏性迁移警告的多供应商 skill 套件；再叠加 skill 兼容性测试（厂商改契约即报警）。Runway 把 skills 定为唯一路径反而放大了这个空位——路径唯一意味着质量竞争者稀少
- **错误语义不统一、可观测性缺位：Replicate'500 但任务实际成功'、fal 上传分片静默损坏、MP4 音频流截断——失败/成功的判定都要用户自己兜底**
  - 证据：replicate-javascript #381'api call failed with 500 but training job actually went through'（https://github.com/replicate/replicate-javascript/issues/381）；fal #1146 分片上传空字节（https://github.com/fal-ai/fal/issues/1146）；fal #1092 音频流早断（https://github.com/fal-ai/fal/issues/1092）
  - 切入：统一错误分类学+run 级本地遥测：每次生成记录成本/时长/失败类别，跨供应商聚合出'哪家哪类失败率高'的实测数据——这既是 CLI 功能，也是可公开的内容资产（类似 fal 的 State of Generative Media 报告，但中立、多供应商）

### 未解问题

- Reddit（r/aivideo、r/StableDiffusion、r/LocalLLaMA）一手吐槽未能抓取：pullpush.io 与 Reddit 均持续 429 限流，Reddit 侧的抱怨密度和付费意愿直接证据缺失——需放开 WebSearch 额度（本会话 200/200 已耗尽）或人工抽查确认
- 'Higgsfield 开源核心仓库'说法未证实：HN 9-17 有帖但无链接无讨论（1 分 0 评），GitHub 的 higgsfield 账号实为深度 RL 教程作者个人号，与公司无关；不得作为事实引用
- fal 锁号问题的真实支持响应率：GitHub issue 几乎 0 回复，但不排除工单渠道正常处理——锁号是 bug 还是风控策略、是否已有修复计划，需进一步证据
- Higgsfield 是否有公开的开发者 API 文档/SDK 及其语言覆盖：本次仅从第三方集成侧反推其 API 存在，官方文档面未核验
- V2EX 上'贵'的吐槽是否转化为付费工具消费：#1242784 等帖 0 回复，未见明确的'愿意为省多少钱付多少'表达，中文市场付费强度需即刻/知乎侧补充
- Runway 'Dev Platform skills 唯一集成路径'迁移的官方公告原文与迁移指南：仅从 commit message 推断，未找到对应 changelog/blog
- 即刻、知乎两个中文渠道完全未覆盖（无可用的直接抓取路径），其中可能存在的集成吐槽未计入

### 来源

- [fal-ai/fal issue #1094：付费后账号锁定（连环锁号投诉起点）](https://github.com/fal-ai/fal/issues/1094)
- [fal-ai/fal issue #1175：80 秒视频被按 10,272 秒计费](https://github.com/fal-ai/fal/issues/1175)
- [fal-ai/fal issue #1163：正余额仍锁号（自动解锁 bug 复现）](https://github.com/fal-ai/fal/issues/1163)
- [fal-ai/fal issue #1172：$70 USDC 充值未入账](https://github.com/fal-ai/fal/issues/1172)
- [fal-ai/fal-js issue #238：queue.submit 无视 retry 配置并重放 POST（幂等缺失）](https://github.com/fal-ai/fal-js/issues/238)
- [fal-ai/fal issue #1146：MultipartUpload 上传空字节](https://github.com/fal-ai/fal/issues/1146)
- [replicate-javascript issue #382：部署禁用仍计费死锁](https://github.com/replicate/replicate-javascript/issues/382)
- [replicate-javascript issue #381：API 返回 500 但训练任务实际成功](https://github.com/replicate/replicate-javascript/issues/381)
- [HN：VideoRouter – OpenRouter for video and image generation APIs](https://news.ycombinator.com/item?id=49733974)
- [HN 评论：VideoRouter 作者阐述供应商价差 5-10 倍（Save 80% 帖）](https://news.ycombinator.com/item?id=49667081)
- [HN 评论：Higgsfield MCP/直连集成幻觉抱怨（bmau5）](https://news.ycombinator.com/item?id=49705458)
- [HN 评论：Higgsfield dark patterns 批评（echelon）](https://news.ycombinator.com/item?id=49401031)
- [HN：Faster than real-time video generation（fal H3 Max）](https://news.ycombinator.com/item?id=49505580)
- [fal 博客：H3 Max Built with fal Inference and Training（9-17）](https://blog.fal.ai/h3-max-built-with-fal-inference-and-training/)
- [fal 博客：Introducing H3 Max by fal（8-27）](https://blog.fal.ai/introducing-h3-max-by-fal/)
- [fal 博客：3D-to-AI pipeline with total control（7-13）](https://blog.fal.ai/from-clay-3d-render-to-a-real-action-short-a-3d-to-ai-pipeline-with-total-control/)
- [runwayml/skills 官方仓库：8-28 'Dev Platform skills sole integration path' 等三连 commit](https://github.com/runwayml/skills)
- [runwayml/sdk-python：spam issue 刷屏无人清理的样例](https://github.com/runwayml/sdk-python/issues/272)
- [Komamotion PR：自实现 fal JWKS 与 Replicate Svix webhook 验签](https://github.com/nexulys/Komamotion/pull/2)
- [Videoai PR：fal queue 句柄持久化与 submit/poll 拆分](https://github.com/FarrukhGulomov/Videoai/pull/12)
- [corsair issue #1369：请求 fal queue status + webhook 支持](https://github.com/corsairdev/corsair/issues/1369)
- [V2EX：接入 Seedance 系列模型——'效果是真的好，贵也是真的贵'](https://www.v2ex.com/t/1242784)
- [V2EX：libTV 本地 MCP 视频工作流（29 个 MCP 工具，回复追问比 wan3 便宜的 API）](https://www.v2ex.com/t/1243225)
- [V2EX：商汤 SenseNova-Skills（Motion HTML 串图片+Seedance 视频）](https://www.v2ex.com/t/1243083)
- [V2EX：全链路 AI 短剧工具（主打稳定可控角色）](https://www.v2ex.com/t/1242811)
- [GitHub：rk-research/HiggsfieldAPI-CLI（9-21 创建的第三方 Higgsfield CLI）](https://github.com/rk-research/HiggsfieldAPI-CLI)
- [GitHub：PRYX-STUDIO/ComfyUI-Higgsfield（9-21 创建的 ComfyUI 集成）](https://github.com/PRYX-STUDIO/ComfyUI-Higgsfield)
- [GitHub：AtlasCloudTeam/agent-skills（公共仓库最后 commit 2026-02-24）](https://github.com/AtlasCloudTeam/agent-skills)
- [GitHub：AtlasCloudTeam org 仓库列表（VideoRouter 首批支持的供应商之一）](https://api.github.com/orgs/AtlasCloudTeam/repos)
- [HN Algolia：fal.ai 近 90 天评论区检索（成本预估不可靠等抱怨）](https://hn.algolia.com/api/v1/search_by_date?query=fal.ai&tags=comment&hitsPerPage=15&numericFilters=created_at_i%3E1753200000)

---

> **Higgsfield + Runway 路未跑成**（429 限流）。已从需求侧获得的信号：Runway 8-28 把 skills 升级为 Dev Platform 唯一集成路径（官方 commit，MCP-aware 方向）；Higgsfield 消费端强、开发者集成面缺失（9-21 一天 3+ 个第三方 CLI 冒出、MCP 被抱怨幻觉）。待补跑后更新本文件。
