import numpy as np

# 2D array (matrix)
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# ----------------------------
# Row slicing
# ----------------------------

# first row
print(arr[0])      # [1 2 3]

# first two rows
print(arr[:2])

# ----------------------------
# Column slicing
# ----------------------------

# first column
print(arr[:, 0])   # [1 4 7]

# second column
print(arr[:, 1])   # [2 5 8]