# 03_displot_explained.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# DISPLOT = FIGURE-LEVEL DISTRIBUTION

# --------------------------------------------

sns.displot(
data=tips,
x="total_bill",
kind="hist",
kde=True
)

plt.show()

# --------------------------------------------

# IDEA:

# - histogram + KDE in one system

# - supports faceting easily

# --------------------------------------------
