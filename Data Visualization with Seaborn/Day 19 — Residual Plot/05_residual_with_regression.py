# 05_residual_with_regression.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# STEP 1: REGRESSION LINE

# --------------------------------------------

sns.regplot(
data=tips,
x="total_bill",
y="tip"
)

plt.title("Regression Line")
plt.show()

# --------------------------------------------

# STEP 2: RESIDUAL ANALYSIS

# --------------------------------------------

sns.residplot(
data=tips,
x="total_bill",
y="tip"
)

plt.title("Residual Analysis")
plt.show()

# --------------------------------------------

# IDEA:

# - regression = prediction

# - residual = error check

# --------------------------------------------
