import numpy as np
import matplotlib.pyplot as plt

"""
MEDIAN LINE VISUALIZATION
-------------------------
Median = middle value (robust against outliers)
"""

data = np.array([5, 7, 8, 10, 12, 50, 13, 11, 9, 6])  # includes outlier (50)

median_value = np.median(data)

x = np.arange(len(data))

plt.plot(x, data, marker="o", label="Data")

plt.axhline(median_value, color="green", linestyle="--", label=f"Median = {median_value}")

plt.title("Median Line Visualization")
plt.xlabel("Index")
plt.ylabel("Value")

plt.legend()
plt.grid(True)

plt.show()