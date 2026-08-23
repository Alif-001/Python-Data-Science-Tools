# 05_custom_palette.py

import seaborn as sns
import matplotlib.pyplot as plt

# --------------------------------------------

# CUSTOM COLOR PALETTE

# --------------------------------------------

custom_colors = ["#ff9999", "#66b3ff", "#99ff99"]

palette = sns.color_palette(custom_colors)

sns.palplot(palette)

plt.title("Custom Palette")
plt.show()

# --------------------------------------------

# IDEA:

# - you control exact colors

# - used in dashboards & branding

# --------------------------------------------
