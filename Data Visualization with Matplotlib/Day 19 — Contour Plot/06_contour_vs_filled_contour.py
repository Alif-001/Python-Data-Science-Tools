import numpy as np
import matplotlib.pyplot as plt

"""
CONTOUR vs FILLED CONTOUR
------------------------
Compare both styles side by side.
"""

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x, y)

Z = np.sin(X) + np.cos(Y)

plt.subplot(1, 2, 1)
plt.contour(X, Y, Z, cmap="coolwarm")
plt.title("Contour Lines")

plt.subplot(1, 2, 2)
plt.contourf(X, Y, Z, cmap="coolwarm")
plt.title("Filled Contour")

plt.show()