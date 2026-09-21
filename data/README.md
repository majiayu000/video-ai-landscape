# 活数据 · Living Data

机器可读的跨厂商数据集。与 `docs/` 的叙事报告不同，这里只放**结构化事实**，每条带 `as_of` 与来源 URL，供 CLI 路由 / 成本估算 / 供应商健康检查直接消费。

## 数据集

| 文件 | 内容 | schema |
|---|---|---|
| `prices.json` | 视频生成跨厂商价格表（含同模型跨供应商价差、隐性成本） | `schema/prices.schema.json` |
| `capabilities.json` | 能力矩阵：首尾帧/延长/参考/音画同生/分辨率/时长/区域/webhook/URL 有效期 | `schema/capabilities.schema.json` |
| `provider-health.json` | 供应商健康信号：changelog 频率、招聘、deprecation、仓库活跃度、资金状态 | 手工维护（见下） |

## 纪律

1. **每条记录必须有 `source_url` 与 `confidence`**（官方源 / 多源交叉 / 单一来源）——没有来源的字段不录入。
2. **顶层 `as_of` 是数据实采日**。CI 每周检查新鲜度，超过 30 天未更新会在 Actions Summary 里标黄（不阻塞构建）。
3. **价格为原值 + 单位原样记录**，不做跨币种换算（换算留给消费方，避免汇率引入错误）；`normalization_notes` 记录归一化建议。
4. 商业数字（估值、收入）不进本目录——那是 `docs/` 带置信度标注的调研内容，不是可计算的契约数据。

## 更新流程

```bash
# 数据由调研会话实采后填入（agent 实抓官方页面），然后：
git add data/ && git commit -m "data: refresh prices/capabilities (as_of YYYY-MM-DD)"
```

CI（`.github/workflows/refresh.yml`）每周一自动运行新鲜度检查；人工触发 workflow 时同样执行。
