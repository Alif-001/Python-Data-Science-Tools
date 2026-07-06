import numpy as np

# 2D array (matrix)
a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [10, 20],
    [30, 40]
])

# -----------------------------------
# 2D element-wise operations
# -----------------------------------

print(a + b)
# [[11 22]
#  [33 44]]

print(a * b)
# [[10 40]
#  [90 160]]