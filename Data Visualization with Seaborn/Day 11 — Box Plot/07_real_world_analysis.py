# 07_real_world_analysis.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# REAL-WORLD BOX PLOT ANALYSIS

# --------------------------------------------

sns.boxplot(
data=tips,
x="time",
y="tip",
hue="smoker"
)

plt.title("Lunch vs Dinner Tip Distribution")
plt.show()

# --------------------------------------------

# INSIGHT:

# - compare spending behavior

# - detect variability

# --------------------------------------------
