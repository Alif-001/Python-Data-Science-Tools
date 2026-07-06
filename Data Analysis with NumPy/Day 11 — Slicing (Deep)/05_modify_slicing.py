import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# ----------------------------
# Slicing modifies original array
# ----------------------------

arr[1:4] = 99

print(arr)
# [10 99 99 99 50]

# ----------------------------
# copy() vs view (important!)
# ----------------------------

a = np.array([1, 2, 3, 4])
b = a[1:3]        # view

b[0] = 999

print(a)  # original change হয়ে যাবে

# safe copy
c = a[1:3].copy()
c[0] = 500

print(a)  # original safe