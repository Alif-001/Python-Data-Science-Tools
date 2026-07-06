import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# access single element
print(arr[0][0])  # row 0, col 0
print(arr[1][2])  # row 1, col 2

# alternative clean way
print(arr[2, 1])  # row 2, col 1