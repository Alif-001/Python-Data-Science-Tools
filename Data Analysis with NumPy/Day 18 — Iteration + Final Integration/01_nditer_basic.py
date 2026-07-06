import numpy as np

# 2D array
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# -----------------------------------
# nditer → element-by-element iteration
# -----------------------------------

# পুরা array iterate করা (clean way)
for x in np.nditer(arr):
    print(x)

# Output:
# 1 2 3 4 5 6