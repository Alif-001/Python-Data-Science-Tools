# 04_confidence_interval.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# CONFIDENCE INTERVAL (CI)

# --------------------------------------------

# Shows uncertainty around the mean

# Default: seaborn adds shaded region

# --------------------------------------------

sns.lineplot(
data=tips,
x="size",
y="total_bill"
)

plt.title("Confidence Interval Example")
plt.show()

# --------------------------------------------

# WHAT IS CI?

# - shaded area = possible variation

# - line = average trend

# --------------------------------------------

# You can remove CI:

sns.lineplot(
data=tips,
x="size",
y="total_bill",
errorbar=None
)

plt.title("Without Confidence Interval")
plt.show()

# --------------------------------------------

# NEW SEABORN VERSION:

# errorbar replaces old ci parameter

# --------------------------------------------
