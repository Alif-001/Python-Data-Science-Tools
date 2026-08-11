import numpy as np
import matplotlib.pyplot as plt

"""
STANDARD DEVIATION VISUALIZATION
--------------------------------
Std deviation shows spread of data.
"""

data = np.array([10, 12, 14, 16, 18, 20, 22, 24, 26, 28])

mean = np.mean(data)
std = np.std(data)

x = np.arange(len(data))

plt.plot(x, data, marker="o", label="Data")

# Mean line
plt.axhline(mean, color="blue", linestyle="--", label="Mean")

# Std deviation range
plt.axhline(mean + std, color="red", linestyle=":")
plt.axhline(mean - std, color="red", linestyle=":")

plt.title("Standard Deviation Visualization")
plt.xlabel("Index")
plt.ylabel("Value")

plt.legend()
plt.grid(True)

plt.show()