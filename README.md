# Freya WalkUp AI Skills

Reusable Codex skills for WalkUp and overseas Web Quiz research workflows.

## Skills

| Skill | Purpose |
|---|---|
| `web-quiz-research` | Research overseas Web Quiz themes with an `index -> research -> results` workflow, social heat, competitor ads, P0/P1/P2/P3 scoring, Markdown report output, and PDF generation. |

## Install

Install `web-quiz-research` into Codex:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo lemoncake1214/freya_walkup-ai-skills \
  --path skills/web-quiz-research
```

Restart Codex after installation.

## Usage

Team members should use their own local `index` and `results` paths:

```text
使用 web-quiz-research

index: /path/to/your/index
results: /path/to/your/results

研究主题：chair walking
请输出完整报告，并生成 md + pdf
```

If no index path is provided, paste the project information directly into the prompt and the skill will treat it as a temporary index.

Example without a local knowledge base:

```text
使用 web-quiz-research

results: /path/to/your/results

以下是本次业务文档信息：
【粘贴产品背景、用户、市场、竞品、关键词、渠道、合规偏好】

研究主题：chair walking
请输出完整报告，并生成 md + pdf
```

## Team Data Safety

Do not commit private business data into this repository.

Keep these out of Git:

- real index files with product strategy or business priorities
- generated results reports and PDFs
- platform exports, ad exports, CSV/XLSX files
- screenshots containing account, billing, or private platform information
- cookies, tokens, API keys, passwords, or browser profile data
- raw user data or performance data that should remain private

The repository should contain reusable methodology only: `SKILL.md`, templates, scoring rules, and utility scripts.

## Notes

- The skill does not store fixed business knowledge; business context should come from the user's index file or pasted document information.
- If `results` is a directory, the skill creates a new Markdown file and a matching PDF file inside that directory.
- Do not commit private ad data, user data, platform credentials, or raw exports to this repository.
