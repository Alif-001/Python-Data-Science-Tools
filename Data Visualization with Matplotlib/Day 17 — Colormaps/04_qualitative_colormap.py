import matplotlib.pyplot as plt
import numpy as np

"""
QUALITATIVE COLORMAP
--------------------
Used for categories (NOT numbers)
Example:
- Class A, B, C
"""

data = np.array([
    [1, 2, 3],
    [3, 1, 2],
    [2, 3, 1]
])

# categorical colors
plt.imshow(data, cmap="Set2")

plt.title("Qualitative Colormap")
plt.colorbar()

plt.show()