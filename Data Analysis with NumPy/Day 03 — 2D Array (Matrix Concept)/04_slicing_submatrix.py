import numpy as np

arr = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

# submatrix (part of matrix)
# syntax: arr[row_start:row_end, col_start:col_end]

sub = arr[0:2, 1:3]

print("Submatrix:")
print(sub)

# first 2 rows, all columns
print(arr[0:2, :])

# all rows, first 2 columns
print(arr[:, 0:2])