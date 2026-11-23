#!/usr/bin/env bash
# 重建调研快照：按 pinned SHA 克隆 7 个厂商技能仓库。
# 用法: ./setup.sh
set -euo pipefail
cd "$(dirname "$0")"

clone() {
  local url=$1 dir=$2 sha=$3
  if [ -d "$dir/.git" ]; then
    echo "✓ $dir 已存在，跳过"
    return
  fi
  echo "→ 克隆 $url"
  git clone "$url" "$dir"
  git -C "$dir" checkout --detach "$sha"
  echo "✓ $dir @ $sha"
}

clone https://github.com/higgsfield-ai/skills.git            higgsfield-skills      27000402070db19d958789d05b3b52b6f4718d7c
clone https://github.com/runwayml/skills.git                 runwayml-skills        6e98d3f3540705331acd748d75427f4bd7c90ce1
clone https://github.com/runwayml/runway-mcp-plugin.git      runway-mcp-plugin      f56e77a
clone https://github.com/AtlasCloudAI/atlas-cloud-skills.git atlascloud-skills      c4bf4c54031b42039cebf3d5fd109f7e96dca20a
clone https://github.com/fal-ai-community/skills.git         fal-community-skills   ca79376d624d244e601f9182fa80b5bf66efec9c
clone https://github.com/elevenlabs/plugin.git               elevenlabs-plugin      9650905958df9e29255f890f2e968b0047fcf944
clone https://github.com/anthropics/skills.git               anthropics-skills      e4bb5d960d87126ff3b3a8af1a104b7db67560ba

echo "完成。下一步: uv run --with markdown python build_skills_site.py"
