import numpy as np

# -----------------------------------
# Combined Linear Algebra example
# -----------------------------------

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [2, 0],
    [1, 2]
])

# matrix multiplication
C = A @ B
print("Matrix Multiplication:\n", C)

# transpose
print("Transpose:\n", A.T)

# dot product (vector example)
v1 = np.array([1, 2])
v2 = np.array([3, 4])

print("Dot Product:", np.dot(v1, v2))