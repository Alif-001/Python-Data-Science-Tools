# 04_row_column_clustering.py

import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

data = iris.drop("species", axis=1)

# --------------------------------------------

# ROW + COLUMN CLUSTERING

# --------------------------------------------

sns.clustermap(
data,
row_cluster=True,
col_cluster=True,
cmap="coolwarm"
)

plt.show()

# --------------------------------------------

# IDEA:

# - rows = samples

# - columns = features

# --------------------------------------------
