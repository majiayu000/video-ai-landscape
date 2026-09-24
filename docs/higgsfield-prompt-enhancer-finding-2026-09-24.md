# Higgsfield PromptEnhancer 调研：CLI 效果对服务端增强的依赖（2026-09-24）

> 方法：克隆 `higgsfield-ai/skills`（HEAD, 2026-09-24）全文 grep "enhance" + 逐文件核对调用链。
> 用户问题：hig 的 skill 在 CLI 过程中是否用到他们的 promptenhancer 服务？单纯用 CLI 是不是做不出效果？

## 结论速览

| 技能 | enhancer 形态 | 效果依赖服务端？ |
|---|---|---|
| product-photoshoot | **服务端** PromptEnhancer（10 模式摄影词汇+结构模板） | **是**——官方承认裸调 noticeably worse |
| marketplace-cards | **服务端**（backend prompt enhancement + hidden templates） | **是** |
| generate（含视频） | 无 | 否——prompt 由 agent 直写，裸调就是正常用法 |
| brandkit（logo） | **技能内契约**（client-side，"you apply this contract yourself"） | 否——白盒 prompt 工程 |
| video-explainer | 无（preset 从服务端拉取，prompt 自写） | 否 |

## 证据（原文引用）

1. `higgsfield-product-photoshoot/SKILL.md:27`：
   "The CLI calls a backend prompt enhancer that holds mode-specific photography vocabulary and structural templates, then submits to `gpt_image_2`"
2. 同文件 :213（Errors 禁止项）：
   "Calling `higgsfield generate create gpt_image_2 --prompt ...` directly ... **bypasses the prompt enhancer and produces noticeably worse output**."
3. `evals/scenarios.md:111,119`：绕过 enhancer 直接调 = 判 Fail（"bypassed the prompt enhancer"）
4. `higgsfield-generate/references/model-catalog.md:163`：
   "its prompt enhancer adds 10 mode-specific templates on top of GPT Image 2"
5. `README.md:57` / `INSTALL.md:9`：marketplace-cards = "backend prompt enhancement" + "hidden marketplace prompt templates"
6. `higgsfield-brandkit/references/logo-prompt-enhancer.md:3`：
   "**There is no server-side enhancer tool in this environment: you apply this contract yourself**, exactly once per Design Brain candidate"
7. 视频反例：`higgsfield-generate/SKILL.md:152` 裸调示例
   `higgsfield generate create seedance_2_5 --prompt "camera dollies in" --mode omni_reference --start-image ./first.png --duration 12 --resolution 1080p --wait`

## 解读

1. **"效果"的本质**：product-photoshoot 的效果 = 隐藏模板层 × 裸模型。CLI 只是传输层，模板不随 CLI 分发。他们的 evals 甚至把 agent 手写 prompt 路径判为失败——技能在强制流量走服务端增强。
2. **增强不是魔法**：mode 模板 = 摄影词汇表 + 结构化模板 + 变体编排（--count 时的 lighting/angle/palette 变化逻辑，SKILL.md:179）。全部是可写进 SKILL references 的确定性 prompt 工程——brandkit 已经自证可行（白盒契约版 enhancer）。
3. **锁服务端是商业策略**：逼用户留在 higgsfield 平台（CLI → 他们的 API → 他们的计费）。技术上无必要性。
4. **对 videokit 的启示（M1 路线）**：
   - 把"商品视频模式模板"（电商主图视频/白底展示/场景种草/规格对比等）写成 videokit 应用技能的 references —— 白盒、可审计、可版本化，效果层面对等
   - 我们的红线③（失败说实话）在这里有天然弹药：他们把"手写 prompt"判 Fail 是在掩盖效果差异的真实来源；我们把这层模板公开
   - 他们视频侧没有 enhancer ⇒ 视频效果竞争回到：模型选择质量（我们的决策树+价差数据）+ prompt 工程质量（M1 模板）——两条我们都能做

## 竞争框架更新

Higgsfield 三层资产拆解：①渠道/平台（CLI+API+计费）②服务端隐藏模板（product-photoshoot 等）③技能文档层（SKILL.md 决策树）。
此前拆解（anatomy 文档）只覆盖③；②是本次新发现——是比③更深的护城河，但可复制方法论、不可复制黑盒本身。我们取③全部公开+②白盒化，绕开①（不设平台，直连厂商 API）。
