import numpy as np

arr = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ],
    [
        [13, 14, 15],
        [16, 17, 18]
    ]
])

# get first two blocks
print(arr[0:2])

# get all rows of first block
print(arr[0, :, :])

# get specific column from all blocks
print(arr[:, :, 1])