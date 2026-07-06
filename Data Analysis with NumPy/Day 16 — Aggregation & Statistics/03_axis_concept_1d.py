import numpy as np

# 1D array
arr = np.array([1, 2, 3, 4, 5])

# -----------------------------------
# 1D array → axis concept simple
# -----------------------------------

# axis নেই (বা axis=0 same)
print(np.sum(arr))
# 15

print(np.mean(arr))
# 3.0