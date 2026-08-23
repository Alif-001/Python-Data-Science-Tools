# 04_masked_heatmap.py

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

tips = sns.load_dataset("tips")

corr = tips.corr(numeric_only=True)

# --------------------------------------------

# CREATE MASK FOR HALF HEATMAP

# --------------------------------------------

mask = np.triu(np.ones_like(corr, dtype=bool))

# --------------------------------------------

# MASKED HEATMAP

# --------------------------------------------

sns.heatmap(
corr,
annot=True,
cmap="coolwarm",
mask=mask
)

plt.title("Lower Triangle Heatmap")
plt.show()

# --------------------------------------------

# IDEA:

# - removes duplicate info

# --------------------------------------------
