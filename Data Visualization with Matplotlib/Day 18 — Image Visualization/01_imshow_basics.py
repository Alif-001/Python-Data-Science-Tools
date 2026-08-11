import matplotlib.pyplot as plt
import numpy as np

"""
DAY 18 - IMAGE VISUALIZATION
---------------------------
imshow() = used to display images from numeric arrays.
Each number = pixel intensity.
"""

# Create a simple "image" (matrix)
image = np.array([
    [0, 50, 100],
    [150, 200, 250],
    [255, 200, 100]
])

# Show image
plt.imshow(image)

plt.title("Basic Image Display")
plt.colorbar()  # shows pixel intensity scale

plt.show()