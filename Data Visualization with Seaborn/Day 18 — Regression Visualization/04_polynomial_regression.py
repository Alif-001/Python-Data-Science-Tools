# 04_polynomial_regression.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# POLYNOMIAL REGRESSION

# --------------------------------------------

# nonlinear relationship fitting

sns.regplot(
data=tips,
x="total_bill",
y="tip",
order=2  # quadratic curve
)

plt.title("Polynomial Regression (Order 2)")
plt.show()

# --------------------------------------------

# IDEA:

# - order=1 → straight line

# - order=2 → curve

# --------------------------------------------
