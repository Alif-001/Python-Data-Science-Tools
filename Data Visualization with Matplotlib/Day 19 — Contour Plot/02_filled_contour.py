import numpy as np
import matplotlib.pyplot as plt

"""
FILLED CONTOUR PLOT
-------------------
Instead of lines, we fill colors between levels.
"""

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x, y)

# Function
Z = np.sin(np.sqrt(X**2 + Y**2))

# Filled contour
plt.contourf(X, Y, Z, cmap="viridis")

plt.title("Filled Contour Plot (sin function)")
plt.colorbar()  # shows value scale

plt.show()