import numpy as np

arr = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ],
    [
        [9, 10],
        [11, 12]
    ]
])

print(arr)

# shape breakdown
print("Shape:", arr.shape)

# explanation:
# (3, 2, 2)
# 3 = number of blocks
# 2 = rows per block
# 2 = columns per row