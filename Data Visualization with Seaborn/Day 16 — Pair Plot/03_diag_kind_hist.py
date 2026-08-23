# 03_diag_kind_hist.py

import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

# --------------------------------------------

# DIAGONAL = DISTRIBUTION VIEW

# --------------------------------------------

sns.pairplot(
iris,
hue="species",
diag_kind="hist"   # histogram on diagonal
)

plt.show()

# --------------------------------------------

# IDEA:

# diagonal shows distribution of each feature

# --------------------------------------------
