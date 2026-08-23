# 04_diag_kind_kde.py

import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

# --------------------------------------------

# KDE ON DIAGONAL

# --------------------------------------------

sns.pairplot(
iris,
hue="species",
diag_kind="kde"
)

plt.show()

# --------------------------------------------

# IDEA:

# smoother distribution view

# --------------------------------------------
