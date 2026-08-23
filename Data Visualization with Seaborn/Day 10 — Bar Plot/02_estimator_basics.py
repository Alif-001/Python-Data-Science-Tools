# 02_estimator_basics.py

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

tips = sns.load_dataset("tips")

# --------------------------------------------

# ESTIMATOR = STATISTICAL FUNCTION

# --------------------------------------------

# Default estimator = mean

sns.barplot(
data=tips,
x="day",
y="total_bill",
estimator=np.mean
)

plt.title("Mean (Default)")
plt.show()

# --------------------------------------------

# You can change estimator:

# --------------------------------------------

sns.barplot(
data=tips,
x="day",
y="total_bill",
estimator=np.median
)

plt.title("Median Total Bill per Day")
plt.show()

# --------------------------------------------

# KEY IDEA:

# estimator decides HOW value is calculated

# --------------------------------------------
