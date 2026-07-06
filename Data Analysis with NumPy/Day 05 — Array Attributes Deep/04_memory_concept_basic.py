import numpy as np

# =========================
# NumPy vs Python List (Memory concept)
# =========================

# Python list (mixed type possible)
py_list = [1, 2, 3, 4]
print("Python List:", py_list)
print("List type:", type(py_list))

# NumPy array (fixed type → efficient memory)
np_arr = np.array([1, 2, 3, 4])
print("\nNumPy Array:", np_arr)
print("dtype:", np_arr.dtype)

# =========================
# Why NumPy faster?
# =========================
# - Same datatype store করে
# - Continuous memory block ব্যবহার করে
# - Vectorized operation possible