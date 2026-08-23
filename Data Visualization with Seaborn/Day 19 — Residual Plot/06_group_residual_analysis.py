# 06_group_residual_analysis.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# GROUP RESIDUAL ANALYSIS

# --------------------------------------------

sns.residplot(
data=tips,
x="total_bill",
y="tip",
scatter_kws={"alpha": 0.5}
)

plt.title("Residual Spread Analysis")
plt.show()

# --------------------------------------------

# IDEA:

# - check consistency across data range

# --------------------------------------------
