import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# slicing syntax: arr[start:end]
print(arr[1:4])  # index 1 to 3

# start to end
print(arr[:3])   # first 3 elements

# step slicing
print(arr[::2])  # every 2nd element