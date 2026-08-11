import matplotlib.pyplot as plt
import numpy as np

"""
ZOOM / CROP IMAGE
----------------
We can show only part of an image using slicing.
"""

image = np.random.randint(0, 255, (10, 10))

# Crop middle section (zoom effect)
cropped = image[3:8, 3:8]

plt.imshow(cropped, cmap="gray")

plt.title("Cropped Image (Zoom Effect)")

plt.colorbar()

plt.show()