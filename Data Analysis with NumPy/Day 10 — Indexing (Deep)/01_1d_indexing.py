import numpy as np

# =========================
# 1D Array Indexing
# =========================

arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)

# index starts from 0
print("First element:", arr[0])
print("Third element:", arr[2])

# negative indexing (from end)
print("Last element:", arr[-1])
print("Second last element:", arr[-2])

# =========================
# Concept:
# arr[index] → single element access
# =========================