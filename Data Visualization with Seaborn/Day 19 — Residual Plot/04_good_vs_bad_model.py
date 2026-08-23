# 04_good_vs_bad_model.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# GOOD MODEL: random residuals

# --------------------------------------------

sns.residplot(
data=tips,
x="total_bill",
y="tip"
)

plt.title("Residuals (Check randomness)")
plt.show()

# --------------------------------------------

# IDEA:

# GOOD MODEL:

# - points randomly scattered

# BAD MODEL:

# - pattern/curve exists

# --------------------------------------------
