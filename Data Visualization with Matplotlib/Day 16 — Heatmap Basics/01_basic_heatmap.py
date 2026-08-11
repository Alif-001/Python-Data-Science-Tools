import matplotlib.pyplot as plt
import numpy as np

"""
DAY 16 - HEATMAP BASICS
-----------------------
Heatmap = visual representation of matrix data using colors.
"""

# Create simple matrix data
data = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Show heatmap
plt.imshow(data, cmap="hot")  # "hot" = color style

plt.title("Basic Heatmap")
plt.colorbar()  # shows color scale

plt.show()