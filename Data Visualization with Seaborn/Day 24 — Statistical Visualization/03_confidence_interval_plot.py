# 03_confidence_interval_plot.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# CONFIDENCE INTERVAL (DEFAULT IN BOXPLOT/LINEPLOT)

# --------------------------------------------

sns.lineplot(
data=tips,
x="day",
y="total_bill"
)

plt.title("Confidence Interval Visualization")
plt.show()

# --------------------------------------------

# IDEA:

# - shaded region = uncertainty range

# --------------------------------------------
