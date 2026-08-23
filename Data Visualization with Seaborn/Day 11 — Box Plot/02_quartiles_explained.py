# 02_quartiles_explained.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# QUARTILES IN BOX PLOT

# --------------------------------------------

sns.boxplot(
data=tips,
x="day",
y="tip"
)

plt.title("Tip Distribution (Quartiles)")
plt.show()

# --------------------------------------------

# QUARTILES:

# Q1 → 25% data point

# Q2 → median (50%)

# Q3 → 75% data point

# --------------------------------------------
