import numpy as np
import matplotlib.pyplot as plt

"""
DAY 24 - NUMPY + MATPLOTLIB
---------------------------
We plot mathematical functions using NumPy arrays.
"""

# Create X values from -10 to 10
x = np.linspace(-10, 10, 100)

# Simple mathematical function: y = x^2
y = x ** 2

plt.plot(x, y)

plt.title("Quadratic Function (y = x²)")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()