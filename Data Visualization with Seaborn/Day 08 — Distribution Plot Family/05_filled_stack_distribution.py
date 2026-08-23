# 05_filled_stack_distribution.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# STACKED DISTRIBUTION

# --------------------------------------------

sns.displot(
data=tips,
x="total_bill",
hue="smoker",
multiple="stack"   # stacking groups
)

plt.title("Stacked Distribution (Smoker vs Non-Smoker)")
plt.show()

# --------------------------------------------

# IDEA:

# - shows total + group contribution

# --------------------------------------------
