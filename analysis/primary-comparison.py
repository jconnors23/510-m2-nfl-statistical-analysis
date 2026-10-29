"""Does Colin Cowherd's Blazin' 5 move the betting market?

Plain summary of the whole script:

1. Read the betting prices from before the show (9 AM) and after it (9 PM).
2. Turn every price into a "win chance" (a percentage).
3. For each game, measure how much that win chance changed over the day.
4. Compare the change for the 5 games Cowherd picked against the change for
   the other 8 games, and test whether the difference is real or just chance.

It reads three CSV files from the data/ folder (the 9 AM prices, the 9 PM
prices, and the picks) and prints three tables: the per-game changes, the
group comparison, and the sample size a full study would need.

Run it with:  python analysis/primary-comparison.py
Needs: pandas, numpy, scipy, statsmodels.
"""

from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.power import TTestIndPower
from statsmodels.stats.weightstats import CompareMeans, DescrStatsW

# Settings, fixed before looking at the data so the result can't be tuned.
SIGNIFICANCE_CUTOFF = 0.05           # below this p-value, a difference counts as "beyond chance"
TARGET_POWER = 0.80                  # used only for the sample-size calculation at the end
PLANNING_EFFECT_SIZES = (0.5, 0.8)   # "moderate" and "large" targets for that calculation

DATA_DIR = Path("data") if Path("data").exists() else Path("../data")


def win_chance(moneyline):
    """Turn a betting price into a win chance between 0 and 1.

    A favorite has a negative price: -150 becomes 150 / 250 = 0.60.
    An underdog has a positive price: +130 becomes 100 / 230 = 0.43.
    """
    price = pd.to_numeric(moneyline)
    size = price.abs()
    return np.where(price < 0, size / (size + 100), 100 / (price + 100))


# === Step 1: read the three files ==========================================
morning = pd.read_csv(DATA_DIR / "odds-before-9am.csv").dropna(subset=["Game"])
evening = pd.read_csv(DATA_DIR / "odds-after-9pm.csv").dropna(subset=["Game"])
picks = pd.read_csv(DATA_DIR / "picks-chosen.csv").dropna(subset=["Blazin Team Favorite"])


# === Step 2: one row per game, with every win chance we might need =========
# The "Spread" cell looks like "steelers -3"; the first word is the favorite.
# For each game we store the favorite's name and four win chances: the favorite
# and the underdog, at the morning reading and at the evening reading.
games = pd.DataFrame({"game": morning["Game"]})
games["favorite"] = morning["Spread"].str.split().str[0].str.lower()
# Favorite's two readings first, then the underdog's two, so each team's
# before-and-after sit side by side.
games["favorite_morning"] = win_chance(morning["Moneyline Favored"])
games["favorite_evening"] = win_chance(evening["Moneyline Favored"])
games["underdog_morning"] = win_chance(morning["Moneyline Underdog"])
games["underdog_evening"] = win_chance(evening["Moneyline Underdog"])


# === Step 3: mark the five games Cowherd picked ============================
# A pick reads like "Falcons to cover"; keep just the team name. The nickname
# ("Falcons") appears inside the game name ("49ers @ Falcons"), so we look for it.
picks["team"] = picks["Blazin Team Favorite"].str.replace(" to cover", "", regex=False).str.strip()
picks["spread"] = pd.to_numeric(picks["Choice"])

games["picked_team"] = pd.NA
for team in picks["team"]:
    games.loc[games["game"].str.contains(team, case=False), "picked_team"] = team

is_picked = games["picked_team"].notna()
picked_is_favorite = games["picked_team"].str.lower() == games["favorite"]


# === Step 4: pick the team to follow, and measure its change ===============
# For a picked game we follow the team Cowherd named; for every other game we
# follow the morning favorite. The "shift" is that team's evening win chance
# minus its morning win chance.
follow_underdog = is_picked & ~picked_is_favorite
games["tracked_team"] = np.where(is_picked, games["picked_team"], games["favorite"])
games["group"] = np.where(is_picked, "picked", "control")
games["morning"] = np.where(follow_underdog, games["underdog_morning"], games["favorite_morning"])
games["evening"] = np.where(follow_underdog, games["underdog_evening"], games["favorite_evening"])
games["shift"] = games["evening"] - games["morning"]

picked_shifts = games.loc[is_picked, "shift"]
control_shifts = games.loc[~is_picked, "shift"]


# === Step 5: check the two conditions that decide which test to use ========
# These only choose the test; they are not results on their own.
#   Shapiro-Wilk: is each group's set of shifts roughly bell-shaped (normal)?
#   Levene:       are the two groups about equally spread out?
# A p-value at or above 0.05 means "no strong reason to doubt it."
picked_normality_p = stats.shapiro(picked_shifts).pvalue
control_normality_p = stats.shapiro(control_shifts).pvalue
equal_spread_p = stats.levene(picked_shifts, control_shifts, center="median").pvalue

both_groups_normal = (picked_normality_p >= SIGNIFICANCE_CUTOFF) and (control_normality_p >= SIGNIFICANCE_CUTOFF)
spreads_are_equal = equal_spread_p >= SIGNIFICANCE_CUTOFF


# === Step 6: compare the two groups ========================================
# The headline number is the picked average minus the control average. Positive
# means the picked teams gained more win chance over the day than the rest.
mean_difference = picked_shifts.mean() - control_shifts.mean()

comparison = CompareMeans(DescrStatsW(picked_shifts), DescrStatsW(control_shifts))
variance_assumption = "pooled" if spreads_are_equal else "unequal"
ci_low, ci_high = comparison.tconfint_diff(alpha=SIGNIFICANCE_CUTOFF, usevar=variance_assumption)

# Cohen's d restates the difference in "standard deviations" — a size that does
# not depend on the scale. Roughly: 0.2 small, 0.5 moderate, 0.8 large.
# The pooled standard deviation combines the two groups' spreads, weighting each
# by its number of games (the standard two-sample formula).
picked_count = len(picked_shifts)
control_count = len(control_shifts)
pooled_variance = (
    (picked_count - 1) * picked_shifts.var() + (control_count - 1) * control_shifts.var()
) / (picked_count + control_count - 2)
cohens_d = mean_difference / np.sqrt(pooled_variance)

# If both groups look normal, compare their averages with a t test (Welch's if
# their spreads differ). If not, fall back to Mann-Whitney, which ranks the
# shifts instead of averaging them.
if both_groups_normal:
    test_statistic, p_value, _ = comparison.ttest_ind(alternative="two-sided", usevar=variance_assumption)
    test_name = "student t" if spreads_are_equal else "welch t"
else:
    result = stats.mannwhitneyu(picked_shifts, control_shifts, alternative="two-sided")
    test_statistic, p_value = result.statistic, result.pvalue
    test_name = "mann-whitney u"


# === Results assembled for printing and for the notebook ===================
# Per-game table: the tracked team's win chance (as a percentage) before and
# after, and the change in percentage points.
table = pd.DataFrame({
    "group": games["group"],
    "endorsed": games["picked_team"],
    "tracked": games["tracked_team"],
    "favorite": games["favorite"],
    "morning_pct": (100 * games["morning"]).round(1),
    "evening_pct": (100 * games["evening"]).round(1),
    "shift_pp": (100 * games["shift"]).round(2),
    "Game": games["game"],
}).sort_values(["group", "Game"], ascending=[False, True])

# One-line summary of every number in the comparison.
summary = pd.Series({
    "picked_n": len(picked_shifts),
    "control_n": len(control_shifts),
    "picked_mean_pp": 100 * picked_shifts.mean(),
    "control_mean_pp": 100 * control_shifts.mean(),
    "difference_pp": 100 * mean_difference,
    "ci_low_pp": 100 * ci_low,
    "ci_high_pp": 100 * ci_high,
    "cohen_d": cohens_d,
    "shapiro_picked_p": picked_normality_p,
    "shapiro_control_p": control_normality_p,
    "levene_p": equal_spread_p,
    "test": test_name,
    "stat": test_statistic,
    "p": p_value,
    "reject_null": bool(p_value < SIGNIFICANCE_CUTOFF),
})

# How many games a full study would need to reliably detect each target effect.
# This describes the design, not how much this 13-game weekend proves.
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

# Settings bundled together so the notebook can show them without repeating numbers.
config = {"alpha": SIGNIFICANCE_CUTOFF, "power": TARGET_POWER}


if __name__ == "__main__":
    print(table.to_string(index=False))
    print()
    print(summary.to_string())
    print()
    print(sample_size.to_string(index=False))
