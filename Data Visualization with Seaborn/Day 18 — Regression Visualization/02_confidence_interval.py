# 02_confidence_interval.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# CONFIDENCE INTERVAL

# --------------------------------------------

# shaded area around regression line

sns.regplot(
data=tips,
x="total_bill",
y="tip"
)

plt.title("Regression with Confidence Interval")
plt.show()

# --------------------------------------------

# IDEA:

# - shaded region = uncertainty

# - wider area = more uncertainty

# --------------------------------------------
