# 05_boxplot_story.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# BOXPLOT = FULL STATISTICAL SUMMARY

# --------------------------------------------

sns.boxplot(
data=tips,
x="day",
y="total_bill"
)

plt.title("Statistical Story (Boxplot)")
plt.show()

# --------------------------------------------

# STORY:

# - median line

# - spread (IQR)

# - outliers

# --------------------------------------------
