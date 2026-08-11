import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

"""
3D WIREFRAME PLOT
----------------
Same as surface but only grid lines (less smooth)
"""

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-5, 5, 30)
y = np.linspace(-5, 5, 30)

X, Y = np.meshgrid(x, y)

Z = X**2 - Y**2

ax.plot_wireframe(X, Y, Z, color="blue")

ax.set_title("3D Wireframe Plot")

plt.show()