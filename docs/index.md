---
hide:
  - toc
---

<div class="field-hero" markdown="1">
  <span class="field-hero__kicker">Pilot Statistical Experiment</span>
  <div class="field-hero__title">Measuring the Blazin' 5 Effect</div>
  <p class="field-hero__sub">When a national TV personality names five NFL teams to bet, does the market's implied win probability move in response, or absorb the picks as noise?</p>
</div>

<div class="stat-row" markdown="1">
  <div class="stat-chip"><span class="stat-chip__num">13</span><span class="stat-chip__label">Games this slate</span></div>
  <div class="stat-chip"><span class="stat-chip__num">5</span><span class="stat-chip__label">Picked games</span></div>
  <div class="stat-chip"><span class="stat-chip__num">8</span><span class="stat-chip__label">Control games</span></div>
  <div class="stat-chip"><span class="stat-chip__num">+0.86pp</span><span class="stat-chip__label">Picked edge (n.s.)</span></div>
</div>

# Overview

This project tests whether a prominent sports-media personality's public picks move the betting market. It focuses on one weekly segment, Colin Cowherd's *Blazin' 5*, in which he names five teams he favors against the point spread, and measures whether the games he picks shift differently from the games he does not, over the same few hours.

The study produces a single comparison: the average change in each team's implied chance of winning for the picked games versus the control games, together with a statistical test of whether that difference is distinguishable from chance. It rests on a small set of odds recorded by hand on one game weekend, so it is framed as a pilot — a first measurement to establish the method and indicate whether the effect warrants a larger study.

## What Each Page Covers

The pages below are ordered as a reading path. The first three walk through the study part by part; the [Written Report](./report.md) then consolidates everything into the formal deliverable.

| Page | Contents |
| :--- | :--- |
| [Background and Design](./pre-experiment-prep.md) | The question, the two competing ideas, the hypotheses, the design, the power analysis, and the data collected |
| [Methods and Statistical Choices](./statistical-choices.md) | The odds-to-probability formulas and every statistical decision, in plain language |
| [Notebook Walkthrough](./notebook-walkthrough.md) | The analysis code explained top to bottom, section by section |
| [Results and Interpretation](./conclusions.md) | The numbers, how to read them honestly, the limits, and how to defend the study |
| [Written Report](./report.md) | The full study, top to bottom, in the report's required order |
| [Glossary and References](./references.md) | Every statistical term defined in plain language, plus the data sources |

## The Study at a Glance

```mermaid
flowchart LR
    A[Record odds<br/>Friday 9 AM] --> B[Cowherd names<br/>his 5 picks]
    B --> C[Record odds<br/>Friday 9 PM]
    C --> D[Convert odds to<br/>win probability]
    D --> E[Compare picked<br/>vs. unpicked games]
    E --> F[Statistical test:<br/>real shift or noise?]
```
