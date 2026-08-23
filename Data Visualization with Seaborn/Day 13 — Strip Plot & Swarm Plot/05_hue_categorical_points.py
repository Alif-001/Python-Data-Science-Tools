# 05_hue_categorical_points.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# HUE = CATEGORY COLOR SPLIT

# --------------------------------------------

sns.stripplot(
data=tips,
x="day",
y="total_bill",
hue="sex"
)

plt.title("Strip Plot with Gender Split")
plt.show()

# Swarm version

sns.swarmplot(
data=tips,
x="day",
y="total_bill",
hue="sex"
)

plt.title("Swarm Plot with Gender Split")
plt.show()

# --------------------------------------------

# INSIGHT:

# - compare groups inside same category

# --------------------------------------------
