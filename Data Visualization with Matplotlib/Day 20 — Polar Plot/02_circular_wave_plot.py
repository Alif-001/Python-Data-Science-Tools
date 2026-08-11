import numpy as np
import matplotlib.pyplot as plt

"""
CIRCULAR WAVE PLOT
------------------
We create circular patterns using sine wave.
"""

theta = np.linspace(0, 2*np.pi, 200)

# Wave pattern radius
r = 3 + np.sin(5 * theta)

plt.subplot(111, projection='polar')
plt.plot(theta, r)

plt.title("Circular Wave Pattern")

plt.show()