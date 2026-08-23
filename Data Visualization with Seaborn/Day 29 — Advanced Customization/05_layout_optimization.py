# 05_layout_optimization.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.histplot(tips["total_bill"], kde=True, ax=axes[0])
axes[0].set_title("Distribution")

sns.boxplot(data=tips, x="day", y="total_bill", ax=axes[1])
axes[1].set_title("Boxplot")

# --------------------------------------------

# LAYOUT FIX

# --------------------------------------------

plt.tight_layout()

plt.show()

# --------------------------------------------

# IDEA:

# - prevents overlapping elements

# --------------------------------------------
