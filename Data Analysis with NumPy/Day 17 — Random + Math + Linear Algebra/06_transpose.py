import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# -----------------------------------
# Transpose (rows ↔ columns swap)
# -----------------------------------

print(arr.T)

# Output:
# [[1 4]
#  [2 5]
#  [3 6]]

# shape change:
# (2,3) → (3,2)