# 01_basic_jointplot.py

# --------------------------------------------

# DAY 17: JOINT PLOT

# --------------------------------------------

import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset

tips = sns.load_dataset("tips")

# --------------------------------------------

# BASIC JOINT PLOT (SCATTER)

# --------------------------------------------

sns.jointplot(
data=tips,
x="total_bill",
y="tip",
kind="scatter"
)

plt.show()

# --------------------------------------------

# IDEA:

# - middle = relationship

# - sides = distributions

# --------------------------------------------
