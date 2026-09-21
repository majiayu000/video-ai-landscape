# 扩展调研 · 视频全厂商 + 大模型 + 训练设施（2026-09-22）

> 方法：6 路 schema 约束 agent 真实网络调研（视频应用层路因限流待补跑）。
> 规则：以 2026-09-22 为"现在"，只看近 90 天动作 + 未来信号；gaps 为核心产出。
> 原始结构化输出：workflow run wf_354c2d89-361。

---


## 中国模型系视频（火山/阿里/腾讯/智谱/PixVerse）

90 天窗口内（2026-06-22 至 2026-09-22），中国视频生成厂商的 Agent 接入面呈现"一家独走、四家缺位"格局：火山/阿里/腾讯/智谱四大厂均无官方视频生成 MCP 或 Agent Skill（mcp.so 上即梦/CogVideo/DashScope/混元相关条目全为第三方，部分甚至用逆向接口），唯一例外是 PixVerse（爱诗科技）——它同时维护官方 CLI（MIT，npm 1.4.5，2026-09-20 仍更新）、官方 MCP 和官方 SKILL.md（v1.28.0，含 execution-contract/prompt-contract、11 个工作流、离线 capabilities 查询），直接验证了"契约优先 CLI + Agent Skill"路线可行且已有人占位。闭源侧模型快速迭代：阿里百炼已到 wan2.7-t2v（快照 2026-06-12，强制异步、task_id 24 小时有效）并出现 wan3.0-video 与 happyhorse-1.1 全家桶；火山 Seedance 2.0 支持音画同生、多模态参考（9 图+3 视频+3 音频）、视频延长/编辑、draft 样片模式与 flex 半价离线队列；腾讯混元正迁往 TokenHub（OpenAI 兼容协议 + submit/query 异步对），且混元生视频 API 直接代销 Vidu 与 Kling 全系列；智谱视频线 90 天内零更新（cogvideox-3 停在 2025-07），转而主推 Managed Agents 的 Skill/MCP 托管基建。最大空位：官方异步任务契约五家五套、有效期 24h-7 天不等、计费单价普遍不在 API 文档里，且无人提供统一的等待/恢复/产物持久化/能力矩阵层；开源侧只剩 Wan2.2（Apache-2.0）仍在活跃维护，CogVideo 已停更 10 个月。

### 近 90 天时间线

- **2026-09-21** — 阿里 Wan-Video/Wan2.2 开源仓库仍有推送（17,580 stars，Apache-2.0），开源线持续维护（https://api.github.com/repos/Wan-Video/Wan2.2）
- **2026-09-20** — PixVerse 官方 CLI（PixVerseAI/cli，MIT）更新推送，npm 多包名同步发布 1.4.5；README 明确面向 Claude Code/Cursor/Codex/LangChain 等 Agent，并支持 --model seedance-2.5（4-30 秒整数时长）（https://github.com/PixVerseAI/cli）
- **2026-09-18** — 火山引擎 volcengine/mcp-server 仓库更新（327 stars、362 commits），但其 100+ MCP server 中没有任何视频生成 server（https://github.com/volcengine/mcp-server）
- **2026-09-22** — 阿里云百炼 wan2.7 文生视频 API 文档当日更新：wan2.7-t2v（快照 2026-06-12）确认强制 X-DashScope-Async 异步两步协议、按秒计费、task_id 与视频 URL 有效期 24 小时；模型列表页另出现 wan3.0-video、happyhorse-1.1 系、happyoyster-1.0-acting（邀测）（https://help.aliyun.com/zh/model-studio/text-to-video-api-reference）
- **2026-09-10** — PixVerse 官方 Agent Skill 仓库（PixVerseAI/skills，含 SKILL.md，当前版本 1.28.0）更新推送——90 天窗口内唯一在维护的官方视频生成 Agent Skill（https://github.com/PixVerseAI/skills）
- **2026-08-26** — 智谱发布 GLM-5.3-Flash（原生多模态、混合注意力）；90 天内智谱无任何视频生成模型更新（cogvideox-3 停在 2025-07-15）（https://docs.bigmodel.cn/cn/update/new-releases）
- **2026-08-19** — 智谱发布 GLM-5.3 旗舰模型（编程/安全方向）；同期其 Managed Agents 平台提供完整 Skill/MCP API（创建/版本/部署），但未接入视频生成（https://docs.bigmodel.cn/cn/update/new-releases）
- **2026-09-22 前后（窗口内核实）** — 腾讯云混元生视频 API 全景确认：SubmitHunyuanToVideoJob/DescribeHunyuanToVideoJob 之外，平台直接代销 Vidu（文生/图生/参考生视频）与 Kling（文生/图生/动作控制/视频编辑/视频延长）接口；购买指南载明混元大模型能力将逐步迁至 TokenHub、原平台停止新增模型能力（https://cloud.tencent.com/document/api/1616/107795）

### Roadmap 信号

- **腾讯混元模型能力将逐步迁至 TokenHub，原平台停止新增模型能力（多源交叉：购买指南迁移公告 + TokenHub 独立产品文档含视频生成调用/模型价格/Claude Code 接入指南 + 新模型命名 yt-video-2.0）**（置信：多源交叉；https://cloud.tencent.com/document/product/1616/79753）
- **Seedance 2.5 疑似已发布或灰度：PixVerse 官方 CLI 已支持 --model seedance-2.5（4-30 秒），第三方 mcp.so 条目约 4 个月前亦提及 Seedance 2.5，但火山官方页面未见 2.5 字样**（置信：多源交叉；https://github.com/PixVerseAI/cli）
- **阿里闭源线持续加代：百炼模型列表已出现 wan3.0-video、happyhorse-1.1 系（t2v/i2v/r2v/video-edit）、happyoyster-1.0-acting（邀测），wan2.5/2.6 已从列表消失（版本快速迭代、旧版下线）**（置信：官方明示；https://help.aliyun.com/zh/model-studio/models）
- **PixVerse 持续加码 Agent 生态：skills 仓库窗口内更新至 v1.28.0，CLI README 直接点名 Claude Code/Cursor/Codex/LangChain/custom agents 为目标用户，并用 npx skills add 分发——把 AI Agent 当一等分发渠道**（置信：官方明示；https://github.com/PixVerseAI/skills）
- **智谱 Managed Agents 平台提供全套 Skill/MCP/部署/凭据 API，为'模型能力 Agent 化托管'铺路，视频生成尚未接入但基建已就绪**（置信：官方明示；https://docs.bigmodel.cn/cn/managed-agents/skills）
- **火山 Seedance 2.0 明示走'音视频联合 + 多模态参考一致性 + 生成/编辑/延长三模式'路线，generate_audio 默认开启、多参考输入上限高（9 图 + 3 视频 + 3 音频）**（置信：官方明示；https://www.volcengine.com/docs/82379/1520757）
- **开源线让位闭源 API 的行业趋势：zai-org/CogVideo 停更约 10 个月（2025-11-04）、Tencent-Hunyuan/HunyuanVideo-1.5 停更约 5 个月（2026-04-10），仅 Wan-Video/Wan2.2 仍活跃——开源只剩阿里一家在坚持**（置信：推断；https://api.github.com/repos/zai-org/CogVideo）
- **腾讯/智谱/PixVerse 三方都在做'他家模型代销'（腾讯代销 Vidu+Kling、智谱代销 Vidu 系、PixVerse 代销 Seedance 2.5/MiniMax/ElevenLabs/Google Lyria 3 Pro）——平台聚合分发成为中国市场显性路线**（置信：官方明示；https://cloud.tencent.com/document/api/1616/107795）

### 做得好的

- PixVerse（爱诗科技）的 Agent 三件套是全球级范本：官方 CLI（MIT）+ 官方 MCP + 官方 SKILL.md，且 SKILL 内置 execution-contract.md / prompt-contract.md、17 个 capabilities 能力文件、11 个工作流（含 storyboard-to-video 四镜头分镜、batch-creation）；pixverse capabilities --json 提供离线机器可读能力查询，--no-wait + 保留任务 ID + "超时不等于失败/非零退出可带部分成功结果" 的恢复语义，与契约优先 CLI 的设计完全同构
- 火山 Seedance 2.0 任务契约设计最完整：异步任务 + callback_url 回调、execution_expires_after 可配（默认 48h，1h~3 天）、任务 ID 保留 7 天、priority 0-9 队列、service_tier flex 离线半价、draft 样片低成本试错模式、return_last_frame 末帧返回以串联多镜头、generate_audio 默认开启（音视频联合生成）、0-9 图 + 0-3 视频 + 0-3 音频多模态参考、支持生成/编辑/延长三种模式
- 阿里的开源/闭源双轨与文档透明度：Wan2.2 以 Apache-2.0 持续维护且 ComfyUI 官方集成；wan2.7 API 文档把异步协议、按秒计费、时长 2-15s 整数、双地域端点、查询 RPS 20、24h 有效期写得最直白，并建议异步回调
- 腾讯的聚合接口设计：混元生视频 API 平台直接代销 Vidu 与 Kling 全系列（含动作控制、视频编辑、视频延长），配合 AigcElement 主体管理接口实现跨模型主体一致性；TokenHub 改用 OpenAI Chat Completions 兼容协议 + 小写下划线参数，显著降低接入成本
- 智谱的 Agent 基建 API 化程度最高：Managed Agents 把 Agent/Skill/版本/部署/记忆/Vault 凭据库全部做成一等 REST API；视频接口用 image_url 数组一张接口同时支持图生视频与首尾帧（第二张图即尾帧）
- 各家对限流与错误码的文档较透明：腾讯每个接口标注 QPS（20-30 次/秒，按 API+地域+子账号维度），DashScope 标注查询 RPS 20 并给出 429 处理建议

### 空位与切入姿势

- **官方视频生成 MCP / Agent Skill 几乎全军缺位（PixVerse 是唯一例外）**
  - 证据：volcengine/mcp-server 100+ 个 server 无一视频生成；mcp.so 上即梦相关 3 个全是第三方（其一明示用逆向接口）、cogvideo 搜索 0 结果、dashscope/hunyuan 均无官方条目；智谱有 Skill 基建但文档明示模板不接受 Skill/MCP 接入视频
  - 切入：为 DashScope/Ark/TokenHub/bigmodel 四家做'官方没有的第一方体验'：契约优先 CLI + 官方级 SKILL.md + MCP 包装，把异步任务、重试、产物落盘封装成 Agent 可直接调用的工具——这正是读者项目的定位，且 PixVerse 已验证该模式能被厂商官方采纳
- **异步任务契约碎片化且有效期短：五家五种协议**
  - 证据：DashScope：POST/GET + X-DashScope-Async 头，task_id 与视频 URL 仅 24h 有效；Ark：/contents/generations/tasks，execution_expires_after 默认 48h、任务 ID 保留 7 天；TokenHub：/v1/api/video/submit + /query，status queued→completed；BigModel：/paas/v4/videos/generations 轮询；腾讯：SubmitXxxJob/DescribeXxxJob 成对接口，各家状态机、参数命名、轮询频率限制互不兼容
  - 切入：统一任务层：本地 task store + 断线 resume + 到期前自动把产物迁移到用户自有存储（S3/R2/本地），把'24 小时后 URL 失效'变成不会发生的痛点；一份 capabilities.json 描述五家差异
- **计费透明度差：闭源侧几乎查不到提交前单价**
  - 证据：百炼模型列表页无任何单价（wan2.7 仅知按秒计费，wan3.0-video 无价格）；智谱视频 API 文档零计费信息；TokenHub 视频生成页无单价；腾讯购买指南只覆盖风格化/跳舞/唱演，不含文生/图生视频单价
  - 切入：CLI 内置成本估算器：提交前按 分辨率×时长×模型单价表 展示预估费用与余额检查（火山 Seedance 2.0 开通还要求账户余额≥200 元，这类门槛最该在提交前提示）
- **长任务等待/恢复体验未被厂商产品化**
  - 证据：官方文档只建议'轮询或配回调'，无 CLI 友好方案；DashScope 任务耗时 1-5 分钟、 Ark 最长 3 天；只有 PixVerse 做了 --no-wait/超时语义但仅覆盖自家订阅体系（CLI 需订阅、走 credits，不适合纯 API 开发者）
  - 切入：跨厂商的 wait/resume/断点恢复 + 部分成功保留语义（非零退出可带已完成产物），配 --json 机器可读输出——把 PixVerse 的单厂商契约升级为五厂商统一契约
- **能力矩阵无跨厂商机器可读标准**
  - 证据：首尾帧（智谱 image_url 双图、腾讯 Kling 系、PixVerse transition）、视频延长（Ark 官方支持、腾讯 Kling 接口、PixVerse create extend）、参考生视频（Seedance 2.0 多模态、Vidu reference、腾讯/智谱代销版）、音频联合（Seedance generate_audio）——能力各家都有但名称/参数/限制完全不同，且 PixVerse 的 capabilities --json 只描述自己
  - 切入：定义开源的 video-capabilities 规范（模型×能力×参数域×区域限制×单价×有效期），做五厂商的适配器矩阵——聚合之上的聚合，读者 CLI 的护城河所在
- **智谱视频线 90 天停滞，与 Agent 基建投入严重不对称**
  - 证据：更新日志窗口内全是 LLM（GLM-5.3 2026-08-19、GLM-5.3-Flash 2026-08-26）；cogvideox-3 停在 2025-07-15，但其 4K/60fps/首尾帧/10s 时长在国产闭源 API 中仍是差异化参数；CogVideo 开源仓库停更 10 个月
  - 切入：cogvideox-3 是'能力强但无 Agent 接入'的洼地：接入成本最低（OpenAI 风格 REST + 单接口首尾帧），适合作为多厂商 CLI 的第一批适配目标之一
- **开源/云端混合路由无人做**
  - 证据：Wan2.2（Apache-2.0，17.6k stars，ComfyUI 官方集成，TI2V-5B 可跑 RTX 4090）仍在活跃维护，而百炼闭源 wan2.7/wan3.0 按秒收费；CogVideo/混元开源线停更后本地路线只剩 Wan
  - 切入：CLI 支持 --provider local-comfyui 与云端同构调用：草稿用本地 Wan2.2 5B、成片用云端 wan2.7/Seedance，同一契约下按成本/质量路由
- **中文区域限制散落且文档化不足**
  - 证据：PixVerse SKILL 明示 CN 区不支持独立 voice/music、模型可用性有差异（需 PIXVERSE_REGION）；百炼 cn-beijing 与 ap-southeast-1 双端点行为差异需自行阅读；火山实人信息限制（真人面部输入受限）藏在参数说明里
  - 切入：区域感知的能力矩阵与运行时检查（region×model×capability 三维），避免 Agent 在 CN 区提交注定失败的任务

### 未解问题

- Seedance 2.5 是否已官方 GA：火山官方文档只写到 2.0 系（2-0-260128、1.5 pro、1.0 pro），2.5 目前仅见于 PixVerse CLI 参数与第三方 MCP 描述，火山产品动态页因 JS 渲染无法抓取核实
- 腾讯混元生视频文生/图生视频的具体单价：'计费概述（混元生视频）'页未抓到正文；yt-video-2.0 与混元视频版本的对应关系、TokenHub 视频任务的产物 URL 保留期均未披露
- wan3.0-video 的 GA 状态、价格及与 wan2.7 的分工；happyhorse（快马？）/happyoyster 的定位与发布日期；wan2.5/2.6 是否已从百炼下线
- Tencent-Hunyuan/HunyuanVideo 原始仓库的 GitHub API 返回缺失，仅核实了 HunyuanVideo-1.5 仓库（2026-04-10 后无推送）；是否有 HunyuanVideo 2.x 未确认
- 即梦（Dreamina）消费端的 Agent 化进展无第一手资料（仅第三方逆向接口 MCP 存在）；火山方舟是否会在 Coze/Trae 生态内做视频生成 Skill 亦无公开信息
- 智谱视频生成 API 是否计划接入其 Managed Agents Skill 体系（当前文档明示 Inline template 不接受 MCP/Tools/Skills override）

### 来源

- [PixVerse 官方 CLI（GitHub）](https://github.com/PixVerseAI/cli)
- [PixVerse 官方 Agent Skill 仓库（含 SKILL.md v1.28.0）](https://github.com/PixVerseAI/skills)
- [PixVerse CLI README（Agent 集成与命令面）](https://raw.githubusercontent.com/PixVerseAI/cli/main/README.md)
- [PixVerse SKILL.md 原文（execution/prompt contract、11 工作流）](https://raw.githubusercontent.com/PixVerseAI/skills/main/skills/SKILL.md)
- [PixVerse 官方 MCP server](https://github.com/PixVerseAI/PixVerse-MCP)
- [火山方舟 Seedance 2.0 API 参考（异步任务/回调/样片/flex）](https://www.volcengine.com/docs/82379/1520757)
- [volcengine/mcp-server（无视频生成 server）](https://github.com/volcengine/mcp-server)
- [阿里云百炼 万相2.7 文生视频 API 参考](https://help.aliyun.com/zh/model-studio/text-to-video-api-reference)
- [阿里云百炼 模型列表（wan3.0-video / happyhorse / happyoyster）](https://help.aliyun.com/zh/model-studio/models)
- [Wan-Video/Wan2.2 开源仓库（GitHub API 数据）](https://api.github.com/repos/Wan-Video/Wan2.2)
- [腾讯云混元生视频 API 概览（含 Vidu/Kling 代销接口）](https://cloud.tencent.com/document/api/1616/107795)
- [腾讯云混元生视频 购买指南（含 TokenHub 迁移公告）](https://cloud.tencent.com/document/product/1616/79753)
- [腾讯云 TokenHub 视频生成调用指南（yt-video-2.0，submit/query）](https://cloud.tencent.com/document/product/1823/130081)
- [腾讯云 TokenHub 产品文档](https://cloud.tencent.com/document/product/1823)
- [智谱 视频生成异步 API（cogvideox-3 / Vidu 系）](https://docs.bigmodel.cn/api-reference/%E6%A8%A1%E5%9E%8B-api/%E8%A7%86%E9%A2%91%E7%94%9F%E6%88%90%E5%BC%82%E6%AD%A5)
- [智谱 产品更新日志（GLM-5.3 等）](https://docs.bigmodel.cn/cn/update/new-releases)
- [智谱 Managed Agents Skills 文档](https://docs.bigmodel.cn/cn/managed-agents/skills)
- [Tencent-Hunyuan/HunyuanVideo-1.5（GitHub API 数据）](https://api.github.com/repos/Tencent-Hunyuan/HunyuanVideo-1.5)
- [zai-org/CogVideo（GitHub API 数据，停更）](https://api.github.com/repos/zai-org/CogVideo)
- [mcp.so 即梦搜索（全第三方）](https://mcp.so/search?q=jimeng)
- [mcp.so CogVideo 搜索（0 结果）](https://mcp.so/search?q=cogvideo)
- [mcp.so DashScope 搜索（无官方）](https://mcp.so/search?q=dashscope)
- [mcp.so Hunyuan 搜索（无官方视频 MCP）](https://mcp.so/search?q=hunyuan)
- [npm registry PixVerse CLI 包（1.4.5）](https://registry.npmjs.org/-/v1/search?text=pixverse)

---

## 西方与开源视频（LTX/Decart/Genmo/Stability/Moonvalley/ComfyUI）

西方/开源视频模型近 90 天呈双轨收敛:开源侧 Lightricks(LTX-2.5,162 万月下载,<$10M ARR 免费商用)+ ComfyUI 官方构成生态主场,云 API 侧 Decart(四语言 SDK、llms.txt、秒级透明定价)开发者体验最成熟;Genmo 的 Mochi 开源线已死(仓库一年无实质维护、无 release),Stability 视频线停滞转向音频与版权合作,Moonvalley 的 Marey(合规模型)API 仍 waitlist-only,Odyssey 转向世界模型。方向已被官方亲自验证:Comfy-Org 于 2026-07-01 创建 comfy-mcp(本地 40 工具)+ Comfy Cloud MCP + comfy-skills(Claude Code 插件),最大社区桥 artokun/comfyui-mcp 随即宣布弃档——"给本地 ComfyUI 做 MCP 桥"这个空位已关闭。真正的空位在桥之上的一层:除 MiniMax/Comfy 外所有西方厂商(Lightricks、Moonvalley、Decart、Stability、Odyssey)都没有官方 MCP/Skill/CLI;"成本即合约"(dry-run 报价 + 硬顶 + 降级建议)只有 168★ 的 vibeframe 在做;Marey 类"版权可控"能力没有出现在任何接口层的合约字段里。对 contract-first 多供应商 CLI,最优切入:云 API 与本地 ComfyUI 同一契约、license_tier/commercial_safe 与 max-cost 做成协议一等公民、补齐跨本地/云的异步任务等待与恢复。

### 近 90 天时间线

- **2026-07-01** — ComfyUI 官方组织创建 comfy-mcp:本地优先的 MCP server,约 40 个工具,基于 comfy-cli 构建,双许可(AGPL-3.0 或商业许可),2026-09-20 仍在活跃推送(234★)（https://api.github.com/repos/Comfy-Org/comfy-mcp）
- **2026-08~09(README 现状)** — Comfy 官方形成三件套:comfy-mcp(本地)+ Comfy Cloud MCP(远程 cloud.comfy.org/mcp)+ comfy-skills(Claude Code 插件,/comfy-cloud:generate-video);README 明确本地视频生成在消费级 GPU(8-24GB VRAM)上 slow or infeasible（https://github.com/Comfy-Org/comfy-mcp）
- **2026-09(公告,归档定于 2026-10-09)** — 最大社区桥 artokun/comfyui-mcp(759★)宣布不再维护,原因直指官方 Comfy Agent + Comfy MCP 上线——社区桥让位于官方的时代信号（https://github.com/artokun/comfyui-mcp）
- **2026-08-25** — Stability AI 完成 Series B(本轮 $76M,累计 $232M),投资方为 EA/索尼音乐/环球/华纳;官网近期新闻只有 Stable Audio 3.0,/stable-video 仍停留在 SVD——视频生成线实质停滞（https://stability.ai）
- **2026-09-15** — Odyssey 官宣基础世界模型 Odyssey-3,称 coming weeks 内公开发布;原 Explorer 产品已从官网下架,无 API(注:该页可核实性存疑,见 open_questions)（https://odyssey.systems/introducing-odyssey-3）
- **2026-08-26** — Lightricks 开源栈持续推进:LTX-2 官方 Python 推理/LoRA 训练包(9,491★,带 CLI)与 LTX-Desktop 开源桌面端(2,015★,Apache-2.0)同日推送;ComfyUI-LTXVideo(4,138★)2026-09-17 再推送（https://api.github.com/orgs/Lightricks/repos）
- **2026-09-11 前后(6-11 天前)** — LTX-2.5(22B DiT + Gemma 4 12B 编码器,音视频同步)IC-LoRA 家族密集更新:像素空间放大器 5.84k 下载、Ingredients、Day-To-Night 等;主模型月下载 162.7 万,diffusers 支持需装 GitHub main(未进正式版),ComfyUI 官方模板 day-1 跟进且 int8 量化仅 ComfyUI 可用（https://huggingface.co/Lightricks/LTX-2.5）
- **2026-08-05 前后** — 社区 uncensored 微调 Sulphur-2-base(基于 LTX-2.3,9B,t2v+i2v)上线,月下载 18.3 万、2.07k likes,数周内衍生出 20 个量化版 + adapter + merge——开放权重的衍生速度标杆（https://huggingface.co/SulphurAI/Sulphur-2-base）
- **2026-09(趋势页现状)** — HF text-to-video 趋势榜被 MiniMax-H3 衍生品霸榜:Turbo-LoRA 21.3 万月下载、ComfyUI 适配器(drbaph)20.1 万月下载且约 3 天前刚更新、alibaba-pai Acc-LoRA 9.6 万 + ControlNet-Union 1.57 万、FastH3 蒸馏与 GGUF 快速跟进——ComfyUI 集成速度明显快于 diffusers 正式打包（https://huggingface.co/models?pipeline_tag=text-to-video&sort=trending）
- **2026-09(文档现状)** — Decart 平台矩阵成型:Lucy 2.5(30FPS 实时)、Oasis 3、DOS;JS/Python/Swift/Android 四 SDK 均含 Realtime(WebRTC)/Process/Queue 三 API;Queue 仅轮询无 webhook;定价透明到秒(lucy-2.5 实时 $0.02/s、视频 $0.04/s、oasis-3-preview $0.02/s),但无成本预估工具、无 MCP(仅 Coding Agents 文档页)（https://docs.platform.decart.ai/getting-started/pricing）
- **2026-07-26** — vibeframe(多供应商生成媒体 CLI + MCP,Seedance/Runway/Veo/Kling,BYOK,'Your keys, your bill, your ceiling')最后一次推送:--dry-run 无 key 报价、--max-cost 硬顶(COST_CAP_EXCEEDED + retryWith 更便宜替代)、免费本地路径(Kokoro + 无头 Chrome + FFmpeg)（https://github.com/vericontext/vibeframe）
- **2026-09-08** — Generative-Media-Skills(4,316★,MIT)推送:真正的 SKILL.md 合集('recipes, not bash wrappers',支持 Claude Code/Cursor/Gemini CLI)+ muapi mcp serve(19 工具),但硬绑 muapi.ai 聚合器(utm 追踪 + Stripe 充值)（https://github.com/SamurAIGPT/Generative-Media-Skills）
- **2026-09(页面现状)** — Moonvalley Marey 公开 API 仍为 waitlist-only,无定价/文档/SDK/MCP;'FULLY LICENSED, Commercially safe' 主打不变;实际可用路径只有 ComfyUI Partner Nodes 与 fal.ai(均为 2025 年老集成)（https://moonvalley.com/api）

### Roadmap 信号

- **ComfyUI 本地/云双轨 MCP 将成为 agent 接入视频生成的默认方式,社区通用桥被官方取代**（置信：多源交叉(官方仓库 2026-07-01 创建 + 官方 skills 插件 + 最大社区桥 artokun/comfyui-mcp 因官方入场而宣布弃档)；https://github.com/Comfy-Org/comfy-mcp）
- **Odyssey-3 将在未来数周公开发布(基础世界模型,非视频 API)**（置信：官方明示(官网 'we're excited to release it publicly in the coming weeks';但该页可核实性存疑,见 open_questions)；https://odyssey.systems/introducing-odyssey-3）
- **Moonvalley Marey 公开 API 将开放(当前 waitlist 收单中),开放后主打企业合规视频生成**（置信：官方明示 waitlist 机制存在;开放时点未知；https://moonvalley.com/api）
- **Stability 重心已转音频/版权合作,视频生成(SVD 线)不再投入,自托管 licensing 仍是其企业路径**（置信：多源交叉(官网新闻只有 Stable Audio 3.0;新投资方为 EA/索尼/环球/华纳等内容巨头;/stable-video 无更新)；https://stability.ai）
- **LTX-2.5 的 diffusers 正式版打包在即;ComfyUI 将继续优先获得官方量化/模板支持**（置信：推断(模型卡明说 diffusers 需装 GitHub main;'int8 仅 ComfyUI'暗示与 ComfyUI 深度绑定)；https://huggingface.co/Lightricks/LTX-2.5）
- **LTX 开源生态将继续裂变:官方 IC-LoRA 家族持续更新,社区 uncensored 微调(Sulphur-2)与量化生态跟随每个新基座**（置信：多源交叉(官方 LoRA 6-11 天前更新 + Sulphur-2 月下载 18.3 万 + ComfyUI-LTXVideo 2026-09-17 推送)；https://huggingface.co/Lightricks）
- **Decart 从创意视频工具转向实时世界模型/具身场景(Oasis 3、Lucy 2.5 30FPS 实时、驾驶合作)**（置信：推断(产品命名与定价结构均指向实时/交互;融资叙事围绕 Oasis)；https://www.decart.ai）
- **MiniMax 系开源权重生态(H3 基座 + LoRA/ControlNet/量化)将持续主导 HF 开源视频下载量,且官方已发 MCP(与并行研究组交叉)**（置信：多源交叉(HF 趋势榜 + MiniMax-AI/MiniMax-MCP 官方仓库 2026-08-20)；https://huggingface.co/models?pipeline_tag=text-to-video&sort=trending）

### 做得好的

- Comfy-Org 把'agent 接入'当产品做:comfy-mcp(本地 40 工具)+ Comfy Cloud MCP(远程)+ comfy-skills(Claude Code 插件)三件套,且 comfy-cli 作为公共底座被官方 MCP 复用——官方下场定义了这一层的形态
- Lightricks 的开源-商业化双轨最完整:开放权重(月下载 162 万)+ ComfyUI 官方模板 day-1 + diffusers + 开源桌面端 LTX-Desktop + 官方 API(console.ltx.io)+ status 页 + 清晰 license($10M ARR 以下免费商用)+ 官方 LoRA 训练包,IC-LoRA 家族持续供给下游能力(放大/.ingredients/风格)
- Decart 的开发者体验标杆:JS/Python/Swift/Android 四语言 SDK、OpenAPI、llms.txt、Realtime/Process/Queue 三种 API 形态、定价透明到秒并给出可复算的成本示例——是'API 契约完整性'的参照系
- vibeframe 的成本即合约设计:--dry-run 无 key 也能报价、--max-cost 硬顶触发 COST_CAP_EXCEEDED 并附 retryWith 更便宜的替代模型、--skip-video 省钱路径、免费本地降级——这是多供应商 CLI 该有的费控形态
- Nomi 的'本地 ComfyUI 就是一个 provider'抽象:Electron GUI + 23 个 MCP 工具,导入 ComfyUI workflow 并对 /object_info 做依赖 diff 找缺节点/缺模型,内置 66 项各家 provider 认证配置但明确'不代理不转售推理'——本地/云统一的先例
- HF 社区的量化/蒸馏快反链条:新基座权重(LTX-2.3、MiniMax-H3)数周内出现 GGUF/FP8/蒸馏 LoRA/ComfyUI 适配器,长尾 GPU 被快速覆盖,ComfyUI 集成始终快于 diffusers 正式包

### 空位与切入姿势

- **除 MiniMax 与 Comfy 官方外,所有西方视频厂商都没有官方 MCP/Agent Skill/CLI:Lightricks(只有 API+桌面 GUI)、Moonvalley(连 API 都 waitlist)、Decart(只有 llms.txt 和 Coding Agents 文档页)、Stability、Odyssey 全部缺位**
  - 证据：GitHub org 全量扫描:Lightricks org 无 MCP/skill/API-tool 仓库;Decart docs 无 MCP 章节;moonvalley.com/api 仅 waitlist;对比 MiniMax-AI/MiniMax-MCP(1,585★)与 Comfy-Org/comfy-mcp 的官方入场
  - 切入：做 contract-first 的统一 CLI/MCP:同一套 submit/wait/cancel/dry-run 契约下同时路由云 API(LTX/Decart/fal 上的 Marey)与本地 ComfyUI;厂商不做桥,第三方统一层有真实需求(GitHub 'comfyui mcp' 329 结果、'video generation mcp' 376 结果全是零散社区桥)
- **'成本即合约'几乎无人做:只有 168★ 的 vibeframe 实现 dry-run 报价 + max-cost 硬顶 + retryWith 降级;LTX 有定价页但无预估器,Decart 定价透明但要求自己算秒数,Comfy 本地路径无成本概念(只看 VRAM)**
  - 证据：vibeframe README:'Estimated cost $10.93 exceeds --max-cost $3.00.' + COST_CAP_EXCEEDED 错误码 + retryWith 字段,'Your keys, your bill, your ceiling';docs.platform.decart.ai 只有单价与两个手算示例
  - 切入：把成本做成协议一等公民:--dry-run 全供应商报价(本地路径报显存/时长预估)、--max-cost 硬顶、机器可读的 COST_CAP_EXCEEDED + 更便宜替代(降分辨率/换模型/转本地),这对 agent 自动化调用是刚需——agent 不该在不知道价格的情况下扣用户的卡
- **跨本地/云的异步任务体验断裂:Decart Queue API 只有轮询无 webhook;Comfy 官方承认消费级 GPU 本地视频 slow or infeasible;没有任何工具统一'本地跑不动自动落云、断点恢复、同一 job id 两栖'**
  - 证据：docs.platform.decart.ai Queue 章节:'Poll this endpoint to check if your job has completed';Comfy-Org/comfy-mcp README 本地视频 slow or infeasible 且 Apple GPU 不推荐;Nomi 只做 provider 抽象不做任务迁移
  - 切入：长任务编排层:统一 job id + 状态机(submit/poll/webhook 自适配)、崩溃后 resume、本地显存不足或超时自动 retryWith 云端同款模型——这正是 coding agent 场景里 MCP 工具最缺的 wait/resume 语义
- **'版权可控'没有出现在任何接口合约里:Marey 主打 FULLY LICENSED 但无法直连(waitlist、无 SDK/MCP);LTX license 按 $10M ARR 分层;Stability 靠自托管 license;没有任何 CLI/MCP 用字段表达 commercial-safe 档位**
  - 证据：moonvalley.com/api:'FULLY LICENSED, Commercially safe' 但无文档;HF Lightricks/LTX-2.5 license 标签为 ltx-2.x-community-license-agreement(免费线 <$10M 营收);stability.ai /license 面向自托管;vibeframe/Nomi 等现有多供应商工具均无合规件字段
  - 切入：在多供应商契约里定义 license_tier/commercial_safe 字段并做路由:commercial_safe=true 时自动限定到 Marey(经 fal 或 ComfyUI Partner Nodes)/LTX 社区许可(校验用户营收档)/Stability 自托管;企业 agent 集成(广告、游戏、影视预演)愿意为'可审计的训练数据来源'付溢价——这是模型厂商各自讲了但没人统一表达的层
- **Agent Skill 生态被聚合器把持:最大的 SKILL.md 合集(4.3k★)硬绑 muapi.ai 聚合器,带 utm_source 追踪和 Stripe 充值漏斗,用户的 key 和账单被中间层抽成**
  - 证据：SamurAIGPT/Generative-Media-Skills README:视频工具 muapi_video_generate(13 模型)/muapi_video_from_image(16 模型)全部走 muapi.ai,`muapi mcp serve` 需其 API key + 顶部充值
  - 切入：做纯净 BYOK 的 skill/CLI 合集:自己的 key、自己的账单、无抽成(继承 vibeframe 理念),再叠加成本合约与合规档位——4.3k★ 证明需求真实,聚合器模式证明用户反感点也真实
- **开源模型选型风险高、生态更替快:Mochi 开源线已死(无 release、README 新闻停在 2024-11、org 最后推送 2025-11);Pixelle-MCP(1,116★)、joenorton/comfyui-mcp-server(410★)等社区桥停滞;新基座(Sulphur-2)甚至无明确 license 标签**
  - 证据：github.com/genmoai/mochi:3.7k★、63 commits、零 release、最新新闻 2024-11-26;GitHub API 显示 org 最后 push 2025-11-14;genmo.ai 官网只剩 Mochi 1 和联系邮箱,无 API/定价
  - 切入：CLI 的模型层设计成可插拔契约(model_id + 能力声明 + license 元数据),模型换代只改配置不改代码;给每个 provider/model 标 maintenance_status(官方活跃/社区停滞/已死)和 license 字段,把 Mochi 式的'生态突然死亡'变成可预期风险而非事故

### 未解问题

- LTX 官方 API 具体定价与计费粒度:确认存在 docs.ltx.io/pricing 与 console.ltx.io,但两次抓取均未取到定价正文(ltx.io 曾报 Header overflow)
- Comfy Cloud MCP 与 Comfy Agent 的官方发布公告日期:blog.comfy.org 渲染不出文章列表;comfy-mcp 创建于 2026-07-01 可作下界
- Decart 宣称的 $3 亿融资:官网 raise 页面未标日期,TechCrunch 报道(2026-06-10 Oasis 驾驶)与 2025-08 $1 亿@$31 亿估值为多源交叉,轮次细节未核实
- Odyssey-3 官宣页的可核实性:WebFetch 小模型对 introducing-odyssey-3 页面链接真实性提出质疑,'coming weeks' 的确切时点与发布形态(开源权重?产品?API?)未知
- MiniMax-H3 基座权重本身是否官方开源、归属哪条产品线(HF 趋势被衍生品霸榜)——属并行研究组(海螺/MiniMax)的深挖范围,此处仅交叉引用
- Genmo 现状:官网只有 Mochi 1 介绍与 hi@genmo.ai,是否还有存活的 API/世界模型产品线无法从公开页面确认
- Moonvalley 公开 API 的开放时间表、定价与是否附 SDK/MCP——waitlist 之外无任何信息

### 来源

- [Comfy-Org/comfy-mcp(官方本地 MCP,2026-07-01 创建)](https://api.github.com/repos/Comfy-Org/comfy-mcp)
- [Comfy-Org/comfy-skills(Comfy Cloud skills 与 Claude Code 插件)](https://github.com/Comfy-Org/comfy-skills)
- [artokun/comfyui-mcp(社区桥因官方入场弃档)](https://github.com/artokun/comfyui-mcp)
- [Lightricks org 仓库全量(API,含 LTX-2/LTX-Desktop/ComfyUI-LTXVideo 推送时间)](https://api.github.com/orgs/Lightricks/repos)
- [Lightricks/LTX-2(官方推理与 LoRA 训练包,含 CLI)](https://github.com/Lightricks/LTX-2)
- [Lightricks/LTX-2.5 模型卡(162 万月下载,社区许可,ComfyUI/diffusers 集成现状)](https://huggingface.co/Lightricks/LTX-2.5)
- [Lightricks HF org(IC-LoRA 家族)](https://huggingface.co/Lightricks)
- [LTX 官网(API/控制台/定价页/状态页/许可)](https://ltx.io)
- [Stability AI 官网(Series B、产品线现状)](https://stability.ai)
- [Moonvalley Marey API(waitlist-only)](https://moonvalley.com/api)
- [ComfyUI 官方博客:Marey Realism v1.5 native Partner Nodes(2025-07-08,窗口外交叉引用)](https://blog.comfy.org/p/marey-realism-v15-in-comfyui-built)
- [Decart 平台定价(Lucy 2.5/Oasis 3,秒级单价)](https://docs.platform.decart.ai/getting-started/pricing)
- [Decart 官网(产品矩阵与融资叙事)](https://www.decart.ai)
- [Odyssey-3 官宣(可核实性存疑)](https://odyssey.systems/introducing-odyssey-3)
- [genmoai/mochi(开源线死亡证据)](https://github.com/genmoai/mochi)
- [Genmo 官网(无 API/定价)](https://www.genmo.ai)
- [vericontext/vibeframe(成本即合约 CLI+MCP)](https://github.com/vericontext/vibeframe)
- [SamurAIGPT/Generative-Media-Skills(SKILL.md 合集,muapi 聚合器绑定)](https://github.com/SamurAIGPT/Generative-Media-Skills)
- [aqm857886159/Nomi(本地 ComfyUI 即 provider 的 GUI+MCP)](https://github.com/aqm857886159/Nomi)
- [HuggingFace text-to-video 趋势榜(MiniMax-H3 衍生生态)](https://huggingface.co/models?pipeline_tag=text-to-video&sort=trending)
- [SulphurAI/Sulphur-2-base(LTX-2.3 社区 uncensored 微调,18.3 万月下载)](https://huggingface.co/SulphurAI/Sulphur-2-base)
- [MiniMax-AI/MiniMax-MCP(官方 MCP,交叉引用)](https://github.com/MiniMax-AI/MiniMax-MCP)

---

## 视频应用层（HeyGen/Synthesia/D-ID/Captions/Tavus）

> （限流失败，补跑中）

---

## 大模型厂商（OpenAI/Anthropic/Google/Meta/xAI/Mistral + 中国阵营）

近 90 天（2026-06-22～09-22）国际三家完成了 agent 运行时的平台化收敛：OpenAI 弃用 Agent Builder、关停 Assistants API，推出 Agents API 公测（托管 harness、持久会话、恢复）和 GPT-6 Astra；Google 把视频理解升级为 agentic 主动导航（Gemini 3.8 Flash）并让 computer use 进入 API Preview；Anthropic 发布 Fable 5.1 并把接口向"长时程 agent 运行时"演进。中国厂商以"兼容存量生态 + 托管 agent 运行时 + 激进定价"贴身跟进：DeepSeek V4.1-Flash（原生视觉+峰谷半价）、智谱 GLM-5→5.3 连发（GLM-skills、官方 MCP 套件、Managed Agents）、Qwen3.8 + qwen-code 生态、字节 Seedance 2.5 + ModelArk Managed Agents、月之暗面 Kimi K3 + kimi-code。作为"驱动视频生成流水线的大脑"综合排序：Google（视频原语最全、agentic 视频理解独一档）> OpenAI（编排运行时最强）≈ Anthropic（标准定义权+工具面最稳）> Meta（Muse Spark 一次补齐 agent 能力但 API 未熟）＞ xAI/Mistral；中国阵营智谱生态闭环最完整、DeepSeek 是性价比大脑、Qwen 工具链最全。"没有一家原生提供视频生成编排层"的判断基本成立但有限定：各家编排全部绑自家模型与沙箱，视频生成只在工具/MCP 原语层被官方化（Google Genmedia MCP servers），"分镜→扩写→生成→VLM 判片→重试/换模型"的跨厂商垂直编排层、统一异步任务契约、判片闭环，是三个明确且无人占据的空位——正是 contract-first 多供应商 CLI 的切入点。

### 近 90 天时间线

- **2026-06-23** — Mistral 发布 OCR 4（文档智能）；次日给 Le Chat 连接器加权限控制——把 MCP 连接器治理产品化（https://mistral.ai/news）
- **2026-07-07** — Meta 发布 Muse Image 与 Muse Video（T2V 早期预览、原生音频、Arena T2V 第 3 名）；Muse Image 内置 RL 涌现的自我精修（改稿/重生成/换工具）（https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/）
- **2026-07-08** — 字节 Seedream 5.0 Pro 图像模型发布（主打'懂设计'）；7 月内 Seed 系列连发音频创作、音视频全双工模型（https://seed.bytedance.com/en）
- **2026-07-09** — Meta 发布 Muse Spark 1.1 + Meta Model API 公测：单模型内 MCP server 零样本泛化、computer use（自决'写脚本还是点击'）、主/子智能体分工、1M 上下文主动压缩（https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/）
- **2026-07-09** — OpenAI 发布 GPT-5.6 家族（Sol/Terra/Luna）：Programmatic Tool Calling、持久化推理、max effort，并在 Responses API 推出多智能体编排 beta（https://developers.openai.com/changelog）
- **2026-07-09** — Mistral Studio 上线：把 prompts 和 skills 做成'系统记录'（版本化、可归属、可追溯）（https://mistral.ai/news）
- **2026-07-31** — DeepSeek V4-Flash 公测：原生支持 OpenAI Responses API 格式并'专门适配 Codex'；agent 基准超 V4-Pro-Preview（https://api-docs.deepseek.com/updates）
- **2026-07-31** — 字节 Seedance 2.5 视频生成模型发布：'一条过'创作、灵活参考引用（https://seed.bytedance.com/en）
- **2026-08-13** — DeepSeek V4-Pro GA：thinking 增加低/高/max 三档 effort；推出峰谷定价（谷时为峰值一半，8-16 生效）（https://api-docs.deepseek.com/updates）
- **2026-08-17** — 阿里开源 Qwen3.8（8-27 追加 Qwen3.8-Flash-Next）；同期 Qwen-AgentWorld、E-CommerceBench 等 agent 仓库密集更新（https://github.com/orgs/QwenLM/repositories?type=all&sort=updated）
- **2026-08-20** — Mistral 发布 Agentic Search：让 AI 在复杂文档中导航、阅读、交叉验证的检索层（https://mistral.ai/news）
- **2026-08-21** — DeepSeek V4-Flash-Vision-Exp 实验版：视觉 agent 能力自称'接近 Opus-4.8'（Terminal-Bench 83.9、NL2Repo 57.7）（https://api-docs.deepseek.com/updates）
- **2026-08-26** — OpenAI 正式关停 Assistants API，全面迁移到 Responses/Conversations API——旧 agent 接口时代结束（https://developers.openai.com/changelog）
- **2026-09-01** — Anthropic 发布 Claude Fable 5.1 / Mythos 5.1：effort 分级、preserved thinking（append-only 历史）、refusal fallback、cache 读取降至 $0.25/MTok（https://www.anthropic.com/news）
- **2026-09-01** — 智谱 GLM-5 开源仓库更新（'From Vibe Coding to Agentic Engineering'）；中文文档线已推进到 GLM-5.3 旗舰（自称编码/agent'比肩 Claude Fable 5'）与 GLM-5.3-Flash（原生理解图片/视频）（https://docs.bigmodel.cn/cn/guide/start/model-overview）
- **2026-09-03** — OpenAI 发布 GPT-6 Astra（涵盖推理/编码/computer use/research，仅 Responses API 支持工具）；同日 Responses API 推长任务控制：异步工具调用、WebSocket 中途转向、中途改 reasoning effort（https://developers.openai.com/changelog）
- **2026-09-08** — Mistral 完成 €3B D 轮融资，投后估值超 €21B（https://mistral.ai/news）
- **2026-09-10** — OpenAI Agents API 公测：托管 Codex harness、会话编排、上下文压缩与恢复、持久会话、自定义工具/MCP、托管或自托管沙箱——编排即 API（https://developers.openai.com/changelog）
- **2026-09-10** — DeepSeek V4.1-Flash：新架构家族最小模型、原生多模态视觉理解，API 同步降价（https://api-docs.deepseek.com/updates）
- **2026-09-17** — Google 文档双更新：Gemini 3.8 Flash 上线 agentic video understanding（模型主动导航时间线，长视频省 88% token、最长支持 3 小时输入）；computer use 工具支持 3.8 Flash（浏览器/移动/桌面，带安全策略与注入检测，仍为 Preview）（https://ai.google.dev/gemini-api/docs/video-understanding）
- **2026-09-17** — xAI 文档显示 Grok Build（grok-4.7，agentic 编码，API+CLI 早期访问）与 Imagine API（图像+视频生成/编辑）；agent 工具面仅列函数调用与联网搜索（https://docs.x.ai/docs/overview）
- **2026-09-20** — 阿里 Qwen-MM-Plugins（'让任意 agent harness 多模态原生'，2.9k★）与 Qwen-Image-2.1 更新；qwen-code（28k★，MCP/Auto-Skills/SKILL.md/子智能体开箱即用）9-21 仍在高频提交（https://github.com/orgs/QwenLM/repositories?type=all&sort=updated）
- **2026-09-21** — 国产 CLI 三强同日活跃：智谱 ZCode（自家 harness，5.4k★）、月之暗面 kimi-code（7.6k★，MCP 会话式配置、插件市场、子智能体、视频输入/屏幕录像、ACP 协议）（https://github.com/MoonshotAI/kimi-code）

### Roadmap 信号

- **Google 把视频理解/生成全面 agentic 化：动态时间线导航、对话式视频编辑（Omni Flash + Interactions API 多轮）、Veo 3.1 场景延展——'判片-重改'正在内化进模型 API 层，未来判片可能不需要外挂**（置信：官方明示（文档 2026-09-17/06-30 更新）；https://ai.google.dev/gemini-api/docs/video）
- **OpenAI 的 AgentKit 收敛为 Agents API 主航道（Agent Builder 6 月已弃用）→ 托管 agent 运行时（会话/恢复/压缩）是 OpenAI 未来两个季度的重心，视频侧（Sora）在 API 层 90 天内静默**（置信：官方明示（changelog）；https://developers.openai.com/changelog）
- **'托管 agent 运行时'全行业趋同：Anthropic（2026-04 beta）→ 字节 ModelArk → 智谱 bigmodel 先后出现同构资源模型（Agent/Environment/Session/Vault/Skill/Deployment/记忆/定时任务），2026 下半年各家会卷'沙箱生态与技能市场'而非裸模型**（置信：多源交叉（三家文档结构比对）；https://docs.bigmodel.cn/llms.txt）
- **SKILL.md 正在跨 harness 成为事实标准：Qwen Code（.qwen/skills/SKILL.md + Auto-Skills）、kimi-code（.agents/skills + 插件市场）、智谱 GLM-skills、字节 ModelArk Skills、Mistral Studio skills 治理——一个'跨厂商技能分发层'的生态位正在打开**（置信：多源交叉；https://github.com/QwenLM/qwen-code）
- **Meta Muse Video 仅'coming soon to creators and Meta AI'，Model API 公测未含视频生成、定价未公开——若 Meta 视频进 API，T2V 供给端将再添一强，多供应商路由价值上升**（置信：官方明示（上线节奏）+ 推断（API 时间表）；https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/）
- **DeepSeek 双接口战略（OpenAI + Anthropic 兼容、Codex 专门适配）代表中国厂商路线：不定义新标准、全面兼容存量 agent 生态抢用户——未来国产 API 的'Claude Code 兼容端点'会成为标配**（置信：官方明示；https://api-docs.deepseek.com/updates）
- **xAI 向创作（Imagine API 图+视频生成/编辑）与编码（Grok Build）两端扩张，但 agent 工具面（MCP/computer use/代码执行）未见官方产品化——若补齐将改变第六名格局**（置信：推断（官方文档页覆盖不足）；https://docs.x.ai/docs/overview）
- **Anthropic 的 API 正在'操作系统化'：append-only 历史、effort 分级、refusal 自动回退、任务预算、cache 读 $0.25/MTok——长时程 agent 运行时接口会持续加约束换稳定性，跟随者（智谱、DeepSeek）大概率复制这套语义**（置信：官方明示；https://www.anthropic.com/claude-fable-and-mythos-5-1）
- **Google computer use 仍是 Preview 且推荐客户端自持循环（Playwright + Docker 参考）——距离'官方托管 computer use'尚有一步，这块是 OpenAI（GPT-6 Astra）与 Anthropic（server-hosted computer use）相对领先的位置**（置信：官方明示（标注 Preview）；https://ai.google.dev/gemini-api/docs/computer-use）

### 做得好的

- Google 把'视频即上下文'工程化最深：全系模型支持视频输入（最长 3 小时）、agentic video understanding 让模型自己导航时间线、Gemini Omni Flash 提供'对话式视频编辑'API、Genmedia MCP servers 把 Veo/Imagen/Lyria 官方 MCP 化——离'视频流水线原语'最近的一家
- OpenAI 的运行时收敛果断：关停 Assistants、弃用 Agent Builder，全部押注 Responses API + Agents API（托管 harness、恢复、压缩、WebSocket 中途转向），'编排即 API'路线清晰且工程完成度高
- Anthropic 拥有标准定义权：MCP 与 SKILL.md 都由它定义并被全行业采纳；Managed Agents（vaults 凭据、outcome 评分器、定时部署、多智能体会话）+ 七语言 SDK + Batches 半价 + Message Batches 长任务，生态位最完整
- 国产 CLI 三强（qwen-code 28k★、kimi-code、ZCode）用'多协议兼容'（同时吃 OpenAI/Anthropic/Gemini 接口、GLM 编码计划直接兼容 Claude Code）换增长，迭代速度和免费额度（Gemini CLI 1000 次/天、GLM-Flash 免费）非常激进
- DeepSeek 重新定义了成本结构：峰谷定价（谷时半价）把'可延迟负载'（批量生成、判片）的价格打到新低，且 V4.1-Flash 原生视觉 + Responses API/Codex 双适配，是性价比最高的'流水线大脑'候选
- 智谱是国产里生态闭环最完整的：官方 MCP servers 套件（视觉理解 MCP 少见）、GLM-skills 官方技能库、Managed Agents 全套资源模型、异步视频生成 API、批量 API、$18 包月编码计划、CogVideoX-3 甚至接入了 Vidu 作伙伴模型
- Mistral Studio 把 prompts/skills 当'系统记录'做版本化治理 + MCP 人审控制——'技能资产化'的思路值得所有工具链学习
- Meta Muse Spark 1.1 一次性补齐 agent 短板：MCP server 零样本泛化、computer use（自决脚本化 vs 点击）、多智能体主从分工，且把 1M 上下文'主动压缩'做进模型层；Muse Video 原生音频直接进 T2V 第一梯队（Arena 第 3）
- 字节把'模型+托管 agent+媒体生成'放进同一朵云：ModelArk 的 Managed Agents（Skills/MCP/Vaults/持久记忆/Multi Agent/Define Outcome）与 Seedance 2.5、Seedream 5.0 Pro 同栈，是国内离'一站式创作中台'最近的形态
- 对判片场景的直接利好：多家在同一窗口内大幅降低多模态判断成本——DeepSeek V4.1-Flash（原生视觉+降价）、GLM-5.3-Flash（原生图/视频理解）、Gemini 3.8 Flash（token 效率 +88%）都让'每次生成后跑一遍 VLM 评审'变得经济上可行

### 空位与切入姿势

- **没有一家提供'跨供应商视频生成编排层'——判断基本成立，但需要限定词：'编排'本身正在被各家做成产品，只是全部绑死自家模型与沙箱**
  - 证据：OpenAI Agents API（9/10）编排的是自家 Codex harness；Anthropic/字节 ModelArk/智谱三家的 Managed Agents 都是'自家模型+自家沙箱'的通用 agent 运行时；Google 最接近（Genmedia MCP servers 把 Veo/Imagen 官方 MCP 化 + ADK graph workflows），但媒体工具只限谷歌自家模型；没有任何一家把'分镜规划→prompt 扩写→多模型生成→VLM 判片→重试/换模型→合成'作为可购买的产品层
  - 切入：独立开发者的 contract-first 多供应商 CLI 正好卡进这个空位：把编排层做成'大脑可插拔'（任意大模型当决策者），把各家长任务契约（Google operations、智谱/火山异步任务、fal queue）统一成一套可恢复的任务协议——厂商做'单家垂直整合'，你做'跨家中立编排'
- **'生成结果→VLM 判片→结构化失败原因→自动重试/换模型'的闭环没有任何厂商产品化**
  - 证据：Google 的 agentic video understanding 是'理解'不是'评判-重试'；Meta Muse Image 的自我精修（edit/regenerate/switch tactics）仅限自家图像生成且未进 API；Anthropic 与字节的 Managed Agents 都有'Outcome/Define Outcome'通用评分器，但不懂视频领域维度（时序一致性、口型同步、物理合理性、分镜偏差）
  - 切入：把'判片'做成领域专用层：用便宜多模态模型（DeepSeek V4.1-Flash、GLM-5.3-Flash、Gemini 3.8 Flash）当 judge，输出结构化失败分类，驱动自动重试或跨模型路由——这是所有厂商因利益冲突（不愿给自己的生成打低分）永远做不好的中立环节
- **长异步任务的等待/恢复契约严重碎片化，至少五种模式并存**
  - 证据：智谱视频生成是'异步提交+查询结果'轮询（docs.bigmodel.cn 视频生成异步 API）；Google 用 operations；OpenAI 新推 WebSocket 中途转向；字节 ModelArk 用 session 事件流；智谱知识库部分接口用 callback_url 回调——无跨厂商的提交/查询/取消/恢复/幂等标准
  - 切入：这正是 CLI 项目的 contract-first 核心卖点：统一任务句柄（提交/查询/取消/断线恢复/幂等键），按厂商写适配器，用户面向一套协议写流水线；断线重连后能从任务句柄恢复状态，是所有官方 SDK 都没做的一层
- **视频生成尚未被系统性 MCP 化，'官方 MCP server'大多只是自家能力封装**
  - 证据：Google Genmedia MCP（Imagen/Veo/Lyria）是唯一官方媒体生成 MCP；智谱有四个官方 MCP（视觉理解/联网搜索/网页读取/zread）但不含 CogVideoX；OpenAI 走 Hosted MCP connector 路线；xAI overview 页未列 MCP；DeepSeek 官方 changelog 全篇无 MCP 字样
  - 切入：做'多厂商视频生成统一 MCP server'（一个 server 暴露 Seedance/Veo/Sora/可灵/CogVideoX…），让任何 agent（Claude Code、qwen-code、kimi-code、ZCode）即插即用——Google 已验证该模式的产品形态，跨厂商版本空着
- **计费透明度与成本可预测性差异极大，且视频类按'媒体分辨率计 token'这类隐性成本容易踩坑**
  - 证据：Google 视频输入按分辨率计 token（低清约 100 token/秒、高清 300）；Meta Model API 未公开定价；xAI 文档页无价格数字；对比之下 DeepSeek 推出峰谷定价（谷时半价）、智谱有免费 Flash 档 + $18 包月——成本端没有统一的'预估'接口
  - 切入：给 CLI 内置成本估算器 + 峰谷调度器：每条视频生成前输出预估成本区间，把可延迟的批量任务自动排到 DeepSeek 谷时/智谱免费档；这是对独立开发者和小团队最直接的成本杠杆
- **视频输入（VLM 判片的前提）供给严重不均，且与视频生成能力分家**
  - 证据：Gemini 全系支持视频输入（最长 3 小时）；Kimi K3 原生视觉已进 CLI（可直接喂屏幕录像）；GLM-5.3-Flash 原生理解图/视频；DeepSeek 8 月才补上视觉实验版；Claude 官方无视频输入（仅图像/PDF，判片需自行抽帧）；Mistral/xAI 的视频输入能力在官方文档未见明确说明
  - 切入：在 CLI 里做'供应商无关的视频判片封装'：对不支持视频输入的模型自动抽帧+图片批判，对支持的直传——同一判片质量下的成本差可达 10 倍，路由本身就是价值
- **中国厂商 agent 生态'强执行、弱标准'：协议定义权缺席、computer use 官方 API 缺位、多供应商质量一致性要靠社区自证**
  - 证据：MCP 与 SKILL.md 均由 Anthropic 定义，国产全部以兼容姿态接入（Qwen Code 多协议、GLM 编码计划兼容 Claude Code、DeepSeek 双接口）；computer use 侧智谱是 AutoGLM-Phone（手机场景）+ 阿里 open-computer-use 是 Qwen Code 的 MCP 服务而非平台 API；MoonshotAI 的 K2-Vendor-Verifier（593★）专门校验'不同供应商 Kimi API 精度一致性'——说明国内转售/分发链路的输出质量参差是公认痛点
  - 切入：面向中国供应商做'一致性与直连适配层'：多供应商同模型输出校验、国内网络可直连的模型池、国产 API 的统一判片基线——这是国际工具（LangChain/LangSmith 等）进不来、国内大厂不屑做的本土空位
- **OpenAI 阵营出现'产品层回撤'信号：面向低代码的 Agent Builder 被弃用，Evals 平台与可复用 prompt 对象同时进入弃用流程**
  - 证据：OpenAI changelog 2026-06-03：弃用 reusable prompt objects、Evals platform、Agent Builder；8-26 关停 Assistants API
  - 切入：低代码/可视化编排用户被 OpenAI 主动释放出来；CLI+配置文件（contract-first）恰好是'比低代码稳、比 SDK 省事'的中间形态，可承接这部分开发者

### 未解问题

- OpenAI Sora 2 API 近 90 天在开发者 changelog 无任何条目，其 API 侧迭代状态、定价与能力变化未能核实（openai.com 主站 403）
- 月之暗面平台侧信息缺失：Kimi for Coding 订阅定价、官方 MCP 支持、是否提供 Anthropic 兼容端点未核实（platform.moonshot.ai 连接失败；GitHub 侧仅见 kimi-code OAuth + API key 两种接入）
- 火山方舟国内侧未直接核实：豆包 App/Dola 的 agent 能力、方舟 MCP 市场、Seedance 国内 API 的异步细节——本次只核实了国际版 BytePlus ModelArk
- 通义万相 Wan 视频模型近 90 天版本节奏未核实（Wan 在独立 Wan-AI org 下，不在 QwenLM org）
- Meta Model API 的公开定价与 Muse Video 的 API 开放时间表均未公布
- Google computer use 的 GA 时间表未明示（当前 Preview）；Anthropic computer use 近 90 天无新闻条目，其 server-hosted 形态的最新状态未单独核实
- xAI Imagine API 的视频生成规格（时长/分辨率/价格）与 Agent Tools 是否支持 MCP，需要进一步抓 docs.x.ai 子页面确认

### 来源

- [Anthropic Newsroom（Fable 5.1 / Mythos 5.1，2026-09-01）](https://www.anthropic.com/news)
- [OpenAI Developers Changelog（Agents API / GPT-6 Astra / GPT-5.6 / Assistants API 关停）](https://developers.openai.com/changelog)
- [OpenAI Agents SDK — MCP 支持文档](https://openai.github.io/openai-agents-python/mcp/)
- [openai/codex（Codex CLI，125.7k★）](https://github.com/openai/codex)
- [Gemini API — Video Understanding（agentic video understanding，2026-09-17 更新）](https://ai.google.dev/gemini-api/docs/video-understanding)
- [Gemini API — Video Generation（Gemini Omni Flash / Veo 3.1）](https://ai.google.dev/gemini-api/docs/video)
- [Gemini API — Computer Use（Gemini 3.8 Flash，Preview）](https://ai.google.dev/gemini-api/docs/computer-use)
- [Google ADK — MCP（双向支持 + Genmedia MCP servers）](https://adk.dev/mcp/)
- [google-gemini/gemini-cli（107.1k★，MCP + GEMINI.md + 媒体生成）](https://github.com/google-gemini/gemini-cli)
- [xAI Docs Overview（Grok Build / Imagine API）](https://docs.x.ai/docs/overview)
- [Mistral News（Studio / Agentic Search / €3B 融资）](https://mistral.ai/news)
- [Meta — Introducing Muse Spark 1.1（Meta Model API 公测）](https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/)
- [Meta — Introducing Muse Image and Muse Video](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/)
- [DeepSeek API 更新日志（V4.1-Flash / V4-Pro 峰谷定价 / Vision-Exp）](https://api-docs.deepseek.com/updates)
- [QwenLM GitHub Org（Qwen3.8 / qwen-code / Qwen-MM-Plugins）](https://github.com/orgs/QwenLM/repositories?type=all&sort=updated)
- [QwenLM/qwen-code（MCP/Auto-Skills/SKILL.md/多协议）](https://github.com/QwenLM/qwen-code)
- [MoonshotAI GitHub Org（Kimi-K3 / Kimi-K2.5 / kimi-code）](https://github.com/MoonshotAI)
- [MoonshotAI/kimi-code（MCP 会话配置/插件市场/视频输入）](https://github.com/MoonshotAI/kimi-code)
- [zai-org GitHub Org（GLM-5 / GLM-V / ZCode / GLM-skills / Open-AutoGLM）](https://github.com/orgs/zai-org/repositories?type=all&sort=updated)
- [智谱 BigModel 模型总览（GLM-5.3 / CogVideoX-3 / Vidu 伙伴模型）](https://docs.bigmodel.cn/cn/guide/start/model-overview)
- [智谱 BigModel 文档索引（Managed Agents / 官方 MCP / 异步视频生成 / Batch）](https://docs.bigmodel.cn/llms.txt)
- [Z.ai Docs（GLM-5.3 / GLM Coding Plan $18/月 / SDK）](https://docs.z.ai/)
- [ByteDance Seed 官网（Seedance 2.5 / Seedream 5.0 Pro / Seed2.1）](https://seed.bytedance.com/en)
- [BytePlus ModelArk 文档（Managed Agents / Skills / MCP / Vaults / Seedance）](https://docs.byteplus.com/en/docs/modelark)

---

## 训练/微调基础设施（Together/RunPod/Replicate/Modal/Fireworks/Lambda/硅基流动）

七家训练/推理基础设施厂商在最近 90 天里把「视频生成托管」卷得很凶——Together 聚合了 Seedance 2.5/2.0、Wan 2.7、Kling、Vidu 并按条计价，RunPod 上架 Wan 2.2/2.6 端点（含可外挂 LoRA 权重的变体），Replicate 拥有最大视频目录（Sora-2、Veo 3.1、Kling v3、Wan 3 等），硅基流动托管 Wan2.2——但「视频微调 as a service」在全部七家全面缺位：所有微调产品都止步于 LLM（+VLM/生图），视频角色一致性只以三种零散形态存在（Modal 自管代码示例、RunPod 端点吃外部 LoRA URL、厂商 reference-image API）。Agent 集成在推理侧已经内卷（RunPod 双 MCP+官方 skills 插件、Together 12 个 SKILL.md+docs MCP、Replicate remote MCP+code mode、Fireworks firectl+docs MCP），训练侧的 agent 化只有苗头（Fireworks agentic RL、Lambda 研究线）。对你的 contract-first 多供应商视频 CLI 而言，最大空位非常清晰：没有任何一家提供「一条命令完成角色视频 LoRA 训练→权重托管→agent 可调用」的服务，且视频侧的长任务恢复、URL 过期归档、成本归一化语义普遍比 LLM 侧落后一代。

### 近 90 天时间线

- **2026-08-31** — Fireworks 宣布 Training API 正式 GA（SFT/DPO/RFT/蒸馏，任务级 create/resume/cancel/metrics 端点），但仅覆盖 LLM，无图像/视频生成模型训练（https://fireworks.ai/blog）
- **2026-07-15** — Fireworks 宣布 Series D 融资与 $1B ARR；7/26 发文推广 Kimi K3 LoRA 训练、7/30 讨论 LoRA vs FullFT 选型——训练叙事全部围绕 LLM（https://fireworks.ai/blog）
- **2026-06-24** — Fireworks 把自用前沿实验室训练基础设施开放为 GLM 5.2 托管训练服务——「训练即托管服务」路线明确但限于大语言模型（https://fireworks.ai/blog）
- **2026-08-04** — Replicate 上架 FLUX 3（Black Forest Labs 首个音视频一体模型）并发布使用指南；整个 90 天窗口 Replicate 博客仅 2 篇，2025-11 并入 Cloudflare 后发布节奏显著放缓（https://replicate.com/blog）
- **2026-09（页面未标日期，推断 90 天内）** — Together 上架 Seedance 2.5（$0.115/条）、Seedance 2.0（$0.16/条）、MiniMax H3（$0.1391/条）、FLUX 3，另有 Wan-AI/Kuaishou/Vidu 各 5 个模型，并配 Wan 2.7 与 Seedance 2.5 官方 quickstart——多供应商视频聚合成型（https://www.together.ai/models）
- **2026-07-16 ~ 07-29** — Modal 连发「1M 并发沙箱」（7/16）、「Devin Outposts 驻场」（7/21）、「Modal is a computer」（7/9）、「Hugging Face agent 事件回应」（7/29）——全面转向 agent 基础计算层叙事，90 天内无视频模型相关动作（https://modal.com/blog）
- **2026-06-23** — Modal 发布 Auto Endpoints（自动伸缩推理端点）；7/6 发文「How to price serverless GPUs」把定价透明当卖点；训练产品（Training）已在产品线但 90 天无视频相关更新（https://modal.com/blog）
- **2026-09-03** — RunPod 上架 Pruna P-Video-Edit 公共端点教程（视频编辑推理）；RunPod 90 天博客无任何视频 LoRA 训练/微调内容（https://www.runpod.io/blog）
- **2026-09-01 ~ 09-14** — RunPod 三连：ISO 27001 认证（9/1）、私有 GPU 池与预留容量（9/11）、Global Volumes beta（9/14）——面向 agent 工作负载的基础设施成熟化（https://www.runpod.io/blog）
- **2026-09-02** — RunPod 发文「Designing MCP tools that don't blow up your agent's context window」——官方下场讨论 agent 工具设计（https://www.runpod.io/blog）
- **2026-09-10** — Lambda 发布 OpenResearcher（可复现的 deep research agent 训练流水线）；8/25 发布 AgentFlow（「当 agent 的工作流自己学习」）——训练侧 agent 化最密集的研究输出（https://lambda.ai/blog）
- **2026-09-17** — Lambda 发文「Closing the loop: agentic evaluation for image editing foundation models」——用 agent 评估闭环反哺图像基础模型训练，是最接近「agent 驱动训练」的信号（https://lambda.ai/blog）
- **2026-08-12 ~ 08-27** — Lambda 完成 $926M 投资级抵押 term loan（8/12 定价、8/27 交割）扩 GPU 产能——算力扩张但无视频/托管推理产品动作（https://lambda.ai/blog）
- **2026-09（文档无日期，推断近期）** — RunPod Wan 2.2 端点支持外挂 high/low-noise LoRA 权重（传 safetensors URL，$0.35-0.56/条，URL 7 天过期）——「自带 LoRA 来推理」路线，但没人帮用户训练（https://docs.runpod.io/public-endpoints/models/wan-2-2-i2v-lora.md）

### Roadmap 信号

- **Fireworks 训练平台化是其明确主航道：Training API GA（8/31）+ agentic RL cookbook + 为 GLM 5.2 提供托管训练 + 训练成本估算器；但其训练目前严格限于 LLM**（置信：官方明示；https://fireworks.ai/blog）
- **Together 明确走多供应商视频聚合：Seedance/Wan/Kling/Vidu/MiniMax 全上、按条计价、Wan 2.7 与 Seedance 2.5 配 quickstart、skills 和 docs MCP 均覆盖视频域；视频训练能力未见任何布局**（置信：官方明示；https://www.together.ai/models）
- **RunPod 押注「agent 原生 GPU 云」：MCP×2 + 官方 skills 插件 + agent-setup 专页 + ISO 27001 + 预留容量/Global Volumes；下一步大概率是把更多生成媒体端点（已见 Wan/Pruna 系列）纳入公共端点目录**（置信：官方明示；https://docs.runpod.io/get-started/agent-skills.md）
- **Lambda 正沿「agentic 训练/评估」研究线密集输出（OpenResearcher 9/10、AgentFlow 8/25、图像编辑基础模型 agentic 评估 9/17），有把 agent 驱动训练产品化的势头，但截至今日无任何产品公告**（置信：多源交叉（研究线密集，产品化为推断）；https://lambda.ai/blog）
- **Replicate 自 2025-11 宣布并入 Cloudflare 后进入明显维护期：90 天仅 2 篇博客、官方 CLI 至今无 release、视频 trainer 生态停更——其「社区模型+训练分发」心智正被让出**（置信：多源交叉；https://replicate.com/blog）
- **厂商侧把角色一致性推向「大模型 reference API」而非用户自训 LoRA：Replicate 上架 bytedance/dreamactor-m2.0、Together 建了 reference-and-keyframes 文档、Kling omni 系列扩展——open-weight LoRA 路线被留给第三方基础设施商**（置信：多源交叉；https://replicate.com/collections/text-to-video）
- **推断：若 Fireworks 或 Together 把训练 API 扩展到生成媒体（图像/视频 LoRA），上述空位将在产品层面被碾平；从 Fireworks 训练路线全在 LLM 看，窗口期约为 6-12 个月量级**（置信：推断；https://docs.fireworks.ai/llms.txt）

### 做得好的

- RunPod 的 agent 集成是七家里最完整的：官方双 MCP server（API 管理类走 OAuth 托管在 mcp.getrunpod.io + 免鉴权文档检索类在 docs.runpod.io/mcp）、一行命令装官方 skills 插件（npx skills add runpod/runpod-plugins-official，6 个技能+内置路由）、runpodctl 甚至有 billing 子命令、SDK 覆盖 Python/JS/Go——独立 CLI 可直接借鉴它的技能路由结构和 Claude Code 安装命令写法
- Together 的 12 个官方 SKILL.md 技能按领域拆分（chat/images/video/audio/fine-tuning/batch/evals/sandboxes 等）并明确定义技能间 hand-off 边界使 agent 能链式调用，遵循 agentskills.io 开放规范——这是 SKILL.md 设计的最佳范本，可照抄其结构做你自己的 CLI 技能
- Replicate 的 remote MCP（mcp.replicate.com）宣称覆盖全部 HTTP API（含 trainings），还实验性提供 code mode：在 Deno 沙箱里让模型直接写 TypeScript 调 API 以省上下文——多步骤 agent 工作流的正确方向，值得在 CLI 的 agent 接入层复用
- Fireworks 的训练任务生命周期契约最完整：jobs REST API 有 create/resume/cancel/metrics 端点，SDK 有 TrainerJobManager/WeightSyncer 等抽象，还有训练成本估算器——长异步任务的「恢复」语义可直接参考它的 API 形状
- Together 和 RunPod 的推理响应都内嵌 cost 字段（Together 示例 "cost": 0.28；RunPod output.cost）——计费可观测已是现成好实践，contract-first CLI 应把 cost 当一等公民字段归一化
- Modal 的 music-video-gen 示例证明视频角色 LoRA 技术配方已成熟：4-8 张照片+trigger token，几分钟训练，7×H100 并行约 5 分钟产出 30 秒成片，finetune-id 资产化管理——只差有人把它从 clone-and-run 代码封装成服务
- Replicate 的训练计费最透明：训练按秒计费且文档直接给出单价（8×H100 = $0.0122/秒，一次 FLUX 微调约 $1.46）——跨厂商成本对比页可以拿它当锚点

### 空位与切入姿势

- **「视频 LoRA 训练 as a service」在全部七家缺位：所有微调产品止步于 LLM（Fireworks SFT/DPO/RFT、Together LoRA/DPO/VLM、硅基流动对话+生图微调），没有任何一家接受视频训练数据；Replicate 的视频微调自 2025-01（HunyuanVideo）后再无产品级更新**
  - 证据：Together 微调文档只提文本与视觉语言模型；Fireworks llms.txt 训练页面全部为文本 SFT/DPO/RFT；硅基流动微调文档原话「选择对话模型微调或者生图模型微调」；Replicate text-to-video 合集与 fofr 等高产出创作者页面均无视频 trainer；RunPod 文档索引无任何 LoRA 训练指南
  - 切入：你的 CLI 串联「Modal/RunPod spot GPU 跑开源 Wan LoRA 训练配方（diffusion-pipe/musubi-tuner 类）→ 权重托管（HF repo/RunPod volume）→ RunPod LoRA 端点或 Replicate 模型推理」为一条命令；训练配方本身（超参、数据格式、触发词）作为可分发的 contract 资产——这是所有厂商都不敢做轻资产服务的空位
- **角色一致性当前是三条互不相通的断路：a) 厂商 reference API（每次推理带参考图/关键帧，无持久角色资产）b) RunPod 端点外挂 LoRA URL（用户必须自己去别处训练）c) Modal 开源示例（自己跑 JupyterLab 训练，非服务）**
  - 证据：Together 有「Reference images and keyframes」文档页、Replicate 上架 bytedance/dreamactor-m2.0（角色表演视频模型）；RunPod WAN 2.2 端点要求 input.high_noise_loras[].path 自备 safetensors 文件；Modal music-video-gen 是 clone 仓库自管代码（4-8 张照片→训练数分钟→7×H100 并行出片），文档明说「it's just code and containers」
  - 切入：把「角色资产」抽象成跨厂商可复用的契约：一个 character_id = 训练数据集 + LoRA 权重引用 + trigger 词 + 一致性评测集 + 各家端点适配器；训练一次、随处推理（RunPod 端点/Replicate 社区模型/自建 Modal 应用），并生成一致性对比报告
- **训练侧 agent 化刚萌芽且全部指向 LLM：Fireworks 的 agentic RL 是「训练 agent」而非「agent 驱动训练」；RunPod 官方六技能能让 agent 开 Pod/部署函数，但没有任何训练配方技能；Together 12 技能中的 fine-tuning 只覆盖 LoRA/DPO/VLM；无人提供「agent 整理数据→发起视频训练→评估→注册推理端点」闭环**
  - 证据：Fireworks llms.txt 训练 cookbook 含 agentic-rl 与 Remote Agent Quickstart（均面向 LLM RL）；RunPod 技能列表为 runpod/runpod-mcp/runpodctl/flash/companion-clis/runpod-usage/runpod-migrate，零训练技能；Together skills 覆盖页明确 fine-tuning 范围是 LoRA/DPO/VLM（文本域）
  - 切入：做一个「视频角色训练 skill」（SKILL.md + CLI 子命令）：agent 读角色图集→自动 caption/trigger 词→发起训练→用 VLM 评角色一致性→产出成本与质量报告→把权重注册到推理端点；与你已有的 generate JSON contract 天然衔接
- **视频长任务体验比 LLM 侧落后一代：Together 视频依赖客户端每 60 秒轮询、文档无 webhook、输出 URL 过期需「立即下载」；RunPod 视频 URL 7 天过期且 LoRA 端点只文档化了 runsync 同步路由；七家里只有 Replicate 有完整 webhook 文档、Fireworks 有训练任务 resume 端点**
  - 证据：Together 视频文档原话「Video generation is asynchronous: you create a job, receive a job ID, and poll for completion」及「Download videos immediately after completion」；RunPod Wan 端点文档「Video URLs expire after 7 days」且仅示例 /runsync；docs.together.ai 索引中无 webhook 页
  - 切入：CLI 提供统一异步契约：轮询/webhook 自适应 + 任务句柄可跨进程恢复（Fireworks resume 思路推广到推理）+ 结果自动归档到对象存储防 URL 过期——把「过期 URL」这类所有厂商文档都在警告的坑变成产品差异点
- **计费透明度严重不均：硅基流动视频文档无任何价格链接，Lambda 走销售询价模式，Together 视频费率不在文档页（仅响应内 cost 字段），只有 Replicate（训练 $0.0122/秒、约 $1.46/次）和 RunPod（$0.35-0.56/条、响应带 output.cost）直白；Fireworks 有成本估算器但仅限 LLM 训练**
  - 证据：硅基流动 docs 导航无 pricing（只有 misc_finance FAQ）；Together 视频文档唯一价格线索是示例响应 "cost": 0.28；Replicate fine-tune 指南给出精确单价与总价；RunPod Wan 端点文档列出分时长单价
  - 切入：CLI 归一化各厂商 cost 字段为统一货币视图 + 预算护栏（agent 自动化时代训练+推理链路必须有美元上限与中断保护）；顺手做跨厂商视频生成价格追踪器作为引流内容
- **Replicate 被收购后社区训练生态停摆：「社区模型+一键训练」心智无人接盘——90 天仅 2 篇博客、官方 CLI 无 release、视频目录全是官方/厂商模型而社区 trainer 缺位，头部创作者 fofr 的训练类模型只剩 44 次运行的实验仓库**
  - 证据：replicate.com/blog 90 天窗口仅 FLUX 3 指南（8/4）与 Krea 2（6/23）两篇；text-to-video 合集零 trainer；fofr 页面训练类仅 qwen-black-goya-training（5 runs）与 flux-training-experiments（44 runs）
  - 切入：接住空出的「训练配方分发」位置：CLI 内建配方市场/模板仓库（Wan/Hunyuan/LTX 微调配方+评测集），一键在不同基础设施（Modal/RunPod）复现——正是原 Replicate 社区生态的核心体验，如今无人维护

### 未解问题

- Replicate 当前是否仍有可运行的视频模型 trainer（HunyuanVideo 之后无公开产品更新，2026 目录中未发现 Wan/Hunyuan trainer）？
- Together 视频 API 是否提供 webhook/回调，还是只有客户端轮询？视频模型的公开费率表在哪个页面？
- 硅基流动视频生成的具体定价是多少？是否支持传入自定义 LoRA 权重？
- Modal 是否计划推出官方平台级 MCP server（文档索引只有用户自建 FastMCP 的示例，无平台管理 MCP）？
- Lambda 是否仍维护独立 CLI 与托管推理 API（docs.lambda.ai 首页只列 GPU 云/私有云/托管 K8s/Slurm，未列 CLI 与推理 API）？
- Fireworks Training API 是否会扩展到图像/视频生成模型，有无时间表？
- Modal music-video-gen 示例的底模是否仍是 Wan2.1（示例卡片如此标注，但正文已不点名模型版本）？

### 来源

- [Replicate Blog（90 天仅 2 篇；并入 Cloudflare 公告）](https://replicate.com/blog)
- [Replicate Text-to-Video 模型合集（Sora-2/Veo 3.1/Kling v3/Wan 3/DreamActor 等，无 trainer）](https://replicate.com/collections/text-to-video)
- [Replicate 官方 MCP Server 文档（remote mcp.replicate.com + code mode）](https://replicate.com/docs/reference/mcp)
- [Replicate 微调入门（fast-flux-trainer、按秒计费 $0.0122/s）](https://replicate.com/docs/get-started/fine-tune-with-flux)
- [Replicate 官方 CLI（GitHub，含 training/train 命令）](https://github.com/replicate/cli)
- [Replicate 创作者 fofr 模型页（无视频 trainer）](https://replicate.com/fofr)
- [Modal Blog（atom feed，90 天动作：沙箱/agent/定价透明）](https://modal.com/blog)
- [Modal 示例：Fine-tune Wan2.1 video models on your face（music-video-gen）](https://modal.com/docs/examples/music-video-gen)
- [Modal 示例总目录（LTX/FLUX LoRA/长训练任务/MCP 示例）](https://modal.com/docs/examples)
- [Modal 文档 llms.txt（CLI 全套；无平台 MCP；多节点训练 Beta）](https://modal.com/docs/llms.txt)
- [Together AI 模型库（Seedance 2.5/2.0、MiniMax H3、Wan/Kuaishou/Vidu 系列，按条计价）](https://www.together.ai/models)
- [Together 微调总览（LLM+VLM，tg CLI，轮询无 webhook，无视频微调）](https://docs.together.ai/docs/fine-tuning-overview)
- [Together 视频生成文档（异步 job + 轮询、cost 字段、URL 过期警告）](https://docs.together.ai/docs/inference/videos/overview.md)
- [Together Coding Agent Setup（12 个 SKILL.md 技能 + docs MCP）](https://docs.together.ai/docs/agent-skills.md)
- [Together 文档索引 llms.txt（视频/CLI/batch/Queue API 全目录）](https://docs.together.ai/llms.txt)
- [Fireworks Blog（Training API GA、Series D、$1B ARR、Kimi K3 LoRA 训练）](https://fireworks.ai/blog)
- [Fireworks 文档索引 llms.txt（firectl 训练命令、SFT/DPO/RFT/agentic RL；无视频生成）](https://docs.fireworks.ai/llms.txt)
- [RunPod Blog（ISO 27001、Global Volumes、MCP 工具设计、P-Video-Edit）](https://www.runpod.io/blog)
- [RunPod 文档索引 llms.txt（runpodctl/Flash CLI/SDK 三语言/Wan 端点/agent-skills）](https://docs.runpod.io/llms.txt)
- [RunPod 官方 MCP Servers 文档（API MCP + Docs MCP，OAuth）](https://docs.runpod.io/get-started/mcp-servers.md)
- [RunPod Agent Skills 文档（6 技能+路由，npx skills add 安装）](https://docs.runpod.io/get-started/agent-skills.md)
- [RunPod WAN 2.2 LoRA 端点文档（外挂 LoRA URL、$0.35-0.56/条、URL 7 天过期）](https://docs.runpod.io/public-endpoints/models/wan-2-2-i2v-lora.md)
- [Lambda Blog（OpenResearcher/AgentFlow/agentic eval、$926M term loan）](https://lambda.ai/blog)
- [Lambda 文档（GPU 云/托管 K8s/Slurm；Mochi 视频微调教程；无 CLI/MCP）](https://docs.lambda.ai)
- [硅基流动模型广场（无视频模型在列，视频为独立过滤类目）](https://www.siliconflow.cn/models)
- [硅基流动文档（视频 submit/status 两步 API；微调仅对话+生图；无 CLI/MCP/价格）](https://docs.siliconflow.cn/en/)
- [硅基流动视频生成用户指南（Wan2.2-T2V/I2V-A14B，异步提交+取链接）](https://docs.siliconflow.cn/docs/userguide/capabilities/video)
- [硅基流动微调指南（对话/生图二选一，无视频微调）](https://docs.siliconflow.cn/docs/userguide/guides/fine-tune)

---

## LLM × 视频交叉（编排/判片/分镜契约/MCP 化）

过去 90 天 LLM×视频交叉层出现两个确定性变化：Runway 于 2026-09-11 上线全行业第一个官方托管视频生成 MCP（mcp.runwayml.com/mcp + OAuth 免 API key + 两个官方 SKILL.md），Google 则把视频理解升级为 agentic 能力（模型自导航时间线，官方称省 88% token）并把视频生成并进 Gemini API 文档（Gemini Omni Flash）。与此同时，任务最关心的"判片/验收层"确认无人产品化：VBench 等研究体系停在 pip 包+leaderboard，OpenAI Sora 2 API 只返回 queued/in_progress/completed/failed 四态且全文无 judging，官方 MCP Registry 里 13 个 video server 全是第三方小厂、fal/Kling/Luma 等均无官方 MCP。LLM 侧边界也摸清：Claude API 明确无视频输入（GIF 只取首帧），Qwen3-VL/Gemini 提供小时级视频+秒级时间戳的理解原料但没人把它接到生成验收上。最大空位集中在三处——生成后自动判片并输出结构化 verdict、失败重试决策层、跨厂商分镜 JSON 契约，三者全是契约优先 CLI 的主场，且社区（Playwright 驱动 GUI 的 MCP、多模型聚合网关）已在用最脏的方式抢这些活，证明需求真实存在。

### 近 90 天时间线

- **2026-09-22 查证（页面实时数据）** — 官方 MCP Registry 按 video 检索：仅 13 个唯一 server（30 条含版本），全部为第三方小厂（NoonAI 视频匿名化、Tegas、Filmee 动漫、VideoZero 等），无一来自 Runway/Luma/Kling/fal/Google/OpenAI 等主流厂商；官方 servers 参考仓库 7 个参考 server 中视频生成类为零（图像类 EverArt 已归档）（https://registry.modelcontextprotocol.io/v0/servers?search=video）
- **2026-09-11（仓库创建日）** — Runway 成为视频生成厂商中第一家上官方托管 MCP 的：mcp.runwayml.com/mcp（Streamable HTTP + OAuth 2.1/PKCE 免 API key），配套 Cursor/Grok 官方插件与两个官方 SKILL.md（runway-media 单发生成、runway-workflows 多步工作流图），并在工具描述里明示会消耗计划内 credits（https://github.com/runwayml/runway-mcp-plugin）
- **2026-09-17（文档最后更新）** — Google 把 Gemini 视频理解升级为 agentic 能力：模型自主导航视频时间线、按需调阅转写、动态调帧率与分辨率，官方称最高省 88% token 且长视频质量约 +7%；静态采样 1FPS/66 token 每帧，1M 上下文下低清 3 小时/高清 1 小时，支持 YouTube URL（单请求 10 条）；文档导航同时出现 Gemini Omni Flash 视频生成指南入口（看+生成收拢进同一 API 面）（https://ai.google.dev/gemini-api/docs/video-understanding）
- **2026-09-22 查证（现行文档）** — OpenAI Sora 2 API 现行契约：POST /videos 创建 + GET /videos/{id} 轮询（10-20 秒间隔）+ video.completed/video.failed webhook，sora-2/sora-2-pro 支持 16/20 秒，characters（角色一致性）、extensions（续接）、edits 端点，remix 端点废弃中；官方建议用 Batch API 跑 shot lists，但无任何分镜端点、无判片/验收能力、页面不展示每秒定价（https://developers.openai.com/api/docs/guides/video-generation）
- **2026-09-22 查证（页面日期 2026-09-17）** — Twelve Labs 产品化视频理解：Pegasus 1.5（号称对 2 小时内资产做全时程推理，自称多模态 prompt 超 Gemini 3.1 Pro 13.1%）+ Jockey『首个视频智能 agent』+ 60 倍实时摄取管线；官网接入方式出现 MCP tab（与 API+SDK 并列）——但它面向媒体库检索/合规/集锦，不面向 AI 生成片的验收（https://www.twelvelabs.io/）
- **2026-09-22 查证** — Claude API 确认无视频输入：仅支持 JPEG/PNG/GIF/WebP 静态图，GIF 动图『不支持动画、只取第一帧』，FAQ 明确 Claude 只能理解不能生成/编辑图像——围绕 Claude 的视频判片必须自行抽帧（https://platform.claude.com/docs/en/build-with-claude/vision）
- **2026-09-22 查证** — Anthropic 官方 skills 仓库 19 个 skill（mcp-builder、skill-creator、文档三件套等）无一与视频生成/分镜/判片相关——视频管线在 Agent Skill 层完全空白（https://github.com/anthropics/skills）
- **2026-09-22 查证** — LTX Studio（已迁至 ltx.io）把 scripting→storyboarding→shot 控制→角色/场景一致性→剪辑交付全流程内化进封闭平台，同时开源 LTX-2/2.5 多模态模型权重与训练框架引流；平台无开放 API 的分镜契约（https://ltx.io/studio）
- **2026-09-18（最近更新）** — fal 无官方 MCP 的现状由社区补位：第三方 luminarylane/fal-mcp-server（56 星）是『fal MCP』事实标准，另有多个 0-4 星同类——官方 registry 与 fal 官方渠道均无第一方 server（https://github.com/luminarylane/fal-mcp-server）
- **2026-09-16（最近更新）** — 社区开始做『分镜+片段拼接』工作流 MCP：honestTai/seedance-movie-mcp 在火山方舟 Seedance 上实现分镜与片段拼接编排——这类管线层工作没有厂商官方版本（https://github.com/honestTai/seedance-movie-mcp）
- **2026-09-11（最近更新）** — 第三方多厂商聚合网关出现：Saga-Labs/dora-mcp 把 Veo 3、Kling 2.6、SeeDance 2、Grok Imagine 等 16 个模型收进单一 OAuth 端点，并『生成前先返回各模型成本』——反证主流厂商 API 未把成本预估做成一等公民（https://github.com/Saga-Labs/dora-mcp）
- **2026-09-21（最近更新，2025-09~11 为权重发布期）** — Qwen3-VL 能力边界确认：原生 256K 上下文可扩至 1M、hours-long 视频全回溯+秒级时间戳索引、默认 fps=2 采样、开源全尺寸权重（2B~235B-A22B）——判片层的开源原料免费可得（https://raw.githubusercontent.com/QwenLM/Qwen3-VL/main/README.md）
- **2026-09-22 查证（最新动态为 2026-03 I2V Arena）** — VBench 系（VBench/VBench++/VBench-2.0）仍是判片研究层事实标准：16+ 维度（时序闪烁、运动平滑、主体一致性、物理真实性等）、1.8k 星、pip 可装、含 18 万条 40 余模型生成片的 Arena——但没有任何商用 API 或托管服务（https://github.com/Vchitect/VBench）

### Roadmap 信号

- **Runway 把 agent 分发当一等渠道：官方托管 MCP + Cursor/Grok 插件市场 + 官方 skills 于 2026-09-11 同步上线，README 写明『无需 API key、用现有 Runway 计划扣费』——API→agent 直连是其未来 6-12 个月的明确投入方向，其余厂商大概率跟进**（置信：官方明示；https://github.com/runwayml/runway-mcp-plugin）
- **Google 在把『看视频』和『生成视频』都收拢进单一 Gemini API 面：视频理解文档 agentic 化（自导航时间线/自适应帧率与分辨率，2026-09-17 更新），文档导航出现 Gemini Omni Flash 视频生成指南入口**（置信：官方明示；https://ai.google.dev/gemini-api/docs/video-understanding）
- **OpenAI 把 Sora API 收敛成无人值守渲染农场契约：remix 废弃并入 edits、新增 characters 角色一致性与 extensions 续接、官方建议 Batch API 跑 shot lists、webhook 覆盖 completed/failed——方向是批量管线，但官方明确不做分镜与判片，留白给上层工具**（置信：官方明示；https://developers.openai.com/api/docs/guides/video-generation）
- **判片/验收与重试决策层将由第三方补齐：官方 Registry 13 个 video server 全是小厂，社区已在卷多厂商聚合（dora-mcp 16 模型 OAuth 网关+成本预告）与分镜拼接工作流（seedance-movie-mcp），无任何主流厂商官方覆盖『生成后自动验收』**（置信：多源交叉；https://registry.modelcontextprotocol.io/v0/servers?search=video）
- **Anthropic 短期不会官方支持视频输入/判片：Claude vision 文档只覆盖静态图且 GIF 只取首帧，官方 skills 里也无视频方向——围绕 Claude 的视频工作流必须自行抽帧，这个抽帧+判片粘合层没有官方竞争者**（置信：官方明示；https://platform.claude.com/docs/en/build-with-claude/vision）
- **视频理解厂商正向 agent 生态输送能力：Twelve Labs 官网接入方式出现 MCP tab（与 API+SDK、Integrations 并列），且 Jockey 定位为视频智能 agent——判片所需的 VLM 原料会越来越容易从第三方获取**（置信：多源交叉；https://www.twelvelabs.io/）
- **Lightricks 走『封闭平台+开源模型』双轨：LTX Studio 平台内化全流程，LTX-2/2.5 权重与训练框架全开源——开源权重供给会持续放大自部署判片/生成管线的可行性**（置信：官方明示；https://ltx.io/studio）

### 做得好的

- Runway 官方 agent 全家桶是行业样板：托管 MCP + OAuth 2.1/PKCE（用户免 API key）+ 官方 SKILL.md 教 agent 处理上传/长任务/选工具 + 工具描述里明示扣 credits——把 CLI 作者最头疼的『异步等待、鉴权、计费告知』都替 agent 想好了，值得直接对标
- OpenAI Sora 2 API 的异步契约干净完整：创建/轮询/webhook(video.completed、video.failed)/下载内容四件套 + Batch API 官方支持 shot lists + 库管理端点（list/delete），是『长任务状态机』的清晰参考实现
- Google 的 agentic video understanding 把『用 VLM 看视频』的成本工程做到可用：模型自主决定看哪些时间段/抽哪些帧/何时读转写，88% token 节省让『每条生成片都过一遍 VLM 判片』在经济上成立——这是判片层能产品化的前提
- Twelve Labs 验证了视频理解层的付费需求（NFL 等客户、60 倍实时摄取、search/summarize/highlight/embed 全套 API），且已开始向 agent 生态开放（官网 MCP tab）
- Qwen3-VL 开源权重（2B~235B）+ 秒级时间戳索引 + hours-long 视频，让独立开发者可以零成本自部署判片模型，不被 API 定价绑架
- LTX-2/LTX-2.5 开源权重+训练框架公开，训练侧开源供给充足，自部署路线可行
- VBench 把判片维度学理化（16+ 维度、VBench-2.0 物理真实性），可直接借为 CLI 验收 rubric，不用自己发明评分体系

### 空位与切入姿势

- **生成后自动判片/验收层无人产品化——这是最大的空位**
  - 证据：VBench 系只有 pip 包和 leaderboard（GitHub 明确无商用 API）；OpenAI Sora 2 API 指南全文无任何 judging/验收能力（抓取结论原话：Video understanding/judging: Not mentioned anywhere）；各厂商 API 统一只返回 queued/in_progress/completed/failed，『片子有没有把 prompt 里的动作做对』没有任何结构化输出；Twelve Labs 的理解能力面向存量媒体库而非生成片验收
  - 切入：在 CLI 里做一等的 judge 步骤：抽帧→喂 Gemini/Qwen-VL→按 VBench 维度输出结构化 JSON verdict（运动一致性/文字渲染/物理合理性/与原 prompt 对齐度）+ 每厂商通过阈值；契约里生成与验收同权重，这是 fal/AtlasCloud/Higgsfield/Runway 全都没做的一层
- **失败重试决策无标准、无工具**
  - 证据：Sora 提供 video.failed webhook 但只到『失败』为止，全行业没有 failure taxonomy（内容违规 vs 参数错 vs 模型随机抽风），『要不要重试、换什么参数重试』完全甩给调用方
  - 切入：CLI 定义跨厂商失败分类学 + 策略化重试（降时长/换模型/改 prompt 后重投），把 9 个厂商各自的 failed 语义归一成同一份 JSON——契约优先 CLI 的天然卖点
- **视频生成厂商官方 MCP 仅 Runway 一家，agent 分发渠道严重缺位**
  - 证据：官方 Registry 13 个 video server 无一主流厂商；fal 官方 MCP 不存在（最高星为第三方 56 星）；Luma/Kling/海螺/Vidu/Pika 均无官方 server；社区已经在用最脏方式补位（pixelle-video-mcp-server 用 Playwright 驱动 GUI 生成视频）
  - 切入：做『非官方但契约化』的多厂商聚合 MCP/CLI 抢先占位——Runway 官方 2026-09 刚进场的动作证明这个形态是厂商公认的下一步，独立开发者可以比其余厂商的官方团队早半步
- **Agent Skill 层完全空白**
  - 证据：anthropics/skills 官方 19 个 skill 无一视频相关；全网唯一官方视频 skills 是 Runway 为自己 MCP 写的两个（只覆盖 Runway）——没有跨厂商『分镜→生成→判片→拼接』的通用 SKILL.md
  - 切入：写一个 vendor-agnostic 的 video-pipeline SKILL.md 绑自家 CLI：教 agent 用统一 JSON 契约跨 9 家厂商编排，Runway 已示范 SKILL.md 该怎么写（含异步与 credits 处理），照着标准做跨厂商版
- **LLM 剧本→分镜与开放生成 API 之间断链，分镜无契约标准**
  - 证据：LTX Studio/Google Flow 把分镜锁在封闭 GUI；OpenAI 官方指南对分镜的唯一建议是『用 Batch API 跑 shot lists』但没有 shot list 格式标准；Sora remix 端点废弃、无 storyboard 端点
  - 切入：定义可版本化的分镜 JSON 契约（镜头/角色/连贯性约束/每镜目标厂商与参数），CLI 把任意 LLM 生成的分镜编译成多厂商生成任务——把 LTX Studio 的封闭体验开放化，正是契约优先路线的核心场景
- **提示词扩写是服务端黑盒、不可插拔**
  - 证据：fal 的 prompt upsampler 绑定自家模型服务端执行，Luma/Kling 的『自动增强』是开关不是管线节点，没有厂商暴露扩写前中间表示，也不允许外部 LLM 扩写后保持契约字段完整
  - 切入：CLI 提供 pluggable prompt-expander：接任意 LLM 扩写，输出同时保留结构化字段+扩写后 prose，判片时可对回用户原始意图——扩写从厂商私有特性变成管线一等节点
- **计费透明度参差，成本预估不是一等公民**
  - 证据：OpenAI 视频指南页面不展示每秒定价（抓取确认 pricing: Not shown）；Runway 只在 MCP 工具描述里口头声明扣 credits；第三方 dora-mcp 把『生成前先返回各模型成本』当核心卖点，反证主流厂商没做好
  - 切入：CLI 的 dry-run 契约字段：每条任务在提交前返回各厂商预估成本+预计时长，跨厂商比价后再投递
- **开源模型（训练侧）与托管 API 之间无统一契约工具**
  - 证据：LTX-2/2.5、Wan、Qwen-VL 等开源权重+训练框架公开可自部署，但没有任何工具让自部署端点与托管 API 共用同一份请求/判片契约；社区甚至 resort 到 Playwright 驱动网页 GUI
  - 切入：同一 CLI 契约下可切换 hosted API 与自部署 vLLM/ComfyUI 端点，判片 rubric 对两者一视同仁——独立开发者用开源权重压成本、用托管 API 冲质量的混合路线目前无人铺路

### 未解问题

- Google Flow/Veo 的 Scenebuilder、Ingredients to Video、Frames to Video 等分镜功能现状与 90 天内更新未能核实——flow.google.com 只返回登录页，需登录后或从 help 文档验证
- Gemini Omni Flash 视频生成指南的模型细节、定价与 GA 状态——本次只确认了官方文档导航入口存在，未读指南正文
- OpenAI Sora 2 / sora-2-pro 的每秒定价——视频指南页不展示，pricing 页未抓取
- Qwen 侧 90 天内（2026-06 后）是否有视频生成+理解联动的新发布——qwenlm.github.io 已迁移至 qwen.ai，新站未抓取
- Kling/海螺/Vidu/Higgsfield/Pika/ElevenLabs 在 90 天内是否发布过 MCP 或 agent 接入——本次依赖既有并行调研结论，未逐一重抓一手页面
- Twelve Labs 官网 MCP tab 的具体内容（工具清单、覆盖哪些能力）——tab 无详情，需注册或查其文档
- 主流厂商是否在内部悄悄用 VLM 自检后才返回结果（quietly served）——无公开一手证据，只能确认对外 API 契约里没有验收层
- Remotion 是否有未发布到博客的 agent/MCP 计划——docs/ai/plugins 路径存在但本次未深挖

### 来源

- [MCP Official Registry — video search results](https://registry.modelcontextprotocol.io/v0/servers?search=video)
- [modelcontextprotocol/servers — reference & archived servers](https://github.com/modelcontextprotocol/servers)
- [runwayml/runway-mcp-plugin — 官方托管 MCP + skills](https://github.com/runwayml/runway-mcp-plugin)
- [Gemini API — Video understanding（agentic，2026-09-17 更新）](https://ai.google.dev/gemini-api/docs/video-understanding)
- [OpenAI — Video generation with Sora（developers.openai.com 现行指南）](https://developers.openai.com/api/docs/guides/video-generation)
- [Claude Docs — Vision（无视频输入，GIF 只取首帧）](https://platform.claude.com/docs/en/build-with-claude/vision)
- [QwenLM/Qwen3-VL README — 能力边界与发布时间线](https://raw.githubusercontent.com/QwenLM/Qwen3-VL/main/README.md)
- [Vchitect/VBench — 判片研究层事实标准](https://github.com/Vchitect/VBench)
- [Twelve Labs 官网 — Pegasus 1.5 / Jockey / MCP tab](https://www.twelvelabs.io/)
- [LTX Studio（ltx.io）— 全流程平台 + LTX-2 开源](https://ltx.io/studio)
- [anthropics/skills — 官方 skills 仓库（无视频类）](https://github.com/anthropics/skills)
- [luminarylane/fal-mcp-server — 第三方 fal MCP（56 星）](https://github.com/luminarylane/fal-mcp-server)
- [honestTai/seedance-movie-mcp — 火山方舟分镜拼接社区 MCP](https://github.com/honestTai/seedance-movie-mcp)
- [Saga-Labs/dora-mcp — 16 模型聚合 OAuth 网关](https://github.com/Saga-Labs/dora-mcp)
- [Samge0/pixelle-video-mcp-server — Playwright 驱动 GUI 生成视频](https://github.com/Samge0/pixelle-video-mcp-server)
- [Glama MCP 目录 — video generation servers](https://glama.ai/mcp/servers?query=video+generation)

---
