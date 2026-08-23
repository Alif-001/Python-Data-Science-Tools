# 04_multiple_kde.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# MULTIPLE KDE CURVES

# --------------------------------------------

# Compare distributions between groups

sns.kdeplot(
data=tips,
x="total_bill",
hue="sex",   # male vs female
fill=False
)

plt.title("KDE Comparison: Male vs Female")
plt.show()

# --------------------------------------------

# INSIGHT:

# - each group has its own smooth curve

# --------------------------------------------
