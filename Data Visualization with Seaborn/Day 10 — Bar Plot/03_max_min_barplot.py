# 03_max_min_barplot.py

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

tips = sns.load_dataset("tips")

# --------------------------------------------

# MAX VALUE PER GROUP

# --------------------------------------------

sns.barplot(
data=tips,
x="day",
y="total_bill",
estimator=np.max
)

plt.title("Maximum Bill per Day")
plt.show()

# --------------------------------------------

# MIN VALUE PER GROUP

# --------------------------------------------

sns.barplot(
data=tips,
x="day",
y="total_bill",
estimator=np.min
)

plt.title("Minimum Bill per Day")
plt.show()

# --------------------------------------------

# INSIGHT:

# - max → highest spender

# - min → lowest spender

# --------------------------------------------
