# 01_basic_residplot.py

# --------------------------------------------

# DAY 19: RESIDUAL PLOT (ERROR ANALYSIS)

# --------------------------------------------

import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset

tips = sns.load_dataset("tips")

# --------------------------------------------

# RESIDUAL PLOT

# --------------------------------------------

# residual = actual - predicted value

sns.residplot(
data=tips,
x="total_bill",
y="tip"
)

plt.title("Residual Plot: Bill vs Tip")
plt.show()

# --------------------------------------------

# IDEA:

# - checks prediction errors

# --------------------------------------------
