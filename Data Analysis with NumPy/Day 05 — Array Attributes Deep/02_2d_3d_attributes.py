import numpy as np

# =========================
# 2D Array (Matrix)
# =========================
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])

print("2D Array:\n", arr2)

print("ndim:", arr2.ndim)   # 2D
print("shape:", arr2.shape) # (row, column)
print("size:", arr2.size)   # total elements

# =========================
# 3D Array (Tensor)
# =========================
arr3 = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print("\n3D Array:\n", arr3)

print("ndim:", arr3.ndim)
print("shape:", arr3.shape)
print("size:", arr3.size)