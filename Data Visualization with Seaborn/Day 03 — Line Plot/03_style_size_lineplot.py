# 03_style_size_lineplot.py

import seaborn as sns
import matplotlib.pyplot as plt

flights = sns.load_dataset("flights")

# --------------------------------------------

# STYLE + SIZE IN LINE PLOT

# --------------------------------------------

# style → different line patterns

# size → different line thickness

sns.lineplot(
data=flights,
x="year",
y="passengers",
hue="month",     # color grouping
style="month",   # line style (dashed, solid, etc.)
size="month"     # thickness variation
)

plt.title("Style + Size Line Plot")
plt.legend(bbox_to_anchor=(1.05, 1))
plt.show()

# --------------------------------------------

# KEY IDEA:

# - hue = color

# - style = pattern

# - size = thickness

# --------------------------------------------
