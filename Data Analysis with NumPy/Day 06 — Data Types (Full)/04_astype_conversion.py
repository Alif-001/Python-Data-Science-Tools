import numpy as np

# =========================
# astype() → datatype convert
# =========================

arr = np.array([1, 2, 3, 4])

print("Original array:", arr)
print("Original dtype:", arr.dtype)

# int → float conversion
arr_float = arr.astype(np.float64)
print("\nConverted to float:", arr_float)
print("dtype:", arr_float.dtype)

# float → int conversion (decimal loss হবে)
arr2 = np.array([1.9, 2.7, 3.5])
arr_int = arr2.astype(np.int32)

print("\nFloat to int (lossy):", arr_int)
print("dtype:", arr_int.dtype)