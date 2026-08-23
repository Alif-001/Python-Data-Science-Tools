# 01_basic_displot.py

# --------------------------------------------

# DAY 8: DISTRIBUTION PLOT FAMILY

# --------------------------------------------

import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset

tips = sns.load_dataset("tips")

# --------------------------------------------

# BASIC DISTRIBUTION PLOT

# --------------------------------------------

# displot = figure-level distribution function

sns.displot(
data=tips,
x="total_bill"
)

plt.show()

# --------------------------------------------

# IDEA:

# - combines histogram logic

# - figure-level (auto layout)

# --------------------------------------------
