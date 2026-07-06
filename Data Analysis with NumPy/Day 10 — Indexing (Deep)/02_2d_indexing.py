import numpy as np

# =========================
# 2D Array Indexing (Matrix)
# =========================

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print("Matrix:\n", arr)

# format: arr[row][col]

print("Element (0,0):", arr[0][0])
print("Element (1,2):", arr[1][2])
print("Element (2,1):", arr[2][1])

# alternative format (recommended)
print("Element (1,1):", arr[1, 1])

# =========================
# Concept:
# row = first index
# column = second index
# =========================