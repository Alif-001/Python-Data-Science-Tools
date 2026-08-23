# 06_real_world_analysis.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# REAL-WORLD ANALYSIS

# --------------------------------------------

sns.swarmplot(
data=tips,
x="time",
y="tip",
hue="smoker"
)

plt.title("Tip Behavior: Lunch vs Dinner")
plt.show()

# --------------------------------------------

# INSIGHT:

# - see every customer behavior

# - detect patterns clearly

# --------------------------------------------
