import numpy as np

# 2D array
arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# -----------------------------------
# 2D Boolean filtering
# -----------------------------------

# flatten করে filter করে নেয়
print(arr[arr > 50])
# Output: [60 70 80 90]

# condition based modify
arr[arr < 50] = -1

print(arr)
# Output:
# [[-1 -1 30]
#  [-1 50 60]
#  [70 80 90]]