# 04_qualitative_palette.py

import seaborn as sns
import matplotlib.pyplot as plt

# --------------------------------------------

# QUALITATIVE PALETTE (CATEGORIES)

# --------------------------------------------

palette = sns.color_palette("Set2", 8)

sns.palplot(palette)

plt.title("Qualitative Palette (Set2)")
plt.show()

# --------------------------------------------

# IDEA:

# - used for categories (no order)

# --------------------------------------------
