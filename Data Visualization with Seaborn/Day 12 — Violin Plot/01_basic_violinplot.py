# 01_basic_violinplot.py

# --------------------------------------------

# DAY 12: VIOLIN PLOT

# --------------------------------------------

import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset

tips = sns.load_dataset("tips")

# --------------------------------------------

# BASIC VIOLIN PLOT

# --------------------------------------------

# Shows full distribution shape

sns.violinplot(
data=tips,
x="day",
y="total_bill"
)

plt.title("Violin Plot: Total Bill per Day")
plt.show()

# --------------------------------------------

# IDEA:

# - wide area = more data points

# - narrow area = fewer points

# --------------------------------------------
