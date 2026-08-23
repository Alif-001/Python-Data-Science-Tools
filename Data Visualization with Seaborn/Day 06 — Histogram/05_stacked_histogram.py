# 05_stacked_histogram.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# STACKED HISTOGRAM

# --------------------------------------------

# Shows group contribution inside same bar

sns.histplot(
data=tips,
x="total_bill",
hue="sex",
multiple="stack"
)

plt.title("Stacked Histogram (Male vs Female)")
plt.show()

# --------------------------------------------

# WHAT YOU SEE:

# - bars stacked by category

# - total distribution + group split

# --------------------------------------------
