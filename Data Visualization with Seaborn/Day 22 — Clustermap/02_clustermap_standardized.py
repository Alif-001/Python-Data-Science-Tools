# 02_clustermap_standardized.py

import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

data = iris.drop("species", axis=1)

# --------------------------------------------

# STANDARDIZATION (IMPORTANT STEP)

# --------------------------------------------

# makes all features comparable

data_scaled = (data - data.mean()) / data.std()

# --------------------------------------------

# CLUSTERMAP WITH SCALED DATA

# --------------------------------------------

sns.clustermap(data_scaled, cmap="coolwarm")

plt.show()

# --------------------------------------------

# WHY?

# - prevents large-scale features dominating

# --------------------------------------------
