# 深挖第二轮 · 竞品 / 一致性配方 / 判片设计 / 合规标准 / 源码考古（2026-09-22）

> 方法：8 路 schema 约束 agent（资本路数图路因网络故障待补跑；价格表与能力矩阵两路已直接灌入 `data/prices.json` 与 `data/capabilities.json`，不入本文件）。
> 规则：以 2026-09-22 为"现在"，一手来源优先，空位判断必须附证据。
> 原始结构化输出：workflow run wf_1b079cd9-5e7。

---


## 直接竞品拆解（VideoRouter / vibeframe / muapi 系 / RunComfy / PixVerse / ComfyUI 官方）

六家竞品/近邻拆解（今天 2026-09-22；全部结论附一手 URL，本地 AtlasCloud CLI 仓库为"我们"的定位参照）。

【a) VideoRouter / videorouter.sh（Synvia Corp, Newark CA）】做什么：OpenAI 兼容统一 API 的"OpenRouter for video"，按价格/健康度在 Fal、WaveSpeedAI、Atlas Cloud、Replicate、Novita 之间路由，渲染中自动 failover，逐请求列出供应商成本+平台费；自建部分开源权重模型（Wan、HunyuanVideo、MiniMax H3）。商业模式：统一 2% 平台费（对标 OpenRouter 5.5%），无订阅无折扣，BYO key 也照收 2%；报价表直接列出 "MiniMax H3 Developer (Atlas) $0.020→$0.0202/sec"、"Wan 3.0 (Atlas) $0.0404/sec"——Atlas Cloud 是其上游供应商之一。不做什么：不开源平台本身；无 dry-run 成本预检/硬顶；官方 CLI @videorouter/cli 在 npm 不存在（registry 查询 not found），官方 skills 仓库 synvia-corp/videorouter-skills 0★；社区零牵引（HN 9/16 帖 1 分 1 评论，作者 franklin_yao karma=1；9/11 帖 2 分），5 天内从"Save 80%"改为"OpenRouter for video"说明定位仍在漂移。活跃度：官网与定价页活跃，GitHub 生态近乎为零。威胁等级：中高（方向与我们+中立层完全重叠，但执行面是空壳）；对 Atlas 同时是渠道而非纯对手。

【b) vibeframe（vericontext/vibeframe, 168★）】做什么：CLI+MCP，让 coding agent 用用户自己的 key 调 Seedance/Runway/Veo/Kling 生成视频；核心契约是 --dry-run 免 key 报价、--max-cost 硬顶（超限返回 COST_CAP_EXCEEDED + retryWith 两条降级路径 + 完整报价 plan）、机器可读错误信封与恢复动作；编排委托 Remotion/Hyperframes（自称非 HeyGen 关联）。商业模式：无（MIT 开源、BYOK、不抽成，npm 包 @vibeframe/cli）。不做什么：不托管、不代账、无统一计费与目录，全部成本透明转嫁。活跃度：单人 Kiyeon Jeon（1110/1117 contributions，bio "AI Engineer"）；2026-02-01 建仓，最后 push 与最后 release 均停在 2026-07-26（v0.115.2），已停滞 8 周；npm 766 下载/月；51 个 issue 全关闭、0 开放。威胁等级：低（验证了成本契约需求，但不构成商业威胁）。

【c) muapi.ai 系 SKILL.md 合集（SamurAIGPT/Generative-Media-Skills, 4316★）】做什么：面向 Claude Code/Cursor/Gemini CLI 的 100+ 模型技能合集（41 个 UGC/电商向视频图片配方 + core 原语），底层全部走 muapi-cli；UTM 漏斗完整（repo homepage 和 "Powered by MuAPI" 徽章均带 utm_source=github&utm_campaign=generative-media-skills）；计费为 Stripe 充值积分（muapi account topup --amount 20 经 Stripe checkout）。定价页宣称比 Fal 低 60-64%（Seedance 2.5 720p $0.34/sec）、比 OpenAI 官方低 29-31%，低于成本价的逻辑不可持续或为引流，抽成率不公开。不做什么：无成本预检；无中立性（只指向 muapi）。真实使用与口碑背离：4316★/494 fork 但 muapi-cli 仅 1,934 npm 下载/月；仓库 2023-05-25 创建，issue 跟踪器里是 privateGPT 时代的旧账（"404 after running privateGPT.py"、"Run slowly in my 16G notebook"）——星数大量继承自已转型旧仓库；issue 区几乎全是 dependabot 与互推机器人，73 个 issue 中找不到真实用户抱怨，生态靠 SamurAIGPT(99 仓库/619 粉丝)+Anil-matcha（Open-Generative-AI 29k★）约 25+ 个仓库 README 互链刷量。威胁等级：中（分发机器真实存在，但产品与信任面薄）。

【d) RunComfy CLI + genmedia-labs 技能矩阵】做什么：runcomfy-com 官方 Rust CLI（@runcomfy/cli，OAuth+token，models/run/status/result、Serverless ComfyUI 部署、LoRA 训练全流程）+ 官方 skills（12★，走 skills.sh 与 Claude/Cursor marketplace 插件）+ 托管 MCP（31 工具）。商业模式：ComfyUI 云 GPU 托管 + Model API + LoRA 训练，积分计费。3.8M 安装解剖：skills.sh 显示 genmedia-labs/skills（匿名组织，单人 kalvinrv，2026-08-12 建仓、仅 3 commits、13★）33 个技能共 3.8M 安装、357 个 UTM 链接指向 runcomfy.com、零 fal 端点——是 RunComfy 的营销阵地（前期文档已做源码级核实）；但顶部 5 个技能安装数 597.5K-599.5K 高度一致，疑似批量/统一计数；真实使用侧 @runcomfy/cli 仅 1,652 npm 下载/月、官方仓库 1★，fal 官方社区 skills 也仅 8.8K 安装且 5/13 停更。周边还有 prime-skills、agentspace-so、doany-ai 等 SEO 式第三方技能农场。活跃度：2026-09 多面并进（cli 9/7、mcp+skills 9/15、gemini 9/6）。威胁等级：分发渠道上中高、产品面上低。

【e) PixVerse 官方 CLI（PixVerseAI/cli, 59★, MIT）+ skills（61★）】做什么："UI-free 版 pixverse.ai"，npm pixverse（4,275 下载/月），OAuth device flow，订阅制积分；约 27 个视频模型（自家 V6/C1 + 第三方 Sora/Veo/Kling/Seedance/Wan/MiniMax/Grok——单厂商聚合者）。契约是全场最佳参照：仓库根 capabilities.json（schema 1.2.0，"Generated from Commander definitions, Do not hand-edit"，exit codes 0-7 含 CREDIT_INSUFFICIENT=4、CONCURRENCY_LIMIT=7，trace_id，global/cn 双区）；skills/references/execution-contract.md 精确到 streams 分工、批次 partial completion 的 JSON 形态（items/failed_ids/fail_count）、防丢数据的 jq 单行模板；prompt-contract.md 界定"生成不改 prompt、优化需授权、禁止加质量垫话/保留故意孪生与品牌文本"。不做什么：无成本预检（积分不足是运行时退出码）、订阅墙、无跨厂商。活跃度：cli 9/20、skills 9/10 仍在推送（v1.4.5）。威胁等级：低（单厂商），但其契约工件是我们最应吸收的标杆。

【f) ComfyUI 官方两轨（Comfy-Org）】本地轨：comfy-cli（974★，技能随 CLI 二进制分发 comfy skills install）、comfy-mcp（234★，AGPL-3.0-or-later OR Commercial 双许可的 open-core，含 MCP Registry 所有权令牌机制）；云轨：comfy-skills（200★，Claude Code 插件 /comfy-cloud:* 斜杠命令 + hosted MCP cloud.comfy.org/mcp）。官方作者规则已成文："steer the approach, defer the specifics"——安装时固化的命令禁止写死模型名/模板/节点，必须指向运行时 discovery 工具。商业模式：开源引流 + Comfy Cloud 订阅。活跃度：全场最高（9/16-9/21 连发 mcp/skills/python-ts SDK/api-proxy）。威胁等级：对中立层低（云轨只覆盖自家目录），但其作者规则应成为行业标准。

【总判断】这一层目前是"强分发、弱契约"：会刷量的（muapi、RunComfy 矩阵）没有统一契约与真实使用；有契约的（PixVerse）只覆盖自家且无成本预检；有成本契约的（vibeframe）是停滞单人项目；方向正确的中立路由（VideoRouter）社区与 agent 面是空壳且已把 Atlas 当上游。差位点详见 gaps。

### 关键信号

- **VideoRouter 定位 5 天内从'Save 80%'切换为'OpenRouter for video'，以 2% 费率对标 OpenRouter 5.5%，并同步铺设官方 CLI（npm 未实际发布）与 skills 仓库——正在抢中立层身位但执行面尚空**（置信：官方源；https://videorouter.sh/pricing）
- **vibeframe 自 2026-07-26 v0.115.2 后零 push 零 release，单人维护（1110/1117 contributions），npm 766 下载/月——成本契约赛道暂无活跃对手**（置信：官方源（GitHub/npm API）；https://github.com/vericontext/vibeframe）
- **RunComfy 2026-09 多面并进：官方 Rust CLI（9-07）、31 工具 MCP 与 skills（9-15）、Gemini CLI 技能（9-06）、Claude/Cursor marketplace 插件；genmedia-labs 矩阵 8-12 建仓、6 周冲到 skills.sh 3.8M 安装——分发通道争夺已白热化**（置信：多源交叉（GitHub API + skills.sh + 前期源码级核查）；https://github.com/runcomfy-com）
- **muapi 生态 8-9 月密集上新（Sora-2-api、seedance-2.5-mcp、Grok-Imagine、MiniMax H3 等 25+ 互链仓库），但主技能仓库 9-08 后停更、npm 月下载仅 1.9K——刷量节奏仍在、产品迭代放缓**（置信：官方源（GitHub）+ npm 数据交叉；https://github.com/SamurAIGPT/Generative-Media-Skills）
- **PixVerse 官方 CLI/skills 持续演进（cli 9-20 推送、v1.4.5、capabilities schema 1.2.0；skills 9-10），单厂商契约标杆在加速拉开与社区技能的差距**（置信：官方源；https://github.com/PixVerseAI/cli）
- **Comfy-Org 本地+云双轨 9 月连发（comfy-mcp 9-20、comfy-skills 9-16、python/ts SDK 9-21、api-proxy），官方作者规则（禁止固化模型名）已成文——agent 契约正在被官方层面标准化**（置信：官方源；https://github.com/Comfy-Org/comfy-skills）
- **fal 官方社区 skills 自 2026-05-13 停更、skills.sh 仅 8.8K 安装，而 RunComfy 矩阵 3.8M——两大平台在第三方技能分发通道上的真空仍在扩大**（置信：单一来源（前期会话源码级核查，2026-09-22 文档）；https://github.com/AtlasCloudTeam）

### 要点 / 模式清单

- Atlas Cloud 已被 VideoRouter 列为上游报价源（其定价页标注 MiniMax H3 Developer (Atlas)、Wan 3.0 (Atlas)）——中立层目前是渠道而非对手，存在渠道杠杆与上游条款谈判位
- agent-native 定位已落地：CLI+可安装 skills+MCP+JSON 契约+遥测+自动更新均已发布（本仓库 docs/AGENT_QUICKSTART.md、skills install、atlas-mcp）
- 自有模型目录是价格真相源，做跨厂商 dry-run 报价与成本预检比任何 BYOK 工具更准
- 契约工程传统已成型：specs/、qa/、generate JSON 契约（PR #48）、agent 输入/恢复/产物契约加固（PR #50），与 PixVerse 标杆同构
- 干净分发面：无 UTM 漏斗、无匿名矩阵、无刷量历史，在与 muapi/RunComfy 矩阵的信任对比中是天然卖点

### 空位与建议

- **成本前置契约（先报价、硬顶、拒绝时给降级路径）全场只有停滞的单人项目 vibeframe 在做，其余五家全部缺失：VideoRouter 只有事后预算告警；PixVerse 的积分不足是运行时退出码（exit 4）且 cost_credits 可能缺席；muapi/RunComfy 纯充值后扣**
  - 证据：vibeframe README 的 --dry-run/--max-cost/COST_CAP_EXCEEDED+retryWith 机制（github.com/vericontext/vibeframe）vs 其 766 npm 下载/月、2026-07-26 起零 push；PixVerse capabilities.json exit codes（github.com/PixVerseAI/cli）
  - 建议：Atlas 把 dry-run 报价+max-cost 硬顶+retryWith 降级做成跨供应商一级契约能力；自有模型目录是价格真相源，官方平台做报价比 BYOK 工具更准——这是 'The model platform your AI agent already knows how to use' 叙事的最硬抓手
- **中立路由层 VideoRouter 的 agent 表面是空壳：README 宣传的 @videorouter/cli 在 npm 不存在，官方 skills 仓库 0★，HN 社区零牵引（1 分 1 评论、作者 karma=1），平台闭源，定位 5 天内漂移**
  - 证据：npm registry 查询 @videorouter/cli not found；github.com/synvia-corp/videorouter-skills（0★）；hn.algolia.com/api/v1/items/49733974
  - 建议：在其羽翼未丰前占住 agent 表面的信任位；同时把它当渠道：videorouter.sh/pricing 已把 Atlas 列为上游报价源（MiniMax H3、Wan 3.0 标注 Atlas），中立层每转发一次调用 Atlas 都在抽税——与其封堵不如谈上游条款+保证 agent 表面体验不被截流
- **skills.sh 分发通道被 RunComfy 匿名矩阵（genmedia-labs，单人 3 commits）以 3.8M 装机占领，但装机数高度可疑（顶部 5 技能 597.5K-599.5K 几乎相同）且真实使用极低（@runcomfy/cli 1,652 npm 下载/月、官方仓库 1★）**
  - 证据：skills.sh/genmedia-labs/skills（33 技能、3.8M、357 个 runcomfy UTM）；api.npmjs.org/downloads/point/last-month/@runcomfy/cli；github.com/genmedia-labs/skills（13★）
  - 建议：不打装机量、打质量与信任：发布 vendor-neutral 的 cost-aware 路由、跨厂商 fallback、真实基准对比技能，用可验证的下载/调用数据对照矩阵的匿名 UTM 漏斗；竞品技能'只懂自家目录'（fal 8.8K、RunComfy 只指向 runcomfy.com）正好留出中立路由技能空位
- **muapi 的 4.3k★ 与真实使用（muapi-cli 1,934 npm 下载/月）严重背离：星数部分继承自 2023 年 privateGPT 时代旧仓库（issue 跟踪器留有旧项目问题），生态靠 SamurAIGPT+Anil-matcha 约 25+ 仓库 README 互链与 UTM 徽章刷量；低于 Fal 官方价 60%+ 的定价机制不透明，73 个 issue 里找不到真实用户讨论**
  - 证据：github.com/SamurAIGPT/Generative-Media-Skills issues（2023-10 'privateGPT.py'、'Run slowly in my 16G notebook'）；repo homepage UTM 参数；api.npmjs.org/downloads/point/last-month/muapi-cli
  - 建议：以'真实可验证'立身：公开 npm/装机/调用的真实统计、零 UTM 的干净技能、明码价格表；在内容上对打其 41 个 UGC 配方（这是真实需求），用 Atlas 自己的 Seedance 一手价与 schema 做更可复现的配方
- **契约工件的官方标杆已由 PixVerse 树立（生成的 capabilities.json、execution-contract 的批次 partial-completion 语义与 jq 模板、prompt-contract 的改写授权边界），但它订阅墙、无成本预检、只覆盖自家+转售的模型目录**
  - 证据：github.com/PixVerseAI/cli capabilities.json（exit 4=CREDIT_INSUFFICIENT 为事后码）；github.com/PixVerseAI/skills references/execution-contract.md、prompt-contract.md 原文
  - 建议：吸收其全部形态（生成式 capabilities、双流约定、批次语义、trace_id、prompt 授权契约）并加上跨厂商目录与提交前成本预检，形成严格超集；Atlas 的 specs/、qa/、generate JSON 契约（PR #48）已有同构基础
- **Comfy 官方已把'防腐烂作者规则'成文化（steer the approach, defer the specifics：禁止写死模型名/模板，强制运行时 discovery），但其云轨只覆盖自家目录、本地轨核心是 AGPL 双许可**
  - 证据：github.com/Comfy-Org/comfy-skills README 作者规则章节；github.com/Comfy-Org/comfy-mcp（AGPL-3.0-or-later OR Commercial）
  - 建议：把该规则直接采纳进 Atlas skill 规范并对齐措辞（成为事实标准的一部分而非追赶者）；商业许可上 Atlas 公开二进制+私有源的模式无需 AGPL 也能讲'官方级契约+商用友好'故事
- **六家中无任何一家提供跨供应商的统一 job 契约+内容寻址产物校验+幂等重放；fal 官方社区 skills 在 skills.sh 仅 8.8K 安装且 2026-05-13 停更，跨厂商公共层仍是空位**
  - 证据：六家 README/契约文件逐查均无（本报告各仓库来源）；fal 侧结论来自前期源码级核查 docs/research-vendor-next-moves-2026-09-22.md（本地 video-ai-landscape 仓库）
  - 建议：Atlas 以平台身份把统一契约做成可被中立层（含 VideoRouter 类路由）引用的标准：submit/poll/cancel/artifact + SHA256 产物校验 + 幂等重放，平台+契约双重身份是厂商自己永远做不到的位置

### 未解问题

- VideoRouter 定价页未写明预付/后付与 BYO-key 场景 2% 是否照收的执行细节；Synvia Corp 公司规模、融资与 fal/Replicate 关系未知
- muapi 低于 Fal 官方价 60%+ 的可持续机制不明（积分过期？套利？补贴引流？）；4.3k★ 与 1.9K npm 月下载的背离无法从公开数据定论主因（继承星 vs 刷量比例）
- skills.sh 安装计数口径未公开：顶部 5 技能 597.5K-599.5K 高度一致，需确认是否存在批量/机器人计数或统一渠道归因
- Atlas 对被 VideoRouter 等路由层的官方立场（接受转售、定价加成还是限制），以及若 2% 中立层长大，上游平台的反制手段
- vibeframe 停更 8 周的原因（单人放弃、转型还是被收编）——若其成本契约理念被大厂吸收，窗口期判断需修正

### 来源

- [VideoRouter 官网（定位、路由供应商、2% 费率、Atlas 上游）](https://videorouter.sh)
- [VideoRouter 定价页（2% vs OpenRouter 5.5%、含 Atlas 报价行）](https://videorouter.sh/pricing)
- [HN Algolia：VideoRouter 发布帖 2026-09-16（1 分 1 评论）](https://hn.algolia.com/api/v1/items/49733974)
- [HN Algolia：VideoRouter 早期帖 2026-09-11（Save 80%，2 分）](https://hn.algolia.com/api/v1/items/49667080)
- [HN 作者 franklin_yao（karma=1）](https://news.ycombinator.com/user?id=franklin_yao)
- [VideoRouter 官方 skills 仓库（synvia-corp，0★，CLI npm 包不存在）](https://github.com/synvia-corp/videorouter-skills)
- [vibeframe 仓库（168★，dry-run+max-cost 契约，2026-07-26 停更）](https://github.com/vericontext/vibeframe)
- [vibeframe 作者 Kiyeon Jeon 主页](https://github.com/kiyeonjeon21)
- [@vibeframe/cli npm 月下载 766](https://api.npmjs.org/downloads/point/last-month/@vibeframe/cli)
- [muapi Generative-Media-Skills（4316★，UTM homepage，2023 旧仓库转型）](https://github.com/SamurAIGPT/Generative-Media-Skills)
- [muapi 定价页（宣称低于 Fal 60-64%）](https://muapi.ai/pricing)
- [muapi-cli 仓库（Stripe topup 积分制）](https://github.com/SamurAIGPT/muapi-cli)
- [muapi-cli npm 月下载 1,934](https://api.npmjs.org/downloads/point/last-month/muapi-cli)
- [RunComfy 官方 skills（skills.sh + marketplace 插件）](https://github.com/runcomfy-com/skills)
- [RunComfy 官方 CLI（Rust，1★）](https://github.com/runcomfy-com/runcomfy-cli)
- [RunComfy 官方 MCP（31 工具）](https://github.com/runcomfy-com/runcomfy-mcp)
- [genmedia-labs/skills（匿名营销阵地，13★，3 commits）](https://github.com/genmedia-labs/skills)
- [skills.sh：genmedia-labs 3.8M 安装页](https://skills.sh/genmedia-labs/skills)
- [@runcomfy/cli npm 月下载 1,652](https://api.npmjs.org/downloads/point/last-month/@runcomfy/cli)
- [PixVerse 官方 CLI（MIT，capabilities.json 契约）](https://github.com/PixVerseAI/cli)
- [PixVerse 官方 skills 仓库](https://github.com/PixVerseAI/skills)
- [PixVerse execution-contract.md 原文](https://raw.githubusercontent.com/PixVerseAI/skills/main/skills/references/execution-contract.md)
- [PixVerse prompt-contract.md 原文](https://raw.githubusercontent.com/PixVerseAI/skills/main/skills/references/prompt-contract.md)
- [Comfy-Org comfy-skills（云插件+官方作者规则）](https://github.com/Comfy-Org/comfy-skills)
- [Comfy-Org comfy-mcp（本地 MCP，AGPL OR Commercial）](https://github.com/Comfy-Org/comfy-mcp)
- [Comfy-Org comfy-cli（974★，技能随二进制分发）](https://github.com/Comfy-Org/comfy-cli)
- [pixverse npm 月下载 4,275](https://api.npmjs.org/downloads/point/last-month/pixverse)
- [前期核查文档：fal vs RunComfy 分发通道（本地 video-ai-landscape 仓库）](file:///Users/lifcc/Desktop/code/AI/tools/video-ai-landscape/docs/research-vendor-next-moves-2026-09-22.md)

---

## 角色一致性技术路线（Wan2.2 LoRA / VACE / 商业 API 形态 / character_id 契约）

角色一致性技术路线深挖（截至 2026-09-22，全部依据可给出 URL 的一手来源）。结论：(1) 自训路线已完全可行——kohya musubi-tuner 官方文档明确支持 Wan2.1/2.2 LoRA，fp8+block swap 下"720x1280 图像训练仅需 24GB 显存"（wan.md 原文），Wan2.2 双 DiT（高/低噪声）可用 --dit_high_noise + --timestep_boundary（T2V 0.875 / I2V 0.9）联合或分段训练；tdrussell diffusion-pipe 支持 Wan2.2 但强制 Deepspeed 流水线并行（面向多卡），提供 wan_14b_min_vram.toml 极限显存配置，且已在 RTX 4090 上验证（PyTorch 2.9+CUDA 12.8）。(2) 单卡成本：RunPod RTX 4090 Community $0.34/hr、Secure $0.74/hr，RTX 5090 $0.69/$0.99，H100 SXM $2.69/$3.49；Modal 按秒计费 H100 $0.001097/s（约 $3.95/hr）、A100 80G 约 $2.50/hr、L40S 约 $1.95/hr（时薪为秒价×3600 折算，非官方报价）。按单卡 4090 训 24 小时估算约 $8-18，属于个人开发者可承受区间；但两平台定价页均无独立 spot/interruptible 档位（RunPod 的低价来自 Community Cloud，Modal 靠按秒计费实现弹性），"spot 补位"的真实形态是被抢占风险更低的社区云/按秒计费。(3) 参考控制路线：开源侧 VACE（Wan2.1-VACE-1.3B/14B，Apache-2.0，R2V 参考生成，--src_ref_images）与 ByteDance Phantom（Wan2.1 基座，单/多主体参考≤4 图，Apache-2.0）都停在 Wan2.1，尚无 Wan2.2 版本；闭源侧已收敛到"@名字"引用范式——Kling 3.0 Omni 的 contents[].type=element（element_id + @名称语法，单任务最多 3 个 element，配 Element Management API）、Vidu reference2video 的 subjects[]（每主体≤3 图、@subjectname 引用、总量≤7、viduq1-q3/2.0）、火山 Seedance 2.5 的 omni_reference_task_type + role=reference_image/reference_video（@图像1/@视频1 语法，doubao-seedance-2-5-260628）。(4) 数字人路线：HeyGen Avatar V 主打"Character consistency across every angle, expression, and video"，REST/CLI/MCP 接入、批量 100 请求/调用，但 API 单价藏在登录墙后；ByteDance OmniHuman-1/1.5（图像+音频驱动、1 分钟以上动态表演）明确闭源——官方页声明"we do not offer services/downloads anywhere"。(5) 修正性发现：fal.ai 已有 fal-ai/wan-trainer/t2v-14b（"Train custom LoRAs for Wan-2.1 T2V 14B"）——"训练设施厂商完全不做视频 LoRA 托管训练"的前提不成立，真实情况是覆盖极薄（仅 Wan2.1 T2V 一个模型，无 Wan2.2、无 I2V）。这为 character_id 契约 + 托管 Wan2.2 双专家 LoRA 训练配方留出明确机会：契约需包含数据集规格（视频+同名 .txt 字幕 / musubi JSONL）、LoRA 权重引用（区分高/低噪声 DiT、timestep_boundary）、trigger 词、一致性评测集、以及四套商业端点适配器（element_id / subjects / reference_image / avatar_id）。

### 关键信号

- **Kling 3.0 Omni 把角色资产变成一等 API 对象：contents[].type=element + Element Management API + @名称 prompt 引用，单任务最多 3 个 element，支持 multi_shot 1-6 镜头与 4k**（置信：官方源（kling.ai 端点文档全文抓取）；https://kling.ai/document-api/api/video/3-0-omni/image-to-video）
- **火山 Seedance 2.5 推出 omni_reference_task_type（全模态参考），content 支持 role=reference_image/reference_video 且可混排 @图像N/@视频N 引用，参考输入从图片扩展到视频**（置信：官方源（火山引擎 API 文档，2026-09-21 更新）；https://docs.volcengine.com/docs/ark/create-video-generation-task-api?lang=zh）
- **Vidu subjects 机制支持命名主体（@subjectname、每主体 3 图、7 个引用上限、viduq3 系列），并在 q2-pro 上把参考输入扩展到视频片段（8s×1 或 5s×2）**（置信：官方源（platform.vidu.com API 文档）；https://platform.vidu.com/docs/reference-to-video）
- **闭源与开源的能力差距正在从'画质'转向'角色资产管理'：HeyGen Avatar V 以跨视频一致性为卖点并配套 Avatar/Consent 管理端点，OmniHuman 坚持闭源不发放权重**（置信：官方源（developers.heygen.com、omnihuman-lab.github.io）；https://developers.heygen.com/）
- **开源参考控制基座停留在 Wan2.1：VACE 仓库最后一次实质更新为 2025-10-17（benchmark 更新），模型列表无 Wan2.2；Phantom 亦为 Wan2.1 基座——Wan2.2 参考控制是开源社区可见的下一个空白**（置信：官方源（仓库现状推断，注意'无 Wan2.2 VACE'为截至抓取日的缺席证据，非官方声明）；https://github.com/ali-vilab/VACE）
- **托管视频 LoRA 训练开始萌芽但极薄：fal.ai 仅 wan-trainer/t2v-14b（Wan2.1），图像侧 trainer 则已形成产品线（FLUX 系 5 个、Qwen、Z-Image）——预计视频 trainer 会按图像侧路径逐步补齐**（置信：官方源（fal.ai 页面；趋势判断为推断）；https://fal.ai/explore/best-lora-trainers）
- **训练框架活跃度集中在 musubi-tuner（2026-09 仍在合并多架构 PR，扩展到视频+音频联合训练），单人维护的 diffusion-pipe 走多卡 Deepspeed 路线——单卡配方以 musubi 为事实标准**（置信：官方源（两仓库 README/changelog 交叉）；https://github.com/kohya-ss/musubi-tuner）

### 要点 / 模式清单

- 自训 Wan2.2 角色 LoRA 的显存门槛已被官方文档证明在消费级可达（24GB + fp8 + block swap），单卡 4090 云租成本低于 $1/hr，技术可行性不再是瓶颈
- 商业 API 三巨头（Kling/Vidu/Seedance）在多参考引用上独立收敛到 '@名称 + 资产 ID' 范式，说明 character_id 契约有清晰的行业原型可抽象
- 开源参考控制模型（VACE、Phantom）均为 Apache-2.0 且权重开放，允许将参考控制能力与自训 LoRA 组合进同一 pipeline，不受许可证约束

### 空位与建议

- **跨厂商角色资产无统一标准：Kling 用 element_id（Element Management API 托管）、Vidu 用 subjects[]（name+images）、Seedance 用 content[].role=reference_image/reference_video、HeyGen 用 avatar_id（Avatar Management 端点），四套角色引用机制互不兼容且平台内资产不可导出**
  - 证据：Kling：POST /image-to-video/kling-3.0 的 contents 元素 type=element（element_id+id，最多 3 个）https://kling.ai/document-api/api/video/3-0-omni/image-to-video；Vidu：POST /ent/v2/reference2video 的 subjects 数组 https://platform.vidu.com/docs/reference-to-video；Seedance：omni_reference_task_type + @图像1 语法 https://docs.volcengine.com/docs/ark/create-video-generation-task-api?lang=zh；HeyGen：Avatar Management（Create Avatar/Avatar Consent/Avatar Groups/Avatar Looks）https://developers.heygen.com/
  - 建议：character_id 契约设计为一层可迁移资产描述（数据集清单+LoRA 权重引用含 Wan2.2 高/低噪声双 DiT 与 timestep_boundary+trigger 词+一致性评测集），并实现四个端点适配器把同一角色投射到 element_id/subjects/reference_image/avatar_id；这是所有厂商都没做的集成位
- **开源参考控制模型停留在 Wan2.1 基座：VACE 最新版本为 Wan2.1-VACE-1.3B/14B（2025-05 发布，仓库最后更新 2025-10-17），无 Wan2.2 VACE；Phantom 也是 Wan2.1 基座（2025-05-27 发布 14B）**
  - 证据：VACE README 模型列表仅 Wan2.1-VACE 与 VACE-LTX，无 Wan2.2 条目 https://github.com/ali-vilab/VACE；Phantom README 明确 'Phantom-Wan model relies on the Wan2.1 VAE and Text Encoder' https://github.com/Phantom-video/Phantom
  - 建议：用 musubi-tuner 在 Wan2.2 上自训角色 LoRA 是当前唯一开源路径；训练配方应显式处理双专家结构（先训低噪声 DiT 0-875/0-900 段再训高噪声段，或联合训练），这是 Wan2.1 教程没有的新问题
- **托管视频 LoRA 训练覆盖极薄且停在上一代：fal.ai 仅有 wan-trainer/t2v-14b（Wan2.1 T2V 14B），无 Wan2.2/无 I2V trainer；Replicate 搜索无 Wan LoRA trainer；RunPod/Modal 只卖裸算力不提供托管训练**
  - 证据：fal.ai Best Lora Trainers 列表含 'fal-ai/wan-trainer/t2v-14b — Train custom LoRAs for Wan-2.1 T2V 14B'，其余 9 个 trainer 全是图像模型 https://fal.ai/explore/best-lora-trainers；RunPod 定价页只有 Community/Secure/Serverless 算力档位 https://www.runpod.io/pricing；Modal 只有按秒 GPU 单价 https://modal.com/pricing
  - 建议：技术上难在：Wan2.2 双 DiT 使显存翻倍（musubi 文档：Windows 下 fp8 仍需约 42GB 共享显存、约 96GB 内存），14B 需要 Deepspeed 流水线并行（diffusion-pipe 强依赖），视频数据集需预缓存 latents/T5——这些使 serverless 单卡托管难以套用图像 LoRA 的产品形态。商业机会是用 musubi 单卡配方（fp8+block swap，24GB）做成托管任务队列，主打 4090/5090 低价档（$0.34-0.99/hr）
- **RunPod/Modal 均无真正的 spot/interruptible GPU 档位公开标价，'spot GPU 补位'的常见叙事与现价页不符**
  - 证据：RunPod 定价页仅列出 Community Cloud 与 Secure Cloud 两档及 Serverless 单价，无 bid/spot 字段 https://www.runpod.io/pricing；Modal 全部 GPU 按秒计价、无抢占式实例类别 https://modal.com/pricing
  - 建议：成本估算应以 Community Cloud（4090 $0.34/hr）和按秒计费（Modal L40S $1.95/hr 折算）为基准：单角色 LoRA 若需 12-24 单卡小时，成本区间约 $4-24，训练瓶颈是数据集预处理与双 DiT 显存而非单价；真正缺口是断点续训支持（spot 被抢占后恢复）
- **开源生态缺少面向角色一致性的公开评测集：VACE-Benchmark 面向编辑/生成任务，没有跨模型（VACE vs Phantom vs 商业 API）的角色一致性基准**
  - 证据：VACE README 提到 'VACE-Benchmark has been updated to incorporate the evaluation data'（2025-10-17）但评测对象是 VACE 自身任务族 https://github.com/ali-vilab/VACE；Phantom 只发布了训练数据集 Phantom-Data https://github.com/Phantom-video/Phantom
  - 建议：character_id 契约内建小型一致性评测集（同一角色跨 5-10 个场景/表情/光照的参考-生成对）+ 自动评分（人脸相似度+CLIP/DINO 特征距离），使'角色资产'可验收、可对比商业 API 输出
- **数字人路线闭源且 API 价格不透明：OmniHuman-1/1.5 官方明确不提供下载与服务；HeyGen API 单价藏在登录墙后的 pricing modal**
  - 证据：OmniHuman 官方页：'Currently, we do not offer services/downloads anywhere' https://omnihuman-lab.github.io/；OmniHuman-1.5 论文 arXiv:2508.19209（2025-08）https://omnihuman-lab.github.io/v1_5/；HeyGen 定价页仅有订阅套餐（Creator $29/Pro $49/Business $149 每月），API 价格链接指向 app.heygen.com 登录后弹窗 https://www.heygen.com/pricing
  - 建议：对需要可自托管/可导出的角色资产的用户，开源 Wan2.2 LoRA + 音频驱动（musubi 已支持 MiniMax-H3 视频+音频联合训练，2026-09-16 起）是唯一非锁定路线

### 未解问题

- Kling 3.0 / 3.0 Omni 的正式上线日期与 element 相关计费单价（文档确认能力存在，但定价页为 SPA 未能抓取；2.5 Turbo 的价格本次也未取得一手数字）
- Seedance 2.5 全模态参考的参考图/视频数量上限、分辨率档位与刊例价（使用必读与定价子页未抓取正文；0.2/0.6 元每秒为 2.0 mini/fast 促销价）
- HeyGen API 的具体计费结构（登录墙后），以及 Avatar V 是否开放非人形角色
- OmniHuman 是否会经由即梦/火山引擎开放 API（官方页否认任何服务，但产品化路径未知）
- Wan2.2 版 VACE 或 Phantom 是否会在社区出现（Kijai ComfyUI wrapper 生态是否会补位）
- 上一轮报告中'七家训练设施厂商'的具体名单不在本会话上下文中，本结论基于本次直接验证的 fal.ai/Replicate/RunPod/Modal 四家，其余厂商未能逐一核实
- musubi-tuner 在 24GB 单卡上训练 Wan2.2 视频 LoRA 的实际吞吐（小时/迭代数）缺少官方基准，训练时长与总成本只能给区间估算

### 来源

- [kohya-ss/musubi-tuner（README：支持 Wan2.1/2.2 等，显存建议与更新日志）](https://github.com/kohya-ss/musubi-tuner)
- [musubi-tuner docs/wan.md（Wan2.2 双 DiT 训练、fp8+block swap 24GB、timestep_boundary）](https://github.com/kohya-ss/musubi-tuner/blob/main/docs/wan.md)
- [tdrussell/diffusion-pipe（README：Wan2.2 支持、Deepspeed 流水线并行、4090 验证、数据集格式）](https://github.com/tdrussell/diffusion-pipe)
- [ali-vilab/VACE（README：R2V 参考生成、Wan2.1-VACE 1.3B/14B 权重、Apache-2.0、更新记录）](https://github.com/ali-vilab/VACE)
- [Phantom-video/Phantom（README：ByteDance 单/多主体参考、Wan2.1 基座、Apache-2.0、HuMo 后续）](https://github.com/Phantom-video/Phantom)
- [Kling AI 文档 Capability Map（Kling 3.0 & 3.0 Omni：element reference，high consistence）](https://kling.ai/document-api/guides/get-started/capability-map)
- [Kling 3.0 Omni Image to Video API（contents[].type=element、element_id、@名称、最多 3 个 element、4k/10s/multi_shot）](https://kling.ai/document-api/api/video/3-0-omni/image-to-video)
- [Vidu platform 文档 Reference to Video（POST /ent/v2/reference2video、subjects/@subjectname、每主体 3 图、总量 7）](https://platform.vidu.com/docs/reference-to-video)
- [火山方舟 创建视频生成任务 API（Seedance 2.5 全量公开、omni_reference_task_type、role=reference_image/reference_video、@图像N 语法、2.0 促销价）](https://docs.volcengine.com/docs/ark/create-video-generation-task-api?lang=zh)
- [BytePlus ModelArk 文档导航（Seedance 2.5/2.0 教程与 portrait videos 条目，最后更新日期）](https://docs.byteplus.com/en/docs/ModelArk)
- [HeyGen 开发者门户（Avatar V character consistency、Avatar Management 端点、REST/CLI/MCP、批量 100 请求）](https://developers.heygen.com/)
- [HeyGen 定价页（Creator $29 / Pro $49 / Business $149 等，API 价格不在本页）](https://www.heygen.com/pricing)
- [OmniHuman 官方项目页（闭源声明：do not offer services/downloads anywhere；arXiv:2502.01061）](https://omnihuman-lab.github.io/)
- [OmniHuman-1.5 项目页（图像+音频驱动、System1/2 双系统、arXiv:2508.19209）](https://omnihuman-lab.github.io/v1_5/)
- [fal.ai Best Lora Trainers（fal-ai/wan-trainer/t2v-14b 为唯一视频 trainer；其余为图像 trainer）](https://fal.ai/explore/best-lora-trainers)
- [RunPod 定价页（4090 $0.34/$0.74、5090 $0.69/$0.99、H100 SXM $2.69/$3.49；无 spot 档位）](https://www.runpod.io/pricing)
- [Modal 定价页（按秒计费：H100 $0.001097/s、A100 80G $0.000694/s、L40S $0.000542/s）](https://modal.com/pricing)

---

## 判片与验收层设计（VBench / VLM judge / 抽帧 / verdict schema）

# 判片/验收层设计深挖（judge rubric + verdict schema 设计输入）

## a) 先例体系
**VBench（官方仓库已核对，16 维，精确名称）**：质量 7 维——`subject_consistency`、`background_consistency`、`temporal_flickering`、`motion_smoothness`、`dynamic_degree`、`aesthetic_quality`、`imaging_quality`；语义 9 维——`object_class`、`multiple_objects`、`human_action`、`color`、`spatial_relationship`、`scene`、`temporal_style`、`appearance_style`、`overall_consistency`。权重与归一化在 `scripts/constant.py` 开源。VBench-2.0（arXiv 2503.21755）转向"内在忠实度"：18 个细粒度维度覆盖物理合理性/常识推理/人体运动，但具体维度名未在 README 列出。**关键启示**：temporal_flickering/motion_smoothness 这类维度 VLM 在低帧率下不可见，判片维度必须按"VLM 可判性"重新分层。
**VideoFeedback（TIGER-Lab，官方 HF 页核对）**：33.6k 条（test 680），每条 8-24 帧 JPG + prompt + mp4 链接 + **5 个整数分**：visual quality / temporal consistency / dynamic degree / text-to-video alignment / factual consistency；数据页观测为 1-4 分制（中置信，与论文口径需复核）；标注方式即"GPT-4V 扮演判片专家"的多轮对话——这就是 VLM-as-judge 判视频的最直接数据先例，可直接取样本做 judge few-shot 校准。
**EvalCrafter（CVPR 2024）**：17 个客观指标 + 8.6k 人工标注（5 个方面，明确含 visual quality 与 t2v alignment），工具箱含 RAFT（光流）、DOVER、CLIP 等——光流在评测界是**运动度量**而非选帧手段。
**图像域 VLM-as-judge 产品化先例**：VIEScore（官方仓库核对）对图像生成/编辑输出 SC（语义一致）+ PQ（感知质量）+ Overall 三分，`--mllm` 支持 gpt4v/gpt4o/gemini 等 10 种后端，官方 news 声明"GPT-4o 达到与人类 on par 的相关性"；仓库内已有 `t2v` 任务标记。DALL-E 3 报告用 GPT-4V 做自动评测是业界惯例（单一来源、本次未复核一手 PDF，低置信）。

## b) Judge 候选 VLM 能力矩阵（全部官方一手来源）
| 模型 | 视频输入 | 关键机制 | 价格/1M（in/out） | 判片适配 |
|---|---|---|---|---|
| **Gemini 3.8 Flash** | 原生 mp4/mov/webm 等 9 种 | **agentic 模式**（`"processing":"agentic"`）：模型"选择性查看 transcript、动态调整帧率与分辨率"，response steps 出现 `processing_call/processing_result` 即自导航时间线；官方称长视频"最多省 88% token、质量 +7%"。静态模式默认 1FPS，低分辨率 66 token/帧、高分辨率 258 token/帧，音频 32 token/秒；自定义 fps 与裁剪仅静态模式；prompt 可引用 MM:SS 时间戳 | $0.75/$3.75（促销价至 2026-12-31，之后 $1.50/$7.50）；Batch 半价 | 首选 judge：原生视频 + 时间戳引用 + 自适应抽帧，10s 判片成本约 $0.005 |
| **Qwen3-VL**（235B-A22B-Instruct） | 原生视频，"小时级视频全召回 + 秒级索引"，Text-Timestamp Alignment 时间戳定位 | 默认 fps=2，视频 token 预算上限 16384，上下文 256K（YaRN factor=3 可扩 1M） | OpenRouter 实测：$0.21/$1.9（235B）、$0.13/$0.52（30B-A3B）、$0.117/$0.455（8B）、$0.104/$0.416（32B）；OpenRouter 侧 input_modalities 仅 text+image（视频需转帧图传入） | 失败事件秒级定位最佳；自建推理可自控抽帧 |
| **Claude（全系）** | **无视频输入，官方原文："Animations are unsupported, and only the first frame is used"（GIF 只取首帧）** | 规避方案：抽帧转多图。API 单请求最多 600 张；**超过 20 张触发 2000px 长边硬限**（否则 invalid_request_error）；1920×1080 帧标准档降采样到 1456×819=1560 token，高分辨率档（4.7+）4784 token | 10 帧 ≈ 15.6K token，Haiku 4.5（$1/1M）约 $0.016/次——比 Gemini 原生贵 3-5 倍 | 仅适合"网格拼图"式降采样判片（如 3×3 网格=1 张图），不推荐做主 judge |
| **GLM-4.6V**（z.ai 官方） | 支持视频（Input Modality: Video/Image/Text/File），128K 上下文，"一次推理约一小时视频" | 原生 Function Calling；具体帧/像素上限文档未给 | $0.3/$0.9；FlashX $0.04/$0.4；**Flash 免费** | Flash 免费/FlashX 做"粗筛级"，FlashX 价格约为 Gemini 的 1/10 |
| **DeepSeek V4.1-Flash**（官方定价页） | 定价页标 vision ✓（deepseek-v4-pro 无视觉）；**是否支持视频未确认** | 1M 上下文；峰谷价差 2 倍（谷时=UTC 周一至五 01-04 及 06-10 点） | in $0.15（谷）/ $0.3（峰）；out $0.6/$1.2 | 若支持视频则为谷时批量判片的低价选项，需先验证 |

## c) 抽帧方案对比
- **均匀抽帧**：Gemini 静态默认 1FPS、Qwen 默认 2FPS。成本可预测、全片覆盖；但瞬时缺陷（闪烁单帧伪影）与慢漂移可能落在帧间。10s@1080p 在 Gemini 低分辨率 = 660 token（≈$0.0005）。
- **关键帧/查询自适应**：VideoTree（CVPR 2025）证明 query 相关的树式选帧优于均匀聚类选帧，对"对齐度"维度最有效；缺点是"质量/一致性"等全局维度可能因选帧偏置失真。Gemini agentic 模式内部即此机制，但**黑盒不可控**（无法保证每维度的覆盖度）。
- **光流选帧**：无公开的判片选帧方案（光流在 EvalCrafter/VBench 里只做运动度量）；RAFT 逐帧对计算成本高。判片场景的空白点。
- **推荐混合**：第一段均匀低分辨率全片（Gemini 静态 low res）→ verdict 标记可疑时间窗 → 第二段对可疑窗 agentic/高分辨率复核。成本约为单次纯 agentic 的 1.5 倍，但每维度证据可审计。

## d) 设计草案
### verdict JSON schema v1.0
```json
{
  "verdict_version": "1.0",
  "generation": {"generation_id": "gen_xxx", "provider_model": "...", "request": {"prompt": "...", "params": {"seed": 0, "duration_s": 10, "resolution": "1080p"}}, "artifact": {"video_url": "...", "sha256": "..."}},
  "evidence": {"sampling": {"method": "uniform|adaptive|two_pass", "fps_sent": 1.0, "n_frames": 10, "timestamps_s": []}, "judge": {"model": "gemini-3.8-flash", "processing": "agentic", "tokens_in": 0, "tokens_out": 0, "cost_usd": 0.0, "rubric_version": "r1"}},
  "alignment": {"elements": [{"element_id": "e1", "type": "subject|action|scene|style|count|text|camera", "text": "prompt 原文片段", "present": true, "timestamps_s": [1.5], "note": "..."}], "adherence_score": 8.5, "missing": ["e3"], "contradicted": []},
  "dimensions": [{"id": "prompt_adherence|subject_consistency|temporal_consistency|motion_quality|visual_quality|aesthetics|safety_overlay", "score": 8.5, "confidence": 0.9, "evidence_ts_s": [1.5, 4.0]}],
  "failures": [{"code": "IDENTITY_DRIFT", "severity": "minor|major|hard", "timestamps_s": [6.0], "description": "主角发色第6秒改变"}],
  "failure_codes": ["PROMPT_OMISSION","PROMPT_CONTRADICTION","COUNT_ERROR","SPATIAL_RELATION_ERROR","TEXT_RENDER_ERROR","IDENTITY_DRIFT","OBJECT_VANISH","OBJECT_DUPLICATE","MORPHING","FLICKER","GHOSTING","MOTION_ARTIFACT","PHYSICS_VIOLATION","ANATOMY_ERROR","WATERMARK_LOGO","COMPRESSION_ARTIFACT","COLOR_SHIFT","FRAMING_ISSUE","UNSAFE_CONTENT"],
  "overall": {"score": 7.8, "verdict": "pass|conditional_pass|fail", "confidence": 0.85, "one_line": "..."},
  "action": {"recommended": "accept|retry_same_model|retry_other_model|revise_prompt|abandon", "reason": "...", "hints": {"target_failure_codes": ["IDENTITY_DRIFT"], "prompt_suggestion": "...", "fallback_model": "..."}, "retry_budget_left": 1}
}
```
**判定→动作映射（写进 rubric 尾部）**：overall≥8 且无 major/hard 失败且 adherence≥7 → accept；adherence 缺失/矛盾（PROMPT_OMISSION/CONTRADICTION/COUNT/SPATIAL）→ revise_prompt；FLICKER/ARTIFACT/MOTION 等瞬态类且 overall≥5 → retry_same_model（换 seed）；IDENTITY_DRIFT/PHYSICS_VIOLATION 且当前模型已知此弱点 → retry_other_model；hard 失败（UNSAFE/WATERMARK）或重试 2 次后仍 <5 → abandon。

### judge rubric（可整段贴 system prompt）
```
你是 AI 生成视频的验收判片员。输入：原始 prompt + 按时间戳标注的帧序列。规则：
1) 先证据后打分：每个维度分数必须引用 MM:SS 时间戳，无证据的分数无效。
2) 只扣 prompt 要求的东西：prompt 未提及的属性不扣 alignment 分。
3) 分制 0-10 锚点：9-10 优秀（该维度无可挑剔）；7-8 良好（轻微瑕疵不影响使用）；5-6 及格（明显缺陷但仍可用）；3-4 差（影响观感/偏离要求）；0-2 崩坏（不可用）。
4) prompt_adherence：9-10=所有元素出现且无矛盾；7-8=主要元素在、次要缺失；5-6=主体对但动作/风格偏；0-4=主体错误或与 prompt 相反。
5) subject_consistency：0-4=身份改变/换人；5-6=衣着发型漂移；7-8=轻微变化；9-10=跨帧完全稳定。
6) temporal_consistency：9-10=背景物体无闪变；5-6=局部闪烁/物体短暂消失；0-4=场景突变级不一致。
7) motion_quality：0-4=运动崩溃/形变；5-6=卡顿滑步；7-8=偶发抖动；9-10=平滑且符合物理。
8) visual_quality：按伪影/模糊/压缩逐级；aesthetics：构图/色彩/光影。
9) safety_overlay 为硬性项：水印/logo/不当内容 → 直接在 failures 记 hard 并给 verdict=fail。
10) 不确定时给保守分并降低 confidence 字段；两难时以"用户会不会要求退款"为准。
11) 输出仅限 verdict JSON，禁止额外文本。
```

## 总成本参考（10s 1080p 单次判片，官方价推算）
Gemini 3.8 Flash 静态低分辨率 ≈ $0.005（980 in + 1K out token）；agentic 短视频成本相近、TTFT 略增；Qwen3-VL 235B（OpenRouter）≈ $0.006；GLM-4.6V-FlashX ≈ $0.001；Claude 帧图方案 ≈ $0.016 且受 20 张/2000px 限制。批量验收层建议：GLM-Flash 免费粗筛 → Gemini 3.8 agentic 精判 → 争议样本 Claude 高分辨率网格复核。

### 关键信号

- **Gemini Flash 系促销价 2027-01-01 起翻倍（$0.75→$1.50 in，$3.75→$7.50 out），验收层单位成本预算须按 2 倍规划；Batch 接口现半价可部分对冲**（置信：官方定价页，高置信；https://ai.google.dev/gemini-api/docs/pricing）
- **Gemini agentic 视频处理已从旗舰下沉到 3.5 Flash-Lite（$0.30/$2.50 档），判断：能力向廉价层扩散，2027 年低阶模型判片可能够用**（置信：官方文档列出可用模型清单，高置信（扩散速度为推断）；https://ai.google.dev/gemini-api/docs/video-understanding）
- **DeepSeek 峰谷定价制度化（谷时半价、UTC 周一至五 01-04/06-10 点），夜间批量判片/回归评测有 50% 成本套利空间**（置信：官方定价页，高置信；https://api-docs.deepseek.com/quick_start/pricing）
- **Qwen3-VL 上下文 256K→1M（YaRN factor=3）官方支持路径，单次判小时级视频（验收长视频）在权重层面已无障碍，等推理栈（vLLM/SGLang）跟进**（置信：官方 README，高置信；https://github.com/QwenLM/Qwen3-VL）
- **Gemini YouTube URL 直传为免费预览功能（免费层 8 小时/天，Gemini 2.5+ 单请求 10 个视频），竞品参考视频分析可零成本**（置信：官方文档，高置信；https://ai.google.dev/gemini-api/docs/video-understanding）
- **VBench-2.0 转向'内在忠实度'（物理合理性/常识/人体运动 18 维）并支持自定义视频单维评测——学界评测重心正转向判片层需要的维度**（置信：官方仓库描述，中置信（18 维具体名单未在 README 列出）；https://github.com/Vchitect/VBench）

### 要点 / 模式清单

- VBench 16 维体系与权重表完全开源（scripts/constant.py），判片维度体系可直接抄作 baseline，不必自造维度名
- VideoFeedback 33.6k 条 GPT-4V 判片标注（8-24 帧+prompt+5 维分数+推理文本）可直接抽 test 680 条做 judge 的 few-shot 校准集与打分回归测试集
- VIEScore 已验证 GPT-4o/Gemini 作为 judge 与人类相关性 on par（官方 news 声明），且代码已含 t2v 任务标记——图像判片范式有可迁移实现
- Gemini 3.8 Flash agentic 视频处理 + MM:SS 时间戳引用 + steps 可观测（processing_call/result）是工程上最短路径：抽帧、定位、判分三件事在单次 API 调用内完成
- Qwen3-VL 秒级时间戳定位（Text-Timestamp Alignment）+ 自建推理可自控抽帧，是唯一能自托管的高能力视频 judge
- GLM-4.6V-Flash 免费档 + FlashX $0.04/$0.4 使两级判片（免费粗筛+付费精判）在成本上成立
- DeepSeek 谷时半价（UTC 周一至五 01-04/06-10 点）适合夜间批量复判/回归评测

### 空位与建议

- **所有现有评测基准（VBench/VideoFeedback/EvalCrafter）都是'评模型排行榜'设计，输出单一加权总分，没有'单次生成是否可接受 + 下一步动作'的决策层——verdict→action 映射（retry/换模型/改 prompt/放弃）在任何公开方案中都不存在**
  - 证据：VBench Total Score 是 Quality 与 Semantic 的加权平均（README 明示）；VideoFeedback 每行只有 5 个整数分列，无 action/verdict 字段（官方 HF 数据页核对）
  - 建议：设计验收层时把 failure_codes 枚举→action 的映射做成一等公民并记录 retry 预算，这是与所有基准的差异化点，也可沉淀为失败模式数据集
- **维度对输入粒度的依赖不同但没有任何方案做'按维度分配帧率'的分诊：temporal_flickering/motion_smoothness 需要高帧率或光流才可见，VLM 1FPS 均匀抽帧下系统性盲判；Gemini agentic 自适应是黑盒，无法保证质量维度覆盖度**
  - 证据：VBench 官方说明仅 6 个维度支持自定义视频输入（flickering/smoothness 依赖专用指标而非 VLM）；Gemini 文档明示自定义 fps 仅静态模式、agentic 帧率由模型自调
  - 建议：两段式判片（低分辨率全片→可疑时间窗高分辨率/agentic 复核）+ 维度级 evidence_ts 审计，把'看不见的维度'显式降 confidence 而非假装打了分
- **Claude/文本强模型无视频输入的规避方案没有产品化实现：多帧图超 20 张触发 2000px 硬限、网格拼图损失细节，均无公开的判片级方案与精度损失数据**
  - 证据：Claude 官方文档：'Animations are unsupported, and only the first frame is used'；>20 图触发 many-image 2000px 限制并返回 invalid_request_error（官方原文核对）
  - 建议：若需要 Claude 做判片（推理能力强），网格拼图+局部裁剪二次判的两跳方案是空白，可建立'拼图粒度 vs 判分精度'的内部基准
- **光流/运动感知选帧在判片场景没有任何公开方案：光流只出现在评测指标里（RAFT 在 EvalCrafter 工具箱），选帧文献（VideoTree 等）全部基于 CLIP/查询相似度，对'运动崩溃/形变'类失败的捕捉靠运气**
  - 证据：EvalCrafter README 列出 RAFT 为指标依赖；VideoTree 为 query-adaptive 树式选帧（CVPR 2025），无生成质量判断应用（官方仓库核对）
  - 建议：低成本变体：ffmpeg 场景切换检测 + 帧差分作为'运动异常'选帧信号，喂给 judge 做定点复核，成本远低于 RAFT
- **视频 judge 自身的打分一致性（同视频重判方差、judge 换版本漂移）无公开数据：图像域有 VIEScore 的相关性验证，视频域 VideoFeedback 只发布了标注没发布 judge 一致性指标**
  - 证据：VideoFeedback 官方页只含 5 维分数与对话标注；VIEScore 相关性声明仅覆盖图像任务（两个官方仓库核对）
  - 建议：验收层上线即跑 test-retest：同 50 条样本×2 次判分，监控分数方差与 verdict 翻转率，rubric 加版本号使 judge 升级可回溯——这是内部基础设施资产
- **判片成本无公开基准：Gemini '省 88%' 只声明长视频场景；短视频（5-10s 生成物）各 judge 的实际 token/成本/一致性权衡零公开数据**
  - 证据：Gemini 文档：88% 节省限定'long-form content'，且明示短视频 agentic 'may slightly increase TTFT (<5 minutes)'（官方原文）
  - 建议：用同一批生成物在 Gemini 静态/agentic、Qwen3-VL、GLM-FlashX 四档跑成本-一致性矩阵，输出内部'每美元判片量'基线；促销价窗口（2026-12-31 截止）内建 cheapest-first 路由

### 未解问题

- DeepSeek V4.1-Flash 的 vision 输入是否支持视频（定价页只标 vision ✓，未写视频格式/帧限制）——若支持，其谷时半价是最便宜的批量判片选项之一
- GLM-4.6V 视频输入的帧数/像素/文件大小上限在文档页未给出，需查 API reference 或实测
- VideoFeedback 分数口径冲突：HF 数据页观测为 1-4 整数，论文常被引述为其他分制——用作校准集前需对照论文原始标注 prompt
- Gemini agentic 模式的 thinking/tool_use token 计费细节（是否全部按 output 价）与短视频场景的实际节省率需实测
- Gemini 3.8 Flash 的准确发布日期与 3.7/3.6 的能力差异（定价页同价，文档未给差异表）
- judge 换版本（如 Gemini 3.8→4.x）时 rubric 分数漂移幅度——需要建立内部回归集后才能回答
- DALL-E 3 报告中 GPT-4V 自动评测细节本次未能复核（PDF 超 WebFetch 体积上限），仅低置信引用

### 来源

- [VBench（Vchitect）官方仓库：16 维评测体系与权重](https://github.com/Vchitect/VBench)
- [Gemini API 文档：Video Understanding（agentic 模式、88% token 节省、1FPS 默认、token 计算）](https://ai.google.dev/gemini-api/docs/video-understanding)
- [Gemini API 官方定价页（3.8 Flash 促销价至 2026-12-31、各档 Flash-Lite 价格）](https://ai.google.dev/gemini-api/docs/pricing)
- [Qwen3-VL 官方仓库（小时级视频+秒级索引、fps=2 默认、16384 token/视频、256K→1M）](https://github.com/QwenLM/Qwen3-VL)
- [Claude Vision 官方文档（动画不支持仅取首帧、600 张/请求、20 张触发 2000px 限制、token 计算）](https://platform.claude.com/docs/en/build-with-claude/vision)
- [VideoFeedback 数据集（TIGER-Lab，33.6k，5 维分数，GPT-4V 判片标注）](https://huggingface.co/datasets/TIGER-Lab/VideoFeedback)
- [z.ai 官方定价（GLM-4.6V $0.3/$0.9、FlashX $0.04/$0.4、Flash 免费）](https://docs.z.ai/guides/overview/pricing)
- [GLM-4.6V 模型文档（视频输入、128K 上下文、原生 Function Calling）](https://docs.z.ai/guides/vlm/glm-4.6v)
- [DeepSeek 官方定价（V4.1-Flash vision、峰谷半价、v4-pro 无视觉）](https://api-docs.deepseek.com/quick_start/pricing)
- [VIEScore 官方仓库（SC/PQ/O 三分、GPT-4o 与人类相关性 on par、t2v 任务标记）](https://github.com/TIGER-AI-Lab/VIEScore)
- [VideoTree 官方仓库（CVPR 2025，query-adaptive 树式关键帧选择）](https://github.com/Ziyang412/VideoTree)
- [EvalCrafter 官方仓库（CVPR 2024，17 客观指标+8.6k 人工标注，RAFT 光流指标）](https://github.com/evalcrafter/EvalCrafter)
- [OpenRouter 公开模型 API（Qwen3-VL 全系实测定价与模态）](https://openrouter.ai/api/v1/models)

---

## 合规与标准（内容标识办法 / C2PA / SKILL.md 治理 / MCP 演进）

合规与标准深挖结论（截至 2026-09-22，全部基于一手来源实测/抓取）：中国侧，《人工智能生成合成内容标识办法》（国信办通字〔2025〕2号，2025-09-01 施行）与强制性国标 GB 45438-2025（2025-02-28 发布、2025-09-01 实施、现行）构成"显式标识（视频：起始画面+播放周边显著提示，下载导出须保留）+ 隐式标识（文件元数据须含生成合成属性、服务提供者名称/编码、内容编号）"双层义务，传播平台有三情形核验义务（办法第6条），用户可依第9条约定"无显式标识交付"但需协议+≥6个月日志。四家视频 API 实测（官方文档抓取）：可灵 `options.watermark_info.enabled` 默认 false、火山方舟 Seedance `watermark` 默认 false、Vidu `watermark` 默认不加（但默认水印文案即"内容由AI生成"，支持 `wm_url` 定制与 `watermarked_url` 返回）、MiniMax 英文 API 全文档零水印参数——即显式标识责任系统性落在调用方，且无一家文档化 AIGC 隐式元数据输出（第5条符合性盲区，契约需设计 label_required / implicit_metadata / c2pa / 责任划分字段）。国际侧，C2PA 规范已到 2.3，TikTok/OpenAI/Google/Meta 均在指导委员会；YouTube 官方确认会依据 C2PA 元数据或内部检测自动打 AI 标、反复不披露可下架或取消 YPP 资格。规范治理侧，SKILL.md 由 Anthropic 首创后"以开放标准发布、向生态开放贡献"（agentskills.io 官方原文），未见捐入中立基金会、无规范版本号/变更日志/兼容承诺，`allowed-tools` 仍标注 Experimental（"支持程度因 agent 实现而异"）——第三方 skill 存在兼容风险，规格内已提供 `compatibility` 字段与 skills-ref 校验器作缓解。MCP 当前版本 2026-07-28 完成无状态化重构："Stateless, self-contained requests"+按请求版本/能力协商（`_meta` + `MCP-Protocol-Version` 头）+强制 `server/discover`；Roots/Sampling/Logging/动态客户端注册被弃用（最早 2027-07-28 可移除），HTTP+SSE 传输可在 SEP-2596 转 Final 三个月后移除；长任务应迁移到 Tasks 扩展（`io.modelcontextprotocol/tasks`：CreateTaskResult/taskId 持久化/轮询/input_required 中途输入/取消），其语义与视频生成这类分钟级任务高度契合，但属 opt-in 扩展、客户端支持矩阵未定。

### 关键信号

- **MCP 弃用特性移除窗口：Roots、Sampling、Logging、动态客户端注册最早 2027-07-28 起的修订版可被正式移除；HTTP+SSE 传输在 SEP-2596 转 Final 三个月后即可移除——依赖旧传输/特性的集成需在窗口内迁移**（置信：官方源（modelcontextprotocol.io/specification/2026-07-28/deprecated 弃用注册表原文）；https://modelcontextprotocol.io/specification/2026-07-28/deprecated）
- **MCP 'Skills over MCP' 工作组已出现在 2026-07-28 规范页扩展/社区章节，Agent Skills 与 MCP 生态正在合流——skill 分发方式可能从文件复制演进为 MCP 发现/消费**（置信：官方源（spec 概览页列出该工作组链接）；https://modelcontextprotocol.io/specification/2026-07-28/）
- **YouTube 自动检测与自动打标会随 C2PA 普及扩大：官方明确 C2PA 元数据与内部检测均可触发自动 AI 标签，且该类标签创作者不可自行更正**（置信：官方源（YouTube 帮助中心原文）；https://support.google.com/youtube/answer/14328491）
- **Vidu 把'内容由AI生成'固化为默认水印文案并允许 wm_url 自定义——国产厂商已开始把 AIGC 显式标识做成产品能力，预计其余厂商将跟进把默认值翻转为默认加水印**（置信：官方源（Vidu 文档）+趋势推断（推断部分置信度：低）；https://platform.vidu.cn/docs/text-to-video）
- **C2PA 规范持续演进（现行 2.3），指导委员会含 TikTok/OpenAI/Google/Meta/BBC/Sony——视频内容凭证大概率成为国际分发的事实要求**（置信：官方源（c2pa.org）；对'视频厂商未来默认嵌入 C2PA'的预测置信度：中；https://c2pa.org/）

### 要点 / 模式清单

- 中国合规制度清晰且已生效：显式（视频起始画面+播放周边）与隐式（元数据）双层义务、平台三情形核验、第9条无标识交付的合法通道均有官方条文可依
- 厂商水印参数已具备：可灵/Seedance/Vidu 均提供可编程水印开关，Vidu 还支持自定义水印图与独立 watermarked_url 返回，平台侧开启成本低
- MCP Tasks 扩展与视频生成任务模型天然匹配：taskId 持久化、轮询、input_required 中途输入、取消语义完整，官方明确适配长任务与外部作业系统
- C2PA 生态覆盖主要分发端：YouTube 官方确认会读取 C2PA 元数据自动打标，TikTok/OpenAI/Google/Meta 均在指导委员会，国际分发链路有现成溯源通道
- Agent Skills 已成事实标准：Gemini CLI、GitHub Copilot、VS Code、OpenAI Codex、Cursor 等数十个客户端列于官方展示墙，且规格自带 compatibility 字段与 skills-ref 校验器可用作兼容防线

### 空位与建议

- **四家国产视频生成 API 默认交付无水印成片（可灵 watermark_info.enabled 默认 false、Seedance watermark 默认 false、Vidu 默认不加、MiniMax 无此参数），显式标识责任系统性转移给 API 调用方**
  - 证据：官方源：可灵文档原文 "watermark_info.enabled: boolean // true includes watermark; false excludes watermark. Default: false"（kling.ai/document-api/api/video/3-0-omni/text-to-video.md）；火山方舟创建视频生成任务 API "watermark boolean 默认值 false | 视频水印"（docs.volcengine.com/docs/ark/create-video-generation-task-api）；Vidu 文生视频 "watermark Bool 可选…默认不加"（platform.vidu.cn/docs/text-to-video）；MiniMax 英文 API 文档（video-generation-t2v 等 3 页，页面内容完整）中 watermark/水印 出现 0 次
  - 建议：生成平台必须把合规动作收进自身契约：新增 label_required（CN 出境默认 true，办法第4条）、label_mode（vendor_watermark / caller_overlay / platform_label）、vendor_watermark_param 能力矩阵（kling: options.watermark_info.enabled；seedance: watermark；vidu: watermark+wm_url+wm_position；minimax: 无→必须后处理烧录）三个字段，按厂商路由水印策略
- **无一家视频厂商在 API 文档中说明输出文件是否写入 AIGC 隐式元数据（办法第5条与 GB 45438-2025 要求元数据含生成合成属性、服务提供者名称/编码、内容编号）——强标符合性存在可验证的盲区**
  - 证据：官方源负面证据：可灵/火山/Vidu/MiniMax 四份 API 文档抓取全文中均无 隐式元数据/AIGC metadata/C2PA 字样；办法第5条原文（cac.gov.cn 全文）与 GB 45438-2025（openstd 官方库：强制性国标、现行、2025-09-01 实施）
  - 建议：契约新增 implicit_metadata: {enabled, provider_name_or_code, content_id, standard: 'GB 45438-2025'}，并建设元数据写入/校验层（下载厂商成片→检测隐式标识→缺失则代写入），同时用 Vidu 的 meta_data 透传字段（'元数据标识，json格式字符串'）作为厂商侧注入通道
- **用户'无显式标识交付'（办法第9条）没有标准化落地路径：需同时满足协议约定义务+日志留存≥6个月，现有调用链无对应字段与留痕**
  - 证据：官方源：办法第9条原文——'服务提供者应当在用户协议中明确约定…并依法保存有关记录满六个月'（cac.gov.cn 全文）
  - 建议：契约新增 label_waiver: {requested_by_user, agreement_version, log_retention_months>=6} 三元组，无该三元组的请求强制走 label_required=true 路径；日志写入与任务记录同库
- **抖音/B站/快手的平台侧 AI 内容核验规则无可直接机读的官方规则页（安全与信任中心/社区规则页为 SPA 或未公开 URL），平台适配只能靠逆向或人工盯守**
  - 证据：官方源（义务锚点）：办法第6条规定传播平台三种核验情形（元数据检出/用户申明/疑似 traces）并须在元数据中添加传播要素信息（cac.gov.cn）；实测：trust.douyin.com 首页链接中无 AI 标识规则入口，95.douyin.com 连接失败，Bing 定位 bilibili/kuaishou 规则页失败（返回通用首页）
  - 建议：契约新增 platform_disclosure 适配层字段（platform: 'douyin'|'bili'|'kuaishou'|'youtube'|'tiktok', verify_mode: 'metadata'|'declaration'|'traces', propagation_ref）并在内部维护平台规则镜像表；把三个平台规则原文 URL 列为待补的一手证据缺口
- **TikTok 的 AI 标注与 C2PA 具体政策页当前不可直接核实（newsroom 旧文 URL 重定向到无关文章，help center 正文 JS 反爬不可机读），仅有 c2pa.org 指导委员会成员身份这一官方锚点**
  - 证据：官方源：c2pa.org Steering Committee 列出 TikTok/OpenAI/Google/Meta/Adobe/BBC/Sony 等（c2pa.org）；实测：newsroom.tiktok.com/en-us/partnering-with-industry-to-combat-misleading-ai-content 与 labeling-ai-generated-content-c2pa 均重定向至无关内容，support.tiktok.com 正文未渲染
  - 建议：对 TikTok 政策引用降级为'多源交叉/待补一手来源'并列入开放问题；分发契约中 tiktok.ai_label 字段先按最严假设（必须自标注）设计，待拿到官方页后回填
- **SKILL.md 规范治理薄弱：Anthropic 首创但未捐入中立基金会，无规范版本号、无变更日志、无兼容承诺，allowed-tools 字段为 Experimental 且'支持程度因 agent 实现而异'——第三方 skill 存在被规范演进破坏的风险**
  - 证据：官方源：agentskills.io 原文 'The Agent Skills format was originally developed by Anthropic, released as an open standard…open to contributions from the broader ecosystem'；agentskills/agentskills README 无版本化/治理机构章节（145 commits、无 release/tag 内容）；agentskills.io/specification 原文 'allowed-tools…Experimental. Support for this field may vary between agent implementations'
  - 建议：内部 skill 仓库契约：固定 spec 快照（记录抓取日）、只依赖 name/description 两个必填字段、用 compatibility 字段声明目标宿主（'Designed for Claude Code (or similar products)' 官方示例句式）、CI 跑 skills-ref validate；不把 allowed-tools 当作跨宿主保证
- **MCP 2026-07-28 无状态化重构对长任务（视频生成分钟级）server 是破坏性迁移：初始化握手时代（2025-11-25 及更早）进入向后兼容模式，Roots/Sampling/Logging/动态客户端注册已弃用（最早 2027-07-28 可移除），HTTP+SSE 可在 SEP-2596 转 Final 三个月后移除**
  - 证据：官方源：modelcontextprotocol.io/specification/versioning 'The current protocol version is 2026-07-28'；spec 概览 'Stateless, self-contained requests…Per-request capability negotiation'；deprecated 页列出弃用表与最早移除日
  - 建议：视频生成 MCP server 直接按 2026-07-28 设计：无粘性会话、每请求带 _meta 协议版本、实现 server/discover、任务状态外置持久化；用 Tasks 扩展（CreateTaskResult/taskId/ttlMs/pollIntervalMs/input_required）替代长连接阻塞——官方明确列其适用场景为 'Long-running operations…External job systems…Unreliable connections'
- **MCP Tasks 仍是 opt-in 扩展而非核心协议，客户端支持矩阵未在本次核实范围内，第三方宿主可能不支持任务化结果**
  - 证据：官方源：tasks/overview 'MCP Tasks is an extension to the core MCP specification. Host support varies by client. Task support requires explicit opt-in from both client and server'；规范正文另见 'Skills over MCP' 工作组与 MCP Apps 扩展并列
  - 建议：服务端双形态输出：客户端未声明 io.modelcontextprotocol/tasks 时回退同步/轮询 API 形态；契约中增加 transport_profile 字段（mcp_2026_07_28 / mcp_2025_11_25 / http_json）+ capabilities 协商结果记录

### 未解问题

- 四家厂商 API 输出成片是否已实际写入 GB 45438-2025 隐式元数据字段？（文档均未说明，需下载成片做元数据解析实测——这是契约 implicit_metadata 字段能否省略的前提）
- TikTok AI 标注与 C2PA 政策的官方原文页（2024-05 newsroom 公告与 help center 正文）——本次因改版与反爬未能取得，需人工补证后再回填 tiktok.ai_label 契约字段
- 抖音安全与信任中心（trust.douyin.com）内 AI 内容标识规则的具体页面、B站社区规则中 AI 生成内容声明条款、快手社区管理规范 AI 条款的一手 URL
- MiniMax 中文开放平台（platform.minimaxi.com，需登录）视频生成文档是否存在英文站没有的水印参数
- agentskills/agentskills 仓库 CONTRIBUTING.md 中是否有治理/RFC 流程与规范版本化机制（README 未涉及，本次未抓取该文件）
- MCP Tasks 扩展在各主流宿主的客户端支持矩阵（modelcontextprotocol.io/extensions/client-matrix）——决定视频 MCP server 是否默认启用任务化输出

### 来源

- [关于印发《人工智能生成合成内容标识办法》的通知（国信办通字〔2025〕2号，全文）](https://www.cac.gov.cn/2025-03/14/c_1743654684782215.htm)
- [GB 45438-2025《网络安全技术 人工智能生成合成内容标识方法》官方标准目录记录（强制性国标，现行，2025-09-01 实施）](https://openstd.samr.gov.cn/bzgk/gb/std_list?p.p1=0&p.p90=circulation_date&p.p91=desc&p.p2=45438)
- [Kling AI API 文档：Kling 3.0 & 3.0 Omni - Text to Video（options.watermark_info 默认 false）](https://kling.ai/document-api/api/video/3-0-omni/text-to-video.md)
- [火山方舟：创建视频生成任务 API（watermark boolean 默认值 false）](https://docs.volcengine.com/docs/ark/create-video-generation-task-api?lang=zh)
- [Vidu API 文档：文生视频（watermark/wm_position/wm_url/watermarked_url，默认不加，默认水印文案'内容由AI生成'）](https://platform.vidu.cn/docs/text-to-video)
- [MiniMax API Docs：Create Text-to-Video Generation Task（全文档无 watermark 参数——官方负面证据）](https://platform.minimax.io/docs/api-reference/video-generation-t2v)
- [YouTube Help：Disclosing use of GenAI content（披露要求、自动打标含 C2PA 元数据、违规后果）](https://support.google.com/youtube/answer/14328491)
- [C2PA 官网（规范 2.3；指导委员会：Adobe/Amazon/BBC/Google/Meta/Microsoft/OpenAI/Sony/TikTok/Truepic 等）](https://c2pa.org/)
- [MCP Versioning（当前协议版本 2026-07-28；按请求版本协商与 server/discover）](https://modelcontextprotocol.io/specification/versioning)
- [MCP 2026-07-28 Specification（Stateless, self-contained requests；Tasks/Skills over MCP/MCP Apps 扩展）](https://modelcontextprotocol.io/specification/2026-07-28/)
- [MCP Deprecated Features 注册表（Roots/Sampling/Logging/DCR 弃用，最早 2027-07-28 移除；HTTP+SSE 移除窗口）](https://modelcontextprotocol.io/specification/2026-07-28/deprecated)
- [MCP Tasks 扩展总览（CreateTaskResult/taskId 持久化/轮询/input_required/取消；ext-tasks 仓库）](https://modelcontextprotocol.io/extensions/tasks/overview)
- [Agent Skills 官网（'originally developed by Anthropic, released as an open standard'；采纳方展示墙）](https://agentskills.io)
- [Agent Skills Specification（SKILL.md 字段表；allowed-tools 标注 Experimental）](https://agentskills.io/specification)
- [agentskills/agentskills GitHub 仓库（Apache-2.0 / CC-BY-4.0；README 无治理机构与版本化承诺）](https://github.com/agentskills/agentskills)
- [抖音安全与信任中心（平台侧规则的官方入口，AI 标识规则页待补证）](https://trust.douyin.com)

---

## 本地源码考古 + PixVerse 参照（契约设计模式提取）

对 7 个本地克隆仓库（anthropics/higgsfield/runwayml/runway-mcp/atlascloud/fal/elevenlabs 共 103 个 SKILL.md）做了契约设计模式考古，并以 PixVerse 官方仓库（skills + cli）为远程对照。核心发现：(1) frontmatter 三代演进——官方最小 name+description → 厂商扩展（version/user-invocable/allowed-tools/argument-hint/metadata），description 写法上 higgsfield 的「Use when 触发词 + NOT for 反向路由 + Chain with 链式声明」是技能间路由的最优解，无需任何额外机制；(2) 异步表达三派——CLI 阻塞（higgsfield --wait，默认 10m 超时/3s 间隔，rejoin 用 generate wait <id>）、SDK wait-helper（runway waitForTaskOutput，'Submit once; do not add a manual polling loop'）、显式轮询（fal --async→request_id→status；atlas 固定 2s），共同不变量是轮询静默、永不重复提交、状态查询只读；(3) 计费披露两极——runway 全透明（SKILL.md 内置每模型 credit 表、输出行带成本、get_credit_balance 前置）vs higgsfield「不预算成本、除非用户问」（cost 子命令按需），atlas 独特：把成本语义编入状态机（重试=显式决策，先报旧 ID 与新增成本）；(4) 错误处理四形态——错误→动作映射表（runway）、按报错字符串的 playbook 含 CLI 版本 bug workaround（higgsfield troubleshooting.md）、终态/非终态分类学（atlas：timeout/慢输出/轮询中断≠失败）、退出码语义学（PixVerse exit 0-7，'exit 0≠生成完成'、'exit 2 timeout≠提交失败'）；(5) 组合模式四派——基座+表面技能（runway-dev + '+' 语法）、基础技能+路由数据技能（fal genmedia + model-routing）、能力与方法论分离（atlas spec/execution 二分）、单入口三路由表（PixVerse 唯一 SKILL.md + capabilities/ + workflows/ + 'Read only what the task needs'）；(6) PixVerse 作为最接近路线的参照，其独有价值是把契约拆成三份独立文件：execution-contract.md（stdout/stderr 流分离、ID 分型与可移植性、部分批处理形态学、幂等键、并发退避 5/10/20s、cost_credits 缺失≠免费）、prompt-contract.md（生成式请求不改写、'Optimize and generate' 一次授权、禁止 mandatory quality/logo/subtitle pads、'Missing decorative detail is not a reason to ask questions'）、persistent-assets.md（角色/道具注册表），加上 capabilities.json 离线机器可读能力发现与不耗 credit 的离线回归测试套件。对照 Atlas CLI 现状（近期 commit 已有 agent input/recovery/artifact contracts 与 generate JSON contract），主要空位在：退出码语义表、幂等键、prompt 改写授权契约、部分失败输出形状、prose 回归测试。

### 关键信号

- **技能元数据标准化进行中：anthropics 官方 spec 已从仓库内迁至 agentskills.io/specification（本地 spec/agent-skills-spec.md 仅剩链接），elevenlabs 已使用 openclaw 命名空间的 metadata.env 声明凭证依赖——frontmatter 正从'自由字段'走向'跨厂商标准+厂商扩展'两层**（置信：官方源（anthropics-skills 仓库内文件 + elevenlabs-plugin 仓库内文件交叉）；https://agentskills.io/specification）
- **厂商 CLI 把'能力发现'做成离线机读契约：PixVerse capabilities.json（normalized compact encoding）+ pixverse capabilities --json 按需查询，并在 SKILL.md 中禁止窄任务加载全量目录——模型目录的时效责任从 SKILL.md prose 转移到 CLI 数据文件**（置信：官方源（cli README + skills SKILL.md 原文）；https://github.com/PixVerseAI/cli）
- **契约文件从 SKILL.md 中析出成为趋势：PixVerse execution-contract/prompt-contract/persistent-assets 三份横切契约、atlas execution.md 独立成册且被两个技能共享——'计费状态机''改写授权'这类跨技能不变量正在离开单技能正文，成为仓库级契约文件**（置信：官方源（两个仓库原文结构对照）；https://raw.githubusercontent.com/PixVerseAI/skills/main/skills/references/execution-contract.md）
- **技能评测成为工程标配：higgsfield evals/（10 场景+rubric+轮次制）与 PixVerse tests/（离线 unittest，不耗 credit）表明头部厂商已把 SKILL.md 当代码维护，配 CI（higgsfield .github/workflows/validate-skills.yml 校验 frontmatter/版本同步/引用/孤儿文件）**（置信：官方源（两仓库 README/CI 配置）；https://github.com/PixVerseAI/skills）

### 要点 / 模式清单

- 【frontmatter】官方基线（anthropics skill-creator）：仅 name+description 必填，description 是唯一触发机制且要求写得'pushy'防欠触发；三级渐进披露（metadata ~100 词 → SKILL.md <500 行 → references 不限）。证据：anthropics-skills/skills/skill-creator/SKILL.md L67、L88-93
- 【frontmatter】厂商扩展字段谱系：higgsfield=version+argument-hint+allowed-tools:Bash；runwayml=user-invocable+allowed-tools 白名单（如 Bash(uv run *)）；elevenlabs=license+compatibility+metadata.openclaw.env（声明 ELEVENLABS_API_KEY 依赖）；fal=metadata.author+version；atlas/runway-mcp=最小两字段。扩展字段集中在'权限收窄、参数提示、env 依赖'三类
- 【frontmatter/description 写法】higgsfield 三段式：正向触发词（Use when: "make a video"...）+ 能力清单（Modes: ...）+ 反向路由（NOT for: ... use higgsfield-brandkit instead）+ Chain with 声明（soul-id 产出 reference_id → generate 消费）。description 长达 ~250 词但把跨技能路由决策前置到触发层。证据：higgsfield-skills/higgsfield-generate/SKILL.md L4-24
- 【异步/CLI 阻塞派】higgsfield：'Submit and wait in one shot'——generate create <jst> --wait 阻塞至终态并 stdout 打印结果，--wait-timeout 默认 10m、--wait-interval 默认 3s；中断重入用 generate wait <job_id> --json，'never duplicate a running job'；UX 规则明确'Polling is silent... don't narrate polling job'。证据：higgsfield-generate/SKILL.md L45-49、L124、higgsfield-video-explainer/SKILL.md L276
- 【异步/SDK 派】runway-dev：链式等待 helper 'await client.<op>.create({...}).waitForTaskOutput()'，'Submit once; do not add a manual polling loop or auto-resubmit'，捕获 TaskFailedError 上抛任务详情；MCP get_task 仅用于流程外调试。证据：runwayml-skills/skills/runway-dev/SKILL.md L58-60
- 【异步/显式轮询派】fal：run --async 返回 request_id，genmedia status 逐个串行轮询（'one failure must not cancel others'），每个轮询是独立 Bash 调用；400 'Request is still in progress' = 继续以同 ID 轮询，'Do not re-fire the original genmedia run --async'。证据：fal-community-skills/skills/fal-gamedev/SKILL.md L32-73
- 【异步/状态机派（最完备）】atlas universal-video-prompt 与 seedance 两技能共享同一'Billable task state machine'6 条：提交即记录 prediction ID+stage；starting/queued/pending/processing 为活跃态轮询同 ID 永不重复提交；completed 须下载校验（截断视频报 moov atom not found→重下载而非重新生成）；failed/timeout/canceled 为终态、重试是显式决策且先报旧 ID+新增成本；零处理时长/慢输出/本地轮询超时/会话中断/状态查询错误≠失败，保留 ID 恢复轮询；continue=恢复永不=重试授权。金句：'A status lookup is read-only... that substitution is how a polling loop turns into a billing incident'。证据：atlascloud-skills/skills/universal-video-prompt-skill/references/execution.md L45-84
- 【计费】runway 全透明模式：SKILL.md 内置每模型 credit 表（gen4.5 12 credits/sec、veo3 40 credits/sec、gen4_image_turbo 2 credits），交付行强制带成本 'Generated with gen4_image (1080p, 8 credits)'，billable 验证前强制 get_credit_balance，credits×$0.01 换算美元，rw-check-org-details 独立技能查余额/限额/用量历史。证据：rw-generate-video/SKILL.md L32-40、use-runway-api/SKILL.md L172-173、rw-check-org-details/SKILL.md L86-99
- 【计费】higgsfield 反向模式：UX 规则 5 'Don't pre-estimate cost or optimize for cheaper models unless the user asks. Prefer the quality default first'，成本仅按需经 generate cost <jst> 子命令查询；用户被引导相信'后端负责质量默认'。证据：higgsfield-generate/SKILL.md L48、references/troubleshooting.md Cost 节
- 【计费/PixVerse】'cost_credits is optional and may be absent, so absence does not mean free generation' + exit 4 insufficient credits='stop until resolved'；runway-mcp 则取中道：'For anything beyond a single quick generation, state the rough cost and confirm'。证据：PixVerse execution-contract.md §1、runway-mcp-plugin/skills/runway-media/SKILL.md Before you start #3
- 【错误处理】四种形态：a) 错误→动作映射表（runway-dev Errors 节：Validation→修字段重试一次/Auth→停/Rate limit→遵守 retry interval/FAILED→禁止自动重提）；b) 按报错字符串 playbook（higgsfield troubleshooting.md：Session expired/Invalid values/DataDome captcha 等逐条给动作，含 CLI 1.1.20 nano_banana_pro job 引用误标 bug 的 workaround）；c) HTTP 动词级重试策略（atlas-cloud：GET 自动指数退避重试 3 次 1s→2s→4s，POST 一律不重试防重复扣费）；d) 退出码语义学（PixVerse exit 0-7，每码带 agent 动作）。证据：runway-dev/SKILL.md L72-78、higgsfield troubleshooting.md、atlas-cloud/SKILL.md L489-501、PixVerse execution-contract.md §4
- 【工作流组合】四派：a) 基座+表面（runway-dev 基座教 MCP 策略/凭证/错误共享语义，5 个 runway-dev-* 表面技能用 '+' 语法组合加载，'Surface skills repeat their minimum setup so they remain useful when installed alone'）；b) 基础技能+数据技能（fal genmedia 是唯一执行通道 'Every other skill executes its work through genmedia commands'，model-routing 是纯数据技能存默认 endpoint ID + 5 步验证阶梯）；c) 能力/方法论分离（atlas：atlas-cloud 教怎么调 API，universal-video-prompt 教怎么写 prompt spec——spec 与 execution 刻意解耦 'the spec must not depend on who executes it'）；d) 单入口路由表（PixVerse 唯一 SKILL.md，17 任务→capabilities/*.md、创意任务→策略文件、流水线→workflows/*.md 三张表 + 'Read only what the task needs' 加载纪律）。证据：runway-dev/SKILL.md L80-90、genmedia/SKILL.md L8-10、universal-video-prompt-skill/references/execution.md L1-4、PixVerse skills/SKILL.md
- 【reference 组织】全部遵循 anthropics 三级结构；特色做法：atlas 的 .zh-CN.md 语言路由（中文请求先读中文工作流，模型 ID/JSON 键/命令保持英文不翻译）；higgsfield references/model-catalog.md 等按域拆分且 troubleshooting.md 独立成册；fal-workflow references/ 含 PATTERNS/WORKFLOWS/MODELS/node-rules 声明式与命令式双模式文档；PixVerse references/ 放三份横切契约（execution/prompt/persistent-assets）供所有 capability/workflow 文件引用
- 【时效契约】runway-dev：'Installed skill prose is workflow guidance, not the canonical API schema'，合同解析四级阶梯 llms.txt→相关子集→api.md→openapi.json，'Do not invent endpoints, field names, or model constraints'；runway-mcp 把模型/时长/credit 时效推给 MCP tool descriptions（'Read them before choosing parameters'）；PixVerse 把能力目录做成 capabilities.json 离线机读 + pixverse capabilities --json 按需查询而非全量加载。证据：runway-dev/SKILL.md L27-34、runway-media/SKILL.md L9、PixVerse cli README
- 【哲学差异】anthropics=最小官方规范+渐进披露+防欠触发；higgsfield=UX 优先的 CLI 包装（轮询静默/语言自适应/不预算成本/批量禁问）+ 把 markdown 当代码做回归（evals/ 10 场景+评分 rubric，'Plain markdown drifts. Without a fixed set of scenarios... every refactor is a hope'）；runway=双产品线分离（SDK 集成 vs agent 直发）+ llms.txt 时效阶梯；fal=agent-first CLI（--json 纪律/smart routing/never invent endpoint IDs/schema 先行）；atlas=执行隔离主义（计费状态机/凭证作用域/恢复状态文件）；elevenlabs=SDK 文档型技能+凭证技能独立（setup-api-key 先验证已有 key 再走安装流程，'Do not print, quote, or repeat the key'）+ architect 微技能家族；runway-mcp=最小包装（工具路由表+Inputs/Results/Don't 三节）
- 【PixVerse 契约亮点】execution-contract.md：stdout/stderr 流分离且 'Partial batches may return usable stdout with a nonzero exit'；ID 分型（image_id/video_id/audio_id/project_id 各归其位）+ 'An ID from another account or workspace is not an interchangeable input'；部分批处理形态学（items 存成功、failed_ids/fail_count 报失败、单成功可坍缩为单对象形状、'never classify a partial batch from an exit code alone'）；'Do not run create a second time to parse an ID'；幂等键 'Use a stable --idempotency-key from the first submission... An intentional replacement of a confirmed failed generation needs a new key and may cost credits'；并发限制退避 'retry at most three times with increasing delay (for example 5/10/20 seconds)'；'Do not switch models or workspaces just to evade a failed request'；下载失败≠生成失败。prompt-contract.md：生成式请求不改写（可提一次改进建议但 'Do not turn silence into acceptance of a rewrite'）；'Optimize and generate' 一次授权覆盖整链不重复询问；禁加 'mandatory quality, logo, subtitle, twin, or motion pads'；'Missing decorative detail is not a reason to ask questions'；提问仅限阻塞性歧义；对话文本除非要求否则逐字保留。证据：raw.githubusercontent.com/PixVerseAI/skills 两份契约原文
- 【评测即工程】higgsfield evals/（dev-only 不随包分发，10 场景+rubric，3 轮稳定后才固化进 CLAUDE.md 'Key Decisions (Do Not Revisit Without Data)'）与 PixVerse tests/（python unittest 离线回归套件，'no credits consumed'）殊途同归：SKILL.md 是纯 markdown 会漂移，必须场景化回归守护。证据：higgsfield-skills/evals/README.md、PixVerse skills README Testing 节

### 空位与建议

- **我们的 CLI 缺少显式退出码语义表：agent 无法从退出码区分'查询成功但生成未完成'与'提交失败'，容易把 timeout 当成提交失败而重复提交**
  - 证据：PixVerse exit 0-7 每码配 agent 动作（2=timeout 'Resume the existing task; do not assume submission failed'；4=insufficient credits 'stop until resolved'；7=concurrency 'query account slots --json, then bounded backoff'），且明令 'never classify a partial batch from an exit code alone'；对照本仓（AtlasCloudTeam/cli）近期 commit 'harden agent input, recovery, and artifact contracts' 说明恢复契约在建设中但退出码语义未见文档化
  - 建议：建议 1：为 CLI 定义 0-7 式稳定退出码表并写进 SKILL.md/契约文件，每码必须附 agent 应做动作一句；至少覆盖：成功≠生成完成、轮询超时≠提交失败、余额不足即停、并发限制退避重试。这是 agent 契约的第一公民，优先于一切 flag 设计
- **缺少幂等键机制：网络歧义（请求发出但响应丢失）后 agent 无法安全重试，只能赌'任务其实没创建'**
  - 证据：PixVerse：'Use a stable --idempotency-key from the first submission'，同一逻辑重试复用 key，有意重跑换新 key 'and may cost credits'；voice/music 的 --client-request-id 明确'仅 tracing 非去重'，歧义网络错误后禁止自动重提；atlas 状态机则要求重试前'报告旧 ID 与新增成本'
  - 建议：建议 2：CLI 增加稳定 --idempotency-key：首次提交生成/由 agent 提供逻辑 key，服务端去重；契约中写明三档——同逻辑重试复用 key、有意重跑须换 key 且 CLI 打印成本提示、歧义错误后先查 status 再决定
- **缺少 prompt 改写授权契约：skill 何时可以改用户 prompt、何时禁止、优化后是否需要再次确认，无成文规则**
  - 证据：PixVerse prompt-contract.md 是唯一把'改写权'契约化的厂商：'A generation-only request uses the supplied prompt unchanged'、可免费提一次改进建议但 'Do not turn silence into acceptance of a rewrite'、'Optimize and generate authorizes using the result in the requested generation; do not ask for the same approval again'、禁止 'mandatory quality, logo, subtitle, twin, or motion pads'、'Ask only for an ambiguity that prevents the requested result'
  - 建议：建议 3：为我们的 SKILL.md 新增 references/prompt-contract.md，四节：生成式请求不改写（可一次性建议）；显式 optimize 授权重写且一次授权覆盖整链；可改/禁改清单（保留主体/动作/场景/台词/约束，禁止 mandatory pads）；提问门槛（仅阻塞性歧义，'Missing decorative detail is not a reason to ask questions'）
- **批量/多阶段生成的部分失败输出形状未定义：部分成功时 stdout/JSON 长什么样、成功项与失败项如何共存，agent 可能丢弃已成功的结果**
  - 证据：PixVerse 用整节定义形态学：单对象 vs items 数组、failed_ids/fail_count 可与可用 ID 共存（'Submission failures may also produce fail_count, including with usable IDs'）、单成功可坍缩、'Preserve successful outputs on partial failure'、jq 提取表达式内置
  - 建议：建议 4：在 generate JSON contract 中固化部分失败形状：top-level status + items[]（每项含 id/status/url）+ failed_ids + fail_count；契约明文：部分失败禁止丢弃成功产物、退出码单独不足以判定批次结果、单成功坍缩规则
- **重试语义缺'终态/非终态'分类学：轮询超时、慢输出、状态查询报错容易被误判为失败而重新提交，造成重复扣费**
  - 证据：atlas 状态机（我们自己仓库的 skills）：'A zero or missing processing-time field, a delayed output, a local polling timeout, a stopped turn, or a transient status-query error is not proof of failure. Preserve the ID and resume polling.'；fal：400 still-in-progress 须以同 ID 重试 status 而非重发任务；PixVerse：'A missing or temporarily inaccessible download does not establish that generation failed'
  - 建议：建议 5：把 atlas 状态机提升为 CLI+SKILL 共享契约文件（references/execution.md 或 execution-contract.md），CLI --wait 行为与 SKILL 轮询指引共用同一套状态词汇表（active/terminal-success/terminal-failure/not-failure），并写明'状态查询只读，永不以生成调用替代'——这是跨 CLI 与 SKILL 的单一事实源
- **ID 的作用域与可移植性规则未成文：跨账号/工作区的 ID 能否作输入、上传资产 ID 与生成任务 ID 的区别，靠 agent 猜**
  - 证据：PixVerse：ID 分型（image_id/video_id/audio_id/project_id/task id 各自语义）+ 'An ID from another account or workspace is not an interchangeable input' + 'asset upload returns an id that is not a pending generation'；runway-mcp：'Output of an earlier Runway call: pass its taskId where the tool accepts one instead of copying a signed URL'
  - 建议：建议 6：CLI 契约中增加 ID 语义节：每类 ID 的字段名与生命周期、跨账号/工作区不可互换、上传 ID≠任务 ID、签名 URL 过期时限（runway 标注 ~24-48h 并要求持久化产物）
- **多阶段任务的断点恢复缺持久化协议：会话中断后 agent 无从得知已提交任务的 ID 与阶段**
  - 证据：atlas execution.md：'Keep a small state file per job: stage name → prediction ID → status → output path. That file is what makes an interrupted multi-stage job cheap to finish instead of expensive to redo' + seedance 的 execution.resumePredictionIds.<stage>（grid/ref1/seg1/shot1/clip1 阶段键）；higgsfield explainer：'Timeout: rejoin with higgsfield generate wait <job_id> --json; never duplicate a running job'
  - 建议：建议 7：CLI 原生支持任务状态文件（如 .atlas/jobs.json：stage→prediction_id→status→output_path），generate create 自动写入、wait --json 自动更新；SKILL.md 指示 agent 会话恢复时先读状态文件 rejoin 而非重提；顺序依赖阶段强制串行、独立镜头可并发
- **SKILL.md 的时效声明缺失：内嵌模型目录/参数表会随服务端漂移，agent 可能信任过期 prose 拒绝实际可用的模型**
  - 证据：runway-dev：'Installed skill prose is workflow guidance, not the canonical API schema' + llms.txt→api.md→openapi.json 解析阶梯；fal：'Never invent endpoint IDs' + schema 先行验证；higgsfield：'If the user says a model exists but search returns no results, trust that signal and verify with the full model list before answering'；PixVerse：capabilities.json 离线机读 + 'report required upgrades rather than inventing unsupported flag/model combinations'
  - 建议：建议 8：每个 SKILL.md 加一节'Current contracts'：声明 prose 仅为工作流指引、模型/参数以 CLI 查询为准（model list/get --json 或 capabilities --json 按需查询），给出文档解析阶梯；内嵌模型表标注'可能过期，提交前用 X 命令验证'
- **SKILL.md 无回归测试：markdown 重构（改默认模型、路由逻辑、提示词）没有守护，每次编辑都是赌博**
  - 证据：higgsfield evals/README.md：'Skill behavior is defined in plain markdown. Plain markdown drifts. Without a fixed set of scenarios + scoring rubric, every refactor is a hope.' 10 场景+rubric，3 轮稳定后固化为 'Key Decisions (Do Not Revisit Without Data)'；PixVerse tests/ 为离线 unittest 套件 'no credits consumed'
  - 建议：建议 9：建 evals/ 目录（dev-only 不随包分发）：10 个用户请求+期望行为+评分 rubric，覆盖模式选择、默认模型路由、错误恢复、计费提示四类决策；每次 SKILL.md PR 跑一轮；PixVerse 式离线 CLI 回归（不耗 credit 的 mock/录像回放）可作为第二层
- **技能间路由依赖正文叙述而非 description 层：我们的技能触发后如何引导去兄弟技能、如何声明链式关系，缺少统一句式**
  - 证据：higgsfield 八技能 description 统一三段式：Use when 触发词 + Chain with（soul-id 产 reference_id → generate 以 --soul-id 消费）+ NOT for 反向路由（'NOT for: Soul training... use higgsfield-soul-id'）；runway 用 '+' 前缀语法组合表面技能且要求'表面技能自带最小安装指引，单独安装也可用'
  - 建议：建议 10：统一我们的 description 写法为四件套：能力一句话 + Use when 触发词枚举（含用户可能说的口语）+ Chain with（上游产出什么 ID/字段、下游哪个技能消费）+ NOT for 反向路由到兄弟技能；多表面技能各自内嵌最小 setup 使其单独可用；frontmatter 补 allowed-tools 收窄与 argument-hint

### 未解问题

- agentskills.io/specification 的最新官方 frontmatter 字段清单未抓取——若我们要对齐标准，需确认官方是否已收纳 allowed-tools/argument-hint/metadata 等厂商扩展字段
- PixVerse persistent-assets.md（角色/道具注册表协议）未读取——它是第三份契约，其'注册表+导入+缓存'协议可能对我们的人物一致性（reference_id 类）功能有直接参考价值
- higgsfield-ai/cli 仓库本身未核查（install.sh URL 来自 SKILL.md 正文）；其 --wait 幂等性（超时后 rejoin 是否可能重复创建任务）未知
- fal skills/index.json 与 build-skills-index.py 的技能发现/分发机制未深读——若我们在做 marketplace 式分发可补查
- Atlas CLI 当前 --wait 实现在歧义网络错误后的行为（是否已有幂等保护）需在本仓源码中确认，方能评估建议 2 的实现成本

### 来源

- [[本地] higgsfield-generate SKILL.md（CLI 阻塞式异步、UX 规则、NOT-for 路由）](file:///Users/lifcc/Desktop/code/AI/tools/video-ai-landscape/higgsfield-skills/higgsfield-generate/SKILL.md)
- [[本地] higgsfield troubleshooting.md（按报错字符串 playbook、cost 子命令）](file:///Users/lifcc/Desktop/code/AI/tools/video-ai-landscape/higgsfield-skills/higgsfield-generate/references/troubleshooting.md)
- [[本地] higgsfield evals/README.md（prose 回归测试哲学）](file:///Users/lifcc/Desktop/code/AI/tools/video-ai-landscape/higgsfield-skills/evals/README.md)
- [[本地] atlascloud universal-video-prompt-skill references/execution.md（计费任务状态机、凭证作用域、恢复协议）](file:///Users/lifcc/Desktop/code/AI/tools/video-ai-landscape/atlascloud-skills/skills/universal-video-prompt-skill/references/execution.md)
- [[本地] atlascloud seedance-2-5-skill SKILL.md（execution resumePredictionIds、2s 轮询间隔）](file:///Users/lifcc/Desktop/code/AI/tools/video-ai-landscape/atlascloud-skills/skills/seedance-2-5-skill/SKILL.md)
- [[本地] atlascloud atlas-cloud SKILL.md（GET 指数退避/POST 禁重试防重复扣费）](file:///Users/lifcc/Desktop/code/AI/tools/video-ai-landscape/atlascloud-skills/atlas-cloud/SKILL.md)
- [[本地] runwayml runway-dev SKILL.md（基座+表面技能、llms.txt 时效阶梯、SDK wait helper、错误映射表）](file:///Users/lifcc/Desktop/code/AI/tools/video-ai-landscape/runwayml-skills/skills/runway-dev/SKILL.md)
- [[本地] runwayml rw-generate-video SKILL.md（每模型 credit 表）](file:///Users/lifcc/Desktop/code/AI/tools/video-ai-landscape/runwayml-skills/skills/rw-generate-video/SKILL.md)
- [[本地] runwayml rw-check-org-details SKILL.md（credit 余额/限额/美元换算）](file:///Users/lifcc/Desktop/code/AI/tools/video-ai-landscape/runwayml-skills/skills/rw-check-org-details/SKILL.md)
- [[本地] fal genmedia SKILL.md（agent-first CLI、--json 纪律、async+poll 模式）](file:///Users/lifcc/Desktop/code/AI/tools/video-ai-landscape/fal-community-skills/skills/genmedia/SKILL.md)
- [[本地] fal fal-gamedev SKILL.md（并行 async 发射+串行轮询、400 still-in-progress 语义）](file:///Users/lifcc/Desktop/code/AI/tools/video-ai-landscape/fal-community-skills/skills/fal-gamedev/SKILL.md)
- [[本地] fal model-routing SKILL.md（数据技能+endpoint 验证阶梯）](file:///Users/lifcc/Desktop/code/AI/tools/video-ai-landscape/fal-community-skills/skills/model-routing/SKILL.md)
- [[本地] anthropics skill-creator SKILL.md（官方规范：渐进披露、pushy description、scripts/references/assets 结构）](file:///Users/lifcc/Desktop/code/AI/tools/video-ai-landscape/anthropics-skills/skills/skill-creator/SKILL.md)
- [[本地] anthropics spec 指针（官方规范迁至 agentskills.io）](file:///Users/lifcc/Desktop/code/AI/tools/video-ai-landscape/anthropics-skills/spec/agent-skills-spec.md)
- [[本地] elevenlabs setup-api-key SKILL.md（凭证技能：先验证后安装、key 不回显）](file:///Users/lifcc/Desktop/code/AI/tools/video-ai-landscape/elevenlabs-plugin/skills/general/setup-api-key/SKILL.md)
- [[本地] runway-mcp-plugin runway-media SKILL.md（MCP 包装模式、rough cost 确认规则）](file:///Users/lifcc/Desktop/code/AI/tools/video-ai-landscape/runway-mcp-plugin/skills/runway-media/SKILL.md)
- [[远程] PixVerseAI/skills 仓库（单入口 SKILL.md + capabilities/workflows + 三契约文件结构）](https://github.com/PixVerseAI/skills)
- [[远程] PixVerse execution-contract.md 原文（流分离/ID 语义/部分批处理/幂等键/退出码/退避）](https://raw.githubusercontent.com/PixVerseAI/skills/main/skills/references/execution-contract.md)
- [[远程] PixVerse prompt-contract.md 原文（改写授权/禁改清单/提问门槛）](https://raw.githubusercontent.com/PixVerseAI/skills/main/skills/references/prompt-contract.md)
- [[远程] PixVerse skills/SKILL.md 原文（三路由表、加载纪律、契约引用方式）](https://raw.githubusercontent.com/PixVerseAI/skills/main/skills/SKILL.md)
- [[远程] PixVerseAI/cli 仓库（退出码 0-7、task wait/status、capabilities.json、npm 分发）](https://github.com/PixVerseAI/cli)

---
