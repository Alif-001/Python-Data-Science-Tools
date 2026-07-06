import numpy as np

arr = np.array([5, 10, 15, 20, 25, 30])

# -----------------------------------
# Fancy indexing vs boolean indexing
# -----------------------------------

# fancy indexing
print(arr[[0, 3, 5]])
# [5 20 30]

# boolean indexing (comparison based)
print(arr[arr > 15])
# [20 25 30]

# -----------------------------------
# Combine idea (filter + fancy style)
# -----------------------------------

filtered = arr[arr > 10]
print(filtered)