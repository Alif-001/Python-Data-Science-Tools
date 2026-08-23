# 02_annotated_heatmap.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

corr = tips.corr(numeric_only=True)

# --------------------------------------------

# ANNOTATED HEATMAP

# --------------------------------------------

sns.heatmap(
corr,
annot=True  # show numbers inside cells
)

plt.title("Heatmap with Values")
plt.show()

# --------------------------------------------

# IDEA:

# - exact correlation values visible

# --------------------------------------------
