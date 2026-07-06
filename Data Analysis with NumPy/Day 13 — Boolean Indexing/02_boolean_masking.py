import numpy as np

arr = np.array([5, 10, 15, 20, 25, 30])

# -----------------------------------
# Mask তৈরি করা (True/False array)
# -----------------------------------

mask = arr > 15

print(mask)
# Output: [False False False True True True]

# mask ব্যবহার করে filtering
print(arr[mask])
# Output: [20 25 30]