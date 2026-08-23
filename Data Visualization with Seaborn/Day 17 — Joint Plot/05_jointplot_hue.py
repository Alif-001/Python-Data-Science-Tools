# 05_jointplot_hue.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# GROUP COMPARISON WITH HUE

# --------------------------------------------

sns.jointplot(
data=tips,
x="total_bill",
y="tip",
hue="sex",
kind="scatter"
)

plt.show()

# --------------------------------------------

# INSIGHT:

# - compare male vs female patterns

# --------------------------------------------
