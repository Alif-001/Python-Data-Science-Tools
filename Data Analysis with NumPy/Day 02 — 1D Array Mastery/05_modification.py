import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# modify single element
arr[0] = 100

print("After change:", arr)

# modify multiple elements
arr[1:3] = 999

print("After slicing change:", arr)