# 02_hue_pairplot.py

import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

# --------------------------------------------

# HUE = CLASS SEPARATION

# --------------------------------------------

# species-based visualization

sns.pairplot(
iris,
hue="species"
)

plt.show()

# --------------------------------------------

# INSIGHT:

# - see class separation visually

# --------------------------------------------
