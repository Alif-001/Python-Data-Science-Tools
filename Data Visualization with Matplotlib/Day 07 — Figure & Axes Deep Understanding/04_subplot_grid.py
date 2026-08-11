import matplotlib.pyplot as plt

"""
SUBPLOT GRID (2x2)
------------------
Multiple plots in grid format.
"""

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.figure(figsize=(8, 6))

# 2x2 grid

plt.subplot(2, 2, 1)
plt.plot(x, y)
plt.title("Plot 1")

plt.subplot(2, 2, 2)
plt.plot(y, x)
plt.title("Plot 2")

plt.subplot(2, 2, 3)
plt.plot(x, [i*2 for i in x])
plt.title("Plot 3")

plt.subplot(2, 2, 4)
plt.plot(y, [i/2 for i in y])
plt.title("Plot 4")

plt.tight_layout()

plt.show()