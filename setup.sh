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

clone https://github.com/higgsfield-ai/skills.git            higgsfield-skills      f83af0bc1d937c8119099a11f8ebbf5e6fb99819
clone https://github.com/runwayml/skills.git                 runwayml-skills        e3dffc1
clone https://github.com/runwayml/runway-mcp-plugin.git      runway-mcp-plugin      f56e77a
clone https://github.com/AtlasCloudAI/atlas-cloud-skills.git atlascloud-skills      5ce115e6ede3f950490c375c4c5b94b60c0775ee
clone https://github.com/fal-ai-community/skills.git         fal-community-skills   9ca8504
clone https://github.com/elevenlabs/plugin.git               elevenlabs-plugin      c7eef3cbcf1ff3ef12066a4e8ea964749d8e94be
clone https://github.com/anthropics/skills.git               anthropics-skills      dbd4588f9e1033efb41dad4bef2f7947c8993d44

echo "完成。下一步: uv run --with markdown python build_skills_site.py"
