import numpy as np
import matplotlib.pyplot as plt

"""
2D FUNCTION VISUALIZATION
------------------------
Contour plot helps visualize mathematical functions.
"""

x = np.linspace(-4, 4, 200)
y = np.linspace(-4, 4, 200)

X, Y = np.meshgrid(x, y)

# Example function (wave pattern)
Z = np.sin(X) * np.cos(Y)

plt.contourf(X, Y, Z, cmap="plasma")

plt.title("2D Function Visualization")
plt.colorbar()

plt.show()