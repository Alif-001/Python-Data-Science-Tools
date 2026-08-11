import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

"""
CAMERA ANGLE CONTROL
--------------------
We rotate the view of 3D plot.
"""

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-3, 3, 30)
y = np.linspace(-3, 3, 30)

X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)

ax.plot_surface(X, Y, Z, cmap="coolwarm")

# Camera angle control
ax.view_init(elev=30, azim=45)

ax.set_title("3D Plot with Camera Angle")

plt.show()