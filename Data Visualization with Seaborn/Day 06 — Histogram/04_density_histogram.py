# 04_density_histogram.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# DENSITY HISTOGRAM

# --------------------------------------------

# Instead of counts → shows probability density

sns.histplot(
data=tips,
x="total_bill",
stat="density"
)

plt.title("Density Histogram")
plt.show()

# --------------------------------------------

# WHY USE IT?

# - useful for probability understanding

# - smooth comparison

# --------------------------------------------

# Optional: KDE overlay

sns.histplot(
data=tips,
x="total_bill",
kde=True
)

plt.title("Histogram + KDE")
plt.show()

# --------------------------------------------

# KDE = smooth curve of distribution

# --------------------------------------------
