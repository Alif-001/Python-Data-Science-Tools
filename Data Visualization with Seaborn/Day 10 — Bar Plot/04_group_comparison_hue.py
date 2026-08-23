# 04_group_comparison_hue.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# GROUP COMPARISON

# --------------------------------------------

sns.barplot(
data=tips,
x="day",
y="total_bill",
hue="sex"   # male vs female
)

plt.title("Gender-wise Average Bill per Day")
plt.show()

# --------------------------------------------

# INSIGHT:

# Compare multiple groups side by side

# --------------------------------------------
