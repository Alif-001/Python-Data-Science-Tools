# 07_real_world_count_analysis.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# REAL-WORLD COUNT ANALYSIS

# --------------------------------------------

sns.countplot(
data=tips,
x="time",
hue="smoker"
)

plt.title("Lunch vs Dinner Smoking Distribution")
plt.show()

# --------------------------------------------

# INSIGHT:

# - compare behavior across categories

# - useful in business analytics

# --------------------------------------------
