# 07_real_world_dashboard.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# REAL-WORLD ANALYSIS DASHBOARD

# --------------------------------------------

g = sns.FacetGrid(
data=tips,
col="day",
hue="sex"
)

g.map(sns.boxplot, "time", "total_bill")
g.add_legend()

plt.show()

# --------------------------------------------

# INSIGHT:

# - mini dashboards per category

# - used in real analytics reports

# --------------------------------------------
