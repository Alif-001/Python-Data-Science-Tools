import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# -----------------------------------
# Row + Column indexing together
# -----------------------------------

# একই সাথে specific elements select করা
# (row index list + column index list)

rows = [0, 1, 2]
cols = [2, 1, 0]

print(arr[rows, cols])

# Output:
# [30 50 70]
# Explanation:
# (0,2) → 30
# (1,1) → 50
# (2,0) → 70