# 06_group_comparison_boxplot.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# GROUP COMPARISON

# --------------------------------------------

sns.boxplot(
data=tips,
x="day",
y="total_bill",
hue="sex"   # male vs female
)

plt.title("Gender-wise Bill Distribution")
plt.show()

# --------------------------------------------

# INSIGHT:

# - compare distributions side by side

# --------------------------------------------
