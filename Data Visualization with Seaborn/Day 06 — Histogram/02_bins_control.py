# 02_bins_control.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# BINS = number of intervals

# --------------------------------------------

# Few bins = rough view

sns.histplot(
data=tips,
x="total_bill",
bins=5
)

plt.title("Histogram with Few Bins")
plt.show()

# More bins = detailed view

sns.histplot(
data=tips,
x="total_bill",
bins=30
)

plt.title("Histogram with Many Bins")
plt.show()

# --------------------------------------------

# IDEA:

# - low bins → smooth overview

# - high bins → detailed pattern

# --------------------------------------------
