import numpy as np

# -----------------------------------
# Row broadcasting
# -----------------------------------

a = np.array([
    [1],
    [2],
    [3]
])

b = np.array([10, 20, 30])

print(a + b)

# Output:
# [[11 21 31]
#  [12 22 32]
#  [13 23 33]]

# explanation:
# a column-wise expand + b row-wise expand