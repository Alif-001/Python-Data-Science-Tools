# 05_vars_subset_pairplot.py

import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

# --------------------------------------------

# SELECT ONLY IMPORTANT FEATURES

# --------------------------------------------

sns.pairplot(
iris,
vars=["sepal_length", "sepal_width", "petal_length"],
hue="species"
)

plt.show()

# --------------------------------------------

# IDEA:

# reduce complexity for better insight

# --------------------------------------------
