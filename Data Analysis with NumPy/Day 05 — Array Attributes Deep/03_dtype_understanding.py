import numpy as np

# =========================
# Integer array
# =========================
arr1 = np.array([1, 2, 3])
print("Array:", arr1)
print("dtype:", arr1.dtype)  # int type

# =========================
# Float array
# =========================
arr2 = np.array([1.5, 2.5, 3.7])
print("\nArray:", arr2)
print("dtype:", arr2.dtype)  # float type

# =========================
# Mixed data (NumPy auto conversion)
# =========================
arr3 = np.array([1, 2, 3.5])
print("\nArray:", arr3)
print("dtype:", arr3.dtype)  # upcast → float

# =========================
# String mixing → all becomes string
# =========================
arr4 = np.array([1, 2, "hello"])
print("\nArray:", arr4)
print("dtype:", arr4.dtype)  # string type