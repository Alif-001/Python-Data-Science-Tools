import matplotlib.pyplot as plt

"""
CORRELATION TYPES
-----------------

1. Positive correlation → both increase together
2. Negative correlation → one increases, other decreases
3. No correlation → no pattern
"""

# Positive correlation
x1 = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]

# Negative correlation
x2 = [1, 2, 3, 4, 5]
y2 = [10, 8, 6, 4, 2]

# No correlation
x3 = [1, 2, 3, 4, 5]
y3 = [5, 2, 8, 1, 7]

plt.figure(figsize=(10, 4))

# Positive
plt.subplot(1, 3, 1)
plt.scatter(x1, y1)
plt.title("Positive")

# Negative
plt.subplot(1, 3, 2)
plt.scatter(x2, y2)
plt.title("Negative")

# No correlation
plt.subplot(1, 3, 3)
plt.scatter(x3, y3)
plt.title("No Correlation")

plt.tight_layout()
plt.show()