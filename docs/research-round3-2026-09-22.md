# 第三轮全域调研 · 需求侧 / 下游行业 / 技术前沿 / 开源生态（2026-09-22）

> 方法：8 路 schema 约束 agent 真实网络检索（2 波 × 4 路并行，run wf_924b570c，8/8 零失败，292 次工具调用）。
> 前瞻纪律：只收 2026-06-22 后信号；每条关键结论带 source_url 与置信度（官方源/多源交叉/单一来源/推断）；商业数字注明未经审计。
> 需求侧两路（workflows/pain_points/willingness_to_pay）回答"谁在买单、骂什么"；行业三路回答"钱在哪"；前沿与开源两路回答"未来约束什么设计"。


## 需求侧 · 开发者/创作者社区痛点（HN/Reddit/GitHub 一手）

**摘要**：90 天窗口（2026-06-22 后）需求侧信号集中三层。工作流：开发者用 Claude Code 当"导演"，把 Seedance/Kling/Veo 与 Nano Banana、ElevenLabs、ffmpeg 粘成管线，并自建轮询、断点续跑、机检 QC（GitHub 90 天内出现至少 8 个视频 API 轮询/包装仓库，最高 788 星）；聚合层密集上线（VideoRouter、Velokey、useapi、APIMart），卖点均为统一 API+failover+比价。痛点频率：重生成成本与可用率放大、角色一致性漂移、轮询/并发上限自建轮子属"反复出现"；审核门槛与真脸企业授权（约 $14k/年）、API 碎片化+转售溢价（最高较官方 +82%）属"多次出现"。付费意愿：$200/部 10 分钟短片被公开接受，$15/30s 被明确骂贵，$300/月先享包有人买。限制：Reddit/X/知乎掘金抓取被拒，已如实列入 open_questions。

### 观察到的真实工作流

- **dawndrain（HN 用户，独立开发者）**（置信度：官方源）  
  管道：Claude Code 任导演的 10 分钟 AI 电影管线：Claude 拆剧本/提交任务/QC/组装，人只管账号与导演笔记；自建 gen.py（处理 Higgsfield 8 任务并发上限）、pool_run.py（跳过已完成镜头=断点重试）、assemble.py、dub_clip.py（换台词不重渲视频）、pitch_check/listen.py（语音 QC）。一版约 2.5 小时、约 $200  
  工具：Seedance 2.0（经 Higgsfield CLI）、Nano Banana Pro、ElevenLabs、Sonilo（配乐）、Gemini（视/听 QC）、ffmpeg  
  来源：<https://github.com/dawndrain/movie-gen>
- **lixiaoxiao9888-create（中文 AIGC 短剧团队，788★ 仓库作者）**（置信度：官方源）  
  管道：把国内 AIGC 短剧生产固化为 agent 规则库：立项锁参数→五阶门控编剧→资产锁定（角色 4 View 资产板+台账）→分镜→提示词封装→validate_prompt.py 机检（C1~C20，FAIL 清零才交付）→独立质检。Seedance 2.5/2.0 强制二选一，MiniMax H3 做格式支线，即梦次选，可灵已降级 LEGACY  
  工具：Seedance 2.5/2.0、MiniMax H3、即梦、OpenClaw/WorkBuddy/豆包 Coze/Dify、Python 机检脚本  
  来源：<https://github.com/lixiaoxiao9888-create/manju-laoli-skill>
- **liyue-aigc（中文创作者，371★ 仓库作者）**（置信度：官方源）  
  管道：Dreamina/即梦上的提示词编排：整理参考图+分镜为可执行视频脚本，用提示词结构实现角色锁定（保身份五官、剥离背景姿势），并对旧提示词做时间/运镜/人物/物理/声音冲突诊断（只诊断不重写、不自动提交任务）  
  工具：Seedance 2.5（经 Dreamina/即梦）、提示词模板+诊断器  
  来源：<https://github.com/liyue-aigc/seedance-2-5-video-director>
- **letorig（开源作者，542★）**（置信度：官方源）  
  管道：统一异步 Python 客户端聚合四家视频 API：每家一个 provider adapter，CLI 提交/查状态，FastAPI 本地 Web UI 做任务轮询+MP4 下载+会话内任务历史，另含 MCP server 目录。README 明言动机是多家 API 碎片化，且'各家 API 与模型 ID 独立变动'  
  工具：Seedance 2.5/2.0/Kling 3.0/MiniMax H3/Wan 3.0、Python asyncio、FastAPI、MCP  
  来源：<https://github.com/letorig/video-generator-client>
- **《The Cully Hill Boys》剧组（110 分钟 AI 长片，HN 用户 whythismatters 转述片尾字幕）**（置信度：单一来源）  
  管道：全片每一帧用 Seedance 生成（含所有台词语音），真演员签约授权但零实拍；脸部/character sheets 用 Soul Cinema，反打镜头与改点用 Seedream+Nano Banana，提示词由 Claude 在两个会话分别生成（图/视频）  
  工具：Seedance（视频+语音）、Soul Cinema、Seedream、Nano Banana、Claude  
  来源：<https://news.ycombinator.com/item?id=49484677>
- **gunwooterry 转述其 VFX 朋友圈（HN 评论）**（置信度：单一来源）  
  管道：专业 VFX 从业者把 Seedance 与 Beeble（SwitchX 模型）串联做演员表演迁移  
  工具：Seedance、Beeble SwitchX  
  来源：<https://news.ycombinator.com/item?id=49138302>
- **GitHub 90 天内自建任务基建的群体（≥8 个仓库）**（置信度：官方源）  
  管道：各自重写同一套任务基建：sam12-4/video-generation-api（job submission+async lifecycle+status polling+webhook callbacks）、Seemerry/video-generation-skill（Claude Code 技能内自动轮询）、marswon/workbuddy-gettoken-seedance-skill（轮询+下载+断点续批分镜）、Cadmusyiu/kling-gen（JWT+轮询+上传下载）、Anil-matcha/Wan-3.0-Prime-API（SDK+MCP）、abuzar-tech007（Replicate+polling）、outstand-agency/vibes-api（非官方 FastAPI 包 private API+自建 Cloudflare R2 存储）  
  工具：Python/FastAPI、polling、webhook、MCP、Cloudflare R2  
  来源：<https://api.github.com/search/repositories?q=%22video+generation%22+%22polling%22+created:%3E2026-06-22>
- **franklin_yao（VideoRouter 作者）与 Velokey、useapi.net、APIMart 等聚合层开发者**（置信度：官方源）  
  管道：视频版 OpenRouter 密集上线：VideoRouter 统一 Sora/Kling/Veo/MiniMax/Wan/Hunyuan/Seedance 等 15+ 模型，底层在 Fal、WaveSpeedAI、Atlas Cloud、Replicate、Novita 间比价路由+健康检查故障转移+预算告警，收 2% 平台费；Velokey 一个 API 覆盖 Kling/Veo/Seedance/Sora（OpenAI 兼容、自动 failover、Seedance 2.0 $0.29/s）；useapi 用 $15/月订阅+消费端积分（PixVerse/Runway/Dreamina/MiniMax）绕开开发者 API 定价；APIMart 打折聚合但被 HN 评论质疑代理池  
  工具：统一网关、OpenAI 兼容 SDK、failover、比价路由  
  来源：<https://videorouter.sh>
- **dagaci（HN 评论者）**（置信度：单一来源）  
  管道：ComfyUI 工作流+本地提示词扩写小模型再接 raw 视频 API（与 MiniMax H3 对比时被指不公平但真实存在）  
  工具：ComfyUI、本地 LLM、raw API  
  来源：<https://news.ycombinator.com/item?id=49138302>

### 痛点（按频率分级）

- **重生成成本被'可用率'放大：$15/30s 定价下 userbinator 推算 $1800/小时、按 1/10 可用率即 $18000/小时成品；rudolftheone 指出不一致/物理错误的 retake 让实际成本远高于标价；Genego 自述 5 万+分镜图花费 $10k+ 推理费；dawndrain 分享'两次改词失败就换内容'的重试铁律**〔反复出现〕  
  机会：按'可用镜头'而非'生成次数'计费的成本核算工具、成品级智能重试策略、重生成预算熔断  
  证据：<https://news.ycombinator.com/item?id=49138302>
- **角色/资产跨镜漂移：中文团队为此发明 Asset-First（先出 4 View 角色资产板再分镜）与首镜单主体禁并列句式；liyue-aigc 专门做角色锁定与身份漂移诊断；ada1981 在 VideoRouter 帖追问'Seedance 2.5 配 reference images/char sheets 能不能跑通'；长片剧组外购 Soul Cinema 出 character sheets**〔反复出现〕  
  机会：跨模型角色资产库+一致引用编译层，把各家 reference/char-sheet 能力差异抹平  
  证据：<https://github.com/lixiaoxiao9888-create/manju-laoli-skill>
- **任务轮询/并发上限/断点续跑全靠自建：官方 API 限 3 并发任务（4K 仅 1 个）、Higgsfield 限 8 任务，90 天内 GitHub 出现至少 8 个专写 polling/resume/webhook 的个人轮子；聚合商卖点第一条全是 failover**〔反复出现〕  
  机会：统一异步任务层（轮询抽象+webhook+断点续跑+跨厂商并发调度），已被至少三家商业产品验证需求  
  证据：<https://api.github.com/search/repositories?q=%22video+generation%22+%22polling%22+created:%3E2026-06-22>
- **内容审核与权利门槛不对称：官方 API 真脸引用被锁进约 $14k/年起企业授权（转述，未经审计）；jarjoura 指出 Google/xAI 因 deepfake 把引用生成限 720p 并禁音频同步，Seedance 对持证制作公司另有通道；国内团队手工维护'安全转译词典'（血腥→'气浪震散'）且'不承诺 100% 通过'；echelon 称 Seedance 2.0 少过滤后被 IP 方施压收紧**〔多次出现〕  
  机会：审核预检中间件/合规转译工具/授权工作流自动化，衔接企业权利层与个人开发者  
  证据：<https://useapi.net/docs/articles/seedance-2-api-pricing>
- **API 碎片化+转售价差离谱：useapi 实测 16 家中官方 BytePlus $1.87/5s 1080p，fal $3.41（+82% 溢价）仍是市场默认，Replicate $2.25，仅 Segmind $1.70 低于官方；低价幌子普遍是 720p 报价/turbo 蒸馏版/无美元锚定积分**〔反复出现〕  
  机会：分辨率/变体对齐的透明比价+统一接入；注意 useapi 文档有利益相关，数字需独立复核  
  证据：<https://useapi.net/docs/articles/seedance-2-api-pricing>
- **模型固有质量缺陷：定长填充导致角色'说完台词僵住等笑点'（arjie/sheept）、静止表演不可用与时长注水（manju-laoli C15 时长守恒门+静止段禁用铁律）、长镜头漂移（bobkb 称 Kling 做不到）、物理与地标错误、整体'AI 感'（sickcodebruh/efficax/orbital-decay）**〔反复出现〕  
  机会：自动化 QC（Gemini 视检、F0 语音筛查、C1~C20 机检已有手工先例）+缺陷定向重生成  
  证据：<https://news.ycombinator.com/item?id=49138302>
- **提示词语法碎片化+否定词失效：'视频模型对否定不敏感、对词根敏感'，禁令'哪怕挂着不/禁也会被渲染'，需禁令失效三改法；各模型语法契约不同需'彻底分流'+H3 六段式自动转换**〔多次出现〕  
  机会：跨模型提示词编译器（一份创意编译到各家语法契约，含否定改写）  
  证据：<https://github.com/lixiaoxiao9888-create/manju-laoli-skill>
- **API 早期访问门槛与区域锁：Seedance 2.5 公开 API 前需 $300/月 Lumina 企业包（burgeekingdom 在 HN 追问'有人真拿到 API 了吗'）；官方要求 $30.10 不退款预付包；Dreamina 1080p/4K 锁加拿大区账号；Runway 旧免费档新账号不可用且 10-15 分钟/条**〔多次出现〕  
  机会：全球可用的正规转售+一致 SLA+低门槛试用  
  证据：<https://news.ycombinator.com/item?id=49206655>
- **音画同步/口型故障：liyue-aigc 把'对白音色、BGM 移除与声画同步'列为核心功能即是佐证；dawndrain 专门写 dub_clip.py 换台词不重渲视频；Google/xAI 直接禁音频同步**〔多次出现〕  
  机会：后期音轨替换/对口型管线作为独立工具  
  证据：<https://github.com/dawndrain/movie-gen>
- **产物存储与链接时效：vibes-api 特意自建 Cloudflare R2 存产物；movie-gen 媒体刻意不入 git（'credits permitting'可再生），隐含产物托管与再生成成本顾虑**〔个例〕  
  机会：产物托管+内容寻址缓存，避免重付费  
  证据：<https://github.com/outstand-agency/vibes-api>

### 付费意愿信号

- $200/部 10 分钟短片被作者公开接受并当作卖点（约 80 个镜头、15 轮迭代），但评论区立即质疑'LLM 补贴结束后会更贵'——付费意愿真实存在、对成本曲线敏感
- $15/30s（Seedance 2.5 经 Dreamina 1440 credits）被早期采用者 JimsonYang 明确拒绝升级：'不值得双倍变量成本'——$0.25-0.5/s 是心理关口
- $300/月 Lumina 企业包有人为提前拿到 Seedance 2.5 API 而付费（JimsonYang 自述）
- 约 $14k/年 的真脸引用企业授权作为官方定价存在（useapi 转述，未经审计）——高端授权市场被官方锁定
- fal.ai 较官方溢价约 82% 仍被称为'市场默认'——为可靠性与 UX 支付高溢价的直接证据（useapi 文档，利益相关）
- 个人创作者 Genego 自述花费'upwards of $10k on inference'产出 5 万+分镜图——万元级个人支出已出现
- HN 出现'$100 AI Music Video'制作帖（Claude Fable 5 vs GPT-5.6 Sol），前两段镜头用 Kling 生成——百元级内容制作场景成型
- useapi $15/月订阅+消费积分模式用'绕开开发者 API 定价'获客——价格敏感用户愿为省钱付小额订阅
- 聚合层资本市场验证：HN 评论转述 Stripe 以 $7B+ 收购 OpenRouter、fal 以 $8B 估值融资（媒体口径，未经审计）——统一接入层价值被市场认可

### 机会清单

- 统一异步任务层：轮询/webhook 抽象+断点续跑+跨厂商并发调度（官方 3 并发、Higgsfield 8 并发是硬约束；90 天内 ≥8 个个人轮子+3 家商业产品同向验证）
- 跨模型角色/资产一致性层：character sheet 资产库+引用编译，抹平各家 reference 能力差异（Asset-First、Soul Cinema、角色锁定均为手工先例）
- 透明比价+统一路由：分辨率/变体对齐的真实价格目录，2% 平台费已被 VideoRouter 定为可行锚点，82% 溢价是定价空间上限参照
- 审核预检/合规转译中间件：把国内团队手工'安全转译词典'产品化，衔接 $14k/年 企业授权与个人开发者之间的断层
- 自动 QC+定向重生成：视检（Gemini）、语音筛查（F0）、规则机检（C1~C20）已有手工方案，可产品化为'FAIL 清零才交付'的成品级质量门
- 按'可用镜头'口径的成本可观测性与预算熔断：用户思维已从 credit 转向成品可用率，工具仍停留在 credit 计数
- 跨模型提示词编译器：一份创意编译到各家语法契约，自动处理否定词失效与段缝衔接

### 未决问题

- Reddit r/aivideo、r/StableDiffusion、r/videogenesis 无法取证：www/old.reddit 及 r.jina.ai 代理三次尝试均 403 反爬拦截，Reddit 侧痛点频率未经一手验证（本次 WebSearch 配额也已耗尽）
- X/indie hackers 的 build-in-public video AI builder 未能检索（无搜索预算+平台封锁），该渠道样本缺失
- 知乎/掘金/即刻等中文社区直接抓取被拒（掘金 ECONNREFUSED、API 429），中文侧证据主要来自 GitHub 中文仓库（788★/371★ 等），缺社区讨论原文
- HN 搜 'kling' 大量命中 Ladybird 开发者 Andreas Kling 而非可灵 AI，可灵 API 的开发者抱怨样本偏少，其痛点覆盖可能低估
- 商业数字均未经审计：$14k/年 企业授权、OpenRouter $7B+ 收购价、fal $8B 估值、$3B 融资（SCMP 引述'消息人士'）皆为转述或利益相关方文档口径
- useapi.net 的 16 厂商比价为聚合商自家文档（利益相关），fal +82% 溢价等数字需独立复核
- bucketkingdom（'有人真拿到 Seedance 2.5 API 吗'）等访问门槛抱怨只有单条 HN 评论，缺系统性统计

### 来源

- [HN: Seedance 2.5（442 分/255 评论主讨论帖）](https://news.ycombinator.com/item?id=49138302)
- [HN: Tell HN - Seedance 2.5 API Pricing](https://news.ycombinator.com/item?id=49170050)
- [useapi.net: Open pricing dataset for the Seedance 2.0 API, across 16 vendors](https://useapi.net/docs/articles/seedance-2-api-pricing)
- [GitHub: dawndrain/movie-gen（Claude Code+Seedance 电影管线）](https://github.com/dawndrain/movie-gen)
- [GitHub: lixiaoxiao9888-create/manju-laoli-skill（中文短剧工业化规则库，788★）](https://github.com/lixiaoxiao9888-create/manju-laoli-skill)
- [GitHub: liyue-aigc/seedance-2-5-video-director（角色锁定+诊断，371★）](https://github.com/liyue-aigc/seedance-2-5-video-director)
- [GitHub: letorig/video-generator-client（异步统一客户端，542★）](https://github.com/letorig/video-generator-client)
- [GitHub API: video generation polling 轮子搜索（90 天 7 仓）](https://api.github.com/search/repositories?q=%22video+generation%22+%22polling%22+created:%3E2026-06-22)
- [GitHub API: seedance 新建仓库搜索（90 天 8761 仓）](https://api.github.com/search/repositories?q=seedance+created:%3E2026-06-22)
- [VideoRouter 官网（视频版 OpenRouter，2% 费率）](https://videorouter.sh)
- [Velokey 官网（One Task API，Seedance $0.29/s）](https://velokey.ai)
- [HN: VideoRouter – OpenRouter for video and image generation APIs（含 ada1981 角色一致性追问）](https://news.ycombinator.com/item?id=49733974)
- [HN: Show HN - Seedance 2.5 video API on Atlas Cloud（含访问门槛追问）](https://news.ycombinator.com/item?id=49206655)
- [HN: The Cully Hill Boys – 110 minute AI film（全 Seedance 工作流转述）](https://news.ycombinator.com/item?id=49484677)
- [HN: Show HN - A Pipeline for Making 10-minute AI Movies（$200/2.5h 讨论串）](https://news.ycombinator.com/item?id=48978961)
- [HN: APIMart 折扣聚合器（代理池质疑）](https://news.ycombinator.com/item?id=49299000)
- [GitHub: outstand-agency/vibes-api（非官方 wrapper+R2 自建存储）](https://github.com/outstand-agency/vibes-api)
- [HN Algolia API: seedance 评论检索（90 天 65 条）](https://hn.algolia.com/api/v1/search_by_date?query=seedance&tags=comment&numericFilters=created_at_i%3E1782259200)
- [HN: Seedance 2.5 官方公告（ByteDance SEED 博客）](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5)
- [SCMP: Kling AI nears US$3B round at US$18B valuation（转述，未经审计）](https://www.scmp.com/tech/big-tech/article/3359059/chinas-kling-ai-nears-us3-billion-round-us18-billion-valuation-sources)


## 需求侧 · 单位经济学（谁真的在赚钱）

**摘要**：90天窗口内，视频生成需求侧的钱流向两类：①模型/平台层——可灵Q2收入同比+200%（快手Q2营收355.4亿）、可灵$18B估值融资$2.8B、Runway与HeyGen各达$200M ARR（多源）；②电商广告素材——AI UGC单条$1-11 vs 真人$185-2000，50条AI变体<$200 vs 真人$7,500+，品牌按$29-220/月订阅付费。被证伪的是无脸YouTube slop变现：YouTube 7月起对"批量生产/重复"内容去货币化，Flippa在售AI视频站MRR低至$19-2.3K且多为自报。价格两极：海外厂商涨价（DoNews称Runway gen4_turbo涨至$0.45/5s，与官方页$0.25冲突待核）、中国价格战+补贴（PixPix亿元补贴）、开源权重（MiniMax H3可跑3090）压垮转售套壳站（Libtv一折甩卖Seedance被字节封禁）。结论：服务电商素材批量管道与成本敏感开发者，勿做slop变现流。

### 观察到的真实工作流

- **欧美DTC/电商品牌**（置信度：单一来源）  
  管道：AI UGC广告素材批量生产：订阅混合工具栈，单批生成30-50条变体投Meta/TikTok，以量补质  
  工具：Creatify($39-99/月)/HeyGen($29-49/月)/Arcads($110-220/月，=$11/条)/Captions  
  来源：<https://okaneland.com/study/ai-ugc-ad-economics/>
- **Faceless YouTube频道运营者（全球，中英均有）**（置信度：官方源）  
  管道：Claude Code/开源流水线批量生成shorts：90天新增158个相关GitHub repo（最高252★）；印度成熟工作室按₹5,000-15,000/条接单，头部与长尾收入差距拉大  
  工具：Claude Code skills+Remotion+ElevenLabs+ffmpeg  
  来源：<https://github.com/hassancs91/claude-faceless-shorts-creator>
- **中国工具站/套壳站**（置信度：单一来源）  
  管道：低价转售模型API抢单：Libtv以约1折甩卖Seedance 2.5被字节封禁；PixPix以4.6折+亿元补贴抢电商客户——毛利被上游定价击穿  
  工具：Seedance 2.5 API（火山引擎）/订阅转售  
  来源：<https://36kr.com/search/articles/Libtv>
- **AI视频模型厂商**（置信度：多源交叉）  
  管道：订阅+API双轨商业化：可灵Q2收入+200%、$18B估值融资$2.8B（阿里/腾讯）；Runway 9月跨$200M ARR；HeyGen 6月官宣$200M ARR；海外涨价vs中国降价的分化定价  
  工具：自有API（可灵/Runway/HeyGen/MiniMax H3）  
  来源：<https://wallstreetcn.com/articles/3779792>
- **独立开发者（个人/小团队）**（置信度：单一来源）  
  管道：为控成本弃用AI视频API改用Remotion程序化渲染（HN 2026-08-11原话：'not as expensive as using an AI video model like Veo'）；或等开源权重自托管——MiniMax H3开源后跑3090级消费GPU（AMD day-0支持）  
  工具：Remotion/MiniMax H3 open weights/ComfyUI  
  来源：<https://news.ycombinator.com/item?id=49259309>
- **网站买家/套壳创业者**（置信度：单一来源）  
  管道：Flippa买卖AI视频SaaS站：videogenr（MRR $19，要价$979）、AI视频站（利润$2.3K/月要价$49K）、AI视频平台（利润$450/月要价$15K）——小套壳资产化退出通道  
  工具：Flippa市场（acquire.com未能访问验证）  
  来源：<https://flippa.com/search?filter[property_type]=site&q=AI%20video>

### 痛点（按频率分级）

- **视频API计费不透明且贵：积分制/无滚存/无退款（Arcads被点名），端点频繁弃用（fal页面同页3个迁移通知），xAI TTS从$4.20跳涨至$15/1M字符**〔反复出现〕  
  机会：成本路由CLI：跨模型实时单价对比+硬预算上限+端点弃用监控与自动迁移  
  证据：<https://fal.ai/models/fal-ai/veo3/api>
- **Slop变现被平台+监管围堵：YouTube 7月起去货币化批量AI内容、EU AI Act 8/2生效（罚€15M或3%营收）、FTC假评论规则每条最高$53,088、Meta强制AI标注、中国警方通报AI副业骗局**〔反复出现〕  
  机会：合规内建：披露标签/来源审计日志，让素材管道对品牌法务可采购  
  证据：<https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/>
- **转售套壳站被上游挤压：一折甩卖被封号、补贴战击穿毛利——'为字节打工一辈子'的担忧**〔多次出现〕  
  机会：官方批量/经销商层级，或做成本透明的路由工具而非转售  
  证据：<https://36kr.com/search/articles/Libtv>
- **AI UGC转化率存疑：Ipsos/Syracuse测试AI广告under-index -5 vs 真人+11，仅13%观众能识别AI广告；'数量能否补质量'无独立复现**〔多次出现〕  
  机会：素材CLI内置A/B测试与效果归因，把ROAS口径做实  
  证据：<https://okaneland.com/study/ai-ugc-ad-economics/>
- **模型/端点每季度更替（veo3弃用、Sora退出API、LTX-2.3迁移提示），买方管道与工具站反复重写集成**〔反复出现〕  
  机会：统一抽象层+迁移测试套件，卖'不变'而非'最新'  
  证据：<https://fal.ai/models/fal-ai/veo3/api>

### 付费意愿信号

- AI UGC工具订阅$29-220/月（折合$1-11/条）：HeyGen $29/600积分、$49/1000积分（20积分/分钟）；Creatify Starter $39/100、Pro $99/300；Arcads $110/10条、$220/20条——官方定价页，经okaneland 2026-07逐字核验
- 真人UGC基准：约$185/条（Collabstr 2026均值，21,000+合作样本），全包$500-2000含授权（授权加价30-50%）——Collabstr数据经okaneland转述（未审计）
- 视频API单价锚：Veo3 $0.40/秒（有声）/$0.20（无声），5s≈$2/条；Veo3 Fast $0.15/$0.10/秒——fal.ai官方页（本次实取）；Runway gen4_turbo $0.25/5s——官方PDF（本次实取）；DoNews称Runway/Luma涨价、可灵降价（单一来源，与官方页部分冲突）
- 批量场景预算：50条变体AI方案<$200 vs 真人约$7,500+（约37倍差）——okaneland测算
- 印度无脸频道报价₹5,000-15,000/条——Business Standard 2026-09-12（采访报价）
- 网站交易价：AI视频站要价$979（MRR $19）/$15K（利润$450/月）/$49K（利润$2.3K/月，约21倍月利）——Flippa卖家自报，未经审计
- 资本验证：可灵$2.8B融资@$18B估值（2026-07，多源）；fal.ai $8B（The Information 3月'谈判中'+8月HN评论称已close，单一来源）；HeyGen/Runway各$200M ARR（官方公告/Bloomberg，多源）
- 运行成本实证：Levels用fal跑生成约$4,000/天（赞助性质，HN评论）——单一来源；GetLatka估算faceless.video ARR $330K（未审计估算）

### 机会清单

- 成本路由+透明CLI：统一Veo/Kling/Seedance/Wan/H3接口，实时显示每条成本、硬预算上限、端点弃用监控与自动迁移——直击fal弃用通知、Remotion-vs-Veo、Libtv三重痛点
- 电商批量素材工作流（变体矩阵、批量生成、投放格式导出），按量计费而非订阅——中国补贴战与美国50变体<$200测算证明该层有真实预算
- 混合渲染：AI镜头+Remotion/模板的省钱组合，服务明确拒绝Veo成本的程序化视频开发者（HN直接证据）
- 自托管路由：封装MiniMax H3开源权重+消费级GPU（3090/AMD day-0）本地执行，给成本敏感用户'零API费'档位
- 合规即服务：输出EU AI Act（2026-08-02生效）/FTC/Meta要求的披露标签与素材来源日志——生效后成为品牌采购硬门槛
- 反向定位：不做slop变现自动化（YouTube打击+警方反诈的红色区域），聚焦电商/品牌素材这条'能赚钱'的管道——区分结论：电商素材与品牌内容是赚钱工作流，slop频道与转售套壳不是

### 未决问题

- X/推特上开发商公开的视频API月账单截图未获一手验证（X无搜索通道），lane③仅间接证据（fal $4K/天赞助运行、HN成本讨论、$2k自训案例）——留待人工补查
- DoNews称Runway Gen4 Turbo从$0.25涨至$0.45/5s，但官方文档当前实取$0.25/5s——涨价是否回撤或层级口径差异待核实
- fal.ai $8B轮是否正式关闭：仅3月The Information'谈判中'+8月HN评论，无官宣
- 火山引擎上Seedance 2.5官方单价页未能加载验证（Libtv'一折甩卖'的基准价缺失）
- faceless.video $330K ARR为GetLatka估算非审计；Flippa利润均为卖家自报——整体缺少第三方收入验证渠道
- AI UGC转化劣势（Ipsos -5 vs +11）仅一项独立研究且经okaneland转述，需复现
- acquire.com上的AI视频工具出售列表未能访问（仅获Flippa证据），商业模式的退出市场画像不完整

### 来源

- [fal.ai Veo3 API定价与弃用通知（官方）](https://fal.ai/models/fal-ai/veo3/api)
- [Runway API官方定价PDF](https://docs.dev.runwayml.com/assets/pricing.pdf)
- [The AI UGC ad math: $2 a video (okaneland, 2026-07-07)](https://okaneland.com/study/ai-ugc-ad-economics/)
- [TechCrunch: YouTube clarifies AI slop monetization policies (2026-07-20)](https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/)
- [Business Standard: Indian faceless channels earnings gap (2026-09-12)](https://www.business-standard.com/industry/news/indian-faceless-youtube-channels-show-wide-earnings-gap-ahead-of-new-monetization-rules-125091201023_1.html)
- [华尔街见闻：快手Q2营收355.4亿元，可灵AI收入暴增超200%（2026-08-19）](https://wallstreetcn.com/articles/3779792)
- [华尔街见闻：BAT全上车，可灵投后估值180亿美元（2026-07）](https://wallstreetcn.com/articles/3776128)
- [36kr：贴钱1折甩卖Seedance2.5，Libtv们要为字节打工一辈子？（2026-08-13，搜索页存档）](https://36kr.com/search/articles/Libtv)
- [DoNews：涨价与降价并存——AI视频生成冰火两重天（2026-07-24，搜索页存档）](https://www.donews.com/search?q=冰火两重天)
- [Flippa：videogenr.com AI视频SaaS出售（MRR $19，要价$979）](https://flippa.com/13365327-ai-powered-video-generation-platform-for-creating-viral-short-form-content-tiktok-reels-scalable-saas-with-strong-demand-and-monetization-potential)
- [Flippa搜索：AI video在售站点（$49K/$15K挂牌）](https://flippa.com/search?filter[property_type]=site&q=AI%20video)
- [HN：OpenRouter 7B vs fal.ai $8B讨论（含$8B评论，2026-08-16）](https://news.ycombinator.com/item?id=49323381)
- [HN：开发者用Remotion替代Veo控制成本（2026-08-11）](https://news.ycombinator.com/item?id=49259309)
- [HN：Levels用fal日烧$4,000的赞助运行（2026-08-29）](https://news.ycombinator.com/item?id=49492243)
- [HN：Seedance 2.5 vs MiniMax H3开源权重跑3090（2026-08-02）](https://news.ycombinator.com/item?id=49138302)
- [HN：Bloomberg Runway Hits $200M ARR转投（2026-09-08）](https://news.ycombinator.com/item?id=49614119)
- [GitHub：claude-faceless-shorts-creator（252★，90天最高星无脸频道流水线）](https://github.com/hassancs91/claude-faceless-shorts-creator)
- [GitHub API：faceless youtube仓库搜索（90天新增158个）](https://api.github.com/search/repositories?q=faceless+youtube+created:%3E2026-06-22)
- [Google News RSS存档：GetLatka faceless.video $330K ARR（2026-08-10）及Runway/HeyGen/MiniMax等多源标题](https://news.google.com/rss/search?q=faceless.video+revenue)
- [Google News RSS存档：MiniMax H3开源权重多源报道（Reuters 2026-07-30/SCMP 2026-07-31等）](https://news.google.com/rss/search?q=minimax+H3+open+weights)


## 下游行业 · 短剧出海与 AI 短剧

**摘要**：90天窗口内AI短剧从尝鲜进入工业化：2026上半年抖音端AI剧/漫剧新上架22.19万部，Q1新微短剧约95%为AI生成；9月1日《微短剧发展管理办法》施行（分级审核+每集AI标识）。管线层成新战场：字节内测工业化平台，商汤Seko用户破百万，AI漫剧成本降至真人1/5。出海侧大盘日耗约3000万美元（媒体口径），红果海外版下载破亿，TikTok亲自下场付费短剧。但98.7%未回本、爆率不足0.5%，平台治理收紧（高频AI脸零流量）。工具链空白集中在多语种译配、脸谱授权合规、投前回本预测；真人+AI混合制片受政策扶持，是下一窗口。

### 90 天时间线

- **2026-06-30**〔多源交叉〕 The Dial报道：中国微短剧日均约2.15亿人观看超1小时；2026Q1约12.2万部AI生成短剧上线；红果4月已下架超1万部低质AI剧（与澎湃报道互证）  
  来源：<https://www.thedial.world/articles/news/chinese-micro-dramas>
- **2026-07-03**〔多源交叉〕 可灵从快手拆分独立后完成近30亿美元融资、估值180亿美元（媒体披露口径，未经审计文件确认）  
  来源：<https://m.thepaper.cn/newsDetail_forward_33507133>
- **2026-07-27**〔单一来源〕 RestOfWorld调查：AI换脸盗用真人演员表演泛滥；深圳ActID等'脸谱授权'市场成型（约800用户、300持证、99-500元/集）；红果7月启动'同质化脸'专项治理（具体数字为该媒体采访所得）  
  来源：<https://restofworld.org/2026/07/china-ai-actors-microdramas/>
- **2026-08-06**〔多源交叉〕 CNA：2026Q1中国新微短剧超95%为AI生成，一年前接近零（引DataEye口径）  
  来源：<https://www.channelnewsasia.com/east-asia/ai-microdrama-china-film-industry-actors-jobs-6229191>
- **2026-08-18**〔多源交叉〕 Reuters：好莱坞制片厂收缩传统制作、转投微短剧追逐TikTok受众，洛杉矶微短剧制作设施兴起  
  来源：<https://www.reuters.com/business/media-telecom/microdramas-boom-shrinking-hollywood-studios-chase-tiktok-audience-2026-08-18/>
- **2026-08-22**〔多源交叉〕 CNN（引DataEye等）：2026年前3个月12万+部微短剧上线、95%为AI；AI制作120分钟项目约5人一周约1.5万元（约为低端真人制作1/10）；AI生成分钟价从1000元跌至最低约150元（数据未审计）  
  来源：<https://edition.cnn.com/2026/08/22/style/short-drama-ai-china-intl-hnk>
- **2026-09-01**〔官方源〕 《微短剧发展管理办法》（广电总局令第16号）施行：按投资额30万/80万元分三级审核，第34条要求每集显著位置标注AI生成；同期DataEye口径：上半年抖音端AI剧/漫剧新剧22.19万部、累计播放5157亿次，每77部仅1部回本（98.7%未回本，未审计行业数据）  
  来源：<https://m.thepaper.cn/newsDetail_forward_33967164>
- **2026-09-10**〔单一来源〕 澎湃/上观'管线战'深度：AI漫剧月上架量从1月约2万部增至3月4.7万部；字节内测短剧工业化平台（模型调度/资产复用/团队协作）；商汤Seko上线两月10万用户、现超100万（聚合Seedance/可灵+SekoIDX一致性+SekoTalk口型+无限画布）；行业爆款率仅0.16%；上海'沪8条'徐汇基地已聚62家企业  
  来源：<https://m.thepaper.cn/newsDetail_forward_34043110>

### 做得好（可借力）

- 供给工业化速度惊人：月产4.7万部漫剧、Q1新剧95% AI化，AI漫剧中档成本800-1200元/分钟、整体约为真人短剧1/5——供应链成熟，任何上游工具都有现成需求方
- 管线层快速起量：Seko两月10万→100万+用户验证了'聚合多模型+一致性+口型'的PMF；字节、商汤、TapNow、Flova、咪咕悦创、小云雀等相继入场，工具生态已过教育期
- 出海变现路径已验证：海外短剧大盘日耗约3000万美元（36kr口径）、H1 AI短剧出海收入预计12.7亿美元、红果海外版下载破亿/日活700万、ReelShort扭亏为盈年入约71亿元、TikTok下场付费短剧——分发与商业化模型清晰
- 平台治理与合规框架先行：红果高频AI脸零流量调控、4月下架3522部低质漫剧，抖音8月3日上线AI剧预检工具（肖像权/版权），管理办法明确AI标识——合规规则明朗降低了后来者的政策不确定性

### 将要发生（可搭车）

- 政策转向真人精品：广电总局9月明确大力扶持优质真人微短剧、6平台至少60亿元投真人、红果创享计划真人剧30万保底（AI剧10万）——'真人+AI增效'混合制片是下一个政策与资金窗口
- 生成成本继续下探：Seedance 9月中旬开始降价（此前已到1元/秒），可灵大额融资后将扩产能——每轮降价都触发一轮产能与内容供给爆发，工具层需求随之放大
- TikTok 9月14日推出AI转绘/AI重制短剧功能——平台级AI再创作入口开放，存量爆款可低成本翻新出海
- IP双向开发成平台标配：《聚宝仙盆》等漫剧爆后'反向开发'真人版（21财经9-19报道），'漫剧试错→真人放大'流水线将被更多平台复制
- 区域补贴窗口：AI微短剧'沪8条'9月18日正式落地，徐汇基地62家企业、最高20万算力/5万语料/500万投资优惠——工具商可复制此模式落位其他城市（温州等地已批量上线AI短剧项目）
- 头部平台开放创作者生态：ReelShort创始人Joey Jia宣称'超越微短剧'构建新娱乐生态（Variety/Deadline 6-18/19），9月初ReelShort×OnSolo办全球AI短剧创作大赛（RSS标题级信号）——UGC供给缺口意味着创作工具与教程（如TapNow×影视飓风49元课程）可搭车
- 海外免费(IAA)模式起量：红果海外版'免费为王'下载破亿——广告变现占比上升将爆炸性放大广告素材生产需求（AI漫剧已主导投放素材，AI剪辑师需求同比+179%）
- DramaBox（点众）7月20日与Globavend签AI剧全球分发协议（GlobeNewswire，原文链接未取到）——平台外部分发/联运渠道打开，利好内容供应商

### 空位（可占位）

- **多语种译配/本地化环节无公开玩家——出海最后一公里空白**  
  证据：9-10'管线战'报道盘点剧本→分镜→生成→剪辑各环节玩家（Seko/TapNow/Flova/字节内测），唯独没有翻译配音环节；同期出海收入预计12.7亿美元、海外红果免费模式起量放大多语言内容需求；海外爆款需西语/葡语/英语多版本，国内工具商无一公开宣称覆盖'译制+配音+口型对齐'  
  切入：做面向短剧出海的AI译配管线（翻译+AI配音+口型对齐+文化梗本地化），以API嵌入Seko/TapNow等生成管线，绑定无自研大模型的中型出海厂（ShortMax/九州、DramaBox/点众、BlinkDrama）
- **人脸/声音授权与生成一致性割裂，合规层无人产品化**  
  证据：RestOfWorld 7-27：ActID约800用户/300持证、99-500元/集，广州互联网法院三年约700起AI脸纠纷，字节2026年清理8.5万+侵权视频；红果对高频AI脸零流量、抖音上线预检工具——授权市场已自发出现，但与SekoIDX类一致性生成工具未打通  
  切入：做'带授权凭证的生成'：正版肖像/声音授权库+角色一致性生成一体化，输出可直接过平台预检的结果，向制作方按集收费
- **投前回本预测/爆款筛选层空白**  
  证据：98.7%未回本、22.19万部新剧破亿仅1055部（0.48%）、管线战报道行业爆率0.16%；出海日耗约3000万美元中买量为最大成本项——海量供给下'拍什么、投不投'的决策工具无人提供  
  切入：用平台播放/完留数据训练回本概率模型，提供AI小成本试播+投放建议SaaS，向制作方与出海投放代理收费
- **真人短剧AI增效工具链缺位**  
  证据：广电9月扶持真人精品+60亿平台资金+红果真人剧30万保底，但横店真人短剧锐减90%（第一财经RSS标题）、真人产能缺口巨大；AI仿真人剧占比已达70.62%却面临AI标识与治理收紧——'真人骨架+AI降本'的结合部无方案曝光  
  切入：真人短剧AI增效包：AI虚拟场景/群演补产能，叠加AI译配让一部真人剧多语言发行（真人剧出海本地化成本最高，降本空间明确），对接拿保底的中腰部承制方

### 未决问题

- ShortMax/九州与DramaBox/点众90天窗口内的AI采用率、AI剧占比无官方口径（仅点众2025年营收145亿元媒体报道，未经审计）；两家财报未公开披露AI相关成本结构变化
- 字节内测的短剧工业化平台名称、上线时间、是否对外开放均未公开，无法判断其对第三方管线商的挤压时间表
- 'H1 AI短剧出海收入12.7亿美元、TikTok分账8200万美元'（虎嗅转引）的原始统计方、口径与审计状态未核实
- ReelShort与母公司中文在线诉讼的进展及其对出海格局的影响仅获36kr RSS标题级信号，未获原文
- 译配环节是真空白还是被大厂内部消化（如字节平台内置），公开信息无法确证——建议用一手访谈验证
- 晚点LatePost/雷峰网直达报道因搜索渠道受限未获取，可能遗漏深度报道；ReelShort创始人Joey Jia生态化言论仅有RSS标题，未获全文

### 来源

- [澎湃新闻|上观新闻：AI短剧月产4.7万部，隐形'管线'战打响，字节商汤已下场（2026-09-10）](https://m.thepaper.cn/newsDetail_forward_34043110)
- [澎湃新闻：AI短剧98.7%未回本；《微短剧发展管理办法》9月1日施行解读（2026-09-01）](https://m.thepaper.cn/newsDetail_forward_33967164)
- [澎湃新闻：可灵独立后近30亿美元融资、估值180亿美元（2026-07-03）](https://m.thepaper.cn/newsDetail_forward_33507133)
- [CNN: China's AI-generated microdramas boom (2026-08-22)](https://edition.cnn.com/2026/08/22/style/short-drama-ai-china-intl-hnk)
- [RestOfWorld: They starred in shows. Then AI actors ripped off their performances (2026-07-27)](https://restofworld.org/2026/07/china-ai-actors-microdramas/)
- [Reuters: Microdramas boom, shrinking Hollywood as studios chase TikTok audience (2026-08-18)](https://www.reuters.com/business/media-telecom/microdramas-boom-shrinking-hollywood-studios-chase-tiktok-audience-2026-08-18/)
- [CNA: AI is rewriting China's filmmaking rulebook (2026-08-06)](https://www.channelnewsasia.com/east-asia/ai-microdrama-china-film-industry-actors-jobs-6229191)
- [The Dial: How China's short dramas are redefining entertainment (2026-06-30)](https://www.thedial.world/articles/news/chinese-micro-dramas)


## 下游行业 · 广告创意自动化 + 游戏视频

**摘要**：90天窗口内三层同时演进。平台层：TikTok把Seedance 2.5直接内嵌Symphony（30秒、50个多模态参考、C2PA+水印内建），Google Asset Studio多模态视频在Demand Gen GA，Meta发布Advantage+官方案例集；模型层价格崩塌：Veo Lite官方$0.05/秒、Creatify宣称$0.01/秒，对照真人UGC约$167/条，差距约百倍（多为厂商口径）。反信号同样明确：Icon从AI Admaker转向真人代理、卖家投诉自动素材误导、BI称Meta AI广告成品牌噩梦——信任缺口大于成本缺口。SaaS编排层（Smartly/Celtra）未接视频生成API，游戏侧仅DeNA买量案例。可占位：跨平台批量变体与合规审核中间件、游戏素材vertical、素材级成本分析。

### 90 天时间线

- **2026-06-22**〔官方源〕 TikTok 发布 Symphony Agent（对话式生成/管理广告）并扩充 TikTok One Content Suite UGC 库  
  来源：<https://ads.tiktok.com/business/en-US/blog/symphony-agent>
- **2026-06-30**〔官方源〕 TikTok Agentic Hub 上线：基于 Ads MCP 的 AI 代理/Skills 市场，覆盖投放、报告、创意管理，HubSpot、Innovid、Mobvista、Wix 等已上架，无需 API 凭证即可接入  
  来源：<https://ads.tiktok.com/business/en-US/blog/tiktok-agentic-hub-ai-agents-skills-mcp>
- **2026-07-07**〔官方源〕 Meta 发布 Muse Image 与 Muse Video 研究模型（广告产品整合未公告）  
  来源：<https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/>
- **2026-07-09**〔官方源〕 Meta 发布 Muse Spark 1.1 与 Meta Model API，模型 API 化  
  来源：<https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/>
- **2026-07-14**〔官方源〕 WARC×TikTok 报告：90% 营销者以 AI 为核心创意工具、88% 称素材产量上升、45% 称质量显著提升、50% 媒体预算花在与平台不适配的素材上（400 名营销负责人调研；厂商委托，未审计）  
  来源：<https://ads.tiktok.com/business/en-US/blog/warc-report-new-creative-advantage>
- **2026-07-14**〔单一来源〕 Business Insider：《Meta 的 AI 广告梦已成品牌噩梦》——品牌对 Meta AI 广告工具混乱不满（正文被反爬，仅标题级信源，媒体转述）  
  来源：<https://www.businessinsider.com/metas-ai-ads-push-causes-chaos-for-brands-2026-7>
- **2026-07-28**〔官方源〕 TikTok Q3 产品预览：Symphony Avatar 升级（配音+产品演示+虚拟试穿，免重拍产出 UGC 风格）、GMV Max Creative Excellence 经 Symphony 自动生成商品视频、Smart+ Catalog 创意升级与图片/视频自动爬取  
  来源：<https://ads.tiktok.com/business/en-US/blog/tiktok-product-preview>
- **2026-08-01**〔多源交叉〕 字节跳动发布 Seedance 2.5（一条过生成、灵活参考；HN 442 分/255 评论，多方传播）  
  来源：<https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5>
- **2026-08-03**〔官方源〕 TikTok Symphony 集成 Dreamina Seedance 2.5：视频 15s→30s、参考 9→50 个多模态、时间戳级导演控制，同步内建 C2PA 内容凭证+隐形水印+提示词审核（限部分付费广告主/市场）  
  来源：<https://ads.tiktok.com/business/en-US/blog/transforming-video-creation-tiktok-symphony-dreamina-seedance>
- **2026-08-04**〔单一来源〕 HN 社区帖：Seedance 2.5 API 定价较 v2 贵约 50%（无官方价目表佐证）  
  来源：<https://hn.algolia.com/api/v1/search_by_date?query=%22Seedance%202.5%20API%20Pricing%22&tags=story>
- **2026-08-23**〔单一来源〕 Icon（icon.com）Keynote 宣布转型「The Agency」：从 AI Admaker 转向真人 UGC——$1000/月 3 天出 6 条 100% 真人广告；自称 288+ 品牌、1288+ 创作者、融资 $30M+（Founders Fund 等；均厂商自述未审计）  
  来源：<https://icon.com>
- **2026-08-25**〔单一来源〕 CNA 报道：Shopee/TikTok 卖家投诉平台自动生成的 AI 广告货不对板、误导消费者（媒体转述）  
  来源：<https://www.channelnewsasia.com/singapore/ai-generated-videos-shopee-tiktok-misleading-sellers-6336961>
- **2026-08-26**〔单一来源〕 DeNA 手游 Solitaire Spellbook×Creatify Studio 案例：每轮 10–12 条 AI 视频变体、24h 交付，最优 Creative Score 3.0 素材每千次展示安装为基准 3 倍；Studio 通用口径每客户每周 10–100+ 条（厂商案例，未审计，未披露成本）  
  来源：<https://creatify.ai/case-study/dena>
- **2026-08-27**〔官方源〕 Google Demand Gen 八月更新：Asset Studio 多模态视频创作 GA（分镜→横竖版素材一个工作流）；官方称 H2 Demand Gen 改进带来约 30% 转化提升（内部数据，未审计）  
  来源：<https://blog.google/products/ads-commerce/demand-gen-drop-august-2026/>
- **2026-09-03**〔官方源〕 Smartly 成为 Reddit Max 广告首个官方 API 合作伙伴，主打 AI 创意变体自动化——通稿未提及任何视频生成模型集成  
  来源：<https://www.smartly.io/resources/smartly-and-reddits-max-campaigns>
- **2026-09-03**〔官方源〕 Meta 商业官方案例集：五家广告主凭 Advantage+ creative（进阶赋能型创意）、Business Agent、Omni for Auto 实现降本增效——窗口内 Advantage+ 少有的官方一手声量  
  来源：<https://www.facebook.com/business/news/businesses-driving-results-with-meta-ai-ads>
- **2026-09-11**〔官方源〕 Roblox RDC 2026：Build 标签页提示词建游戏（新西兰 alpha 以来约 9000 款；71% 的 Build 创作者从未用过 Studio）；Scene Generator（提示词+参考图→可玩场景布局）年内上线 Build+Studio；创作者近 12 个月分成 $1.7B（公司口径）  
  来源：<https://about.roblox.com/newsroom/2026/09/rdc-2026-the-world-needs-more-play>
- **2026-09-12**〔单一来源〕 AI 长片《Deviant》上映，终幕用 Seedance 2.5（经 Higgsfield）制作——生成视频进入长片正片（Show HN 单一来源）  
  来源：<https://www.deviantmovie.com>
- **2026-09-15**〔单一来源〕 Creatify 发布 Boreal，宣称「前沿质量、一美分一秒」（约 $0.01/s，30 秒素材约 $0.3；厂商自述未审计，自研或转发未确认）  
  来源：<https://creatify.ai/blog/introducing-boreal-frontier-quality-ai-video-at-a-cent-a-second>
- **2026-09-16**〔官方源〕 Google Rethink 2026 假日季合集：主打 AI Max 测试/规划工具与 agentic 商务，未提生成式创意/Veo——生成创意尚未进入 Google 假日季主叙事  
  来源：<https://blog.google/products/ads-commerce/rethink-2026/>

### 做得好（可借力）

- TikTok 把前沿模型直接搬进投放界面：Symphony 内嵌 Seedance 2.5（30 秒、50 个多模态参考、时间戳级导演控制），并同步内建 C2PA 内容凭证+隐形水印+提示词审核——生成与合规一步到位，这条链路可直接借力（经 API/Skills 接入而非重建）
- TikTok Agentic Hub 开放 Ads MCP + Skills 市场，HubSpot、Innovid、Mobvista、Wix 等已上架——第三方开发者被官方接纳为平台能力扩展者，生态接口已打开
- Google 走工作流整合路线：Asset Studio「分镜→横竖版多尺寸素材」一体化进入 Demand Gen GA，重点是把模型藏进投放工作流而非卖裸模型
- 字节系从模型发布到进投放工具只隔两天（8/1 发布→8/3 进 Symphony），模型层到应用层传导速度业内最快
- 需求端已被 WARC×TikTok 调研确认：90% 营销者以 AI 为核心创意工具、88% 素材产量上升——下游放量是行业共识（注意：厂商委托调研，未审计）
- 游戏 UGC 平台基础设施化：Roblox 提示词建游戏已产出约 9000 款、创作者年分成 $1.7B，提示词→场景的创作者工具栈在快速铺开

### 将要发生（可搭车）

- Roblox Scene Generator「今年晚些时候」上线 Build+Studio（提示词+参考图→可玩场景布局）——游戏/UGC 场景素材工具可搭车
- Meta Connect 2026（9/23–24，窗口后一天）将至：Meta 已在 7 月 API 化模型（Muse Spark 1.1）、9/8 发布 Muse 个人 AI 代理，广告侧（Muse Video 接入 Advantage+ creative）发布概率高，值得盯官方直播
- Google Rethink 2026 主打「AI 驱动假日季」+ AI Max 测试工具先行——Q4 假日季素材放量需求确定，生成式创意大概率在假期后补位
- TikTok GMV Max Creative Excellence 将经 Symphony 自动生成商品视频并随 Q3 铺开——电商素材生成全面平台化，第三方电商素材工具窗口在收窄
- Seedance 2.5 经第三方 API 托管（Atlas Cloud 等）扩散——模型 API 分销/合规托管通道正在形成，可做上游聚合
- TikTok Agentic Hub 明言生态将持续扩张——在其 MCP 上发布第三方 Skills 是被官方背书的入场方式

### 空位（可占位）

- **SaaS 编排层无人接视频生成 API：批量变体下游仍是空位**  
  证据：Smartly 9/3 成为 Reddit Max 首个 API 合作伙伴，通稿只讲「AI 创意变体自动化」，无任何视频生成模型集成；Celtra 官网与 7 月创意报告同样无视频模型接入。平台内嵌（TikTok/Goolge）覆盖不了跨平台客户的多渠道管线  
  切入：做「视频生成 API（Veo/Seedance/Boreal 任一）→企业创意自动化管线」的连接器：跨 Meta/Google/TikTok 的批量变体+尺寸适配+投放反馈闭环，补 Smartly/Celtra 的缺位
- **跨平台合规审核/素材治理中间层空白**  
  证据：TikTok 8/3 自建 C2PA+隐形水印+提示词审核，但仅限自家生态；CNA 8/25 报道卖家被自动生成素材误导；BI 7/14 报道 Meta AI 广告致品牌混乱——窗口内没有任何第三方 provenance 校验或品牌安全 QA 工具出现  
  切入：跨平台 AI 素材合规审计中间件：内容凭证校验、误导性检测、各平台政策映射，卖给代理和品牌方
- **游戏 vertical 几乎无人做：无 trailer/过场/store 素材公开案例**  
  证据：窗口内游戏公司公开案例仅 DeNA 休闲游戏买量（Creatify 厂商案例，未披露成本）；HN 检索无 studio 级案例；Roblox Scene Generator 尚未上线；GameLook 等中文游戏媒体检索失败，无反例证据  
  切入：面向游戏厂商的 store 页素材/预告片生成管线，内建 Steam AI 披露合规工作流——买量素材已被 DeNA 验证有 ROI，向上游 trailer 延伸无人占位
- **素材级成本-效果度量无人做**  
  证据：所有成本锚点均为厂商口径：Veo Lite 官方 $0.05/s（30s 约 $1.5）、Boreal 自述 $0.01/s（约 $0.3）、Icon 真人 UGC $167/条（营销价）；WARC 指出 50% 预算花在不适配素材上，但没有工具把「生成成本-平台表现-人力成本」放进同一归因视图  
  切入：creative cost analytics：素材级成本归因与边际 ROI 度量，代理和投放团队的采购决策刚需
- **纯 AI 质量天花板已被市场用脚投票：真人+AI 混合供给无人编排**  
  证据：Icon 8/23 从「AI Admaker」整体转向「100% 真人 UGC」（$1000/月 6 条），并自称 $30M+ 融资（未审计）；同月 CNA 报道自动素材误导投诉——AI-only 在 UGC 风格赛道正失去信任  
  切入：混合供给编排层：AI 批量长尾素材+真人 hero 素材统一调度与质检，而非站队纯 AI 或纯真人

### 未决问题

- Meta Advantage+ creative 窗口内的具体功能更新清单未获得：Meta newsroom 无广告工具专项公告，仅 9/3 官方案例集；BI 7/14 批评报道正文被反爬，细节未核实——需 Meta for Business 渠道或 Meta Connect（9/23–24）确认
- Seedance 2.5 官方 API 价目表未找到一手来源（HN 社区帖称比 v2 贵约 50%，未证实）
- 品牌方/代理经审计的单条素材成本数据（AI vs 真人）不存在公开版本——所有数字均为厂商营销口径，本报告的成本结论仅在「量级」意义上成立
- 中文生态覆盖不足：巨量引擎「即创」（aic.oceanengine.com）存在但窗口内无可检索的带日期动态；GameLook 连接失败、qbitai 403，中国游戏厂商（米哈游/网易等）生成视频案例未能系统检索
- Creatify Boreal 为自研模型还是转发第三方未确认；其 $0.01/s 口径无第三方基准佐证
- Meta Muse Video（7/7 研究发布）是否会/何时接入 Advantage+ creative 未有任何公告
- WebSearch 配额耗尽后依赖 WebFetch 直连一手源，媒体面（除 HN API 外）覆盖有盲区

### 来源

- [TikTok: Introducing Symphony Agent](https://ads.tiktok.com/business/en-US/blog/symphony-agent)
- [TikTok Agentic Hub: AI Agents & Skills with Ads MCP](https://ads.tiktok.com/business/en-US/blog/tiktok-agentic-hub-ai-agents-skills-mcp)
- [Meta: Introducing Muse Image and Muse Video](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/)
- [Meta: Muse Spark 1.1 / Meta Model API](https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/)
- [WARC×TikTok: The New Creative Advantage（厂商委托调研）](https://ads.tiktok.com/business/en-US/blog/warc-report-new-creative-advantage)
- [Business Insider: Meta's AI advertising dreams have become a nightmare for brands（媒体转述）](https://www.businessinsider.com/metas-ai-ads-push-causes-chaos-for-brands-2026-7)
- [TikTok Q3 2026 Product Preview](https://ads.tiktok.com/business/en-US/blog/tiktok-product-preview)
- [ByteDance Seed: Introducing Seedance 2.5](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5)
- [TikTok Symphony × Dreamina Seedance 2.5](https://ads.tiktok.com/business/en-US/blog/transforming-video-creation-tiktok-symphony-dreamina-seedance)
- [HN Algolia: Seedance 2.5 API Pricing（社区帖）](https://hn.algolia.com/api/v1/search_by_date?query=%22Seedance%202.5%20API%20Pricing%22&tags=story)
- [Icon — Keynote 2026: The Agency（厂商自述）](https://icon.com)
- [CNA: Shopee/TikTok 卖家投诉自动生成 AI 广告误导（媒体转述）](https://www.channelnewsasia.com/singapore/ai-generated-videos-shopee-tiktok-misleading-sellers-6336961)
- [Creatify × DeNA 案例研究（厂商案例，未审计）](https://creatify.ai/case-study/dena)
- [Google: Demand Gen Drop August 2026 — Multimodal Video Creation in Asset Studio](https://blog.google/products/ads-commerce/demand-gen-drop-august-2026/)
- [Smartly: Reddit Max 首个 API 合作伙伴](https://www.smartly.io/resources/smartly-and-reddits-max-campaigns)
- [Meta Business: 五家广告主的 Meta AI 广告成效](https://www.facebook.com/business/news/businesses-driving-results-with-meta-ai-ads)
- [Roblox RDC 2026: The World Needs More Play](https://about.roblox.com/newsroom/2026/09/rdc-2026-the-world-needs-more-play)
- [Deviant — AI 长片（Seedance 2.5 终幕）](https://www.deviantmovie.com)
- [Creatify Boreal: 一美分一秒（厂商自述）](https://creatify.ai/blog/introducing-boreal-frontier-quality-ai-video-at-a-cent-a-second)
- [Google: Rethink 2026 假日季合集](https://blog.google/products/ads-commerce/rethink-2026/)
- [Google AI 官方定价页（Veo 3.1 Lite/Fast/Standard 按秒计费，页面无日期）](https://ai.google.dev/pricing)


## 下游行业 · 影视/虚拟制片/后期

**摘要**：90天内（2026-06-22~09-22）影视/虚拟制片赛道成本驱动加速：Netflix Q2股东信（官方源）披露2026年约300部作品使用GenAI、集中于后期、覆盖概念/预可视化到交付全链路；SEC 10-Q口径披露5.87亿美元收购InterPositive（后期dailies模型）；BBC R&D发布低成本生成式虚拟制片Osmia；Autodesk Flow Studio（原Wonder Dynamics）官方集成Seedance/Wan等第三方模型并以USD导出；迪士尼设首位公司级CTO（10-2上任）；威尼斯Reply AI电影节3000+投稿。明显缺口：previz→生成无标准化契约、影院级QC验收无人定义、传统VP工具商（Mo-Sys）90天沉默、Runway与中文生态未获一手验证。

### 90 天时间线

- **2026-07-16**〔官方源〕 Netflix Q2 2026股东信：GenAI工作流已用于约300部作品，最大集中度在后期制作；明确'从概念与预可视化到后期与交付'全生命周期口径；案例：Glory(印度)、Brasil 70(巴西)、The American Experiment(美国，AI增强人群/历史战争/世界观定场镜头)。商业背景数字为公司未经审计陈述（财报信），采用事实为官方口径。  
  来源：<https://s22.q4cdn.com/959853165/files/doc_financials/2026/q2/FINAL-Q2-26-Shareholder-Letter.pdf>
- **2026-07-17**〔多源交叉〕 Netflix以5.87亿美元现金收购Ben Affleck创办的InterPositive（SEC Form 10-Q监管披露口径，非审计报表；交易2026年3月完成）；工具基于生产dailies构建后期AI模型（混音/重打光/加VFX），'不走典型视觉生成路线'；Affleck任Netflix高级顾问。Variety+THR+HN多源交叉。  
  来源：<https://variety.com/2026/film/news/netflix-paid-587-million-ben-affleck-ai-interpositive-1236815111/>
- **2026-07-24**〔官方源〕 BBC R&D发布Osmia VP研究：用AI+低成本技术实现虚拟制片，替代昂贵传统LED volume基础设施——90天内唯一官方的'生成式+虚拟制片'结合公开信号。  
  来源：<https://www.bbc.co.uk/rd/articles/2026-07-virtual-production>
- **2026-08-11**〔单一来源〕 popcorn.movie上线（HN Show）：'AI电影界的烂番茄'，按所用工具归因排名AI影片——社区级AI电影评价基础设施出现。  
  来源：<https://news.ycombinator.com/item?id=49256954>
- **2026-09-04**〔单一来源〕 Semafor威尼斯Reply AI电影节报道：3000+投稿、10部入围；Catherine Hardwicke称导演用AI做背景与预可视化；罗马Labyrinth Studios为Sky Cinema制作剧集。文中A24×Google $75M、Disney×OpenAI $1B Sora授权均为媒体转述（未经审计、无一手确认）。  
  来源：<https://www.semafor.com/article/09/04/2026/filmmakers-tout-ais-use-in-hollywood-at-the-other-film-festival-in-venice>
- **2026-09-11**〔官方源〕 Autodesk Flow Studio官方页（原Wonder Dynamics Wonder Studio，页面dateModified 2026-09-11）：新增3D Editor+Canvas，集成第三方前沿视频模型Seedance 2.5(字节)/Wan 3.0(阿里)/Flux 3/Nano Banana 2(谷歌)，30秒1080p原生音频、50参考图，USD导出至Maya/Blender/Unreal——动捕/roto工具官方转向'生成前可控层'聚合器。  
  来源：<https://www.autodesk.com/products/flow-studio/overview>
- **2026-09-18**〔单一来源〕 NYT报道：迪士尼聘用Character.AI CEO Karandeep Anand出任首位公司级CTO，向CEO Josh D'Amaro汇报，2026-10-02上任，多名Character.AI技术人员随同加入（媒体对官方人事的报道）。  
  来源：<https://www.nytimes.com/2026/09/18/business/media/disney-ai-technology-karandeep-anand.html>

### 做得好（可借力）

- Netflix公开采用规模与全链路口径（约300部、后期为主、previz→交付），为后期/预演AI工具提供最高级别的预算合法性锚点，可直接引用其股东信原文立项
- 商业数字罕见可核验：$587M收购走SEC Form 10-Q监管披露（非审计报表但监管口径），Variety+THR+HN多源交叉
- BBC R&D公开发布低成本生成式虚拟制片（Osmia）研究，提供可复用的公开技术蓝本
- Autodesk Flow Studio官方集成中文系模型（Seedance/Wan）+USD可编辑导出，说明动捕/roto工具正成为'生成前可控层'标准载体，存在集成接口位
- 独立管线活跃：威尼斯Reply AI电影节3000+投稿、Labyrinth Studios为Sky Cinema制作、popcorn.movie工具归因排名——展示与分发渠道成型
- AI进入片厂决策层：迪士尼首位公司级CTO、Affleck任Netflix高级顾问，采购与立项话语权上移

### 将要发生（可搭车）

- 2026-10-02迪士尼CTO Anand上任，预计随后出现公司级AI供应商、采购与组织动作，可搭车对接
- 2026-10 Netflix Q3财报预计更新GenAI采用数字，'约300部'可能变成季度环比追踪指标，值得盯股东信
- InterPositive dailies→后期模型管线化（混音/重打光/VFX）将流入Netflix制作流程，形成后期工具链官方需求信号
- BBC Osmia为研究项目，后续试点、工具开源或论文可期，低成本的gen+VP路线有跟随空间
- AI电影节年度周期（Reply威尼斯、Runway赛事）与popcorn.movie式工具归因排名持续产出公开管线案例
- OpenAI官方注记Sora消费产品已于2026-04-26停用，叠加Disney×OpenAI授权传闻，预计有新产品或授权落地公告

### 空位（可占位）

- **previz→生成无标准化数据契约：Netflix官方确认previz→post全链路GenAI使用，但90天内无任何公开的预演→生成交换格式或合同标准，各家均为私有管线（InterPositive dailies、Flow Studio仅USD单点导出）**  
  证据：Netflix Q2 2026股东信原文覆盖'concept and pre-visualization through post and delivery'；HN/官方渠道检索无previz-to-gen格式信号；Flow Studio官方页仅见USD导出  
  切入：定义开放的previs-to-gen shot contract（相机/镜头/走位/plate引用的schema），对接生成端（Runway/可灵/Flow），占位成为行业交换格式
- **影院级QC/验收标准无人做：只有社区级排名与创意节展，面向片厂的AI素材验收基准（时序一致性、闪烁、颗粒匹配）无公开工具或标准**  
  证据：90天内仅有popcorn.movie（社区工具归因）与Reply电影节（创意展示）；Netflix股东信明言'更高质量更快更便宜交付'却无公开验收口径  
  切入：做面向片厂/保险方的AI shot QC基准与验收工具链，直接借Netflix'质量'话语立项
- **高预算端采用不透明，以并购与财报口径披露：真实工作流细节（哪些镜头、比例、验收流程）零公开，授权传闻无一手确认**  
  证据：$587M InterPositive走10-Q披露；Semafor报道的A24×Google $75M、Disney×OpenAI $1B均无一手文件  
  切入：公开管线teardown案例研究+面向片厂资产管理（Autodesk Flow生态）的集成报告，填补'披露黑箱'信任缺口
- **传统VP工具商窗口期沉默：Mo-Sys最新官方动态停留在2026-03（VP Pro XR赴奥斯卡），LED volume与生成管线结合无新公开信号；BBC Osmia是唯一gen+VP信号且为低成本路线**  
  证据：mo-sys.com/news页最新条目均为窗口前（2026-03及更早）；Wonder Dynamics官网重定向至Autodesk Flow Studio后动作集中在2026-09-11一次  
  切入：LED volume+生成背景扩展/实时gen层的集成工具，抢在Mo-Sys/Disguise官方方案之前占位（Osmia证明低成本需求真实存在）

### 未决问题

- Runway 90天影视侧一手信号未获取：/news页返回2024年陈旧缓存、sitemap重定向、/research页论文无日期标注（描述提及Gen-4/Aleph/Act-Two），电影合作伙伴关系无法落窗验证
- Disney×OpenAI $1B Sora授权与A24×Google $75M仅为Semafor媒体转述（未经审计、无一手确认），且OpenAI官方页注明Sora产品已于2026-04-26停用，存在口径矛盾待解
- 中文生态（可灵/即梦/Vidu与影视合作）未验证：本环境Bing/DuckDuckGo检索被封、量子站内检索无结果；Autodesk集成Seedance/Wan侧面说明中文模型已进入国际制作工具链，但直接影视级合作证据缺失
- SAG-AFTRA AI条款执行90天动态：官网抓取失败（MCP 500）、HN无信号，工会执行力度未知
- Netflix'约300部作品'中previz环节具体占比未披露（信中仅说明后期集中度最大）
- Gene Wilder AI声音用于Wonka衍生片（The Golden Ticket）仅为The Verge对财报电话的转述，未一手验证

### 来源

- [Netflix Q2 2026 Shareholder Letter (官方PDF)](https://s22.q4cdn.com/959853165/files/doc_financials/2026/q2/FINAL-Q2-26-Shareholder-Letter.pdf)
- [Variety: Netflix paid $587M for Ben Affleck's AI startup InterPositive](https://variety.com/2026/film/news/netflix-paid-587-million-ben-affleck-ai-interpositive-1236815111/)
- [The Hollywood Reporter: Netflix price for Ben Affleck AI company revealed](https://www.hollywoodreporter.com/business/business-news/netflix-price-ben-affleck-ai-company-revealed-1236651217/)
- [The Verge: Netflix says AI used in hundreds of titles](https://www.theverge.com/streaming/966633/netflix-ai-titles-q2-2026-earnings)
- [BBC R&D: Osmia VP — AI for low-cost virtual production](https://www.bbc.co.uk/rd/articles/2026-07-virtual-production)
- [Semafor: Filmmakers tout AI's use in Hollywood at the other film festival in Venice](https://www.semafor.com/article/09/04/2026/filmmakers-tout-ais-use-in-hollywood-at-the-other-film-festival-in-venice)
- [NYT: Disney hires Character.AI CEO Karandeep Anand as first companywide CTO](https://www.nytimes.com/2026/09/18/business/media/disney-ai-technology-karandeep-anand.html)
- [popcorn.movie (HN Show: Rotten Tomatoes for AI films)](https://news.ycombinator.com/item?id=49256954)
- [Autodesk Flow Studio (formerly Wonder Studio) 官方页](https://www.autodesk.com/products/flow-studio/overview)
- [OpenAI Sora页面（产品于2026-04-26停用注记）](https://openai.com/index/sora-is-here/)
- [Mo-Sys news（窗口期沉默证据）](https://www.mo-sys.com/news/)
- [Runway research（无日期论文列表）](https://runwayml.com/research)
- [HN Algolia API（检索基础设施）](https://hn.algolia.com/api/v1/)


## 技术前沿路线图（能力跳变 → 契约冲击推演）

**摘要**：90天窗口五条主线齐动：①长视频进入免训练外推时代，KV缓存记忆工程让5秒基座产出2分钟视频（24×），多镜头编排论文密集；②流式生成达22-30FPS单卡实时，MiniMax H3等开放权重模型已"快于实时"商用，Seedance 2.5破30秒；③世界模型分水岭：World Labs官方发布Atlas（1分钟1440p+显式3D高斯输出），开源侧LingBot-World 2.0小时级交互世界获1800星，Anthropic $6B收购Decart流产（未经审计媒体报道）；④音画同步/口型达30FPS多人全双工；⑤判片侧FIRM-Video奖励模型+约15个新基准，暴露VBench高分≠物理正确（0.8 vs ≤0.42），判片闭环首次具备可自动化地基，但DF26显示深伪检测器近随机。

### 90 天突破（含产业化距离）

- **长视频·KV缓存记忆工程（免训练外推）**（产业化：1年内，置信度：多源交叉）：窗口内约18篇论文集中出现：FreqForcing频谱自锚定把5秒基座外推到2分钟（24×），另有LayerRecall、RECAP-Forcing、DensityKV、ISPA、Surprise Forcing、SlotMem、Diff-VF（免训练短→长）、Xema（SLO下服务）等，路线收敛为'短模型+记忆/频域锚定长输出'，无需重训基座  
  来源：<http://export.arxiv.org/api/query?search_query=all:%22long+video+generation%22&sortBy=submittedDate&sortOrder=descending>
- **长视频·多镜头与导演级编排**（产业化：1年内，置信度：多源交叉）：CineWeaver用位置编码操控多镜头切换，ShotPlan（2026-07-21）引入可学习规划token做镜头计划，Vorch-Director在LTX-2上用噪声残差做多镜头导演修正：从'生成连续视频'转向'执行镜头脚本'  
  来源：<https://pensioner-11.github.io/ShotPlan/>
- **流式/实时生成·因果蒸馏工业化**（产业化：1年内，置信度：多源交叉）：Self-Forcing谱系（Ms. Forcing、Stream Forcing、DynaForcing）+ Causal-rCM（arXiv 2606.25473，应用于Cosmos世界模型）把扩散压到少步因果生成；NVIDIA官方FastGen-PDD并行解码蒸馏（2026-08-05）佐证大厂押注；学术端22-27FPS、产品端已快于实时  
  来源：<https://research.nvidia.com/labs/genair/pdd/>
- **开放权重近实时视频模型商用（MiniMax H3）**（产业化：已上线，置信度：多源交叉）：MiniMax H3/H3 Max：开放权重模型在r/StableDiffusion办AMA（2026-08-06），fal.ai以'快于实时'上线H3 Max并称质量Pareto前沿，NVIDIA Sana团队发布DGX Spark上768p一分钟生成教程（2026-09-12）：开放权重+消费级/边缘实时化  
  来源：<https://nvlabs.github.io/Sana/Sol-Engine/Sol-H3-Spark/>
- **商业闭源模型时长破30秒（Seedance 2.5）**（产业化：已上线，置信度：单一来源）：字节Seedance 2.5被媒体报道突破30秒时长壁垒（2026-06-23，窗口首日）；另捕获Meta官方X账号宣布发布MuseVideo视频生成模型（2026-07-08，细节未核验）  
  来源：<https://www.the-decoder.com/bytedances-seedance-2-5-breaks-the-30-second-barrier-for-ai-video-generation/>
- **World Labs Atlas官方发布（多模态世界模型）**（产业化：1年内，置信度：官方源）：2026-09-01 World Labs（李飞飞）官方博客发布Atlas：自回归扩散transformer，以相机位姿为空间上下文，相机控制生成最长1分钟1440p视频，同时输出显式3D（高斯溅射）与时空模拟；已开放早期访问并将并入Marble。90天窗口内最重要的世界模型官方公告  
  来源：<https://worldlabs.ai/blog/atlas>
- **开源交互式世界模型生态爆发**（产业化：已上线，置信度：多源交叉）：LingBot-World 2.0（Robbyant/lingbot-world-v2，2026-07-08创建、2026-09-10仍在更新，1803星/142叉）主打'无限世界+多样交互'（小时级）；Kyutai MIRA多人共享世界、MiniWorld宣称8卡GPU可训、HelixWorld等：交互世界模型门槛快速下探  
  来源：<https://github.com/Robbyant/lingbot-world-v2>
- **世界模型资本信号：Anthropic-$6B Decart交易流产**（产业化：更远或不确定，置信度：多源交叉）：Bloomberg报道：Anthropic曾在2026年7月洽谈以$6B收购实时世界模型公司Decart，2026-09-08报道已放弃。注意：商业数字为媒体报道、未经审计，且交易未发生，但确认了实时世界模型的战略定价量级  
  来源：<https://www.bloomberg.com/news/articles/2026-09-08/anthropic-said-to-walk-away-from-6-billion-decart-acquisition>
- **NVIDIA Cosmos官方动态：模型层停滞、工具链活跃**（产业化：已上线，置信度：官方源）：GitHub官方org数据：模型仓库（predict2.5最后推送2026-06-08、transfer2.5为2026-06-30、reason2为2026-06-07）窗口内无新模型；窗口内活跃的是cosmos-rl RL框架（2026-09-21）与xenna数据管线（2026-09-01）。'Cosmos 3'仅见于Causal-rCM论文自述，无官方佐证  
  来源：<https://api.github.com/orgs/nvidia-cosmos/repos?sort=pushed&per_page=30>
- **Genie 3窗口内无官方更新（负面发现）**（产业化：更远或不确定，置信度：推断）：HN按日期检索仅见2026-08-06对2025-08-05原博客的转贴（3分，低热度）；DeepMind官方博客列表未见Genie系列新条目。Genie 3仍停留在'限量预览'叙事，官方进展不可证  
  来源：<https://hn.algolia.com/api/v1/search_by_date?query=Genie%203&tags=story&hitsPerPage=30>
- **4D/场景持久一致性**（产业化：1-3年，置信度：多源交叉）：Streaming4D（分块自回归+增量3D重建联合生成）、DAR（视频作为原生4D渲染器）、Hallo4D（4D幻觉校正）、4DSynth（程序化世界生成）：视频与显式3D表示在生成过程中双向耦合  
  来源：<http://export.arxiv.org/api/query?search_query=all:%224D+generation%22&sortBy=submittedDate&sortOrder=descending>
- **音画同步/口型达实时多人级**（产业化：1年内，置信度：多源交叉）：TBDub（7.13FPS视觉配音/翻译口型）、InterTalk（30FPS多人对话生成）、FacePlex（全双工语音+面部联合token）、CETalk（情感可控）：从'单人对齐'进化到'多人实时+情感+全双工'  
  来源：<http://export.arxiv.org/api/query?search_query=all:%22lip+sync%22&sortBy=submittedDate&sortOrder=descending>
- **视频奖励模型落地（FIRM-Video）**（产业化：1年内，置信度：多源交叉）：FIRM-Video（arXiv 2608.21839）：清单（checklist）驱动的视频奖励模型，配88K规模数据集，把'好不好'拆成可归因的细粒度判据——判片闭环从纯VLM打分走向结构化、可回归的自动化验收  
  来源：<https://arxiv.org/abs/2608.21839>
- **视频评测基准大爆发+物理鸿沟实锤**（产业化：1年内，置信度：多源交叉）：窗口内约15个新基准：StreamAV-Bench（首个流式音视频生成基准，2608.26336）、VWG-Bench（VLM-as-Judge，2609.11242）、OmniVBench（2609.22069）、PAWBench（概率物理）、Principia（生成器VBench约0.8但关系物理≤0.42）、CamEval（电影语言）、DF26（主流深伪检测器接近随机）：综合分与物理正确性严重脱钩被量化  
  来源：<https://arxiv.org/abs/2608.26336>

### 对契约/判片/角色资产三层的冲击推演

- **能力跳变**：免训练时长外推：5秒基座→2分钟输出（KV缓存/记忆工程，24×）
  - 任务契约：duration从固定5/10s档位改为'基座时长×外推倍率'两段式字段；新增memory_budget与'外推漂移声明'；多镜头序列字段从3-4镜上调至12+镜，长视频任务首次可进契约
  - 判片闭环：整片全检不可行，改为首/中/尾分块抽检+时间漂移曲线硬指标（角色ID相似度、光照/场景退化斜率），长尾帧离群率设为一票否决阈值
  - 角色资产：角色资产必须携带'时间不变式'包：多时刻参考帧集+频域指纹，供外推过程周期性重锚定；单参考帧资产在>30s任务上贬值
- **能力跳变**：流式/实时生成：22-30FPS单卡、因果蒸馏、中途可干预
  - 任务契约：契约从异步作业+轮询改为声明式latency_budget/fps/可恢复token；prompt支持中途热更新（分块续写语义），'一次性提交整单'模式作废
  - 判片闭环：判片后置QC改为分块在线抽检（块级判片API、拒块即重生成），判块延迟必须小于生成块时长；StreamAV-Bench类协议可直接作为判片接口规范
  - 角色资产：资产需预编译为低延迟运行时格式：身份embedding/KV前缀缓存，支持'身份前缀注入'替代逐帧贴参考图，否则实时管线无法消费
- **能力跳变**：世界模型原生3D：Atlas视频+显式3D双产物、相机位姿条件化
  - 任务契约：任务契约出现双产物字段：2D视频轨+3D场景轨（splat/mesh+相机位姿轨）；camera_path从文本导演提示升为一等结构化输入参数
  - 判片闭环：新增几何一致性通道：重投影误差、多视角一致性、概率物理判分（PAWBench/Principia类）；VLM-only判片被证伪（VBench 0.8 vs 物理≤0.42），必须多判器融合
  - 角色资产：角色资产升级为'3D一致身份资产'：可渲染splat/mesh+表情基，保证任意相机轨迹下角色不崩；纯2D图参考资产无法参与相机控制类任务
- **能力跳变**：判片可自动化：FIRM-Video清单式奖励模型+15个新基准
  - 任务契约：契约内嵌机器可读验收清单schema（物理/时序/口型/镜头连续性逐项布尔+分值），生成方与判片方共享同一checklist，验收从vibe变为可回归测试；需新增provenance/水印字段应对深伪检测失效
  - 判片闭环：判片闭环三级流水：VRM初筛→checklist细粒度归因→人工只处理不确定带；DF26显示检测器近随机，真伪判别不可依赖检测器，须依赖链上元数据
  - 角色资产：角色一致性获得可量化判据（跨镜头ID相似度阈值、音色相似度阈值）；角色资产包须附带评测锚点：多角度标准帧、音色样本、blendshape清单
- **能力跳变**：音画一体实时化：30FPS多人对话、全双工、情感可控
  - 任务契约：契约新增audio_track（对白文本+情感参数）、lip_sync_tolerance（音画偏移毫秒上限）、多人对话轮次表（speaker turns）；'无声视频+后期配音'类契约被淘汰
  - 判片闭环：判片强制项：音画偏移检测（<45ms）、口型-音素对齐分、多人场景说话人归属正确率；静音片段默认判缺陷
  - 角色资产：角色资产必须声画一体：音色ID+嘴形blendshape+谈话风格token打包，单看'长得像'的资产不再满足对话类任务

### 未决问题

- World Labs Atlas一手博客两次直连失败（ECONNREFUSED），最终经webReader快照取得官方文案；价格、分辨率档位、早期访问准入细节未逐项验证
- DeepMind Genie 3窗口内无新官方公告可证：HN仅有2026-08-06对2025-08-05原博客的低热度转贴；DeepMind官方博客列表快照缓存偏旧（最新可见条目2025-10），不排除存在未被索引的更新
- NVIDIA 'Cosmos 3'仅出现在Causal-rCM论文自述中，nvidia-cosmos官方org窗口内无对应仓库或公告，真实性待官方确认
- 中文一手源未系统采集：WebSearch预算耗尽后仅依赖arXiv/HN/GitHub三个英文API，快手可灵、海螺、即梦、混元等国产厂商的中文官方公告（公众号/官网）未覆盖，本报告中'商业闭源'侧对国产动态的覆盖可能低估
- Visko Orbis 1.0（自称小时级4K 24FPS实时交互）、DreamForge（$2k训练成本实时世界模型）、Physion Arc 1.0（分钟级agent生成）均为公司/作者自述的单一来源，无第三方复现，未纳入主结论
- MiniMax H3'开放权重'依据Reddit AMA与fal.ai页面，许可证条款与权重下载渠道未直接核验；Meta MuseVideo仅捕获官方X账号转贴，规模与开放程度未核验
- DF26显示主流深伪检测器接近随机水平，对判片'真伪鉴别'能力的路线含义（是否应全面转向C2PA/内容溯源）需专门调研，超出本lane范围

### 来源

- [World Labs Atlas 官方博客（2026-09-01）](https://worldlabs.ai/blog/atlas)
- [Robbyant/lingbot-world-v2（LingBot-World 2.0，GitHub API 元数据）](https://github.com/Robbyant/lingbot-world-v2)
- [Bloomberg: Anthropic Said to Walk Away from $6B Decart Acquisition（2026-09-08，商业数字未经审计）](https://www.bloomberg.com/news/articles/2026-09-08/anthropic-said-to-walk-away-from-6-billion-decart-acquisition)
- [NVIDIA FastGen-PDD: Parallel Decoding Distillation（官方研究页，2026-08-05）](https://research.nvidia.com/labs/genair/pdd/)
- [nvidia-cosmos org 仓库活跃度（GitHub API，官方数据）](https://api.github.com/orgs/nvidia-cosmos/repos?sort=pushed&per_page=30)
- [FIRM-Video：清单驱动视频奖励模型（arXiv 2608.21839）](https://arxiv.org/abs/2608.21839)
- [StreamAV-Bench：首个流式音视频生成基准（arXiv 2608.26336）](https://arxiv.org/abs/2608.26336)
- [VWG-Bench：VLM-as-Judge 视频生成评测（arXiv 2609.11242）](https://arxiv.org/abs/2609.11242)
- [OmniVBench（arXiv 2609.22069）](https://arxiv.org/abs/2609.22069)
- [Causal-rCM：因果一致性蒸馏应用于世界模型（arXiv 2606.25473）](https://arxiv.org/abs/2606.25473)
- [Visko Orbis 1.0：小时级4K实时交互（arXiv 2607.26694，单一来源极端声明）](https://arxiv.org/abs/2607.26694)
- [MiniMax H3 Max on fal.ai（快于实时商用服务）](https://fal.ai/tools/minimax-h3-max)
- [Sana Sol-Engine：MiniMax-H3 768p DGX Spark 一分钟生成（NVIDIA，2026-09-12）](https://nvlabs.github.io/Sana/Sol-Engine/Sol-H3-Spark/)
- [The Decoder: ByteDance Seedance 2.5 破30秒（2026-06-23，媒体转述）](https://www.the-decoder.com/bytedances-seedance-2-5-breaks-the-30-second-barrier-for-ai-video-generation/)
- [ShotPlan: Cinematic Video Generation with Learnable Planning Token](https://pensioner-11.github.io/ShotPlan/)
- [DeepMind 官方博客列表（Genie 3 窗口内无新条目可证）](https://deepmind.google/discover/blog/)
- [HN Algolia 按日期检索（窗口内 'video generation' 证据查询口）](https://hn.algolia.com/api/v1/search_by_date?query=%22video%20generation%22&tags=story&numericFilters=created_at_i%3E1782086400)
- [arXiv 导出 API：长视频生成按提交日降序（证据查询口）](http://export.arxiv.org/api/query?search_query=all:%22long+video+generation%22&sortBy=submittedDate&sortOrder=descending)
- [DreamForge：$2k 训练实时世界模型（公司自述）](https://trydreamforge.com)
- [Physion Arc 1.0：分钟级视频生成 agent（公司博客自述）](https://physionlabs.ai/blog/physion-arc1.0)


## 开源生态 · 经济面（ComfyUI nodes / CivitAI / HF 趋势）

**摘要**：90天窗口内开源视频生态发生权力转移：MiniMax H3（7-28开放权重，33B，同步音视频，HF月下载404万，自定义community license）以day-0 ComfyUI支持引爆生态，一个月长出十几个H3专用节点；LTX-2.5（7-23，月下载163万）靠官方IC-LoRA控制件体系扩张；Wan系（全Apache-2.0）进入存量维护，窗口内仅Wan-Dancer-14B小幅更新。最关键信号：头部WanVideoWrapper（6708★）自5-24零提交、1282个open issues无人接盘，而kijai本人转向ComfyUI内核/内存可视化。可构建面三大空白清晰：跨任务生产契约（ComfyUI原生缺失，中文社区已自行发明production.json）、判片/QC验收节点、LoRA可移植格式。所有star/下载为平台API自报数据，未经审计。

### 90 天时间线

- **2026-07-01**〔官方源〕 ComfyUI 官方发布 comfy-mcp（本地 MCP server，让 AI agent 驱动 ComfyUI），至 9-20 仍活跃提交，234★  
  来源：<https://api.github.com/repos/Comfy-Org/comfy-mcp>
- **2026-07-03**〔官方源〕 生数科技开源 Vidu-S（实时交互/可编辑/空间视频生成），429★，但 repo 无 license 文件（GitHub API license=null），开源程度存疑  
  来源：<https://api.github.com/repos/shengshu-ai/Vidu-S>
- **2026-07-10**〔官方源〕 阿里 Wan-AI 发布 Wan-Dancer-14B（music-to-dance 图生视频，Apache-2.0，HF 月下载 15,792）——窗口内 Wan 官方唯一新模型  
  来源：<https://huggingface.co/api/models/Wan-AI/Wan-Dancer-14B>
- **2026-07-23**〔官方源〕 Lightricks 发布 LTX-2.5（HF createdAt 2026-07-23；月下载 1,626,742，4,642 likes，license:other 自定义社区协议），8-11 起配套 IC-LoRA 控制件（Pixel Spatial Upscaler/Outpainting）持续扩张  
  来源：<https://huggingface.co/api/models?author=Lightricks&sort=downloads>
- **2026-07-26**〔官方源〕 OpenMOSS 开源 OmniVAE（统一音视频 VAE，跨模态对齐），86★，窗口内活跃  
  来源：<https://api.github.com/search/repositories?q=video+generation+created:%3E2026-06-22&sort=stars>
- **2026-07-28**〔官方源〕 MiniMax 开放 MiniMax-H3 权重：~33.1B 参数，image-text-to-video + 同步音频（audio VAE 独立组件），768p/2K 两档，diffusers 原生，license 为自定义 minimax-h3-community-license-agreement（非 OSI）  
  来源：<https://huggingface.co/api/models/MiniMaxAI/MiniMax-H3?full=true>
- **2026-08-03**〔多源交叉〕 'MiniMax H3 Day-0 Support in ComfyUI: Open Weights, Native Audio, and 2K Video' 上 HN 首页，334 分 94 评论——模型厂把 ComfyUI day-0 模板当官方发布渠道  
  来源：<https://hn.algolia.com/api/v1/search_by_date?query=ComfyUI&tags=story&hitsPerPage=20>
- **2026-08-04**〔多源交叉〕 H3 ComfyUI 生态一个月内爆发：H3-Motion-Context（993★，跨镜头动作/音频接续）、MiniMaxH3-Director（297★，时间线编辑器）、H3-FaceRefine（424★，小脸修复）、VDN-H3（238★，原生注意力节点）、Prompt-Writer（217★）、Image-Studio（174★）  
  来源：<https://api.github.com/search/repositories?q=topic:comfyui+created:%3E2026-06-22&sort=stars>
- **2026-08-30**〔官方源〕 中文社区 suihe1/short-drama-production（163★，Apache-2.0）：用 production.json 把短剧生产串成有状态链（hash 绑定审批、QC 返工门），生成走 MiniMax 官方/CompShare 适配器，README 明言 ComfyUI 集成'属于可扩展接入方向，并非开箱即用内置节点'——证明生产契约需求存在而 ComfyUI 侧空白  
  来源：<https://raw.githubusercontent.com/suihe1/short-drama-production/main/README.md>
- **2026-09-02**〔官方源〕 头部 wrapper 断档确认：WanVideoWrapper（6,708★，1,282 open issues）最后提交停在 2026-05-24，90 天窗口内零更新；同期 KJNodes（3,306★，9-13）与 VideoHelperSuite（1,849★，9-02）持续维护。kijai 本人转向 ComfyUI fork、comfy-kitchen 内核库、MemoryVisualization（192★）及 musubi-tuner LTX-2 分支  
  来源：<https://api.github.com/repos/kijai/ComfyUI-WanVideoWrapper/commits?per_page=5>
- **2026-09-16**〔官方源〕 H3 本地化蒸馏/量化持续涌现：FastVideo FastH3 4/8-step（NVFP4）、MLX INT8/INT6 社区版（9-16/17），本地推理门槛快速下降  
  来源：<https://huggingface.co/api/models?pipeline_tag=text-to-video&sort=createdAt>
- **2026-09-20**〔官方源〕 H3 相关 LoRA 生态起步：asmr-trigger-audio-h3-lora（187 下载）、MiniMax-H3-Multishot-Workflow（14 下载）——社区用 HF 承载 H3 LoRA，trigger-word 约定、无统一元数据格式  
  来源：<https://huggingface.co/api/models?pipeline_tag=text-to-video&sort=createdAt>

### 做得好（可借力）

- MiniMax H3 的 day-0 ComfyUI 支持模式：模型厂直接把 ComfyUI 模板作为官方发布渠道之一（HN 334 分证明社区认可），新模型冷启动成本极低
- Wan 系列全线 Apache-2.0：开源视频模型里最宽松 license，生态摩擦最小，商用无顾虑
- Lightricks IC-LoRA 体系：官方把'控制'（upscale/outpaint/detailer/ingredients）做成标准 LoRA 组件，控制件商品化路径已被验证
- ComfyUI 官方补 agent 基础件：comfy-mcp 让 AI agent 驱动本地 ComfyUI，方向明确且仍在高频迭代（9-20 push）
- 头部 utility nodes（KJNodes 3,306★、VideoHelperSuite 1,849★）维护稳定，ComfyUI 主仓库 134,295★ 窗口内日更
- 头部维护者 kijai 转向底层（comfy-kitchen 内核库、MemoryVisualization 内存可视化）——说明性能/内存层开始被最高水平贡献者投入

### 将要发生（可搭车）

- H3 蒸馏版迭代节奏（FastH3 8-step V2 于 9-16/17 刚发）→ 预计消费级单卡跑 2K 音视频生成在 1-2 个季度内成为默认预期，本地推理优化工具需求持续放大
- ComfyUI 官方 agent 化路线（comfy-mcp）→ 官方在做'agent 驱动生成'，第三方若做'agent 驱动生产管理'层正好错位互补
- LTX IC-LoRA 体系 9-01 一次更新 3 个控制件 → 控制件持续商品化，各模型 base 的 IC-LoRA 兼容/转换层会出现需求
- vrhino（'self-contained native runtime and model format for local AI video generation'，8-27 起）→ 本地视频推理的容器化/标准化封装趋势已有人抢跑，验证了'运行时+模型格式'方向
- H3/LTX 均为自定义 community license → 随生态做大，商用授权条款大概率演进，license 合规工具/信息层有价值
- Vidu-S 若补齐 license 开源程度加深 → 实时交互视频生成赛道开源化，交互式工作流（非离线渲染）将成新范式

### 空位（可占位）

- **头部 Wan wrapper 断档无人接盘：生态第一 wrapper（6,708★）窗口内零提交、1,282 open issues 堆积，而 Wan 模型本身仍是 Apache-2.0 存量主力**  
  证据：GitHub API: WanVideoWrapper pushed_at=2026-05-24，最后 5 条提交均早于窗口；kijai 仓库列表显示其精力已转向 ComfyUI fork/comfy-kitchen/MemoryVisualization  
  切入：两条路：fork 接管维护 WanVideoWrapper（直接继承 6.7k 用户基本盘），或做 model-agnostic 的统一视频模型 wrapper 层，把 Wan/H3/LTX 的差异（各自 node pack 互不兼容）抽象掉
- **ComfyUI 无统一任务队列/生产契约：跨镜头长片生产需要状态、依赖、审批、失败恢复，ComfyUI 只有单次 workflow 执行；中文社区已被迫在 ComfyUI 之外自造 production.json 契约（hash 绑定审批、stale 传播、QC 返工门），且 README 明言 ComfyUI 集成'并非开箱即用'**  
  证据：suihe1/short-drama-production README：生产链状态/审批/QC 全部在自有 production-kit.mjs 中实现，ComfyUI 仅列为可扩展方向；Comfy-Org 官方 90 天内只发了 comfy-mcp（执行驱动），未涉及生产层契约  
  切入：把 production.json 式契约做成 ComfyUI 原生节点/扩展：任务 DAG、镜头级状态、审批门、断点续跑——短剧/广告批量生产场景直接付费意愿最强（该 repo 8-30 创建已 163★）
- **判片/QC 验收节点缺失：H3 生态一个月长出的十几款节点全在生成侧（接续、修复、提示词、时间线），没有任何标准化的'机器判片'节点（质量评估、镜头一致性检查、口型/音频对齐校验、批量验收打分）；QC 仅存在于链下脚本（FFmpeg 粗剪 QC、离线 HTML 分镜查看器）**  
  证据：GitHub topic:comfyui 新 repo 列表逐项核对：Motion-Context/FaceRefine/Director/Prompt-Writer/Image-Studio 均为生成或修复侧；short-drama-production 的 QC 也是链下 post-kit.mjs+人工审批  
  切入：VLM-as-judge 视频判片节点：接 H3/Qwen-VL 本地模型输出结构化评分（构图/一致性/时长/音频对齐），与生产契约的审批门对接——这是把'人类审片'自动化的空白位
- **LoRA/控制件无可移植格式：同一创意资产要为每个 base 重复打包（CivitAI 采样到一个 LoRA 同名发布 Krea2/Qwen/Wan/HiDream/Flux 五个版本）；HF 社区 H3 LoRA 只有 trigger-word 口头约定；LTX 用自家 IC-LoRA 命名体系；无统一的 trigger/推荐参数/base 兼容矩阵声明格式，工具链无法自动校验兼容性**  
  证据：CivitAI API 采样（Elsa 测试 LoRA 携 5 个 base 版本）；HF text-to-video 最新上传中 H3 LoRA 无 schema；'Wan Video 2.2' 精确枚举查询返回空（baseModel 枚举名碎片化佐证）  
  切入：定义 LoRA portability manifest（trigger words、推荐 CFG/steps、base 兼容矩阵、checksum）+ ComfyUI 校验/自动映射节点；CivitAI 下载量最大的痛点就是装错版本
- **license 碎片化无决策工具：Wan（Apache-2.0）vs H3/LTX（自定义 community license）条款完全不同，团队选型时无法程序化判断商用可用性**  
  证据：HF API license tag 对照：Wan-AI 全系 apache-2.0；MiniMax-H3 为 minimax-h3-community-license-agreement；Lightricks 全系 license:other  
  切入：低成本切入：开源 license 合规对照表/CLI 检查器，随生产契约一起分发

### 未决问题

- CivitAI 视频 LoRA 精确数量级无法核实：v1 API 不返回 totalCount（metadata 仅含 nextCursor）；'Wan Video 2.2' 精确 baseModel 枚举查询返回空 items，真实枚举名（如 'Wan Video 14B t2v'）导致统计口径不清，需登录态或尚未公开的 stats API
- CivitAI 窗口内（2026-06-22 后）政策变化未发现公开公告：newsroom 最新条目为 2026-04-09 'Two Front Doors'（civitai.com/civitai.red 域名拆分，属窗口前背景）；本会话 WebSearch 预算耗尽，无法检索媒体报道交叉验证版权清理/付费墙变动
- comfy.org/blog 与 blog.comfy.org 均抓取失败/无文章列表（newsletter 形式），ComfyUI 官方 90 天内视频相关正式公告（如 native Wan 2.2 模板）未能一手核实
- MiniMax-H3 community license 的具体商用限制条款未读取全文（仅确认非 Apache、文件为 docs/QA-about-License.md）
- Vidu-S GitHub API license=null，宣称'开源'但默认保留所有权利，实际开放范围待查
- Gaps 判断基于 GitHub topic:comfyui 与 video-generation 两个搜索面 + HN，可能遗漏未打 topic 的项目

### 来源

- [GitHub API: kijai/ComfyUI-WanVideoWrapper（stars/pushed_at/commits）](https://api.github.com/repos/kijai/ComfyUI-WanVideoWrapper)
- [GitHub API: kijai 仓库列表（转向证据）](https://api.github.com/users/kijai/repos?sort=pushed)
- [GitHub API: kijai/ComfyUI-KJNodes](https://api.github.com/repos/kijai/ComfyUI-KJNodes)
- [GitHub API: Kosinkadink/ComfyUI-VideoHelperSuite](https://api.github.com/repos/Kosinkadink/ComfyUI-VideoHelperSuite)
- [GitHub Search: 窗口内新建 video-generation 仓库](https://api.github.com/search/repositories?q=video+generation+created:%3E2026-06-22&sort=stars)
- [GitHub Search: 窗口内新建 topic:comfyui 仓库](https://api.github.com/search/repositories?q=topic:comfyui+created:%3E2026-06-22&sort=stars)
- [GitHub API: shengshu-ai/Vidu-S（license=null）](https://api.github.com/repos/shengshu-ai/Vidu-S)
- [HuggingFace API: Wan-AI 全模型（全 Apache-2.0）](https://huggingface.co/api/models?author=Wan-AI&sort=downloads)
- [HuggingFace API: MiniMaxAI/MiniMax-H3 模型卡（404万月下载/33.1B/自定义license）](https://huggingface.co/api/models/MiniMaxAI/MiniMax-H3?full=true)
- [HuggingFace API: Lightricks 全模型（LTX-2.5 等）](https://huggingface.co/api/models?author=Lightricks&sort=downloads)
- [HuggingFace API: text-to-video 最新创建模型（蒸馏/LoRA 生态）](https://huggingface.co/api/models?pipeline_tag=text-to-video&sort=createdAt)
- [HN Algolia: ComfyUI 相关窗口内故事（MiniMax H3 Day-0，334分）](https://hn.algolia.com/api/v1/search_by_date?query=ComfyUI&tags=story&hitsPerPage=20)
- [CivitAI API: Wan Video base LORA 采样（无 totalCount）](https://civitai.com/api/v1/models?types=LORA&baseModels=Wan%20Video&sort=Newest)
- [CivitAI Newsroom（最新公告 2026-04-09，窗口内无）](https://civitai.com/newsroom)
- [suihe1/short-drama-production README（production.json 契约/链下QC/ComfyUI非内置）](https://raw.githubusercontent.com/suihe1/short-drama-production/main/README.md)


## 开源生态 · 数据集与版权/训练数据供给

**摘要**：90天窗口内四条线索清晰：①开源视频数据集"有量无权"——LAION-BVD（1000万小时/8000万视频，8月发布）是最大开源视频文本集但明确禁止商用；Netflix开源Apache-2.0分层视频集（权利人直发范式）；TikTok 4.5B条仅为违约采集的元数据。没有任何大规模可商用license的视频-文本数据集发布。②授权市场图片先行、视频缺席：Getty-OpenAI检索授权（6/22，股价+145~200%）、Getty-Shutterstock 37亿美元合并终止（7/1）、Getty发MCP Server把授权API化——均不含视频训练授权。③诉讼侧：Anthropic 15亿美元和解获批（7/20）确立数据定价锚；MPA-ByteDance签首个AI版权协议（8/16）但只治输出侧，训练数据责任留白；Suno源码泄露、Apple/Twitch案显示抓取型供给全面承压。④中国：备案常态化（累计988款、端侧首批7款）、类人AI新规在途、执法集中在内容侧；训练数据灰市活跃（0.85元素材包、15美元租脸）。核心判断：合规训练视频数据供给是全链条最大空白，直接决定视频LoRA串联机会的形态——数据包+license工具+备案材料生成是可占位位。

### 90 天时间线

- **2026-06-22**〔多源交叉〕 Getty Images 与 OpenAI 签多年内容授权（授权视觉内容进入 ChatGPT/检索），GETY 盘中涨 145%–200%；属图片/检索侧授权，未见视频训练权  
  来源：<https://news.google.com/rss/articles/CBMihgFBVV95cUxOVWdwaFNWeE41a2Z5UXN4b1hBODN3cE1jV05mcWxYOWhTNHB5UGRCdE1EZnNPdzd3VDFWUVJTSjRnRnNxWURNSVJmTWY5QVhEbWlXY2xvamtZUk9tbkZ5d2k5MUctSjlUV1praWpNQU8yczE0ZUNfQkd0S2JmNm91U25fQlhadw?oc=5>
- **2026-06-22**〔单一来源〕 中国知识产权律师网载文：AI短剧素材包低至0.85元，侵权隐患重重——中文侧灰市训练/素材供给的缩影  
  来源：<https://news.google.com/rss/search?q=AI%20%E7%89%88%E6%9D%83%20%E5%88%A4%E5%86%B3%20%E8%A7%86%E9%A2%91%20after%3A2026-06-22&hl=zh-CN&gl=CN&ceid=CN:zh-Hans>
- **2026-07-01**〔多源交叉〕 Getty 终止35亿美元收购 Shutterstock：英国CMA要求剥离Shutterstock全球编辑业务（含Backgrid/Splash），尽管美国DOJ已无条件放行；两大图库独立后均面临AI竞争  
  来源：<https://www.theverge.com/tech/960047/getty-shutterstock-merger-agreement-termination>
- **2026-07-03**〔单一来源〕 Apple 在版权诉讼中辩护称抓取 YouTube 视频用于 AI 训练——消费级视频抓取的合法性问题正式进入法庭  
  来源：<https://news.google.com/rss/articles/CBMieEFVX3lxTE9USzNYLWNSdWY1UWxNdWlWakhCYXVCYVdCSXZVRVZHVndycnBqbjlTUDRwaUl2NG5valRkN2JMOGJXRFdfRFk3b3hxeVoxdmFuUXdzZHpaRzF2VHhrR05JQlI0Y185aTFNWi1tNUpNV2dPT3dkTjZOWQ?oc=5>
- **2026-07-06**〔单一来源〕 SCMP：类人AI新规临近，字节跳动与阿里巴巴下线拟人化AI智能体——中国AIGC合规执法从内容扩展到产品形态  
  来源：<https://www.scmp.com/tech/big-tech/article/3359482/bytedance-and-alibaba-disable-humanlike-ai-custom-agents-new-rules-loom>
- **2026-07-10**〔官方源〕 国家网信办：截至6月30日累计988款生成式人工智能服务完成备案（央视网报道官方口径）  
  来源：<https://news.google.com/rss/search?q=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%20%E5%A4%87%E6%A1%88%20after%3A2026-06-22&hl=zh-CN&gl=CN&ceid=CN:zh-Hans>
- **2026-07-09**〔官方源〕 Netflix 在 HF 开源 Vera-Layered-Video-Dataset：Apache-2.0、1–10万段分层视频、text-to-video/分层扩散（arXiv 2606.23610）——权利人直接开放自有内容的少数案例  
  来源：<https://huggingface.co/datasets/netflix/Vera-Layered-Video-Dataset>
- **2026-07-15**〔多源交叉〕 网信办公示首批7款手机端侧生成式AI服务备案（Apple智能、华为、小米MiMo、努比亚豆包、三星等），评论称进入"持牌经营"阶段；小米同日宣布3年AI投入不低于600亿元  
  来源：<https://news.google.com/rss/search?q=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%20%E5%A4%87%E6%A1%88%20after%3A2026-06-22&hl=zh-CN&gl=CN&ceid=CN:zh-Hans>
- **2026-07-15**〔单一来源〕 Suno 源码遭黑客泄露，曝光其从 YouTube 等平台抓取数百万歌曲训练——抓取型数据供给的法律暴露面被实证（音频案例，模式适用于视频）  
  来源：<https://news.google.com/rss/articles/CBMidkFVX3lxTFBvMFNzSWN2Mzk4cVV0UUpHN0hyS0ZkeFZ3OERpbnlIaFVFQzMzYVpUXy1WdTFQemZGR1NZdGp4eDJnamdHMno3Z0llTElpVTFFbXRaMW94X01IWnFJT0p4TDBocFdvTEhTekgxNUpfVWlfdmx5d1E?oc=5>
- **2026-07-20**〔多源交叉〕 美国法官批准 Anthropic 15亿美元图书版权和解——首个大型训练数据定价锚，媒体称开启"AI数据定价时代"  
  来源：<https://www.reuters.com/world/us-judge-approves-anthropics-15-billion-settlement-copyright-lawsuit-2026-07-20/>
- **2026-07-31**〔官方源〕 中国视频模型分叉：字节 Seedance 2.5 保持闭源（30秒/4K/多参考），MiniMax 同期开源 H3（33B全模态、原生立体声；至9/21 HF下载405万、license:other 社区许可证，美欧英韩部署需申请）——开源侧出现可LoRA微调的视频底模  
  来源：<https://huggingface.co/MiniMaxAI/MiniMax-H3>
- **2026-08-04**〔多源交叉〕 路透：MiniMax 因版权争议收紧 H3 海外使用；同日媒体披露 H3 开放权重对美国/欧盟/英国/韩国本地部署设限——中国厂商因版权风险主动收缩开源边界  
  来源：<https://news.google.com/rss/articles/CBMizgFBVV95cUxPQkZndl9IdGFDU203YzVFLW12VWxmNlc4N1JwUnZSZjZJTUNBM012cE1BZ3hmQ0kya05DSlppTEZOWDJ0NHFlTjRzajNRZlhLajBBR0RNYVJxdWtfWi1iamFUZm5hT3dXQTlXb3ctc3BTTGgtVTVzSW5zWUJhZENuV280SjRSYUJhN3dsamVRRnlGMjhmZjZmRFBBNEdfdG9kSUpVb2wtZ0dwdzlEdjZJS0JiYXJRVU5WWkVFbkZnaW1RYm1icHRkRHlNVXkydw?oc=5>
- **2026-08-13**〔单一来源〕 Getty 发布 MCP Server，将创意/编辑内容接入 AI 工作流与产品——版权方把授权做成 agent 可调用的基础设施  
  来源：<https://news.google.com/rss/articles/CBMiiAJBVV95cUxNcU41UWJtWWJKYWlDZlFRZXh6MS1DVnRocml2STlkRG1RQWtMWmNzUzk0b254SHBZNW5RSVVuVG50Q09QZHZQcU1ZVy1GcGpPSDVLb21lSWtjVVlnSUstRVlQTDlMRG9TOVY0T1NZVkhTeGlCaDJsRFpiaUp6OG9sQlh1RFlmMnVldzBrdWl6UFduQi1tUzhvRlhvcGU3SzUxWi1fRC1Sc2ZjLUVhX1M5UXJxb1NvVGpDT3JBWkMyZVdscENJWmU4SktMWlhLVnljMk1QaklGVDhwSDlOUm5UTnhhWUFJanZiYmRmRE9hQkRRUDJ0MzRPNWk2OUl2Y0RxUm1aX0Q3aXLSAY4CQVVfeXFMTjlzU0R2S19NUjRsb1BfQ3otMWF3Znh3NmpLbm5sWUZHZ1JDZHg0MHdTNTU3LVVMSWlkdUN2aXB4bXctTDVhNVM4V0xURURjcHNsTlMwdzB0ZFdvMVNJRElJTlQzWkdKTURtS181bWNwNVB4QUtQaEQ2TGh2UHRLV05kVW43U092Y3E1VURpb05LdVlZN2pmcWh4SlV5OXJyOHZqaUpiTDFhdlhPXzhfYmFtU1YyYlFWcUJHdmFWeGFkeHhJYV9YMzlNNkJUSV9lNlpKbmxNbmhvcHlnbndXWWltQWw1U2FoeFFDWUlaNmtxZktBQ2JFRS0tQ2VjS2YtcGtWbTZuRXhNc0NOX21R?oc=5>
- **2026-08-17**〔多源交叉〕 MPA 与 ByteDance 签全球首个 AI 版权保护协议，覆盖 Seedance/Seedream 视频与图像模型的输出侧 IP 保护（迪士尼/环球/华纳背景）；TechTimes/36kr 指出训练数据（输入侧）责任仍在诉讼中、留待再议  
  来源：<https://news.google.com/rss/articles/CBMiywFBVV95cUxNMmlJVERMbEdidWhCLURCT0ZKcW1YbTE5OXk0cTFnMmU5ZG1hVVEzRWFRREp2X3J6TWNKNU9ENEF6ZllDem1YWEI3S0c4cWVhRmFpZjFqRUx4ZXNKZmdnYjNtX2s2WmRmY0Vxb3UyLURuSmFqZ2JxM3JPLTFqaHJ3Q3BJQTlRQmw2dC1EOE10Vzh3bzI5VFhacDdKOHFmc0t1MU9VSlh2T25BSWtPVzBReGNaS0ZUQmMtdE9CZ1hnUzJfcGNhdF9OSTZIYw?oc=5>
- **2026-08-26**〔官方源〕 LAION 发布 Big Video Dataset（arXiv 2608.24845）：13亿视频URL/成功下载8000万条/1000万小时/5500万合成字幕片段/3亿帧，明确"仅限研究、禁止商用"——90天内最大开源视频发布仍与商用无缘  
  来源：<https://projects.laion.ai/bvd/>
- **2026-09-03**〔官方源〕 4.5B 条 TikTok 视频记录集上架 HF（289GB、27个parquet、仅元数据无视频文件；license: research-use；发布者自认采集违反 TikTok ToS、属 GDPR 个人数据）——灰色大规模供给与合规真空并存  
  来源：<https://huggingface.co/datasets/kuben-developer/tiktok-videos-4b>

### 做得好（可借力）

- 权利人直发范式成立：Netflix 以 Apache-2.0 开源自有分层视频集（10K–100K段，HF 10.7K下载/59赞），证明版权方自持内容+宽松license+小规模是当前唯一'干净'路径
- LAION-BVD 把 URL 分发+合成字幕+场景切分的全流水线开源化（1.3B URL/55M片段），可复现的数据基础设施成熟，只差商业许可这一层
- 开源视频底模供给侧爆发：MiniMax-H3 开源即获 405万下载、5565赞，证明个人/小团队对可微调视频模型的需求真实且巨大，LoRA 串联有载体
- 版权方开始 API 化授权：Getty MCP Server（8/13）让授权内容可被 agent 直接调用，'授权即基础设施'的形态已经出现
- 中国备案机制高频可预期：CAC 累计公示988款（至6/30）、端侧首批7款批量放行，'持牌经营'路径清晰，合规成本可测算
- 行业出现首个输出侧自律模板：MPA-ByteDance 协议（8/16）给出视频生成平台 IP 合仁的结构，可被后续厂商复用

### 将要发生（可搭车）

- MPA-ByteDance 协议明确把输入侧（训练数据）留作'再议'（36kr 8/20）——视频训练数据授权谈判是下一个必然发生的动作，围绕它会出现第一批视频版权授权产品
- Anthropic $1.5B 和解获批（7/20）把'每作品定价'变成现实锚点——影视/视频权利人会要求同量级和解或授权，'视频版 Anthropic 时刻'大概率在未来2-3个季度出现
- Getty 合并告吹后独立运营、急需 AI 收入：'authentic verified content'战略+OpenAI 检索授权大概率向视频素材和训练权延伸；Shutterstock 同理（7/16 平台化、7/23 无限下载扩张都是变现铺垫）
- EU AI Act 训练数据透明度义务已可执行（MBW 8/4 报道'now law and enforceable'）——来源元数据/provenance 工具从加分项变成合规刚需
- Seedance 已在输出侧屏蔽好莱坞 IP（8/12），输出过滤会倒逼输入侧权利清单——内容指纹/rights-matching 基础设施需求将前置到训练阶段
- 中国类人 AI 新规在途（SCMP 7/6）+ 情感陪伴执法（8月 Doubao）——训练数据来源审查可能被纳入备案材料要求，'备案级数据文档'会成为标准交付物

### 空位（可占位）

- **没有任何大规模、可商用 license 的开源视频-文本数据集：90天内最大开源发布 LAION-BVD（10M小时）明确禁止商用；TikTok 4.5B 集是违约采集的元数据（无视频文件、research-use）；HF 近90天检索无 CC-BY 级视频文本大集发布**  
  证据：LAION 官网原文 'released exclusively for research purposes and not for commercial use'；HF API/页面核验（projects.laion.ai/bvd/、hf.co/datasets/kuben-developer/tiktok-videos-4b）  
  切入：做第一个'商用干净'的中型视频 LoRA 数据集（CC/授权素材/自有拍摄，5万–50万 clip 级），逐条附权利链证明与商用许可——规模让位于可商用性，直接卖给用开源底模训 LoRA 的小团队
- **视频版权授权未跟上图片节奏：窗口内 stock 方全部大动作（Getty-OpenAI 检索授权、Getty MCP、Shutterstock 产品化）均不含视频训练授权；对比图片侧已有'授权替代诉讼'成熟叙事**  
  证据：Google News 窗口内 Getty/Shutterstock/Adobe 全条目盘点（60+条）无一涉及视频训练授权；Getty-OpenAI 被多源描述为 ChatGPT 检索/视觉内容供应  
  切入：stock footage 训练授权中介：把 mid-tier footage 库/UGC 版权方与视频模型团队对接，按 clip 定价+贡献者分成，补上 Getty 们还没做的视频版交易基础设施
- **视频 LoRA 训练数据供给完全无组织：社区实践是模型自生成的1000对（ostris/minimax_h3_1k，license:null，94赞）或0.85元侵权素材包；HF 全部 'video lora' 数据集均无 license 标签**  
  证据：HF API：ostris/minimax_h3_1k license:null、jbilcke-hf 三个 video-lora 集均无 license；ciplawyer.cn 6/22 短剧素材包报道  
  切入：'合规 LoRA 数据包 + license lint 工具'：数据集许可证扫描器、C2PA 溯源附着、一键生成数据来源说明——工具免费获客、数据包收费
- **输出侧合规先行、输入侧（训练数据溯源/审计）工具空白：MPA 协议只治输出，ByteDance 训练责任仍在诉讼；Suno 源码泄露式风险没有任何面向视频团队的训练语料审计工具来防**  
  证据：TechTimes 8/18 标题 'ByteDance Training Liability Stays in Court'；36kr 8/20 输入侧'再议'；Suno 泄露报道 7/15-16  
  切入：训练数据合规即代码：来源注册表+侵权风险审计（泄露/抓取内容指纹比对）+ 中国备案材料自动生成，面向使用开源底模的团队
- **中国侧备案常态化但训练数据来源无细则、无标准工具，灰市在填补空白（15美元租脸、0.85元素材包）——合规供给缺位与执法收紧并存**  
  证据：CAC 备案公示高频运转（988款、端侧7款）但窗口内无训练数据来源新规文本；RestOfWorld 8月租脸报道、ciplawyer 素材包报道  
  切入：面向中国视频生成团队的'备案级'数据供给服务：授权链数据+备案数据来源说明模板，卡位新规落地前的空窗

### 未决问题

- Getty-OpenAI 交易的确切范围：是否含视频素材、是否含训练权？多源标题一致（授权视觉内容进 ChatGPT），但官方新闻稿 URL 本会话未能直接打开验证，细节靠媒体转述
- 窗口内是否签署过未公开的 stock 视频/UGC 训练授权（Shutterstock、Adobe Stock 与模型厂商）？本次检索未发现，但不排除低调签约
- MiniMax-H3 Community License 对商用的具体条款：模型卡未复现许可正文（只链 LICENSE 与 FAQ），'美欧英韩需申请'的完整边界未核实
- Netflix Vera-Layered-Video-Dataset 底层画面是否全部为 Netflix 自有版权内容（Apache-2.0 是数据集许可证，不等于底层内容授权）
- 中国是否会出台训练数据来源合规的部门规章级新规：窗口内只有'新规在途'（类人AI）与备案执行信号，无数据源细则文本
- TikTok 4.5B 数据集的法律后续：发布者已自认违反 ToS 并提供 opt-out 删除通道，下架/集体诉讼风险未发生但存在
- WebSearch 配额本会话耗尽（200/200），依赖 HN Algolia/GitHub/HF/Google News RSS 一手 API 交叉，个别中文报道未能拿到直链，建议后续用站内检索补直链

### 来源

- [LAION Big Video Dataset 官方项目页（10M小时/禁止商用）](https://projects.laion.ai/bvd/)
- [Netflix Vera-Layered-Video-Dataset（HF, Apache-2.0）](https://huggingface.co/datasets/netflix/Vera-Layered-Video-Dataset)
- [TikTok 4.5B posts dataset（HF, research-use, 自认违反ToS）](https://huggingface.co/datasets/kuben-developer/tiktok-videos-4b)
- [MiniMax-H3 模型卡（HF, 社区许可证/地理门槛）](https://huggingface.co/MiniMaxAI/MiniMax-H3)
- [ostris/minimax_h3_1k 社区 LoRA 数据集（HF, 无license）](https://huggingface.co/datasets/ostris/minimax_h3_1k)
- [The Verge: Getty 终止 Shutterstock 合并（UK CMA 条件）](https://www.theverge.com/tech/960047/getty-shutterstock-merger-agreement-termination)
- [Reuters: 法官批准 Anthropic 15亿美元版权和解](https://www.reuters.com/world/us-judge-approves-anthropics-15-billion-settlement-copyright-lawsuit-2026-07-20/)
- [SCMP: 字节/阿里下线类人AI智能体，新规在途](https://www.scmp.com/tech/big-tech/article/3359482/bytedance-and-alibaba-disable-humanlike-ai-custom-agents-new-rules-loom)
- [RestOfWorld: 北京强制下架 AI 恋人（Doubao 执法）](https://restofworld.org/2026/china-ai-boyfriend-ban-bytedance-doubao/)
- [HN Algolia（按日期）：Getty/ByteDance/copyright 事件一手索引](https://hn.algolia.com/api/v1/search_by_date?query=ByteDance&tags=story&numericFilters=created_at_i%3E1782086400)
- [Google News RSS（中文）：人工智能备案 90天检索结果（988款/端侧7款等）](https://news.google.com/rss/search?q=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%20%E5%A4%87%E6%A1%88%20after%3A2026-06-22&hl=zh-CN&gl=CN&ceid=CN:zh-Hans)
- [Google News RSS（英文）：Getty/Shutterstock AI 授权 90天检索结果](https://news.google.com/rss/search?q=Shutterstock%20OR%20Getty%20AI%20video%20licensing%20after%3A2026-06-22&hl=en-US&gl=US&ceid=US:en)
- [Google News RSS：MPA AI copyright 检索（LA times/Variety/Reuters/TikTok newsroom 多源）](https://news.google.com/rss/search?q=%22Motion%20Picture%20Association%22%20AI%20copyright%20after%3A2026-06-22&hl=en-US&gl=US&ceid=US:en)
- [GitHub API: 2026-06-22 后新建 video dataset 仓库（CoinVE-200K MIT 等）](https://api.github.com/search/repositories?q=video+dataset+created:%3E2026-06-22&sort=stars&order=desc)
- [HN: LAION Big Video Dataset 讨论（91分）](https://news.ycombinator.com/item?id=projects.laion.ai/bvd)
