# 02_custom_color_scaling.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

corr = tips.corr(numeric_only=True)

# --------------------------------------------

# CUSTOM COLOR RANGE CONTROL

# --------------------------------------------

sns.heatmap(
corr,
annot=True,
cmap="RdBu",
vmin=-1,   # minimum correlation
vmax=1,    # maximum correlation
center=0   # neutral point
)

plt.title("Custom Scaled Heatmap")
plt.show()

# --------------------------------------------

# WHY IMPORTANT:

# - ensures fair comparison of values

# --------------------------------------------
