import numpy as np
import matplotlib.pyplot as plt

"""
PHYSICS SIMULATION - MOTION
--------------------------
We simulate motion using physics equation:
distance = speed × time
"""

time = np.linspace(0, 10, 100)

speed = 5  # constant speed

distance = speed * time

plt.plot(time, distance, color="blue")

plt.title("Uniform Motion Simulation")
plt.xlabel("Time (s)")
plt.ylabel("Distance (m)")

plt.grid(True)

plt.show()