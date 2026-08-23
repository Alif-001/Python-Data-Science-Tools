# 05_real_world_ml_heatmap.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# REAL ML FEATURE ANALYSIS

# --------------------------------------------

corr = tips.corr(numeric_only=True)

sns.heatmap(
corr,
annot=True,
cmap="Spectral",
center=0,
linewidths=0.5
)

plt.title("ML Feature Correlation Map")
plt.show()

# --------------------------------------------

# INSIGHT:

# - helps feature selection

# - removes redundant variables

# --------------------------------------------
