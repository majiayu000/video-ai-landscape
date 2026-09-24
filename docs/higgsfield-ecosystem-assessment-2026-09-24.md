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
