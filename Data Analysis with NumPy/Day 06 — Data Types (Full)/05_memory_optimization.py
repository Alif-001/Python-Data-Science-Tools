import numpy as np
import sys

# =========================
# Memory Optimization Concept
# =========================

# int64 → বেশি memory নেয়
arr1 = np.array([1, 2, 3, 4, 5], dtype=np.int64)

# int8 → কম memory নেয়
arr2 = np.array([1, 2, 3, 4, 5], dtype=np.int8)

print("int64 array:", arr1)
print("int64 dtype:", arr1.dtype)

print("\nint8 array:", arr2)
print("int8 dtype:", arr2.dtype)

# =========================
# Memory size comparison
# =========================
print("\nMemory (int64):", arr1.nbytes, "bytes")
print("Memory (int8):", arr2.nbytes, "bytes")

# =========================
# Conclusion:
# int8 = small memory (good for ML large datasets)
# int64 = large memory (default, safe)
# =========================