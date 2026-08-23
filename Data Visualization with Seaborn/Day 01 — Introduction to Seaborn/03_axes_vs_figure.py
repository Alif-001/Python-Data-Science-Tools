# 03_axes_vs_figure.py

# --------------------------------------------

# AXES-LEVEL vs FIGURE-LEVEL PLOTS

# --------------------------------------------

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# 1. Axes-level plot

# --------------------------------------------

# These plots are drawn on a single axis

sns.scatterplot(
data=tips,
x="total_bill",
y="tip"
)

plt.title("Axes-level Plot Example")
plt.show()

# --------------------------------------------

# 2. Figure-level plot

# --------------------------------------------

# These create full figure + can contain multiple plots

sns.relplot(
data=tips,
x="total_bill",
y="tip",
kind="scatter"
)

# relplot = figure-level function

# It creates its own figure automatically

plt.title("Figure-level Plot Example")
plt.show()

# --------------------------------------------

# KEY DIFFERENCE:

# --------------------------------------------

# Axes-level:

# - Works inside one plot area

# - Example: scatterplot, lineplot, histplot

# Figure-level:

# - Creates full layout system

# - Supports multiple subplots

# - Example: relplot, catplot, displot

# --------------------------------------------

# END OF DAY 1

# --------------------------------------------
