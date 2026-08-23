# 07_jointplot_vs_pairplot.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# JOINTPLOT vs PAIRPLOT

# --------------------------------------------

# Pairplot = all variables

sns.pairplot(tips[["total_bill", "tip", "size"]])

plt.show()

# Jointplot = only 2 variables

sns.jointplot(
data=tips,
x="total_bill",
y="tip",
kind="scatter"
)

plt.show()

# --------------------------------------------

# IDEA:

# - pairplot = full dataset overview

# - jointplot = deep dive (2 variables)

# --------------------------------------------
