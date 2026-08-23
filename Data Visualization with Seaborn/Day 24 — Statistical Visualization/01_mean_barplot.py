# 01_mean_barplot.py

# --------------------------------------------

# DAY 24: STATISTICAL VISUALIZATION

# --------------------------------------------

import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset

tips = sns.load_dataset("tips")

# --------------------------------------------

# MEAN VISUALIZATION USING BARPLOT

# --------------------------------------------

sns.barplot(
data=tips,
x="day",
y="total_bill"
)

plt.title("Mean Total Bill per Day")
plt.show()

# --------------------------------------------

# IDEA:

# - bar height = mean value

# --------------------------------------------
