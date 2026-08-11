import matplotlib.pyplot as plt

"""
DAY 8 - SUBPLOTS
----------------
Subplots = multiple charts in one figure.
"""

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

# Create first plot
plt.subplot(2, 1, 1)  # 2 rows, 1 column, position 1
plt.plot(x, y)
plt.title("First Plot")

# Create second plot
plt.subplot(2, 1, 2)  # 2 rows, 1 column, position 2
plt.plot(y, x)
plt.title("Second Plot")

plt.tight_layout()
plt.show()