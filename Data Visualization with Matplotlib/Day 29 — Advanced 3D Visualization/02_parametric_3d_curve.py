import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

"""
PARAMETRIC 3D CURVE
-------------------
We define X, Y, Z using a parameter (t).
Used in physics and motion simulation.
"""

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Parameter t
t = np.linspace(0, 20, 200)

# Helix (spiral shape)
x = np.sin(t)
y = np.cos(t)
z = t

ax.plot(x, y, z, color="blue")

ax.set_title("3D Parametric Curve (Helix)")

plt.show()