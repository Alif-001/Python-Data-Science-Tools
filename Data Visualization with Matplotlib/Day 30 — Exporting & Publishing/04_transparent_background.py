import matplotlib.pyplot as plt
import numpy as np

"""
TRANSPARENT BACKGROUND EXPORT
----------------------------
Useful for presentations and overlays.
"""

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)

plt.title("Transparent Background Plot")

# transparent=True removes white background
plt.savefig("transparent_plot.png", transparent=True)

plt.show()