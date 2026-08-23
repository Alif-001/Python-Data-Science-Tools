# 05_histogram_facetgrid.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# HISTOGRAM PER CATEGORY

# --------------------------------------------

g = sns.FacetGrid(
data=tips,
col="smoker"
)

g.map(sns.histplot, "total_bill")

plt.show()

# --------------------------------------------

# IDEA:

# compare distributions visually

# --------------------------------------------
