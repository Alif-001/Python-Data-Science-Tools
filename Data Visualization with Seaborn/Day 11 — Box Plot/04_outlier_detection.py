# 04_outlier_detection.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# OUTLIERS IN BOX PLOT

# --------------------------------------------

# Points outside whiskers = outliers

sns.boxplot(
data=tips,
x="day",
y="total_bill"
)

plt.title("Outlier Detection in Bills")
plt.show()

# --------------------------------------------

# OUTLIERS:

# - unusually high or low values

# - shown as dots

# --------------------------------------------
