import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

"""
CUSTOM COLORMAP
---------------
We define our own color transition.
"""

data = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Custom gradient: green → yellow → red
custom_cmap = LinearSegmentedColormap.from_list(
    "my_colors",
    ["green", "yellow", "red"]
)

plt.imshow(data, cmap=custom_cmap)

plt.title("Custom Colormap")
plt.colorbar()

plt.show()