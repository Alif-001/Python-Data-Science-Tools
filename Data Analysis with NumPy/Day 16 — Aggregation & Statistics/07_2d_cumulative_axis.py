import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# -----------------------------------
# Cumulative with axis
# -----------------------------------

# column-wise cumulative sum
print(np.cumsum(arr, axis=0))

# row-wise cumulative sum
print(np.cumsum(arr, axis=1))