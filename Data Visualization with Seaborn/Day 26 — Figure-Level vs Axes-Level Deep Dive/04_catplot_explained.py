# 04_catplot_explained.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# CATPLOT = FIGURE-LEVEL CATEGORICAL TOOL

# --------------------------------------------

sns.catplot(
data=tips,
x="day",
y="total_bill",
kind="box",
hue="sex"
)

plt.show()

# --------------------------------------------

# IDEA:

# - replaces boxplot, violin, strip, etc.

# --------------------------------------------
