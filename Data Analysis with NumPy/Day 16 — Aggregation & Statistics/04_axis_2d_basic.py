import numpy as np

# 2D array (matrix)
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# -----------------------------------
# axis=0 → column-wise operation
# axis=1 → row-wise operation
# -----------------------------------

# column-wise sum
print(np.sum(arr, axis=0))
# [5 7 9]

# row-wise sum
print(np.sum(arr, axis=1))
# [6 15]

# mean row-wise
print(np.mean(arr, axis=1))
# [2.0 5.0]