import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

"""
DAY 29 - ADVANCED 3D VISUALIZATION
----------------------------------
3D contour = contour lines projected in 3D space.
Used in:
- terrain maps
- ML loss surfaces
"""

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create grid
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x, y)

# Function (mountain-like surface)
Z = np.sin(np.sqrt(X**2 + Y**2))

# 3D surface
ax.plot_surface(X, Y, Z, cmap="viridis", alpha=0.8)

# 3D contour projection on bottom plane
ax.contour(X, Y, Z, zdir='z', offset=-1.5, cmap="coolwarm")

ax.set_title("3D Surface + Contour Projection")

plt.show()