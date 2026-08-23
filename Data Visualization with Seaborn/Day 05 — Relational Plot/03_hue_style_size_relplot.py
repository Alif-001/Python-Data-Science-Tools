# 03_hue_style_size_relplot.py

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# --------------------------------------------

# MULTI-VARIABLE RELPLOT

# --------------------------------------------

# We combine multiple dimensions:

# x, y = main relationship

# hue = category

# size = importance

# style = shape difference

sns.relplot(
data=tips,
x="total_bill",
y="tip",
hue="sex",      # color
size="size",    # bubble size
style="time",   # marker style
kind="scatter"
)

plt.title("Multi-variable Relplot")
plt.show()

# --------------------------------------------

# INSIGHT:

# You can visualize 4 variables at once

# --------------------------------------------
