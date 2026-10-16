# 510-m2-nfl-statistical-analysis

> **Status: pre-experiment — baseline collected.** The morning baseline odds were recorded on Friday, October 16, 2026. The *Blazin' 5* picks and the evening reading are not in yet, so no comparison has been run. This commit captures the design and the baseline data before the rest is collected.

Does a famous sports-media personality's weekly NFL picks actually move the betting market? This project tests that one idea. Each Friday, Colin Cowherd names five teams he favors against the spread in a segment called the *Blazin' 5*. The plan is to record each team's implied chance of winning in the morning before his show and again that evening, then check whether the games he picked shifted differently from the games he left alone.

Because the data is a single weekend of hand-recorded odds, this is a pilot: a first look to see whether the measurement works and whether the effect is worth a larger study, not a final verdict.

## Where the Project Stands

| Stage | State |
| :--- | :--- |
| Design and hypotheses | Done — see [Experiment Preparation](./docs/pre-experiment-prep.md) |
| Morning baseline odds (9 AM) | Done — 13 games, see [Baseline Readings](./docs/baseline-readings.md) |
| Blazin' 5 picks logged | Not yet |
| Evening reading (9 PM) | Not yet |
| Statistical test and results | Not yet — see [Results](./docs/conclusions.md) |

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
                   compare picked vs. unpicked games
                              |
                   statistical test: real shift or noise?
```

## Where to Read Next

The full write-up lives in the documentation. Read these in order.

| Page | What it covers |
| :--- | :--- |
| [Overview](./docs/index.md) | What the study does and what it produces |
| [Experiment Preparation](./docs/pre-experiment-prep.md) | One-page planning summary of every design item |
| [Key Question](./docs/the-question.md) | Why the "tout effect" is worth testing |
| [Planned Experiment](./docs/the-experiment.md) | The groups, the measurement, and the hypotheses |
| [Data Collection](./docs/data-collection.md) | What gets recorded and how odds become a win probability |
| [Baseline Readings](./docs/baseline-readings.md) | The morning odds collected so far, with implied win probabilities |
| [Results](./docs/conclusions.md) | How to read the outcome and its limits |

## Project Layout

```text
510-m2/
├── README.md                 # this file, the front door
├── requirements.txt          # pinned docs-site dependencies
├── blazing_five_pre_exp_data # raw morning baseline odds (tab-separated)
├── .github/
│   └── workflows/
│       └── deploy-docs.yml   # builds + publishes the site to GitHub Pages
├── docs/                     # the full write-up (served as a site)
│   ├── index.md
│   ├── pre-experiment-prep.md
│   ├── the-question.md
│   ├── the-experiment.md
│   ├── data-collection.md
│   ├── baseline-readings.md
│   ├── conclusions.md
│   └── stylesheets/
│       └── extra.css
└── mkdocs.yml                # documentation site config
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
