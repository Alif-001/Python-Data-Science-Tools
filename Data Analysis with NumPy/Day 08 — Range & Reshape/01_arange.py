import numpy as np

# =========================
# np.arange → Python range এর NumPy version
# =========================

# start, end (exclusive), step
arr = np.arange(1, 11, 1)

print("Arange Array:", arr)

# step 2
arr2 = np.arange(0, 20, 2)

print("\nStep 2 Array:", arr2)

# float step possible
arr3 = np.arange(0, 5, 0.5)

print("\nFloat Step Array:", arr3)