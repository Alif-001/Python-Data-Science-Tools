import numpy as np

# 1D array
arr = np.array([10, 20, 30, 40, 50])

# -----------------------------------
# Basic Aggregation Functions
# -----------------------------------

# sum → সব elements যোগ
print(np.sum(arr))
# 150

# mean → average
print(np.mean(arr))
# 30.0

# min → minimum value
print(np.min(arr))
# 10

# max → maximum value
print(np.max(arr))
# 50