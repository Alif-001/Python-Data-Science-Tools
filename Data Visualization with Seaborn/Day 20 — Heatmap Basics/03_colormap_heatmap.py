# 03_colormap_heatmap.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

corr = tips.corr(numeric_only=True)

# --------------------------------------------

# COLORMAP CONTROL

# --------------------------------------------

sns.heatmap(
corr,
annot=True,
cmap="coolwarm"  # blue ↔ red scale
)

plt.title("Heatmap with Custom Colormap")
plt.show()

# --------------------------------------------

# IDEA:

# - red = strong positive

# - blue = negative correlation

# --------------------------------------------
