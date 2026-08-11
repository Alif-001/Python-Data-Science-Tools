import matplotlib.pyplot as plt
import numpy as np

"""
GRAYSCALE IMAGE
---------------
Single channel image (black → white).
0 = black, 255 = white
"""

# Grayscale image matrix
gray_image = np.array([
    [0, 30, 60, 90],
    [120, 150, 180, 210],
    [240, 255, 200, 100],
    [50, 80, 110, 140]
])

# cmap="gray" converts numbers to grayscale
plt.imshow(gray_image, cmap="gray")

plt.title("Grayscale Image")
plt.colorbar()

plt.show()