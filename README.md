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

Use your own local `index` and `results` paths:

```text
使用 web-quiz-research

index: /path/to/your/index
results: /path/to/your/results

研究主题：chair walking
请输出完整报告，并生成 md + pdf
```

If no index path is provided, paste the project information directly into the prompt and the skill will treat it as a temporary index.

## Notes

- The skill does not store fixed business knowledge; business context should come from the user's index file or pasted document information.
- If `results` is a directory, the skill creates a new Markdown file and a matching PDF file inside that directory.
- Do not commit private ad data, user data, platform credentials, or raw exports to this repository.
