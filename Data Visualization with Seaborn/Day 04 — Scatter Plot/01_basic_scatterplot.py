# 01_basic_scatterplot.py

# --------------------------------------------

# DAY 4: SCATTER PLOT (CORRELATION VISUALIZATION)

# --------------------------------------------

import seaborn as sns
import matplotlib.pyplot as plt

# Load built-in dataset

tips = sns.load_dataset("tips")

# --------------------------------------------

# BASIC SCATTER PLOT

# --------------------------------------------

# We compare:

# total_bill (x-axis) vs tip (y-axis)

sns.scatterplot(
data=tips,
x="total_bill",
y="tip"
)

plt.title("Total Bill vs Tip")
plt.show()

# --------------------------------------------

# WHAT YOU LEARN:

# - Each dot = one customer

# - Pattern shows relationship between variables

# --------------------------------------------
