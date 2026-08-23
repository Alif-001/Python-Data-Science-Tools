# 02_row_col_facetgrid.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# ROW + COLUMN FACETING

# --------------------------------------------

g = sns.FacetGrid(
data=tips,
col="sex",
row="smoker"   # additional split
)

g.map(sns.scatterplot, "total_bill", "tip")

plt.show()

# --------------------------------------------

# RESULT:

# - male/female columns

# - smoker/non-smoker rows

# --------------------------------------------
