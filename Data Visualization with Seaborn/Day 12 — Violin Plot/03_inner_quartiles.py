# 03_inner_quartiles.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# INNER QUARTILES IN VIOLIN PLOT

# --------------------------------------------

sns.violinplot(
data=tips,
x="day",
y="total_bill",
inner="quartile"  # shows Q1, median, Q3
)

plt.title("Violin Plot with Quartiles")
plt.show()

# --------------------------------------------

# OTHER OPTIONS:

# inner="box"

# inner="point"

# inner=None

# --------------------------------------------
