import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

"""
SCIENTIFIC 3D HEAT MAP
----------------------
Simulates heat/temperature distribution in space.
"""

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)

X, Y = np.meshgrid(x, y)

# Heat source (center is hot, edges cold)
Z = np.exp(-(X**2 + Y**2) / 10)

# 3D surface heat map
surf = ax.plot_surface(X, Y, Z, cmap="hot")

fig.colorbar(surf)

ax.set_title("Scientific 3D Heat Distribution")

plt.show()