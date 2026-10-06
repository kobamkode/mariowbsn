#!/usr/bin/env bash
set -euo pipefail

# Generate a 1200x630 Open Graph card.
# Usage: scripts/make-og.sh "Title" [output.png] [subtitle] [background]
#   output defaults to assets/images/og-image.png
#   subtitle defaults to mariowbsn.com
#   background: optional photo, cover-cropped + darkened behind the title
# Needs ImageMagick (magick) + Liberation Sans fonts.

title=${1:?usage: make-og.sh "Title" [output.png] [subtitle] [background]}
out=${2:-assets/images/og-image.png}
subtitle=${3:-mariowbsn.com}
background=${4:-}

mkdir -p "$(dirname "$out")"

base=$(mktemp --suffix=.png)
trap 'rm -f "$base"' EXIT

if [[ -n "$background" ]]; then
  magick "$background" -auto-orient -resize '1200x630^' -gravity center -extent 1200x630 \
    -fill '#0d1117' -colorize 55% "$base"
else
  magick -size 1200x630 xc:'#0d1117' "$base"
fi

magick "$base" \
  \( -background none -fill '#e6edf3' -font Liberation-Sans-Bold -pointsize 64 \
     -size 1040x460 caption:"$title" \) \
  -gravity center -geometry +0-40 -composite \
  -fill '#7d8590' -font Liberation-Sans -pointsize 32 \
  -gravity south -annotate +0+50 "$subtitle" \
  "$out"

echo "wrote $out"
