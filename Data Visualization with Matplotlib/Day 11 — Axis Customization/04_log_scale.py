import matplotlib.pyplot as plt

"""
LOG SCALE
---------
Used for large range values (exponential growth)
"""

x = [1, 2, 3, 4, 5]
y = [10, 100, 1000, 10000, 100000]

plt.plot(x, y, marker="o")

# Apply logarithmic scale on Y-axis
plt.yscale("log")

plt.title("Log Scale Example")

plt.show()