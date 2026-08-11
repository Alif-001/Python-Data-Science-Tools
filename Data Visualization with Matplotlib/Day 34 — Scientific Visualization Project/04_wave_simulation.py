import numpy as np
import matplotlib.pyplot as plt

"""
WAVE SIMULATION
--------------
Used in:
- sound waves
- light waves
- signal processing
"""

x = np.linspace(0, 2*np.pi, 200)

wave1 = np.sin(x)
wave2 = np.sin(2*x)

combined = wave1 + wave2

plt.plot(x, wave1, label="Wave 1")
plt.plot(x, wave2, label="Wave 2")
plt.plot(x, combined, label="Combined Wave")

plt.title("Wave Simulation")
plt.legend()
plt.grid(True)

plt.show()