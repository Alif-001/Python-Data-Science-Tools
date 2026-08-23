# 03_jointplot_hex.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# HEXBIN JOINT PLOT

# --------------------------------------------

sns.jointplot(
data=tips,
x="total_bill",
y="tip",
kind="hex"
)

plt.show()

# --------------------------------------------

# IDEA:

# - each hex = data density

# - useful for large datasets

# --------------------------------------------
