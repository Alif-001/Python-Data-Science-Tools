# 01_basic_facetgrid.py

# --------------------------------------------

# DAY 15: FACETGRID (ADVANCED FACETING SYSTEM)

# --------------------------------------------

import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset

tips = sns.load_dataset("tips")

# --------------------------------------------

# CREATE FACET GRID

# --------------------------------------------

# We define row/column structure first

g = sns.FacetGrid(
data=tips,
col="sex"   # split into male / female columns
)

# --------------------------------------------

# MAP A PLOT INTO GRID

# --------------------------------------------

g.map(sns.histplot, "total_bill")

plt.show()

# --------------------------------------------

# IDEA:

# same plot repeated for each category

# --------------------------------------------
