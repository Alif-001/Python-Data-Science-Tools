# 01_basic_regplot.py

# --------------------------------------------

# DAY 18: REGRESSION VISUALIZATION

# --------------------------------------------

import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset

tips = sns.load_dataset("tips")

# --------------------------------------------

# REGRESSION PLOT (regplot)

# --------------------------------------------

# Shows relationship + best fit line

sns.regplot(
data=tips,
x="total_bill",
y="tip"
)

plt.title("Regression: Bill vs Tip")
plt.show()

# --------------------------------------------

# IDEA:

# - points = data

# - line = trend

# --------------------------------------------
