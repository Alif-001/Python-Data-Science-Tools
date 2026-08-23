# 07_row_col_faceting.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# ADVANCED FACETING

# --------------------------------------------

sns.displot(
data=tips,
x="total_bill",
col="sex",
row="smoker",
kde=True
)

plt.show()

# --------------------------------------------

# INSIGHT:

# - multi-dimensional distribution view

# --------------------------------------------
