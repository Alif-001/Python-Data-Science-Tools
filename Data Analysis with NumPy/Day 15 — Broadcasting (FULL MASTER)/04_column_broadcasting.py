import numpy as np

# -----------------------------------
# Column broadcasting (vertical expansion)
# -----------------------------------

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# column vector (shape: (2,1))
b = np.array([
    [10],
    [20]
])

print(a + b)

# Output:
# [[11 12 13]
#  [24 25 26]]

# explanation:
# b column-wise expand হয়ে গেছে