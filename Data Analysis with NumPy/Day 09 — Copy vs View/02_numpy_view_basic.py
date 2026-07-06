import numpy as np

# =========================
# NumPy view concept
# =========================

arr = np.array([1, 2, 3, 4, 5])

view_arr = arr[1:4]  # slicing → view তৈরি করে

print("Original:", arr)
print("View:", view_arr)

# view change করলে original change হবে
view_arr[0] = 999

print("\nAfter modifying view:")
print("Original:", arr)
print("View:", view_arr)

# =========================
# Important:
# slicing = view (shared memory)
# =========================