# 04_best_practices.py

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

# --------------------------------------------

# BEST PRACTICE 1: SIMPLE & CLEAN

# --------------------------------------------

sns.scatterplot(data=df, x="total_bill", y="tip")

plt.title("Simple and Clean Plot")
plt.xlabel("Total Bill")
plt.ylabel("Tip")

plt.grid(True, linestyle="--", alpha=0.3)

plt.show()

# --------------------------------------------

# BEST PRACTICE 2: MEANINGFUL COLOR

# --------------------------------------------

sns.scatterplot(data=df, x="total_bill", y="tip", hue="sex")

plt.title("Meaningful Coloring")

plt.show()

# --------------------------------------------

# RULE:

# - clarity > decoration

# --------------------------------------------
