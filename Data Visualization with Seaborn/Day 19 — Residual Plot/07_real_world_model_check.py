# 07_real_world_model_check.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# REAL-WORLD MODEL CHECK

# --------------------------------------------

sns.residplot(
data=tips,
x="total_bill",
y="tip",
lowess=True
)

plt.axhline(0, color="black")

plt.title("Model Error Pattern Check")
plt.show()

# --------------------------------------------

# INSIGHT:

# - detect bias

# - check model reliability

# --------------------------------------------
