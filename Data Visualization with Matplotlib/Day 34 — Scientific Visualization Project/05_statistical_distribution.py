import numpy as np
import matplotlib.pyplot as plt

"""
STATISTICAL DISTRIBUTION
------------------------
We simulate random data and analyze distribution.
"""

# Normal distribution (bell curve)
data = np.random.normal(loc=50, scale=10, size=1000)

plt.hist(data, bins=30, color="green", edgecolor="black")

plt.title("Normal Distribution (Bell Curve)")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.grid(True)

plt.show()