# 02_sequential_palette.py

import seaborn as sns
import matplotlib.pyplot as plt

# --------------------------------------------

# SEQUENTIAL PALETTE

# --------------------------------------------

palette = sns.color_palette("Blues", 10)

sns.palplot(palette)

plt.title("Sequential Palette (Blues)")
plt.show()

# --------------------------------------------

# IDEA:

# - light = low value

# - dark = high value

# --------------------------------------------
