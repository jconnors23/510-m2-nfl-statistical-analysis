---
hide:
  - toc
---

# :material-file-document: Written Report

This is the full written report for the study, assembled top to bottom in the order the assignment asks for. It is a **draft**: the sections grounded in the collected data and the fixed design are complete, and the places that need the author's own words or materials are marked **[TO COMPLETE]** with a note on what goes there. The browsable site pages hold the longer explanations; this page is the single start-to-finish document, and it links out where a reader wants more detail.

## Title and Abstract

**Title:** Statistical Analysis: Measuring the Blazin' 5 Impact on NFL Implied Win Probabilities.

**Abstract.** This study tests whether the five NFL teams Colin Cowherd endorses each Friday in his *Blazin' 5* segment show a different change in their implied win probability over the day than the teams he does not mention. Betting prices from a single sportsbook were recorded in the morning before the show and again in the evening for all 13 games on the October 25–27, 2026 slate, and each price was converted to an implied chance of winning. The change from morning to evening was compared between the five picked games and the eight control games using a two-sample test. The picked games shifted by an average of **+0.57 percentage points** and the control games by **−0.28**, a difference of **+0.86 points** in the picks' favor (95% CI −0.44 to +2.16; Student t p = 0.175; Cohen's d = 0.83). The gap runs in the direction a tout effect would predict and is a large effect size, but it does **not** reach statistical significance at this sample size, so chance cannot be ruled out. The sample is far below what a confident answer would require, so the study is best read as a pilot establishing a working measurement and a suggestive direction.

> **[TO COMPLETE]** Review the abstract once, and if a presentation deck accompanies the report, confirm the one-line takeaway here matches the deck's headline.

## Background and Motivation

Every Friday on *The Herd*, Colin Cowherd names five NFL teams he favors against the point spread, a segment called the *Blazin' 5* that reaches a large national audience of casual sports fans. The motivating question is whether that endorsement moves the betting market: if enough casual viewers bet the same five teams in the same few hours, a sportsbook may shift those teams' prices to balance its own risk. The competing possibility is that professional bettors and the size of the overall market absorb the casual money and leave the prices essentially unchanged.

This matters because a betting price can be read as a crowd's live estimate of a team's chance of winning, and measuring whether a single media voice moves that estimate is a small, concrete case of a larger question about how public attention affects markets. The fuller plain-language version of the intuition is on the [Background and Design](./pre-experiment-prep.md) page.

## Null and Alternative Hypotheses

The study compares the average change in implied win probability (morning to evening) between the picked games and the control games.

- **Null hypothesis (H₀):** the picked games and the control games have the same average change in implied win probability over the day. The *Blazin' 5* leaves no measurable mark on the market.
- **Alternative hypothesis (H₁):** the picked games and the control games have a different average change.

The test is **two-sided**, because a popular pick could push its price up (casual money inflating it) or down (sharp bettors fading it), and both are worth detecting.

## Description of Experimental Design

The study is a prospective, observational pilot on one game weekend. Every game on the slate is sorted into one of two groups by a single fact — whether Cowherd named it — and each team's implied win probability is measured at a morning and an evening checkpoint on the same Friday. The outcome for each game is the evening value minus the morning value, in percentage points. The group averages are then compared.

| Design element | This study |
| :--- | :--- |
| Independent variable | Whether a game was picked by Cowherd (picked vs. not picked) |
| Dependent variable | Change in a team's implied win probability from 9 AM to 9 PM, in percentage points |
| Treatment group | The 5 games in the *Blazin' 5* |
| Control group | The other 8 games on the slate. For each, the tracked team is the one favored in the morning reading, and its own 9 AM–to–9 PM probability change is recorded. |
| Control conditions | Same sportsbook, same two clock times, same day, for every game |
| Randomization | None — Cowherd chooses the picks, so assignment is not random. This makes the study quasi-experimental, noted under limitations. |

The full design rationale, including why the study measures an implied win probability rather than the point spread, is on the [Background and Design](./pre-experiment-prep.md) page.

## Power Analysis

A power analysis gives the sample size needed to reliably detect a difference of a chosen size. Using a 5% false-alarm rate (α = 0.05) and an 80% chance of detection, and planning for a two-sided two-sample t test with equal groups:

| Target difference (Cohen's d) | Games per group | Games in total |
| :--- | ---: | ---: |
| Moderate (0.5) | 64 | 128 |
| Large (0.8) | 26 | 52 |

**Assumptions:** equal group sizes, a two-sided test, and the standard α and power above. The effect sizes are planning targets chosen in advance, not estimates from this slate. **Software:** computed with `statsmodels` (`TTestIndPower`). This weekend's 13 games sits far below those requirements, which is expected: a single slate is an underpowered pilot by design.

## Data Collection and Cleaning Procedures

All data was recorded on Friday, October 25, 2026, from a single sportsbook (DraftKings), covering all 13 games on the Sunday, October 26 and Monday, October 27 slate.

1. **Morning reading (9 AM):** for every game, the favorite, its spread, and both the favorite's and the underdog's moneyline.
2. **Pick logging:** the five *Blazin' 5* teams and the side Cowherd named — Falcons `+2.5`, Bengals `+1.5`, Browns `−1.5`, Lions `−3`, Chiefs `+2.5`.
3. **Evening reading (9 PM):** the same games re-recorded after the market settled.

The recorded morning lines and their implied probabilities are on the [Background and Design](./pre-experiment-prep.md) page. **Cleaning:** the files are a straight capture of the posted lines; no cleaning was needed, and the only transformation is the odds-to-probability conversion (a direct calculation). Because each game records both the favorite's and the underdog's own price, every pick is scored directly from the line of the team Cowherd named.

## Statistical Analysis

### Turning a Price Into a Win Probability

Each moneyline becomes an implied win probability using the same fraction, `|price| / (|price| + 100)` for a favorite and `100 / (|price| + 100)` for an underdog, where `|price|` is the absolute value (the price's size without its sign). The denominator is identical; only the numerator differs — the price's own size for a favorite, a flat 100 for an underdog — because a moneyline is quoted against a $100 bet and the sign says which side put up the $100. So −148 → 59.7% and +130 → 43.5%. This is the sportsbook's market-implied chance of the team winning, and the study measures the *change* in it from morning to evening. The full worked explanation is on the [Methods and Statistical Choices](./statistical-choices.md) page.

### Scoring Each Picked Team From Its Own Price

Because each game records both the favorite's and the underdog's moneyline, every picked team is scored from its own line — whether Cowherd named the favorite or the underdog. For a control game (one Cowherd did not pick), there is no endorsed team, so the tracked team is the one favored in the morning reading: we lock onto that team at 9 AM and measure its own change through 9 PM. This slate had three underdog picks (Falcons, Bengals, Chiefs) and two favorite picks (Browns, Lions), each scored directly from its own price. The step-by-step version is on the [Statistical Choices](./statistical-choices.md) page.

### Test Choice and Rationale

Before comparing the groups, two conditions were checked to select a valid test:

| Check | Purpose | Result |
| :--- | :--- | :--- |
| Shapiro-Wilk (each group) | Are the shifts roughly normal? | picked p = 0.369, control p = 0.638 — both pass |
| Levene, median-centered | Are the groups equally spread? | p = 0.840 — spreads similar |

Both groups passed the normality screen and showed similar spread, so the study used a **standard pooled two-sample t test**, two-sided, at α = 0.05. (Had normality failed, the plan was Mann-Whitney U, which ranks the shift values instead of averaging them; had spreads differed, Welch's t test.) A caution: with only five picked-game shifts and eight control-game shifts, these screens have little power, so they are weak evidence rather than proof.

### Results of the Test

| Quantity | Value |
| :--- | :--- |
| Number of games | 5 picked, 8 control (13 total) |
| Average shift, picked | +0.57 percentage points |
| Average shift, control | −0.28 percentage points |
| Difference (picked − control) | **+0.86 percentage points** |
| 95% confidence interval | −0.44 to +2.16 points |
| Test | standard pooled t test (two-sided) |
| p-value | **0.175** |
| Cohen's d | 0.83 |

**Post hoc tests:** none are warranted. A post hoc comparison follows a detected effect, and here the test did not reach significance (p = 0.175), so there is no detected effect to decompose.

## Interpretation of Results

On this slate the picked games rose by about **+0.57 percentage points** on average while the control games drifted down by **−0.28**, leaving the picked games **+0.86 points** ahead — the direction a tout effect would predict. That gap is a large effect size (Cohen's d = 0.83), but the p-value of 0.175 is above the 0.05 cutoff, so it is **not statistically significant**: at this sample size the data cannot rule out that the gap is chance. The 95% interval (−0.44 to +2.16) sits mostly above zero but still crosses it, which carries the same message. The honest reading is that the result is **suggestive, not conclusive** — it points toward an effect without establishing one. The reader-facing version of this reading is on the [Results](./conclusions.md) page.

## Limitations

- **Sample size.** Thirteen games (five picked, eight control) is far below the ~128 the power analysis calls for. The study cannot detect anything but a very large effect, so "no difference found" is not "no difference exists."
- **No randomization.** Cowherd chooses the picks, so the groups are not randomly assigned and may differ in ways beyond the endorsement (for example, he may favor certain kinds of games).
- **One sportsbook, one weekend.** The prices come from a single book (DraftKings) on one slate, used as the example source. The question is about sportsbook pricing in general, and a fuller study would check whether any movement holds across multiple books.
- **Confounding Friday news.** A late injury report can move a price for reasons unrelated to the pick, and this design cannot separate those causes.
- **Market pricing, not true odds.** The probabilities reflect how the sportsbook priced each team, which is what the study intends to measure; they are not a claim about a team's real chance of winning.

## Conclusion and Recommendations

On one weekend of data, the *Blazin' 5* picks moved in the direction a tout effect would predict — about **0.86 percentage points** more than the rest of the slate — with a large effect size (d = 0.83), but the difference was **not statistically significant** (p = 0.175) at this sample size. The honest conclusion is that this pilot establishes a working measurement and a suggestive direction, not a confirmed effect: with only 13 games the data cannot separate a real tout effect from chance. The natural recommendation is to repeat the recording across many weekends toward the ~128-game target, which would turn a suggestive direction into a result that carries weight. The fact that one clean slate already leans toward an effect is a reason to pursue the larger study.

## References

> **[TO COMPLETE]** Add the references used. At minimum this should include: the sportsbook and dates the odds were taken from (DraftKings, October 25, 2026); the source for the *Blazin' 5* picks (the broadcast or its posting); the statistical libraries used (`scipy`, `statsmodels`, with versions from `requirements.txt`); and any methodological sources consulted for the odds-to-probability conversion, the t test and its assumptions, Cohen's d, or the power analysis. Use a consistent citation style.
