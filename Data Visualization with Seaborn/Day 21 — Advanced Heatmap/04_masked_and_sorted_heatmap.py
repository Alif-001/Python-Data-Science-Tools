# 04_masked_and_sorted_heatmap.py

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

tips = sns.load_dataset("tips")

corr = tips.corr(numeric_only=True)

# --------------------------------------------

# SORT FEATURES BY CORRELATION STRENGTH

# --------------------------------------------

sorted_corr = corr.abs().sort_values(by="total_bill", ascending=False)

mask = np.triu(np.ones_like(corr, dtype=bool))

# --------------------------------------------

# HEATMAP WITH SORTING + MASK

# --------------------------------------------

sns.heatmap(
corr,
mask=mask,
annot=True,
cmap="coolwarm"
)

plt.title("Sorted Correlation Insight")
plt.show()

# --------------------------------------------

# IDEA:

# - sorting helps find strong features

# --------------------------------------------
