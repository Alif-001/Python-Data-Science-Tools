import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# -----------------------------------
# Condition-based replace
# -----------------------------------

# যেসব value > 30 → 0 করে দাও
arr[arr > 30] = 0

print(arr)
# Output: [10 20 30  0  0]

# আবার নতুন condition
arr = np.array([1, 2, 3, 4, 5])

# যেসব value odd → 99
arr[arr % 2 == 1] = 99

print(arr)
# Output: [99  2 99  4 99]