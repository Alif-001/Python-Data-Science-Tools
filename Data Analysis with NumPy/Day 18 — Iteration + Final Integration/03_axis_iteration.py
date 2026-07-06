import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

# -----------------------------------
# Row-wise iteration
# -----------------------------------

print("Row-wise:")
for row in arr:
    print(row)

# -----------------------------------
# Column-wise iteration
# -----------------------------------

print("Column-wise:")
for col in arr.T:
    print(col)

# .T → transpose (row ↔ column swap)