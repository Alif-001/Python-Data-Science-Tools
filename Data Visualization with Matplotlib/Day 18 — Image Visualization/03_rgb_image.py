import matplotlib.pyplot as plt
import numpy as np

"""
RGB IMAGE
---------
Each pixel has 3 values:
R = Red
G = Green
B = Blue
"""

# Create a simple RGB image (3x3 pixels)
rgb_image = np.array([
    [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
    [[255, 255, 0], [0, 255, 255], [255, 0, 255]],
    [[100, 100, 100], [200, 200, 200], [50, 150, 250]]
])

plt.imshow(rgb_image)

plt.title("RGB Image Display")

plt.show()