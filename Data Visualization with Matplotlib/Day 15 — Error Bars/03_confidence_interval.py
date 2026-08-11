import matplotlib.pyplot as plt
import numpy as np

"""
CONFIDENCE INTERVAL IDEA
------------------------
Represents range where true value may lie.
"""

x = [1, 2, 3, 4, 5]
y = [15, 18, 20, 22, 25]

# Simulated confidence interval (±2 units)
ci = 2

plt.errorbar(x, y, yerr=ci, fmt='o', capsize=5, color="green")

plt.title("Confidence Interval Visualization")

plt.show()