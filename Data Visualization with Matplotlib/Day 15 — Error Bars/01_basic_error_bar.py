import matplotlib.pyplot as plt

"""
DAY 15 - ERROR BARS
-------------------
Error bars show uncertainty or variation in data.

Example:
- measurement ± error
"""

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# Error values (uncertainty in each point)
error = [1, 2, 1.5, 2.5, 3]

plt.errorbar(x, y, yerr=error, fmt='o', capsize=5)

plt.title("Basic Error Bar Plot")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()