# 执行计划 · 从机会地图到产品（v1）

> 制定：2026-09-23 · 依据：三轮 29 路调研（`docs/research-*.md`）+ 战略文档 v2（`docs/ECOSYSTEM-STRATEGY.md`）+ atlas CLI 代码现状实测。
> 本文回答：**先做什么、后做什么、每一步怎么验收、不做什么。**

## 0. 生态位与北极星

**生态位一句话：厂商做"自家围墙内的垂直整合"，我们做"跨厂商的契约、验收与角色资产"——聚合站与厂商都因立场坐不上去的位置。**

- **北极星指标**：一个开发者用一条命令，把一个视频生成任务（含重试与验收）跑通并拿到本地归档产物——跨 ≥3 家厂商行为一致。
- **第一批目标用户**（第三轮需求侧验证）：① 电商素材批量管道（AI UGC $1-11/条 vs 真人 $185-2000，唯一证实规模的赚钱工作流）；② 中文 AIGC 短剧工坊（2026Q1 新微短剧约 95% AI 生成，788★ 工具库证明密度）。
- **反目标**：slop 变现流（YouTube 7 月起去货币化）、纯路由/聚合、低代码编排、薄包装 skill、追 skills.sh 安装数。

## 1. 资产盘点（已有什么）

| 资产 | 状态 | 位置 |
|---|---|---|
| atlas CLI（Go，v0 production-ready） | 单厂商（AtlasCloud）契约先行骨架：`internal/taskstore`（任务持久化）、`internal/contract`、`internal/schema`、`--json` 输出、doctor、skills install、实验性 atlas-mcp、npm 分发 | `AtlasCloudTeam/cli`（工作库） |
| 调研库（本库） | 29 路研究笔记 4 份 + 战略 v2 + data/（价格 34 条、能力矩阵 13 条、schema、CI 新鲜度） | `majiayu000/video-ai-landscape` |
| 设计输入 | verdict schema（judge 路）、musubi-tuner 24GB 配方（recipes 路）、PixVerse 契约语义（patterns 路）、Seedance 2.0 目标契约形态（2A 表） | 研究笔记内 |
| 技能发布经验 | skills.sh 实测 + 103 个 SKILL.md 源码分析 + 官方技能仓库快照站 | 本库 site/ |

**关键架构决策（需拍板，见 §7-D1）**：中立层不能住在厂商品牌的 CLI 里。建议新起**独立中立二进制**（工作名 `videokit`，个人仓库），atlas 作为第一个 provider adapter 移植——研究反复证明"跨厂商中立"是唯一防线（Runway Router/VideoRouter/Hedra 三方挤压纯路由；Cloudflare 吞并 Replicate 吞掉中立托管）。

## 2. 里程碑总览

| 里程碑 | 日期 | 交付物 | 验收标准（fresh command） |
|---|---|---|---|
| **M0 占位与漏斗** | 09-30 前 | skills.sh 厂商级技能矩阵 v1（6 个技能）+ 中立 CLI 仓库立项（spec + README + 契约 v0 草案） | 技能可在 skills.sh 安装；契约草案入库 |
| **M1 任务契约层 MVP** | 10-31 前 | 跨厂商统一任务句柄：submit/poll/cancel/**resume**/artifact 归档，先接 2 家（Seedance 2.0 + Kling 国际 API） | `vk submit → kill 进程 → vk resume` 拿到同一产物；`vk submit --dry-run` 出成本预估；产物到期前自动归档本地 |
| **M2 判片闭环 MVP** | 11-30 前 | verdict schema v0 + 抽帧 + judge 步骤（便宜 VLM）+ verdict 驱动重试 | 一个 10s 生成端到端：生成→判片→低分自动重试→verdict.json 落盘 |
| **M3 角色资产 MVP** | 12-31 前 | character_id 契约 v0 + Wan2.2 LoRA 训练串联 + license/合规字段 | `vk character train → host → infer` 一条链（spot GPU）；资产带评测锚点与 license_tier |
| **M4 公开 1.0** | 2027-03 前 | 三支柱 GA + 供应商寿命预警 + 中国厂商接入规范层（cogvideox-3、TokenHub） | ≥3 厂商一致行为北极星达成；价格/能力数据 30 天新鲜度 CI 绿 |

节奏依据：0-12 月窗口内"契约层+判片层现在占位，6 个月后就是已有标准"（战略 §3）；可灵分拆独立上市评估中（2027 挂牌窗口前锁定集成关系）；HeyGen v1/v2 10-31 日落制造第一个迁移内容窗口。

## 3. 分阶段细案

### M0（本周）· 占位与漏斗 — 成本≈0
- **A1 技能矩阵**：`veo / kling / seedance / wan / cogvideo` 各一 + 总路由技能一。写法照抄三个范本：Runway 价格表内置 + 余额前置检查（计费透明一等公民）、Higgsfield frontmatter（Use when / NOT for / Chain with）、PixVerse 失败语义（超时≠失败、非零退出可带部分成功）。免费技能做漏斗入口（HyperFrames 模型：免费:计费安装量 = 100:1）。
- **A2 中立 CLI 立项**：新仓库 + `docs/CONTRACT-v0.md` 契约草案——统一句柄（submit/poll/cancel/resume/artifact manifest）+ 幂等键 + unresolved 状态机 + 到期归档字段。目标形态 = Seedance 2.0 契约（callback_url、任务 ID 保留 7 天、return_last_frame 串联）；兼容 MCP Tasks 扩展方向。
- **验收**：技能安装可用；契约草案有 5 家厂商字段对照表（数据源：`data/capabilities.json`）。

### M1（10 月）· 任务契约层 — CLI 的地基
- **B1 provider adapter 框架**：每家一个 adapter（能力矩阵声明 `capabilities --json` 离线查询——PixVerse 模式）；并发上限建模（官方 3、Higgsfield 8 是硬约束，需求侧反复出现痛点）。
- **B2 断线恢复**：本地 task store + `resume`（进程 kill / 网络断 / 机重启后拿回任务）；90 天内 GitHub ≥8 个自建轮子仓库证明此为第一痛点。
- **B3 产物归档**：`data/capabilities.json` 已录各家 url_validity（24h-30 天）——到期前自动下载到用户自有存储（R2/S3/本地），内容寻址缓存避免重付费。
- **B4 计费可信层 v0**：per-generation 成本行（Runway 模式）+ `--dry-run` 报价（Vidu 模式）+ 本地账本。价格数据源 `data/prices.json`（同模型跨渠道价差 67%-82%+）。
- **验收**：北极星在 2 家厂商上成立；故障注入测试（断网/杀进程/伪 5xx）全部可恢复。

### M2（11 月）· 判片闭环 — 差异化支柱
- **C1 verdict schema**：checklist 式机器可读验收（物理/时序/口型/镜头连续性逐项布尔+分值）——FIRM-Video 方向；**多判器融合**（VBench 高分≠物理正确已证伪 VLM-only）。
- **C2 judge 管线**：抽帧 → 便宜 VLM（Gemini Flash / GLM-Flash / DeepSeek Flash 档）→ verdict.json；长视频按首/中/尾分块抽检 + 时间漂移曲线（角色 ID 相似度、退化斜率）；音画偏移 <45ms 检测强制项。
- **C3 重试策略**：verdict 驱动（retry / 换模型 / 改 prompt——含否定词改写等编译规则）；预算熔断（超限降级，重生成成本放大 10 倍是反复出现痛点）。
- **验收**：10s 1080p 单次判片成本落在研究测算区间（约 $0.02-0.05）；端到端自动重试演示。

### M3（12 月）· 角色资产 — 七家全缺位的空位
- **D1 character_id 契约**：数据集 + 权重引用 + trigger 词 + **评测锚点**（多角度标准帧、音色样本——判片路结论）+ 各家端点适配器（厂商 reference API / LoRA URL / 自托管三形态抹平）。
- **D2 训练串联**：musubi-tuner Wan2.2 LoRA（fp8+block swap，24GB 显存，4090 Community $0.34/hr → 全程 $8-18）→ HF/Volume 托管 → RunPod/Replicate/厂商 API 推理。
- **D3 合规与数据**：license_tier 字段（Marey FULLY LICENSED 档无处表达的问题）+ label_required/implicit_metadata/c2pa（《标识办法》实测责任在调用方）+ LoRA 可移植 manifest（trigger/CFG/base 兼容矩阵——CivitAI 五版本装错痛点）+ 开源 license 合规 CLI（Wan Apache-2.0 vs H3/LTX 自定义无程序化判断工具）。
- **验收**：同一角色资产在 ≥2 家推理端点产出一致性达标片段（跨镜头 ID 相似度阈值）。

### M4（2027 Q1）· 公开 1.0 与护城河加深
- 三支柱 GA + 北极星扩到 ≥3 厂商；供应商寿命预警功能化（定期快照模型目录 diff + 弃用页监测——Sora 12 个月全周期退场、HeyGen 10-31 日落都是模板案例）；中国厂商国际接入（cogvideox-3 洼地：4K/60fps/首尾帧无人接；腾讯 TokenHub 适配器——新平台文档真空期第一时间进）。
- 内容飞轮：静默断裂修复内容（Sora 9-24 后一手故障修复 + n8n 死模板纠偏）持续供给。

## 4. 风险登记（研究依据 → 对冲）

| 风险 | 依据 | 对冲 |
|---|---|---|
| 厂商断契约常态化 | Sora 全周期 12 个月退场；Pika 砍 dk_；HeyGen 10-31 | 契约层把供应商死亡当常态假设；寿命预警内置 |
| 编排层撞车（12-24 月） | fal Agent / Runway Router / OpenAI Agents API 三线全绑自家 | 跨厂商中立立场 = 唯一防线；不碰编排只做契约 |
| 上市潮价格战压毛利 | MiniMax 已挂牌、可灵/阶跃排队；纯转售中间商被挤出 | 不做转售；赚价格离散度信息与可用性红利（数据层） |
| 榜单毒性 | genmedia-labs 13★/60 万安装刷量嫌疑；Zenity 170 万恶意家族 | 技能是漏斗不是产品；不追安装数 |
| 独立开发带宽 | 一人节奏 | 里程碑严格串行，每阶段独立可发布；M0 成本≈0 先建分发 |
| 前推翻转契约设计 | 长视频外推/实时流式/3D 双产物（2D 节 5 条约束） | 契约字段预留（两段式时长、latency_budget、双产物轨）；每季对照前沿笔记复核一次 |

## 5. 不做清单（每季复核）

纯路由/聚合站 · 编排平台 · 中立模型托管（Cloudflare-Replicate 已证品类消失） · slop 变现流 · 低代码可视化编排 · 绑定单一厂商 · 押注世界模型 · 追 skills.sh 安装数。

## 6. 资源与成本

- 人力：一人 + agent 工作流（本库调研模式已验证：29 路、零编造、全程可溯源）。
- 现金成本：M0 ≈ $0；M2 判片 ≈ $0.02-0.05/次；M3 LoRA 训练 $8-18/次（spot）；M1/M4 以 API 实测消耗为主，预算由 B4 熔断自己管。

## 7. 待拍板决策点

- **D1 载体**：新起独立中立二进制（推荐，立场干净）vs 在 atlas 内做多 provider（快但品牌立场冲突）。
- **D2 技能发布账号**：skills.sh 用哪个 GitHub 账号/组织发布（个人 majiayu000 vs 新组织）。
- **D3 首批两家厂商**：推荐 Seedance 2.0（契约最完整，2A 目标形态）+ Kling 国际 API（文档成熟、Unit 计价清晰）；备选 Wan（开源侧可全链路自控）。
- **D4 判片默认 VLM**：三选一（Gemini Flash / GLM-Flash / DeepSeek Flash），建议做成可插拔 + 内置比价。
