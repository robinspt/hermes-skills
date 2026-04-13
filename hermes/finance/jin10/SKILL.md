---
name: jin10
description: Query Jin10 quotes, flash headlines, news, and economic calendar data. 适用于黄金/白银/原油/外汇报价、财经快讯、资讯详情、财经日历、非农和央行事件等请求。
version: 1.0.0
author: Jin10 Skill Maintainers
platforms: [macos, linux]
metadata:
  hermes:
    tags: [finance, markets, news, calendar, china]
    category: finance
    requires_toolsets: [terminal]
required_environment_variables:
  - name: JIN10_API_TOKEN
    prompt: Jin10 API token
    help: Get one at https://mcp.jin10.com/app
    required_for: Access to the Jin10 MCP endpoint
---

# Jin10 Skill

> 致谢：感谢金十数据提供 MCP 服务。本 skill 仅进行使用方式转换，无意替代或模仿金十数据官方服务。

Use this skill to access Jin10 market data through the bundled Python CLI. It wraps the Jin10 MCP endpoint behind stable shell commands, so do not write raw MCP `initialize`, `tools/call`, `resources/read`, or session-header logic in chat.

Assume the skill is installed at `~/.hermes/skills/finance/jin10`. If the user installs it through `skills.external_dirs`, keep the same relative layout and substitute the actual root path.

## When to Use

- 用户问黄金、白银、原油、外汇等品种的最新报价或代码。
- 用户问某个主题的最新财经快讯，例如美联储、非农、原油、关税。
- 用户问某个主题的资讯列表，或要求打开某篇 Jin10 资讯详情。
- 用户问财经日历、本周重点数据、高重要性事件、非农、CPI、央行决议。
- 不要把这个 skill 用于一般网页搜索、券商专属报价，或 Jin10 数据覆盖之外的问题。

## Quick Reference

```bash
python3 ~/.hermes/skills/finance/jin10/scripts/jin10.py --format json codes
python3 ~/.hermes/skills/finance/jin10/scripts/jin10.py --format json quote XAUUSD
python3 ~/.hermes/skills/finance/jin10/scripts/jin10.py --format json flash search "美联储"
python3 ~/.hermes/skills/finance/jin10/scripts/jin10.py --format json news search "原油"
python3 ~/.hermes/skills/finance/jin10/scripts/jin10.py --format json news get 123456
python3 ~/.hermes/skills/finance/jin10/scripts/jin10.py --format json calendar --high-importance
```

Read [references/api-contract.md](references/api-contract.md) when you need the field contract or selection rules.

## Procedure

1. 先判断请求属于 `quote`、`flash`、`news` 还是 `calendar`。
2. 默认使用 `--format json`，只有在用户明确需要可读块状文本时才切到 `--format text`。
3. 查询报价时，如果代码不明确，先跑 `codes`，再跑 `quote <CODE>`。
4. 查询主题快讯时，优先用 `flash search <关键词>`；只有顺序浏览最新流时才用 `flash list` 和 `--cursor`。
5. 查询资讯时，先用 `news search <关键词>` 或 `news list` 找到条目，再用 `news get <id>` 取详情。
6. 查询财经日历时，默认用 `calendar`；按主题筛选时用 `--keyword`；只要重磅事件时用 `--high-importance`。
7. 回复时保留代码、时间戳、事件值、文章 ID 等关键信息；除非用户另有要求，否则优先用中文总结。

## Pitfalls

- 不要在对话里手写 MCP 协议消息。统一调用脚本。
- 不要假设 Hermes 会把 `~/.hermes/.env` 内容暴露给模型；应依赖 `required_environment_variables` 和终端环境透传。
- 如果 `JIN10_API_TOKEN` 缺失，命令会直接失败。Hermes 在本地 CLI 加载 skill 时可以安全提示用户补齐。
- `flash search` 用于关键词过滤；需要翻页时应使用 `flash list --cursor ...`。
- `news get` 必须先拿到有效的文章 `id`。
- 如果用户问的是交易所原生价格或特定券商盘口，需要说明这里返回的是 Jin10 数据，不是交易所直连行情。

## Verification

- 命令退出码应为 `0`。
- JSON 输出结构应符合预期：
  - `quote`: `data.code`、`data.name`、`data.time`
  - `flash` / `news` 列表：`data.items`
  - `news get`: `data.id`、`data.title`、`data.content`
  - `calendar`: `data`
- 报价请求要确认返回的 `code` 与目标品种一致。
- 列表请求在宣称“没有更多结果”之前，要检查 `has_more` 和 `next_cursor`。
