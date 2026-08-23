# 06_real_world_joint_analysis.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# REAL-WORLD ANALYSIS

# --------------------------------------------

sns.jointplot(
data=tips,
x="total_bill",
y="tip",
kind="reg"
)

plt.show()

# --------------------------------------------

# INSIGHT:

# - check if bigger bill = bigger tip

# - business correlation analysis

# --------------------------------------------
