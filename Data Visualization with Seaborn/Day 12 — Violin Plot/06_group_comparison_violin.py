# 06_group_comparison_violin.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# GROUP COMPARISON VIOLIN

# --------------------------------------------

sns.violinplot(
data=tips,
x="day",
y="tip",
hue="smoker"
)

plt.title("Smoker vs Non-Smoker Tip Distribution")
plt.show()

# --------------------------------------------

# INSIGHT:

# - compare shape differences

# - detect behavior patterns

# --------------------------------------------
