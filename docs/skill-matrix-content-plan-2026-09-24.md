# M0 技能矩阵 · 内容料单与施工清单

> 制定：2026-09-24 · 依据：Higgsfield 技能解剖（施工模板）+ 本库调研数据（素材来源）
> 用途：M0 六技能要写的每一个内容件、素材从哪来、完成状态。**本文就是施工跟踪表**，写完一项勾一项。
> 依赖说明：以下所有写作工作不依赖 D1/D2 拍板；仅"发布"一步需要 D2（发布账号）。

## 1. 通用骨架（每个技能都有，照解剖图八段）

| # | 内容件 | 说明 | 素材来源 | 状态 |
|---|---|---|---|---|
| 1.1 | frontmatter 三段式 | Use when 触发词 + Chain with + NOT for 边界 | 各家调研笔记 | ☐ |
| 1.2 | Step 0 | 没 key 引导（去哪注册、env 变量名）、CLI 依赖检查 | 各家官方文档 | ☐ |
| 1.3 | 选型决策树 | 该厂商内部：什么需求选哪个模型/档位 | data/capabilities.json | ☐ |
| 1.4 | 价格表（内置） | 每模型单价，写死在技能里 | data/prices.json（34 条） | ☐ |
| 1.5 | 参数矩阵 | 时长/分辨率/首尾帧/参考输入 × 模型接受表 | data/capabilities.json | ☐ |
| 1.6 | 命令示例 | 3-5 条可直抄的完整调用（含 --json） | 调研笔记 | ☐ |
| 1.7 | Errors 表 | 每种报错 → 处置动作 | 调研抓到的报错实录 | ☐ |
| 1.8 | references/troubleshooting.md | 深度排障（按需加载） | 同上 | ☐ |

## 2. 各技能独有内容（差异化的部分）

| 技能 | 独有内容（我们独有的信息增量） | 素材来源 | 状态 |
|---|---|---|---|
| **veo** | 产物 URL **24h 过期必须立即下载**（新手第一坑）；3.1 Lite 批量档位；时长/分辨率枚举 | 厂商调研 + capabilities | ☐ |
| **kling** | Unit 计价对照；3.0 vs 3.0 Turbo 差价；首尾帧用法；**并发上限 3 硬约束**（排队写法） | 厂商调研 | ☐ |
| **seedance** | 2.5 vs 2.0（4K）选择；t2v / omni_reference / video_edit / video_extension 四模式；**任务 ID 保留 7 天 + return_last_frame 串联**（契约范本） | 2A 目标契约 + 厂商调研 | ☐ |
| **wan** | **零 API 费路线**：自托管配方（24GB 显存、musubi-tuner）；spot 4090 $0.34/hr 算账；LoRA 训练 $8-18；Apache-2.0 商用说明 | recipes 路 + 判片路 | ☐ |
| **cogvideo** | **4K/60fps/首尾帧能力洼地**（无人知晓）；国际接入方法；价格洼地对照 | 厂商调研 | ☐ |
| **router** | 跨厂商决策表（任务×预算×质量→选哪家）；**同模型跨渠道价差 67-82%+ 对照表**（王牌数据）；六技能 Chain 关系 | prices.json + useapi 比价调研 | ☐ |

## 3. 仓库底座（一次做好，全部技能复用）

| # | 内容件 | 说明 | 照抄对象 | 状态 |
|---|---|---|---|---|
| 3.1 | README | 一句话说清 + 安装 + 技能列表 | higgsfield README | ☐ |
| 3.2 | COOKBOOK.md | 3-5 个跨技能剧本；四段式（What it does / Why / What you say / What agent does） | higgsfield COOKBOOK | ☐ |
| 3.3 | INSTALL.md + INSTALL_FOR_AGENTS.md | 后者开篇写给 agent："You are an AI coding agent..." | higgsfield 同名件 | ☐ |
| 3.4 | evals/scenarios.md | 每技能 ≥3 道行为题，带 Pass/Partial/Fail 标准 | higgsfield evals | ☐ |
| 3.5 | VERSION + update-check.sh | 版本源 + 用户侧升级检查（三态输出） | higgsfield scripts | ☐ |
| 3.6 | CI validate-skills.yml | frontmatter/版本同步/references 存在性 | higgsfield CI | ☐ |
| 3.7 | 三端 plugin.json | .claude-plugin / .codex-plugin / .cursor-plugin | higgsfield 同名件 | ☐ |
| 3.8 | MIT LICENSE | 允许被抄 | — | ☐ |

## 4. 差异化红线（每个技能必须体现，写完对照检查）

1. **价格先报**——动手前先报价（Higgsfield UX 规则第 5 条反着写）
2. **技能级版本号**——每个 SKILL.md 带 version，变更可追溯
3. **失败说实话**——超时≠失败、部分成功要报告（PixVerse 语义）
4. **跨厂商不锁平台**——有哪家的 key 用哪家；router 技能明示替代选项

## 5. 总量与依赖

- **约 30 个文件**：6×SKILL.md（各 200-350 行）+ ~15 references + 底座 8-9 件
- 全部素材已在调研库，工作是"提炼改写为 agent 可执行指令"，非新研究
- 成本 $0 · 写作 1-2 天（agent 工作流）· 发布动作待 D2

## 6. 完成定义（M0 验收）

- [ ] skills.sh 可搜到、可安装（待 D2 账号）
- [ ] `npx skills add <name>` 换机复装成功
- [ ] evals 题在全新会话跑，Pass 率 ≥ 80%
- [ ] 差异化红线 4 项逐技能过检
