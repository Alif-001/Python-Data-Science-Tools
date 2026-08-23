# 01_theme_basics.py

# --------------------------------------------

# DAY 2: SEABORN STYLING & THEMES

# --------------------------------------------

import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset (built-in sample data)

tips = sns.load_dataset("tips")

# --------------------------------------------

# 1. set_theme() - modern recommended way

# --------------------------------------------

# This controls:

# - background style

# - grid

# - font scale

# - overall appearance

sns.set_theme(
style="darkgrid",   # background style
palette="deep",     # default color palette
font_scale=1.2      # text size
)

# --------------------------------------------

# Simple plot to see theme effect

# --------------------------------------------

sns.scatterplot(
data=tips,
x="total_bill",
y="tip"
)

plt.title("Theme Demo - darkgrid")
plt.show()

# --------------------------------------------

# Try changing style:

# whitegrid, dark, white, ticks

# --------------------------------------------
