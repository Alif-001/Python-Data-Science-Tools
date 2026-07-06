import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

# -----------------------------------
# Axis visualization
# -----------------------------------

# axis=0 → vertical (column direction)
print(np.sum(arr, axis=0))

# axis=1 → horizontal (row direction)
print(np.sum(arr, axis=1))

# min per column
print(np.min(arr, axis=0))

# max per row
print(np.max(arr, axis=1))