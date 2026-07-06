import numpy as np

# =========================
# View vs Copy comparison
# =========================

arr = np.array([1, 2, 3, 4, 5])

view_arr = arr[1:4]      # view
copy_arr = arr[1:4].copy()  # deep copy

# change view
view_arr[0] = 111

# change copy
copy_arr[0] = 222

print("Original:", arr)
print("View:", view_arr)
print("Copy:", copy_arr)

# =========================
# Output concept:
# - view → original affected
# - copy → independent
# =========================