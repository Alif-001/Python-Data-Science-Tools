# 02_median_comparison.py

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

tips = sns.load_dataset("tips")

# --------------------------------------------

# MEAN VS MEDIAN ANALYSIS

# --------------------------------------------

mean_vals = tips.groupby("day")["total_bill"].mean()
median_vals = tips.groupby("day")["total_bill"].median()

# --------------------------------------------

# PLOT COMPARISON

# --------------------------------------------

plt.plot(mean_vals.index, mean_vals.values, label="Mean")
plt.plot(median_vals.index, median_vals.values, label="Median")

plt.title("Mean vs Median Comparison")
plt.legend()
plt.show()

# --------------------------------------------

# IDEA:

# - difference shows skewness

# --------------------------------------------
