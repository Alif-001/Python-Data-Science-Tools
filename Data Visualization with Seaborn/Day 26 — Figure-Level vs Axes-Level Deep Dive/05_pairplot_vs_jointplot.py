# 05_pairplot_vs_jointplot.py

import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")
tips = sns.load_dataset("tips")

# --------------------------------------------

# PAIRPLOT = MULTI VARIABLE VIEW

# --------------------------------------------

sns.pairplot(iris, hue="species")

plt.show()

# --------------------------------------------

# JOINTPLOT = 2 VARIABLE DEEP ANALYSIS

# --------------------------------------------

sns.jointplot(
data=tips,
x="total_bill",
y="tip",
kind="scatter"
)

plt.show()

# --------------------------------------------

# IDEA:

# - pairplot = full dataset view

# - jointplot = deep 2-variable focus

# --------------------------------------------
