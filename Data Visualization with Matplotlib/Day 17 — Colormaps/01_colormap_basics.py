import matplotlib.pyplot as plt
import numpy as np

"""
DAY 17 - COLORMAPS
------------------
Colormap = how numbers are converted into colors.

Example:
- small value = light color
- big value = dark color
"""

# Simple matrix data
data = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# 'viridis' is a default professional colormap
plt.imshow(data, cmap="viridis")

plt.title("Basic Colormap Example")
plt.colorbar()  # shows color scale

plt.show()