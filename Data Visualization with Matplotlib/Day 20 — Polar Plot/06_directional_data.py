import numpy as np
import matplotlib.pyplot as plt

"""
DIRECTIONAL DATA VISUALIZATION
------------------------------
Used in:
- wind direction
- movement direction
"""

# Example wind direction (degrees → radians)
directions = np.deg2rad([0, 45, 90, 135, 180, 225, 270, 315])

# Wind speed
speed = [5, 7, 3, 6, 8, 4, 2, 9]

plt.subplot(111, projection='polar')

plt.bar(directions, speed, width=0.3, alpha=0.7)

plt.title("Wind Direction Chart")

plt.show()