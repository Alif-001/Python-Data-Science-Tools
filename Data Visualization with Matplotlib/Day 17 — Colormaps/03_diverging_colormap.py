import matplotlib.pyplot as plt
import numpy as np

"""
DIVERGING COLORMAP
------------------
Used when data has:
- negative values
- positive values
"""

data = np.array([
    [-5, -3, 0],
    [1, 3, 5],
    [6, 8, 10]
])

# coolwarm = blue (low) → white → red (high)
plt.imshow(data, cmap="coolwarm")

plt.title("Diverging Colormap")
plt.colorbar()

plt.show()