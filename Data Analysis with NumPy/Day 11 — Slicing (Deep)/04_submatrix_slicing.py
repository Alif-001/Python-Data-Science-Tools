import numpy as np

arr = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

# ----------------------------
# Submatrix extraction
# ----------------------------

# rows 0-1, cols 1-3
sub = arr[0:2, 1:3]

print(sub)
# [[20 30]
#  [60 70]]

# full middle block
print(arr[:, 1:3])