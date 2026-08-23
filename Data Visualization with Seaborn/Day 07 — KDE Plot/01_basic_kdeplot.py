# 01_basic_kdeplot.py

# --------------------------------------------

# DAY 7: KDE PLOT (KERNEL DENSITY ESTIMATION)

# --------------------------------------------

import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset

tips = sns.load_dataset("tips")

# --------------------------------------------

# BASIC KDE PLOT

# --------------------------------------------

# KDE shows smooth version of histogram

sns.kdeplot(
data=tips,
x="total_bill"
)

plt.title("KDE Plot of Total Bill")
plt.show()

# --------------------------------------------

# IDEA:

# Instead of bars → smooth curve

# --------------------------------------------
