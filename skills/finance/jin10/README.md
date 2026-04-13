# Jin10 Skill for Hermes Agent

English | [中文](#jin10-金十数据-skill-for-hermes-agent)

## Overview

This skill lets Hermes Agent query Jin10 market data through a bundled Python CLI wrapper around the official Jin10 MCP endpoint.

It is designed for:

- spot gold, silver, crude oil, and FX quotes
- Jin10 flash headlines
- Jin10 news search and article details
- economic calendar events and high-importance releases

This is a packaging and usage adaptation for Hermes Agent. It is not an official Jin10 product.

> Acknowledgment: Thanks to Jin10 for providing the MCP service. This skill only adapts the usage format and does not intend to replace or imitate Jin10's official service.

## Requirements

- Hermes Agent
- `python3`
- a local Jin10 token file at `~/.config/jin10/api_token`

## Installation

From the repository root, copy this skill into your Hermes skills directory:

```bash
mkdir -p ~/.hermes/skills/finance
cp -r skills/finance/jin10 ~/.hermes/skills/finance/
mkdir -p ~/.config/jin10
chmod 700 ~/.config/jin10
nano ~/.config/jin10/api_token
chmod 600 ~/.config/jin10/api_token
```

Paste your Jin10 token into that file as the only content, save, and exit `nano`.

Get your Jin10 token from: `https://mcp.jin10.com/app`

If you use Hermes messaging platforms such as Discord, restart the gateway after installing or updating the skill:

```bash
hermes gateway restart
```

## Usage

### CLI

One-shot:

```bash
hermes chat --toolsets skills,terminal -q "/jin10 check the latest gold price"
```

Interactive:

```text
/jin10 check the latest gold price
/jin10 search flash headlines about the Fed
/jin10 show today's high-importance economic calendar
```

### Discord / Messaging Platforms

You can invoke the skill directly:

```text
/jin10 看看最新的金价
```

If Discord autocomplete does not show `/jin10`, that does not necessarily mean the skill is unavailable. Use:

```text
/commands
```

to confirm that Hermes has loaded the skill on the messaging side. If needed, check additional pages with `/commands 2`, `/commands 3`, and so on. Then type `/jin10 ...` manually. Dynamic local skills may not always appear immediately in Discord's native slash-command autocomplete, even when they are available and working.

## What the Skill Runs

The skill uses the bundled script:

```bash
python3 ~/.hermes/skills/finance/jin10/scripts/jin10.py --format json ...
```

Supported commands:

- `codes`
- `quote <CODE>`
- `flash list`
- `flash search <KEYWORD>`
- `news list`
- `news search <KEYWORD>`
- `news get <ID>`
- `calendar`
- `calendar --keyword <KEYWORD>`
- `calendar --high-importance`

## Notes

- The skill depends on Hermes `skills` and `terminal` toolsets.
- For messaging platforms, installation changes are safest after `hermes gateway restart`.
- If `~/.config/jin10/api_token` is missing or empty, the script will fail fast with a clear error.
- The skill returns Jin10 data, not exchange-direct market data.

## Directory Layout

```text
jin10/
├── SKILL.md
├── README.md
├── jin10/
├── references/
└── scripts/
```

## References

- Hermes skills guide: `https://hermes-agent.nousresearch.com/docs/guides/work-with-skills`
- Hermes skills system: `https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/`
- Hermes creating skills: `https://hermes-agent.nousresearch.com/docs/developer-guide/creating-skills`
- Hermes slash commands: `https://hermes-agent.nousresearch.com/docs/reference/slash-commands`

---

# Jin10 金十数据 Skill for Hermes Agent

## 概述

这个 skill 用于让 Hermes Agent 通过随包附带的 Python CLI 调用金十数据服务，底层包装的是 Jin10 官方 MCP 端点。

适用场景：

- 现货黄金、白银、原油、外汇等报价查询
- 金十财经快讯查询
- 金十资讯搜索与详情读取
- 财经日历与高重要性事件查询

这是面向 Hermes Agent 的封装与使用方式转换，不是 Jin10 官方产品。

> 致谢：感谢金十数据提供 MCP 服务。本 skill 仅进行使用方式转换，无意替代或模仿金十数据官方服务。

## 依赖条件

- Hermes Agent
- `python3`
- 本地 Jin10 token 文件：`~/.config/jin10/api_token`

## 安装方法

在仓库根目录执行下面的命令，把这个 skill 复制到 Hermes 的 skills 目录：

```bash
mkdir -p ~/.hermes/skills/finance
cp -r skills/finance/jin10 ~/.hermes/skills/finance/
mkdir -p ~/.config/jin10
chmod 700 ~/.config/jin10
nano ~/.config/jin10/api_token
chmod 600 ~/.config/jin10/api_token
```

把 Jin10 token 粘贴到这个文件里，确保文件中只有 token 本身，保存并退出 `nano`。

Jin10 token 获取地址：`https://mcp.jin10.com/app`

如果你要在 Discord 等消息平台使用，安装或更新后建议重启 gateway：

```bash
hermes gateway restart
```

## 使用方式

### CLI

单次调用：

```bash
hermes chat --toolsets skills,terminal -q "/jin10 看看最新的金价"
```

交互会话中直接输入：

```text
/jin10 看看最新的金价
/jin10 搜索美联储相关快讯
/jin10 看一下今天高重要性的财经日历
```

### Discord / 消息平台

可以直接调用：

```text
/jin10 看看最新的金价
```

如果 Discord 输入 `/` 后没有自动补全出 `jin10`，并不一定代表这个 skill 不可用。请先执行：

```text
/commands
```

用来确认 Hermes 是否已经在消息平台侧识别到这个 skill。必要时继续翻页查看，比如 `/commands 2`、`/commands 3`。确认存在后，再手动输入 `/jin10 ...` 即可。动态本地 skill 在 Discord 原生命令自动补全中不一定会立即显示，但通常仍然可以正常使用。

## Skill 实际执行的命令

底层调用的是这个脚本：

```bash
python3 ~/.hermes/skills/finance/jin10/scripts/jin10.py --format json ...
```

支持的命令包括：

- `codes`
- `quote <CODE>`
- `flash list`
- `flash search <关键词>`
- `news list`
- `news search <关键词>`
- `news get <ID>`
- `calendar`
- `calendar --keyword <关键词>`
- `calendar --high-importance`

## 说明

- 该 skill 依赖 Hermes 的 `skills` 与 `terminal` toolsets。
- 在消息平台中使用时，安装或更新后最好执行一次 `hermes gateway restart`。
- 如果 `~/.config/jin10/api_token` 不存在或为空，脚本会直接报错并提示。
- 该 skill 返回的是 Jin10 数据，不是交易所直连行情。

## 目录结构

```text
jin10/
├── SKILL.md
├── README.md
├── jin10/
├── references/
└── scripts/
```

## 参考文档

- Hermes skills 使用指南：`https://hermes-agent.nousresearch.com/docs/guides/work-with-skills`
- Hermes skills 系统：`https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/`
- Hermes 创建 skills：`https://hermes-agent.nousresearch.com/docs/developer-guide/creating-skills`
- Hermes slash commands：`https://hermes-agent.nousresearch.com/docs/reference/slash-commands`
