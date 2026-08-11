import numpy as np
import matplotlib.pyplot as plt

"""
SINE WAVE VISUALIZATION
----------------------
Used in:
- sound waves
- signal processing
- physics
"""

# Create smooth X values (time)
x = np.linspace(0, 2 * np.pi, 100)

# Sine function
y = np.sin(x)

plt.plot(x, y)

plt.title("Sine Wave")
plt.xlabel("Angle (radians)")
plt.ylabel("Amplitude")

plt.grid(True)  # show grid

plt.show()