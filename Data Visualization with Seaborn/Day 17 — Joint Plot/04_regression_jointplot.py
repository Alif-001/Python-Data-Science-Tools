# 04_regression_jointplot.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# REGRESSION JOINT PLOT

# --------------------------------------------

sns.jointplot(
data=tips,
x="total_bill",
y="tip",
kind="reg"   # regression line
)

plt.show()

# --------------------------------------------

# IDEA:

# - shows trend line

# - checks correlation direction

# --------------------------------------------
