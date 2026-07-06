import numpy as np

# 1D array
arr = np.array([10, 15, 20, 25, 30, 35, 40])

# -----------------------------------
# Boolean Indexing (Condition Filtering)
# -----------------------------------

# যেসব value > 20
print(arr[arr > 20])
# Output: [25 30 35 40]

# যেসব value <= 20
print(arr[arr <= 20])
# Output: [10 15 20]

# যেসব value == 30
print(arr[arr == 30])
# Output: [30]