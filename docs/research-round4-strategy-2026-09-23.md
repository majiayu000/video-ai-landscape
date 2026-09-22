# 第四轮 · 战略理论研究（2026-09-23）

> 方法：6 路 schema 约束 agent 检索（2 波 × 3，run wf_ff44befa，6/6 零失败，173 次工具调用）。
> 产出物性：35 个历史案例 + 33 条定律，每条定律 = 案例证据 + 对中立契约层的推论。
> 纪律：历史案例允许任意年代来源；2026 现状断言限 90 天一手源 + 置信度标注；商业数字注明未经审计。
> 上层合成见 （战略纲领）。


## 抽象层幸存者前例（Stripe/Twilio/Plaid/Zapier/OpenRouter/HashiCorp/Docker）

**摘要**：七个案例揭示同一结构：抽象层幸存的必要条件是——下层极度碎片化、自己持有状态资产（账户/工作流/授权/信任）、对下层是"帮它卖"的增量关系而非截流。Stripe/Twilio/Plaid/Zapier 由此独立壮大；无状态路由的 OpenRouter 从 2026-05-30 的 $1.3B 估值到 2026-08-19 官宣被 Stripe 收购（报道价约 $7.5B，未经审计）；HashiCorp 2023 年 BUSL 收紧中立性后被社区分叉反噬、终卖 IBM；Docker 亲手把容器格式捐成开放标准——生态永生、商业公司被挤出平台层。对契约层的推论：格式开放+中立治理，商业价值放在标准之外的验收执行与角色资产上；拒绝任何单厂商绑定；把模型碎片化当计时器而非永恒结构。

### 案例

- **Stripe（对银行卡网络的抽象）**（2010–至今）→ 结局：**幸存并独立壮大**〔多源交叉〕
  - 经过：2010 年 Collison 兄弟创立，2011-09 公开发布，约 4-5 年成为美国初创支付默认选项（推断），统治位置延续至今。估值轨迹：2021-03 $95B → 2023-03 $50B（腰斩危机）→ 2025-02 $91.5B → 2026-02 tender $159B。2025 年 TPV 超 $1.9T（+34%），2024 年营收 $5.1B（公司口径，未经审计）。2026-08-19 以报道价约 $7.5B 收购 OpenRouter（官方公告未披露价格）。差点死掉：2022-2023 估值从 $95B 跌至 $50B，靠盈利与 AI 支付叙事恢复。
  - 关键因子：下层（数千银行+全球卡组织）极度碎片化且整合壁垒高；把合规/风控/拒付/商户账户打包成信任品牌，是下层给不了的增值；与卡组织是增量关系（带来交易量），从不截流；开发者生态与文档成为分发渠道
  - 来源：<https://en.wikipedia.org/wiki/Stripe,_Inc.>
- **Twilio（对电信运营商的抽象）**（2008–至今）→ 结局：**幸存并独立壮大**〔多源交叉〕
  - 经过：2008 年创立，对运营商语音/短信做 API 抽象，定义 CPaaS 品类；约 8 年到 IPO（2016-06-23，首日 +92%）。SendGrid 2018（$3B）、Segment 2020（$3.2B）。注意：经核实 Twilio 至今独立上市（2025 营收 $5.07B、净利 $33.8M），未被 Salesforce 收购——任务前提需修正。差点死掉：2022-09 裁员 11%、2023-02 再裁 17%、2024-01 创始人 Jeff Lawson 在激进投资者施压下卸任 CEO，出售传闻未兑现，现任 CEO Khozema Shipchandler 转向利润重建并于 2025 收购 Stytch。
  - 关键因子：运营商关系+全球号码/合规是难以复制的稀缺资产；抽象本身可替代性强（Telnyx/MessageBird 更便宜），溢价被竞争压掉；纯 API 转发缺乏状态锁定 → 高增长不可持续，被迫并购扩面（SendGrid/Segment）消化不良；危机后靠收缩+多产品组合保住独立地位
  - 来源：<https://en.wikipedia.org/wiki/Twilio>
- **Plaid（对银行数据接口的抽象）**（2013–至今）→ 结局：**仍在竞争中**〔多源交叉〕
  - 经过：2012 年立项、2013 年成立，一个 API 连接上万家银行，约 5-7 年成为美国金融科技默认数据层（Venmo/Chime 等）。Visa 2020-01-13 宣布 $5.3B 收购（其 CEO 明言是对'威胁美国借记业务'的保险），2021-01-12 被 DOJ 反垄断阻止而放弃。估值：2021-04 $13.4B → 2025-04 降至 $6.1B（-54%）→ 2026-02 员工股转让 $8B（仍低于峰值 40%，未经审计）。2025-07 Chase 公开称 Plaid 类中间商'massively taxing'其 API，2025-09 Bloomberg 报道双方达成数据协议——抽象层被下层从'免费水管'改造成'受控付费渠道'。
  - 关键因子：万级银行连接覆盖+消费授权流成为行业标准是护城河；被监管阻止收购反而保住了中立席位与独立估值曲线；下层最大玩家（Chase）一旦把数据当资产收费，抽象层议价权立刻受损；估值从 $13.4B 到 $6.1B 说明：下层管控收紧 = 抽象层价值折价
  - 来源：<https://en.wikipedia.org/wiki/Plaid_(company)>
- **Zapier（对 SaaS API 的集成抽象）**（2011–至今）→ 结局：**幸存并独立壮大**〔多源交叉〕
  - 经过：2011 年项目启动、2012 年 YC 后正式运营，约 4-5 年确立 SaaS 自动化统治位置（2016 年 60 万用户，2018 年 $35M ARR）。2014 年起盈利，累计外部融资仅约 $1.3M，2021-01 二级交易估值 $5B（未经审计）。2026 年连接 9000+ 应用、66,000+ trigger/action，2026 年推出官方 MCP 集成让 Claude/ChatGPT 直接驱动 Zapier 工作流——在 agent 新范式里主动换位而非被绕过。从未有过濒死时刻，是七案中唯一无危机者。
  - 关键因子：下层 SaaS 数量超线性增长 → n² 集成问题随时间变大，抽象价值递增；持有工作流状态+用户习惯+应用目录三层锁定，是纯路由不具备的；对下层 SaaS 是需求分发渠道（帮它获客），无人有动机杀死它；不融资=无退出压力，可用永续视角经营
  - 来源：<https://en.wikipedia.org/wiki/Zapier>
- **OpenRouter（对 LLM API 的路由抽象）**（2023–至今（2026-08 加入 Stripe））→ 结局：**被收购**〔官方源〕
  - 经过：2023 年 Alex Atallah 与 Luis Vichy 创立，约 2 年成为 LLM 路由默认选项：官方口径 400+ 模型、日处理 10T+ tokens、10M+ 开发者、年 10x 推理增速。2026-05-30 Series B $113M（CapitalG 领投）估值约 $1.3B；82 天后：2026-07-23 WSJ 报道约 $10B 谈判 → 2026-08-16 Bloomberg 报道 $7B+ 成交 → 2026-08-19 官方博客确认'OpenRouter is Joining Stripe'，承诺 same name/product/roadmap；报道价约 $7.5B（官方未披露，未经审计）。HN 评论引泄露分析称其营收约 $50M、约 140x 收入倍数（单一来源、未证实）。交割后仍正常发版（2026-09-22 Batch API）。
  - 关键因子：存活靠模型市场短期极度碎片化+迭代极快（A/B/failover/预付费绕限额）；约 10% 加价的无状态转发，接口向 OpenAI 兼容标准收敛后套利空间必然变薄；无状态路由没有独立上市出路，被上层基础设施巨头收购是统计意义的常态结局；独立生存时间窗仅约 3 年——碎片化红利期有多短
  - 来源：<https://openrouter.ai/blog/announcements/openrouter-is-joining-stripe/>
- **HashiCorp（基础设施工具层）**（2012–2025（并入 IBM））→ 结局：**被收购**〔多源交叉〕
  - 经过：2012 年创立（Vagrant/Terraform/Vault/Consul），约 6-9 年统治 IaC 品类，2021-12 IPO（目标估值约 $13B，募 $1.2B）。2023-08 将 Terraform 从开源转 BUSL 授权 → 社区立即分叉 OpenTofu 并交 Linux Foundation 中立托管（drop-in 替代，3900+ providers）——中立性破产被社区'反向吞掉'一块核心资产。2024-04-24 IBM 宣布 $6.4B 收购，2025-02-27 经英国 CMA 审查后交割，Terraform 从此成为 IBM 渠道组件。
  - 关键因子：吃下层云碎片化红利起家，但 AWS/Azure/GCP 原生工具+K8s 生态持续绕行；对社区产出收紧授权 = 亲手触发中立分叉，抽象物本身只有托管权没有所有权；上市后增长放缓、股价深度低于峰值 → 卖给相邻整合方是终局；开源工具层的'社区信任'是不可再生的资产负债表项目
  - 来源：<https://en.wikipedia.org/wiki/HashiCorp>
- **Docker（格式标准化后商业公司失利的反例）**（2008–至今（dotCloud→Docker，2013 更名））→ 结局：**其他（注明）**〔多源交叉〕
  - 经过：2013-10 更名并开源容器引擎，2013-2015 约 2-3 年达生态巅峰。2015-06-22 主导 OCI 开放容器标准，2017-03 把 containerd 捐给 CNCF（12 月 1.0 GA）并在 Moby 项目下开源引擎；编排层（持续计费处）输给 Kubernetes；2019-11-13 将 Docker Enterprise 卖给 Mirantis（价格未披露）并 $35M 重组——公司差点死掉的时刻。此后退守 Docker Hub/Desktop 订阅的开发者工具业务（2022-03 $105M Series C，Bain），2025-02 新 CEO Don Johnson，2025-09-05 收购 MCP Defender 切入 agent 安全。格式赢得一切，公司失去平台。
  - 关键因子：亲手把核心资产捐为中立标准（OCI/containerd/CNCF）换来生态胜利但放弃平台垄断；可标准化的只是格式；编排/持续计费层被 K8s 生态拿走；退守'开发者入口工具'（Desktop/Hub）仍有订阅价值，但不再是基础设施层；公司幸存、生态永生、平台出局——三者可以同时成立
  - 来源：<https://en.wikipedia.org/wiki/Docker,_Inc.>

### 定律

- **L1 抽象层的价值与下层的碎片化程度成正比；下层一旦收敛出单一赢家或单一事实标准，中立抽象层立即贬值。**
  - 证据：Stripe/Twilio/Plaid/Zapier 全部立于极度碎片化下层（数千银行、运营商、全球卡组织、9000+ SaaS）；OpenRouter 因 400+ 模型的短期碎片化 82 天内估值 $1.3B→$7.5B；反例 Docker：OCI 标准化+K8s 收敛后商业公司被挤出平台层。
  - 推论：我们对 Veo/Kling/Seedance/Wan 的碎片化红利是时间窗口不是永久结构。应在窗口期内把价值沉淀到标准之外的状态资产（验收基准、角色资产），并预设'某家视频模型赢家通吃'时的 pivot 路径（转做该赢家生态的验收/合规层）。
- **L2 无状态的路由/转发层必然被收购或利润归零；有状态资产（工作流、账户、授权、信任记录）才有独立生存权。**
  - 证据：OpenRouter 约 10% 加价的无状态转发，3 年内终被 Stripe 收购；Zapier 持有工作流状态+2014 年起持续盈利+9000 应用目录，独立至今；Stripe 的状态是商户/合规/风控记录，Plaid 的状态是消费授权关系。
  - 推论：我们的'契约+验收+角色资产'必须做成留在我们平台、可积累、用户不愿迁移的版本化资产（验收数据集、角色一致性资产库），纯'统一 JSON 格式'转发没有护城河，会重演 OpenRouter 剧本。
- **L3 与下层做增量分配（帮它卖）则共存；一旦在下层玩家之间做裁决式路由并截流收费，就会招致下层官方下场杀死或收费管控。**
  - 证据：Stripe/Plaid 早期为卡组织和银行带交易量，相安无事；Plaid 被 Chase 定性为'massively taxing'（2025-07）后被迫签受控付费数据协议（2025-09）；OpenRouter 在厂商间路由抽成，厂商官方 API/MCP 下场后只剩聚合套利；HashiCorp BUSL 收紧授权，被社区中立分叉 OpenTofu 反杀。
  - 推论：契约层不要做'哪家模型更好'的裁决式路由和流量抽成（那是 fal/OpenRouter 的战场且必招厂商下场）；中立性应体现为'验收与资产格式不偏向任何厂商'，商业模式做厂商愿意付费的'契约兼容性认证/验收基准'——帮厂商自证合格，而非拦截它的需求。
- **L4 中立性是要主动防守的资产：被任一下层玩家拥有，就变成那个玩家的渠道，失去其余所有玩家；中立治理（基金会化）是终极防线。**
  - 证据：Visa $5.3B 收购 Plaid 被 DOJ 阻止（Visa 自认是防守性保险），反而保住 Plaid 的中立席位与后续 $13.4B→$8B 独立估值曲线；HashiCorp 卖给 IBM 后 Terraform 成为 IBM 工具；OpenTofu/Linux Foundation 证明中立托管可立即接管被污染的抽象物。
  - 推论：契约层全部价值押在'不被任何一家视频厂商拥有'。拒绝任何单厂商投资/收购/排他合作；当契约生态足够大时，把规范移交中立基金会（Linux Foundation 模式）应作为预案而非临时救火。
- **L5 把'格式'捐成开放标准会杀死自己的平台垄断（Docker），但标准制定者以'标准之上的服务'生存；可被标准化的只有格式，双边网络（支付/信任/清算）不会被标准商品化。**
  - 证据：Docker 2015 OCI+2017 containerd/CNCF：格式永生、Docker Inc 失去平台、退守开发者入口工具；对照卡组织：网络标准从未开源却垄断清算层数十年——被商品化的只是报文格式，不是信任与清算网络。
  - 推论：应主动把契约 schema、验收协议做成开放标准（防厂商各自圈地、抢标准时间窗），商业产品只做标准无法覆盖的三件事：验收执行的评测集、角色资产的版权/存储/版本管理、跨厂商一致性保证——格式免费，验收收费。
- **L6 抽象层从建立到统治约需 2-9 年（纯路由 2-3 年、深度基础设施 4-9 年），且中途必有一次估值腰斩/被吞/信任危机；活过危机的共性是刚需不可替代。**
  - 证据：Stripe 2021→2023 估值 $95B→$50B 后恢复；Twilio 2022-23 两轮裁员 17%+创始人被迫离任；Plaid 估值 $13.4B→$6.1B；HashiCorp 2023 license 危机；Docker 2019 卖掉企业业务。OpenRouter 未经历危机即被买走，结局是并入巨头而非独立壮大。
  - 推论：按'4-6 年统治周期+一次死亡谷'规划现金流与融资节奏，不按风口速度。预设 2027-2028 年'厂商集体官方下场+融资寒冬'的死亡谷，届时厂商无法自我评级的'验收层'是刚需门票——验收必须先于危机成为收入结构的主干。

### 战略启示（本路）

- 立即从'无状态统一 API'升级为'有状态资产层'：版本化契约+可积累验收数据+角色资产库，是唯一不被路由套利逻辑定价的护城河（OpenRouter 82 天被吞 vs Zapier 十四年独立，是同一律的两个结局）。
- 契约格式尽早开放并预设中立治理（Linux Foundation 模式）；商业产品只做标准之上的验收执行与角色资产管理——格式免费，验收收费（Docker/OCI 与 OpenTofu 双向证据）。
- 对厂商只做'付费验收认证'的增量关系，不做裁决式路由抽成；拒绝任何单厂商投资/排他绑定（Plaid×Chase 与 Visa 被阻止案正反两面证据）。
- 把模型碎片化当计时器：红利期（参照 OpenRouter 仅约 3 年）内完成状态资产冷启动，并写好'单一视频模型赢家通吃'时的 pivot 预案。
- 按 4-6 年周期+一次死亡谷做财务规划；OpenRouter 式快速溢价退出不应是默认剧本，除非退出能换到'成为标准'的席位。

### 未决问题

- Stripe 收购 OpenRouter 的最终成交价：官方公告未披露，$7B+（Bloomberg 2026-08-16）与 $7.5B（转引）均为媒体报道、未经审计，也未见交割完成公告——'预计数周内交割'是否已完成需跟踪。
- Stripe×PayPal $53B 联合要约（2026-07-15，与 Advent International）仅为要约，HN 检索未见后续成交确认，结果未知。
- OpenRouter 交割后是否维持'same name, same product'承诺、API 定价与条款是否变化，尚无 90 天后的观察数据。
- Plaid 与 Chase 在 2026 年近 90 天窗口内的协议状态/费率无一手来源（仅有 2025-07 CNBC 与 2025-09 Bloomberg），Chase 模式是否已扩散到其他大银行未核实。
- Zapier 2025-2026 年 ARR 无公开一手来源（仍私有），本次未对 2026 营收做任何断言。
- Twilio 2023-24 是否正式启动出售流程：激进投资者施压有多源证据，正式出售探索未证实。
- 视频生成子市场（Veo/Kling/Seedance/Wan）当前碎片化程度、OpenRouter 视频路由真实份额、以及各厂商官方 MCP/skills 的覆盖范围，需专门一路核实——本路结论向该场景的外推均标注为推断。

### 来源

- [OpenRouter 官方公告：OpenRouter is Joining Stripe（2026-08-19）](https://openrouter.ai/blog/announcements/openrouter-is-joining-stripe/)
- [OpenRouter 博客索引（收购后持续发版至 2026-09-22）](https://openrouter.ai/blog)
- [Wikipedia: OpenRouter（创立、Series B $113M/$1.3B、收购报道）](https://en.wikipedia.org/wiki/OpenRouter)
- [Wikipedia: Stripe, Inc.（估值轨迹、TPV、2026 收购与 PayPal 要约）](https://en.wikipedia.org/wiki/Stripe,_Inc.)
- [Wikipedia: Twilio（独立现状、2025 财务、CEO 更替）](https://en.wikipedia.org/wiki/Twilio)
- [Wikipedia: Plaid (company)（Visa 收购被阻、估值曲线、2026-02 员工股转让）](https://en.wikipedia.org/wiki/Plaid_(company))
- [HN Algolia: Plaid/JPMorgan 检索（CNBC 2025-07-28 'massively taxing'、Bloomberg 2025-09-25 数据协议）](https://hn.algolia.com/api/v1/search?query=Plaid%20JPMorgan&tags=story)
- [Wikipedia: Zapier（盈利史、$5B 估值、2026 MCP 集成）](https://en.wikipedia.org/wiki/Zapier)
- [Wikipedia: HashiCorp（IPO、IBM 收购 2025-02-27 交割）](https://en.wikipedia.org/wiki/HashiCorp)
- [OpenTofu 官网（BUSL 触发的分叉、Linux Foundation 托管）](https://opentofu.org/)
- [Wikipedia: Docker, Inc.（Mirantis 出售、融资史、2025 CEO/MCP Defender）](https://en.wikipedia.org/wiki/Docker,_Inc.)
- [Wikipedia: Docker (software)（OCI 2015-06-22、Moby 2017）](https://en.wikipedia.org/wiki/Docker_(software))
- [CoreOS 博客：rkt 与 containerd 捐赠 CNCF（2017-03）](https://coreos.com/blog/rkt-container-runtime-to-the-cncf.html)
- [HN Algolia: OpenRouter×Stripe 全时间线检索（2026-07-23 至 2026-08-31）](https://hn.algolia.com/api/v1/search?query=OpenRouter%20Stripe&tags=story)
- [HN: OpenRouter is joining Stripe（964 points，含成交价与营收泄露分析讨论）](https://news.ycombinator.com/item?id=49364559)


## 平台吞噬史（Twitter/Facebook/Reader/YouTube/Salesforce/AWS-fal/Reddit/Apple）

**摘要**：跨8个平台史案例（Twitter/Facebook/Google Reader/YouTube/Salesforce/AWS-fal/Reddit/Apple）提炼"平台容忍第三方层"的充要条件与"动手杀"的可观测领先信号。核心结论：平台只容忍三类第三方层——不碰核心变现、不拥有用户关系、且价值放大可计量（可抽成/可回流）；当 API 从"补贴"被重定义为"资产"、官方替代品成熟、或平台所有者/监管压力变更时启动收割，且条款埋雷先行于执行数月到数年（Twitter 2012埋雷2023执行）。对契约层的推论：做 vendor 的可审计需求放大器而非计费旁路；用户关系归开发者、单厂商依赖设架构上限；差异化落在 vendor 条款未覆盖的中立区（验收/回放/角色资产=用户资产）；对头部 aggregator 被官方收编（AWS-fal 型）保持预警。fal-AWS 官方博客（2026-05-19）距今约127天超90天窗口，已在 open_questions 标注。

### 案例

- **Twitter API 与第三方客户端**（2010-2023（余波至2026））→ 结局：**被平台杀死**〔多源交叉〕
  - 经过：2010-2011 鼓励客户端生态；2012-08-16 官方宣布 API v1.1 规则（第三方客户端10万用户上限、'一致性体验'条款）埋下 kill switch；2023-02/03 免费API关闭+按量付费，Tweetbot/Twitterrific 等全灭。2026-09-22 抓取 docs.x.com 官方文档确认现状：v2 为 pay-per-usage 付费分层，v1.1 仅legacy。
  - 关键因子：第三方客户端与官方体验同质化、直接分流广告变现所需的完整用户关系；2012 条款已埋雷（上限+一致性），执行滞后10年——条款先行是稳定规律；2022-23 所有权变更+广告收入崩塌（收购杠杆）触发收割；免费客户端对平台财务贡献为零、纯成本无回流
  - 来源：<https://dev.twitter.com/blog/changes-coming-to-twitter-api ; https://daringfireball.net/2023/03/tweetbot_and_twitterrific_face_the_cliff ; https://docs.x.com/x-api/getting-started/about-x-api>
- **Facebook Platform 与社交游戏层（Zynga 类）**（2007-2014）→ 结局：**被平台杀死**〔官方源〕
  - 经过：2007 f8 开放，免费病毒分发（通知/私信）催生社交游戏层；2010-2011 收紧病毒渠道；2010-12-26 Facebook 与 Zynga 签 Developer Addendum No.2（后作为 FB 2012 S-1 的 EX-10.13 披露——依赖深到要写进招股书）；2014-04-30 Graph API v2.0+新登录正式收回好友数据与分发。
  - 关键因子：平台先补贴病毒分发、开发商全部押注，随后在用户增长放缓时收回——'养肥'是平台增长函数而非恶意；头部依赖者被签城下之盟（独家/广告承诺），平台把依赖合同化；身份与关系数据是平台护城河，绝不外溢给 API 层（v2.0 的核心）；对头部收编（Zynga 协议）与对长尾收紧同步进行
  - 来源：<https://www.sec.gov/Archives/edgar/data/1326801/000119312512046715/d287954dex1013.htm ; https://developers.facebook.com/blog/post/2014/04/30/the-new-facebook-login/ ; http://cdixon.org/2010/05/08/facebook-zynga-and-buyer-supplier-hold-up>
- **Google Reader 关闭与 RSS 生态**（2005-2013）→ 结局：**其他（注明）**〔官方源〕
  - 经过：2013-03-13 官方博客'A second spring of cleaning'宣布关闭 Reader（当日 HN 1964分）。关闭理由是使用下降与公司战略聚焦（Google+），非因第三方竞争。FeedBurner 等配套同步收缩，RSS hub 生态碎片化，第三方客户端随共享基础设施一起消散。
  - 关键因子：注明：平台自身关闭共享基础设施，第三方层随之碎片化重置，属非竞争性死亡；免费基础设施 API 本质是可随时撤回的补贴，不因第三方遵守规则而豁免；无直接变现的共享 hub 在平台战略转向时最先被弃；生态的'单点hub'结构放大平台单方面决策的破坏半径
  - 来源：<http://googleblog.blogspot.com/2013/03/a-second-spring-of-cleaning.html>
- **YouTube API 选择性执法史**（2013-持续（2026仍有效））→ 结局：**被平台杀死**〔官方源〕
  - 经过：2013-05 Google 以'缺广告'要求微软从 Windows Phone 商店下架 YouTube 客户端（微软向 FTC 申诉后和解重做）；2020-10 youtube-dl 遭 RIAA DMCA 下架（GitHub dmca 库原文，HN 4240分）。2026-09-22 抓取官方 YouTube API Developer Policies 确认 'YouTube Look and Feel' 与反爬条款至今有效：API 客户端不得复刻官方 UI、不得绕过广告。
  - 关键因子：注明：选择性执法——绕过广告/复刻官方UI形态的被禁，遵守条款的嵌入型应用幸存；绕过广告变现是即时红线，无需等待任何窗口期；'Look and Feel' 条款把官方 UI 形态变成永久垄断资产，写进政策而非靠技术执法；平台用 ToS 措辞而非下架动作执法——第三方应在条款层而非事件层做风险监控
  - 来源：<https://developers.google.com/youtube/terms/developer-policies ; https://www.theverge.com/2013/5/15/4334030/google-demands-microsoft-remove-youtube-windows-phone-app ; https://github.com/github/dmca/blob/master/2020/10/2020-10-23-RIAA.md>
- **Salesforce AppExchange（幸存对照组）**（2006-至今（2026仍在运营））→ 结局：**幸存并独立壮大**〔多源交叉〕
  - 经过：2006 年上线的企业 app store，ISV 层持续壮大近20年未被平台收割。结构性原因：ISV 应用运行在 Salesforce 身份/数据模型内（用户关系留平台）、补 CRM 长尾场景不与平台核心竞争、抽成+联合销售使生态收益对平台财务可见（确切抽成比例本轮未获官方页核实，业界常见说法15%，未经审计）。Salesforce 2026-08-27 10-Q 已入 SEC（平台持续经营佐证），但 AppExchange 无单列收入。
  - 关键因子：不拥有用户关系：强制走平台身份，ISV 从不掌控最终客户；不与核心变现竞争：ISV 做平台不做的垂直场景，扩大而非分流 CRM TAM；生态收益可计量可抽成：平台从第三方层直接获得收入线；买家（企业IT）切换成本高，平台无收割紧迫性
  - 来源：<https://www.salesforce.com/blog/2019/02/steve-jobs-inspired-appexchange.html ; https://www.sec.gov/Archives/edgar/data/1108524/000110852426000190/crm-20260731.htm>
- **AWS/云厂与合作伙伴层（含 fal-AWS）**（2006-至今；fal-AWS 2026-05-19）→ 结局：**幸存并独立壮大**〔官方源〕
  - 经过：云厂对第三方层的基本态是共生：partner 层烧平台的 compute、带企业需求。fal 官方博客（2026-05-19）宣布与 AWS 战略合作，自称 250 万开发者（公司口径未审计）；2026-09-22 经 GitHub API 抓取 fal-ai org 确认其活跃且托管 ByteDance Seedance 2.0 官方 API repo——即 aggregator 同时是被模型厂商官方授权的渠道。AWS 以'官方合作+偏好云'收编头部，而非消灭。
  - 关键因子：第三方层是平台收入的放大器（demand amplifier）：fal 越大 AWS compute 卖得越多；不碰平台核心产品边界：AWS 卖基础设施，fal 做生成媒体特化，互补不重叠；企业市场需要解决方案层，平台自己不做的场景是安全区；头部被官方绑定后，中层 aggregator 生态位被上下夹压
  - 来源：<https://blog.fal.ai/fal-and-aws-building-for-the-next-phase-of-generative-media/ ; https://github.com/fal-ai>
- **Reddit API 收费事件**（2023-06（背景2016-2023；财务至今））→ 结局：**被平台杀死**〔官方源〕
  - 经过：2023-04 官宣商业化收费，Apollo 开发者披露报价折合约 2000万美元/年（开发者自估，未经审计）；2023-06-12 数千子版 blackout；2023-06-30 Apollo 等 third-party 客户端全灭。API 从开发者补贴重定义为 data licensing 资产。2026-07-31 10-Q（90天窗口内，SEC官方）：Q2 2026 总营收 $804.9M，其中 Other revenue $43.3M（上年同期 $34.8M，未审计审阅口径），data licensing 计入其中。
  - 关键因子：IPO 前夜变现重组：API 被重新定价为可售数据资产；官方 app（2016）成熟数年后才动手——官方替代品成熟度是领先指标；第三方客户端拥有'会话表面'却不产内容、不回流广告收入，纯被抽走广告库存；黑名单前发生社区反弹（blackout），但未改变决策——用户反弹不构成对价
  - 来源：<https://daringfireball.net/linked/2023/05/31/reddit-apollo-api-pricing ; https://old.reddit.com/r/apolloapp/comments/14nb5qs/today_is_apollo_for_reddits_last_day_and_i_just/ ; https://www.sec.gov/Archives/edgar/data/1713445/000171344526000100/rddt-20260630.htm>
- **Apple 对 web-app 与 App Store 边界的控制**（2008-至今；DMA 事件2024-02/03）→ 结局：**仍在竞争中**〔多源交叉〕
  - 经过：iOS 17.4（2024-02-15 官方确认）为应对 DMA 删除欧盟 Home Screen web apps，两周内（2024-03-01）因开发者反弹回滚——边界随监管外力反复重划。2026-09-22 抓取 WebKit 官方博客：Safari 26.4（2026）继续为 web apps 增加 Keyboard Lock 等能力；且博客索引显示 Apple 已上线官方 Safari MCP server（约2026-09，90天窗口内）——平台一边保留 web 层一边把 agent 入口官方化。
  - 关键因子：监管（DMA）是重划平台边界的最强外力，且平台会先用最弱的第三方层祭旗；删除后两周即回滚：开发者/舆论反弹是有对价的，但只对'非变现相关'的删除有效；边界反复本身构成第三方层的系统性风险——同一能力一年内两次生死翻转；平台同步把 agent/API 入口官方化（Safari MCP server），第三方入口层被两头挤压
  - 来源：<https://9to5mac.com/2024/02/15/ios-17-4-web-apps-european-union/ ; https://9to5mac.com/2024/03/01/apple-home-screen-web-apps-ios-17-eu/ ; https://webkit.org/blog/18136/introducing-the-safari-mcp-server-for-web-developers/>

### 定律

- **L1 平台容忍第三方层的充要条件一：不占据平台核心变现路径——凡绕过平台计费/广告/官方入口的第三方，无论多受欢迎都会被清场，且此红线无窗口期。**
  - 证据：YouTube 2013 以'缺广告'逼微软下架 Windows Phone 客户端（The Verge/wpcentral）；'Look and Feel'与反绕过条款至2026仍写在官方 Developer Policies；Reddit 客户端抽走广告库存后全灭（Apollo $20M/年报价）。对照幸存组：AppExchange 与 AWS-partner 层都让平台直接受益。
  - 推论：契约层必须被设计成 vendor 计费体系的增益而非旁路：输出可审计的 per-vendor attribution（经由契约层的增量调用量/验收通过率/浪费调用减少额），让 vendor 财务系统里出现'契约层渠道'正贡献行。任何'帮用户少付 vendor 钱'的功能都是自杀线。
- **L2 充要条件二：不拥有用户身份与关系。第三方层若持有'会话表面'（客户端入口）即持有时限不一的死亡倒计时，除非把身份与关系交还平台或开发者。**
  - 证据：Tweetbot/Apollo 拥有用户会话表面→死；AppExchange 强制 Salesforce 身份、FB canvas app 困在平台内→活；Graph API v2.0（2014官方博客）的核心正是收回好友数据。
  - 推论：CLI 形态天然拥有开发者工作流——这是我们的高危特征。对策：明确契约层不做任何 vendor 的'客户端'，用户身份与供应商账号全部归属开发者/企业，契约层只持有'合同与验收记录'这类用户资产，并在架构上支持 vendor 被替换而用户无感。
- **L3 充要条件三：价值放大且可计量。平台留下的是能被抽成、被审计、进自己收入表的第三方层；免费无回流的第三方层在平台变现承压时第一个被收割。**
  - 证据：AppExchange 抽成+联合销售、AWS Marketplace 计费（幸存）；Twitter 免费客户端十年零收入回流、Google Reader 无变现 hub（被收割）；Reddit 直接把 API 改写为 data licensing 资产（2023）。
  - 推论：把'放大器价值可观测'做成产品功能：定期发布契约层为各 vendor 带来的合格请求回流报告，并设计让 vendor 能在契约层内售卖更高 SLA 档位（可抽成结构）。中立性不等于免费——可抽成的中立层才是被平台保护的形态。
- **L4 平台的'杀手触发信号'可观测清单：①所有者/商业负责人变更或 IPO/杠杆压力；②API 条款从使用条款重写为许可/资产（pay-per-usage、data licensing 字样出现）；③官方替代品成熟拐点后6-24个月；④与头部第三方签排他/官方合作（收编头部=挤压中层）；⑤条款埋雷先于执行数月到十年。任两项同时出现即为高危。**
  - 证据：①Twitter 2022-23 收购杠杆、Reddit 2023 IPO；②Reddit data licensing、X API 现为 pay-per-usage（docs.x.com 2026-09-22 官方确认）；③Reddit 官方 app 2016→2023 收 API，Twitter 官方客户端强化→2012 规则；④FB-Zynga Addendum（2010，SEC EX-10.13）、AWS-fal 官方合作（2026-05-19官方博客）；⑤Twitter 2012 条款→2023 执行、YouTube Look and Feel 条款至今在案。
  - 推论：建立 vendor-官方化预警看板，监控五信号：video vendor 发布自家 MCP/skills/agent 入口、API 条款重写、价格改按量付费、与超头部 aggregator 签官方绑定、条款中出现'一致性/不得复刻体验'类措辞。利用⑤的滞后性：条款埋雷到执行通常有数月以上窗口，用于提前调整架构与谈判。
- **L5 免费 API 基础设施是可撤回的补贴：平台对'合规但不产生收益'的第三方没有保存义务，关闭决策由平台自身战略周期驱动，与第三方表现无关。**
  - 证据：Google Reader 2013-03-13 官方公告以'使用下降+战略聚焦'关闭（无第三方竞争因素），1964分 HN 反弹未改变结果；Reddit blackout 同样无效——合规与用户反弹都不构成对价。
  - 推论：契约层的核心功能不得依赖任何单一厂商的免费配额或慷慨限免；设硬性架构上限：任一 vendor API 停供24小时内，已生成产物的验收/回放/角色资产仍可离线运行（验收记录与资产本地化）。单厂商依赖度纳入 CI 度量。
- **L6 平台边界会被监管外力强制重划且会反复，平台倾向先用'边缘第三方层'试错；同时平台会把新的入口机会（如 agent/MCP）官方化收回。**
  - 证据：Apple 在 DMA 下 2024-02-15 确认删除欧盟 Home Screen web apps，2024-03-01 即回滚（9to5mac/The Register/Reuters），2026 年 Safari 26.4 仍在为 web apps 加功能，同时 2026-09 上线官方 Safari MCP server（WebKit 官方博客，本轮2026-09-22抓取，90天窗口内）。
  - 推论：两向站位：当监管迫使 video vendor 开放互操作/披露接口时，中立契约层是净受益方；但要避免自己成为监管意义上的'平台/守门人'——只做合同与验收侧，不做内容分发与流量入口。同时把 vendor 官方 MCP/skills 的出现视为入口层官方化信号，尽快把契约层价值锚定在官方入口不做的事（跨厂商验收、回放、角色资产一致性）上。

### 战略启示（本路）

- 把契约层做成 vendor 的可审计需求放大器（per-vendor attribution + 合格请求回流报告），绝不提供绕过 vendor 计费/限流的能力——这是 YouTube 式无窗口期的即死红线。
- 用户身份与关系归开发者所有，vendor 必须可插拔；CLI 的工作流持有权用'只持有合同与验收记录（用户资产）'来对冲。
- 建立五信号预警看板（官方 MCP/skills、条款重写为许可、pay-per-usage、头部排他绑定、一致性条款措辞），条款埋雷到执行的滞后窗口是战略调整时间。
- 差异化必须落在 vendor 条款不覆盖的中立区：验收/回放/角色资产定性为用户资产而非 vendor 内容再分发，且验收不依赖 vendor API 存活（单厂商停供24h仍可运行）。
- 头部 aggregator 被官方收编（AWS-fal 型）是中期必然，生态位应选'合同与验收中立层'而非'流量聚合层'，避免与被收编者在流量层正面竞争。

### 未决问题

- iOS 18.4（2025）欧盟 Home Screen web apps 的删除-恢复循环：本轮搜索预算耗尽未能用一手来源核实，Apple 案例仅覆盖2024-02/03已核实链条与2026-09-22抓取的 WebKit 现状。
- Salesforce AppExchange 抽成精确比例（业界常说15%）：未找到官方页面核实，案例中只以'抽成+联合销售'定性表述。
- fal-AWS 官方合作（官方博客2026-05-19）距今约127天，超出90天一手窗口；90天内未找到进一步一手确认（fal docs/首页未见 AWS 渠道说明，fal-ai GitHub 无 AWS 命名 repo）。
- Reddit 10-Q 的 Other revenue（Q2 2026 $43.3M）中 data licensing 的精确拆分未提取（10-Q 不单列，需查 10-K 定性披露）。
- Twitter 内部 2012条款→2023执行 的决策链一手证据（内部邮件/证词）无公开来源，规律中'条款先行'的内部机制只能从外部时序推断。
- 视频模型厂商（Veo/Kling/Seedance/Wan）官方 MCP/skills 的具体条款措辞是否已出现'一致性/反绕过'类埋雷，属其他 lane 范围，本轮未取证。

### 来源

- [Changes coming in Version 1.1 of the Twitter API (2012-08-16 官方)](https://dev.twitter.com/blog/changes-coming-to-twitter-api)
- [About the X API — 官方文档（2026-09-22 抓取，v2 pay-per-usage 现状）](https://docs.x.com/x-api/getting-started/about-x-api)
- [Tweetbot and Twitterrific Face the Cliff (Daring Fireball, 2023-03-01)](https://daringfireball.net/2023/03/tweetbot_and_twitterrific_face_the_cliff)
- [Facebook–Zynga Developer Addendum No.2 (2010-12-26), FB 2012 S-1 Exhibit 10.13, SEC](https://www.sec.gov/Archives/edgar/data/1326801/000119312512046715/d287954dex1013.htm)
- [The New Facebook Login and Graph API 2.0 (2014-04-30 官方)](https://developers.facebook.com/blog/post/2014/04/30/the-new-facebook-login/)
- [Facebook, Zynga, and buyer-supplier hold up (cdixon, 2010)](http://cdixon.org/2010/05/08/facebook-zynga-and-buyer-supplier-hold-up)
- [A second spring of cleaning (Google 官方, 2013-03-13)](http://googleblog.blogspot.com/2013/03/a-second-spring-of-cleaning.html)
- [YouTube API Services Developer Policies（官方，2026-09-22 抓取，含 Look and Feel 条款）](https://developers.google.com/youtube/terms/developer-policies)
- [Google demands Microsoft removes YouTube Windows Phone app (The Verge, 2013-05-15)](https://www.theverge.com/2013/5/15/4334030/google-demands-microsoft-remove-youtube-windows-phone-app)
- [youtube-dl RIAA DMCA takedown 原文 (GitHub, 2020-10-23)](https://github.com/github/dmca/blob/master/2020/10/2020-10-23-RIAA.md)
- [Advice from Steve Jobs Inspired the AppExchange (Salesforce 官方)](https://www.salesforce.com/blog/2019/02/steve-jobs-inspired-appexchange.html)
- [Salesforce 10-Q（2026-08-27 提交，SEC）](https://www.sec.gov/Archives/edgar/data/1108524/000110852426000190/crm-20260731.htm)
- [fal and AWS: Building for the Next Phase of Generative Media（fal 官方, 2026-05-19）](https://blog.fal.ai/fal-and-aws-building-for-the-next-phase-of-generative-media/)
- [fal-ai GitHub org（2026-09-22 经 GitHub API 抓取；含 seedance-2.0-api 官方 repo）](https://github.com/fal-ai)
- [Reddit API Pricing Would Cost Apollo Developer $20M/Year (Daring Fireball, 2023-05-31)](https://daringfireball.net/linked/2023/05/31/reddit-apollo-api-pricing)
- [Apollo's last update（开发者原帖, 2023-06-30）](https://old.reddit.com/r/apolloapp/comments/14nb5qs/today_is_apollo_for_reddits_last_day_and_i_just/)
- [Reddit 10-Q（2026-07-31 提交，SEC；Q2 2026 营收数据，审阅未审计）](https://www.sec.gov/Archives/edgar/data/1713445/000171344526000100/rddt-20260630.htm)
- [Apple confirms iOS 17.4 removes Home Screen web apps in the EU (9to5Mac, 2024-02-15)](https://9to5mac.com/2024/02/15/ios-17-4-web-apps-european-union/)
- [iOS 17.4 won't remove Home Screen web apps in the EU after all (9to5Mac, 2024-03-01)](https://9to5mac.com/2024/03/01/apple-home-screen-web-apps-ios-17-eu/)
- [WebKit Features for Safari 26.4（官方，2026，web apps 能力持续增强）](https://webkit.org/blog/17862/webkit-features-for-safari-26-4/)
- [Introducing the Safari MCP server for web developers（WebKit 官方，约2026-09）](https://webkit.org/blog/18136/introducing-the-safari-mcp-server-for-web-developers/)


## 价值转移律（商品化方向 → AI 视频栈 10 年推演）

**摘要**：实证确认模型层正在商品化：LLM 同能力推理价 3 年跌约 1000x（$60→$0.06/M），2026 官方现价 Gemini Flash-Lite $0.10/$0.40、DeepSeek V4.1-Flash 峰值 $0.15/$0.60 每百万 token；视频侧 Veo 3.1 标准 $0.40/s（2025-10 发布）→ Lite $0.05/s（2026-03-31 官方，5.5 个月 8x，注：任务称 4 个月有出入）。开放权重加速崩塌：MiniMax H3 开权重 55 天 HF 月下载 377 万（API 实测），ComfyUI 6 天接入本地推理；Wan Apache-2.0 累计 134 万。利润未消失而是沉淀：上游算力（Nvidia DC $89.0B/季 +117%）、头部模型（Anthropic run-rate $65B）、应用层（Cursor $60B 出售、OpenAI 广告 $1B）、数据层（Scale AI $14.3B）。共提炼 7 条规律、5 条战略启示。"PixPix 亿元补贴"未核实，未采信。

### 案例

- **LLM 推理价格崩塌（LLMflation）**（2021-11 至 2026-09）→ 结局：**其他（注明）**〔多源交叉〕
  - 经过：同能力（MMLU 42）推理价从 GPT-3 $60/M（2021）跌至 Llama 3.2 3B $0.06/M（2024），3 年 1000x；GPT-4 级（MMLU 83）3 年跌 62x。2026 官方现价（今日实测定价页）：Gemini 2.5 Flash-Lite $0.10 输入/$0.40 输出每百万 token，Gemini 3.1 Flash-Lite $0.25/$1.50；DeepSeek V4.1-Flash 峰值 $0.15/$0.60、缓存命中低至 $0.003 输入（峰谷定价=公用事业化）。对比 2023-03 GPT-4 首发 $30/$60：旗舰级能力价格约降 200-300x。结果注记：推理层整体商品化，价格崩塌本身即结果，无单一死方。
  - 关键因子：开放权重模型（Llama/DeepSeek/Wan）提供价格地板；推理效率（量化/缓存/峰谷调度）；能力趋同后厂商只剩价格战；厂商用子品牌+官方限时折扣而非直接降价
  - 来源：<https://a16z.com/llmflation-llm-inference-cost/>
- **Veo 3.1 价格阶梯：视频 API 杀价已在发生**（2025-10-15 至 2026-09）→ 结局：**其他（注明）**〔官方源〕
  - 经过：Veo 3.1 发布（2025-10-15）标准价 $0.40/s（720p/1080p）；2026-03-31 官方发布 Veo 3.1 Lite，成本'低于 Veo 3.1 Fast 的 50%'（720p $0.05/s），5.5 个月内官方价降 8x（注：任务称 4 个月，实为约 5.5 个月）；2026-04-07 又下调 Fast 价格。当前官方定价页（今日实测）：标准 $0.40/s、Fast $0.10/s、Lite $0.05/s（1080p $0.08/s，Lite 不支持 4k）。结果注记：厂商主动自我蚕食，用低价子品牌对冲开放权重与竞争，而非全线降价。
  - 关键因子：开源视频模型压出价格地板；厂商用 Lite 子品牌做价格歧视保住标准档利润；推理成本实际下降；高用量应用层是降价的目标买家
  - 来源：<https://blog.google/innovation-and-ai/technology/ai/veo-3-1-lite/>
- **MiniMax H3 开放权重商品化视频推理**（2026-07-28 至今）→ 结局：**仍在竞争中**〔多源交叉〕
  - 经过：H3 视频模型（原生音频/2K）发布开放权重，55 天内 Hugging Face 月下载 3,766,997（HF API 2026-09-23 实测；任务称 404 万有出入，以实测口径为准），ComfyUI 于 6 天后（2026-08-03）Day-0 支持本地推理；MiniMax 同步在官方 GitHub 随权重发布 prompt 'skills' 并经营自家 API——开放权重是获客渠道。对比：Wan 系列 Apache-2.0（协议经 HF API tags 核实）全部仓库累计下载约 134 万。H3 许可证为 minimax-h3-community-license（非 Apache，条款未逐条核读）。
  - 关键因子：开放权重让本地/自托管推理 6 天内成为现实；工作流工具生态（ComfyUI）接入速度决定商品化速度；开放权重+自家 API 双轨：权重当分发，API 收钱；社区许可证保留商用控制权
  - 来源：<https://huggingface.co/MiniMaxAI/MiniMax-H3>
- **LLM 链利润沉淀（2024-2026 实测）**（2024 至 2026-09）→ 结局：**幸存并独立壮大**〔多源交叉〕
  - 经过：推理价格崩塌的同时，利润沉淀在四层（金额均为未经审计的公开报道/官方口径）：①上游算力：Nvidia 数据中心季度收入 $89.0B、同比 +117%（官方新闻稿 2026-08-26）；②头部模型：Anthropic run-rate 2026-03 约 $20B → 2026-08 突破 $65B（Bloomberg/Reuters，非审计）；③应用层：Cursor 母公司 Anysphere 以 $60B 被 SpaceX 收购（CNBC 2026-06-16，单一来源）、OpenAI 广告业务 $1B run-rate（Reuters 2026-08-31）；④数据层：Meta 以 $14.3B 投资拿走 Scale AI 49%（NYT 2025-06）。
  - 关键因子：算力是所有商品化竞争的互补品，吸收最多利润；前沿质量仍有溢价（头部模型例外论）；贴近用户预算/按结果收费的应用层拿走大头；数据与资产权属层被巨额资本重估
  - 来源：<https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027>
- **PC 产业利润向 Wintel 迁移（历史基案）**（1981-2000）→ 结局：**被标准取代**〔多源交叉〕
  - 经过：IBM PC 开放架构被克隆后，组装/整机厂商品化、毛利归地；利润集中到两个不可克隆的互补品：OS（微软）与 CPU（Intel）。这是 Spolsky 'commoditize your complement' 与 Christensen 模块化理论的经典实证。结果注记：组装厂层被 Wintel 标准吸收利润。
  - 关键因子：标准接口让可替换层商品化；互补品（OS/CPU）形成事实垄断；用户绑定在标准之上而非整机之上
  - 来源：<https://www.joelonsoftware.com/2002/06/12/strategy-letter-v/>
- **OpenStack 未能商品化 AWS（反例）**（2010-2019）→ 结局：**其他（注明）**〔多源交叉〕
  - 经过：开源云平台意在用开放源码商品化 AWS，但 AWS 利润未受损，OpenStack 自身碎片化衰退。教训：中立+开放不等于自动商品化——被商品化的一层必须'可替换且替换后不增加用户成本'，AWS 的运营复杂度与能力深度保住了利润。结果注记：商品化尝试失败，开放但难用，生态碎片化。
  - 关键因子：运营复杂度是隐性护城河；开源≠低使用成本；缺乏中立治理外的强生态执行
  - 来源：<https://en.wikipedia.org/wiki/OpenStack>
- **Kubernetes/CNCF：中立标准席位的价值**（2015 至今）→ 结局：**幸存并独立壮大**〔多源交叉〕
  - 经过：Google 将编排器开源并交给中立基金会，主动商品化了编排层本身；标准席位本身获得全行业信任，所有厂商（包括 AWS）最终在其上竞争。对比 OpenStack：中立治理+低使用成本+厂商互操作刚需三者齐备才成立。
  - 关键因子：中立治理换取全行业采用（含竞争对手）；可移植性是用户的真实预算诉求；标准层本身不直接收租，但占据生态心智与人才
  - 来源：<https://www.cncf.io/about/who-we-are/>

### 定律

- **L1 商品化的下一站是互补品：一层商品化时，利润流向它的互补品（算力、贴近结果的应用、数据资产），不流向相邻同质层。**
  - 证据：LLM 推理价 3 年跌 1000x（a16z）与 Veo 5.5 个月官方价跌 8x 同时：Nvidia DC 收入 $89.0B/季（+117%）、Cursor 以 $60B 退出、OpenAI 广告 $1B run-rate——利润全在推理的互补品上。
  - 推论：我们绝不能在'生成调用'上竞争或收费（那是正在崩塌的层），要把任何厂商模型当可替换 commodity，把价值主张完全锚在契约、验收、角色资产这些互补品上。
- **L2 利润不消失，向'对最终结果负责'的一层迁移（Christensen 保守吸引力利润定律）。**
  - 证据：PC 组装厂商品化后利润移至 Wintel；OpenStack 因不承担'更好用'的责任而失败、AWS 凭运营责任保住利润；LLM 链中 token 崩价但企业仍为'可用的结果'付溢价（Anthropic run-rate 5 个月 $20B→$65B）。
  - 推论：视频栈将对'可用成片/镜头通过'负责的一层吸走利润。我们的验收层必须把'通过/不通过'做成可审计、可追责的签字工件（acceptance certificate），而不是建议性评分——签字责任是厂商下场做 MCP 时因利益冲突无法复制的。
- **L3 微笑曲线：生产端（推理）毛利最低，上游资产/IP 与下游分发/验收两端利润最高。**
  - 证据：Wan Apache-2.0（累计 134 万下载）与 H3（55 天 377 万月下载、6 天本地推理）把视频推理端毛利打到地板；同期利润沉淀在上游算力（Nvidia）与下游应用/数据（Cursor $60B、Scale AI $14.3B）。
  - 推论：我们的上游是'角色资产/一致性资产'（IP 位），下游是'验收标准'——两端都要占位；只做中间的格式转换管道必死。
- **L4 免于商品化的特征一：不可替代的累积状态（换供应商也带不走的数据）。**
  - 证据：Cursor 的代码库上下文与工作流（$60B）、Hugging Face 的模型-数据网络、Scale AI 的标注数据（$14.3B）——均随使用增值且不随底层模型更换而消失。
  - 推论：我们部分符合：角色资产库是唯一随时间增值的自有状态，但当前 CLI 形态缺少网络增值（无一致性校验记录沉淀、无风格指纹学习）。要把每次验收留下的证据链变成资产的一部分，纯 prompt 模板不构成此护城河。
- **L5 免于商品化的特征二：被所有厂商需要的中立席位，且中立必须同时降低使用成本。**
  - 证据：Kubernetes/CNCF 成立（中立治理+更好用）；OpenStack 失败（中立但难用）；MiniMax 官方随权重发布 skills、厂商自建 MCP/skills——厂商做集成时会优先自家，跨厂商中立位反而更稀缺。
  - 推论：我们符合位置但未兑现承诺：跨厂商契约正是中立席位。成立前提有二：(a) 厂商官方集成下场后，我们仍提供他们给不了的东西——对竞品模型的验收（厂商自验收有利益冲突）；(b) 接入我们的成本必须显著低于直连每家 API，否则重蹈 OpenStack。
- **L6 免于商品化的特征三：站在预算/结算与责任路径上——按结果收费者拿利润，按成本转售者无定价权。**
  - 证据：按结果收费的应用层（Cursor 订阅、OpenAI 广告 $1B run-rate）拿走利润；按 token/秒转售的聚合层无定价权；DeepSeek 直接用峰谷定价把推理做成公用事业（$0.003 缓存命中）。
  - 推论：我们缺失：目前不在任何结算路径上。演进方向是按'验收通过的结果'计量乃至计费，哪怕先只做成本与通过率账本；停留在按秒转售视频生成的那一层已经死了。
- **L7 开放权重把推理价地板拉平的时滞约 1 周-3 个月：契约层必须把自托管开源模型当一等公民。**
  - 证据：H3 于 2026-07-28 开权重，ComfyUI 6 天后（08-03）Day-0 本地推理，55 天 377 万月下载；Wan Apache-2.0 长期压住开源地板，倒逼 Google 发 Lite 子品牌（$0.05/s）应对。
  - 推论：跨'本地 Wan/H3'与'云端 Veo'的无缝同构验收是我们的核心场景而非边缘场景——价格敏感用户 6 天内就有本地替代，若契约层不覆盖自托管，用户直接绕开我们。

### 战略启示（本路）

- 生成调用本身已是商品：战略上禁止在'更便宜的聚合调用'上竞争（fal/OpenRouter 类转售层已被证明无定价权），一切价值声明锚定'换任何模型，验收标准与角色资产不动'。
- 把验收做成'签字责任'而非'建议'：验收结果=可审计工件（契约+证据+结论+可追责签名），这是厂商官方 MCP/skills 因自验收利益冲突而无法复制的位置。
- 角色资产库是唯一随时间增值的自有资产：格式开放、存储归用户、索引与一致性校验归我们；把每次验收的证据链沉淀为资产，制造'换模型也带不走'的累积状态。
- 自托管开放权重（Wan/H3，6 天即有本地推理生态）必须是一等公民：跨本地/云统一验收是对厂商官方集成的主要差异化，不覆盖自托管等于把价格敏感用户全部让出去。
- 向预算路径移动：按'验收通过的结果'计量/计费（先做成本与通过率账本也行），避免停留在按秒转售层——DeepSeek 峰谷定价已宣告那一层是公用事业。

### 未决问题

- 任务输入中的'PixPix 亿元补贴'：HN Algolia 无任何记录，本环境无法检索中文媒体一手来源，本报告未采信此断言，需人工补充来源后再用。
- Seedance 2.5（2026-08-04 有 API 定价讨论帖）与 Kling/Hailuo 的具体 API 现价及近 90 天降幅未从一手来源核实，'中国价格战'仅有间接证据（Veo Lite 应对性降价、开源地板）。
- SpaceX $60B 收购 Anysphere（Cursor）仅 CNBC 单一来源，未见双方官方公告，存疑待核。
- MiniMax H3 许可证为 minimax-h3-community-license（非 Apache），商用/转售推理具体条款未逐条核读，影响'开放权重商品化力度'的精确表述；Wan 的 Apache-2.0 已核实。
- 任务称 H3 月下载 404 万，HF API 实测 3,766,997（2026-09-23），HF 口径为近 30 天下载且每日波动，以实测口径为准。
- 视频栈'评测/验收层'是否已有独立玩家获得融资或收入的近 90 天证据缺失（未检索到），竞争格局该侧为空白。

### 来源

- [a16z: LLMflation — LLM inference cost is falling 10x/year (Appenzeller, 2024-11)](https://a16z.com/llmflation-llm-inference-cost/)
- [Google Gemini API 官方定价页（Veo 3.1 $0.40/$0.10/$0.05 per s；Gemini 文本模型价，2026-09-23 实测）](https://ai.google.dev/gemini-api/docs/pricing)
- [Google 官方博客: Build with Veo 3.1 Lite（2026-03-31）](https://blog.google/innovation-and-ai/technology/ai/veo-3-1-lite/)
- [Google 开发者博客: Introducing Veo 3.1 in the Gemini API（2025-10-15）](https://developers.googleblog.com/en/introducing-veo-3-1-and-new-creative-capabilities-in-the-gemini-api/)
- [Hugging Face API: MiniMax-H3（月下载 3,766,997，2026-09-23 实测）](https://huggingface.co/MiniMaxAI/MiniMax-H3)
- [ComfyUI 官方博客: MiniMax H3 Day-0 Support（2026-08-03，HN 334 分）](https://blog.comfy.org/p/minimax-h3-day-0-support-in-comfyui)
- [Reuters: China's MiniMax releases H3 video model（2026-07-31）](https://www.reuters.com/world/china/chinas-minimax-releases-h3-video-model-2026-07-31/)
- [Hugging Face: Wan-AI 模型列表（Apache-2.0，累计下载 133.9 万，API 实测）](https://huggingface.co/Wan-AI)
- [DeepSeek 官方定价页（V4.1-Flash 峰谷定价，2026-09-23 实测）](https://api-docs.deepseek.com/quick_start/pricing)
- [Nvidia Q2 FY2027 官方财报新闻稿（2026-08-26，DC $89.0B +117%）](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027)
- [Reuters: Anthropic revenue run rate tops $65B（2026-08-17，非审计）](https://www.reuters.com/technology/anthropic-revenue-run-rate-tops-65-billion-source-says-2026-08-17/)
- [CNBC: SpaceX to buy Cursor AI parent Anysphere for $60B（2026-06-16，单一来源）](https://www.cnbc.com/2026/06/16/-spacex-to-buy-cursor-ai-parent-anysphere-for-60-billion.html)
- [Reuters: OpenAI ad business hits $1B annualized run rate（2026-08-31）](https://www.reuters.com/business/media-telecom/openais-ad-business-hits-1-billion-annualized-revenue-run-rate-2026-08-31/)
- [NYT: Meta invests $14.3B in Scale AI（2025-06-12）](https://www.nytimes.com/2025/06/12/technology/meta-scale-ai.html)
- [Joel Spolsky: Strategy Letter V — Commoditize your Complement（2002）](https://www.joelonsoftware.com/2002/06/12/strategy-letter-v/)
- [Wikipedia: OpenStack（商品化 AWS 失败的反例）](https://en.wikipedia.org/wiki/OpenStack)
- [CNCF: About（中立治理标准席位）](https://www.cncf.io/about/who-we-are/)


## 标准战争（JSON/OpenAPI/OCI/CNCF/Matter/MCP 与中立化路径）

**摘要**：史证：事实标准=先跑起来+宿主传播+极简可拷贝，采纳永远先于治理。中立化要在"强而未霸"时以schema+商标打包捐出：MCP发布12.5个月即捐入Linux Foundation/AAIF并保留认证层；Docker捐了格式仍失商业层（价值上移到编排）；SmartBear捐OpenAPI规范靠工具存活；Markdown/RSS拒捐致CommonMark分叉/Atom竞争。SKILL.md一年约48产品采纳但治理悬置，恰是反面对照组。对我们：先采纳后治理，设触发器即捐schema；护城河放厂商差异知识库、验收执行器与conformance认证。

### 案例

- **JSON 对 XML**（1998-2017（XML 1.0→2001 json.org→2005 Web 2.0 普及→2013 ECMA-404→2017 RFC 8259/STD 90））→ 结局：**幸存并独立壮大**〔多源交叉〕
  - 经过：XML 有最强 backing（W3C、太阳微/微软/IBM 企业阵营），JSON 无任何官方 backing——Douglas Crockford 个人发布、声明不拥有它。JSON 靠更简单、直接映射 JS 对象、浏览器原生 JSON.parse（ES5, 2009）自下而上赢掉 Web API 层；XML 退守文档/企业集成领域。事实普及约 6 年，正式标准化反而晚了十年（先采纳后治理的极端案例）。
  - 关键因子：语法一页纸 vs 规范几百页：极简压倒完备；零控制人：任何人可自由实现与拷贝，无采用税；宿主是浏览器与 AJAX 潮流，不是宣传；正式标准是胜利后的追认，不是胜利的原因
  - 来源：<https://www.rfc-editor.org/rfc/rfc8259>
- **OpenAPI/Swagger：个人项目到事实标准**（2010-2017（Wordnik/Tony Tam 个人项目→2014 Swagger 2.0→2015.9 SmartBear 捐规范、OpenAPI Initiative 入 Linux Foundation→2017 OAS 3.0））→ 结局：**幸存并独立壮大**〔官方源〕
  - 经过：SmartBear 收购 Swagger 品牌后，把规范捐给 Linux Foundation 新设的 OpenAPI Initiative（Google/IBM/Microsoft/PayPal/CapitalOne 等约 26 家创始成员），自己保留工具生意。赢法：真实痛点（REST API 描述）+代码生成/文档工具链先行，再以厂商中立治理解除竞争者顾虑，最后 AWS API Gateway 等云原生支持锁定胜局。从个人项目到不可逆约 7 年。
  - 关键因子：SmartBear 模式：规范中立化，工具商业化——公司活了下来；大厂商联盟背书消除'单一供应商规范'恐惧；工具链先于治理：先让人依赖，再谈组织；捐出的是规范，保留的是品牌与产品线
  - 来源：<https://www.openapis.org/about>
- **Docker 容器格式→OCI 捐赠：救了格式、没救公司**（2013-2019（2013 发布→2015.6 捐镜像/运行时规范予 OCI（Linux Foundation）、runC 捐出→2017 containerd 入 CNCF→2019.11 Docker Enterprise 售予 Mirantis，金额未披露））→ 结局：**其他（注明）**〔官方源〕
  - 经过：Docker 主动把镜像格式与运行时规范捐给 OCI 以防碎片化，随后将容器运行时 containerd 也捐入 CNCF。格式成为全行业标准并存活至今，但商业价值早已上移到编排层：Kubernetes 击败 Docker Swarm，被标准化的那层必然商品化，Docker 的企业平台业务 2019 年出售给 Mirantis（收购），公司转向 Docker Desktop 等开发者工具。标准化精确地商品化了它触碰的那一层。
  - 关键因子：捐格式=主动商品化核心层：换来了生态统一，没换来商业护城河；护城河押错层：价值在编排（K8s）不在镜像格式；捐赠防止了分叉，保住了'格式'这一资产；镜像格式人人可用与 Docker Inc 无关地繁荣
  - 来源：<https://www.mirantis.com/blog/mirantis-acquires-docker-enterprise-platform-business/>
- **Kubernetes→CNCF 基金会路径**（2014-2017（2014.6 开源→2015.7.21 v1.0 发布并捐入新设 CNCF（含商标）→2017 全部主要云厂商提供托管 K8s））→ 结局：**幸存并独立壮大**〔多源交叉〕
  - 经过：Google 以内部 Borg 经验开源 K8s，一年内捐给 Linux Foundation 新设的 CNCF 作为创始项目并移交商标。战略动机：商品化容器编排层以削弱 AWS 的云优势、为 GCP 换取中立信誉。中立治理让每个竞争的云厂商都能共建，conformance 一致性认证把兼容性变成可售卖资产。从开源到事实标准约 3 年——最快的胜出案例。
  - 关键因子：Google 捐出商标与控制权，换取'每家云都是自己人'；conformance 认证程序把标准变成生态准入门槛；基金会路径=竞争者联盟，以速度换合法性后反获速度；捐赠动机清晰利己：标准层商品化，应用层（GCP）受益
  - 来源：<https://coreos.com/blog/kubernetes-1.0-and-cloud-native-computing-foundation/>
- **USB-C：监管强推型**（2014-2024（USB-IF 2014 发布 Type-C→2022.6 欧盟统一充电接口指令→2023.9 苹果 iPhone 15 转用 USB-C→2024.12.28 欧盟生效））→ 结局：**其他（注明）**〔官方源〕
  - 经过：USB-IF 产业联盟先造好标准，欧盟 2022 年立法强制（2024 年末生效，后续涵盖无线充电），终结 Lightning 与 USB-C 十年格式战。苹果在执法前 15 个月即合规——因为欧盟市场大到不值得为它做双 SKU，单一 SKU 又让全球自然趋同。监管是最慢的背书方（规范到强制约 10 年），但一旦出手就是不可逆的终局。结果形态：监管强推使格式全胜，但无单一公司赢家，标准归属联盟 USB-IF。
  - 关键因子：先有联盟标准、后有监管追认，顺序不可倒；监管效力靠市场重力外溢：只立法欧盟，胜在全球；对在位者（苹果）而言双轨成本高于让步成本；周期最长：适合补刀，不适合起手
  - 来源：<https://ec.europa.eu/commission/presscorner/detail/en/ip_22_4949>
- **Matter/Thread：厂商联盟型及其缓慢教训**（2019-2026（Project CHIP 2019.12 宣布（亚马逊/苹果/谷歌/三星+Zigbee 联盟/CSA）→Matter 1.0 推迟至 2022.10→1.4 2024.11→1.5 2025.11（摄像头/能源管理）；2026 年 CSA 新闻重心转向新标准 Suzi））→ 结局：**仍在竞争中**〔多源交叉〕
  - 经过：最大规模竞争者联盟（四巨头+CSA 数百家会员）做统一智能家居标准，代价是共识速度：首发推迟一年，功能以最小公分母推进，认证与桥接碎片化拖慢落地。近 90 天一手观察：CSA 官网新闻room 2026 年 9 月的重心是新标准 Suzi（长距 Zigbee，9.2 开放认证），Matter 仅有会员证言稿（9.3）；生态媒体注意力已转向 AI 智能家居（The Verge 2026-09-03 Anker MindBase）。联盟治理的慢导致生态注意力流失。
  - 关键因子：竞争者共识=最小公分母+发布推迟（1.0 延期一年）；会员激励错位：每家仍想保住自家云与生态入口；四年到 1.5 版本，期间 AI 生态注意力整体迁移；认证体系（CSA）是联盟中真正持续有价值的一环
  - 来源：<https://csa-iot.org/newsroom/matter-1-4-enables-more-capable-smart-homes/>
- **MCP：单厂商控制→捐入中立基金会（任务问题答案：已捐）**（2024.11-2026.9（2024.11.25 Anthropic 发布（David Soria Parra/Justin Spahr-Summers）→2025.3-5 OpenAI/Google DeepMind/Microsoft 先后采纳→2025.12.9 捐入 Linux Foundation 新设 Agentic AI Foundation（AAIF，Anthropic/Block/OpenAI 共同创立，创始项目 MCP/goose/AGENTS.md）→2026.7.28 发布新 schema→2026.7.10 AAIF 推出官方 MCPA 认证→2026.8.18 Google 将 A2A 移入 AAIF））→ 结局：**幸存并独立壮大**〔官方源〕
  - 经过：发布 12.5 个月后在采纳最高点主动捐出：GitHub GOVERNANCE.md 现写明 MCP 为 'a Series of LF Projects, LLC'（Linux Foundation 项目系列），规范与文档 Apache-2.0/CC-BY-4.0，最新 schema 目录为 2026-07-28（2026-07-23 The Register 报道该版'与 stateful 过去决裂'的单点大改）。近 90 天一手证据：AAIF 官方博客 2026-07-10 发布首个官方认证 MCPA（顾问委员会含 Anthropic/Google/AWS/Microsoft/Block/GitHub/Hugging Face）；HN 2026-09-22 出现 OpenMCP 社区分叉，提示治理不完全令人满意；AAIF 已成为 agentic 标准聚集地（MCP、goose、AGENTS.md、agentgateway、A2A、Agent Router 六项目）。
  - 关键因子：捐出时机=强而未霸：最大竞争者已采纳、治理将成采用障碍的临界点；打包捐了 schema+商标（LF Projects Series），只留生态参与权；认证层（MCPA）由基金会承接——把中立化变成新价值层；捐后演进仍快且仍受主导方影响（2026-07-28 stateless 大改）；治理不满的信号：社区分叉 OpenMCP（2026-09-22）
  - 来源：<https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation>
- **SKILL.md/Agent Skills：约 48 产品采纳但治理仍由 Anthropic 系控制**（2025.9-2026.9（anthropics/skills 仓库 2025-09-22 创建（GitHub API 显示 177,610 星，未审计）→独立 agentskills org 2025-12-15 创建、spec 仓库 2025-12-16（25,592 星，未审计）→截至 2026-09-22 官方展示页列出约 48 家采纳产品，未捐入任何基金会））→ 结局：**仍在竞争中**〔官方源〕
  - 经过：近 90 天一手证据（官网与 GitHub API，2026-09-22 抓取）：agentskills.io 展示页枚举约 48 家采纳方，含 OpenAI ChatGPT/Codex、Google Gemini CLI、Microsoft GitHub Copilot/VS Code、Cursor、AWS Kiro、字节 TRAE、Block Goose、Mistral、Databricks、Snowflake 等。但：仓库无 GOVERNANCE.md、无 MAINTAINERS.md；AAIF 官方项目列表中没有它；站点仅称 'originally developed by Anthropic, released as an open standard... open to contributions'。与 MCP 形成完美对照：同为 Anthropic 格式，一个在采纳高峰捐给中立基金会，一个治理悬置一年。Anthropic 自己的 Claude Code 2026-09 起也读取已入 AAIF 的 AGENTS.md，显示中立格式的引力。
  - 关键因子：采纳速度极快：极简格式（一个 SKILL.md+渐进披露）一年约 48 产品；治理悬置：无基金会、无治理文档、出身域名与品牌仍在 Anthropic 系；证明'先跑起来'可以在 12 个月内造出事实标准候选；第三方（OpenAI/Google/Microsoft 产品线）实质承受单厂商规范的全部风险；对照 MCP：中立化是可复制剧本，未做即是风险敞口
  - 来源：<https://agentskills.io>
- **JSON Schema：中立小组织 schema 的宿主传播样本**（2009-2026（Kris Zyp 邮件列表提案→社区 GitHub org 维护→借道 Swagger 2.0/OpenAPI 成为 API 描述的内置方言→2026 仍无基金会归属））→ 结局：**幸存并独立壮大**〔多源交叉〕
  - 经过：近 90 天一手证据：json-schema.org 主页（2026 版权）仍只挂 GitHub org 与 Open Collective 赞助，无任何基金会字样——一个 17 岁的关键 schema 标准至今没有正式治理家。它赢的渠道不是自治而是宿主：OpenAPI/Swagger 把它内嵌为 Schema Object 方言，跟着 API 工具链渗透到每个角落。代价是治理欠账：多年停留在 draft 版本状态、版本演进混乱。
  - 关键因子：宿主传播：被 OpenAPI 内嵌比任何自身推广都有效；无主、宽松授权、任何人可校验实现；工具链（校验器）生态是采用的真实门槛；治理欠账 17 年未补：能赢采用，赢不了演进秩序
  - 来源：<https://json-schema.org/>
- **Markdown：BDFL 控制的胜利与冻结**（2004-2017（Gruber+Swartz 发布→GitHub/Stack Overflow/Reddit 采纳→歧义导致 2014 CommonMark 分叉→2017 GFM 以正式规范发布））→ 结局：**幸存并独立壮大**〔多源交叉〕
  - 经过：Gruber 个人发布、保留控制权，靠博客文化与 GitHub 2008-2009 采纳成为全球写作事实标准。但单人拒绝演进使规范歧义无法修复，工具链被逼出 2014 年 CommonMark 分叉与 GitHub 的 GFM——今天事实上运行的'Markdown 标准'是分叉变体而非原版规范。BDFL 模式采用最快、演进最慢。
  - 关键因子：极简+宿主（GitHub）决定性传播；单主控制：赢采用、冻结演进；歧义+拒绝治理→社区分叉接管实际标准（CommonMark/GFM）；原规范沦为符号，运行标准归分叉
  - 来源：<https://daringfireball.net/projects/markdown/>
- **RSS：单主标准战争与杀手应用的胜利**（1999-2006（Netscape 0.9→Winer 系 0.91/0.92→2002.9 RSS 2.0 发布于哈佛 Berkman→2005 iTunes 播客采用→2005.12 竞争规范 Atom 入 IETF RFC 4287））→ 结局：**其他（注明）**〔多源交叉〕
  - 经过：Dave Winer 个人控制 RSS 商标与演进，治理争议激化出中立化竞争规范 Atom（IETF RFC 4287）；但 RSS 2.0 靠简单+杀手应用（iTunes 2005 播客订阅）赢得事实标准地位。哈佛 Berkman 发布给了半中立法理家。双教训：即使治理差，先跑起来+简单仍能赢；单主控制的信任税（催生 Atom）永久存在。结果形态：RSS 2.0 事实标准胜出但治理争议催生 Atom 分裂生态数年。
  - 关键因子：杀手应用（iTunes 播客）压过流程正统性；极简格式赢过更严谨的 RDF/RSS 1.0；单主控制催生竞争标准（Atom），分裂生态数年；半中立发布地（哈佛）提供有限信任背书
  - 来源：<https://cyber.harvard.edu/rss/rss.html>

### 定律

- **L1 事实标准形成条件①：先跑起来——采纳先于治理，被依赖先于被承认**
  - 证据：JSON 2005 年已普及、2017 年才有 IETF 正式标准；Markdown 靠 GitHub 采纳而非任何组织；Swagger 工具链先行、2015 年才建基金会；MCP 是 OpenAI/Google/Microsoft 先采纳、后捐赠（2025-12-09）；反例 Matter：先组联盟后做产品，首发即延期
  - 推论：未来 6-12 个月契约层唯一 KPI 是让 fal/OpenRouter 级中立路由商与 ≥1 家头部视频模型厂商真实跑通互操作；治理、联盟、认证全部后置
- **L2 事实标准形成条件②：宿主传播——小组织 schema 的赢家渠道是内嵌进高流量宿主，而非自建生态**
  - 证据：JSON Schema 被 OpenAPI 内嵌为方言而普及；Markdown 靠 GitHub；RSS 2.0 靠 iTunes 播客；USB-C 靠欧盟法规这个'超级宿主'外溢全球
  - 推论：把 generate/验收契约发布为可被任意宿主直接引用的标准工件（JSON Schema + TS 类型 + MCP tool 清单三形态），主动做成 fal/OpenRouter/厂商 SDK 的兼容层，绝不要求用户先装我们的 CLI 才能用 schema
- **L3 事实标准形成条件③：极简与可拷贝性压倒完备性——赢家的规范一页读完**
  - 证据：JSON 语法一页纸胜 XML 几百页；RSS 2.0 简单胜 RSS 1.0 严谨；SKILL.md 一个 markdown 文件一年约 48 产品采纳（官方展示页枚举）；Matter 完备但四年未竟、注意力流失
  - 推论：契约 v1 窄到只有 generate 参数+验收谓词+角色资产三段式，一页能读完；宁可迭代十个窄版本，不做 Matter 式全家桶
- **L4 中立化时机规律：在'强而未霸'点捐出——采纳足够多之后、竞争者把你的控制权当采用障碍之前；必须 schema+商标打包**
  - 证据：MCP 发布 12.5 个月即捐 LF/AAIF 且打包商标（2025-12-09），随后 A2A/AGENTS.md/goose 汇入同一中立家；反例 Markdown/RSS 不捐→CommonMark 分叉（2014）/Atom 竞争（2005）架空原规范；反例 Docker 捐晚了且留了平台业务（2019 出售 Mirantis）；正面 SmartBear 捐规范保工具商业（OpenAPI）
  - 推论：设明确触发器：≥2 家头部中立路由商+≥1 家厂商采纳，或任何一方公开质疑我们中立性时，立即把 schema+商标打包捐入 AAIF/Linux Foundation 级中立家（MCP 已把该路径跑成 agentic 领域默认剧本，预计时点：产品发布后 12-18 个月），同时保留 CLI/验收器的开发与商业主导权
- **L5 单厂商控制标准对第三方的风险清单（五类）**
  - 证据：①单点 breaking change：MCP 2026-07-28 版与 stateful 过去决裂（The Register 2026-07-23，仓库 schema 目录证实）；②商标/规范家底在厂商侧：SKILL.md 一年后仍无 GOVERNANCE.md、不在 AAIF；③演进偏向母厂产品：Skills 围绕 Claude Code 能力演进；④治理不满致分叉：OpenMCP（HN 2026-09-22）；⑤认证被第三方收走：AAIF 的 MCPA（2026-07-10）成为官方合规通道
  - 推论：我们同时是上游标准的第三方：对 MCP/SKILL.md/AGENTS.md 全部做版本锁定+双格式适配层，不押注任何单一治理结论；这份五类风险清单应写进我们的文档，作为'契约层为何必须中立'对用户的直接论证
- **L6 商业层规律：标准化精确商品化它触碰的那一层——捐出的 schema 永远不是护城河，护城河在执行与认证层**
  - 证据：OCI 救了容器格式，Docker Enterprise 2019 年仍售予 Mirantis；K8s 规范中立后价值归云厂商；SmartBear 捐 OpenAPI 规范靠工具存活；CNCF conformance 与 AAIF MCPA 把认证做成持续价值层；CSA 认证是 Matter 联盟中最持久的资产
  - 推论：持久资产只能是：各厂商 API 差异知识库（每家的坑）、验收执行器、角色资产运行时、以及未来的 conformance 徽章；schema 从第一天按'会被捐出/被抄走'设计，代码与知识才是护城河

### 战略启示（本路）

- 未来 6-12 个月不组联盟不谈治理：全力拿下 ≥2 家中立路由商（fal/OpenRouter 级）+≥1 家头部视频厂商的真实互操作——采纳是中立化谈判的唯一筹码（MCP/JSON/Markdown 共性）
- 契约 schema 按宿主传播设计：JSON Schema+TS 类型+MCP tool 三形态发布、一页读完、先窄后宽；让人能不装我们 CLI 就依赖 schema
- 设中立化触发器并写进公司文档：采纳达标或中立性遭质疑时，schema+商标打包捐 AAIF/LF，CLI/验收器/知识库留下（SmartBear-OpenAPI 模式）；参考 MCP 时序，发布后 12-18 个月内到达该点
- 把单厂商标准五类风险清单产品化：对 MCP/SKILL.md/AGENTS.md 做版本锁定+双格式适配——既保护自己，也是向用户证明中立层价值的活教材
- 复制认证剧本而非规范剧本：中立 conformance 徽章（对标 CNCF conformance/AAIF MCPA/CSA 认证）是把必然商品化的 schema 变回现金流的唯一已知通道

### 未决问题

- SKILL.md/agentskills org 的商标归属与最终治理结构：仓库无 GOVERNANCE.md，agentskills.io 域名注册主体未验证（本次未做 WHOIS）
- MCP 2026-07-28 版 breaking changes 全清单：仅有 The Register 2026-07-23 报道与仓库 schema 目录佐证，未逐条审阅 spec diff
- Matter 2026 年内是否有 1.5 之后新版本：CSA 官网 90 天内未见版本公告；1.5（2025.11）来自二手报道
- AAIF 董事会席位、会员费与 Anthropic 投票权细节：官方页面未披露
- OpenMCP 分叉（2026-09-22，HN 单帖）的真实动机与采用度：无跟踪数据
- Veo/Kling/Seedance/Wan 官方是否已各自下场做 MCP/skills：属生态 lane，需与其他 lane 交叉验证

### 来源

- [Anthropic: Donating the Model Context Protocol and establishing the Agentic AI Foundation (2025-12-09)](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation)
- [OpenAI: OpenAI Co-Founds the Agentic AI Foundation (2025-12-09)](https://openai.com/index/agentic-ai-foundation)
- [Linux Foundation/AAIF: Formation announcement, founding projects MCP/goose/AGENTS.md (2025-12-09)](https://aaif.io/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation-aaif-anchored-by-new-project-contributions-including-model-context-protocol-mcp-goose-and-agents-md/)
- [MCP 官方博客: MCP Joins the Agentic AI Foundation (2025-12-09)](https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/)
- [MCP 规范仓库（GOVERNANCE.md 确认 LF Projects Series；schema/2026-07-28）(抓取于 2026-09-22)](https://github.com/modelcontextprotocol/modelcontextprotocol)
- [AAIF: Introducing the MCPA — first official MCP certification (2026-07-10)](https://aaif.io/blog/introducing-the-mcpa-the-first-official-certification-for-the-model-context-protocol/)
- [The Register: Model Context Protocol prepares to break with its stateful past (2026-07-23)](https://www.theregister.com/devops/2026/07/23/model-context-protocol-prepares-to-break-with-its-stateful-past/5276722)
- [Techstrong: Google Moves A2A Under Agentic AI Foundation (2026-08-18)](https://techstrong.ai/articles/google-moves-a2a-under-agentic-ai-foundation/)
- [HN: Show HN: OpenMCP — an open, code-first fork of MCP (2026-09-22)](https://github.com/enclawed/omcp)
- [Agent Skills 官网（约 48 家采纳产品展示页；'originally developed by Anthropic'）(抓取于 2026-09-22)](https://agentskills.io)
- [agentskills/agentskills 规范仓库（2025-12-16 创建，无 GOVERNANCE.md）(GitHub API, 2026-09-22)](https://github.com/agentskills/agentskills)
- [anthropics/skills（2025-09-22 创建，177k stars，未审计）(GitHub API, 2026-09-22)](https://github.com/anthropics/skills)
- [OpenAPI Initiative 官方 About（SmartBear 捐赠 + Linux Foundation 治理）](https://www.openapis.org/about)
- [Docker 官方博客: Open Container Initiative 捐赠公告 (2015-06)](https://www.docker.com/blog/open-container-initiative/)
- [OCI 官方 Overview](https://opencontainers.org/about/overview/)
- [Mirantis: Mirantis Acquires Docker Enterprise Platform Business (2019-11)](https://www.mirantis.com/blog/mirantis-acquires-docker-enterprise-platform-business/)
- [CoreOS: Kubernetes 1.0 and the Cloud Native Computing Foundation (2015-07-21)](https://coreos.com/blog/kubernetes-1.0-and-cloud-native-computing-foundation/)
- [CNCF: Who We Are（2015 年创立，K8s 为创始项目）](https://www.cncf.io/about/who-we-are/)
- [欧盟委员会: Common charger 新闻稿 IP/22/4949 (2022-06-23)](https://ec.europa.eu/commission/presscorner/detail/en/ip_22_4949)
- [欧盟委员会: Common charger 政策页（2024-12-28 生效）](https://digital-strategy.ec.europa.eu/en/policies/common-charger)
- [CSA: Matter 1.4 Enables More Capable Smart Homes (2024-11)](https://csa-iot.org/newsroom/matter-1-4-enables-more-capable-smart-homes/)
- [CSA Newsroom（2026-09 抓取：Suzi 认证开放 2026-09-02；Matter 仅有会员证言 2026-09-03）](https://csa-iot.org/newsroom/)
- [iClarified: Matter 1.5 Officially Adds Support for Smart Cameras and Energy Management (2025-11)](https://www.iclarified.com/99104/matter-15-officially-adds-support-for-smart-cameras-and-energy-management)
- [RSS 2.0 规范（哈佛 Berkman 托管）](https://cyber.harvard.edu/rss/rss.html)
- [IETF RFC 4287: The Atom Syndication Format (2005-12)](https://datatracker.ietf.org/doc/html/rfc4287)
- [Daring Fireball: Markdown (2004)](https://daringfireball.net/projects/markdown/)
- [CommonMark（2014 分叉）](https://commonmark.org/)
- [GitHub Flavored Markdown Spec (2017)](https://github.github.com/gfm/)
- [json.org（Crockford）](https://www.json.org/json-en.html)
- [IETF RFC 8259: The JavaScript Object Notation (JSON) Data Interchange Format / STD 90 (2017-12)](https://www.rfc-editor.org/rfc/rfc8259)
- [JSON Schema 官网（2026-09 抓取：仍无基金会归属，GitHub+Open Collective）](https://json-schema.org/)


## 终局图谱（被收购/反垄断/IPO/小而利 四条退出路线）

**摘要**：中立层终局图谱：①最常见退出是被上游卡位式收购——NVIDIA $12.9B 收 Hugging Face、Cloudflare 收 Replicate、Databricks 连环并购，价格锚定买方战略价值而非自身收入；②反垄断只在十亿美元级且买方是垄断者时介入（Visa-Plaid 被阻止、Nvidia-Groq 遭回溯调查）；③IPO 门槛≈$150-200M 收入加 50% 以上增速，2026 窗口开启但对 infra 怀疑加深，且 IPO 非终点（HashiCorp 三年后被 IBM 收）；④小而利可行（Basecamp 27 年、Zapier 用 $1.3M 融资到 $5B 估值），但托管成本失控即关闭独立选项。建议：以独立盈利为主路线、被收购为期权，现在开始攒中立承诺、可导出性、干净账本三样筹码。

### 案例

- **NVIDIA 收购 Hugging Face**（2026-09-03 宣布，预计 2027 年交割）→ 结局：**被收购**〔多源交叉〕
  - 经过：NVIDIA 以约 $12.9B（官方公告原文 $12,930,300,000，其中 $1B 留员工）收购开源模型中立枢纽 Hugging Face（18M+ 开发者、3M+ 模型）。HF 一年前曾拒绝 NVIDIA $500M 投资，最终以整售告终。公告写入中立承诺：平台保持开放、不强制使用 NVIDIA 算力。评论界（The Register）警告"开放不等于中立"，担心 Transformers 生态被倾斜向 TRT-LLM 等自家产品。
  - 关键因子：中立枢纽的战略卡位价值远超其收入体量（12.9B 远超任何收入倍数逻辑）；开源基础设施的存储/带宽/算力成本压力由买方兜底，是卖方接受的主因；唯一性即议价权：成为事实标准后拒小钱能换大钱；中立性承诺被写进交易公告，但法律可执行性待考
  - 来源：<https://blogs.nvidia.com/blog/nvidia-to-acquire-hugging-face/>
- **Replicate 并入 Cloudflare**（2025-11-17）→ 结局：**被收购**〔官方源〕
  - 经过：多厂商模型推理聚合 API Replicate 全团队加入 Cloudflare，金额未披露。官方博客承诺 API 不变、品牌延续，叙事是成为"分布式 AI 操作系统"的原语层。没有自有模型的聚合层被云平台收编，是跑通量生意者最典型的归宿。
  - 关键因子：无自有模型的聚合 API 对云厂商是即插即用的卡位资产；用"API 不变"承诺保住客户信任，降低收购对收入的破坏；金额未披露——团队规模级别 deal，而非平台级对价
  - 来源：<https://replicate.com/blog/replicate-cloudflare>
- **ElectricSQL 加入 Databricks/Neon**（2026-08-11）→ 结局：**被收购**〔官方源〕
  - 经过：Postgres 同步引擎 ElectricSQL 加入 Databricks 旗下 Neon，为 agent 数据基建（Lakebase/agent sandboxes）补上同步原语。关键细节：开源项目（Sync、PGlite、TanStack DB、Durable Streams）保留，但 Electric Cloud 托管服务关停，客户必须自托管或迁移。买方只要技术，不要业务线。
  - 关键因子：agent 基础设施是 2025-2026 收购潮的核心主题（Databricks 连环并购 Tecton/Mooncake/Panther/Electric）；小团队承担不起全球托管成本，被收购时托管业务直接关停；客户迁移安排写进公告——中立层死于收购时用户仍需付迁移税
  - 来源：<https://electric.ax/blog/2026/08/11/electric-joining-databricks>
- **Visa 收购 Plaid 被 DOJ 阻止**（2020-01 宣布 $5.3B → 2021-01 放弃）→ 结局：**其他（注明）**〔官方源〕
  - 经过：Visa 拟 $5.3B 收购银行数据中立枢纽 Plaid，DOJ 以"垄断者收购新兴竞争威胁"起诉，交易放弃。结局为其他情形：并购被反垄断阻止后 Plaid 独立存续并壮大，2026-05 成为 ChatGPT 个人金融功能的银行连接器——反垄断把一个 $5.3B 的退出变成了更大的独立资产。
  - 关键因子：只有当买方是垄断者、标的是"未来威胁"时监管才出手；中立枢纽地位本身就是监管保护的对象；被阻止的卖方不一定是输家——独立性反而放大了平台化机会
  - 来源：<https://www.justice.gov/opa/pr/visa-and-plaid-abandon-merger-after-antitrust-division-s-suit-block>
- **NVIDIA-Groq $20B 授权结构遭监管调查**（2025-12 结构曝光 → 2026-09-09 NYT 报道监管调查）→ 结局：**其他（注明）**〔多源交叉〕
  - 经过：NVIDIA 以约 $20B 的非并购授权/雇佣结构取得 Groq 技术与团队，绕过并购申报义务，被评论称为"反垄断漏洞"；NYT 2026-09-09 报道监管机构已对该交易展开调查。结局为其他情形：规避审查的结构性类收购，遭监管回溯介入。监管会迟到，但对规避结构会追认审查。
  - 关键因子：非并购交易结构（授权+挖人）可暂时绕过申报，但正被监管补位；算力层整合引发跨阵营的系统性警觉；中国 SAMR 2025-09 已裁定 NVIDIA 违反反垄断法——全球监管态度趋严
  - 来源：<https://www.nytimes.com/2026/09/09/business/nvidia-groq-antitrust.html>
- **HashiCorp：IPO 标杆，三年后被 IBM 收购**（2021-12 IPO → 2024-04-24 IBM 宣布 $6.4B 收购）→ 结局：**其他（注明）**〔多源交叉〕
  - 经过：HashiCorp IPO 时 FY 收入 $211.9M（+75%），最新季度 +49%，目标估值最高 $13B——这是 infra 软件 IPO 的量化门槛样本。结局为其他情形：IPO 不是终点，增长换挡后估值回落，2024 年被 IBM 以 $6.4B（$35/股）收走，低于 IPO 目标估值。
  - 关键因子：IPO 门槛≈$200M 收入 + 50-75% 增速（ZIRP 时代基准）；上市后增速换挡即估值杀，基础设施软件最终仍倾向归入大平台组合；IPO 的价值在于流动性与期权，不是安全上岸
  - 来源：<https://www.cnbc.com/2021/11/29/hashicorp-aiming-for-ipo-valuation-of-up-to-13-billion-in-updated-s-1.html>
- **Nscale：亏损 AI 云公司递交 IPO**（2026-09-18（90 天内））→ 结局：**其他（注明）**〔单一来源〕
  - 经过：AI 云提供商 Nscale 递交 IPO：收入 $140.6M、净亏损 $1.02B 仍可上会——2026 年窗口对 AI 算力概念敞开，亏损不再是硬门槛。结局为其他情形：已递交招股书、尚未上市。同期 NYT（2026-09-21）报道华尔街对 data-center 热潮的怀疑在加深；窗口内还有 OpenAI（2026-06）、Anthropic（2026-06）、Oura（2026-09-21, $2.2B）等申报/上市。
  - 关键因子：AI 叙事让巨额亏损的 infra 公司也能进入公开市场；窗口开放但情绪分化：纯 infra/数据中心关联度越高，怀疑越重；对中立软件层而言，窗口存在但不友好——仍需真实收入
  - 来源：<https://www.cnbc.com/2026/09/18/nscale-ai-cloud-provider-ipo-nscl.html>
- **37signals/Basecamp：27 年独立盈利**（1999 至今）→ 结局：**幸存并独立壮大**〔官方源〕
  - 经过：无 VC、全 bootstrap 的订阅制软件公司，Basecamp 上线约一年产品收入即超过其设计咨询主业，官网自述"Bootstrapped, profitable, & proud"，2022 年买回贝索斯所持股份（广为报道）。从未被收购、从未 IPO，是"小而利"路线存活时间最长的中立软件样本。
  - 关键因子：订阅收入 + 成本纪律（小团队），27 年不依赖外部资本；不与平台正面竞争（做项目管理而非操作系统），无被卡位价值也就无被吞并压力；收入数字从不公开——私有市场对它无定价权
  - 来源：<https://basecamp.com/about>
- **Zapier：中立自动化层的独立样本**（2011 至今）→ 结局：**幸存并独立壮大**〔多源交叉〕
  - 经过：API 自动化中立层 Zapier 仅用 $1.3M 融资，2021 年二手股交易估值达 $5B（Forbes，未审计的私有市场定价），常年盈利。它证明了纯"连接器"中立层可以不卖身：价值在跨厂商集成关系网本身，且始终不做上游 SaaS 业务。
  - 关键因子：中立连接器的价值随接入厂商数量超线性增长，越中立越值钱；几乎不融资=创始人对退出时机有完全决定权；私有市场二手价（未审计）证明中立层存在真实的大额退出期权
  - 来源：<https://www.forbes.com/sites/alexkonrad/2021/03/08/zapier-bootstraps-to-5-billion-valuation/>

### 定律

- **L1 中立层一旦成为行业互操作枢纽，最常见结局是被上游巨头（芯片/云/模型厂）卡位式收购；收购对价锚定买方的战略价值，与标的自身收入弱相关。**
  - 证据：NVIDIA $12.9B 收 Hugging Face（远超收入倍数）、Cloudflare 收 Replicate（金额未披露的团队/技术级收购）、Databricks 2025-2026 连环并购 agent 数据基建（Tecton/Mooncake/ElectricSQL）。
  - 推论：我们的跨厂商视频"契约+验收+角色资产"层若成为默认互操作点，潜在买家排序：云平台（类 Cloudflare）> 模型厂商 > Agent 平台/创作工具链。现在就该识别"谁最怕别人拥有我们"，并拒绝与任何一家独家绑定——绑定会同时消灭中立价值和多方竞价的可能。
- **L2 反垄断只会保护十亿美元级、且买方是垄断者的中立枢纽；对小型中立层监管不会来救，且监管对规避结构（授权/雇佣式类收购）只会回溯追认、不会事前预防。**
  - 证据：Visa-Plaid $5.3B 被 DOJ 阻止（官方源）；Nvidia-Groq $20B 授权结构被监管事后调查（NYT 2026-09）；中国 SAMR 2025-09 裁定 NVIDIA 违反反垄断法。
  - 推论：我们当前体量的生存策略不能指望反垄断。真正的保护是架构性的：让每一层都可被用户替换（可替代性=难以被卡死），同时保持多买方格局，让潜在收购方互相竞价而非让一家免费拿走互操作权。
- **L3 infra 软件 IPO 的量化门槛约为 $150-200M 收入 + 50% 以上增速；2026 窗口对 AI 概念开启（连 $1B 亏损的算力公司都能上会），但对 infra 怀疑在加深；且 IPO 不是终点，增长换挡后照样被平台收购。**
  - 证据：HashiCorp IPO：FY 收入 $211.9M（+75%）、目标估值 $13B，三年后被 IBM 以 $6.4B 收走；Nscale 2026-09-18 以 $140.6M 收入/净亏 $1.02B 递交 IPO；NYT 2026-09-21 报道华尔街对 data-center 热潮怀疑加深。
  - 推论：对独立开发者体量，IPO 概率≈0（差 2-3 个数量级），不应作为设计目标。但所有退出路径（收购、融资）共用同一套尽调材料：现在就按可审计标准记账——收入可预期（订阅/验收计费）、合同干净、无异常关联授权。
- **L4 小而利是真实可选的主路线，但有硬边界：当中立层的成本结构变重（托管/算力/带宽），独立选项会自动关闭，收购从"选择"变成"必然"。**
  - 证据：Basecamp 27 年独立盈利（轻成本订阅制）、Zapier $1.3M 融资到 $5B（纯连接器不做托管重资产）；反例：Hugging Face 的存储带宽压力被 The Register 列为卖身主因之一，ElectricSQL 被收购后 Electric Cloud 托管直接关停。
  - 推论：路线设计要把"重的部分"外包或收费：契约与验收逻辑是纯软件（便宜、可永久独立），角色资产托管是重的（按成本定价或让用户自带存储 BYO）。只要成本曲线可控，37signals 模式对我们就是主路线而非退路。
- **L5 被收购后下游用户的命运完全取决于交易条款：买方可以选择"API 不变"（Replicate）也可以选择关停托管业务只留开源（ElectricSQL）。对用户而言，可导出性与开源兜底是唯一事前保险；对卖方而言，这些承诺反而是抬价筹码。**
  - 证据：Replicate 官方公告承诺 API 不变、品牌延续；ElectricSQL 官方公告宣布 Electric Cloud 关停、客户需迁移；两者均为 90 天内官方一手源。
  - 推论：现在就把"契约/角色资产可完整导出 + OSS 兜底实现"写成公开产品承诺。它一鱼三吃：获客卖点（对冲 Electric 式关停恐惧）、收购谈判筹码（买家买的是社区信任）、以及最坏情况下的用户保护。

### 战略启示（本路）

- 四条路现实概率（独立开发者+agent 工作流体量）：被收购（含 acq-hire）≈ 最现实的退出通道；独立盈利存续 ≈ 完全可行且应设为主路线；反垄断拯救 ≈ 0（规模不够，监管只保护 billion 级枢纽）；IPO ≈ 0（差 2-3 个数量级）。正确姿势：主路线独立盈利 + 把被收购当免费期权养着。
- 现在就要攒的通用筹码（四条路共用）：①中立性——不与任何一家模型厂/云独家绑定；②可导出性+OSS 兜底的公开承诺；③干净账本与合同（按可审计标准）；④识别并保持与 2-3 类潜在买家（云平台>模型厂>Agent 平台）的非排他接触。
- 独立路线的护栏：重资产部分（资产托管/算力）按成本定价或 BYO，纯软件部分（契约+验收）保持便宜；$1M ARR 之前不扩张成本；永远不碰上游厂商的正面业务（不卖自己的模型和算力），否则中立性归零、只剩被收购一条路。
- 收购路线的抬价逻辑：Hugging Face 案例证明"成为事实标准"比短期收入更能撬动战略对价——优先追求默认互操作点地位；同时现在就写好 Replicate 式"API 不变"承诺条款模板，交割时它是用户保护和谈判筹码的双重资产。
- 时间窗判断：2025-11 至 2026-09 的收购潮（HF/Replicate/ElectricSQL/Groq）说明买方预算充裕、基建整合加速，未来 12-18 个月是中立层卖方议价力最强的窗口；但同期官方协议（MCP/agent skills 类标准）也在最快蚕食中立价值——中立层的真正死法不是被收购，而是被标准取代，所以窗口期内"地位优先于收入"。

### 未决问题

- NVIDIA-Hugging Face 交易能否通过反垄断审查？交割最终条款与"中立承诺"的法律可执行性如何（预计 2027 年交割，公告承诺无合同细节公开）？
- EU 与中国监管在 2026 年（近 90 天）对 AI 基础设施并购的一手表态未找到；中国最近的数据点是 2025-09 SAMR 裁定 NVIDIA 违反反垄断法，欧盟立场本轮完全缺失。
- Replicate 与 ElectricSQL 的交易金额均未披露，"卡位收购"的价格区间下限无法校准——我们这个体量（<20 人团队+可用产品）在当前市场大约值 $10M-100M 还是更低，无一手数据。
- Basecamp 与 Zapier 的收入数字均未审计（前者从不公开，后者是 2021 年私有市场二手交易价）；两个样本的健康度无法精确量化。
- 我们的赛道（跨厂商视频生成契约+验收层）没有直接可比的退出案例——所有规律是从 API 中间件/数据基建外推的，可能低估官方 agent 协议标准化（MCP/skills）取代中立层的速度，也可能低估视频资产（角色一致性数据）的独有卡位价值。

### 来源

- [NVIDIA to Acquire Hugging Face（官方公告，含 $12,930,300,000 与中立承诺）](https://blogs.nvidia.com/blog/nvidia-to-acquire-hugging-face/)
- [The Register: Hugging Face is too important to fall into Nvidia's hands（2026-09-03）](https://www.theregister.com/ai-and-ml/2026/09/03/hugging-face-is-too-important-to-fall-into-nvidias-hands/5294363)
- [Replicate is joining Cloudflare（官方博客，2025-11-17）](https://replicate.com/blog/replicate-cloudflare)
- [Cloudflare: Why Replicate is joining Cloudflare](https://blog.cloudflare.com/why-replicate-joining-cloudflare/)
- [ElectricSQL: Electric is joining Databricks（含 Electric Cloud 关停公告）](https://electric.ax/blog/2026/08/11/electric-joining-databricks)
- [Databricks: Electric joins Databricks to bring WASM Postgres to AI agent sandboxes](https://www.databricks.com/blog/electric-joins-databricks-bring-wasm-postgres-ai-agent-sandboxes)
- [DOJ: Visa and Plaid Abandon Merger After Antitrust Division's Suit](https://www.justice.gov/opa/pr/visa-and-plaid-abandon-merger-after-antitrust-division-s-suit-block)
- [Plaid blog: ChatGPT personal finance powered by Plaid（2026-05-15）](https://plaid.com/blog/chatgpt-personal-finance-plaid/)
- [NYT: Regulators Are Investigating Nvidia's Licensing Deal with Groq（2026-09-09）](https://www.nytimes.com/2026/09/09/business/nvidia-groq-antitrust.html)
- [Nvidia's $20B Antitrust Loophole（Groq 交易结构分析，2025-12，HN 549 pts）](https://ossa-ma.github.io/blog/groq)
- [NYT: Nvidia Ruled to Have Violated China's Antitrust Law（2025-09-15）](https://www.nytimes.com/2025/09/15/business/nvidia-china-antitrust.html)
- [CNBC: HashiCorp aiming for $13B valuation in IPO（含 $211.9M 收入/+75%）](https://www.cnbc.com/2021/11/29/hashicorp-aiming-for-ipo-valuation-of-up-to-13-billion-in-updated-s-1.html)
- [IBM Newsroom: IBM to Acquire HashiCorp for $6.4B（2024-04-24）](https://newsroom.ibm.com/2024-04-24-IBM-to-Acquire-HashiCorp-Inc-Creating-a-Comprehensive-End-to-End-Hybrid-Cloud-Platform)
- [CNBC: AI cloud provider Nscale files for IPO on $140.6M revenue, $1.02B net loss（2026-09-18）](https://www.cnbc.com/2026/09/18/nscale-ai-cloud-provider-ipo-nscl.html)
- [NYT: Wall Street Is Growing Skeptical of the Data Center Boom（2026-09-21）](https://www.nytimes.com/2026/09/21/business/ai-data-center-ipos.html)
- [Bloomberg: Oura seeks $2.2 billion in US IPO（2026-09-21）](https://www.bloomberg.com/news/articles/2026-09-21/smart-ring-maker-oura-backers-seek-2-2-billion-in-us-ipo)
- [CNBC: OpenAI confidentially files for IPO（2026-06-08）](https://www.cnbc.com/2026/06/08/openai-confidentially-files-for-ipo-prepping-wall-street-for-ai-debut.html)
- [NPR: Anthropic files for IPO（2026-06）](https://www.npr.org/2026/06/01/nx-s1-5843199/anthropic-ipo-filing-ai-large)
- [Basecamp/37signals About（27 年独立、bootstrapped & profitable）](https://basecamp.com/about)
- [Forbes: Zapier reached a $5B valuation with $1.3M of funding（2021-03）](https://www.forbes.com/sites/alexkonrad/2021/03/08/zapier-bootstraps-to-5-billion-valuation/)


## 波浪时点（云/移动/LLM 三波复盘 → 视频波相位定位）

**摘要**：三波开发者工具浪潮（云 2006-2014、移动 2008-2016、LLM 2022-2024）显示独立中间件窗口逐代减半：约 8 年→4-5 年→约 12 个月。视频生成 API 波正处爆发早段：近 90 天聚合层密集 Show HN（VideoRouter 9 月、Velokey/APIMart 8 月）、useapi 发布 16 家供应商 Seedance 定价表（商品化信号）、GitHub 年内新增 2678 个视频生成仓库、Claude/Codex 技能层爆发；但供应商官方 MCP（火山 2025-04、MiniMax 2025-04、Runway 2025-06）已提前占位——收编与爆发同季出现，相位较 LLM 波压缩 2-3 倍。定位约等于 LLM 波 2023 年 2-4 月，有效窗口 6-12 个月。结论：全力冲刺，但押注厂商无收编动机的中立资产（验收契约、角色资产、跨模型迁移），不做纯路由。

### 案例

- **LangChain（LLM 工具层标准样本）**（2022-10 至今）→ 结局：**幸存并独立壮大**〔官方源〕
  - 经过：仓库创建于 2022-10-17（GitHub API），PyPI 首版 0.0.1 于 2022-10-25。HN 故事量半年曲线（HN Algolia 可复核）：5→89→167（2023 年中峰值）→139→61→56，即在 OpenAI 2023-11-06 发布 Assistants API 后半年内腰斩。当前仓库自述已从'构建 LLM 应用'转为'The agent engineering platform'（转型平台化求生）。
  - 关键因子：发布后 1.5-6 个月为爆发窗口（89→167 篇 HN 故事）；平台官方吸收该层功能后讨论量立即衰减；幸存靠转型做平台/可积累资产，而非原中间件功能
  - 来源：<https://api.github.com/repos/langchain-ai/langchain>
- **OpenAI Assistants API 吸收有状态中间件（平台吃中间件时刻）**（2023-11-06 起）→ 结局：**被平台杀死**〔多源交叉〕
  - 经过：2023-11-06 DevDay 发布 Assistants API，当日 HN 即有概述帖；两周内出现多个第三方 drop-in replacement 与开源复刻（2023-11-15/16/23 HN），证明该层此前是第三方中间件的生存空间、之后被官方收编。这是 LLM 波'平台吸收'的锚点事件。
  - 关键因子：被吸收的功能恰好是中间件最大卖点（状态/检索/工具调用）；收编事件后第三方复刻只能做兼容层而非增长层；从 LangChain 发布到官方收编仅约 12.5 个月
  - 来源：<https://news.ycombinator.com/item?id=38166460>
- **Parse（MBaaS 移动后端，平台风险经典）**（2011-06 至 2017-01）→ 结局：**被收购**〔单一来源〕
  - 经过：2011-06 创立（Wikipedia），2013 年被 Meta/Facebook 收购，2016 年宣布关停，2017-01 服务关闭并开源 Parse Server。独立 MBaaS 层的兴衰与 iOS/Android 平台方自建后端能力（CloudKit、Firebase 收编策略）同步。
  - 关键因子：依附单一生态的中间件随平台策略摇摆而亡；关停后开源是留存开发者的唯一出路；从创立到关停约 5.5 年——移动波中间件窗口的量尺
  - 来源：<https://en.wikipedia.org/wiki/Parse_(platform)>
- **移动跨平台工具 PhoneGap/Xamarin（被平台原生方案取代）**（2008-07 至 2016）→ 结局：**被收购**〔单一来源〕
  - 经过：App Store 2008-07-10 上线开启移动工具波（Wikipedia）；Nitobi 的 PhoneGap 于 2011 年被 Adobe 收购并开源为 Apache Cordova；Xamarin 2011-05 创立、2016 年被 Microsoft 收编。平台方随后推出 React Native/原生 Swift 等方案，第三方跨平台层或被收购或边缘化。
  - 关键因子：技术可用（App Store）到工具爆发约 1-2 年；退出方式几乎全部是被收购而非独立上市；平台方最终用自家技术栈回收该层价值
  - 来源：<https://en.wikipedia.org/wiki/Xamarin>
- **云基础设施抽象层 Heroku→CloudFormation→Terraform（中立层幸存样本）**（2007-06 至今）→ 结局：**幸存并独立壮大**〔官方源〕
  - 经过：Heroku 2007-06 起开发、后被 Salesforce 收购（收购日期本轮未核实）；AWS CloudFormation 2011-02-25 发布（Wikipedia）——厂商官方 IaC 早于中立层；Terraform 仓库 2014-03-13 创建（GitHub API，49,708 星），凭多云中立胜出并成为事实标准。中立抽象层在'多厂商现实'足够强时可以反向胜过单厂商官方方案。
  - 关键因子：中立抽象层的胜负手是覆盖厂商数量与多云现实强度；官方方案（CloudFormation）先发 3 年仍未能锁死中立层；云波独立基础设施层窗口约 8 年（2006→2014）
  - 来源：<https://api.github.com/repos/hashicorp/terraform>
- **视频生成聚合/统一 API 层（2026 现状）**（2026-07 至 2026-09（近 90 天））→ 结局：**仍在竞争中**〔多源交叉〕
  - 经过：VideoRouter（Show HN 2026-09-11/16，官网自述'OpenRouter for video & image'，聚合 Fal/WaveSpeedAI/Replicate/Novita/Sora/Veo/Kling/MiniMax/Luma 等，以自动路由与省价为卖点，1-2 HN 点）；Velokey（2026-08-04 Show HN，OpenAI 兼容、100+ 模型，1 点）；APIMart（2026-08-14，折价聚合，7 点）；useapi 2026-07-21 发布覆盖 16 家供应商的 Seedance 2.0 API 定价数据集——同质聚合密集发布+跨厂商比价表出现，均为商品化前夜信号，尚无赢家。
  - 关键因子：聚合层多家同时 Show HN 且热度仅 1-7 点=无人破圈；16 家供应商卖同一模型 API=分润层已被压薄；定价/折扣为主要卖点=价值主张最易被官方兼容层取代
  - 来源：<https://news.ycombinator.com/item?id=49733974>
- **供应商官方 MCP/技能占位 + 代理端技能层爆发（2026 现状）**（2025-04 至 2026-09）→ 结局：**仍在竞争中**〔官方源〕
  - 经过：官方下场：MiniMax-AI/MiniMax-MCP（2025-04-10，1,585 星）、volcengine/mcp-server（2025-04-12，327 星）、runwayml/runway-api-mcp-server（2025-06-13）。第三方：sora-mcp（2025-10，209 星）、mcp-kling（2025-06）、vibeframe（2026-02，Seedance/Runway/Veo/Kling 接入编码代理，169 星）。技能层：video-shotcraft（2026-07，9,225 星）、anything2explainer（2026-09）等 Claude Code/Codex 视频技能；2026 年内新增 topic:video-generation 仓库 2,678 个（GitHub API），多为应用/技能而非 SDK 包装。
  - 关键因子：官方 MCP 比聚合层爆发早约 12-16 个月出现（与 LLM 波顺序相反）；编码代理（Claude Code/Codex）成为视频 API 的分发入口；应用/技能层数量远超工具层=价值正流向应用端
  - 来源：<https://github.com/MiniMax-AI/MiniMax-MCP>

### 定律

- **L1 开发者工具波的独立中间件窗口逐代减半：云约 8 年、移动约 4-5 年、LLM 约 12 个月；视频波因供应商提前占位与建设者带着 LLM 波经验入场，窗口估计仅 6-12 个月——里程碑必须按季度而非按年设。**
  - 证据：云：EC2 2006→Terraform 2014-03（GitHub API）；移动：App Store 2008-07（Wikipedia）→Parse 2016 宣布关停（Wikipedia）；LLM：LangChain 2022-10-17（GitHub API）→Assistants API 2023-11-06（HN），且 HN 故事量峰值（167，2023 年中）后两个半年衰减至 56-61；视频波：官方 MCP（2025-04/06）与聚合层爆发（2026-07/09）同季活跃（GitHub API + HN Algolia）。
  - 推论：按 LLM 波节奏排 18 个月路线图等于自杀；正确姿势是以季度为单位交付外部可见资产（可复用的验收数据集、角色资产格式、契约测试套件），任何连续两个季度不产生外部可见资产的投入都视为进度落后。
- **L2 平台官方动手做你这一层（Assistants API、官方 MCP）就是中间件的死刑判决书，纯路由/纯转发最先死；活下来的是平台没有动机做、又需要跨厂商中立的资产。**
  - 证据：Assistants API 发布（2023-11-06，HN）后 LangChain 半年故事量 139→61；火山/MiniMax/Runway 官方 MCP 已存在 12-16 个月（GitHub API）；VideoRouter 以'OpenRouter for video+省价'为卖点（官网+HN），说明路由层已在打价格战；useapi 的 16 家定价表宣告转售分润被压薄。
  - 推论：中立契约层绝不能停在'统一 API 调用'——官方 OpenAI 兼容端点和官方 MCP 会吃掉这层。把工程权重压在三处官方不愿碰的位置：跨厂商验收/质量判定标准、角色一致性资产库（跨模型可迁移）、契约测试（同一输入在不同厂商间的可预期差异描述）。
- **L3 '太迟'有四个可观测信号——同质聚合层密集 Show HN、跨厂商价格对比表出现、应用层自建仓库数超过工具包装层、官方占位完成——信号全亮之后再入场只能做应用，不能做层。**
  - 证据：LLM 波对照：2023 年中聚合/包装层 Show HN 密集化+LiteLLM 2023-07-27 出现后，工具层新通用框架再难复制 LangChain 位置；视频波近 90 天已点亮三盏：VideoRouter/Velokey/APIMart 同季 Show HN（HN Algolia）、useapi 16 家定价表（2026-07-21）、2026 年内 2,678 个 topic:video-generation 新仓库且多为应用/技能（GitHub API），唯官方'验收/角色资产'占位未亮。
  - 推论：当前强度判定为'全力冲刺但方向限定'：扩张一切能积累数据与标准的动作（验收规则、角色资产、迁移契约），不在价格路由上消耗资源；同时立即建立相位仪表盘，第四盏灯（官方开始内置验收或角色功能）一旦亮起，立即从扩张转向深耕存量与收租。

### 战略启示（本路）

- 定位：视频 API 波≈LLM 波 2023 年 2-4 月（爆发早段），但供应商收编信号提前同季出现，有效窗口 6-12 个月，按季度设里程碑，全力冲刺。
- 放弃'纯统一 API/路由'叙事：省价与聚合已被 VideoRouter/Velokey/APIMart 和官方兼容端点商品化，主打跨厂商验收契约+角色资产中立层。
- 学习 Terraform 胜 CloudFormation 的路径：中立层赢在多云现实的强度——主动覆盖并公开标注每家厂商（Veo/Kling/Seedance/Sora）的验收差异，把契约层做成'可携带的验收结果标准'。
- 抢占编码代理入口：Claude Code/Codex 技能层（video-shotcraft 9,225 星等）已是分发渠道，官方 MCP 均未内置验收/角色能力，这是 6-12 个月窗口内的空位。
- 建立相位仪表盘并预设开关：跟踪官方 MCP 是否内置验收/角色功能、聚合层是否出现破圈赢家、HN/GitHub 工具层故事量首次环比下降——任一触发即停止扩张、转向深耕存量客户与数据资产变现。

### 未决问题

- 视频波 T0（Seedance/Veo/Kling/Sora API 正式开放日）未逐一核实，相位推算以聚合层与仓库增长反推，误差可能达一个季度。
- OpenRouter 在 LLM 波的确切发布日未核实：HN Algolia 2023 上半年'openrouter'故事 0 命中，可能未发 Show HN，无法用它做聚合层出现时刻的精确对照。
- Heroku 被 Salesforce 收购的具体日期、LangChain 融资细节（种子/A 轮金额）本轮未重新核实，正文已避开这些数字。
- VideoRouter/Velokey/APIMart/useapi 均无公开收入或调用量数据，'无人破圈'的判断仅基于 HN 热度（1-7 点）这一代理指标，可能低估其私有客户盘。
- Kling/快手官方是否已发布 MCP 未确认（GitHub org:klingai 搜索 mcp 为 0，但可能存在于其他 org 或未开源）。
- SamurAIGPT/Generative-Media-Skills 与 py-gpt 等仓库 created_at（2023）与内容（Claude Code 技能）明显不符，疑为改造旧仓库，相关 created_at 已排除不用。

### 来源

- [GitHub API: langchain-ai/langchain (created 2022-10-17)](https://api.github.com/repos/langchain-ai/langchain)
- [PyPI: langchain 首版 0.0.1 (2022-10-25)](https://pypi.org/pypi/langchain/json)
- [HN: Assistants API Overview (2023-11-06)](https://news.ycombinator.com/item?id=38166460)
- [HN Algolia: langchain 故事量曲线（可复核查询）](https://hn.algolia.com/api/v1/search?query=langchain&tags=story)
- [Wikipedia: Parse (platform)](https://en.wikipedia.org/wiki/Parse_(platform))
- [Wikipedia: App Store (Apple) — initial release July 10, 2008](https://en.wikipedia.org/wiki/App_Store_(iOS))
- [Wikipedia: Xamarin](https://en.wikipedia.org/wiki/Xamarin)
- [Wikipedia: Apache Cordova / PhoneGap (Nitobi, Adobe 2011)](https://en.wikipedia.org/wiki/PhoneGap)
- [Wikipedia: AWS CloudFormation — released February 25, 2011](https://en.wikipedia.org/wiki/AWS_CloudFormation)
- [GitHub API: hashicorp/terraform (created 2014-03-13)](https://api.github.com/repos/hashicorp/terraform)
- [HN: VideoRouter — OpenRouter for video and image generation APIs (2026-09-16)](https://news.ycombinator.com/item?id=49733974)
- [VideoRouter 官网（聚合范围与自动路由自述）](https://videorouter.sh)
- [HN: Velokey — One Task API for Kling, Veo, Seedance, and Sora (2026-08-04)](https://news.ycombinator.com/item?id=49163659)
- [HN: useapi — Open pricing dataset for the Seedance 2.0 API, across 16 vendors (2026-07-21)](https://news.ycombinator.com/item?id=48998730)
- [HN: APIMart — Discounted AI API Aggregator for GPT-5, Sora 2 (2026-08-14)](https://news.ycombinator.com/item?id=49299000)
- [HN: Seedance 2.5 (2026-08-01, 442 pts)](https://news.ycombinator.com/item?id=49138302)
- [GitHub: MiniMax-AI/MiniMax-MCP（官方 MCP，2025-04-10）](https://github.com/MiniMax-AI/MiniMax-MCP)
- [GitHub: volcengine/mcp-server（官方，2025-04-12）](https://github.com/volcengine/mcp-server)
- [GitHub: runwayml/runway-api-mcp-server（官方，2025-06-13）](https://github.com/runwayml/runway-api-mcp-server)
- [GitHub Search API: topic:video-generation created:>2026-01-01（2,678 仓库）](https://api.github.com/search/repositories?q=topic:video-generation+created:%3E2026-01-01&sort=stars)
