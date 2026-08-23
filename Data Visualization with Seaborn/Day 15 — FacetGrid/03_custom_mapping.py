# 03_custom_mapping.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# CUSTOM FUNCTION INSIDE FACETGRID

# --------------------------------------------

g = sns.FacetGrid(
data=tips,
col="time"
)

# We can customize how data is plotted

g.map(sns.kdeplot, "total_bill", fill=True)

plt.show()

# --------------------------------------------

# IDEA:

# - each subplot uses same function

# - but different subset of data

# --------------------------------------------
