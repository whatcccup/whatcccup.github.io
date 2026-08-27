from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TUTORIAL_ROOT = ROOT / "docs" / "tutorials"
OUTPUT = ROOT / "docs" / "assets" / "tutorial-tags.json"
PREFERRED_TAG_ORDER = [
    "Obsidian",
    "视频学习",
    "内容采集",
    "本地转录",
    "AI Agent",
    "Skills",
    "快捷指令",
    "移动效率",
]


def strip_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1].replace('\\"', '"')
    return value


def read_frontmatter(path: Path) -> tuple[str, list[str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return path.stem, []

    title = path.stem
    tags: list[str] = []
    in_tags = False
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if line.startswith("title:"):
            title = strip_quotes(line.split(":", 1)[1])
            in_tags = False
        elif line.startswith("tags:"):
            in_tags = True
        elif in_tags and line.startswith("  - "):
            tags.append(strip_quotes(line[4:]))
        elif line and not line.startswith(" "):
            in_tags = False
    return title, tags


def main() -> None:
    tutorials = []
    seen_tags: set[str] = set()
    for path in sorted(TUTORIAL_ROOT.rglob("*.md")):
        if path.name == "index.md":
            continue
        title, tags = read_frontmatter(path)
        relative_path = path.relative_to(ROOT / "docs").with_suffix("")
        tutorials.append(
            {
                "path": f"{relative_path.as_posix()}/",
                "title": title,
                "tags": tags,
            }
        )
        seen_tags.update(tags)

    tags = [tag for tag in PREFERRED_TAG_ORDER if tag in seen_tags]
    tags.extend(sorted(seen_tags.difference(tags)))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps({"tags": tags, "tutorials": tutorials}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
