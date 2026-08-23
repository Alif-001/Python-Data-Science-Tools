# 02_jointplot_kde.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# KDE JOINT PLOT

# --------------------------------------------

sns.jointplot(
data=tips,
x="total_bill",
y="tip",
kind="kde",
fill=True
)

plt.show()

# --------------------------------------------

# IDEA:

# - shows density regions

# - darker = more data points

# --------------------------------------------
