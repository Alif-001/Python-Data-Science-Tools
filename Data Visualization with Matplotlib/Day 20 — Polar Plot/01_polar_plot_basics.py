import numpy as np
import matplotlib.pyplot as plt

"""
DAY 20 - POLAR PLOT BASICS
--------------------------
Polar plot = graph based on:
- angle (θ)
- radius (r)

Instead of X-Y, we use:
r = distance from center
θ = angle
"""

# Create angles (0 to 2π = full circle)
theta = np.linspace(0, 2*np.pi, 100)

# Radius grows like a wave
r = 5 * np.sin(theta)

# Create polar plot
plt.subplot(111, projection='polar')
plt.plot(theta, r)

plt.title("Basic Polar Plot")

plt.show()