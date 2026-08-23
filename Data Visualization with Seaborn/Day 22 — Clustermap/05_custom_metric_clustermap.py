# 05_custom_metric_clustermap.py

import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

data = iris.drop("species", axis=1)

# --------------------------------------------

# CUSTOM DISTANCE METHOD

# --------------------------------------------

sns.clustermap(
data,
metric="euclidean",  # distance type
cmap="Spectral"
)

plt.show()

# --------------------------------------------

# IDEA:

# - different metrics = different grouping

# --------------------------------------------
