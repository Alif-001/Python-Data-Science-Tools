# 07_combined_violin_strip.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# VIOLIN + STRIP COMBINATION

# --------------------------------------------

# Violin = shape

# Strip = real points

sns.violinplot(
data=tips,
x="day",
y="total_bill",
inner=None
)

sns.stripplot(
data=tips,
x="day",
y="total_bill",
color="black",
alpha=0.5
)

plt.title("Distribution + Raw Data Points")
plt.show()

# --------------------------------------------

# BEST PRACTICE:

# - violin shows shape

# - strip shows real data

# --------------------------------------------
