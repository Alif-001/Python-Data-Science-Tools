# 03_subplot_integration.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# CREATE SUBPLOTS

# --------------------------------------------

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# --------------------------------------------

# PLOT 1

# --------------------------------------------

sns.scatterplot(
data=tips,
x="total_bill",
y="tip",
ax=axes[0]
)

axes[0].set_title("Scatter Plot")

# --------------------------------------------

# PLOT 2

# --------------------------------------------

sns.histplot(
data=tips,
x="total_bill",
kde=True,
ax=axes[1]
)

axes[1].set_title("Distribution")

plt.tight_layout()
plt.show()

# --------------------------------------------

# IDEA:

# - multiple insights in one figure

# --------------------------------------------
