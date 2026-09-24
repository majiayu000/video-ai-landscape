# Higgsfield Skill 完整解剖 · M0 施工图

> 拆解日期：2026-09-24 · 来源：`github.com/higgsfield-ai/skills` @ v0.12.0（156 个文件，逐文件核对）+ skills.sh 实时 API
> 用途：我们 M0 六技能矩阵的施工蓝图——**骨架照抄，内容换成我们的调研实证，四件事反着做**。

## 0. 为什么拆它

- skills.sh 上最大的厂商官方账号：9 个技能挂在架上，合计安装 **约 98 万**
- 头部三个：higgsfield-generate 178,706 · product-photoshoot 158,496 · soul-id 157,350
- 它是我们技能的**写法范本**，也是**差异化标尺**（哪里做得烂，哪里就是我们的位置）

## 1. 全景：两层结构

```
higgsfield-ai/skills/            ← 一个仓库 = 9 个技能 + 全套底座
├── .claude-plugin/plugin.json   ┐
├── .codex-plugin/plugin.json    ├ 三端插件市场清单
├── .cursor-plugin/plugin.json   ┘
├── VERSION                      ← 单一版本号源（当前 0.12.0）
├── scripts/update-check.sh      ← 用户侧升级检查
├── evals/scenarios.md           ← 评测题库
├── .github/workflows/validate-skills.yml  ← CI 校验
├── README / INSTALL / INSTALL_FOR_AGENTS / COOKBOOK / CONTRIBUTING / CLAUDE.md / LICENSE(MIT)
├── setup/                       ← 安装入口
│
├── higgsfield-generate/         ← 旗舰技能（178k 安装）
│   ├── SKILL.md                 ← 本体 325 行
│   └── references/ × 12         ← 按需加载文档
├── higgsfield-brandkit/         ← 22 refs + 3 scripts + agents/
├── higgsfield-websites/         ← 35 refs + 12 scripts（游戏技能已并入）
├── higgsfield-soul-id/          ← 2 refs
├── higgsfield-youtube-thumbnail/← 2 refs + agents/
├── higgsfield-video-explainer/  ← 1 ref
├── higgsfield-marketplace-cards/← 纯 SKILL.md
└── higgsfield-product-photoshoot/← 纯 SKILL.md
```

注：skills.sh 上还挂着 higgsfield-game-generation（26,706 安装），实际 8 月 7 日已并入 websites，平台索引未清——**技能发出去之后平台索引有滞后**，我们自己发的时候要留意。

## 2. 仓库底座 · 7 个部件

| # | 部件 | 作用 | 细节 |
|---|---|---|---|
| 1 | 三端 plugin.json | 一个仓库同时进 Claude Code / Codex / Cursor 三个插件市场 | name/version/keywords 对齐 |
| 2 | VERSION 文件 | 全仓库单版本号 "0.12.0" | 弱点见 §4-2 |
| 3 | update-check.sh | 用户本地 `~/.higgsfield-skills/` 存状态，对比远程 VERSION，输出 JUST_UPGRADED / UPGRADE_AVAILABLE / 静默三态 | opt-in、可 snooze、环境变量可测试 |
| 4 | evals/scenarios.md | 人工可跑的评测题库（见下） | 每题带 Pass/Partial/Fail 标准 |
| 5 | CI validate-skills.yml | PR 触发：frontmatter 合法性、版本号同步、references 文件存在性 | PyYAML 实现 |
| 6 | 根文档套件 | README / INSTALL / INSTALL_FOR_AGENTS（专给 agent 看）/ COOKBOOK / CONTRIBUTING | |
| 7 | LICENSE（MIT）+ setup/ | 别人能合法抄、一键装 | |

### evals 题库长什么样（真实示例）

> **用户**："随手来张雪地狐狸的写实图"
> **预期行为**：选 nano_banana_2 级别；**不选** Soul（没提脸）；**不选**贵的 GPT Image（"随手"= 别用力过猛）；用 `--wait` 一步到位；干完前闭嘴；交一个 URL + 一句总结
> **打分**：Pass = 模型选对、单 URL、零废话 / Partial = 模型对但话痨 / Fail = 模型错、重复提交、URL 坏

题库定位：给人工或另一个 agent 在全新会话里跑，验收的是**技能写出来后 agent 的行为**，不是代码单元测试。

## 3. 单技能解剖（以旗舰 generate 为例）

### 3.1 SKILL.md 八段固定结构

| 段 | 内容 | 我们抄不抄 |
|---|---|---|
| ① YAML frontmatter | 见 3.2 | ✅ |
| ② Step 0 Bootstrap | CLI 不在 PATH → curl 一键装；未登录 → 引导 `auth login` 并等待确认 | ✅（换成我们的 CLI） |
| ③ UX Rules | 说人话五条：不吐 JSON、不念内部黑话（"正在轮询"）、跟用户语言、别批量问、**不预估成本**（← 反面教材，见 §4-1） | ✅ 但第 5 条反着写 |
| ④ Discovery guardrail | 语义搜索搜不到 ≠ 不存在，先跑全量模型列表再下结论 | ✅ |
| ⑤ Workflow | 一整棵**选型决策树**：什么需求 → 哪个模型，细到"别因为旧模型参数枚举好读就降级" | ✅（填我们的 5 家厂商数据） |
| ⑥ Media flags 表 | --image / --start-image / --end-image / --video / --audio 每个哪些模型接受，矩阵表 + 备注参考数组模型的显式参数 | ✅（对应 capabilities.json 首尾帧/参考轨字段） |
| ⑦ Common params | 9 条可直接复制的完整命令，含 `--json` 机器可读模式、stdin 管道 | ✅ |
| ⑧ Errors | 每种报错 → 处置动作（缺参数→去问；枚举错→列出合法值；Session expired→去登录） | ✅ + 补超时语义 |

### 3.2 frontmatter 关键字段（description 是主战场）

```yaml
version: 0.12.0
name: higgsfield-generate
description: |
  一句话能力 + 默认模型；
  Use when: <20+ 个用户触发词，覆盖中英文说法>;
  Chain with: higgsfield-soul-id（身份一致性）;
  NOT for: <6 个明确划走的场景，各自指向对应技能>
argument-hint: "[prompt] [--model <name>] [--image|--video <path>]"
allowed-tools: Bash
```

要点：**agent 靠 description 决定装不装、用不用**——三段式（Use when / Chain with / NOT for）就是技能间的流量分配协议；`allowed-tools: Bash` 说明技能本体只是"指挥 agent 跑 CLI 的说明书"，执行全在 CLI。

### 3.3 references 按需加载（省 token 的关键设计）

SKILL.md 压在 350 行内，细节全部外置，正文末尾放索引："Load on demand"。规模对照：

| 技能 | references | scripts |
|---|---|---|
| websites | 35 个（游戏/滚动叙事/SEO/安全…） | 12 个（glb 处理、骨骼、管线） |
| brandkit | 22 个 | 3 个（含 brandbook PDF 渲染） |
| generate | 12 个（模型目录/提示词工程/故障排查/marketing 7 件套） | — |
| soul-id | 2 | — |
| youtube-thumbnail | 2 | — |
| video-explainer | 1 | — |
| marketplace-cards / product-photoshoot | 0 | — |

规律：**纯说明书技能可以零依赖；活儿越重，references/scripts 越多**。

### 3.4 agents/openai.yaml

OpenAI 端界面文案：display_name / short_description / default_prompt（带 `$技能名` 引用）。只在需要自定义界面文案的技能里有。

## 4. 三个关键发现（差异化的证据）

1. **"不预估成本"是写进规则的**。UX Rules 第 5 条原文：*"Don't pre-estimate cost or optimize for cheaper models unless the user asks."* —— 用户骂"钱用得比想象快"、官方 9 月连发两篇文道歉，根源就在这条规则。**我们第 1 条规则反着写：动手前先报价。**
2. **版本化是仓库级，不是技能级**。全仓库一个 VERSION 0.12.0，改模型默认值直接 commit main（9-11 实测无版本号变更）——用户装着的副本无法知道技能内容变过。**我们做技能级版本号 + 变更日志。**
3. **失败语义不完整**。有 Errors 段（报错→处置，值得抄），但超时、部分成功、任务卡死的语义没定义（对比：PixVerse 范本明确"超时≠失败、非零退出可带部分成功"）。**我们补齐状态机语义。**

## 5. M0 施工清单（照此执行）

**照抄骨架**：① frontmatter 三段式 description ② 八段 SKILL.md 结构 ③ references 按需加载、本体 ≤350 行 ④ evals 题库（每技能 ≥3 题）⑤ VERSION + update-check ⑥ CI 校验 ⑦ 三端 plugin.json ⑧ MIT LICENSE

**反着做的四件事**：① 价格先报（第一条规则）② 技能级版本号 ③ 失败说实话（超时≠失败）④ 跨厂商不锁平台（有哪家的 key 用哪家）

**内容来源**：选型决策树填 `data/capabilities.json`（能力矩阵 13 条）；价格表填 `data/prices.json`（34 条，同模型跨渠道价差 67%-82%+）；失败语义填五家厂商调研的报错实录。

## 6. 来源清单

- 仓库树：`api.github.com/repos/higgsfield-ai/skills/git/trees/main?recursive=1`（156 文件）
- SKILL.md / plugin.json / VERSION / evals / update-check.sh / CI：raw.githubusercontent.com @ main（2026-09-24 取）
- 安装量：`skills.sh/api/search?q=higgsfield`（2026-09-24 实时）
- 佐证历史：`docs/research-vendor-next-moves-2026-09-22.md`（Higgsfield+Runway 路）
