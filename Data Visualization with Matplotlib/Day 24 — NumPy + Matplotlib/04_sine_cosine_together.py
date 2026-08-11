import numpy as np
import matplotlib.pyplot as plt

"""
SINE + COSINE TOGETHER
----------------------
Compare two waves in one graph.
"""

x = np.linspace(0, 2 * np.pi, 100)

sin_y = np.sin(x)
cos_y = np.cos(x)

plt.plot(x, sin_y, label="Sine Wave")
plt.plot(x, cos_y, label="Cosine Wave")

plt.title("Sine vs Cosine")
plt.xlabel("X")
plt.ylabel("Value")

plt.legend()
plt.grid(True)

plt.show()