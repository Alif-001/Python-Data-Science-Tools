# 05_horizontal_countplot.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# HORIZONTAL COUNT PLOT

# --------------------------------------------

sns.countplot(
data=tips,
y="day"   # swap axis
)

plt.title("Horizontal Count Plot")
plt.show()

# --------------------------------------------

# WHY USE THIS?

# - better for long category names

# - improves readability

# --------------------------------------------
