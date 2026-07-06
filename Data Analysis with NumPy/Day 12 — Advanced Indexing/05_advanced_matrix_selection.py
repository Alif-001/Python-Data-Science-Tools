import numpy as np

arr = np.array([
    [11, 12, 13],
    [21, 22, 23],
    [31, 32, 33]
])

# -----------------------------------
# Advanced pattern selection
# -----------------------------------

# diagonal-like selection using indexing
rows = [0, 1, 2]
cols = [0, 1, 2]

print(arr[rows, cols])
# Output: [11 22 33]

# reverse diagonal
cols_rev = [2, 1, 0]

print(arr[rows, cols_rev])
# Output: [13 22 31]