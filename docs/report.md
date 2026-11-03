---
hide:
  - toc
---
## I. Title and Abstract

**Title:** NFL Statistical Analysis: Measuring the Blazin' 5 Effect on Implied Win Probability.

**Abstract.** This study tests whether the five NFL teams Colin Cowherd endorses each Friday in his *Blazin' 5* segment show a different change in their implied win probability than the teams he does not mention. It is a **pilot** — a small, deliberately scoped first run on one NFL week, meant to prove the measurement works and signal whether the effect is worth a larger study. Betting prices from a single sportsbook were recorded on Friday, October 23, 2026, in the morning before the show and again in the evening, for all 13 games on the following Sunday, October 25 (Week 7), and each price was converted to an implied win probability. The change from morning to evening was compared between the five picked games and the eight control games using a two-sided two-sample Student's t-test. The picked games shifted by an average of **+0.57 percentage points** and the control games by **−0.28**, a difference of **+0.86 percentage points** in the endorsed teams' favor (95% CI −0.44 to +2.16; Student t p = 0.175; Cohen's d = 0.83). The gap runs in the direction an endorsement effect would predict — picked teams gaining more implied win chances than the non-picked teams — but it does **not** reach statistical significance at this sample size, and 0.86 percentage points may be too small to matter much in practice even if it were real. The sample size is far below what a confident answer would require, so the study is best read as a pilot that establishes a working measurement rather than any finding about the picks.

## II. Background and Motivation

Every Friday on *The Herd*, Colin Cowherd names five NFL teams he favors against the point spread, a segment called the *Blazin' 5* that reaches a large national audience of casual sports fans. The motivating question is whether that endorsement moves the betting market: if enough viewers act on the same five picks, the prices on those teams could move in response. This matters because a betting price can be read as a crowd's live estimate of a team's chance of winning, and measuring whether a single media voice moves that estimate is a small, concrete case of a larger question about how public attention impacts markets.

## III. Null and Alternative Hypotheses

The study compares the average change in implied win probability (morning to evening) between the picked games and the control games.

- **Null hypothesis (H₀):** the picked games and the control games have the same average change in implied win probability over the day. The *Blazin' 5* leaves no measurable mark on the market.
- **Alternative hypothesis (H₁):** the picked games and the control games have a different average change in implied win probability over the day. The *Blazin' 5* leaves a measurable mark on the market — the endorsed teams' prices move differently from the rest of the slate, whether that movement is upward or downward.

The test is **two-sided**, because a popular pick could move an endorsed team's price up or down.

## IV. Description of Experimental Design

The study is a prospective, observational **pilot** on one NFL week, and it is **quasi-experimental** by nature. Both labels matter for reading the results, so they are stated plainly here:

- **Pilot.** The study runs the full measurement once, on a single slate of 13 games, to show that the method works end to end and to see which way the effect points. A pilot is not expected to settle the question — the [power analysis](#v-power-analysis) below shows this slate is far too small for that — so its job is to validate the measurement and justify (or not) a larger follow-up.
- **Quasi-experimental.** In a true experiment the researcher assigns subjects to groups at random. Here no one does: the two groups form on their own because Cowherd, not the study, decides which five games are picked. That lack of random assignment is what makes the design quasi-experimental, and it means the picked and control games may differ in ways beyond the endorsement (for example, if Cowherd tends to pick close games). The study can therefore detect an *association* — whether the picked games moved differently from the rest — but not *causation*, that the picks themselves drove the difference.

Every game on the slate is sorted into one of two groups by a single fact — whether Cowherd named it — and each team's implied win probability is measured at a morning and an evening checkpoint on the same Friday. The outcome for each game is the evening value minus the morning value, in percentage points. The group averages are then compared.

| Design element | This study |
| :--- | :--- |
| Independent variable | Whether a game was picked by Cowherd (picked vs. not picked) |
| Dependent variable | Change in a team's implied win probability from 9 AM to 9 PM, in percentage points |
| Treatment group | The 5 games in the *Blazin' 5* |
| Control group | The other 8 games on the slate. For each, the tracked team is the one favored in the morning reading, and its own 9 AM–to–9 PM probability change is recorded. |
| Control conditions | Same sportsbook, same day morning and evening, each game |

The study uses implied win probability as its measure because it is a single, directly calculable number — a plain percentage chance of winning — that is easy to compare from morning to evening. A point spread or a raw moneyline is harder to read at a glance and does not translate as cleanly into "how likely is this team to win according to the public".

## V. Power Analysis

A power analysis gives the sample size needed to reliably detect a difference of a chosen size. The target effect is a **moderate** difference, Cohen's d = 0.5 — the conventional benchmark effect size to power for. Using a 5% false-alarm rate (α = 0.05) and an 80% chance of detection, for a two-sided two-sample Student's t-test with equal groups:

| Target difference (Cohen's d) | Games per group | Games in total |
| :--- | ---: | ---: |
| Moderate (0.5) | 64 | 128 |

**Assumptions:** equal group sizes, a two-sided test, and the standard α and power above. **Software:** computed with `statsmodels` (`TTestIndPower`). This weekend's 13 games sits far below the ~128 required, which is expected: a single slate is an underpowered pilot by design.

## VI. Data Collection and Cleaning Procedures

All data was recorded on Friday, October 23, 2026, from a single sportsbook (DraftKings), covering all 13 games on the following Sunday, October 25 (Week 7) slate.

1. **Morning reading (9 AM):** for every game, the favorite, its spread, and both the favorite's and the underdog's moneyline.
2. **Pick logging:** the five *Blazin' 5* teams and the side Cowherd named — Falcons `+2.5`, Bengals `+1.5`, Browns `−1.5`, Lions `−3`, Chiefs `+2.5`.
3. **Evening reading (9 PM):** the same games re-recorded after the market settled.

**Cleaning:** the recorded values were used exactly as posted — none were corrected, imputed, or dropped. The only cleaning was light formatting to make the hand-entered fields consistent: blank rows removed, team names read from the spread text and lower-cased (entries were typed with mixed capitalization), and the picks trimmed of their "to cover" label and stray spaces before being matched to their games. The one real transformation is the odds-to-probability conversion.

The 13 morning favorites and the implied win chance each line works out to:

| Game | Favorite | Spread | Moneyline | Implied win chance |
| :--- | :--- | ---: | ---: | ---: |
| Steelers @ Saints (Paris) | Steelers | -3 | -175 | 63.6% |
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

## VII. Statistical Analysis

### Turning a Price Into a Win Probability

Each moneyline becomes an implied win probability: `|price| / (|price| + 100)` for a favorite and `100 / (|price| + 100)` for an underdog, where `|price|` is the number without its sign. So −148 → 59.7% and +130 → 43.5%. This is the sportsbook's implied chance of the team winning, and the study measures the *change* in it from morning to evening. For each game, we follow one team and track how its win probability changes. In a picked game we follow the team Cowherd picked; in every other game we follow the team that was originally favored that morning.

### Test Choice and Rationale

Before comparing the groups, two conditions were checked to select a valid test:

| Check | Purpose | Result |
| :--- | :--- | :--- |
| Shapiro-Wilk (each group) | Are the shifts roughly normal? | picked p = 0.369, control p = 0.638 — both pass |
| Levene, median-centered | Do the groups have equal variance? | p = 0.840 — variances similar |

Both groups passed the normality screen and showed similar variance, so the study used a **two-sided two-sample Student's t-test** (the version that assumes equal variance), at α = 0.05. (Had normality failed, the plan was Mann-Whitney U, which ranks the shift values instead of averaging them; had the variances differed, Welch's t-test.) A caution: with only five picked-game shifts and eight control-game shifts, these checks would usually come back "passed" whether or not the assumptions actually hold — there are too few data points for them to flag anything but a gross violation.

### Results of the Test

| Quantity | Value |
| :--- | :--- |
| Number of games | 5 picked, 8 control (13 total) |
| Average shift, picked | +0.57 percentage points |
| Average shift, control | −0.28 percentage points |
| Difference (picked − control) | **+0.86 percentage points** |
| 95% confidence interval | −0.44 to +2.16 percentage points |
| Test | Two-sided two-sample Student's t-test |
| p-value | **0.175** |
| Cohen's d | 0.83 |

## VIII. Interpretation of Results

On this slate the picked games rose by about **+0.57 percentage points** on average while the control games drifted down by **−0.28**, leaving the picked games **+0.86 percentage points** ahead — the direction an endorsement effect would predict. The result falls short on two separate counts:

- **Not statistically significant.** The p-value of 0.175 is above the 0.05 cutoff, so at this sample size the data cannot rule out that the gap is chance. With only 13 games there is too little data to tell a real effect from chance variation. The 95% confidence interval (−0.44 to +2.16 percentage points) says the same thing: it includes zero, so "no difference" is still possible.
- **Possibly not practically significant.** Even taken at face value, a 0.86-percentage-point move in win probability is small — a fraction of a point. It is not nothing, but a change that size may well be too small to matter in practice, so a confirmed effect of this magnitude would not necessarily be important.

The effect size (Cohen's d = 0.83) is reported because it is a standard part of the analysis, but it is not evidence the result is meaningful: a standardized measure can read "large" even when, as here, the underlying change is unconfirmed and possibly too small to matter. The overall finding is that this slate shows no reliable effect — only a direction, which a far larger study would be needed to test properly.

## IX. Limitations

- **Sample size.** Thirteen games (five picked, eight control) is far below the ~128 the power analysis calls for. The study cannot detect anything but a very large effect, so "no difference found" is not "no difference exists."
- **No randomization.** Cowherd chooses the picks, so the groups are not randomly assigned and may differ in ways beyond the endorsement (for example, he may favor certain kinds of games).
- **One sportsbook, one weekend.** The prices come from a single book (DraftKings) on one slate. Different sportsbooks can price the same game differently, so a fuller study would check whether any movement holds across multiple books.
- **Confounding Friday news.** A late injury report can move a price for reasons unrelated to the pick, and this design cannot separate those causes.
- **Market pricing, not true odds.** The probabilities reflect how the sportsbook priced each team, which is what the study intends to measure; they are not a claim about a team's real chance of winning.

## X. Conclusion and Recommendations

On one weekend of data, the *Blazin' 5* picks moved about **0.86 percentage points** more than the rest of the slate — the direction an endorsement effect would predict — but the difference was **not statistically significant** (p = 0.175) at this sample size, and 0.86 percentage points may be too small to matter much in practice even if it were real. The overall assessment is that this pilot's value is in establishing a working measurement, not in any finding: with only 13 games the data cannot separate a genuine effect from chance, and even if it could, a gap this small might not matter much. The natural next step is to repeat the recording across many weekends toward the ~128-game target, which is what a real test of the question would require. This run shows the method works end to end; whether the picks actually move the market is left for that larger study.

## XI. References

1. Cowherd, C. *The Herd with Colin Cowherd* — *Blazin' 5* segment (video). The five picks and the side named for each were logged from this broadcast. <https://www.youtube.com/watch?v=fuRkH_gVIwE&t=443s>
2. ESPN. *NFL Odds* (moneylines provided by DraftKings). Morning and evening moneylines for every game on the October 23–25, 2026 slate were recorded from this source. <https://www.espn.com/nfl/odds>
3. Repository. The full analysis, the recorded odds, and the complete documentation are in the project repository: <https://github.com/jconnors23/510-m2-nfl-statistical-analysis>.
