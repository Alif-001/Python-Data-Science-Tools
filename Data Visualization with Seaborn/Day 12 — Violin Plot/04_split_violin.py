# 04_split_violin.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# SPLIT VIOLIN PLOT

# --------------------------------------------

# Compare 2 groups inside one violin

sns.violinplot(
data=tips,
x="day",
y="total_bill",
hue="sex",     # split by gender
split=True     # IMPORTANT
)

plt.title("Split Violin: Male vs Female")
plt.show()

# --------------------------------------------

# IDEA:

# left side = one group

# right side = another group

# --------------------------------------------
