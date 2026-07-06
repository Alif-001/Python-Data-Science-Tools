import numpy as np

# =========================
# int type array
# =========================
arr_int = np.array([1, 2, 3])
print("Integer array:", arr_int)
print("dtype:", arr_int.dtype)   # int64 / int32 (system dependent)

# =========================
# float type array
# =========================
arr_float = np.array([1.5, 2.7, 3.0])
print("\nFloat array:", arr_float)
print("dtype:", arr_float.dtype)

# =========================
# bool type array
# =========================
arr_bool = np.array([True, False, True])
print("\nBoolean array:", arr_bool)
print("dtype:", arr_bool.dtype)

# =========================
# string type array
# =========================
arr_str = np.array(["a", "b", "c"])
print("\nString array:", arr_str)
print("dtype:", arr_str.dtype)