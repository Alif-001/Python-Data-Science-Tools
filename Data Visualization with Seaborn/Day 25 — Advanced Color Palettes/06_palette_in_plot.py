# 06_palette_in_plot.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# APPLY PALETTE IN REAL VISUALIZATION

# --------------------------------------------

sns.barplot(
data=tips,
x="day",
y="total_bill",
palette="Blues"
)

plt.title("Barplot with Sequential Palette")
plt.show()

# --------------------------------------------

# IDEA:

# - colors reflect magnitude

# --------------------------------------------
