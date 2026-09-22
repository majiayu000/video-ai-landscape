# 生态推演与战略 · 前瞻版（v2）

> 生成：2026-09-22 · 方法：**21 路 schema 约束 agent 真实网络调研**（5 路生态维度 + 4 路 Sora 深挖 + 5 路厂商前瞻 + 6 路全域扩展 + 8 路第二轮深挖，含 2 路限流补跑）+ 交叉合成。
> 本文回答一个问题：**他们哪里做得好、未来要做什么、没做什么我们能做。**
> 置信度：**[官方源]** > **[多源交叉]** > **[单一来源]** > *推断*。机器可读数据见 `data/`（价格 34 条、能力矩阵 13 条，as_of 2026-09-22）。逐路原始发现见 `docs/research-*.md`。

## 0. 核心判断（TL;DR）

1. **接入层战争的形态已经定型**：SKILL.md + MCP + CLI 三件套。**PixVerse（中国唯一全做齐的厂商）、Tavus（机器可读全家桶）、Runway（官方托管视频 MCP 第一家）** 已亲自验证路线可行——这不再是判断，是既成事实。
2. **但厂商集体收缩回围墙**：fal 全押 fal Agent + 双 MCP（CLI/skills 通道战略放弃）；Higgsfield 转向 ChatGPT 宿主分发；HeyGen 把渲染收拢进 Hyperframes 并 10-31 日落 v1/v2 API；Pika 砍掉旧 Developer API。**每一家都只覆盖自己，跨厂商公共层无人做**。
3. **纯"路由/聚合"正在失去护城河**：Runway 三周连击把自己做成多模型调度层（Model Router→容量回退→路由历史）；VideoRouter 上线但零牵引（HN 1 分 1 评）且收 2% 平台费；Hedra 从应用层转身做 75+ 模型聚合；腾讯混元代销 Vidu/Kling。**聚合在垂直分层挤入，中立层必须退守到"契约 + 验收 + 一致性资产"——聚合站做不了的三件事。**
4. **价值正沿六层栈上移**（L3 标准已定局 → L4 分发/信任、L5 编排/验收开战），而 90 天证据显示 **L5 的三个具体空位——跨厂商任务契约、生成后判片闭环、角色一致性资产——没有任何一家能做**（利益冲突 + 立场限制），这是结构性而非暂时性的空位。

## 1. 六层栈（90 天后的更新）

```
L5 编排/验收层      ← 空位确认扩大且经需求侧验证：90 天内 GitHub 出现 ≥8 个自建轮询/续跑仓库（本文第 2C/2D 节）
L4 分发/信任层      ← skills.sh 哑铃型（厂商级技能 vs 聚合技能差两个数量级）+ 榜单数据毒性 + Audits 仅覆盖 50/150 万
L3 标准层 ✅ 已定局  MCP（Tasks 扩展演进中）· SKILL.md（~40 产品采纳，规范仍未捐入中立基金会）· AGENTS.md
L2 聚合/路由层      ← 竞争烈度骤升：fal 官方末轮 $4.5B（Series D）→ $8B 谈判中[单一来源]、OpenRouter 入场视频（2026-08-19 官宣被 Stripe 收购——无状态路由终局的实证）、Runway Model Router、VideoRouter、Hedra 转型、腾讯代销
L1 模型层           美国两强（Veo/Grok）+ 中国两强（Kling/Seedance）+ 开源只剩 Wan2.2 一家活跃
L0 算力/电力        训练侧：4090 Community $0.34/hr，Wan2.2 LoRA 24GB 可训——个人可承受
```

90 天最重要的三条交叉验证主线：

1. **"厂商官方亲自下场"密集出现**：Runway 官方托管 MCP（9-11）、ComfyUI 官方 comfy-mcp + comfy-skills（7-01）、Higgsfield MCP 铺进 7+ 宿主、Synthesia 入场（8 月底）。**信号：agent 面从"第三方包装"进入"官方基建"阶段**——第三方单点包装的窗口正在关闭，跨厂商层的窗口正开着。
2. **平台死亡与断契约成为常态**：Sora 全周期退场（12 个月）[官方源]；Pika 砍 dk_ 密钥；HeyGen 日落 v1/v2；MiniMax MCP 枚举落后自家 API 一代；Azure 比 OpenAI 更早下架 Sora。**每一起都是"契约层必须把供应商死亡当常态假设"的论据。**
3. **中国"一家独走、四家缺位"**：PixVerse 三件套（CLI+MCP+SKILL.md，execution-contract 设计与我们同构）独走；火山/阿里/腾讯/智谱官方视频 MCP/Skill 数量为零。**为四家做"官方没有的第一方体验"是被验证过的空位。**

## 2. 机会地图（本文核心）

### 2A. 做得好——可借力

| 谁 | 做了什么 | 我们怎么借 |
|---|---|---|
| **PixVerse** | 全球最完整的单厂商 agent 三件套：execution-contract.md / prompt-contract.md / `capabilities --json` 离线能力查询 / `--no-wait` 超时不等于失败语义 / 非零退出可带部分成功 | **直接照抄契约语义**，从单厂商升级为五厂商统一层；其源码结构证明该模式可被厂商官方采纳（甚至反向 PR） |
| **Tavus** | llms.txt + openapi.yaml + skill.md 机器可读全家桶；PAL 可委派第三方 MCP | 发现层不依赖注册表：CLI 内置 `--discover` 直接拉厂商自描述文件 |
| **Runway（skills 层）** | SKILL.md 内置每模型 credit 价格表、输出行带成本、`get_credit_balance` 前置检查 | **计费透明做成契约一等公民**的范本（vs Higgsfield 五套计费池不透明——两极中透明那极的写法照抄） |
| **火山 Seedance 2.0** | 任务契约最完整：callback_url、execution_expires_after 可配、任务 ID 保留 7 天、priority 队列、flex 离线半价、draft 样片模式、return_last_frame 串联多镜头 | 统一任务层的目标契约形态——把它做成跨厂商抽象 |
| **ComfyUI 官方** | comfy-mcp（本地 40 工具）+ Comfy Cloud MCP + comfy-skills | 本地路径的官方形态已立：`--provider local-comfyui` 与云同构调用有了对齐对象 |
| **HeyGen HyperFrames** | 免费本地渲染技能（HTML→MP4）拿下 52K stars / 60 万安装 | **免费/本地入口 → 计费 API 升级层**的分发漏斗模型（免费技能与计费技能安装量差 100 倍，入口必须免费） |
| **Vidu** | 全行业唯一做"提交前成本预估"的厂商 | dry-run 报价的方向被厂商背书；我们做成跨厂商版 |
| **fal 双 MCP** | Run MCP（造东西）+ Platform MCP（只读运维）分权设计 | agent 权限分层的参考架构 |
| **Higgsfield skills frontmatter** | 「Use when 触发词 + NOT for 反向路由 + Chain with 链式声明」 | 技能间路由的最优写法，零机制成本，直接采纳 |

### 2B. 将要做——可搭车

| 谁 | 将做什么 | 信号强度 | 我们怎么搭 |
|---|---|---|---|
| **Runway** | Dev Platform 成公司主线（Founding DX Lead + 产品/设计/工程四条线同招）；skills 收敛到 runway-dev-* 唯一路径；Model Router 或扩展成跨厂商路由市场 | [官方明示] | 它做"Runway 内的多模型"，我们做"跨厂商的 Runway 接入"——官方流量可蹭（给 runwayml/skills 提 CLI 层 PR） |
| **fal** | fal Agent GA（文档树已备全：memory/skills/sandbox/training/video-sequences/spending-caps）；/agent-v2 路由已现 | [官方明示] | Agent 正式收费前，契约 CLI 是"不进围墙用同一批能力"的出口 |
| **腾讯** | 混元→TokenHub 迁移（OpenAI 兼容协议 + 代销 Kling/Vidu） | [多源交叉] | TokenHub 新平台 = 新接入面 = 文档/工具真空期，第一时间做适配器 |
| **HeyGen** | 全部渲染收拢 Hyperframes；v1/v2 API 10-31 日落 | [官方明示] | 迁移窗口内容：受影响开发者的迁移工具 + 内容 |
| **Google** | agentic 视频理解（自导航时间线省 88% token）+ Genmedia MCP servers | [官方明示] | 判片层的大脑供给已就位——judge 步骤直接接 |
| **智谱** | Managed Agents 全套 Skill/MCP/部署 API，视频未接入但基建就绪 | [官方明示] | cogvideox-3（4K/60fps/首尾帧，国产闭源独有参数）是"能力强但没人接"的洼地，第一批适配目标 |
| **MCP 规范** | Tasks 扩展（长任务 task handle）演进 | [官方明示] | 视频异步任务的标准归宿——按新规范起步，不做旧的 |

**资金面信号（2026-09-22 资本路数图回收，详见 `docs/research-deep-dive-2`）**：

| 事件 | 状态与置信度 | 含义 |
|---|---|---|
| **MiniMax 港股挂牌** | 2026-01-09（0100.HK），首日 +109%、市值破千亿港元 [官方源/多源交叉] | 港股 AI 退出通道实测走通——可灵/PixVerse/阶跃的估值锚与模板 |
| **可灵分拆独立上市** | 快手 2026-05-12 港交所公告确认"评估中、初步阶段"[官方源]；WSJ 报约 $2.8B 融资（20亿/28亿口径不一）[单一来源]；$20B 估值/最早 2027 为传闻 | 若落地是视频生成史上最大单体资本事件；分拆后独立 P&L 将更激进商业化 API——围绕独立可灵的服务层（聚合/评测/合规出海）尚未有人卡位 |
| **PixVerse $439M C 轮扩展** | 2026-07-14，估值破 $2B [多源交叉]；港股 A1 仅"考虑年内"传闻级 | 中国阵营资本弹药最足的挑战者；其 CLI/技能三件套有官方持续投入保障 |
| **阶跃星辰/智谱 IPO 进程** | 阶跃 50 亿+元 B+（2026-01）+ 传 $2.5B 新融资[未确认交割]；智谱科创板辅导验收（2026-06）[多源交叉] | 中国 LLM 层资本化与视频层撞线；智谱 cogvideox-3 洼地判断获得资金面佐证 |
| **Cloudflare 吞并 Replicate** | 2025-11-17 官宣，对价未披露 [官方源] | **独立中立模型托管品类消失**——中立层只剩"契约+验收+角色资产"可站，不做托管再添论据 |
| **产业资本入场** | Nvidia 入 Decart C 轮、CAA/Comcast 入 Moonvalley、华勤入阶跃 [多源交叉] | 资金为"模型+场景"绑定定价；纯套壳叙事融资窗口收窄 |
| **风险对冲** | fal $8B 谈判未交割、Decart 估值口径分歧（$3.1B vs $4B）、港股上市潮→API 价格战 [多源交叉] | 上市募资方须冲收入 → API 降价最直接 → 纯转售中间商被挤出；中立层价值必须落在路由+SLA+成本优化，赚价格离散度与可用性红利 |

### 2C. 没做——可占位（按确定性排序）

1. **跨厂商统一任务契约**（确定性：最高）
   五家中国协议各异 + webhook 验签各家一套 + 断线恢复全无 + 产物 URL 24h-30 天过期。90 天内至少 4 个独立项目在自造轮子（需求侧证据）。
   → 本地 task store + 统一句柄（submit/poll/cancel/resume/artifact manifest）+ 到期前自动归档到用户自有存储 + 幂等键 + unresolved 状态机。**这是 CLI 的地基。**
2. **生成后判片/验收闭环**（结构性空位：厂商不愿给自己的生成打分）
   VBench 16 维体系已开源（但 flickering 等维度 VLM 低帧率下不可见——需按"VLM 可判性"重新分层）；VideoFeedback 33.6k 带 5 维整数分先例；Claude 无视频输入（GIF 取首帧）→ 抽帧方案是必要件。
   → judge 步骤一等公民：抽帧 → 便宜 VLM（Gemini 3.8 Flash / GLM-5.3-Flash / DeepSeek V4.1-Flash）→ 结构化 verdict JSON（维度分 + 失败分类枚举 + 建议动作 retry/换模型/改 prompt）→ 驱动重试策略。
3. **角色一致性资产契约 + 视频 LoRA 训练串联**（七家训练设施全缺位）
   三条断路：厂商 reference API（无持久资产）/ RunPod 外挂 LoRA URL（得自己去别处训）/ Modal 自管代码。开源侧已可行：musubi-tuner 官方支持 Wan2.2 LoRA，fp8+block swap 下 720×1280 图像训练仅 24GB 显存 [官方文档]；4090 Community $0.34/hr → 24 小时约 $8-18。
   → `character_id` = 数据集 + 权重引用 + trigger 词 + 一致性评测集 + 各家端点适配器；一条命令：训练（spot GPU）→ 托管（HF/Volume）→ 推理（RunPod/Replicate/厂商 API）。
4. **计费可信层**（痛点密度最高：fal 90 天 11+ 条锁号 bug、#1175 80 秒按 10,272 秒计费、官方 0 回复）
   → per-generation 成本账本 + 预算熔断（超限降级）+ 本地账本与供应商账单对账 + 执行时长/计费时长偏差告警。Higgsfield 五套计费池同理需要一个编程化查询口。
5. **供应商寿命预警**（每起断契约都是论据）
   → 定期快照各厂商模型目录（模型/参数/价格/弃用状态），机器可读 diff + 弃用页监测 + 旧→新参数映射建议，嵌进用户 CI。
6. **skills.sh 厂商级技能矩阵**（哑铃型空端：veo 474 / sora 916 / runway 300-500 安装 vs 聚合技能 60 万）
   → 每厂商一个 skill + 总路由 skill，官方调研级质量差异化；**别追安装数**（genmedia-labs 13★/60 万安装、superpowers 集群刷量嫌疑、Zenity 170 万安装恶意家族）。
7. **中国厂商国际接入规范层**：双区端点探测、AK/SK→OAuth 封装、凭据一处配置多平台映射、英文文档——中国厂商不做、国际开发者最痛。
8. **分镜 JSON 契约**：镜头/角色/一致性约束/每镜目标厂商与参数，可版本化——把 LTX Studio 的封闭体验开放化；fal Agent 的 video-sequences 锁在围墙内，开放版空着。
9. **合规字段**（中国《标识办法》+ GB 45438-2025 已生效：显式+隐式双层义务；实测四家视频 API watermark 默认 false、无一家文档化隐式元数据输出——**合规责任系统性落在调用方**）
   → 契约字段：label_required / implicit_metadata / c2pa / 责任划分；commercial-safe 路由（license_tier：Marey FULLY LICENSED 档无处表达）。
10. **不做清单**：纯路由/聚合（Runway+VideoRouter+Hedra 三方挤压）、薄 API 包装 skill、低代码编排（OpenAI 弃用 Agent Builder 证明退潮）、押注世界模型、绑定单一厂商。

### 2D. 第三轮验证：需求侧证据 × 行业纵深 × 前沿推演（2026-09-23 回收，wf_924b570c，8/8 零失败）

**2C 占位 vs 需求证据对照**（详见 `docs/research-round3-2026-09-22.md`）：

| 2C 占位 | 需求侧证据（90 天一手） | 状态 |
|---|---|---|
| 1 统一任务契约 | GitHub ≥8 个自建轮询/断点续跑/webhook 仓库（788★ 中文 skill 库、542★ 统一客户端等）；VideoRouter/Velokey/useapi/APIMart 四家商业聚合卖点第一条全是 failover+统一 API；官方 API 3 并发/Higgsfield 8 并发是硬约束 | ✅ 已验证，最强 |
| 2 判片闭环 | dawndrain 自建 pitch_check/listen.py QC；中文团队 C1~C20 机检门（FAIL 清零才交付）；前沿侧 FIRM-Video 奖励模型 + 15 个新基准使自动化首次可行；**VBench 高分≠物理正确（0.8 vs ≤0.42）证实必须多判器融合** | ✅ 已验证 + 技术地基就位 |
| 3 角色资产 | 中文团队发明 Asset-First（4 View 资产板+台账）；长片剧组外购 Soul Cinema character sheets；liyue-aigc 专做角色漂移诊断——全是手工先例 | ✅ 已验证（手工替代品存在=付费意愿存在） |
| 4 计费可信 | useapi 实测 fal 较官方 +82% 溢价仍是"市场默认"；"两次改词失败就换内容"重试铁律；重生成成本按可用率放大 10 倍的推算帖反复出现 | ✅ 已验证 |
| 5 供应商寿命预警 | 开源侧同样适用：WanVideoWrapper（6708★）自 5-24 零提交、1282 issues 无人接盘 | ✅ 证据扩展到开源 |
| 7 国际接入规范 | 独立开发者自建 542★ 统一客户端动机原话："各家 API 与模型 ID 独立变动" | ✅ 已验证 |

**第三轮新发现的可占位**（补充进 2C 清单）：
- **提示词编译器**：否定词失效三改法、跨模型语法分流（H3 六段式自动转换）已被中文团队手工实现——一份创意编译到各家语法契约
- **审核预检/合规转译中间件**：手工"安全转译词典"（血腥→"气浪震散"）+ $14k/年真脸企业授权门槛，衔接权利层与个人开发者
- **音轨后期管线**：dub_clip.py（换台词不重渲视频）先例；Google/xAI 禁音频同步使后期方案成为刚需
- **LoRA 可移植 manifest + license 合规 CLI**：CivitAI 同一 LoRA 发五个 base 版本装错率高；Wan(Apache-2.0) vs H3/LTX(自定义) 无程序化判断工具
- **电商素材批量管道**：唯一被证实的规模赚钱工作流（AI UGC $1-11/条 vs 真人 $185-2000；50 变体 <$200 vs $7,500+）——CLI 第一批目标用户画像

**行业纵深**：AI 短剧进入工业化（2026Q1 新微短剧约 95% AI 生成；但 98.7% 未回本）——工具空位：多语种译配、脸谱授权合规、投前回本预测；广告侧**信任缺口大于成本缺口**（Icon 从 AI 转回真人代理、Smartly/Celtra 均未接视频生成 API=编排层空位）；影视侧 Netflix 官方披露约 300 部作品用 GenAI、previz→生成无标准契约、影院级 QC 无人定义。反面证伪：YouTube 7 月起对批量 slop 去货币化——勿做 slop 变现流。

**前沿 → 契约设计约束**（12-36 月内必须吸收，完整推演见研究笔记）：
1. 免训练时长外推（5s 基座→2 分钟，KV 缓存记忆工程）→ 契约时长改"基座×外推倍率"两段式 + 角色资产须带"时间不变式"包
2. 流式实时生成（22-30FPS 单卡）→ 契约从异步轮询转向 latency_budget/可恢复 token；判片改分块在线抽检（判块延迟 < 生成块时长）
3. 世界模型双产物（World Labs Atlas：视频+显式 3D）→ 契约新增 2D 视频轨+3D 场景轨双产物字段；纯 2D 图参考资产无法参与相机控制任务
4. 判片可自动化（FIRM-Video）→ 契约内嵌机器可读验收 checklist schema；深伪检测器近随机 → 真伪判别依赖 provenance 元数据
5. 音画一体实时化（30FPS 全双工）→ 契约新增 audio_track/lip_sync_tolerance/多人对话轮次表；"无声视频+后期配音"契约被淘汰

**开源权力转移**：MiniMax H3 开放权重（月下载 404 万、day-0 ComfyUI 支持）一个月长出十几个专用节点；Wan 系（Apache-2.0）进入存量维护；**中文社区已在 ComfyUI 之外自造 production.json 生产契约（hash 绑定审批，8-30 创建已 163★）**——我们要做的契约层，社区已经用脚投票。

## 3. 12-36 个月推演（90 天证据修正版）

| 窗口 | 高确定性事件 | 含义 |
|---|---|---|
| 0-12 月 | 官方 MCP/skills 基建化完成（Runway 已开、其余厂商跟进）；skills.sh 信任机制升级（Audits 扩容、签名）；TokenHub/HeyGen 日落制造迁移窗口；判片先例出现 | **契约层 + 判片层现在占位，6 个月后就是"已有标准"**；迁移工具常态化 |
| 12-24 月 | 编排层争夺战：fal Agent/Runway Router/OpenAI Agents API 三线撞车（全部绑自家）；规范层 SKILL.md 治理变数 | 中立契约层成为各家编排的公共底座或被平台吞噬——**跨厂商是唯一防线** |
| 24-36 月 | 分发 App-Store 化 vs 多注册表并存定型；视频 LoRA 训练服务化（七家中会有厂商补位） | 押注"可审计的可信包 + 可移植"；角色资产格式若成事实标准即护城河 |

## 4. 行动建议（更新版）

资产盘点：contract-first 视频 CLI（在建）+ 调研报告与 103 个 SKILL.md 源码级分析 + **活数据层 `data/`（价格 34 条/能力矩阵 13 条，周更新鲜度检查）** + 双语与中国市场位置。

1. **本周 · skills.sh 厂商级矩阵占位**（成本≈0）：避开聚合赛道（RunComfy 系 60 万安装是刷量嫌疑的营销阵地，别对标它的打法），做厂商级 contract-first 技能（veo/kling/seedance/wan/cogvideo 各一 + 总路由一）+ 免费/本地入口技能（HyperFrames 模型：免费技能 install 是计费技能的 100 倍）。技能是漏斗不是产品。
2. **一个月内 · "静默断裂"修复位**：9-24 Sora API 物理消失后的一手故障修复内容 + 迁移工具（n8n 模板仍在诱导接入死 API）；长期做成"供应商寿命预警"功能（见 2C-5）。
3. **3-6 月主线 · CLI 三支柱**（2C-1/2/3 落地为产品）：
   - **任务契约层**：统一 submit/poll/resume/artifact 归档（地基）
   - **判片闭环**：judge rubric + verdict schema（差异化，`docs/research-deep-dive-2` 已有设计输入）
   - **角色资产**：character_id 契约 + Wan2.2 LoRA 训练串联（七家全缺位，$8-18/次成本已验证）
   三支柱之上才是路由（价格数据已有 `data/prices.json`：同模型跨渠道价差 67%-700%）。**第三轮需求侧验证：三支柱全部从"推断空位"升级为"已验证付费痛点"（见 2D 对照表），第一批目标用户画像 = 电商素材批量管道（唯一证实规模的赚钱工作流）+ 中文 AIGC 短剧工坊（788★ 工具库证明密度）。**
4. **持续 · 数据即基础设施**：`data/*.json` 每月实采刷新（as_of 纪律），价格表 + 能力矩阵 + 供应商健康指数是 CLI 的数据底座，也是别人会引用的公共品。
5. **不要做**：纯路由层、通用聚合站、低代码编排、薄包装 skill、绑定单一厂商、追 skills.sh 安装数。

**生态位一句话：厂商做"自家围墙内的垂直整合"，我们做"跨厂商的契约、验收与角色资产"——聚合站与厂商都因立场坐不上去的位置。**

## 5. Sora 事件验证记录（存档）

**已直接验证 [官方源]**（2026-09-22）：
- OpenAI Deprecations 页：Sora 2 模型与 Videos API 2026-09-24 移除（developers.openai.com）
- OpenAI 帮助中心：App/Web 2026-04-26 停服（help.openai.com）
- 社区开放权重请愿被官方拒绝（2026-09-08"没有发布计划或时间表"）

**深挖结论**（wf_b3382967）："迁移潮"是弱证据（HN 热度归零、GitHub 零迁移仓库、头部厂商零承接）；真实痛点 = 9-24 后 workflow 静默断裂的被动修复。格局未被改变：分食者全是既有玩家；三个次级变化 = 开放权重真空（Wan 3.0 转 API-only）、聚合层资本化（fal $4.5B 官方、$8B 谈判中）、榜单营销战（阿里匿名 Happy Horse 登顶后自曝）。

## 6. 主要来源

官方：PixVerse CLI/Skills 仓库 · Tavus 文档 · Runway docs.dev.runwayml.com · fal docs/changelog · skills.sh(+API) · OpenAI Deprecations · Comfy-Org · 火山方舟文档 · 阿里百炼文档 · 腾讯云文档 · kling.ai · musubi-tuner/diffusion-pipe · VBench/VideoFeedback · GB 45438-2025 与《标识办法》条文
媒体/研究：The Information · CNBC · WSJ · SCMP · Zenity Labs · Socket · a16z · HN(Algolia API 一手数据) · GitHub API 一手数据

> 完整逐条来源见各研究路的结构化输出（workflow runs: wf_328d5117 / wf_b3382967 / wf_30803c52-a09 / wf_354c2d89-361 / wf_1b079cd9-5e7）及 `docs/research-*.md` 三份笔记。二手转述的商业数字已标注，未经审计。

## 7. 新鲜度日志（Freshness Log）

- **2026-09-21**：5 路生态研究（wf_328d5117）完成，形成初版分析。
- **2026-09-22 上午**：直接验证 Sora 关停；实测 skills.sh 推翻"视频类目空着"初判，行动牌 1 改写。
- **2026-09-22 下午**：Sora 深挖回收（迁移潮降级为弱证据、skills.sh 哑铃型确认、榜单毒性实证）；行动牌 2 改写为"静默断裂修复位"。
- **2026-09-22 晚 · 全域扩展 + 第二轮深挖回收（13 路）**：本文重写为前瞻版 v2。关键修正：① Runway Model Router 证明纯路由不设防，中立层定位改为"契约+验收+角色资产"；② genmedia-labs 确认为 RunComfy 营销马甲（源码级证据）；③ 七家训练设施厂商"视频 LoRA 训练即服务"全缺位 + musubi-tuner 24GB 配方使个人训练可行；④ 中国"一家独走四家缺位"（PixVerse 唯一）；⑤《标识办法》实测：API 侧水印默认关、隐式元数据无人做——合规责任在调用方；⑥ 价格/能力数据入库 `data/`（as_of 2026-09-22）。
- **2026-09-23 凌晨 · 资本路数图回收**（money-map 补跑完成，8/8 零失败）：第 2B 节新增资金面信号表。关键修正：① **fal $8B 为谈判中[单一来源]**，官方末轮实为 Series D $4.5B（2025-12）——此前表述过强，已改；② 可灵分拆从传闻升级为快手港交所公告官方确认（评估中）；③ MiniMax 已上市打样港股通道；④ Cloudflare 吞并 Replicate → 中立托管品类消失，强化"不做托管"论据。

- **2026-09-23 凌晨 · 第三轮全域调研回收（8 路）**：需求侧/行业/前沿/开源。新增第 2D 节（占位 vs 需求证据对照 + 前沿契约约束 + 开源权力转移）。关键修正：① 2C 三支柱获一手付费证据（≥8 个自建轮子仓库、C1~C20 机检、Asset-First 资产板）；② VLM-only 判片被 VBench≠物理正确证伪，判片设计改多判器融合；③ 目标用户画像收窄为电商素材管道 + 中文短剧工坊；④ YouTube slop 变现证伪，列入不做清单；⑤ 开源侧中文社区已自造 production.json——契约层有社区脚票。

- **2026-09-23 · 第四轮战略理论回收（6 路，35 案例 33 定律）**：新增 `STRATEGY-DOCTRINE.md`（金字塔顶层纲领）与 `research-round4-strategy-2026-09-23.md`。纲领要点：格式免费验收收费；状态定律（无状态转发必被吞——OpenRouter 82 天被 Stripe 收编为实证）；视频波窗口 6-12 个月、相位≈LLM 波 2023 年 2-4 月；四盏灯相位仪表盘（第四盏=官方内置验收，亮即转向）；九条决策启发式 + 反纲领八条。

**方法论**：任何"窗口判断"必须在行动前 24 小时内用一手数据复核；价格/能力数据超 30 天由 CI 标黄。
