# 510-m2-nfl-statistical-analysis

Does a famous sports-media personality's weekly NFL picks actually move the betting market? This project tests that one idea. Each Friday, Colin Cowherd names five teams he favors against the spread in a segment called the *Blazin' 5*. We record each team's implied chance of winning in the morning before his show and again that evening, then check whether the games he picked shifted differently from the games he left alone.

Because the data is a single weekend of hand-recorded odds, this is a pilot: a first look to see whether the measurement works and whether the effect is worth a larger study, not a final verdict.

## What This Project Contains

| Part | Where |
| :--- | :--- |
| Background, design, hypotheses, data | [Background and Design](./docs/pre-experiment-prep.md) |
| Formulas and every statistical choice | [Methods and Statistical Choices](./docs/statistical-choices.md) |
| The analysis code, explained top to bottom | [Notebook Walkthrough](./docs/notebook-walkthrough.md) |
| The result, interpretation, and limits | [Results and Interpretation](./docs/conclusions.md) |
| The full formal write-up | [Written Report](./docs/report.md) |
| Glossary of every stat term + sources | [Glossary and References](./docs/references.md) |
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

The full write-up lives in the documentation. Read the site in this order: **Overview → Background and Design → Methods and Statistical Choices → Notebook Walkthrough → Results and Interpretation → Written Report → Glossary and References.**

## Project Layout

```text
510-m2/
├── README.md                     # this file, the front door
├── requirements.txt              # pinned docs + analysis dependencies
├── data/                         # the recorded odds and picks (CSV)
│   ├── odds-before-9am.csv
│   ├── odds-after-9pm.csv
│   └── picks-chosen.csv
├── analysis/                     # the comparison code
│   ├── primary-comparison.py     # reads data/, computes the shifts and the test
│   └── primary-comparison.ipynb  # presents what the script computed
├── .github/
│   └── workflows/
│       └── deploy-docs.yml       # builds + publishes the site to GitHub Pages
├── docs/                         # the full write-up (served as a site)
│   ├── index.md
│   ├── pre-experiment-prep.md    # Background and Design
│   ├── statistical-choices.md    # Methods and Statistical Choices
│   ├── notebook-walkthrough.md   # Notebook Walkthrough
│   ├── conclusions.md            # Results and Interpretation
│   ├── report.md                 # Written Report
│   ├── references.md             # Glossary and References
│   └── stylesheets/
│       └── extra.css
└── mkdocs.yml                    # documentation site config
```

## Reading the Docs as a Site

The published site lives at **https://jconnors23.github.io/510-m2-nfl-statistical-analysis/**. A GitHub Actions workflow (`.github/workflows/deploy-docs.yml`) rebuilds and redeploys it on every push to `main`.

Every page under `docs/` is also plain Markdown and reads fine on its own or on the repository host. The pages render as an [MkDocs](https://www.mkdocs.org/) Material site, configured by `mkdocs.yml` in the project root.

### Building It Locally

You will need Python 3.11 or newer. Dependencies are pinned in `requirements.txt`.

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

The two external sources the study drew on. A full glossary of every statistical term, plus the software tools used, is on the [Glossary and References](./docs/references.md) page.

- **Colin Cowherd's *Blazin' 5* picks** — *The Herd with Colin Cowherd* (video). The five picks and the side named for each were logged from this broadcast.
  <https://www.youtube.com/watch?v=fuRkH_gVIwE&t=443s>
- **NFL betting odds (moneylines), provided by DraftKings** — ESPN NFL Odds. Morning and evening moneylines for every game were recorded from here.
  <https://www.espn.com/nfl/odds>
