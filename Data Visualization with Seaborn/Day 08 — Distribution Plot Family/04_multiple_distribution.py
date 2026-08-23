# 04_multiple_distribution.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# MULTIPLE DISTRIBUTIONS

# --------------------------------------------

sns.displot(
data=tips,
x="total_bill",
hue="sex"   # compare male vs female
)

plt.title("Distribution Comparison by Gender")
plt.show()

# --------------------------------------------

# INSIGHT:

# - compare shapes of distributions

# --------------------------------------------
