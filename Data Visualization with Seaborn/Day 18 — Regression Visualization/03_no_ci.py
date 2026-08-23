# 03_no_ci.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# REMOVE CONFIDENCE INTERVAL

# --------------------------------------------

sns.regplot(
data=tips,
x="total_bill",
y="tip",
ci=None
)

plt.title("Regression Line Only (No CI)")
plt.show()

# --------------------------------------------

# IDEA:

# - clean trend line

# - no uncertainty shading

# --------------------------------------------
