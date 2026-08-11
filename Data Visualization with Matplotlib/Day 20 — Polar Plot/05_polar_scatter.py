import numpy as np
import matplotlib.pyplot as plt

"""
POLAR SCATTER PLOT
------------------
Instead of lines, we plot points in circular space.
"""

theta = np.linspace(0, 2*np.pi, 30)
r = np.random.randint(1, 10, 30)

plt.subplot(111, projection='polar')

plt.scatter(theta, r)

plt.title("Polar Scatter Plot")

plt.show()