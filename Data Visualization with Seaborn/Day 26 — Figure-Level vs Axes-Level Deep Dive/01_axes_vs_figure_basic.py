# 01_axes_vs_figure_basic.py

# --------------------------------------------

# DAY 26: FIGURE vs AXES LEVEL

# --------------------------------------------

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# AXES-LEVEL (simple plot)

# --------------------------------------------

sns.scatterplot(
data=tips,
x="total_bill",
y="tip"
)

plt.title("Axes-Level Plot (scatterplot)")
plt.show()

# --------------------------------------------

# FIGURE-LEVEL (automatic layout system)

# --------------------------------------------

sns.relplot(
data=tips,
x="total_bill",
y="tip"
)

plt.title("Figure-Level Plot (relplot)")
plt.show()

# --------------------------------------------

# IDEA:

# - axes = single plot control

# - figure = full figure manager

# --------------------------------------------
