import numpy as np
import matplotlib.pyplot as plt

"""
SCIENTIFIC DATA CONTOUR
-----------------------
Used in:
- physics
- weather maps
- pressure/temperature fields
"""

# Simulated temperature field
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)

X, Y = np.meshgrid(x, y)

# Heat source in center
Z = np.exp(-(X**2 + Y**2) / 20)

plt.contourf(X, Y, Z, cmap="hot")

plt.title("Heat Distribution Map (Scientific Data)")
plt.colorbar()

plt.show()