---
hide:
  - toc
---

# :material-chart-box: Results and Interpretation

This page gives the numbers, how to read them honestly, what the study can and cannot claim, and how to defend it. The formulas and statistical choices behind these numbers are on [Methods and Statistical Choices](./statistical-choices.md).

## What the Slate Showed

On this slate the picked games rose a little over the day while the rest of the slate drifted down slightly, leaving the picked games about **0.86 percentage points** ahead. That gap is the direction a tout effect would predict and is a large effect size, but with only 13 games the test does not clear the significance bar, so chance cannot be ruled out.

| Quantity | Value |
| :--- | :--- |
| Number of games | 5 picked, 8 control (13 total) |
| Average shift, picked | +0.57 percentage points |
| Average shift, control | −0.28 percentage points |
| Difference (picked − control) | **+0.86 percentage points** |
| 95% confidence interval | −0.44 to +2.16 points |
| Test used | standard pooled t test |
| p-value | **0.175** |
| Cohen's d | 0.83 |
| Difference beyond chance? | **No** |

## How to Read These Numbers

The p-value alone would just say "not significant," but the fuller reading is what matters:

- **The average shift for each group.** The picked teams rose by about half a point on average; the control teams fell by about a quarter point. Four of the 13 games did not move at all, so part of the slate was stable while the moves that happened leaned toward the picks.
- **The difference between the groups** (+0.86 points) leans toward the picked side, and the 95% interval (−0.44 to +2.16) sits mostly above zero but still crosses it — so a true difference of zero remains consistent with the data.
- **The test and the effect size together.** The p-value of 0.175 is above the 0.05 cutoff, so the gap is not statistically significant. But Cohen's d = 0.83 is large, meaning the gap between the group averages is substantial relative to the spread of the data. The reason the test is not significant is the tiny sample, not a tiny effect.

The single most important sentence here: **a large effect size with a non-significant p-value, at n = 13, means "suggestive but unconfirmed" — not "proven" and not "nothing."** The small sample cannot separate a real tout effect from a lucky draw, so the honest read is a direction worth chasing with more data, not a finding. Reporting the effect size and the p-value together is deliberate: the d says the gap is sizable, the p-value says the sample is too small to trust it, and the conclusion rests on both.

## What This Study Cannot Claim

- **Sample size.** Thirteen games (five picked, eight control) is far below the ~128 the [power analysis](./pre-experiment-prep.md) calls for. "Not significant" is not "no effect" — the study simply cannot detect anything but a very large effect, and it still leaned toward one.
- **Association, not cause.** Even a significant difference would show that prices moved differently near the picks, not that Cowherd caused it. A Friday injury or sharp money reacting to the same games could move a line, and this design cannot separate those causes.
- **No randomization.** Cowherd chooses the picks, so the groups are not randomly assigned and could differ in ways beyond the endorsement (for example, if he favors marquee or close games). This makes the study quasi-experimental.
- **One book, one weekend.** The prices come from a single sportsbook (DraftKings) on one slate, used as the example source. The question is about sportsbook pricing in general, so a fuller study would check whether any movement holds across multiple books, weeks, and analysts.
- **Market pricing, not true odds.** The probabilities reflect how the sportsbook priced each team, which is what the study measures; they are not a claim about a team's real chance of winning.

## Why a Small Pilot Still Demonstrates Understanding

The gap between 13 games and the ~128 the power analysis calls for is not a flaw to apologize for — it is the point of a pilot, and naming it with a number is what shows statistical maturity:

1. The study was never going to detect a realistic effect on one slate; the power math says so in advance.
2. So the contribution of this run is **not a verdict** but a **validated measurement protocol** — it proves the odds can be captured, converted, grouped, and tested end to end, and it produces an honest, correctly-sized result.
3. The power analysis then specifies what a conclusive version needs: roughly a full season of weekends.

Framed this way, the small sample demonstrates that the design understands the relationship between sample size, effect size, and detectability, and ran a scoped first version rather than overclaiming from thin data.

## Anticipated Questions, and Honest Answers

| Likely challenge | Honest answer |
| :--- | :--- |
| "You can't claim an effect with n = 13." | Correct, and stated up front. The result is reported as suggestive, not confirmed; a large effect size with a non-significant p-value is exactly what a true-but-underpowered effect looks like. |
| "A large d with p = 0.175 — isn't that cherry-picking the good number?" | No. Both are reported together precisely so neither is cherry-picked: the d says the gap is sizable, the p-value says the sample is too small to trust it. |
| "Your groups aren't randomized, so any difference could be game type." | True. The study is quasi-experimental and names this as a core limitation; a bigger study could stratify by game type. |
| "A Friday injury could move a line, not Cowherd." | Also true and unseparable here. This is why even a significant difference would show association, not causation. |
| "Your normality checks are meaningless at this size." | Agreed; they are formally correct but underpowered. Reporting the rank-based test alongside shows the result does not depend on them. |

## What Comes Next

The clearest path from pilot to a study that carries weight, in order of impact:

1. **More weekends.** Repeat the identical protocol across a season toward the ~128-game target. This is the single most important change — and this slate already leans toward an effect the small sample cannot confirm, which is a reason to pursue it.
2. **Stratify or match on game type.** Compare picked games to similar unpicked games (same rough favorite strength, same time slot) to address the non-randomization concern.
3. **Add more sportsbooks.** The prices here come from one book as the example source; checking several would show whether any movement is book-specific or appears across the market, which is the substance of the tout-effect question.
