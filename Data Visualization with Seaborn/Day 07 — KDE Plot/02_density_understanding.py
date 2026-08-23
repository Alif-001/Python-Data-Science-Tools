# 02_density_understanding.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# KDE = PROBABILITY DENSITY

# --------------------------------------------

# It shows where data is concentrated

sns.kdeplot(
data=tips,
x="tip"
)

plt.title("Tip Distribution (Density)")
plt.show()

# --------------------------------------------

# INTERPRETATION:

# - high peak = many values in that region

# - low area = fewer values

# --------------------------------------------
