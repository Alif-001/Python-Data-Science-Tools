# 06_corner_pairplot.py

import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

# --------------------------------------------

# CORNER MODE

# --------------------------------------------

# shows only lower triangle

sns.pairplot(
iris,
hue="species",
corner=True
)

plt.show()

# --------------------------------------------

# IDEA:

# cleaner and less cluttered view

# --------------------------------------------
