import numpy as np
import matplotlib.pyplot as plt

"""
MULTI LINE POLAR PLOT
---------------------
Multiple signals in circular form.
Useful in signal analysis.
"""

theta = np.linspace(0, 2*np.pi, 200)

r1 = 2 + np.sin(3 * theta)
r2 = 2 + np.cos(5 * theta)

plt.subplot(111, projection='polar')

plt.plot(theta, r1, label="Signal 1")
plt.plot(theta, r2, label="Signal 2")

plt.title("Multiple Polar Signals")
plt.legend()

plt.show()