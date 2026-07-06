import numpy as np

# =========================
# np.diag → diagonal matrix তৈরি
# =========================

# 1D array → diagonal matrix
arr = np.diag([1, 2, 3, 4])

print("Diagonal Matrix:\n", arr)

# =========================
# Extract diagonal from matrix
# =========================

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

diag_values = np.diag(matrix)

print("\nOriginal Matrix:\n", matrix)
print("Diagonal Values:", diag_values)