import numpy as np

arr = np.array([10, 15, 20, 25, 30, 35, 40])

# -----------------------------------
# Multiple Conditions (AND, OR, NOT)
# -----------------------------------

# AND condition: (value > 15) AND (value < 35)
print(arr[(arr > 15) & (arr < 35)])
# Output: [20 25 30]

# OR condition: (value < 15) OR (value > 35)
print(arr[(arr < 15) | (arr > 35)])
# Output: [10 40]

# NOT condition: reverse condition
print(arr[~(arr > 25)])
# Output: [10 15 20 25]