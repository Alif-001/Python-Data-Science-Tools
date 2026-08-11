import numpy as np
import matplotlib.pyplot as plt

"""
CONTOUR LEVELS
--------------
We control how many contour lines we want.
"""

x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)

X, Y = np.meshgrid(x, y)

Z = X**2 - Y**2

# levels = number of contour lines
plt.contour(X, Y, Z, levels=20, cmap="coolwarm")

plt.title("Contour Plot with Levels = 20")

plt.colorbar()

plt.show()