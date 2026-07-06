import numpy as np

# 3D array = array of 2D arrays (stack of matrices)

arr = np.array([
    # 1st block (floor)
    [
        [1, 2, 3],
        [4, 5, 6]
    ],

    # 2nd block (floor)
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
])

print("3D Array:")
print(arr)

# shape = (depth, rows, columns)
print("Shape:", arr.shape)

# dimension
print("Dimensions:", arr.ndim)