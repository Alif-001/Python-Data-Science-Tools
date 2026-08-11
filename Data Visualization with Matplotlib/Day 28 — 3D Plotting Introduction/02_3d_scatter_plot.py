import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

"""
3D SCATTER PLOT
---------------
Each point has (x, y, z).
Used in clustering, physics, data distribution.
"""

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Random 3D points
x = np.random.rand(50) * 10
y = np.random.rand(50) * 10
z = np.random.rand(50) * 10

ax.scatter(x, y, z, c=z, cmap="viridis")

ax.set_title("3D Scatter Plot")

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()