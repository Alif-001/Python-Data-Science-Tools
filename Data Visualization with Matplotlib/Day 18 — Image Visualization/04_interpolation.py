import matplotlib.pyplot as plt
import numpy as np

"""
INTERPOLATION
------------
Controls how image is smoothed when zoomed.
"""

image = np.random.randint(0, 255, (5, 5))

# Different interpolation styles
plt.subplot(1, 3, 1)
plt.imshow(image, interpolation="nearest")
plt.title("nearest")

plt.subplot(1, 3, 2)
plt.imshow(image, interpolation="bilinear")
plt.title("bilinear")

plt.subplot(1, 3, 3)
plt.imshow(image, interpolation="bicubic")
plt.title("bicubic")

plt.show()