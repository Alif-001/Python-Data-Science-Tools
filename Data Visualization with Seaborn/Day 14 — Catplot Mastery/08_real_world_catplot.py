# 08_real_world_catplot.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# REAL-WORLD BUSINESS ANALYSIS

# --------------------------------------------

sns.catplot(
data=tips,
x="time",
y="tip",
hue="smoker",
kind="violin"
)

plt.title("Tip Behavior Analysis (Business Insight)")
plt.show()

# --------------------------------------------

# INSIGHT:

# - compare customer behavior patterns

# - useful for business decisions

# --------------------------------------------
