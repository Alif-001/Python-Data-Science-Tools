import numpy as np

arr = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
])

# access full block
print("First block:")
print(arr[0])

# access second block
print("Second block:")
print(arr[1])

# access single element
print(arr[0, 1, 2])  # block 0, row 1, col 2