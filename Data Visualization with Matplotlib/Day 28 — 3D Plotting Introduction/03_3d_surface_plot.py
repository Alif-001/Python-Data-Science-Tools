import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

"""
3D SURFACE PLOT
--------------
Shows a continuous surface (like terrain or ML loss function)
"""

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create grid
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x, y)

# Surface function
Z = np.sin(np.sqrt(X**2 + Y**2))

# Surface plot
ax.plot_surface(X, Y, Z, cmap="viridis")

ax.set_title("3D Surface Plot")

plt.show()