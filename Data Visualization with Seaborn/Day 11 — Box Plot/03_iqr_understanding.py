# 03_iqr_understanding.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# IQR (INTERQUARTILE RANGE)

# --------------------------------------------

# IQR = Q3 - Q1

# middle 50% of data

sns.boxplot(
data=tips,
x="time",
y="total_bill"
)

plt.title("IQR Visualization")
plt.show()

# --------------------------------------------

# BOX = IQR RANGE

# --------------------------------------------
