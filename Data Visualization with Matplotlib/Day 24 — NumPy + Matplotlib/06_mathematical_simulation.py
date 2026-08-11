import numpy as np
import matplotlib.pyplot as plt

"""
MATHEMATICAL SIMULATION
-----------------------
We simulate exponential growth/decay.
Used in:
- population growth
- finance
- physics
"""

x = np.linspace(0, 10, 100)

# Exponential growth
y = np.exp(x * 0.3)

plt.plot(x, y)

plt.title("Exponential Growth Simulation")
plt.xlabel("Time")
plt.ylabel("Growth")

plt.grid(True)

plt.show()