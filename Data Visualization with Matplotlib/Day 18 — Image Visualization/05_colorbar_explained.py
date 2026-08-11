import matplotlib.pyplot as plt
import numpy as np

"""
COLORBAR
--------
Shows mapping between values and colors.
"""

image = np.array([
    [10, 50, 100],
    [150, 200, 250],
    [80, 120, 180]
])

plt.imshow(image, cmap="viridis")

# colorbar = legend for pixel values
plt.colorbar()

plt.title("Image with Colorbar")

plt.show()