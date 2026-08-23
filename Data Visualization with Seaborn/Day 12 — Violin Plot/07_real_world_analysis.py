# 07_real_world_analysis.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# REAL-WORLD VIOLIN ANALYSIS

# --------------------------------------------

sns.violinplot(
data=tips,
x="time",
y="total_bill",
hue="sex",
split=True
)

plt.title("Lunch vs Dinner Spending Distribution")
plt.show()

# --------------------------------------------

# INSIGHT:

# - compare full behavior patterns

# - not just averages (like barplot)

# --------------------------------------------
