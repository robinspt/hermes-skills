# Hermes Skill Build Notes

This file is local-only and should not be committed.

## Goal

Turn a working local wrapper into a Hermes-usable community skill that can be:

- copied into `~/.hermes/skills/`
- installed via `hermes skills install owner/repo/skill`
- used in CLI and messaging platforms

## Build Steps

1. Keep the distributable repo layout simple:
   - `skills/<skill-name>/SKILL.md`
   - helper code under `skills/<skill-name>/...`
2. Put the real skill identity in `SKILL.md` frontmatter:
   - `name`
   - `description`
   - `metadata.hermes.category`
   - `metadata.hermes.requires_toolsets`
3. Keep the packaged skill self-contained:
   - bundled script
   - Python package
   - references
4. Avoid leaking unrelated implementation history:
   - no OpenClaw-specific files
   - no duplicate source trees
   - no `__pycache__` or `.pyc`
5. Make install docs explicit:
   - `git clone`
   - `cd`
   - token setup
   - direct install commands
6. Validate the packaged artifact, not just local source code:
   - `hermes skills inspect owner/repo/skill`
   - `hermes skills install owner/repo/skill`
   - `hermes skills list`
   - `hermes chat --toolsets skills,terminal -q "/skill-name ..."`
7. Test a messaging platform separately after gateway restart.

## Important Findings From This Skill

- This project is a skill adapted from the official Jin10 MCP service.
- Unless the official Jin10 MCP integration pattern changes, do not change the underlying MCP/client logic casually.
- For custom taps, the repo distribution path that worked was `skills/jin10`, not `skills/finance/jin10`.
- After install, Hermes placed the skill at `~/.hermes/skills/jin10/`.
- `metadata.hermes.category: finance` still works for display/category even though the install path has no `finance` segment.
- `hermes skills search jin10` was not a reliable check for successful install.
- Better checks were:
  - `hermes skills inspect owner/repo/skill`
  - `hermes skills install owner/repo/skill`
  - `hermes skills list`
  - actual `/jin10 ...` execution

## Security Scan Lessons

- Community publish scans are sensitive to anything that looks like secret handling or exfiltration.
- Safer packaging choices included:
  - removing `.env` write instructions from README
  - removing explicit env-var setup from skill docs
  - reading the token from a local file path instead of documenting in-band secret export
  - avoiding text like "raw MCP messages"

## Messaging Platform Notes

- Discord could run `/jin10 ...` successfully even when native slash autocomplete was incomplete.
- `/commands` was useful to confirm the command existed on the messaging side.

## Publishing Guidance

- `hermes skills publish ... --to github --repo owner/repo` publishes to the specified GitHub repo, not to a special Hermes-owned official repository.
- For a self-managed custom source, keeping the repo clean and installable mattered more than opening an auto-generated PR back into the same repo.
