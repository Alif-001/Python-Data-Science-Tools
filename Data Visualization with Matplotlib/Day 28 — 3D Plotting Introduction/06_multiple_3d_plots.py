import numpy as np
import matplotlib.pyplot as plt

"""
MULTIPLE 3D PLOTS
-----------------
We show different 3D visualizations together.
"""

fig = plt.figure(figsize=(10, 5))

# ---- Surface Plot ----
ax1 = fig.add_subplot(1, 2, 1, projection='3d')

x = np.linspace(-3, 3, 30)
y = np.linspace(-3, 3, 30)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) + np.cos(Y)

ax1.plot_surface(X, Y, Z, cmap="viridis")
ax1.set_title("Surface Plot")

# ---- Wireframe Plot ----
ax2 = fig.add_subplot(1, 2, 2, projection='3d')
ax2.plot_wireframe(X, Y, Z, color="black")
ax2.set_title("Wireframe Plot")

plt.show()