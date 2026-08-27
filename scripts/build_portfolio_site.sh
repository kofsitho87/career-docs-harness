#!/usr/bin/env bash

set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
output_dir="$repo_root/portfolio/dist"
staging_dir="$(mktemp -d "${TMPDIR:-/tmp}/portfolio-site.XXXXXX")"

cleanup() {
  rm -rf "$staging_dir"
}
trap cleanup EXIT

mkdir -p "$staging_dir/assets"

sed 's#\.\./assets/#./assets/#g' \
  "$repo_root/portfolio/html/heewung-song-portfolio.html" \
  > "$staging_dir/index.html"

for asset in \
  agent-admin-warm-transfer-evidence.png \
  agent-admin-call-classification-evidence.png \
  cupix-ax-operations-screen.png \
  cupix-ax-analytics-screen.png \
  aiu-web-knowledge-answer.png
do
  cp "$repo_root/portfolio/assets/$asset" "$staging_dir/assets/$asset"
done

rm -rf "$output_dir"
mv "$staging_dir" "$output_dir"
trap - EXIT

printf 'Built portfolio site in %s\n' "$output_dir"
