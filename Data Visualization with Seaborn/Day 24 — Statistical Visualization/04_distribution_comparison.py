# 04_distribution_comparison.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# DISTRIBUTION COMPARISON

# --------------------------------------------

sns.histplot(
data=tips,
x="total_bill",
hue="sex",
kde=True,
multiple="stack"
)

plt.title("Distribution Comparison (Male vs Female)")
plt.show()

# --------------------------------------------

# IDEA:

# - compare shape of distributions

# --------------------------------------------
