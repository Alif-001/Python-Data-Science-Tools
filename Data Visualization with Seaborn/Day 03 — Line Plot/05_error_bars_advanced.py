# 05_error_bars_advanced.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# ERROR BARS EXPLANATION

# --------------------------------------------

# Error bars show variability in data:

# - standard deviation

# - confidence interval

# - standard error

# --------------------------------------------

sns.lineplot(
data=tips,
x="day",
y="total_bill",
errorbar="sd"   # standard deviation
)

plt.title("Error Bars (Standard Deviation)")
plt.show()

# --------------------------------------------

# OTHER OPTIONS:

# errorbar="ci" → confidence interval

# errorbar="sd" → standard deviation

# errorbar=None → no error bars

# --------------------------------------------

# GROUPED TREND WITH ERROR BARS

sns.lineplot(
data=tips,
x="day",
y="total_bill",
hue="sex",
errorbar="ci"
)

plt.title("Grouped Trend with Error Bars")
plt.show()

# --------------------------------------------

# END OF DAY 3

# --------------------------------------------
