import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# -----------------------------------
# Cumulative Sum (cumsum)
# -----------------------------------

print(np.cumsum(arr))
# [1 3 6 10 15]

# -----------------------------------
# Cumulative Product (cumprod)
# -----------------------------------

print(np.cumprod(arr))
# [1 2 6 24 120]

# explanation:
# cumsum → running total
# cumprod → running multiplication