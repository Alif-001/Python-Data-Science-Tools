# 06_multiple_group_analysis.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# MULTI-GROUP ANALYSIS

# --------------------------------------------

sns.barplot(
data=tips,
x="day",
y="total_bill",
hue="smoker"
)

plt.title("Smoker vs Non-Smoker Average Bill")
plt.show()

# --------------------------------------------

# INSIGHT:

# - compare behavior across categories

# --------------------------------------------
