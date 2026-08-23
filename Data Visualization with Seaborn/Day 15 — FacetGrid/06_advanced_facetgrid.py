# 06_advanced_facetgrid.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# ADVANCED FACET GRID

# --------------------------------------------

g = sns.FacetGrid(
data=tips,
col="time",
row="sex",
hue="smoker"
)

g.map(sns.scatterplot, "total_bill", "tip")
g.add_legend()

plt.show()

# --------------------------------------------

# RESULT:

# full 2D + category + color analysis

# --------------------------------------------
