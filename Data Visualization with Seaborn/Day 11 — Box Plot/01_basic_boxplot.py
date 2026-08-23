# 01_basic_boxplot.py

# --------------------------------------------

# DAY 11: BOX PLOT (DISTRIBUTION SUMMARY)

# --------------------------------------------

import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset

tips = sns.load_dataset("tips")

# --------------------------------------------

# BASIC BOX PLOT

# --------------------------------------------

# Shows distribution of total_bill per day

sns.boxplot(
data=tips,
x="day",
y="total_bill"
)

plt.title("Box Plot: Total Bill per Day")
plt.show()

# --------------------------------------------

# WHAT YOU SEE:

# - middle line = median

# - box = middle 50% data

# - lines = range

# --------------------------------------------
