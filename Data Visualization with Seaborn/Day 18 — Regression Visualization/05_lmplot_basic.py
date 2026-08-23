# 05_lmplot_basic.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# LM PLOT (FIGURE LEVEL)

# --------------------------------------------

sns.lmplot(
data=tips,
x="total_bill",
y="tip"
)

plt.title("LM Plot Regression")
plt.show()

# --------------------------------------------

# DIFFERENCE:

# - regplot = axes-level

# - lmplot = figure-level

# --------------------------------------------
