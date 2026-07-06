import numpy as np

# =========================
# np.zeros → সব 0 দিয়ে array বানায়
# =========================

arr_zero = np.zeros((3, 4))  # 3 rows, 4 columns

print("Zeros Array:\n", arr_zero)
print("dtype:", arr_zero.dtype)

# =========================
# np.ones → সব 1 দিয়ে array
# =========================

arr_one = np.ones((2, 3))

print("\nOnes Array:\n", arr_one)
print("dtype:", arr_one.dtype)