---
hide:
  - toc
---

# :material-code-braces: Notebook Walkthrough

This page walks through the analysis code top to bottom and explains what each part does, so the full computation can be followed and reproduced without opening a code editor. The code lives in `analysis/primary-comparison.py`; the companion notebook `analysis/primary-comparison.ipynb` simply runs that file and displays its results. The conceptual reasoning behind the choices is on [Methods and Statistical Choices](./statistical-choices.md); this page is the code itself, section by section.

The script runs end to end with:

```
python analysis/primary-comparison.py
```

It reads three CSV files from `data/` and prints three tables: the per-game shifts, the group comparison, and the sample size the design would need.

## 1. Imports and Settings

The script imports its tools and fixes the settings used throughout. `pandas` and `numpy` handle the data and arithmetic; `scipy.stats` supplies the assumption checks and the rank-based test; `statsmodels` supplies the t test, the confidence interval, and the power calculation. The settings have descriptive names and are fixed in advance, so the analysis cannot be tuned to the result.

```python
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.power import TTestIndPower
from statsmodels.stats.weightstats import CompareMeans, DescrStatsW

SIGNIFICANCE_CUTOFF = 0.05           # below this p-value, a difference counts as "beyond chance"
TARGET_POWER = 0.80                  # used only for the sample-size calculation at the end
PLANNING_EFFECT_SIZES = (0.5, 0.8)   # "moderate" and "large" targets for that calculation

DATA_DIR = Path("data") if Path("data").exists() else Path("../data")
```

## 2. One Helper Function

The odds-to-win-chance conversion is used many times, so it gets its own named function. Everything else reads as plain steps in order.

```python
def win_chance(moneyline):
    """Turn a betting price into a win chance between 0 and 1.

    A favorite has a negative price: -150 becomes 150 / 250 = 0.60.
    An underdog has a positive price: +130 becomes 100 / 230 = 0.43.
    """
    price = pd.to_numeric(moneyline)
    size = price.abs()
    return np.where(price < 0, size / (size + 100), 100 / (price + 100))
```

The full explanation of this formula is on [Methods and Statistical Choices](./statistical-choices.md).

## 3. Step 1 — Read the Three Files

The three CSV files are read, dropping any blank spreadsheet rows.

```python
morning = pd.read_csv(DATA_DIR / "odds-before-9am.csv").dropna(subset=["Game"])
evening = pd.read_csv(DATA_DIR / "odds-after-9pm.csv").dropna(subset=["Game"])
picks = pd.read_csv(DATA_DIR / "picks-chosen.csv").dropna(subset=["Blazin Team Favorite"])
```

Each odds file has one row per game with the game name, the spread, the favorite's moneyline, the underdog's moneyline, and a slate/source note.

**What this produces.** `morning` holds the raw prices as recorded (first three rows shown):

```
                     Game      Spread  Moneyline Favored  Moneyline Underdog
Steelers @ Saints (Paris) steelers -3               -175                 145
          Browns @ Titans browns -1.5               -130                 110
          Dolphins @ Jets   jets -4.5               -225                 185
```

`picks` holds the five endorsements, with the side named as a spread in the `Choice` column:

```
Blazin Team Favorite  Choice
    Falcons to cover     2.5
    Bengals to cover     1.5
     Browns to cover    -1.5
      Lions to cover    -3.0
     Chiefs to cover     2.5
```

A positive `Choice` (Falcons, Bengals, Chiefs) is an underdog pick; a negative one (Browns, Lions) is a favorite pick.

## 4. Step 2 — One Row per Game

All the prep collapses into a single table called `games`. For each game it stores the morning favorite (the first word of the spread text) and four win chances: the favorite and the underdog, at each of the two readings.

```python
games = pd.DataFrame({"game": morning["Game"]})
games["favorite"] = morning["Spread"].str.split().str[0].str.lower()
# Favorite's two readings first, then the underdog's two, so each team's
# before-and-after sit side by side.
games["favorite_morning"] = win_chance(morning["Moneyline Favored"])
games["favorite_evening"] = win_chance(evening["Moneyline Favored"])
games["underdog_morning"] = win_chance(morning["Moneyline Underdog"])
games["underdog_evening"] = win_chance(evening["Moneyline Underdog"])
```

**Before:** the raw `morning`/`evening` tables hold moneylines like `-175` and `145`.
**After:** every price has become a win chance between 0 and 1. The columns are grouped so each team's before-and-after sit together — the favorite's morning and evening first, then the underdog's (first three rows):

```
                     game favorite  favorite_morning  favorite_evening  underdog_morning  underdog_evening
Steelers @ Saints (Paris) steelers          0.636364          0.618321          0.408163          0.423729
          Browns @ Titans   browns          0.565217          0.574468          0.476190          0.467290
          Dolphins @ Jets     jets          0.692308          0.692308          0.350877          0.350877
```

For the Steelers game, the favorite's `-175` → `0.636` in the morning and `0.618` in the evening, while the underdog's `145` → `0.408` then `0.424`. Because both sides' chances are stored at both times, each team can later be scored from its own price with no further manipulation.

## 5. Step 3 — Mark the Picked Games

Each pick is recorded as a team and the side Cowherd named (for example, `"Falcons"` with a spread of `2.5`). The script takes the team name and finds it inside the full game name (`"Falcons"` appears in `"49ers @ Falcons"`), then labels those games.

```python
picks["team"] = picks["Blazin Team Favorite"].str.replace(" to cover", "", regex=False).str.strip()
picks["spread"] = pd.to_numeric(picks["Choice"])

games["picked_team"] = pd.NA
for team in picks["team"]:
    games.loc[games["game"].str.contains(team, case=False), "picked_team"] = team

is_picked = games["picked_team"].notna()
picked_is_favorite = games["picked_team"].str.lower() == games["favorite"]
```

**Before:** the pick text was `"Falcons to cover"` with `Choice = 2.5`.
**After:** `picks` holds a clean team and spread, and `games` has a new `picked_team` column — filled for the five picked games, blank (`<NA>`) for the eight control games:

```
   team  spread          game favorite picked_team
Falcons     2.5     ...Falcons   49ers     Falcons
Bengals     1.5     ...Ravens   ravens     Bengals
 Browns    -1.5     ...Titans   browns      Browns
  Lions    -3.0    ...@ lions    lions       Lions
 Chiefs     2.5  ...@ seahawks seahawks      Chiefs
                 Dolphins @ Jets    jets        <NA>
                  rams @ raiders    rams        <NA>
```

The last two lines name two booleans the rest of the script reuses: `is_picked` (true for the five picked games) and `picked_is_favorite` (for a picked game, whether the endorsed team is the favorite — e.g. true for the Browns and Lions, false for the three underdog picks). The data is 13 hand-entered rows verified by eye, so no match-count guard is needed; at this scale a guard would only restate what a glance confirms.

## 6. Step 4 — Follow the Right Team and Measure Its Change

This is the heart of the analysis. The script follows the underdog only when Cowherd picked the underdog; otherwise it follows the favorite (every control game, plus favorite picks). The **shift** is that team's evening win chance minus its morning win chance.

```python
follow_underdog = is_picked & ~picked_is_favorite
games["tracked_team"] = np.where(is_picked, games["picked_team"], games["favorite"])
games["group"] = np.where(is_picked, "picked", "control")
games["morning"] = np.where(follow_underdog, games["underdog_morning"], games["favorite_morning"])
games["evening"] = np.where(follow_underdog, games["underdog_evening"], games["favorite_evening"])
games["shift"] = games["evening"] - games["morning"]

picked_shifts = games.loc[is_picked, "shift"]
control_shifts = games.loc[~is_picked, "shift"]
```

**What this produces.** Every game now has the tracked team, its morning and evening win chance, and the `shift` between them:

```
                     game   group tracked_team  morning  evening   shift
          Browns @ Titans  picked       Browns   0.5652   0.5745  0.0093
          49ers @ Falcons  picked      Falcons   0.4464   0.4464  0.0000
         Bengals @ Ravens  picked      Bengals   0.5050   0.5192  0.0143
          packers @ lions  picked        Lions   0.6296   0.6429  0.0132
        chiefs @ seahawks  picked       Chiefs   0.4545   0.4464 -0.0081
Steelers @ Saints (Paris) control     steelers   0.6364   0.6183 -0.0180
          Dolphins @ Jets control         jets   0.6923   0.6923  0.0000
           rams @ raiders control         rams   0.6575   0.6429 -0.0147
          ...                  ...          ...      ...      ...     ...
```

Note the Falcons, Bengals, and Chiefs rows track the **underdog's** chance (those were underdog picks), while every control row tracks the favorite. The two columns of shifts then split out:

```
picked_shifts  = [0.0093, 0.0000, 0.0143, 0.0132, -0.0081]
control_shifts = [-0.0180, 0.0000, 0.0133, 0.0000, -0.0105, 0.0072, -0.0147, 0.0000]
```

These two lists of shifts are the numbers the whole comparison is built on.

## 7. Step 5 — Check the Conditions That Decide the Test

Before comparing averages, the script checks two conditions: whether each group is roughly bell-shaped (Shapiro-Wilk) and whether the two groups are about equally spread (Levene, centered on the median). A p-value at or above 0.05 means "no strong reason to doubt it." These checks only decide which test is valid; they are not findings.

```python
picked_normality_p = stats.shapiro(picked_shifts).pvalue
control_normality_p = stats.shapiro(control_shifts).pvalue
equal_spread_p = stats.levene(picked_shifts, control_shifts, center="median").pvalue

both_groups_normal = (picked_normality_p >= SIGNIFICANCE_CUTOFF) and (control_normality_p >= SIGNIFICANCE_CUTOFF)
spreads_are_equal = equal_spread_p >= SIGNIFICANCE_CUTOFF
```

**What this produces** on the collected data:

```
picked_normality_p   = 0.369   (>= 0.05, so the picked shifts look normal enough)
control_normality_p  = 0.638   (>= 0.05, so the control shifts look normal enough)
equal_spread_p       = 0.840   (>= 0.05, so the two groups are similarly spread)

both_groups_normal   = True
spreads_are_equal    = True
```

All three checks pass, which points the next step to the standard pooled t test.

## 8. Step 6 — Compare the Two Groups

The headline number is the picked average minus the control average. The script also builds a 95% confidence interval for that difference and Cohen's d (the difference in pooled-standard-deviation units).

```python
mean_difference = picked_shifts.mean() - control_shifts.mean()

comparison = CompareMeans(DescrStatsW(picked_shifts), DescrStatsW(control_shifts))
variance_assumption = "pooled" if spreads_are_equal else "unequal"
ci_low, ci_high = comparison.tconfint_diff(alpha=SIGNIFICANCE_CUTOFF, usevar=variance_assumption)

picked_count = len(picked_shifts)
control_count = len(control_shifts)
pooled_variance = (
    (picked_count - 1) * picked_shifts.var() + (control_count - 1) * control_shifts.var()
) / (picked_count + control_count - 2)
cohens_d = mean_difference / np.sqrt(pooled_variance)
```

**What this produces** (values are in the 0-to-1 scale; the summary later restates them as percentage points):

```
mean_difference = 0.00857        (picked rose 0.86 percentage points more than control)
ci_low, ci_high = -0.00443, 0.02157   (95% interval: -0.44 to +2.16 points)
cohens_d        = 0.827          (a large effect size)
```

Still part of Step 6, the script then runs the chosen test. If both groups passed the normality check it uses a two-sided t test (the standard pooled version, or Welch's if the spreads differed); otherwise it falls back to the Mann-Whitney U test, which ranks the shift values instead of averaging them.

```python
if both_groups_normal:
    test_statistic, p_value, _ = comparison.ttest_ind(alternative="two-sided", usevar=variance_assumption)
    test_name = "student t" if spreads_are_equal else "welch t"
else:
    result = stats.mannwhitneyu(picked_shifts, control_shifts, alternative="two-sided")
    test_statistic, p_value = result.statistic, result.pvalue
    test_name = "mann-whitney u"
```

On the collected data both groups passed, so the standard pooled t test was used:

```
test_name      = "student t"
test_statistic = 1.451
p_value        = 0.175     (above the 0.05 cutoff -> not statistically significant)
```

So the picked games did move more than the control games (a large effect size), but with only 13 games the difference is not strong enough to rule out chance.

## 9. The Sample-Size (Power) Calculation

Separately from the test, the script computes how many games a full study would need to reliably detect a moderate and a large effect, at the fixed cutoff and target power. This describes the design, not the evidence this weekend carries.

```python
power = TTestIndPower()
sample_size = pd.DataFrame({
    "d": PLANNING_EFFECT_SIZES,
    "n_per_group": [
        np.ceil(power.solve_power(effect_size=d, alpha=SIGNIFICANCE_CUTOFF,
                                  power=TARGET_POWER, alternative="two-sided"))
        for d in PLANNING_EFFECT_SIZES
    ],
})
sample_size["total"] = 2 * sample_size["n_per_group"]
```

**What this produces:**

```
  d  n_per_group  total
0.5         64.0  128.0
0.8         26.0   52.0
```

A full study would need about 128 games to reliably detect a moderate effect, or 52 for a large one — far more than this weekend's 13.

## 10. Outputs

Finally the script assembles a per-game `table`, a `summary` of the comparison, the `sample_size` table, and a small `config` of the settings. When run directly it prints the first three; when the notebook imports it, those objects are displayed with formatted labels.

The `summary` is the one-line record every figure in the write-up comes from:

```
picked_n              5
control_n             8
picked_mean_pp        0.57     (picked games rose 0.57 percentage points on average)
control_mean_pp      -0.28     (control games fell 0.28)
difference_pp         0.86     (the headline gap, picked minus control)
ci_low_pp            -0.44
ci_high_pp            2.16
cohen_d               0.83
shapiro_picked_p      0.37
shapiro_control_p     0.64
levene_p              0.84
test                  student t
stat                  1.45
p                     0.17
reject_null           False    (not significant at the 5% cutoff)
```

See [Results and Interpretation](./conclusions.md) for what these values mean and how to read them.
