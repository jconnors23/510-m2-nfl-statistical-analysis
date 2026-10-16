---
hide:
  - toc
---

# Experiment Preparation

This document is the planning sheet for the study. It walks through each item the written report needs at the design stage: the title, why the study matters, the two competing claims being tested, how the experiment is set up, the variables and controls, and how the data will be gathered. The power analysis and any data cleaning are left for later, and this document says why.

The reader-facing write-up of the same material lives across the rest of this site; this sheet is the short, one-page planning version, and it links out to the page that owns each topic in full.

!!! note "Status: baseline collected"
    The morning baseline reading was recorded on **Friday, October 16, 2026 at 9:00 AM**, covering the Sunday, October 18 and Monday, October 19 slate. The recorded lines are on the [Baseline Readings](./baseline-readings.md) page. This is the first of the planned snapshots: the *Blazin' 5* picks and the evening reading have not been logged yet, so no comparison has been run.

## Title

**Statistical Analysis: Measuring the Blazin' 5 Impact on NFL Implied Win Probabilities.**

A pilot experiment testing whether the five weekly NFL picks that Colin Cowherd announces on his show move the betting market's implied chance of each team winning.

## Background and Motivation

Every Friday on his show *The Herd*, Colin Cowherd names five NFL teams he favors against the point spread, in a segment called the *Blazin' 5*. The show reaches a large national audience of casual sports fans, many of whom also place small bets. Betting markets set a price for each team that can be read as that team's implied chance of winning, and sportsbooks adjust those prices as money comes in.

The motivation is a simple question with two plausible answers. If a flood of casual bettors follows Cowherd's picks within the same few hours, the prices for those teams could move noticeably even though nothing about the games changed. On the other hand, professional bettors and the sheer size of the overall betting pool might absorb that casual money and leave the prices essentially where they started. The study is set up to tell these two stories apart with a real measurement rather than a guess.

For the fuller version of the intuition, see [Key Question](./the-question.md).

## Null and Alternative Hypotheses

The study measures, for each team, the change in its implied chance of winning from the morning (before the show) to the evening (after the show). It then compares the average change for the picked teams against the average change for the teams Cowherd did not mention.

- **Null hypothesis:** the picked games and the unpicked games have the same average change in implied win probability over the day. Cowherd's segment leaves no measurable mark on the market.
- **Alternative hypothesis:** the picked games and the unpicked games have a different average change in implied win probability over the day.

The test looks for a difference in either direction, not just one. The picked teams could move up if casual money inflates them, or down if sharp bettors push back against a popular pick, and both outcomes would be worth reporting.

## Description of Experimental Design

This is a prospective, live pilot. On one game weekend we observe the whole slate of NFL games and sort each one into a treated group or a control group based on a single fact: whether Cowherd named it.

- **Treated group** — the five games endorsed in that week's *Blazin' 5* (5 games).
- **Control group** — the rest of the slate that Cowherd did not mention. This weekend's baseline holds 13 games in total, so once the five picks are logged the control group will be the remaining 8.

For every team we track, we record its implied chance of winning twice on Friday: once in the morning before the show airs, and once in the evening after the betting has settled. The measurement for each team is the evening value minus the morning value. We then compare the average of those changes between the two groups.

The design is a quasi-experiment rather than a controlled lab study: we cannot randomly assign which games Cowherd picks, so the groups form from his real choices. This is noted as a limitation below.

For the full design, including why the study uses an implied win probability instead of the point spread, see the [Planned Experiment](./the-experiment.md).

## Independent and Dependent Variables, Control Conditions, Randomization

| Item | What it is |
| :--- | :--- |
| Independent variable | Whether a game was picked by Cowherd (picked or not picked). This is the single thing that separates the two groups. |
| Dependent variable | The change in a team's implied chance of winning from morning to evening on the same Friday, measured as a percentage. |
| Control condition | The unpicked games on the same slate, measured over the same hours on the same day, from the same sportsbook. They stand in for "what normal market drift looks like without a pick." |
| Randomization | None. Cowherd chooses which games to pick, so the groups are not randomly assigned. The study is observational on that point, which is a known limitation of a pilot like this. |

To keep the two groups comparable, every price comes from a single sportsbook, and both the morning and evening readings are taken at fixed times for every game.

## Power Analysis

**Not filled in yet.** A formal power analysis — the calculation of how many games are needed to reliably detect an effect of a given size — belongs with the statistical testing plan, which comes once the measurement approach is locked. It is deliberately left out of this planning sheet for now.

What is already clear, and will frame that later analysis, is that this weekend's 13 games is a small sample. A moderate effect would need on the order of a full season of weekends to detect confidently, so this first run is understood as an underpowered pilot. The exact numbers, the assumed effect size, and the software used will be added when the power analysis is done.

## Assumptions, Calculations, and Software

The planning rests on a few stated assumptions, to be checked when the data is in:

- The morning reading, taken before the show airs, is a fair baseline that is not already reacting to the picks.
- The picked and unpicked games are comparable enough that, absent a tout effect, their prices would drift by similar amounts over the day.
- Prices from a single sportsbook are a reasonable stand-in for the broader market for this pilot.

The only calculation needed at this stage is converting betting odds into an implied chance of winning. A favorite's odds carry a negative number; its win chance is the size of that number divided by the same size plus 100 (for example, -150 becomes 150 ÷ 250, or 60 percent). An underdog's odds carry a positive number; its win chance is 100 divided by that number plus 100 (for example, +130 becomes 100 ÷ 230, or about 43 percent).

The analysis will be done in Python. The statistical tools (for the hypothesis test, effect size, and the later power analysis) will come from the `scipy` and `statsmodels` libraries. No results have been computed yet.

## Data Collection and Cleaning Procedures

**Collection.** All recording happens on Friday around the broadcast. We choose one sportsbook and stay with it for the whole weekend so every number is comparable.

1. **Morning baseline (9 AM) — done.** Recorded on Friday, October 16, 2026, covering 13 games on the Sunday, October 18 and Monday, October 19 slate. Each row holds the favored team, its spread, and its moneyline. The recorded lines are on the [Baseline Readings](./baseline-readings.md) page.
2. **Pick logging (around 1 PM) — pending.** Note the five teams Cowherd endorses on the show.
3. **Evening reading (around 9 PM) — pending.** Record the odds again after the market has settled.

For the recorded fields and the odds-to-probability conversion in full, see [Data Collection](./data-collection.md).

**Cleaning.** There is **no cleaning step yet**. The baseline file is a straight capture of the lines as posted. The only transformation planned is the odds-to-win-probability conversion described above, which is a direct calculation rather than a cleanup. Once the picks and the evening reading are added, this section will cover any genuine cleaning needed, such as handling a game that is postponed, a line that is pulled off the board, or a late injury report that moves a price for reasons unrelated to the picks.
