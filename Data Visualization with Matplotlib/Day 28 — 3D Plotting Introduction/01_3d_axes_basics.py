import numpy as np
import matplotlib.pyplot as plt

# IMPORTANT: 3D plotting toolkit
from mpl_toolkits.mplot3d import Axes3D

"""
DAY 28 - 3D PLOTTING INTRODUCTION
---------------------------------
3D plot adds Z-axis (height/depth).
Used in:
- physics simulation
- ML loss surfaces
- engineering models
"""

# Create figure
fig = plt.figure()

# Add 3D axis
ax = fig.add_subplot(111, projection='3d')

# Sample data
x = [1, 2, 3, 4]
y = [2, 3, 4, 5]
z = [5, 6, 7, 8]

# Plot 3D line
ax.plot(x, y, z)

ax.set_title("Basic 3D Line Plot")
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_zlabel("Z axis")

plt.show()