# 01_triangular_heatmap.py

# --------------------------------------------

# DAY 21: ADVANCED HEATMAPS

# --------------------------------------------

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load dataset

tips = sns.load_dataset("tips")

# Correlation matrix

corr = tips.corr(numeric_only=True)

# --------------------------------------------

# CREATE MASK (UPPER TRIANGLE HIDE)

# --------------------------------------------

mask = np.triu(np.ones_like(corr, dtype=bool))

# --------------------------------------------

# TRIANGULAR HEATMAP

# --------------------------------------------

sns.heatmap(
corr,
mask=mask,
annot=True,
cmap="coolwarm",
vmin=-1,
vmax=1
)

plt.title("Triangular Correlation Heatmap")
plt.show()

# --------------------------------------------

# WHY?

# - removes duplicate info

# - standard in ML reports

# --------------------------------------------
