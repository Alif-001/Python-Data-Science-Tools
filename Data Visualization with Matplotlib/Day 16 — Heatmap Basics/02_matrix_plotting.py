import matplotlib.pyplot as plt
import numpy as np

"""
MATRIX PLOTTING
---------------
Heatmap is basically visualization of matrix.
"""

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

plt.imshow(matrix, cmap="Blues")

plt.title("Matrix Heatmap")
plt.colorbar()

plt.show()