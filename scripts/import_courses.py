from __future__ import annotations

from pathlib import Path
import re

from bs4 import BeautifulSoup
from markdownify import markdownify

from generate_tag_index import main as generate_tag_index


ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT.parent / "legaltechcc-site" / "courses"
OUTPUT_ROOT = ROOT / "docs" / "tutorials" / "obsidian"

COURSES = [
    {
        "slug": "obsidian-web-clipper-bilibili",
        "bvid": "BV1s6TF6hECB",
        "date": "2026-06-30",
        "kicker": "OBSIDIAN · WEB CLIPPER",
        "tags": ["Obsidian", "视频学习", "内容采集"],
    },
    {
        "slug": "obsidian-web-clipper-transcript",
        "bvid": "BV1F93463E35",
        "date": "2026-07-31",
        "kicker": "OBSIDIAN · TRANSCRIPT",
        "tags": ["Obsidian", "视频学习", "本地转录"],
    },
    {
        "slug": "claudian-theschema-setup",
        "bvid": "BV1gbbi6cEeQ",
        "date": "2026-08-18",
        "kicker": "OBSIDIAN · LOCAL AGENT",
        "tags": ["Obsidian", "AI Agent", "Skills"],
    },
    {
        "slug": "obsidian-shortcuts-voice-journal",
        "bvid": "BV13nhG6KEpA",
        "date": "2026-08-25",
        "kicker": "OBSIDIAN · SHORTCUTS",
        "tags": ["Obsidian", "快捷指令", "移动效率"],
        "description": "用 Shortcuts、Daily Notes 与 Advanced URI，把语音内容写入当天笔记的灵感、TODO 或日记区块。",
        "extra": (
            "> 演示所用快捷指令已经整理完成："
            "[添加到 iPhone 快捷指令](https://www.icloud.com/shortcuts/6ba312c9def04548ba609f01a32cdf3b)。"
            "添加后，请先替换 Vault 名称并检查目标 block ID。\n"
        ),
    },
]


def clean_markdown(value: str) -> str:
    value = value.replace("\xa0", " ")
    value = re.sub(r"\n[ \t]+\n", "\n\n", value)
    value = re.sub(r"\n{3,}", "\n\n", value)
    return value.strip() + "\n"


def import_course(course: dict[str, str]) -> None:
    source = SOURCE_ROOT / course["slug"] / "index.html"
    soup = BeautifulSoup(source.read_text(encoding="utf-8"), "html.parser")
    article = soup.select_one("article.source-course")
    content = soup.select_one(".source-content")
    if article is None or content is None:
        raise RuntimeError(f"Cannot find course content in {source}")

    heading = article.select_one("h1")
    title = heading.get_text(" ", strip=True) if heading else course["slug"]
    lead = article.select_one(".lead")
    description = course.get("description") or (lead.get_text(" ", strip=True) if lead else "")
    body = clean_markdown(markdownify(str(content), heading_style="ATX", bullets="-"))

    bvid = course["bvid"]
    player = (
        '<div class="video-embed">\n'
        f'  <iframe src="https://player.bilibili.com/player.html?bvid={bvid}&page=1&high_quality=1&danmaku=0&autoplay=0" '
        'title="B 站课程视频" loading="lazy" allowfullscreen></iframe>\n'
        '</div>\n\n'
        f'<p class="video-link"><a href="https://www.bilibili.com/video/{bvid}/" target="_blank" rel="noopener">'
        '在 B 站打开 →</a></p>\n'
    )
    extra = course.get("extra", "")
    safe_title = title.replace('"', '\\"')
    safe_description = description.replace('"', '\\"')
    tags = "\n".join(f"  - {tag}" for tag in course["tags"])
    page = f'''---
title: "{safe_title}"
description: "{safe_description}"
tags:
{tags}
---

<span class="course-kicker">{course["kicker"]}</span>

# {title}

<p class="course-lead">{description}</p>

<div class="course-meta"><span>教程</span><span>更新：{course["date"]}</span><span>B 站视频</span></div>

{player}

{extra}
{body}'''
    target = OUTPUT_ROOT / f"{course['slug']}.md"
    target.write_text(page, encoding="utf-8")


def main() -> None:
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    for course in COURSES:
        import_course(course)
    generate_tag_index()


if __name__ == "__main__":
    main()
