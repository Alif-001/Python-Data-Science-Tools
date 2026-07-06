import numpy as np

# =========================
# Manual dtype selection
# =========================

# int16 ব্যবহার করলে memory কম লাগে
arr = np.array([100, 200, 300], dtype=np.int16)

print("Array:", arr)
print("dtype:", arr.dtype)

# float32 vs float64 comparison
arr_f = np.array([1, 2, 3], dtype=np.float32)
print("\nFloat32 array:", arr_f)
print("dtype:", arr_f.dtype)

# Default float is float64 (bigger memory)
arr_f2 = np.array([1, 2, 3], dtype=np.float64)
print("\nFloat64 array:", arr_f2)
print("dtype:", arr_f2.dtype)