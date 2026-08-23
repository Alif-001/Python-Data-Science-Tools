# 05_custom_format_heatmap.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

corr = tips.corr(numeric_only=True)

# --------------------------------------------

# CUSTOM FORMATTING

# --------------------------------------------

sns.heatmap(
corr,
annot=True,
fmt=".2f",      # decimal format
linewidths=0.5  # grid lines
)

plt.title("Formatted Heatmap")
plt.show()

# --------------------------------------------

# IDEA:

# - cleaner visualization

# --------------------------------------------
