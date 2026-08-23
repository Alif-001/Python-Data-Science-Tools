# 01_basic_barplot_mean.py

# --------------------------------------------

# DAY 10: BAR PLOT (STATISTICAL SUMMARY)

# --------------------------------------------

import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset

tips = sns.load_dataset("tips")

# --------------------------------------------

# BASIC BAR PLOT

# --------------------------------------------

# By default: shows MEAN (average)

sns.barplot(
data=tips,
x="day",
y="total_bill"
)

plt.title("Average Total Bill per Day")
plt.show()

# --------------------------------------------

# IDEA:

# Each bar = average value

# --------------------------------------------
