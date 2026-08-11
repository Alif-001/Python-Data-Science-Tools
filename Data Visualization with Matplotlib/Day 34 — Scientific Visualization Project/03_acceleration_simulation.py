import numpy as np
import matplotlib.pyplot as plt

"""
ACCELERATION SIMULATION
----------------------
Physics equation:
distance = 0.5 * a * t²
"""

time = np.linspace(0, 10, 100)

a = 2  # acceleration

distance = 0.5 * a * time**2

plt.plot(time, distance, color="red")

plt.title("Acceleration Motion Simulation")
plt.xlabel("Time (s)")
plt.ylabel("Distance (m)")

plt.grid(True)

plt.show()