#!/usr/bin/env bash
# 重建调研快照：按 pinned SHA 克隆 7 个厂商技能仓库。
# 用法: ./setup.sh
set -euo pipefail
cd "$(dirname "$0")"

clone() {
  local url=$1 sha=$2 dir=$3
  if [ -d "$dir/.git" ]; then
    echo "✓ $dir 已存在，跳过"
    return
  fi
  echo "→ 克隆 $url"
  git clone "$url" "$dir"
  git -C "$dir" checkout --detach "$sha"
  echo "✓ $dir @ $sha"
}

clone https://github.com/higgsfield-ai/skills.git            higgsfield-skills      d071406
clone https://github.com/runwayml/skills.git                 runwayml-skills        e3dffc1
clone https://github.com/runwayml/runway-mcp-plugin.git      runway-mcp-plugin      f56e77a
clone https://github.com/AtlasCloudAI/atlas-cloud-skills.git atlascloud-skills      d032b2c
clone https://github.com/fal-ai-community/skills.git         fal-community-skills   9ca8504
clone https://github.com/elevenlabs/plugin.git               elevenlabs-plugin      1c5f1de
clone https://github.com/anthropics/skills.git               anthropics-skills      34040c9

echo "完成。下一步: uv run --with markdown python build_skills_site.py"
