import matplotlib.pyplot as plt
import numpy as np

"""
DAY 21 - STEM PLOT BASICS
------------------------
Stem plot = shows discrete data points clearly.
Used for:
- signals
- samples
- discrete measurements
"""

# X values (time or index)
x = np.arange(0, 10)

# Y values (signal values)
y = np.array([3, 7, 2, 9, 5, 8, 6, 4, 7, 3])

# Stem plot
plt.stem(x, y)

plt.title("Basic Stem Plot")
plt.xlabel("Index")
plt.ylabel("Value")

plt.show()