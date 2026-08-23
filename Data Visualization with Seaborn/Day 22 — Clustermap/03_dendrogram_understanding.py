# 03_dendrogram_understanding.py

import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

data = iris.drop("species", axis=1)

# --------------------------------------------

# DENDROGRAM VISUALIZATION

# --------------------------------------------

# shows hierarchy of similarity

sns.clustermap(
data,
method="ward",  # clustering method
cmap="viridis"
)

plt.show()

# --------------------------------------------

# IDEA:

# - tree structure = similarity grouping

# --------------------------------------------
