---
name: web-quiz-research
description: Analyze overseas Web Quiz themes using a lightweight index/results knowledge workflow with mandatory Chrome-first live retrieval. Read a project index file or pasted document information for business context; actually query user-provided or default sources through the user's Chrome browser when platform login, cookies, or dynamic pages matter, including Facebook, YouTube, Pinterest, Guangdada, Meta Ads Library, and Google Trends; mark public-source evidence and access limits clearly; explore both index-related themes and open health/fitness category opportunities; rank quiz themes by P0/P1/P2/P3; and write structured Markdown/PDF reports into a results file. Use for walking, stretching, fitness, yoga, low-impact workouts, health management, Meta/WebOB paid social funnels, social heat, competitor ad research, Google Trends, Guangdada, Facebook Ads Library, YouTube, Pinterest, and Facebook/Reels.
---

# Web Quiz Research

## Overview

Use this skill to research overseas Web Quiz theme opportunities from a lightweight `index/document -> research -> results` workflow. The skill stores no specific business knowledge; read the user's index file or pasted document information for business context and write final structured findings to a results Markdown file when a path is available.

## Resource Guide

- Read `references/output-template.md` when producing a full results report.
- Read `references/scoring-model.md` when ranking themes, test cells, or prioritizing P0/P1/P2/P3.
- Use `scripts/markdown_to_pdf.py` after writing a Markdown results file to generate a PDF copy in the same results directory.

## Simplified Input Rules

Accept minimal user input:

- Index path or business alias, such as `walking index`, `stretching index`, or `fitness index`.
- If no index path or alias is provided, use the user's pasted document information in the current message as a temporary index. Treat it as the source of product background, funnel, market, users, competitors, keywords, entry links, compliance preferences, and output preferences.
- Optional entry links, such as Guangdada, Meta Ads Library, YouTube, Pinterest, Facebook Reels, or TikTok Creative Center.
- Optional focus, such as `focus on chair walking`, `only competitor analysis`, `only testing priority`, or `open health and fitness exploration`.
- Optional results output path.

Do not ask the user to repeat competitor lists, markets, target users, control groups, keyword seeds, compliance preferences, output structure, default entry links, or default results paths if they are present in the index or pasted document information.

## Default Path Mapping

This skill is team-shareable and should not require the author's local knowledge base. Prefer these sources in order:

1. Explicit `index` path provided by the user.
2. Pasted project document information in the prompt.
3. A Markdown file in a user-provided index directory.
4. Author-only local fallback paths, only when they exist on the current machine.

Team members should provide their own `index` and `results` paths, or paste the project document directly. Explicit user-provided paths always override any fallback.

If the original author says `walking index`, `Hot_quiz index`, or provides `/Users/fengrui1/Desktop/Hot_quiz/index`, map it to this author-only fallback path only when it exists:

`/Users/fengrui1/Desktop/Hot_quiz/index`

When an index path is a directory, read exactly one Markdown file from that directory:

- If the directory contains one `.md` file, read that file.
- If the directory contains multiple `.md` files, prefer a file whose name contains `WalkUp` or `健走`.
- If still ambiguous, ask the user which index file to use.

Current expected walking index file:

`/Users/fengrui1/Desktop/Hot_quiz/index/WalkUp 健走知识库.md`

If the original author says `walking results`, `Hot_quiz results`, or provides `/Users/fengrui1/Desktop/Hot_quiz/results`, map it to this author-only fallback results directory only when it exists:

`/Users/fengrui1/Desktop/Hot_quiz/results`

If the results path is a directory, create a new Markdown file inside it instead of overwriting the directory. Use a clear filename such as:

`web-quiz-research-{YYYY-MM-DD}-{topic-slug}.md`

If the index defines `default_results_path`, prefer that path only when it is more specific than the user's provided results path. If the user explicitly provides `/Users/fengrui1/Desktop/Hot_quiz/results`, use that directory and create a new `.md` file there.

If no usable index path, pasted document information, or author-only fallback exists, ask the user to provide either an index Markdown path, a directory containing one index Markdown file, or pasted project information. Do not require a local knowledge base.

## Workflow

1. Read exactly one index source: a mapped index file, a provided Markdown file, a single Markdown file inside a provided index directory, or the user's pasted document information if no index path is provided.
2. Extract product background, funnel, control group, markets, users, priority themes, keyword seeds, competitor pool, channel rules, entry links, results path, compliance preferences, and output preferences.
3. Interpret the user's current focus: full report, topic-only, competitor-only, social heat-only, open exploration, testing priority-only, or write-to-file.
4. Run two exploration lines by default:
   - Knowledge-related exploration based on index themes, keyword seeds, and competitors.
   - Open health/fitness exploration beyond existing index terms, looking for adjacent quiz opportunities.
5. Collect channel evidence from user-provided links first, then index default links, then built-in defaults.
6. Score and rank themes using `references/scoring-model.md`.
7. Produce the Markdown structure from `references/output-template.md`.
8. If a results path is provided or discovered from the index, write the final report there. If it is a file path, overwrite that file unless the user explicitly requests append. If it is a directory path, create a new Markdown file in that directory. Do not ask again before writing.
9. After the Markdown file is written, generate a PDF file from the same Markdown report using `scripts/markdown_to_pdf.py`. Save the PDF next to the Markdown file using the same basename and `.pdf` extension.

## Mandatory Retrieval And Evidence Rules

Use the project index as business context only. Do not treat index content, prior conclusions, or memory as proof of current external heat.

For every social heat, competitor dynamic, or trend conclusion, collect evidence during the current run. If direct platform retrieval is blocked by login, CAPTCHA, region, paywall, or tool limits, mark the channel as `Access Limited` and do not invent titles, images, spend, view counts, trend values, or backend metrics.

Platform retrieval must be Chrome-first. For Facebook, Facebook Reels, Pinterest, Guangdada, Meta Ads Library, Google Trends, and any other login/profile-dependent source, first attempt retrieval through the user's Chrome browser using the Chrome plugin so the user's existing login permissions, cookies, profile, and extensions can be used. Use generic web search or unauthenticated public pages only after the Chrome attempt fails, is unavailable, or the source itself is public and does not require a logged-in view.

Acceptable evidence labels:

- `Live Retrieval`: directly observed during this run from Facebook, YouTube, Pinterest, Guangdada, Meta Ads Library, Google Trends, TikTok Creative Center, or another user-provided channel.
- `Public Source`: publicly reachable pages, search results, app store pages, official pages, articles, or indexed snippets. These can support a theme, but must not be described as platform heat unless they come from that platform.
- `Index`: project knowledge base facts such as product, market, user, competitor list, historic winning themes, constraints, and default links.
- `Inference`: a business judgment derived from labeled evidence. Always state the evidence basis.
- `Access Limited`: the channel was attempted but not fully readable. Include the attempted link and limitation.

Hard rules:

- P0 themes must have at least one retrieved evidence source from the current run. For claims about `社媒热度` or `竞品动态`, prefer channel-specific `Live Retrieval`; otherwise clearly mark the conclusion as lower-confidence public-source evidence.
- Public information is allowed, but every public-source item must show its source link and be labeled `Public Source`.
- Do not replace a requested channel search with generic web search unless Chrome-backed retrieval has been attempted or the channel is explicitly public and login-free.
- When Chrome-backed retrieval is attempted, record `Chrome Used`, `Chrome Blocked`, or `Chrome Unavailable` in the source verification table.
- If a channel cannot provide visible interaction data, rank heat by visible proxy signals only, such as repeated topic appearance, creator/page prominence, recency, ad volume, creative repetition, or Google Trends direction.
- Never fabricate ad spend, impressions, CTR, conversion, revenue, exact search volume, or backend platform metrics.
- Always include a source verification table in the final report.

## Entry Link Rules

If the user provides entry links, use them first. If they provide only an entry page, complete the filtering yourself where tools allow. For example, if they provide Guangdada's display ads page, filter for health/fitness, Facebook-family placements, recent windows such as 90 days, and index keywords where possible.

If no entry link is provided, use index `Default Entry Links`. If the index lacks defaults, use these built-in defaults:

- Guangdada: `https://guangdada.net/modules/creative/display-ads`
- Meta Ads Library: `https://www.facebook.com/ads/library/`
- YouTube: `https://www.youtube.com/`
- Pinterest: `https://www.pinterest.com/`
- Facebook: `https://www.facebook.com/`
- Facebook Reels: `https://www.facebook.com/reel/`
- Google Trends: `https://trends.google.com/trends/`
- TikTok Creative Center: `https://ads.tiktok.com/business/creativecenter/`

If no usable entry is available after these steps, ask the user for an entry link.

## Channel Collection Rules

Social heat channels:

- Facebook / Reels
- YouTube / Shorts
- Pinterest
- TikTok when requested or present in index
- Google Trends for keyword trend validation

Competitor dynamics channels:

- Guangdada
- Meta Ads Library
- TikTok Creative Center when requested or present in index

For each channel, capture search term, theme, evidence basis, representative title/copy, image or material pattern, source link, and quiz fit. If ad tools expose ad metrics, capture ad count, deduped count, impression estimate, heat, running days, last seen time, advertiser, Top10% status, and re-run status. Never invent unavailable metrics.

Channel-specific requirements:

- Facebook: search public posts, reels, pages, or visible video surfaces. Capture title/copy, visible interactions when available, format, material recognition, source link, and access limits.
- YouTube/Shorts: capture title, channel, visible views/date when available, thumbnail/material pattern, and source link.
- Pinterest: capture pin title/visible copy, image/material pattern, format, source link, and repeated motif.
- Guangdada: search the health/fitness category and competitor names where possible. Use recent window filters such as last 90 days when available. Capture advertiser, title/copy, image/material recognition, visible heat/ad-count/running-day proxies, landing/product if visible, and source link. If login blocks details, mark the limitation.
- Meta Ads Library: search active ads and relevant competitor/page/theme terms. Capture page, ad body, start date/active status, creative type, image/material recognition, landing clue, and library link. Do not claim spend or impressions unless visibly provided by the library.
- Google Trends: compare theme keywords in index markets. Default timeframe is the last 12 months unless the user asks for another window. Capture geo, timeframe, trend direction, related queries/topics if visible, and source link.

Chrome-first retrieval protocol:

1. Load the Chrome skill before platform retrieval when the task asks for Facebook, YouTube, Pinterest, Guangdada, Meta Ads Library, Google Trends, or other browser-based channels.
2. Run the Chrome extension's lightweight connection check before the first Chrome-backed retrieval in the session.
3. Open, search, filter, inspect, and screenshot/read platform pages through the user's Chrome browser whenever the channel may depend on login state, cookies, region, or user profile.
4. Mark successful Chrome retrieval as `Chrome Used` and evidence type as `Live Retrieval`.
5. If Chrome cannot connect, the page blocks access, login is missing, or details are hidden, mark the channel as `Chrome Blocked` or `Chrome Unavailable`, then use `Access Limited` for that channel.
6. Only after recording the Chrome limitation may you use public-source fallback evidence. Label it `Public Source` and do not present it as direct platform heat.

## Output And Write Rules

Use `references/output-template.md` for full reports. If the user requests a short version, output only Testing Priority, First-Round Test Cells, and Final Recommendation.

When writing results:

- If the specified results path is a file, overwrite it unless the user requests append.
- If the specified results path is a directory, create a new Markdown file inside it.
- Always create a PDF copy from the final Markdown file.
- Save the PDF next to the Markdown file with the same basename, for example `web-quiz-research-2026-05-26-chair-walking.pdf`.
- Do not write browsing logs.
- Save only the final structured report.
- After writing, reply with both the Markdown file path and the PDF file path, plus a short summary.

## Team Data Safety Rules

- Do not commit real index files, generated results reports, PDFs, platform exports, screenshots with account information, cookies, tokens, credentials, or raw ad/user data into the skill repository.
- Treat pasted business context, index files, and results as project data. Use them for the current run only unless the user explicitly asks to save them.
- If the repository is public or shared outside the immediate team, keep only reusable methodology, templates, and scripts in the repo.
- Results files should live in a user-provided local `results` directory or private workspace, not inside the shared skill repository.
- When using Chrome-backed retrieval, never record session cookies, account identifiers, private inbox content, billing pages, or non-research personal data in the final report.
- For competitor creative evidence, record source links and material patterns; do not download, rehost, or copy proprietary creative assets into the repository.

## Token Saving Rules

- Read only one index file.
- If using pasted document information as temporary index, do not additionally read default index files unless the user asks.
- Do not read historical results by default.
- Do not read archives by default.
- Keep only high-signal samples per channel.
- Keep 3-5 representative evidence items per theme.
- Limit open exploration to Top 10.
- Limit final testing priority to Top 10-12.
- Use tables instead of long process explanations.

## Compliance Rules

Do not fabricate precise ad spend, search volume, conversion rate, or platform backend data. Mark observation date, keep source links, and separate observed facts from inference. Mention login or access limits when they affect evidence.

Health and weight-management language must be cautious.

Avoid:

- guaranteed weight loss
- lose belly fat fast
- fix metabolism
- cure pain
- no knee pain
- 100% refund if no effect
- age/body shaming
- over-strong before/after

Prefer:

- gentle daily movement
- low-impact routine
- designed for your pace
- support steady progress
- balance and mobility
- build a habit
- beginner-friendly
- no equipment needed
