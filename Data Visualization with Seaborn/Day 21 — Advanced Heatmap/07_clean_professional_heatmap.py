# 07_clean_professional_heatmap.py

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

tips = sns.load_dataset("tips")

corr = tips.corr(numeric_only=True)

mask = np.triu(np.ones_like(corr, dtype=bool))

# --------------------------------------------

# PROFESSIONAL HEATMAP STYLE

# --------------------------------------------

plt.figure(figsize=(6, 5))

sns.heatmap(
corr,
mask=mask,
annot=True,
cmap="coolwarm",
vmin=-1,
vmax=1,
center=0,
linewidths=0.5
)

plt.title("Professional Correlation Heatmap")
plt.show()

# --------------------------------------------

# USED IN:

# - ML reports

# - data science projects

# --------------------------------------------
