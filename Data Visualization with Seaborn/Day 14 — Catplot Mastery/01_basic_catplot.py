# 01_basic_catplot.py

# --------------------------------------------

# DAY 14: CATPLOT MASTER

# --------------------------------------------

import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset

tips = sns.load_dataset("tips")

# --------------------------------------------

# CATPLOT = UNIFIED CATEGORICAL FUNCTION

# --------------------------------------------

# It is a FIGURE-LEVEL function

sns.catplot(
data=tips,
x="day",
y="total_bill"
)

plt.show()

# --------------------------------------------

# NOTE:

# default kind = strip-like visualization

# --------------------------------------------
