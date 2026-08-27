---
title: "利用 Obsidian Web Clipper 快速学习 B 站视频内容"
description: "有字幕的 B 站视频，可以一键剪藏，自动抓取字幕，并用 AI 生成结构化学习笔记。"
tags:
  - Obsidian
  - 视频学习
  - 内容采集
---

<span class="course-kicker">OBSIDIAN · WEB CLIPPER</span>

# 利用 Obsidian Web Clipper 快速学习 B 站视频内容

<p class="course-lead">有字幕的 B 站视频，可以一键剪藏，自动抓取字幕，并用 AI 生成结构化学习笔记。</p>

<div class="course-meta"><span>教程</span><span>更新：2026-06-30</span><span>B 站视频</span></div>

<div class="video-embed">
  <iframe src="https://player.bilibili.com/player.html?bvid=BV1s6TF6hECB&page=1&high_quality=1&danmaku=0&autoplay=0" title="B 站课程视频" loading="lazy" allowfullscreen></iframe>
</div>

<p class="video-link"><a href="https://www.bilibili.com/video/BV1s6TF6hECB/" target="_blank" rel="noopener">在 B 站打开 →</a></p>



## 适用场景

适用于有字幕的 B 站视频：一键剪藏，自动抓字幕，并用 AI 生成结构化笔记。

## 一、为什么需要这个工具

B 站是学习的重要来源，但视频有两个常见问题：

1. **看完就忘**：视频信息密度低，时间戳定位困难。
2. **无法搜索**：事后想找某个知识点，只能靠记忆或逐帧翻。

Obsidian Web Clipper CN 解决了这两个问题：抓取平台自带字幕，并用 AI 自动生成结构笔记。

## 二、安装与配置

### 2.1 安装 Web Clipper CN（中文增强版）

> 官方版不支持 B 站，需要用 Next 蔡蔡开发的 `obsidian-clipper-cn`。

安装方式：

1. 访问 GitHub：[nextcaicai/obsidian-clipper-cn](https://github.com/nextcaicai/obsidian-clipper-cn)。
2. 进入 Release 页面，下载对应版本并解压。
3. 打开 Chrome，进入 `chrome://extensions/`。
4. 开启「开发者模式」。
5. 选择「加载已解压的扩展程序」，选中解压后的文件夹。

### 2.2 配置保管库

打开插件 popup，填入你的 Obsidian 保管库名称，按回车确认。

### 2.3 配置 AI 解释器（关键步骤）

解释器，是剪藏时调用 AI 自动总结内容的配置。

配置供应商：

- 推荐 **DeepSeek**，便宜、速度快；也可以使用 Gemini Flash。
- 填入 `baseurl` 和 API key。
- 模型填 `deepseek-v4-flash`。

默认解释器上下文：

```
{{content}}
```

## 2.4 配置 B 站专用模板

点击已有模板，选择「复制模板」。建议不要新建，因为字段较多，复制后再改更稳。

| 字段 | 值 |
| --- | --- |
| 触发器 | `http://www.bilibili.com/` |
| 笔记位置 | `00-inbox` |
| 笔记名称 | `{{title}}` |

模板内容（B 站视频核心配置）：

```
[视频链接]({{meta:property:og:url}})

{{"根据用户提供的 transcript 转录内容和视频链接，生成结构化的教程笔记。视频链接由用户单独提供或在 transcript 开头注明，请提取该链接并用于所有时间戳跳转。遵循以下原则：1.语言要求：- 笔记必须使用 中文 撰写。- 专有名词、技术术语、品牌名称和人名应适当保留 英文。 2.笔记要求：- 完整信息：尽可能详细地记录教程内容，特别是关键点和重要的结论步骤。 - 去除无关内容：省略广告、填充词、问候语和不相关的言论。 - 保留关键细节：保留重要事实、示例、结论和建议。- 可读布局：必要时使用项目符号，并保持段落简短，增强可读性。- 视频中提及的数学公式必须保留，并以 LaTeX 语法形式呈现，适合 Markdown 渲染。 3.输出说明：- 仅返回最终的 Markdown 内容。- 不要将输出包裹在代码块中。- 避免将编号标题写成有序列表格式，应使用 ## 1. 内容 或 1. **内容** 的形式。4.额外重要任务：- 目录：在笔记开头自动生成一个基于 ## 级标题的目录。目录项为纯文本标题，不要添加任何时间戳跳转链接。- 正文章节标题：每个章节总结标题，并立即添加时间戳跳转，格式为 ## 章节标题-[mm:ss](用户提供的视频链接?t={总秒数})。正确示例：## 1. AI 的发展史- [03:44](https://www.bilibili.com/video/BV1dVopBwEzp/?t=222)。注意：标题在前，跳转标记紧跟其后。-- 禁止使用示例链接：所有跳转链接必须使用用户本次提供的视频URL，禁止保留任何内置示例链接。5. AI总结：在笔记末尾加入简短的 AI 生成总结，二级标题为 ## AI 总结。"}}

---

{{transcript}}
```

## 2.5 一键剪藏

1. 打开 B 站视频。
2. 点插件图标。
3. 确认笔记名称和保存位置。
4. 点击保存。

约 3 秒后，Obsidian 中会生成：

- 带时间戳跳转的章节结构。
- AI 生成的教程笔记。
- 完整字幕原文。

## 三、进阶技巧

### 3.1 模板触发器实现自动化

配置好 B 站模板后，每次打开 B 站视频页面，Web Clipper 会自动识别并显示对应模板，无需每次手动选择。

### 3.2 过滤器修复链接

B 站分享链接通常带一堆参数，可以用过滤器清理：

```
{{meta:property:og:url}}
```

这个变量直接输出干净的视频链接，例如 `https://www.bilibili.com/video/BVxxxxx`。

### 3.3 多工具协作工作流

```
有字幕视频：Web Clipper CN → AI 总结 → 100-Learning
    ↓
学习完成后移动到 200-sources
    ↓
基于 wiki 知识体系消化整理
```

## 四、常见问题

### Web Clipper CN 抓不到字幕怎么办？

检查视频是否有字幕。有些视频 up 主没有开启字幕功能；无字幕视频只能用 BiliNote。

### AI 总结太笼统怎么办？

调整解释器的 prompt，增加「必须包含具体步骤」「列出每个关键结论」等要求。
