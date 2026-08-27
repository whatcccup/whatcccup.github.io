# 测测的 AI 笔记

使用 Material for MkDocs 构建的 Markdown 网站。

## 教程目录

教程按主题文件夹组织：

```text
docs/tutorials/
├── index.md
└── obsidian/
    ├── index.md
    ├── .pages
    └── *.md
```

以后可以在 `docs/tutorials/` 下增加与 `obsidian/` 并列的新分类。每个分类建议包含：

- `index.md`：分类介绍页。
- `.pages`：分类名称与页面顺序。
- 教程 Markdown：每篇教程一个文件。

## 在 GitHub 上传教程

1. 复制 [`templates/tutorial.md`](templates/tutorial.md)。
2. 把新文件上传到对应分类，例如 `docs/tutorials/obsidian/`。
3. 在文件开头填写 `title`、`description` 和 `tags`：

```yaml
---
title: 教程标题
description: 一句话介绍
tags:
  - Obsidian
  - 视频学习
---
```

4. 把改动提交到 GitHub 的 `main` 分支。

提交后，GitHub Actions 会自动：

1. 扫描所有分类文件夹中的 Markdown。
2. 更新左侧 Tag 筛选索引。
3. 把 Markdown 构建成 HTML。
4. 发布到 `gh-pages` 分支。

只上传 Markdown 即可更新教程，但必须满足三个条件：文件位于 `docs/tutorials/<分类>/`、提交到 `main` 分支、仓库已经启用 GitHub Pages 和 Actions。

## 页面顺序

- `docs/tutorials/.pages` 控制分类顺序。
- 分类内的 `.pages` 控制教程顺序。
- `.pages` 中的 `...` 会自动收录没有显式列出的新文件，并放在已固定页面之后。
- 如果要精确调整一篇新教程的位置，把它的文件名加入对应分类的 `.pages` 即可。

## 插入 B 站视频

Markdown 中可以直接插入 HTML。推荐复制模板里的播放器区块，只替换两处 BV 号：

```html
<div class="video-embed">
  <iframe src="https://player.bilibili.com/player.html?bvid=BV号&page=1&high_quality=1&danmaku=0&autoplay=0" title="B 站课程视频" loading="lazy" allowfullscreen></iframe>
</div>

<p class="video-link"><a href="https://www.bilibili.com/video/BV号/" target="_blank" rel="noopener">在 B 站打开 →</a></p>
```

`autoplay=0` 明确关闭自动播放；iframe 也没有申请 `autoplay` 权限。用户需要主动点击后才会播放。

本地首次预览：

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python scripts/generate_tag_index.py
.venv/bin/mkdocs serve
```

推送到 GitHub 的 `main` 分支后，工作流会自动构建并发布到 `gh-pages` 分支。
