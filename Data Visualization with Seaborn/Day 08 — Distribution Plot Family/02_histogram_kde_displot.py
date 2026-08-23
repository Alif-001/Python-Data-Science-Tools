# 02_histogram_kde_displot.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# HISTOGRAM + KDE IN ONE PLOT

# --------------------------------------------

sns.displot(
data=tips,
x="total_bill",
kde=True   # adds smooth curve
)

plt.title("Histogram + KDE (displot)")
plt.show()

# --------------------------------------------

# KEY IDEA:

# - bars = frequency

# - curve = density shape

# --------------------------------------------
