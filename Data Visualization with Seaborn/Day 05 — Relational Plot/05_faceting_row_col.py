# 05_faceting_row_col.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# ROW + COL FACETING

# --------------------------------------------

# row = vertical split

# col = horizontal split

sns.relplot(
data=tips,
x="total_bill",
y="tip",
hue="time",
col="sex",
row="smoker",
kind="scatter"
)

plt.show()

# --------------------------------------------

# YOU GET MULTIPLE MINI GRAPHS:

# - sex split (columns)

# - smoker split (rows)

# --------------------------------------------
