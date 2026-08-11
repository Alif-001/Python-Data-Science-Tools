import matplotlib.pyplot as plt
import numpy as np

"""
DAY 35 - FINAL MASTERY REVISION
------------------------------
This file teaches: WHICH plot to use WHEN.
"""

x = np.arange(1, 8)
y = [10, 20, 15, 25, 30, 28, 35]

# 1. Line plot → trend over time
plt.subplot(1, 3, 1)
plt.plot(x, y)
plt.title("Trend (Line Plot)")

# 2. Bar plot → comparison
plt.subplot(1, 3, 2)
plt.bar(x, y)
plt.title("Comparison (Bar Plot)")

# 3. Scatter plot → relationship
plt.subplot(1, 3, 3)
plt.scatter(x, y)
plt.title("Relationship (Scatter)")

plt.tight_layout()
plt.show()