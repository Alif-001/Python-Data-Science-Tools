import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# ----------------------------
# Step slicing concept
# ----------------------------

# reverse array
print(arr[::-1])   # [9 8 7 6 5 4 3 2 1]

# every 3rd element
print(arr[::3])    # [1 4 7]

# middle range with step
print(arr[2:8:2])  # [3 5 7]