# 04_multiple_variables_facetgrid.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# MULTI-VARIABLE FACETING

# --------------------------------------------

g = sns.FacetGrid(
data=tips,
col="day",
hue="sex"
)

g.map(sns.scatterplot, "total_bill", "tip")

# Add legend manually

g.add_legend()

plt.show()

# --------------------------------------------

# IDEA:

# combine faceting + hue

# --------------------------------------------
