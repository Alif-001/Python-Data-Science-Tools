# 07_kde_vs_hist.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# HISTOGRAM + KDE COMPARISON

# --------------------------------------------

sns.histplot(
data=tips,
x="total_bill",
kde=True
)

plt.title("Histogram + KDE Together")
plt.show()

# --------------------------------------------

# IDEA:

# - histogram = raw frequency

# - KDE = smooth probability shape

# --------------------------------------------
