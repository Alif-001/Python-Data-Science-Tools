import numpy as np

# =========================
# Upcasting concept (automatic type conversion)
# =========================

# int + float → float (safe type)
arr1 = np.array([1, 2, 3.5])
print("Mixed int+float:", arr1)
print("dtype:", arr1.dtype)  # float64

# int + float + string → string
arr2 = np.array([1, 2, "hello"])
print("\nMixed int+string:", arr2)
print("dtype:", arr2.dtype)  # <U... (string)

# bool + int → int (True=1, False=0)
arr3 = np.array([True, False, 1])
print("\nBool + int:", arr3)
print("dtype:", arr3.dtype)