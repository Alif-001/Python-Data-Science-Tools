# 07_real_world_insight_pairplot.py

import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

# --------------------------------------------

# REAL-WORLD ANALYSIS

# --------------------------------------------

sns.pairplot(
iris,
hue="species",
diag_kind="kde",
corner=True
)

plt.show()

# --------------------------------------------

# INSIGHT:

# - detect correlation patterns

# - identify separable classes

# --------------------------------------------
