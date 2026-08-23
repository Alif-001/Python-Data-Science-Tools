# 02_understanding_residuals.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# RESIDUAL MEANING

# --------------------------------------------

# points above 0 = under-predicted

# points below 0 = over-predicted

sns.residplot(
data=tips,
x="total_bill",
y="tip"
)

plt.axhline(0, color="red")  # reference line

plt.title("Residual Meaning Visualization")
plt.show()

# --------------------------------------------

# IDEA:

# - red line = perfect prediction line

# --------------------------------------------
