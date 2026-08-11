import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

"""
MIXED SCIENTIFIC VISUALIZATION
-----------------------------
Combines surface + scatter points.
Used in ML and physics analysis.
"""

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Surface
x = np.linspace(-3, 3, 50)
y = np.linspace(-3, 3, 50)

X, Y = np.meshgrid(x, y)
Z = np.sin(X) + np.cos(Y)

ax.plot_surface(X, Y, Z, alpha=0.7, cmap="viridis")

# Random sample points on top
xs = np.random.uniform(-3, 3, 50)
ys = np.random.uniform(-3, 3, 50)
zs = np.sin(xs) + np.cos(ys)

ax.scatter(xs, ys, zs, color="red")

ax.set_title("Surface + Data Points Visualization")

plt.show()