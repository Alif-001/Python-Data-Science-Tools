import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

"""
SURFACE COLORING
----------------
We color surface based on height (Z values).
Used in:
- terrain maps
- ML loss landscapes
"""

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-4, 4, 100)
y = np.linspace(-4, 4, 100)

X, Y = np.meshgrid(x, y)

# Surface function
Z = np.sin(X) * np.cos(Y)

# Color depends on Z values
surf = ax.plot_surface(X, Y, Z, cmap="plasma")

fig.colorbar(surf)

ax.set_title("Colored 3D Surface")

plt.show()