import numpy as np

# 2D array (matrix)
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# -----------------------------------
# Row-wise fancy indexing
# -----------------------------------

# row 0 এবং row 2 একসাথে
print(arr[[0, 2]])

# Output:
# [[1 2 3]
#  [7 8 9]]

# -----------------------------------
# Column selection using fancy indexing
# -----------------------------------

# column-wise selection (advanced trick)
print(arr[:, [0, 2]])

# Output:
# [[1 3]
#  [4 6]
#  [7 9]]