import numpy as np
import matplotlib.pyplot as plt

"""
COSINE WAVE VISUALIZATION
------------------------
Similar to sine wave but phase shifted.
"""

x = np.linspace(0, 2 * np.pi, 100)

y = np.cos(x)

plt.plot(x, y, color="red")

plt.title("Cosine Wave")
plt.xlabel("Angle (radians)")
plt.ylabel("Amplitude")

plt.grid(True)

plt.show()