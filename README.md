# 510-m2-nfl-statistical-analysis

Does a famous sports-media personality's weekly NFL picks actually move the betting market? This study tests that one idea. Each Friday, Colin Cowherd names five teams he favors against the spread in a segment called the *Blazin' 5*. For one Week 7 slate, we recorded each team's implied chance of winning on Friday morning before his show and again that evening, then checked whether the games he picked shifted differently from the games he left alone.

Because the data is a single weekend of 13 games, this is a pilot — a first look to see whether the measurement works and whether the effect is worth a larger study, not a final verdict. **The result:** the picked games moved about 0.86 percentage points more than the rest, in the direction an endorsement effect would predict, but the difference was not statistically significant (p = 0.175) and is small enough that it may not matter in practice even if real. The honest read is a direction worth a larger study, not a confirmed effect.

> **Start here: the [Full Report](./docs/report.md)** is the complete study, read start to finish, and answers most questions on its own.
>
> **Presentation: [Josiah_Connors_M2_Presentation.pdf](./Josiah_Connors_M2_Presentation.pdf)** is the slide deck, or [watch the presentation](https://www.youtube.com/watch?v=DD7weJ0z4f8).
>
> **How it was built: the [AI Design Manifest](./ai-design-manifest.md)** documents which AI interface drove each stage of the work.

## What This Study Contains

| Part | Where |
| :--- | :--- |
| The complete study, start to finish (primary deliverable) | [Full Report](./docs/report.md) |
| The presentation slide deck | [Josiah_Connors_M2_Presentation.pdf](./Josiah_Connors_M2_Presentation.pdf) |
| The recorded presentation (video) | [Watch on YouTube](https://www.youtube.com/watch?v=DD7weJ0z4f8) |
| Every number worked step by step | [Win % Calculation](./docs/calculation.md) |
| The analysis code, explained top to bottom | [Notebook Walkthrough](./docs/notebook-walkthrough.md) |
| Data sources and a glossary of terms | [References and Appendix](./docs/references.md) |
| Which AI tool was used at each stage | [AI Design Manifest](./ai-design-manifest.md) |
| Reproducible analysis code | `analysis/` |

## How It Works

```text
  Friday 9 AM            Friday ~1 PM           Friday 9 PM
  record all odds  -->   Cowherd names 5   -->  record all odds
                         picks on air
        |                                             |
        +---------------------------------------------+
                              |
                   convert odds to win probability
                              |
                   compare picked vs. control games
                              |
                   statistical test: real shift or noise?
```

## Where to Read Next

After the [Full Report](./docs/report.md), go to the page that matches what you want:

- To **see the code** that produces the numbers → [Notebook Walkthrough](./docs/notebook-walkthrough.md)
- To **check any number step by step**, from a betting price to the final result → [Win % Calculation](./docs/calculation.md)
- To **look up a term** (p-value, Cohen's d, power analysis, the tests) or find the **data sources** → [References and Appendix](./docs/references.md)
- To see **which AI interface drove each stage** → [AI Design Manifest](./ai-design-manifest.md)

## Repository Layout

```text
510-m2/
├── README.md                          # this file, the front door
├── Josiah_Connors_M2_Presentation.pdf # the presentation slide deck
├── ai-design-manifest.md              # which AI tool was used at each stage
├── requirements.txt                   # pinned docs + analysis dependencies
├── data/                              # the recorded odds and picks (CSV)
│   ├── odds-before-9am.csv
│   ├── odds-after-9pm.csv
│   └── picks-chosen.csv
├── analysis/                          # the comparison code
│   ├── primary-comparison.py          # reads data/, computes the shifts and the test
│   └── primary-comparison.ipynb       # presents what the script computed
├── .github/
│   └── workflows/
│       └── deploy-docs.yml            # builds + publishes the site to GitHub Pages
├── docs/                              # the full write-up (served as a site)
│   ├── index.md                       # Overview
│   ├── report.md                      # Full Report (primary deliverable)
│   ├── calculation.md                 # Win % Calculation (every number step by step)
│   ├── notebook-walkthrough.md        # Notebook Walkthrough
│   ├── references.md                  # References and Appendix (glossary)
│   └── stylesheets/
│       └── extra.css
└── mkdocs.yml                         # documentation site config
```

## Reading the Docs as a Site

The published site lives at **https://jconnors23.github.io/510-m2-nfl-statistical-analysis/**. A GitHub Actions workflow (`.github/workflows/deploy-docs.yml`) rebuilds and redeploys it on every push to `main`.

Every page under `docs/` is also plain Markdown and reads fine on its own or on the repository host. The pages render as an [MkDocs](https://www.mkdocs.org/) Material site, configured by `mkdocs.yml` in the repository root.

### Building It Locally

You will need Python 3.12 or newer (the pinned `numpy` requires it). Dependencies are pinned in `requirements.txt`.

Create and activate a virtual environment:

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

Install the pinned dependencies:

```bash
pip install -r requirements.txt
```

Preview the site locally at http://127.0.0.1:8000:

```bash
mkdocs serve
```

Render the static site into `site/`:

```bash
mkdocs build
```

## References

The two external sources the study drew on, plus an appendix glossary of every statistical term, are on the [References and Appendix](./docs/references.md) page.

- **Colin Cowherd's *Blazin' 5* picks** — *The Herd with Colin Cowherd* (video). The five picks and the side named for each were logged from this broadcast.
  <https://www.youtube.com/watch?v=fuRkH_gVIwE&t=443s>
- **NFL betting odds (moneylines), provided by DraftKings** — ESPN NFL Odds. Morning and evening moneylines for every game were recorded from here.
  <https://www.espn.com/nfl/odds>
