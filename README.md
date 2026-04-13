# Hermes Skills Repository

English | [中文](#hermes-skills-仓库说明)

## Overview

This repository contains custom skills for Hermes Agent.

Current published skill:

- `hermes/finance/jin10` — Jin10 market quotes, flash headlines, news lookup, and economic calendar access through a bundled Python CLI wrapper.

The `jin10` skill is designed for both CLI and messaging-platform use in Hermes, including Discord.

## Repository Layout

```text
.
├── hermes/
│   └── finance/
│       └── jin10/
│           ├── SKILL.md
│           ├── README.md
│           ├── jin10/
│           ├── references/
│           └── scripts/
├── SKILL.md                    # Earlier source skill definition kept for reference
├── jin10/                      # Source Python package from the original adaptation
├── references/
└── scripts/
```

The Hermes-ready distributable skill lives under:

```text
hermes/finance/jin10
```

## Install This Skill

### Option 1: Copy into `~/.hermes/skills/`

```bash
mkdir -p ~/.hermes/skills/finance
cp -r hermes/finance/jin10 ~/.hermes/skills/finance/
printf 'JIN10_API_TOKEN=sk-xxxx\n' >> ~/.hermes/.env
```

Then start a new Hermes session, or restart the gateway if you use Discord/Telegram:

```bash
hermes gateway restart
```

### Option 2: Install from GitHub path

Once this repository is pushed, Hermes users can install directly from GitHub:

```bash
hermes skills install robinspt/hermes-skills/hermes/finance/jin10
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

to confirm that Hermes has loaded the skill on the messaging side. If needed, check additional pages with `/commands 2`, `/commands 3`, and so on. Then type `/jin10 ...` manually.

## Publishing Notes

- Hermes skill document: `hermes/finance/jin10/SKILL.md`
- Skill name: `jin10`
- Category: `finance`
- Required environment variable: `JIN10_API_TOKEN`
- Required Hermes toolsets: `skills`, `terminal`

To publish with Hermes CLI from a machine that has Hermes installed:

```bash
hermes skills publish hermes/finance/jin10 --to github --repo robinspt/hermes-skills
```

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

当前主要 skill：

- `hermes/finance/jin10`：通过随包分发的 Python CLI，提供金十行情报价、财经快讯、资讯搜索与财经日历查询能力。

`jin10` skill 可用于 Hermes CLI，也可用于 Discord 等消息平台。

## 仓库结构

```text
.
├── hermes/
│   └── finance/
│       └── jin10/
│           ├── SKILL.md
│           ├── README.md
│           ├── jin10/
│           ├── references/
│           └── scripts/
├── SKILL.md                    # 较早的源 skill 定义，保留作参考
├── jin10/                      # 原始适配中的 Python 包
├── references/
└── scripts/
```

真正用于 Hermes 分发和安装的目录是：

```text
hermes/finance/jin10
```

## 安装方法

### 方式一：复制到 `~/.hermes/skills/`

```bash
mkdir -p ~/.hermes/skills/finance
cp -r hermes/finance/jin10 ~/.hermes/skills/finance/
printf 'JIN10_API_TOKEN=sk-xxxx\n' >> ~/.hermes/.env
```

如果你使用 Discord、Telegram 等消息平台，安装或更新后建议执行：

```bash
hermes gateway restart
```

### 方式二：从 GitHub 路径安装

仓库推送完成后，Hermes 用户可以直接从 GitHub 安装：

```bash
hermes skills install robinspt/hermes-skills/hermes/finance/jin10
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

用来确认 Hermes 是否已经在消息平台侧识别到这个 skill。必要时继续翻页查看，比如 `/commands 2`、`/commands 3`。确认存在后，再手动输入 `/jin10 ...`。

## 发布说明

- Hermes skill 文档：`hermes/finance/jin10/SKILL.md`
- skill 名称：`jin10`
- 分类：`finance`
- 必需环境变量：`JIN10_API_TOKEN`
- 依赖的 Hermes toolsets：`skills`、`terminal`

在已安装 Hermes CLI 的机器上，可以用下面的命令发布：

```bash
hermes skills publish hermes/finance/jin10 --to github --repo robinspt/hermes-skills
```

## 参考文档

- Skills 使用指南：`https://hermes-agent.nousresearch.com/docs/guides/work-with-skills`
- Skills 系统：`https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/`
- 创建 Skills：`https://hermes-agent.nousresearch.com/docs/developer-guide/creating-skills`
- Slash Commands：`https://hermes-agent.nousresearch.com/docs/reference/slash-commands`
- CLI Commands：`https://hermes-agent.nousresearch.com/docs/reference/cli-commands/`
