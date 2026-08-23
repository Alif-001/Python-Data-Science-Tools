# 07_real_world_business_analysis.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# REAL-WORLD ANALYSIS EXAMPLE

# --------------------------------------------

sns.barplot(
data=tips,
x="time",
y="tip",
hue="sex"
)

plt.title("Lunch vs Dinner Tip Analysis")
plt.show()

# --------------------------------------------

# INSIGHT:

# - helps in business decisions

# - compare customer behavior

# --------------------------------------------
