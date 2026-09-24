# Higgsfield 生态与效果评估

> 评估日期：2026-09-24 · 数据：GitHub API / skills.sh API 一手拉取（当日）+ 本库三轮调研（103 SKILL.md 考古、厂商动向路）
> 口径：商业数字（融资/收入）未进调研库一手确认的，一律不给数。外部新闻佐证待补（当日搜索额度已满）。

## 1. 生态：分发很广，但是"官方独角戏"

### 1.1 分发面（强，一手数据）

| 渠道 | 数据 | 置信 |
|---|---|---|
| skills.sh | 9 个官方技能 ≈ 98 万安装，平台最大厂商账号；头部 generate 178,706 / product-photoshoot 158,496 / soul-id 157,350 | 官方 API 实时 |
| GitHub skills 仓库 | 1,117 ★ / 216 fork（2026-04-09 创建，5 个半月） | 官方 API |
| GitHub cli 仓库 | 579 ★；**8 月零提交**，进维护态（9-18 恢复 push，伴随 API 首发） | 官方 API |
| MCP 分发 | 免 API key 铺进 ChatGPT / GPT-6 Astra / Claude / Cursor 等 7+ 客户端 | 官方 changelog |
| 其他 | After Effects 插件（7-13）；Enterprise SOC 2 + SSO（8-19） | 官方 changelog |

### 1.2 生态空心三信号

1. **贡献者 5 人**：前两名 49+32 commits——内部团队仓库，不是社区生态。第三方仿写技能最好 395 安装 vs 官方 178,706，差 **450 倍**：没有第三方在它上面长出来。
2. **CLI 被自己放弃**：重心转向 ChatGPT 分发与无代码 App（Apps，7-07；GPT-6 Astra，9-07），开发者侧入口停在维护态。
3. **工程卫生一般**：版本号全仓库一个（VERSION 0.12.0）、改模型默认值直接 commit main（9-11 无版本号变更）、game-generation 并入 websites 后 skills.sh 索引未清。

**定性：广播型生态（官方→用户单向灌），不是平台型生态（第三方共建）。**

## 2. 效果：产品需求真，工程与账是软肋

### 2.1 被验证有效的

| 项 | 证据 |
|---|---|
| 锁脸/一致性招牌 | soul-id 157k 安装；Soul 系列（2.0/Cinema/Location/Cast）分工明确 |
| URL 导商品→广告链 | Marketing Studio 被复购的工作流形态；Click-to-Ad（URL 驱动） |
| UX 剧本路线 | websites/brandkit/explainer 被视为最完整的"应用工厂"技能族 |
| 工程自觉性中上 | evals/ 10 场景+评分 rubric+3 轮稳定制；CI 校验 frontmatter/版本同步/引用（103 SKILL.md 考古结论：头部水准） |

### 2.2 被验证翻车的

| 项 | 证据 |
|---|---|
| 计费黑箱（最大差评点） | 五套计费面并存（credits / All Unlimited / Bonus Seconds / MCP 专属 credits / console API）；官方 9-10、9-15 连发两篇文解释"钱为何用得快"；**根因已定位：UX 规则第 5 条 "Don't pre-estimate cost" 写进技能** |
| 无限套餐体验 | 忙时降速、共享并发、一次一任务（7-20 changelog 自述） |
| API 太新 + 工具停更 | API 9-16 首发即仅 8 天；计费口径仍在抖；CLI 维护态——新 API 配旧工具 |
| 版本不可追溯 | 技能级无版本，用户侧副本无从知道内容变过 |
| 质量验证缺位 | evals 测 agent 行为，无生成产物质量评测；无确定性验收 |

## 3. 对我们的战略含义

1. **需求与渠道双重验证**：锁脸、商品图、广告有人抢着用（98 万安装）；技能分发渠道有效。
2. **软肋即我们的差异化四件事**：价格先报 / 技能级版本号 / 失败说实话 / 跨厂商不锁平台——每一条都对应它的一个已实证差评。
3. **它正在腾位置**：主动离开开发者 CLI 阵地（转 ChatGPT/无代码），M0 六个开发者向技能正好补位。同台竞争时，它的差评就是我们的对比卖点。
4. **广播型生态的空位**：无第三方在长——谁能先把"第三方可共建"的结构（跨厂商、中立）立起来，谁拿走平台型生态。

## 4. 附：数据快照方法

- `api.github.com/repos/higgsfield-ai/{skills,cli}`（stars/forks/issues/pushed_at）
- `api.github.com/repos/higgsfield-ai/skills/contributors`（5 人）与 `/commits?since=2026-06-24`（skills 59 / cli 21）
- `skills.sh/api/search?q=higgsfield`（安装量实时）
- 本库 `docs/research-vendor-next-moves-2026-09-22.md`（时间线与分化判断）· `docs/research-deep-dive-2-2026-09-22.md`（evals/计费/版本化考古）
## 5. 横评快照 · skills.sh 全景与玩法拆解（2026-09-24 探索追加）

### 5.1 官方技能安装量对比（skills.sh API 实时）

| 厂商 | 官方技能最高安装 | 生态状态 |
|---|---|---|
| Higgsfield | 178,706（generate） | 9 技能 ≈ 98 万，视频类绝对第一 |
| Runway | 527（rw-generate-video） | 全系几百量级；开发者重心在 SDK/MCP，不在技能 |
| fal | 919（fal-image-edit，官方） | 官方存在感弱；第三方 nexu-io 系每个约 2.5k |
| PixVerse | 826 | 契约设计最强（考古结论），分发最小 |
| AtlasCloud | 649（atlas-cloud） | 工作库对应厂商，同量级 |
| ElevenLabs | 官方仅 96；第三方 prime-skills 361,275 | **第三方反超官方 3759 倍**——唯一反向案例 |
| Anthropic（基线） | canvas-design 110,396 | 标准制定者 |
| Google（基线） | agents-cli 家族每个 ≈ 329k | 大厂自灌安装 |

**结论 1**：视频类技能在 skills.sh = Higgsfield 一家独大，其他视频厂商全部没上心（几百 vs 十几万）。Runway/fal 的开发者注意力在 SDK 与 MCP——**"开发者向视频技能"这一层既没有第二梯队，也没有认真的竞争者**。
**结论 2**：ElevenLabs 案例证明技能分发上官方身份不是必需，触发词质量与实效才是——**个人账号发布（D2 选 majiayu000）不构成劣势**。

### 5.2 GitHub skills 仓库对照（2026-09-24）

| 仓库 | stars | 最后 push | 备注 |
|---|---|---|---|
| anthropics/skills | 177,863 | 09-22 | 官方标准 |
| higgsfield-ai/skills | 1,117 | 09-14 | 厂商中最大 |
| elevenlabs/skills | 459 | 09-16 | |
| fal-ai-community/skills | 246 | 05-13 | **停更 4 个月** |
| runwayml/skills | 69 | 08-28 | |
| PixVerseAI/skills | 61 | 09-10 | 契约最强，社区最小 |

### 5.3 HN 热度：接近零

近 90 天 higgsfield 相关 story 最高 5 pts，无一条进入主流视野（唯一相关提问："Why Suddenly higgsfield made its core repo Opensource?"，1 pt，9-17）。它的营销主场在 TikTok/创作者侧，开发者社区声量 ≈ 0。
**含义**：98 万安装里几乎不含"HN 型开发者"——其用户画像与我们的电商素材/短剧工坊管道用户重叠度，高于与硅谷开发者重叠度。技能渠道触达的正是我们要的人。

### 5.4 COOKBOOK 拆解：它的玩法是"跨技能剧本"

Recipe 统一格式 = What it does / Why powerful / **What you say**（用户原话）/ What the agent does（bash 链）。旗舰配方：创始人一张头像 → soul-id 训练 → product-photoshoot 出 5 个场景 → generate（kling3_0）把最好的 2 条动画化——一次会话产出整套品牌内容，自述对标"创意公司第一个 sprint"。

两个发现：

1. **它本质是"带 UX 的聚合层"**：generate 底层跑的是 Kling / Seedance / Veo / Grok / Gemini 等别人家的模型——技能只是它聚合生意的前端皮肤。这解释了为什么它不做契约层（每接一家新模型只需换皮）；也再次确认我们的位置（契约、验收、角色资产）它结构性做不了。
2. **INSTALL_FOR_AGENTS.md 是成熟样例**：开篇即 "You are an AI coding agent. Follow this exactly."，CLI 安装→OAuth 验证→按平台路径装技能（Claude/Cursor/Codex 各一行）全流程写给 agent 执行。我们 M0 的 INSTALL 照此写。

### 5.5 本轮探索待办

- [ ] Higgsfield API（9-16 首发）定价页与计费口径实测——待外部搜索额度恢复
- [ ] prime-skills/elevenlabs-music-generation（361k）拆解：第三方如何打赢官方——可反哺我们的触发词写法
- [ ] nexu-io fal 系技能（2.5k 级）拆解：小团队技能的安装量天花板样本
