import numpy as np

# =========================
# Full practice combo
# =========================

# step 1: create range data
arr = np.arange(1, 13)

# step 2: reshape
mat = arr.reshape(3, 4)

print("Matrix:\n", mat)

# step 3: flatten
f = mat.flatten()

# step 4: ravel
r = mat.ravel()

print("\nFlatten:", f)
print("Ravel:", r)

# step 5: modify ravel (affects original)
r[0] = 100

print("\nAfter ravel modification:")
print(mat)