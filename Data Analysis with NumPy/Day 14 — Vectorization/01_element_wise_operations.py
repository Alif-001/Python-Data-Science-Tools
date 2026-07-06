import numpy as np

# 1D arrays
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

# -----------------------------------
# Element-wise operations (Vectorization concept)
# -----------------------------------

# যোগ (addition)
print(a + b)   # [11 22 33 44]

# বিয়োগ (subtraction)
print(a - b)   # [-9 -18 -27 -36]

# গুণ (multiplication)
print(a * b)   # [10 40 90 160]

# ভাগ (division)
print(b / a)   # [10. 10. 10. 10.]