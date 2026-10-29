---
hide:
  - toc
---

# :material-book-open-variant: Glossary and References

This page has two parts. First, a **glossary** defining every statistical and betting term used in this project. Second, the **references**: the data sources and tools the study relied on.

## :material-school: Glossary of Terms

Every term below appears somewhere in the study, defined in plain language and using the study's own example numbers where it helps.

### The Core Idea

<div class="glossary-term" markdown="1">
### Implied win probability
A betting price, restated as a percentage chance of a team winning. It is the single thing this study measures. For example, a price of −148 works out to a 59.7% implied chance of winning. It reflects how the betting market (the sportsbook) priced the team, not a guaranteed true probability.
</div>

<div class="glossary-term" markdown="1">
### Moneyline
A betting price written as a positive or negative number. A **negative** moneyline (like −148) marks a favorite; a **positive** one (like +130) marks an underdog. The study converts each moneyline into an implied win probability.
</div>

<div class="glossary-term" markdown="1">
### Favorite / Underdog
The **favorite** is the team the market thinks is more likely to win (negative moneyline). The **underdog** is the team thought less likely to win (positive moneyline).
</div>

<div class="glossary-term" markdown="1">
### Point spread
The margin of victory the market expects, like "−3" (favored to win by 3). It only moves in half-point steps, which is why the study uses implied win probability instead — the probability moves in much finer increments and captures small shifts the spread would miss.
</div>

<div class="glossary-term" markdown="1">
### Shift
This study's outcome for each game: a team's implied win probability in the evening minus its probability in the morning, in percentage points. A shift of +1.4 means the team became 1.4 percentage points more likely to win over the day.
</div>

### Experiment Design Terms

<div class="glossary-term" markdown="1">
### Treatment group (picked games)
The group that received the thing being studied. Here, the five games Cowherd endorsed in the *Blazin' 5*.
</div>

<div class="glossary-term" markdown="1">
### Control group
The comparison group that did *not* receive the treatment — the games Cowherd did not pick. It shows how a normal game's price drifts over the day, so the picked games can be compared against a baseline.
</div>

<div class="glossary-term" markdown="1">
### Independent variable
The factor being varied or sorted on — here, whether a game was picked by Cowherd (yes or no).
</div>

<div class="glossary-term" markdown="1">
### Dependent variable
The outcome being measured for a response — here, the shift in a team's implied win probability.
</div>

<div class="glossary-term" markdown="1">
### Randomization
Assigning subjects to groups by chance. This study has **none**: Cowherd chooses the picks, so the groups form on their own. Without randomization the groups may differ in unobserved ways, which limits what the study can claim.
</div>

<div class="glossary-term" markdown="1">
### Quasi-experiment
A study that compares groups which formed on their own rather than by random assignment. Because Cowherd's picks are not random, this study is quasi-experimental.
</div>

<div class="glossary-term" markdown="1">
### Observational study
A study that watches what happens without controlling it. It can show that two things are associated but cannot prove one caused the other.
</div>

<div class="glossary-term" markdown="1">
### Pilot study
A small first run whose job is to prove the measurement works and hint at a direction, not to deliver a final answer. This whole study is a pilot.
</div>

<div class="glossary-term" markdown="1">
### Confounder
Something other than the treatment that could explain the result. Here, a Friday injury report could move a price for reasons unrelated to Cowherd's pick — that injury news is a confounder.
</div>

### Core Statistics

<div class="glossary-term" markdown="1">
### Mean (average)
Add up the values and divide by how many there are. The study compares the **mean shift** of the picked games against the mean shift of the control games.
</div>

<div class="glossary-term" markdown="1">
### Median
The middle value when the numbers are sorted. Less affected by one unusually large value than the mean, which is why one of the assumption checks (Levene) is centered on it.
</div>

<div class="glossary-term" markdown="1">
### Standard deviation
A measure of how spread out the values are. A small standard deviation means the numbers cluster near the mean; a large one means they are scattered.
</div>

<div class="glossary-term" markdown="1">
### Percentage point
The unit for the shift. Going from a 50% chance to a 52% chance is a rise of **2 percentage points**. (Different from "2 percent," which would be a relative change — this study always means percentage points.)
</div>

### Hypothesis Testing

<div class="glossary-term" markdown="1">
### Null hypothesis (H₀)
The default "nothing is going on" claim. Here: the picked and control games have the same average shift. A test tries to find evidence against it.
</div>

<div class="glossary-term" markdown="1">
### Alternative hypothesis (H₁)
The claim that there *is* a difference. Here: the picked and control games have different average shifts.
</div>

<div class="glossary-term" markdown="1">
### p-value
The probability of observing a difference at least as large as the one found, *if the null hypothesis were true* (that is, if there were no real effect). A small p-value means the result would be surprising under "no effect," making it evidence of a real difference. This study's p-value is **0.175** — large, meaning the observed gap could easily arise by chance.
</div>

<div class="glossary-term" markdown="1">
### Alpha (significance level)
The cutoff decided in advance for how small a p-value has to be to count as "statistically significant." This study uses **α = 0.05**, a 1-in-20 risk of a false alarm.
</div>

<div class="glossary-term" markdown="1">
### Statistically significant
A result whose p-value falls below alpha. A p-value of 0.175 is **above** 0.05, so this study's result is **not** statistically significant.
</div>

<div class="glossary-term" markdown="1">
### Two-sided (two-tailed) test
A test that looks for a difference in *either* direction (the picked games could move up or down relative to control). The opposite, a one-sided test, only checks one direction. This study is two-sided.
</div>

<div class="glossary-term" markdown="1">
### Failing to reject the null
When a test does not find enough evidence against the null hypothesis. Crucially, this is **not** the same as proving the null is true — it can also mean the sample was too small to detect a real effect. That is exactly this study's situation.
</div>

### Measuring Effect and Precision

<div class="glossary-term" markdown="1">
### Effect size
How *big* a difference is, separate from whether it is statistically significant. A difference can be large but still not significant if the sample is small — which is this study's result.
</div>

<div class="glossary-term" markdown="1">
### Cohen's d
A common effect-size measure: the gap between two group means expressed in standard-deviation units. Rough guide: 0.2 small, 0.5 moderate, 0.8 large. This study's d = **0.83**, a large gap — the reason the result is called "suggestive" despite not being significant.
</div>

<div class="glossary-term" markdown="1">
### Confidence interval (95%)
A range of plausible values for the true difference, built so that this kind of range would capture the truth 95% of the time. This study's interval is **−0.44 to +2.16 points**. Because it crosses zero, "no difference" is still plausible.
</div>

### Power and Sample Size

<div class="glossary-term" markdown="1">
### Statistical power
The chance a study would detect a real effect of a given size if one exists. Low power means a study can miss real effects. This study has low power because the sample is tiny.
</div>

<div class="glossary-term" markdown="1">
### Power analysis
A calculation, done in advance, of how many observations are needed to reach a target power (usually 80%). This study's power analysis says about **128 games** are needed for a moderate effect; it has 13, so it is underpowered by design.
</div>

<div class="glossary-term" markdown="1">
### Underpowered
Having too small a sample to reliably detect the effect of interest. A deliberately underpowered pilot is fine as long as it does not overclaim.
</div>

### The Specific Tests Used

<div class="glossary-term" markdown="1">
### Two-sample t test
A test that compares the means of two groups to see if they differ more than chance would explain. The "pooled" (standard) version assumes the two groups have similar spread. This study used the pooled two-sample t test.
</div>

<div class="glossary-term" markdown="1">
### Welch's t test
A version of the t test that does **not** assume the two groups are equally spread. It is the fallback if the equal-spread check fails. Not needed here, since the spreads were similar.
</div>

<div class="glossary-term" markdown="1">
### Mann-Whitney U test
A test that compares two groups by ranking all the values instead of averaging them. It makes no bell-shape assumption, so it is the fallback if the normality check fails. Not needed here, since both groups passed the normality check.
</div>

<div class="glossary-term" markdown="1">
### Shapiro-Wilk test
A check for whether a group's values are roughly normal (bell-shaped). Used to decide whether a t test is appropriate. Note: on very small samples it has little power, so passing it is weak evidence.
</div>

<div class="glossary-term" markdown="1">
### Levene's test
A check for whether two groups are about equally spread out. The study uses the median-centered version, which is sturdier against one unusual value. It decides between the pooled and Welch t tests.
</div>

<div class="glossary-term" markdown="1">
### Normal distribution (bell curve)
The common symmetric, bell-shaped pattern many measurements follow. Several tests assume the data is roughly normal, which is why the Shapiro-Wilk check exists.
</div>

<div class="glossary-term" markdown="1">
### Post hoc test
A follow-up test done *after* finding a significant effect, to pin down where the difference lies. None is used here because nothing significant was found.
</div>

## :material-link-variant: References

### Data Sources

<div class="references" markdown="1">

1. **Colin Cowherd's *Blazin' 5* picks.** *The Herd with Colin Cowherd*, episode segment (video). The five NFL picks and the sides named were logged from this broadcast. <https://www.youtube.com/watch?v=fuRkH_gVIwE&t=443s>

2. **NFL betting odds (moneylines), provided by DraftKings.** ESPN NFL Odds. Morning and evening moneylines for every game on the slate were recorded from this source. <https://www.espn.com/nfl/odds>

</div>

### Software and Tools

<div class="references" markdown="1">

3. **Python** (version 3.11+), used for the full analysis.

4. **pandas** and **NumPy**, for loading the data and computing the shifts. Pinned versions are in `requirements.txt`.

5. **SciPy** (`scipy.stats`), for the Shapiro-Wilk, Levene, and Mann-Whitney tests.

6. **statsmodels** (`statsmodels.stats`), for the two-sample t test, the confidence interval, and the power analysis (`TTestIndPower`).

7. **MkDocs** with the **Material for MkDocs** theme, used to build this documentation site.

</div>

> **Note on citation style:** the data sources above are listed with the exact links used. If a formal citation style (APA, MLA) is required for submission, format entries 1–2 accordingly and add access dates.
