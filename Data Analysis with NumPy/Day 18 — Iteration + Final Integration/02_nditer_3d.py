import numpy as np

# 3D array
arr = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

# -----------------------------------
# 3D iteration using nditer
# -----------------------------------

for x in np.nditer(arr):
    print(x)

# সব element flatten হয়ে iterate হবে