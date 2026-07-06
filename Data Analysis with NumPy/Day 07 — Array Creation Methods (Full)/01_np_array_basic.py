import numpy as np

# =========================
# np.array → basic array creation
# =========================

# list → NumPy array
arr = np.array([1, 2, 3, 4, 5])

print("Array:", arr)
print("dtype:", arr.dtype)
print("shape:", arr.shape)

# 2D array
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])

print("\n2D Array:\n", arr2)
print("shape:", arr2.shape)
print("ndim:", arr2.ndim)