---
hide:
  - toc
---

# :material-clipboard-text: Background and Design

This page covers why the study exists, the two competing ideas it tests, the hypotheses, the experimental design, the sample-size reasoning, and how the data was collected — everything up to the analysis itself. The analysis and its formulas are on [Methods and Statistical Choices](./statistical-choices.md); the numbers are on [Results and Interpretation](./conclusions.md).

!!! success "Data collection complete"
    A full weekend of data was collected on **Friday, October 25, 2026** — morning prices, evening prices, and the five *Blazin' 5* picks — and checked: 13 games in both the morning and evening files (matching game lists, no missing prices), both the favorite's and the underdog's moneyline recorded at each time, and all five picks logged with a side that matches the game's favorite or underdog correctly.

## The Question

Every Friday on his show *The Herd*, Colin Cowherd names five NFL teams he favors against the point spread. The segment is called the *Blazin' 5*, and it reaches a large national audience of casual sports fans, many of whom also place small bets. The question is direct: **when Cowherd endorses a team, does the betting market move in that team's favor more than it would have on its own?**

A betting price can be read as a team's implied chance of winning. If a large number of casual bettors follow Cowherd's picks within the same few hours, a sportsbook may adjust those prices to balance its own risk, and the picked teams would then show a larger shift in their implied chance of winning over the day than teams he did not mention.

## Why It Is Interesting

There are two competing stories, and the study is set up to tell them apart.

- **The crowd moves the price.** Millions of casual viewers act on the same five picks within the same few hours. That concentrated, one-directional betting could push the price for those teams noticeably, even though the underlying game has not changed.
- **The market absorbs it as noise.** Professional bettors and the size of the overall betting pool may outweigh the casual money, leaving the price essentially where it would have been. In this case, a celebrity pick is one small input among many.

Neither story is obviously correct ahead of time, which is what makes the question worth a real measurement rather than a guess.

## Null and Alternative Hypotheses

The study measures, for each team, the change in its implied chance of winning from morning to evening, then compares the average change for the picked teams against the average change for the teams Cowherd did not mention.

- **Null hypothesis:** the picked games and the unpicked games have the same average change in implied win probability over the day. The *Blazin' 5* leaves no measurable mark on the market.
- **Alternative hypothesis:** the picked games and the unpicked games have a different average change.

The test looks for a difference **in either direction**, because the crowd could inflate a picked team's price or sharp bettors could push back against a popular pick — both outcomes are plausible and both would be worth reporting.

## The Experimental Design

This is a prospective, observational pilot on one game weekend. Every game on the slate is sorted into one of two groups by a single fact — whether Cowherd named it — and each tracked team's implied win probability is measured at a morning and an evening checkpoint on the same Friday. The outcome for each game is the evening value minus the morning value, in percentage points, and the group averages are compared.

| Group | What it contains | Size this slate |
| :--- | :--- | :--- |
| Picked games | The five games Cowherd endorsed in the *Blazin' 5* | 5 |
| Control games | The rest of the slate he did not mention | 8 |

For a picked game, we track the exact team Cowherd endorsed. For a control game, we track the team that was favored in the morning reading: we see which team is the favorite at 9 AM, lock onto that team, and measure its own change through the evening. Choosing the morning favorite before any movement happens keeps the choice of which team to follow independent of the movement we are measuring, and gives both groups a consistent rule.

| Design element | This study |
| :--- | :--- |
| Independent variable | Whether a game was picked by Cowherd (picked vs. not picked) |
| Dependent variable | Change in a team's implied win probability from 9 AM to 9 PM, in percentage points |
| Control condition | The unpicked games on the same slate, same two clock times, same day, same sportsbook |
| Randomization | None — Cowherd chooses the picks, so assignment is not random. This makes the study quasi-experimental, noted as a limitation on the Results page. |

### Why a Win Probability Instead of the Point Spread

The study measures the shift in implied win probability rather than the point spread because the probability is easier to track. A point spread only moves in half-point steps (from −3 to −3.5, for example), so a small market shift does not show up until it is big enough to jump a whole half-point. The implied win probability moves in much finer fractional increments, so it registers the small day-to-day movements this study is trying to catch — and a fine-grained percentage is a cleaner number to average and run statistics on.

## Power Analysis

A power analysis gives the sample size needed to reliably detect a difference of a chosen size. Using a 5% false-alarm rate (α = 0.05) and an 80% chance of detection, for a two-sided two-sample t test with equal groups:

| Target difference (Cohen's d) | Games per group | Games in total |
| :--- | ---: | ---: |
| Moderate (0.5) | 64 | 128 |
| Large (0.8) | 26 | 52 |

These were computed with `statsmodels`. The effect sizes are planning targets chosen in advance, not estimates from this slate. This weekend's 13 games sits far below those requirements, which is expected: a single slate is an **underpowered pilot by design**, meant to prove the measurement works and hint at a direction, not to settle the question.

## Data Collection

All recording happened on Friday, October 25, 2026, from a single sportsbook (DraftKings), across the 13-game Sunday, October 26 and Monday, October 27 slate.

1. **Morning reading (9 AM).** For each game: the favorite, its spread, and both the favorite's and the underdog's moneyline.
2. **Pick logging.** The five *Blazin' 5* picks and the side named: Falcons `+2.5`, Bengals `+1.5`, Browns `−1.5`, Lions `−3`, Chiefs `+2.5`.
3. **Evening reading (9 PM).** The same games re-recorded after the market settled.

Because each game records both the favorite's and the underdog's own price, every pick is scored directly from the line of the team Cowherd named — three underdogs (Falcons, Bengals, Chiefs) and two favorites (Browns, Lions). **Cleaning:** the files are a straight capture of the posted lines; no cleaning was needed, and the only transformation is the odds-to-probability conversion, covered on [Methods and Statistical Choices](./statistical-choices.md).

## The Morning Lines

Each row is one game's favorite, with the spread and moneyline as posted and the implied win probability it works out to.

| Game | Favorite | Spread | Moneyline | Implied win probability |
| :--- | :--- | ---: | ---: | ---: |
| Steelers @ Saints (London) | Steelers | -3 | -175 | 63.6% |
| Browns @ Titans | Browns | -1.5 | -130 | 56.5% |
| Dolphins @ Jets | Jets | -4.5 | -225 | 69.2% |
| 49ers @ Falcons | 49ers | -2.5 | -148 | 59.7% |
| Bengals @ Ravens | Ravens | -1.5 | -118 | 54.1% |
| Colts @ Vikings | Vikings | -6.5 | -278 | 73.5% |
| Giants @ Texans | Texans | -10.5 | -520 | 83.9% |
| Bucs @ Panthers | Panthers | -3 | -162 | 61.8% |
| Broncos @ Cardinals | Broncos | -4.5 | -230 | 69.7% |
| Rams @ Raiders | Rams | -3.5 | -192 | 65.8% |
| Packers @ Lions | Lions | -3 | -170 | 63.0% |
| Chiefs @ Seahawks | Seahawks | -3 | -142 | 58.7% |
| Cowboys @ Eagles | Cowboys | -4.5 | -218 | 68.6% |

The 13 favorites span a range from the **Ravens at 54.1%** (a near-coin-flip game) up to the **Texans at 83.9%** (a heavy favorite). That spread matters: a team already priced in the low 80s has less room to move than a team near 50%.
