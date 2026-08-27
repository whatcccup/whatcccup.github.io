---
title: "Claudian 完整安装与 Skill 配置"
description: "把 Claude Code 或 Codex 接进 Obsidian，再用 TheSchema Skill 约束知识库整理、查询和检查流程。"
tags:
  - Obsidian
  - AI Agent
  - Skills
---

<span class="course-kicker">OBSIDIAN · LOCAL AGENT</span>

# Claudian 完整安装与 Skill 配置

<p class="course-lead">把 Claude Code 或 Codex 接进 Obsidian，再用 TheSchema Skill 约束知识库整理、查询和检查流程。</p>

<div class="course-meta"><span>教程</span><span>更新：2026-08-18</span><span>B 站视频</span></div>

<div class="video-embed">
  <iframe src="https://player.bilibili.com/player.html?bvid=BV1gbbi6cEeQ&page=1&high_quality=1&danmaku=0&autoplay=0" title="B 站课程视频" loading="lazy" allowfullscreen></iframe>
</div>

<p class="video-link"><a href="https://www.bilibili.com/video/BV1gbbi6cEeQ/" target="_blank" rel="noopener">在 B 站打开 →</a></p>



> **INFO · 2026-08-18 更新**
>
> Claudian 已上架 Obsidian 官方社区插件市场，普通用户不再需要从 GitHub Releases 手动下载 `main.js`、`manifest.json` 和 `styles.css`。本教程已同步更新安装方式，并补充当前 Provider、Skill、Session 与隐私边界。

本教程要完成以下闭环：

1. 理解 Claudian、Obsidian、CLI、模型服务之间的关系。
2. 安装并验证 Claude Code CLI；按需安装 Codex CLI。
3. 使用 CC Switch 管理 Claude Code 的不同模型 Provider。
4. 安装 Claudian，并让它在 Obsidian 中成功读取和创建笔记。
5. 看懂 `.claudian`、`.claude`、`~/.claude/projects` 等存储位置。

---

## 1. 先理解最终会安装什么

装完 Claudian，Obsidian 里的笔记就能直接交给本地 Agent 处理。

但多数插件只是多了一个聊天框。

Claudian 不太一样。

它把 Claude Code 或 Codex 这样的本地 Agent，直接接进你的知识库。

本教程会从零开始，完成安装与验证。

最后再加一套 TheSchema Skill。

让它不只会聊天，还知道该怎么读、怎么整理、怎么检查你的知识库。

---

### 1.1 四层结构

先把关系讲清楚。

Obsidian 是你的桌面界面。

Claudian 是桥。

Claude Code 或 Codex CLI 是真正干活的 Agent。

模型 API 则是后面的动力来源。

所以 Claudian 不是一个独立模型，也不是另一个 ChatGPT。

它负责把 Obsidian 当前笔记、Vault 文件和你的问题，交给本地 CLI 处理。

---

### 1.2 CLI 与本地桌面端的区别

CLI 是 Command Line Interface，也就是命令行界面。

桌面端通常是 GUI。

你靠鼠标、菜单和按钮操作。

CLI 靠一行行文本命令操作。

对刚接触终端的人，CLI 看着像黑盒。

但对 AI 来说，它反而更直接。

AI 不用找按钮，也不用猜界面坐标。

它可以读帮助文档，组合命令，再根据结果继续行动。

---

### 1.3 Claudian、Claude Code 与 Claude Desktop

这也是 Claudian 和 Claude Desktop 的关键区别。

Claude Desktop 更像一个完整聊天应用。

它有自己的界面和会话体验。

Claude Code 则是运行在本机目录里的 Agent。

它能读取文件、修改文件、执行命令，再检查结果。

Claudian 做的事，是把这种 CLI 能力嵌回 Obsidian。

你仍然在熟悉的笔记界面工作。

真正的文件操作交给 CLI。

---

### 1.4 为什么这套组合适合 Obsidian

为什么这套组合适合 Obsidian？

因为 Obsidian 的笔记就是本地 Markdown 文件。

不是锁在某个网页数据库里的私有内容。

哪怕将来你换掉 Obsidian，文件还在。

哪怕你换掉 Claude Code，另一套 Agent 也能继续读取。

这就是 File over App。

工具可以换，文件和知识积累归你。

---

## 2. 开始前的准备

安装前先准备四样东西。

第一，一个正在使用的 Obsidian Vault。

Claudian 只支持 Obsidian 桌面版，官方当前要求 Obsidian 1.7.2 或更高版本。

第二，Claude Code CLI 或 Codex CLI，至少选一个。

第三，对应的官方账号、订阅，或者模型 API Key。

第四，能打开终端并执行几条命令。

在这四项基础条件之外，我非常推荐你安装 CC Switch。它不是 Claudian 的必需组件，但能用图形界面集中管理 Claude Code、Codex 的 Provider、环境变量、MCP 和 Skills，后续切换模型时会省去大量手改配置文件的工作。

本文以 macOS 为主。

所有 API Key 都不要出现在截图、公开笔记或共享文件中。

---

### 2.1 Claudian 的优势

先把优点和代价摆在一起。

Claudian 本身免费、开源、本地运行。

这里的“本地运行”是指插件和 CLI 在你的电脑上工作，不代表内容永远不离开本机。你的输入、主动附加的文件和工具调用结果，会发送给当前配置的模型 Provider；敏感笔记是否适合提交给 API，仍需由你判断。

它可以接 Claude Code，也可以接 Codex。

当前版本还支持 Grok、OpenCode 和 Pi 等 Provider；本课程仍以功能更完整的 Claude，以及可选的 Codex 为主。

你已有账号或 API Key 时，不必再为插件单独买一份 AI 订阅。

它还能借助兼容接口切换不同模型。

Claudian 除了侧边栏对话，还支持行内编辑、Plan Mode、多标签会话、历史恢复、分叉与压缩；输入 `@` 可以引用 Vault 文件等上下文，输入 `/` 或 `$` 可以发现命令与 Skills。具体入口会随 Provider 不同而略有区别。

---

### 2.2 使用前必须知道的限制

Claudian 已进入 Obsidian 官方社区插件市场，但它仍是第三方社区插件，不是 Obsidian 官方团队开发的内置功能。

普通用户直接从社区插件市场安装即可；GitHub Release 手动安装只保留为市场不可用时的备用方案。

它依赖本机 CLI 环境，第一次配置有门槛。

开源项目的功能和维护节奏，也取决于开发者。

Claudian 产生的过程文件可能持续增长。

这些目录要不要同步，不能装完就不管。

---

## 3. 安装 Claude Code CLI

如果你主要用 Claude、MiniMax，或者兼容 Anthropic 协议的模型，我更推荐 Claude Code 这条路线。官方安装教程：[在这里](https://code.claude.com/docs/zh-CN/overview)。

现在官方更推荐原生安装。

macOS 可以用 Homebrew Cask：

```
brew install --cask claude-code
claude --version
```

`claude-code` 对应较稳健的 stable 通道。Homebrew 安装不会自动升级，可以定期执行：

```
brew upgrade claude-code
```

如果需要第一时间使用最新版本，可选择 `claude-code@latest`，但教程默认使用 stable 通道。

也可以使用官方安装脚本。

装好后，在普通终端里先运行一次 `claude`。

确认它能正常启动，再碰 Claudian。

不要把 CLI 安装和插件安装混在一起排错。

部分旧版教程会让用户手动在 `~/.claude.json` 写入 `hasCompletedOnboarding`。

现在不要把它当成默认安装步骤。

先走当前版本的官方登录和初始化。

只有兼容服务明确要求，或者你确认卡在旧版 onboarding 状态时，再单独处理。

---

## 4. 可选：安装 Codex CLI

如果你使用 OpenAI 模型，也可以装 Codex CLI。官方安装教程：[在这里](https://learn.chatgpt.com/docs/codex/cli#getting-started)，提供了多种安装方式，可任选。

macOS 可以使用 Homebrew Cask：

```
brew install --cask codex
```

也可以使用 npm：

```
npm install -g @openai/codex
```

第一次启动时按提示登录。

如果通过 CC Switch 使用 ChatGPT / Codex OAuth，先在 CC Switch 的认证页面完成官方登录。若还要给 Codex 接入只支持 OpenAI Chat Completions 的第三方模型，通常需要开启 CC Switch Local Routing；这可能与本机已有代理或路由软件冲突。初学者只用官方 Codex 登录会更简单。

然后运行：

```
codex --version
which codex
```

前一条确认程序可用。

后一条告诉你可执行文件在哪里。

---

### 4.1 CLI 路径与 GUI PATH 问题

这里有个常见误区。

很多人一上来就手填 CLI 路径。

Claudian 官方现在建议，先把路径留空，让插件自动发现。

只有看到 `spawn claude ENOENT`，或者 `Claude CLI not found`，再手动处理。

原生安装通常直接指向 `claude` 可执行文件。

如果是旧的 npm 安装，还可能遇到 Node 和 CLI 不在同一个目录。

这时先比较：

```
dirname "$(which claude)"
dirname "$(which node)"
```

路径不一致时，优先改用原生安装。

或者把 Node 所在目录加入 Claudian 的 PATH 环境变量。

---

## 5. 推荐方案：使用 CC Switch 管理模型配置

如果你需要在官方 Claude、MiniMax 和其他兼容服务之间切换，我推荐 CC Switch。

CC Switch 唯一官方网站：[ccswitch.io](https://ccswitch.io)。源码与 Release 下载位于 [farion1231/cc-switch](https://github.com/farion1231/cc-switch)。请只从这两个官方渠道访问或下载，不要使用名称相近的第三方网站。

它不是模型，也不是 Claudian 的必需组件。

它是一个本地配置管理器。

你可以把多个 Provider 保存成不同方案，再切换当前生效的配置。

这样比反复手改 `settings.json` 更直观，也更不容易把 JSON 写坏。

---

### 5.1 安装 CC Switch

macOS 可以直接安装：

```
brew install --cask cc-switch
```

安装完成后先不要急着添加 Provider。第一次打开 CC Switch，应先完成通用设置。

---

### 5.2 先完成 CC Switch 设置页

进入 CC Switch 后，点击左上角的设置入口。

先设置软件语言和外观主题。这两项只影响界面，可按个人习惯选择。

然后找到“主页显示”或类似选项，只保留本机实际使用的应用。例如你安装了 Claude Code、Claude Desktop 和 Codex，就把这三项显示在主页；没有安装的工具可以隐藏，减少干扰。

接着配置 Skills。推荐这样设置：

1. 将 **Storage Location** 设置为共享目录 `~/.agents/skills/`。
2. 将 **Skill Sync Method** 设置为软链接，也就是 Symlink。

这样所有 Skill 的实体文件集中保存在一个目录中。Claude Code、Codex 等工具需要使用某个 Skill 时，由 CC Switch 在对应应用目录创建软链接，不必复制多份文件。

如果设置页提供“Codex 应用增强”，并且你同时使用 Codex 官方登录和第三方 Provider，建议开启相关选项，以便不同配置之间继续识别会话记录。该功能名称可能随版本调整，应以当前 CC Switch 界面说明为准。

窗口行为只影响 CC Switch 如何打开、关闭或驻留后台，可按个人习惯设置。

完成这些设置后，再回到 CC Switch 主页，按应用页面逐一添加配置。

---

### 5.3 在 Claude Code 页面添加 Provider

回到主页，先进入 **Claude Code** 页面，然后点击右上角的加号。

#### 使用 Claude 官方账号

如果你有可用于 Claude Code 的官方订阅账号，可以选择 `Claude Official`。

官方账号通常不需要在 CC Switch 的 Provider 表单中填写 API Key。添加并启用该配置后，进入一个准备使用 Claude Code 的项目目录，运行：

```
claude
```

如果终端提示尚未登录，输入：

```
/login
```

然后按浏览器页面提示完成官方认证。认证完成后回到终端继续使用。

#### 使用第三方兼容模型

如果使用 Kimi、MiniMax、DeepSeek 或其他兼容 Anthropic 协议的服务，在 Claude Code 页面点击加号后，选择对应的 Provider 预设。

依次完成以下配置：

1. 填写服务商提供的 Base URL。
2. 粘贴在服务商控制台创建的 API Key。
3. 点击“管理与测试”或当前版本中的连接测试入口，先确认接口能够访问。
4. 在“模型映射”区域点击“获取模型列表”，读取该账号当前可以使用的真实模型 ID。
5. 分别为 Haiku、Sonnet、Opus 和兜底模型选择对应的真实模型。
6. 只有服务商明确支持扩展上下文时，才开启对应的长上下文选项。
7. 保存并添加 Provider，再执行一次连通性测试。

Haiku 通常对应速度更快、成本更低的模型；Sonnet 适合作为日常主力；Opus 对应能力更强的模型。你也可以把多个档位映射到同一个模型，但应逐项确认，避免某个档位仍指向旧模型。

API Key 往往只在创建时完整显示一次。保存时应使用密码管理器等安全工具，不要把 Key 写进课程笔记、截图或公开仓库。

启用新 Provider 前，先退出正在运行的 Claude Code 会话。然后在 CC Switch 中启用新配置，再重新运行 `claude`。这个顺序可以避免旧进程继续使用切换前的环境变量。

进入新会话后使用：

```
/status
```

核对当前 Provider 和模型。界面可能仍显示 Haiku、Sonnet 或 Opus 这些 Claude 档位名称，实际调用的模型由 CC Switch 中的映射决定。

---

### 5.4 在 Codex 页面完成官方登录

Codex 官方登录与 Claude Code 的流程不同。

如果使用 ChatGPT 账号登录 Codex，先打开 CC Switch 的“设置 → 认证”页面，找到 `ChatGPT（Codex OAuth）`，点击“使用 ChatGPT 登录”。

浏览器会打开 OpenAI 授权页面。按页面提示完成认证；如果页面生成授权码，就将该授权码复制回 CC Switch。不要公开认证完成后产生的 Access Token 或其他凭据。

认证成功后回到 CC Switch 的 **Codex** 页面，确认 `OpenAI Official` 配置已经出现并处于可用状态。然后再启动 Codex CLI 验证登录。

如果要给 Codex 添加只支持 OpenAI Chat Completions 的第三方模型，通常还需要开启 Local Routing 并配置模型映射。本地路由可能与代理或其他网络路由软件冲突，因此初学者优先使用 Codex 官方登录；第三方兼容模型更推荐通过 Claude Code 路线接入。

---

### 5.5 CC Switch 的本地存储位置

CC Switch 的好处是配置集中。

但你也要知道它把东西存在哪里。

它的数据库在 `~/.cc-switch/cc-switch.db`。

本机设置在 `~/.cc-switch/settings.json`。

自动备份在 `~/.cc-switch/backups/`。

Skill 默认放在 `~/.cc-switch/skills/`，再通过链接共享给对应工具。

从 CC Switch v3.13.0 开始，Skill 的单一来源目录也可以切换为 `~/.agents/skills/`，更适合 Claude Code、Codex 等多个工具共享。这里要区分两个设置：

- **Storage Location** 决定 Skill 的源文件存在哪里。
- **Skill Sync Method** 决定向各应用目录分发时使用软链接还是复制。

如果你希望只维护一份 Skill，建议选择共享来源目录并使用软链接；切换前先确认现有目录是实体还是软链接，避免制造重复副本。

这里可能包含 Provider 信息和本地配置。

不要把整个 `.cc-switch` 目录随便上传到公开仓库。

---

### 5.6 不使用 CC Switch 时的手动配置

如果你不用 CC Switch，也可以手动配置 Claude Code。

用户级配置通常放在 `~/.claude/settings.json`。

一个兼容 Anthropic 协议的示意配置可以写成：

```
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://provider.example.com/anthropic",
    "ANTHROPIC_AUTH_TOKEN": "YOUR_API_KEY",
    "API_TIMEOUT_MS": "3000000",
    "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1",
    "ANTHROPIC_MODEL": "YOUR_MODEL_NAME",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "YOUR_MODEL_NAME",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "YOUR_MODEL_NAME",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "YOUR_MODEL_NAME"
  }
}
```

字段要以服务商当前文档为准。

不要直接复制未经核验的真实地址和旧模型名。

这里的超时和非必要流量开关属于可选兼容项。

服务商没有要求时，不必照抄。

配置完先在单独的测试目录验证：

```
mkdir -p ~/claude-workspace
cd ~/claude-workspace
claude
```

进入后用 `/status` 核对当前 Provider 和模型。

---

## 6. 安装 Claudian

CLI 验证通过后，再安装 Claudian。

打开 Obsidian 设置，进入「第三方插件」或「社区插件」。

点击「浏览」，搜索 `Claudian`。

确认插件名称为 **Claudian**，来源对应官方开源仓库 `YishenTu/claudian`，然后点击安装并启用。

社区市场里可能出现名称接近的扩展版本，例如针对其他 CLI 增加支持的分支。请根据实际 Provider 选择，不要把相似名称误认为同一个插件。本课程使用的是 `Claudian`。

> **NOTE · 备用安装方式**
>
> 只有社区插件市场无法访问，或需要测试特定 Release 时，才从 [Claudian 官方 Releases](https://github.com/YishenTu/claudian/releases) 下载 `main.js`、`manifest.json` 和 `styles.css`，放入 `<Vault>/.obsidian/plugins/claudian/`。这已经不是普通用户的首选安装方式。

---

### 6.1 在 Obsidian 中启用插件

回到 Obsidian。

打开设置，进入第三方插件。

如果安全模式还开着，先允许第三方插件。

找到 Claudian 并启用。

如果社区市场搜索不到，先更新 Obsidian 桌面版并重新打开社区插件页面；只有采用备用手动安装时，才需要检查 `manifest.json` 是否位于 `claudian` 文件夹第一层。

---

## 7. 配置 Claudian

接着打开 Claudian 设置。

设置界面的第一页是通用设置。

这一页保持默认即可，本教程不修改。

接下来根据你实际使用的 Provider，进入 Claude 或 Codex 页面。

---

### 7.1 配置 Claude 页面

先打开 macOS 终端，输入：

```
which claude
```

终端会返回 Claude Code 的可执行文件路径，例如：

```
/opt/homebrew/bin/claude
```

复制终端返回的完整路径。回到 Obsidian，依次打开「设置 → Claudian → Claude」，把它粘贴到 `Claude CLI path`。

不要只复制所在文件夹，也不要把 `which claude` 这几个字粘进输入框。这里需要的是指向 `claude` 可执行文件的完整路径。

Claudian 支持自动检测，因此也可以先将路径留空。如果自动检测失败，或者你想明确指定某个 Claude Code 安装，就使用 `which claude` 返回的路径手动填写。

接着一定要开启 `Load user Claude settings`，也就是“加载用户 Claude 设置”。

CC Switch 会把当前生效的 Claude Code 配置写入用户级 `~/.claude/settings.json`。开启这个选项后，Claudian 才会加载其中由 CC Switch 管理的 Provider、模型映射和环境变量。

开启后也要留意权限设置：用户级 Claude Code 权限规则会一并加载，应确认它们符合你对当前 Vault 的安全要求。

---

### 7.2 配置 Codex 页面

Codex 的方法相同。先在终端输入：

```
which codex
```

终端可能返回：

```
/opt/homebrew/bin/codex
```

复制完整结果。回到「设置 → Claudian → Codex」，将路径粘贴到 `Codex CLI path`。

同样，不要只填 `/opt/homebrew/bin/` 这样的文件夹路径。输入框里应该以 `codex` 可执行文件结尾。

Claudian 同样支持自动检测 Codex 路径。你可以留空使用自动检测，也可以使用 `which codex` 手动指定路径。

---

### 7.3 只有需要改变 Claude 模型映射时，才配置环境变量

如果你接受 CC Switch 当前展示和映射的 Claude 模型名称，到这里就不需要再添加任何环境变量。保持 Claudian 加载用户 Claude 设置即可，避免出现两套相互冲突的配置。

只有当你不希望使用 CC Switch 当前提供的 Claude 模型名称，想让 Claudian 将 Sonnet、Opus、Haiku 映射到服务商指定的其他模型时，才打开 Claudian 的 Environment 设置，选择 Claude Provider，并粘贴下面这段配置：

```
ANTHROPIC_MODEL=YOUR_MODEL_NAME
ANTHROPIC_DEFAULT_SONNET_MODEL=YOUR_SONNET_MODEL_NAME
ANTHROPIC_DEFAULT_OPUS_MODEL=YOUR_OPUS_MODEL_NAME
ANTHROPIC_DEFAULT_HAIKU_MODEL=YOUR_HAIKU_MODEL_NAME
```

把每个占位符替换为服务商文档中真实存在的模型 ID。例如，如果服务商只提供一个模型，也可以把四行都填写成同一个模型 ID。

不要在这里重复填写 Base URL 或 API Key，除非你明确希望 Claudian 覆盖 CC Switch 的 Provider 配置。模型环境变量会优先影响 Claudian 的模型选择；填写错误会导致请求时报“模型不存在”或类似错误。

保存配置后新建 Claudian 会话，再检查模型名称和实际响应。已有 Session 可能继续保留创建时的 Provider 与模型状态。

---

## 8. 完成第一次最小验证

现在做第一次最小测试。

新建一篇不含敏感信息的测试笔记。

打开 Claudian 面板。

让它只做一件事：总结当前笔记的三个要点。

如果能读到当前笔记，说明 Obsidian 到 Claudian 这一段通了。

再让它创建一个临时 Markdown 文件。

如果权限提示出现，先看清目标路径，再允许。

这一步通了，才算 Agent 的文件能力真的接上。

---

## 9. 常见故障排查

### 9.1 模型名不正确或 CLI 找不到

如果对话里显示的模型名不对，先新建会话。

已有会话可能保留旧 Provider 状态。

如果提示 CLI 找不到，先回普通终端运行 `claude --version` 或 `codex --version`。

终端也找不到，就是 CLI 安装问题。

终端能找到，Obsidian 找不到，多半是 GUI 应用拿到的 PATH 不完整。

这时再手填 CLI 路径，或者补 PATH。

---

### 9.2 模型请求失败

如果模型请求失败，按三层排查。

第一层看 CLI 能不能启动。

第二层看 Provider 的 Base URL、Key 和模型名。

第三层看 Claudian 有没有加载正确的用户设置和环境变量。

不要一次改五个地方。

每次只改一层，再做同一个最小测试。

这样才能知道问题到底在哪。

---

## 10. 看懂 Claudian 与 Claude Code 的存储架构

接下来讲文件存储架构。

你的 Vault 是内容资产层。

普通笔记、附件、`300-wiki` 都在这里。

`.obsidian/` 是 Obsidian 的应用配置层。

Claudian 插件代码在 `.obsidian/plugins/claudian/`。

`.claudian/claudian-settings.json` 保存 Claudian 的共享设置和 Provider 配置。

`.claudian/sessions/*.meta.json` 保存跨 Provider 的 Session 元数据。

项目里的 `.claude/` 主要保存 Claude Code 的规则、设置和 Skills 等项目配置。

Claudian 管理的 Claude MCP 配置位于 `.claude/mcp.json`；Claude 的命令、Skills 和 SubAgent 通常分别位于 `.claude/commands/`、`.claude/skills/` 和 `.claude/agents/`。

用户级 Claude Code 配置则在 Vault 外面的 `~/.claude/`。

这几个目录名字接近，但作用不一样。

---

### 10.1 Claudian Session 保存在哪里

Claudian 对话也分两层保存。

Claudian 自己的设置和 Session 元数据，分别放在：

```
<Vault>/.claudian/claudian-settings.json
<Vault>/.claudian/sessions/*.meta.json
```

这里更像会话目录和索引层。

Claude Provider 的完整对话转录，沿用 Claude Code 的用户级目录：

```
~/.claude/projects/<项目路径编码>/<session-id>.jsonl
```

如果使用 Codex Provider，完整 session 则在：

```
~/.codex/sessions/
```

其他 Provider 会沿用各自的原生存储位置，例如 Grok 使用 `~/.grok/sessions/`，Pi 使用项目内或用户目录下的 `.pi/agent/sessions/`。本教程不展开这些 Provider 的配置。

所以，只同步 Vault 里的 `.claudian/`，不等于同步了全部完整对话。

---

### 10.2 生成的 CLAUDE.md 保存在哪里

如果你让 Claudian 里的 Claude 执行 `/init`，或者明确要求它生成 `CLAUDE.md`，位置取决于当时的工作目录和目标路径。

Claudian 把 Vault 当作 Agent 的工作目录。

因此在 Vault 根目录执行 `/init`，项目规则通常会写到：

```
<Vault>/CLAUDE.md
```

Claude Code 也支持：

```
<Vault>/.claude/CLAUDE.md
```

前者更醒目，也更方便和团队共享。

后者适合把 Claude Code 配置集中在 `.claude` 目录。

两者都属于项目级指令。

新的 Claude Code 会话从这个 Vault 启动时，会自动加载它们。

---

### 10.3 Claude Desktop 能否读取

那 Claude Desktop 能不能读？

普通 Claude Desktop 聊天不会自动扫描你的 Vault。

它也不会自动读取 Claudian 的 `.claudian` 会话索引，或 Claude Code 用户目录里的 JSONL 转录。

`CLAUDE.md` 是 Claude Code 的项目指令机制。

不能因为同一台电脑装了 Claude Desktop，就假设桌面聊天会自动加载。

---

如果你使用 Claude Desktop 的 Cowork，并把这个 Vault 作为本地文件夹连接，它可以访问文件夹中的 `CLAUDE.md`。

但“能够访问”不等于“按 Claude Code 规则自动加载”。

稳妥做法是把关键内容配置成 Cowork 项目指令，或者在任务中明确让它读取 `CLAUDE.md`。

如果你只是想延续 Claudian 的旧对话，也不要直接把 JSONL 当成桌面端会话导入。

更合适的是让 Claudian 先生成一份 Markdown 总结，再交给 Claude Desktop。

---

### 10.4 同步与隐私建议

如果你开了 Obsidian Sync、iCloud 或 Git，不要无脑同步所有隐藏目录。

普通 Markdown 笔记当然要同步。

但 `.claudian/` 和 `.claude/` 可能增长很快，也可能含本机路径、会话或配置。

建议先检查实际内容，再决定排除策略。

API Key 不要写进课程笔记，不要截图，也不要提交到 Git。

配置文件需要备份时，先用占位符替换密钥。

---

## 11. 安装 TheSchema Skill

接下来安装一套 TheSchema Skill，为 Claudian 增加适用于当前知识库的工作规范。

> **TIP**
>
> TheSchema 背后的理论来源，与 Andrej Karpathy 提出的 LLM Wiki 模式有关。本教程只处理 Skill 的安装、配置和验证，不展开 LLM Wiki 的原理。如需了解 TheSchema 的思想来源，可以阅读 Karpathy LLM Wiki 课程预告；这不影响本文的安装步骤。

Claudian 解决的是“怎么把 Agent 接进 Obsidian”。

Skill 解决的是“接进来以后，Agent 应该按什么方法工作”。

TheSchema Skill 会把知识库任务分成三种状态。

INGEST 负责把学习资料提炼进 wiki。

QUERY 负责基于现有 wiki 回答问题。

LINT 负责检查矛盾、孤立页面和缺失链接。

---

### 11.1 Skill 是怎样加载的

Skill 不是一段每次都要复制的超长 Prompt。

它是一个文件夹。

里面至少有 `SKILL.md`。

Agent 启动时通常只看到 name 和 description。

请求命中后，才读取完整指令。

指令再需要某个参考文件时，才继续加载。

这叫渐进式披露。

它能让你安装很多 Skill，又不用一开始把所有说明塞进上下文。

---

### 11.2 Skill 的源目录与发现目录

如果前面已经把 CC Switch 的 **Storage Location** 设置为 `~/.agents/skills/`，这套 TheSchema Skill 的共享源目录应当是：

```
~/.agents/skills/obsidian-theschema-workflow/
└── SKILL.md
```

这是 Skill 的实体目录，也是唯一需要维护的版本。下面只在 Vault 中创建入口，不再复制 `SKILL.md`。

这段先演示 Claude Code 路线。

Claude Code 从 Vault 项目级 `.claude/skills/`，或者用户级 `~/.claude/skills/` 发现 Skill。

如果 Claudian 当前接的是 Codex，当前版本可以从 Vault 的 `.codex/skills/` 和 `.agents/skills/` 发现 Skill；用户级 Codex Skill 通常位于 `~/.codex/skills/`。

因此 Claude 与 Codex 的 Vault 级发现目录并不完全相同，不能只在一个目录放实体副本后假设两边都会加载。

推荐做软链接。

这样只维护一份源文件。

项目里看到的是入口，不会出现两个版本。

---

### 11.3 为 Claude Code 创建项目级 Skill 入口

`ln -s` 是 macOS 和 Linux 创建软链接的命令，基本格式是：

```
ln -s <源文件或源目录> <软链接入口>
```

源目录写在前面，入口写在后面。软链接类似快捷方式：Agent 访问 Vault 中的入口时，实际读取的是共享源目录里的文件。

在 Vault 根目录执行：

```
test -f "$HOME/.agents/skills/obsidian-theschema-workflow/SKILL.md" && \
mkdir -p .claude/skills && \
ln -s "$HOME/.agents/skills/obsidian-theschema-workflow" \
  .claude/skills/obsidian-theschema-workflow
```

第一条命令检查共享源目录中是否真的存在 `SKILL.md`。没有任何输出并正常返回，说明文件存在；如果提示不存在，应先修正源路径，不要继续创建链接。

第二条命令创建 Claude Code 的项目级 Skill 目录。第三条命令建立软链接，让 Claude Code 使用共享源文件，而不是复制出第二份。

执行前先确认当前目录就是 Vault 根目录。`$HOME` 会自动展开为当前用户的主目录，因此不要把示例中的用户名写死。

再检查链接：

```
ls -la .claude/skills/obsidian-theschema-workflow
readlink .claude/skills/obsidian-theschema-workflow
```

`ls -la` 的结果开头应当是 `l`，并显示箭头指向共享源目录。`readlink` 会直接输出链接目标。

如果目标位置已经存在普通文件或目录，`ln -s` 会提示 `File exists`。先用 `ls -ld` 判断它是文件、目录还是旧软链接，再决定如何迁移；不要为了重建链接直接删除未检查的内容。

---

### 11.4 为 Codex 创建项目级 Skill 入口

如果还要让 Claudian 的 Codex Provider 使用同一份 Skill，可以在 Vault 根目录执行：

```
test -f "$HOME/.agents/skills/obsidian-theschema-workflow/SKILL.md" && \
mkdir -p .agents/skills && \
ln -s "$HOME/.agents/skills/obsidian-theschema-workflow" \
  .agents/skills/obsidian-theschema-workflow
```

然后验证：

```
ls -la .agents/skills/obsidian-theschema-workflow
readlink .agents/skills/obsidian-theschema-workflow
```

也可以直接使用 CC Switch 的 Skill 同步功能，让它根据前面选择的 Symlink 方式创建各应用入口。无论采用哪种方式，都只维护 `~/.agents/skills/obsidian-theschema-workflow/` 这一份实体内容。

在 Claudian 中，新建会话后输入 `/` 或 `$` 检查 Skill 是否出现；输入 `@` 可以引用具体文件。Claude 与 Codex 的发现入口可能不同，应以当前 Provider 的菜单结果为准。

如果你的 Skill 没有存放在 `~/.agents/skills/`，不要照抄源路径。

先找到包含 `SKILL.md` 的真实目录，再把 `ln -s` 后面的第一个参数替换成该目录的绝对路径。

---

### 11.5 为什么不复制 TheSchema.md

为什么不把 `TheSchema.md` 复制进 Skill？

因为规则会更新。

复制一份，很快就会出现两个真相源。

这个 Skill 的设计是：每次触发后，先完整读取 Vault 里的 `300-wiki/TheSchema.md`。

工作流规则永远以这份实时文件为准。

Skill 只负责识别任务状态、加载规范、约束边界和完成验证。

---

## 12. 参考资料

- [Claudian 官方仓库](https://github.com/YishenTu/claudian)
- [Claudian Releases](https://github.com/YishenTu/claudian/releases)
- [Claudian 社区插件安装与隐私说明](https://github.com/YishenTu/claudian/blob/main/README.md)
- [Claude Code 安装文档](https://code.claude.com/docs/en/installation)
- [Claude Code CLAUDE.md 与 Memory 文档](https://code.claude.com/docs/en/memory)
- [Codex CLI 官方入门](https://help.openai.com/en/articles/11096431)
- [CC Switch 官方仓库](https://github.com/farion1231/cc-switch)
- [CC Switch Skills 管理文档](https://github.com/farion1231/cc-switch/blob/main/docs/user-manual/en/3-extensions/3.3-skills.md)
- CLI
- Skills 技能系统
- Skill 渐进式披露机制
- File over App
- TheSchema
