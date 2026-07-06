import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Original:")
print(arr)

# update single value
arr[0, 1] = 999

# update full row
arr[1] = [100, 200, 300]

# update column
arr[:, 2] = [7, 7, 7]

print("After update:")
print(arr)