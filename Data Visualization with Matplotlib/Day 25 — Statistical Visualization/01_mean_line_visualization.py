import numpy as np
import matplotlib.pyplot as plt

"""
DAY 25 - STATISTICAL VISUALIZATION
----------------------------------
We visualize data + mean line.

Mean = average value of dataset
"""

# Sample data
data = np.array([10, 12, 15, 14, 18, 20, 22, 19, 17, 16])

# Calculate mean
mean_value = np.mean(data)

# X axis (index)
x = np.arange(len(data))

# Plot data
plt.plot(x, data, marker="o", label="Data")

# Mean line
plt.axhline(mean_value, color="red", linestyle="--", label=f"Mean = {mean_value:.2f}")

plt.title("Mean Line Visualization")
plt.xlabel("Index")
plt.ylabel("Value")

plt.legend()
plt.grid(True)

plt.show()