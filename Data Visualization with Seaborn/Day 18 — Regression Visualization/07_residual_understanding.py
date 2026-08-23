# 07_residual_understanding.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# RESIDUAL IDEA (CONCEPT)

# --------------------------------------------

# residual = actual - predicted

sns.residplot(
data=tips,
x="total_bill",
y="tip"
)

plt.title("Residual Plot (Error Visualization)")
plt.show()

# --------------------------------------------

# IDEA:

# - points above/below zero = error

# - helps model evaluation

# --------------------------------------------
