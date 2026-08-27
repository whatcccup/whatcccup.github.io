---
title: "用 iPhone 快捷指令语音录入 Obsidian：三分支写入灵感、TODO 与日记"
description: "用 Shortcuts、Daily Notes 与 Advanced URI，把语音内容写入当天笔记的灵感、TODO 或日记区块。"
tags:
  - Obsidian
  - 快捷指令
  - 移动效率
---

<span class="course-kicker">OBSIDIAN · SHORTCUTS</span>

# 用 iPhone 快捷指令语音录入 Obsidian：三分支写入灵感、TODO 与日记

<p class="course-lead">用 Shortcuts、Daily Notes 与 Advanced URI，把语音内容写入当天笔记的灵感、TODO 或日记区块。</p>

<div class="course-meta"><span>教程</span><span>更新：2026-08-25</span><span>B 站视频</span></div>

<div class="video-embed">
  <iframe src="https://player.bilibili.com/player.html?bvid=BV13nhG6KEpA&page=1&high_quality=1&danmaku=0&autoplay=0" title="B 站课程视频" loading="lazy" allowfullscreen></iframe>
</div>

<p class="video-link"><a href="https://www.bilibili.com/video/BV13nhG6KEpA/" target="_blank" rel="noopener">在 B 站打开 →</a></p>


> 演示所用快捷指令已经整理完成：[添加到 iPhone 快捷指令](https://www.icloud.com/shortcuts/6ba312c9def04548ba609f01a32cdf3b)。添加后，请先替换 Vault 名称并检查目标 block ID。

## 1. 先理解 URI、Obsidian 原生 URI 与 Advanced URI

### 1.1 URI 是什么

URI 是“统一资源标识符”。网页地址通常以 `https://` 开头；而 App 也可以注册自己的 URI 协议，用一段链接接收命令和参数。

Obsidian 注册的协议是 `obsidian://`。例如：

```
obsidian://open?vault=仓库名&file=笔记路径
```

点击后，iPhone 会把这段链接交给 Obsidian。`open` 是动作，`vault` 和 `file` 是动作所需的参数。

> **说明 参数名是 `vault`，不是 `vote`**
> `vault` 指 Obsidian 仓库。教程中的通用占位符统一写成 `vault=仓库名`；请替换为自己的仓库名称。

### 1.2 原生 URI 能做什么

Obsidian 原生 URI 已经可以打开仓库、打开指定笔记、创建笔记，以及打开或创建当天日记。它还可以定位到标题或块，例如：

```
obsidian://open?vault=仓库名&file=笔记路径%23%5E目标块ID
```

这足以解决“打开哪篇笔记、看到哪个位置”的问题。

### 1.3 原生 URI 的缺口

本课的目标不只是打开笔记，而是一次完成：

1. 找到当天日记或某篇指定笔记；
2. 定位到某个 block ID；
3. 把刚刚确认的文字追加到这个位置。

原生 URI 的日记写入可以把内容追加到文件，却没有一个稳定的单一步骤，把“日记 + 指定 block + 写入内容”组合在一起。只用原生 URI，通常会变成“先跳转到块，再手动粘贴”。

**Advanced URI** 是 Obsidian 的社区插件。它提供了按标题、行号或 block ID 定位并追加内容的能力，所以快捷指令可以直接完成写入，不需要用户再在编辑器里找位置。

> **提示 本课的边界**
> Advanced URI 解决的是快速写入，不是加密或任务管理。待办仍然是普通 Markdown 任务，之后可在 Obsidian 中勾选完成。

---

## 2. 课前准备

### 2.1 开启 Daily Notes：先让 Obsidian 知道“今天”是哪篇笔记

在 Obsidian 设置中启用“日记”核心插件，并确认它可以打开或创建当天日记。需要检查三项配置：

1. 日记文件名格式；
2. 日记保存文件夹；
3. 新建日记使用的模板。

`daily=true` 的含义不是让快捷指令自己计算日期，而是让 Obsidian 按这三项既有设置找到“今天”的日记。只有 Daily Notes 正常工作后，才适合使用本课的 `daily=true` 链接。

> **说明 原生 URI 不需要额外开启**
> `obsidian://` 是 Obsidian 自带的 URI 协议；运行过 Obsidian 后，iPhone 就能将这类链接交给它处理。Advanced URI 则是额外安装并启用的社区插件。

### 2.2 先区分原生 URI 与 Advanced URI

如果你只需要将内容追加到当天日记**末尾**，没有指定 block 的需求，优先使用原生 URI：

```
obsidian://daily?vault=仓库名&content=URL编码后的文本&append
```

它的特点是：

- 使用 Obsidian 内置的 `daily` 动作；
- 只依赖 Daily Notes，不需要安装 Advanced URI；
- 内容会追加到当天日记的末尾；
- 适合简单的“快速补一句话”。

当你需要把内容写到某个固定区块，才改用 Advanced URI：

```
obsidian://adv-uri?vault=仓库名&daily=true&block=目标块ID&data=URL编码后的文本&mode=append
```

两者的变化很明确：原生 URI 使用 `content` 和 `append`，Advanced URI 使用 `data`、`block` 和 `mode=append`。后者多出的 `block`，就是将“日记末尾追加”升级为“写到指定位置”的关键。

### 2.3 准备日记模板与目标块

若你也采用本库的模板，可以参考：Daily Note 模板。

在你的日记模板中为三个写入位置设置稳定的 block ID：

```
## ✅ 今日任务 ^to-do

## 📷 今日日记 ^dairy

## 🔄 今日灵感 ^inspiration
```

三个 ID 的用途如下：

| 记录类型 | block ID | 建议写入格式 |
| --- | --- | --- |
| 记灵感 | `inspiration` | `- 💡 内容` |
| 记 TODO | `to-do` | `- [ ] 内容` |
| 记日记 | `dairy` | 普通正文 |

填写 URI 时，`block=` 后只写 ID 本身，例如 `block=to-do`，不要带 `^`。

> **注意 模板与当天笔记都要检查**
> 模板改动不会自动写入已经创建的日记。若当天日记早于模板改动创建，请手动补上对应的 block ID，否则 Advanced URI 无法准确落位。

### 2.4 安装 Advanced URI

在 iPhone 和桌面端 Obsidian 的社区插件中安装并启用 **Advanced URI**。本课依赖其向 block 追加内容的能力，建议使用 2.0.0 或更高版本。

先用一个只打开、不写入的通用链接测试目标块：

```
obsidian://adv-uri?vault=仓库名&daily=true&block=to-do
```

如果无法打开，请依次检查：

1. `仓库名` 是否替换为 Obsidian 仓库切换器中显示的真实名称；
2. Advanced URI 是否已启用；
3. 日记插件是否已启用；
4. 当天日记是否含有 `^to-do`。

### 2.5 截图清单

录制或发布图文课程时，建议准备以下画面：

1. iPhone 上 Daily Notes 已启用、当天日记可创建的画面；
2. 原生 URI 将文字追加到日记末尾的画面；
3. iPhone 上 Advanced URI 已启用的画面；
4. 日记模板中三个标题和 block ID 的画面；
5. 快捷指令全景图；
6. “编辑确认文字”输入框与“记灵感 / 记 TODO / 记日记”选择菜单；
7. 三种内容分别写入当日日记对应区块的前后对比。

---

## 3. 快捷指令的三分支结构

在 iPhone 的“快捷指令”App 中新建一个快捷指令，建议命名为：**语音记录日记**。

以下步骤中的“魔法变量”均指从上一步动作点选插入的蓝色变量，而不是手动输入变量名称。

### 3.1 听写并允许用户修正

依次添加两个动作：

1. **听写文本**
   - 语言：中文。
2. **询问输入**
   - 提示：`确认或编辑本次内容`
   - 输入类型：文本。
   - 默认答案：选择上一步的“听写文本”。
   - 若系统显示“允许多行输入”，建议开启。

听写容易出现同音字、专有名词或标点问题。用户在第二步直接修正后，后续流程只使用修正后的版本。

### 3.2 让用户选择三种记录类型

添加以下两个动作：

3. **列表**
   - 第一项：`记灵感`
   - 第二项：`记 TODO`
   - 第三项：`记日记`
4. **从列表中选择**
   - 提示：`这条内容要记录到哪里？`

这一步既是分类，也是第二次确认：用户先确认文字，再决定这是一项行动、一条灵感，还是一段日记正文。

### 3.3 外层 if：先处理灵感

添加一个 **如果** 动作：

```
如果「所选项目」是“记灵感”
```

在“如果”分支内依次添加：

5. **文本**

   ```
   - 💡「询问输入的结果」
   ```
6. **设置变量**

   - 变量名：`本次内容`
   - 值：上一步“文本”。
7. **文本**

   ```
   inspiration
   ```
8. **设置变量**

   - 变量名：`目标块`
   - 值：上一步“文本”。

### 3.4 外层 otherwise 中嵌套 if：TODO 或日记

在外层 **否则** 分支内，再添加一个 **如果** 动作：

```
如果「所选项目」是“记 TODO”
```

在这个内层“如果”分支内添加：

9. **文本**

   ```
   - [ ]「询问输入的结果」
   ```
10. **设置变量**

    - 变量名：`本次内容`
    - 值：上一步“文本”。
11. **文本**

    ```
    to-do
    ```
12. **设置变量**

    - 变量名：`目标块`
    - 值：上一步“文本”。

在这个内层 **否则** 分支内，写入“记日记”的兜底逻辑：

13. **文本**

    ```
    「询问输入的结果」
    ```
14. **设置变量**

    - 变量名：`本次内容`
    - 值：上一步“文本”。
15. **文本**

    ```
    dairy
    ```
16. **设置变量**

    - 变量名：`目标块`
    - 值：上一步“文本”。

然后依次关闭内层 **结束如果** 和外层 **结束如果**。

完整逻辑应当如下：

```
如果 所选项目 是 记灵感
    本次内容 = - 💡已确认文字
    目标块 = inspiration
否则
    如果 所选项目 是 记 TODO
        本次内容 = - [ ]已确认文字
        目标块 = to-do
    否则
        本次内容 = 已确认文字
        目标块 = dairy
    结束如果
结束如果
```

这里最后的 `otherwise` 正是“记日记”分支。因为列表只给出三项，既不是“记灵感”、也不是“记 TODO”的选择，只会是“记日记”。

> **提示 TODO 为什么必须是 `- [ ]`**
> 这是 Obsidian 的标准未完成任务格式。它会被日记中的 Dataview 查询和 待办汇总 自动识别；之后在日记或汇总页任意一处勾选，都会更新同一项 Markdown 任务。

---

## 4. 通用空白版：编码并生成写入链接

本节没有任何个人仓库名、路径或日记名称。请将占位符替换为自己的实际值。

### 4.1 只编码内容

在两个 **结束如果** 后添加：

17. **URL 编码**
    - 输入：变量 `本次内容`。

不要对整条 Obsidian 链接执行 URL 编码。URI 中的 `?`、`&`、= 必须保留为参数分隔符；只有内容里的空格、换行、`&`、`#` 等字符需要编码。

### 4.2 通用写入链接

18. **文本**

```
obsidian://adv-uri?vault=仓库名&daily=true&block=目标块ID&data=URL编码后的文本&mode=append
```

在快捷指令里，将占位符替换为魔法变量或真实配置：

| 占位符 | 应替换为 |
| --- | --- |
| `仓库名` | 你的 Obsidian Vault 名称；若包含空格，需对空格进行 URL 编码。 |
| `目标块ID` | 变量 `目标块`。 |
| `URL编码后的文本` | 第 17 步“URL 编码”的输出。 |

实际在“文本”动作中，它会呈现为：

```
obsidian://adv-uri?vault=仓库名&daily=true&block=「目标块」&data=「URL 编码后的文本」&mode=append
```

`目标块` 与 `URL 编码后的文本` 都是蓝色魔法变量。

> **注意 两个常见错误**
>
> 1. 内容必须放在 `data=` 与 `&mode=append` 之间。
> 2. `data=` 与 `clipboard=true` 二选一。本教程使用 `data=`，不要再添加 `clipboard=true`。

### 4.3 执行写入

19. **打开 URL**
    - 输入：上一步完整的文本。

当 `daily=true` 存在时，Advanced URI 会依据 Obsidian 的日记设置打开或创建当天日记，然后将内容追加到目标块之后。

---

## 5. 个人示例：仓库名为 `man`，使用 Daily Notes

这一节只用于演示参数如何替换，不是教程正文的默认配置。

假设：

- 你的仓库名是 `man`；
- 今天的日记在 Obsidian 中显示为“什么不拉不拉不拉不拉不拉”；
- 你已设置 Daily Notes，因此不需要在 URI 中写出这个日记的文件名或路径；
- 你选择“记日记”，目标块为 `dairy`。

那么“文本”动作的 URL 形态为：

```
obsidian://adv-uri?vault=man&daily=true&block=dairy&data=「URL编码后的文本」&mode=append
```

这里的 `daily=true` 是关键：它让 Obsidian 按自己的 Daily Notes 配置决定今天是哪篇笔记。日记的可见标题即使是“什么不拉不拉不拉不拉不拉”，也不必作为 URI 参数传入。

若选择“记 TODO”，同一条链接只需把目标块换为 `to-do`；若选择“记灵感”，换为 `inspiration`。快捷指令已经通过变量完成这一步，因此用户不需要手动修改链接。

---

## 6. 不使用 Daily Notes：按日期与路径定位指定笔记

如果你没有启用 Daily Notes，或者你希望快捷指令写入某一篇按日期命名的指定笔记，请把 `daily=true` 改为 `filepath=...`。

### 6.1 `filepath` 的通用结构

`filepath` 必须是**相对于仓库根目录**的路径，不是 Mac 或 iPhone 的绝对文件路径。路径中的 `/` 需要写成 `%2F`。

```
obsidian://adv-uri?vault=仓库名&filepath=文件夹%2F年份%2F月份%2F日期文件名&block=目标块ID&data=URL编码后的文本&mode=append
```

例如，假设你的笔记按 `YYYY/MM/YYYY-MM-DD.md` 保存到 `20-Journal/Daily`，2026 年 8 月 21 日这篇笔记的写入链接可以是：

```
obsidian://adv-uri?vault=man&filepath=20-Journal%2FDaily%2F2026%2F08%2F2026-08-21&block=dairy&data=「URL编码后的文本」&mode=append
```

如果只想打开指定仓库、指定路径、指定块，而不写入内容，去掉 `data` 与 `mode`：

```
obsidian://adv-uri?vault=man&filepath=20-Journal%2FDaily%2F2026%2F08%2F2026-08-21&block=dairy
```

### 6.2 在 Shortcuts 中生成日期路径

当文件名含日期时，格式必须和你真实的文件名完全一致。可使用以下动作：

1. **当前日期**。
2. **格式化日期**：格式 `yyyy-MM-dd`，得到“日期文件名”。
3. **格式化日期**：格式 `yyyy`，得到“年份目录”。
4. **格式化日期**：格式 `MM`，得到“月份目录”。
5. **文本**：拼接 `filepath` 与上述三个魔法变量。

例如，“文本”动作可以写成：

```
obsidian://adv-uri?vault=仓库名&filepath=日记文件夹%2F「年份目录」%2F「月份目录」%2F「日期文件名」&block=「目标块」&data=「URL编码后的文本」&mode=append
```

常见日期格式对应关系：

| 实际文件名示例 | “格式化日期”格式 |
| --- | --- |
| `2026-08-21.md` | `yyyy-MM-dd` |
| `20260821.md` | `yyyyMMdd` |
| `2026年08月21日.md` | `yyyy年MM月dd日` |
| `08-21-2026.md` | `MM-dd-yyyy` |

> **注意 年、月、日应使用大写占位符**
> `MM` 才会固定输出两位月份，例如 `08`；`mm` 在许多日期格式中表示分钟。若你的路径按月份分目录，月份格式错误会导致找不到文件。

### 6.3 选择哪一种方案

| 你的情况 | 链接识别方式 |
| --- | --- |
| 已启用 Daily Notes，写入今天日记 | `daily=true` |
| 没有 Daily Notes，但文件名可由日期生成 | `filepath=...` + 格式化日期 |
| 要写入一篇固定笔记 | `filepath=固定相对路径` |
| 只想打开指定块，不写入 | 保留 `vault`、`filepath`、`block`，删除 `data`、`mode` |

---

## 7. 按顺序测试三条路径

先分别测试三条路径，避免一次改动多个变量后难以定位问题。

### 测试 A：记 TODO

1. 运行快捷指令并说：`给客户确认会议时间`。
2. 在编辑框中确认或修改文本。
3. 选择“记 TODO”。
4. 确认 `^to-do` 下出现：

   ```
   - [ ] 给客户确认会议时间
   ```
5. 在日记或 待办汇总 中勾选它，确认状态同步。

### 测试 B：记灵感

1. 运行快捷指令并说：`用案例对比解释合同条款风险`。
2. 在编辑框中确认或修改文本。
3. 选择“记灵感”。
4. 确认 `^inspiration` 下出现：

   ```
   - 💡 用案例对比解释合同条款风险
   ```

### 测试 C：记日记

1. 运行快捷指令并说：`今天把快捷指令的三种记录方式整理清楚了`。
2. 在编辑框中确认或修改文本。
3. 选择“记日记”。
4. 确认 `^dairy` 下出现该段普通正文，而非 TODO 复选框或灵感项目符号。

---

## 8. 常见问题

### 内容被写到文件末尾，而不是目标位置

检查 URL 中是否包含正确的 `block` 与 `mode`，例如：

```
block=to-do&data=URL编码后的文本&mode=append
```

同时确认当前日记中存在该 block ID。新模板不会自动倒灌到旧日记。

### 内容出现 `%20`、`%26` 等字符

通常是编码时机错误。要把“URL 编码”动作的输出放到 `data=` 后；不要编码整条 URI，也不要把未编码原文直接拼入 URI。

### TODO 没有被待办汇总识别

TODO 分支的内容必须以 `- [ ]` 开头，并位于“今日任务”区块。`- TODO`、`[]` 或普通项目符号都不会被识别为可勾选任务。

### 打开了错误的仓库或笔记

检查 `vault=仓库名` 是否已替换为真实名称。按路径定位时，再检查 `filepath` 是否从仓库根目录开始、分隔符是否写为 `%2F`、日期格式是否与文件名一致。

### 多设备上暂时看不到新内容

URI 的写入发生在执行快捷指令的设备上。等待 Obsidian Sync 或 iCloud 同步完成后，再在另一台设备查看；同步未完成时不要同时编辑同一条任务。

---

## 9. 完成后的使用习惯

- 是需要执行的下一步，就选“记 TODO”。
- 是选题、方法或一句提醒，就选“记灵感”。
- 是当天发生的事或感受，就选“记日记”。
- 听写有误，先在编辑确认框中修正，再执行写入。
- TODO 完成后，在日记或待办汇总中任意一处勾选即可。

这条快捷指令不试图替代复杂项目管理系统。它专门解决“刚想到、还不想打开笔记找位置”时的快速归档问题。

---

## 参考资料

- [Obsidian URI 中文帮助](https://obsidian.md/zh/help/uri)
- [Advanced URI：导航到 heading 或 block](https://publish.obsidian.md/advanced-uri-doc/Actions/Navigation)
- [Advanced URI：写入与追加内容](https://publish.obsidian.md/advanced-uri-doc/Actions/Writing)
- [Advanced URI 更新记录：支持向 block 追加或前插](https://github.com/Vinzent03/obsidian-advanced-uri/blob/master/CHANGELOG.md)
