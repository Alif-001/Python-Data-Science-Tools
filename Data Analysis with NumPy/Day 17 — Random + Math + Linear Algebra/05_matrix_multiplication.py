import numpy as np

# -----------------------------------
# Matrix multiplication
# -----------------------------------

a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])

# matrix multiplication (IMPORTANT)
print(np.matmul(a, b))

# বা shortcut:
print(a @ b)

# difference:
# * → element-wise multiplication
# @ → matrix multiplication