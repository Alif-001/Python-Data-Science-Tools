import numpy as np
import matplotlib.pyplot as plt

"""
DAY 19 - CONTOUR PLOT BASICS
----------------------------
Contour plot = lines that connect same values (like height map).
Think of it like a "topographic map".
"""

# Create X and Y grid
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x, y)

# Simple 2D function (z = x^2 + y^2)
Z = X**2 + Y**2

# Draw contour lines
plt.contour(X, Y, Z)

plt.title("Basic Contour Plot (z = x² + y²)")
plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.show()