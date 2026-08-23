# 01_basic_clustermap.py

# --------------------------------------------

# DAY 22: CLUSTERMAP

# --------------------------------------------

import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset

iris = sns.load_dataset("iris")

# We only use numeric columns

data = iris.drop("species", axis=1)

# --------------------------------------------

# CLUSTERMAP

# --------------------------------------------

# Automatically groups similar features

sns.clustermap(data)

plt.title("Basic Clustermap")
plt.show()

# --------------------------------------------

# IDEA:

# - similar rows/columns are grouped together

# --------------------------------------------
