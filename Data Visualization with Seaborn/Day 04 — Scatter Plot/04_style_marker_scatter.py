# 04_style_marker_scatter.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# STYLE = DIFFERENT MARKERS

# --------------------------------------------

# We use style to visually separate categories

sns.scatterplot(
data=tips,
x="total_bill",
y="tip",
hue="sex",     # color
style="time",  # marker type
)

plt.title("Scatter Plot with Style + Hue")
plt.show()

# --------------------------------------------

# INSIGHT:

# - hue = color difference

# - style = shape difference

# --------------------------------------------
