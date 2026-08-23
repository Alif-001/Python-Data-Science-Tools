# 03_bins_and_rug.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# CONTROL BINS + RUG PLOT

# --------------------------------------------

sns.displot(
data=tips,
x="total_bill",
bins=20,   # number of intervals
rug=True    # shows individual points
)

plt.title("Distribution with Rug Plot")
plt.show()

# --------------------------------------------

# RUG = small ticks showing raw data points

# --------------------------------------------
