# Scoring Model

Use this model to rank Web Quiz theme opportunities as P0 / P1 / P2 / P3.

## Dimensions

Score each dimension from 1-5.

| Dimension | 1 | 3 | 5 |
|---|---|---|---|
| User fit | Weak fit with index users | Some fit | Strong fit with target user structure |
| Business/control relevance | Far from current direction | Adjacent | Directly extends current control group or business focus |
| Social heat | Little visible activity | Moderate signals | Strong repeated signals across channels |
| Competitor ad strength | No clear competitor activity | Some activity | Strong, recent, repeated competitor ads |
| Evidence quality | Index or inference only | One retrieved channel or credible public source | Multiple live retrieved sources, or one channel with strong visible proxy metrics |
| Web Quiz fit | Hard to turn into quiz | Possible with framing | Easy to turn into quiz hook, questions, feedback, paywall |
| Material producibility | Hard to make assets | Somewhat feasible | Easy to produce high-volume ads and quiz visuals |
| Compliance risk | High risk | Manageable | Low risk with safe wording |
| Channel fit | Weak for current media buying | Some fit | Strong fit for Meta/WebOB or requested channels |

## Priority Rules

| Priority | Definition | Typical action |
|---|---|---|
| P0 | Strong user fit, strong heat, strong competitor or social evidence, strong Web Quiz fit, manageable compliance risk. | Test immediately. |
| P1 | Worth testing; evidence is strong in some dimensions or works as a P0 extension. | Build test cells after P0. |
| P2 | Interesting but evidence is weaker, more adjacent, or needs small-budget validation. | Observe or run small test. |
| P3 | Not recommended as main test; weak fit, high risk, or poor quiz conversion fit. | Use only as branch/content inspiration. |

## Evidence Labels

Use these labels consistently in scoring and output:

- `Live Retrieval`: Directly observed during this run from the requested platform or tool.
- `Public Source`: Publicly reachable source such as search result, official page, app store page, article, indexed snippet, or public website.
- `Index`: Project knowledge base or pasted business context.
- `Inference`: Business judgment derived from labeled evidence.
- `Access Limited`: A retrieval attempt was blocked or incomplete due to login, CAPTCHA, region, paywall, tool limitations, or unavailable details.

For Facebook, YouTube, Pinterest, Guangdada, Meta Ads Library, Google Trends, and other browser-based sources, `Live Retrieval` should normally mean Chrome-backed retrieval through the user's Chrome browser. If Chrome was not used, explicitly explain why in the source verification table.

## Suggested Thresholds

| Priority | Suggested pattern |
|---|---|
| P0 | Average score >= 4.2 and no critical compliance risk |
| P1 | Average score 3.6-4.1 or one evidence line is very strong |
| P2 | Average score 2.8-3.5, trend is plausible but incomplete |
| P3 | Average score < 2.8 or risk/fit issue blocks main testing |

Do not treat thresholds as mechanical. Use judgment when a theme has unusually strong social or competitor evidence.

Evidence gates:

- P0 cannot rely only on `Index` or `Inference`.
- P0 needs at least one current-run retrieved source. For social heat or competitor dynamic claims, prefer channel-specific `Live Retrieval`; if only `Public Source` is available, mark confidence lower and explain the limitation.
- For login/profile-dependent channels, P0 social or competitor claims should be based on `Chrome Used` evidence where possible. If Chrome was blocked or unavailable, downgrade confidence or explain the compensating evidence.
- P1 can use one strong `Public Source` plus strong index fit, but must not be described as proven social/ad heat unless the platform was actually retrieved.
- P2/P3 can be based on weaker public-source or inference-led signals, as long as the evidence type is labeled.
- `Access Limited` should reduce confidence unless other retrieved sources compensate.

## Tie-Breakers

When themes have similar scores, prefer:

1. Better fit with current index user structure.
2. Stronger Web Quiz first-screen hook.
3. Easier visual/material production.
4. Lower compliance risk.
5. Clearer path to first-round test cells.

## Evidence Rules

- Distinguish observed facts from inference.
- Do not invent unavailable ad spend, search volume, conversion, or backend metrics.
- Keep source links with evidence.
- Mention login or access limitations.
- Use observation date for real-time research.
- Public information can count as evidence only when labeled `Public Source` and linked.
- Do not convert public-source evidence into a channel-specific heat claim. For example, an indexed article about chair yoga is not Facebook heat unless Facebook itself was retrieved.
