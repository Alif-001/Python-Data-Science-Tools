# 05_horizontal_boxplot.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# HORIZONTAL BOX PLOT

# --------------------------------------------

sns.boxplot(
data=tips,
x="total_bill",
y="day"   # swap axes
)

plt.title("Horizontal Box Plot")
plt.show()

# --------------------------------------------

# WHY USE THIS?

# - better readability

# - useful for many categories

# --------------------------------------------
