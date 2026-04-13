# Hermes Skills Repository

English | [中文](#hermes-skills-仓库说明)

## Overview

This repository contains custom skills for Hermes Agent.

> Acknowledgment: Thanks to Jin10 for providing the MCP service. This skill only adapts the usage format and does not intend to replace or imitate the [official Jin10 service](https://mcp.jin10.com/app).
>
> Token and service page: `https://mcp.jin10.com/app`

Current published skill:

- `skills/jin10` — Jin10 market quotes, flash headlines, news lookup, and economic calendar access through a bundled Python CLI wrapper.

The `jin10` skill is designed for both CLI and messaging-platform use in Hermes, including Discord.

## Repository Layout

```text
.
├── skills/
│   └── jin10/
│       ├── SKILL.md
│       ├── README.md
│       ├── jin10/
│       ├── references/
│       └── scripts/
├── README.md
└── .gitignore
```

The Hermes-ready distributable skill lives under:

```text
skills/jin10
```

## Install This Skill

### Prerequisite: Create Your Jin10 Token File

```bash
mkdir -p ~/.config/jin10
chmod 700 ~/.config/jin10
nano ~/.config/jin10/api_token
chmod 600 ~/.config/jin10/api_token
```

Paste your Jin10 token into that file as the only content, save, and exit `nano`.

Get your Jin10 token from: `https://mcp.jin10.com/app`

### Option 1: Copy into `~/.hermes/skills/`

```bash
git clone https://github.com/robinspt/hermes-skills.git
cd hermes-skills
mkdir -p ~/.hermes/skills
cp -r skills/jin10 ~/.hermes/skills/
```

### Option 2: Add This Repository as a Custom Tap

```bash
git clone https://github.com/robinspt/hermes-skills.git
cd hermes-skills
hermes skills tap add robinspt/hermes-skills
hermes skills inspect robinspt/hermes-skills/jin10
hermes skills install robinspt/hermes-skills/jin10
hermes skills list
```

After either install method, start a new Hermes session, or restart the gateway if you use Discord/Telegram:

```bash
hermes gateway restart
```

## Usage

### CLI

```bash
hermes chat --toolsets skills,terminal -q "/jin10 check the latest gold price"
```

### Discord / Messaging Platforms

```text
/jin10 看看最新的金价
```

If Discord does not autocomplete `/jin10`, that does not necessarily mean the skill is unavailable. Use:

```text
/commands
```

to confirm that Hermes has loaded the skill on the messaging side. If needed, check additional pages with `/commands 2`, `/commands 3`, and so on. Then type `/jin10 ...` manually. This can happen because Discord's native slash command registration is limited to 100 commands.

## Custom Repository Notes

- Hermes skill document: `skills/jin10/SKILL.md`
- Skill name: `jin10`
- Category: `finance`
- Local token file: `~/.config/jin10/api_token`
- Required Hermes toolsets: `skills`, `terminal`

## References

- Working with Skills: `https://hermes-agent.nousresearch.com/docs/guides/work-with-skills`
- Skills System: `https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/`
- Creating Skills: `https://hermes-agent.nousresearch.com/docs/developer-guide/creating-skills`
- Slash Commands Reference: `https://hermes-agent.nousresearch.com/docs/reference/slash-commands`
- CLI Commands Reference: `https://hermes-agent.nousresearch.com/docs/reference/cli-commands/`

---

# Hermes Skills 仓库说明

## 概述

这个仓库用于存放 Hermes Agent 的自定义 skills。

> 致谢：感谢金十数据提供 MCP 服务。本 skill 仅进行使用方式转换，无意替代或模仿[金十数据官方服务](https://mcp.jin10.com/app)。
>
> 获取地址：`https://mcp.jin10.com/app`

当前主要 skill：

- `skills/jin10`：通过随包分发的 Python CLI，提供金十行情报价、财经快讯、资讯搜索与财经日历查询能力。

`jin10` skill 可用于 Hermes CLI，也可用于 Discord 等消息平台。

## 仓库结构

```text
.
├── skills/
│   └── jin10/
│       ├── SKILL.md
│       ├── README.md
│       ├── jin10/
│       ├── references/
│       └── scripts/
├── README.md
└── .gitignore
```

真正用于 Hermes 分发和安装的目录是：

```text
skills/jin10
```

## 安装方法

### 前置条件：创建 Jin10 token 文件

```bash
mkdir -p ~/.config/jin10
chmod 700 ~/.config/jin10
nano ~/.config/jin10/api_token
chmod 600 ~/.config/jin10/api_token
```

把 Jin10 token 粘贴到这个文件里，确保文件中只有 token 本身，保存并退出 `nano`。

Jin10 token 获取地址：`https://mcp.jin10.com/app`

### 方式一：复制到 `~/.hermes/skills/`

```bash
git clone https://github.com/robinspt/hermes-skills.git
cd hermes-skills
mkdir -p ~/.hermes/skills
cp -r skills/jin10 ~/.hermes/skills/
```

### 方式二：把仓库添加为自定义 Tap

```bash
git clone https://github.com/robinspt/hermes-skills.git
cd hermes-skills
hermes skills tap add robinspt/hermes-skills
hermes skills inspect robinspt/hermes-skills/jin10
hermes skills install robinspt/hermes-skills/jin10
hermes skills list
```

如果你使用 Discord、Telegram 等消息平台，任一安装方式完成后都建议执行：

```bash
hermes gateway restart
```

## 使用方式

### CLI

```bash
hermes chat --toolsets skills,terminal -q "/jin10 看看最新的金价"
```

### Discord / 消息平台

```text
/jin10 看看最新的金价
```

如果 Discord 没有自动补全出 `/jin10`，并不一定代表这个 skill 不可用。请先执行：

```text
/commands
```

用来确认 Hermes 是否已经在消息平台侧识别到这个 skill。必要时继续翻页查看，比如 `/commands 2`、`/commands 3`。确认存在后，再手动输入 `/jin10 ...`。出现这种情况，可能是因为 Discord 原生 slash command 注册数量上限为 100。

## 自定义仓库说明

- Hermes skill 文档：`skills/jin10/SKILL.md`
- skill 名称：`jin10`
- 分类：`finance`
- 本地 token 文件：`~/.config/jin10/api_token`
- 依赖的 Hermes toolsets：`skills`、`terminal`

## 参考文档

- Skills 使用指南：`https://hermes-agent.nousresearch.com/docs/guides/work-with-skills`
- Skills 系统：`https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/`
- 创建 Skills：`https://hermes-agent.nousresearch.com/docs/developer-guide/creating-skills`
- Slash Commands：`https://hermes-agent.nousresearch.com/docs/reference/slash-commands`
- CLI Commands：`https://hermes-agent.nousresearch.com/docs/reference/cli-commands/`
