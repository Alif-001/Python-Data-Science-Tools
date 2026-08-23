# 05_density_understanding.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# VIOLIN = KDE + BOX COMBINATION

# --------------------------------------------

sns.violinplot(
data=tips,
x="time",
y="tip",
inner="point"
)

plt.title("Tip Distribution Density")
plt.show()

# --------------------------------------------

# IDEA:

# - thick area = high density

# - thin area = low density

# --------------------------------------------
