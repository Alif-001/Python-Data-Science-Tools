import matplotlib.pyplot as plt
import numpy as np

"""
COLOR NORMALIZATION
-------------------
Controls how values map to colors.

Without normalization:
- extreme values dominate color scale
"""

data = np.array([
    [10, 200, 300],
    [50, 400, 600],
    [70, 800, 1000]
])

plt.imshow(data, cmap="viridis")

plt.title("Without Normalization")
plt.colorbar()

plt.show()