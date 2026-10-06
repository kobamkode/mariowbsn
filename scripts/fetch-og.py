#!/usr/bin/env python3
"""Fetch a related Openverse image for a Hugo post and compose an OG card.

Usage: scripts/fetch-og.py content/posts/<slug>.md

Reads the post's TOML front matter, searches Openverse (no API key) using the
post tags (fallback: title), downloads the top result, and composes
assets/images/og/<slug>.png via scripts/make-og.sh.

Openverse images are mostly Creative Commons. The script prints the credit
line, include it in the post when the license requires attribution.
"""

import json
import os
import re
import subprocess
import sys
import tempfile
import tomllib
import urllib.parse
import urllib.request

API = "https://api.openverse.org/v1/images/"
UA = "mariowbsn-og/1.0 (+https://mariowbsn.com)"


def front_matter(path):
    text = open(path, encoding="utf-8").read()
    if not text.startswith("+++"):
        sys.exit(f"{path}: no TOML front matter")
    return tomllib.loads(text[3:text.index("+++", 3)])


def search(query):
    qs = urllib.parse.urlencode({
        "q": query,
        "page_size": "10",
        "license_type": "commercial",
        "license": "cc0,pdm,by,by-sa",
        "mature": "false",
    })
    req = urllib.request.Request(API + "?" + qs, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp).get("results", [])


def download(url, out):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as resp, open(out, "wb") as f:
        f.write(resp.read())


def main():
    if len(sys.argv) not in (2, 3):
        sys.exit("usage: fetch-og.py content/posts/<slug>.md [search query]")
    src = sys.argv[1]
    fm = front_matter(src)
    slug = os.path.basename(src).removesuffix(".md")
    title = fm.get("title", slug)
    tags = [str(t) for t in fm.get("tags", [])]
    title_main = re.split(r"[:|–—-]", title)[0].strip()

    if len(sys.argv) == 3:
        queries = [sys.argv[2]]
    else:
        queries = [" ".join(tags), title_main, title, *tags]
    pick = None
    for q in dict.fromkeys(q for q in queries if q):
        pick = next((r for r in search(q) if r.get("url")), None)
        if pick:
            query = q
            break
    if not pick:
        sys.exit(f"no image found for: {queries}")

    out = f"assets/images/og/{slug}.png"
    fd, tmp = tempfile.mkstemp()
    os.close(fd)
    try:
        download(pick["url"], tmp)
        subprocess.run(
            ["scripts/make-og.sh", title, out, "mariowbsn.com", tmp],
            check=True,
        )
    finally:
        os.unlink(tmp)

    print(f"image:  {out}")
    print(f"query:  {query!r}")
    print(f"credit: {pick.get('title', '?')} by {pick.get('creator', '?')} "
          f"({pick.get('license', '?')}) {pick.get('foreign_landing_url', '')}")
    print(f"wire:   images = ['{out}']")


if __name__ == "__main__":
    main()
