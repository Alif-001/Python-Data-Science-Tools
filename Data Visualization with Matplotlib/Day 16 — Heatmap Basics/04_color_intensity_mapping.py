import matplotlib.pyplot as plt
import numpy as np

"""
COLOR INTENSITY MAPPING
-----------------------
Higher value = darker/brighter color
"""

data = np.array([
    [5, 10, 15],
    [20, 25, 30],
    [35, 40, 45]
])

plt.imshow(data, cmap="viridis")  # professional color map

plt.title("Color Intensity Heatmap")
plt.colorbar()

plt.show()