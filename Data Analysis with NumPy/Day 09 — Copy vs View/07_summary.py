import numpy as np

# =========================
# Summary demo
# =========================

arr = np.array([1, 2, 3, 4, 5])

view = arr[1:4]
copy = arr.copy()

view[0] = 999
copy[0] = 888

print("Original:", arr)
print("View:", view)
print("Copy:", copy)

# =========================
# Key takeaway:
# =========================
# view  → shared memory (fast, risky)
# copy  → separate memory (safe)