# 03_diverging_palette.py

import seaborn as sns
import matplotlib.pyplot as plt

# --------------------------------------------

# DIVERGING PALETTE

# --------------------------------------------

palette = sns.color_palette("coolwarm", 10)

sns.palplot(palette)

plt.title("Diverging Palette (Coolwarm)")
plt.show()

# --------------------------------------------

# IDEA:

# - blue = low

# - red = high

# - middle = neutral

# --------------------------------------------
