import numpy as np

# =========================
# Modifying Elements
# =========================

arr = np.array([10, 20, 30, 40, 50])

print("Original:", arr)

# single element change
arr[0] = 999

print("After change:", arr)

# =========================
# 2D modification
# =========================

matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

print("\nMatrix:\n", matrix)

# change single element
matrix[0, 1] = 999

# change full row
matrix[1] = [100, 200, 300]

print("\nModified Matrix:\n", matrix)