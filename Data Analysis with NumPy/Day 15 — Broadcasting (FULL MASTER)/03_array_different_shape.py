import numpy as np

# -----------------------------------
# Different shape broadcasting
# -----------------------------------

# 2D array
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# 1D array
b = np.array([10, 20, 30])

# b automatically row-wise expand হয়
print(a + b)

# Output:
# [[11 22 33]
#  [14 25 36]]