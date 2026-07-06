import numpy as np

arr = np.array([1, 2, 3, 4])

# -----------------------------------
# Broadcasting (important concept)
# -----------------------------------

# ছোট array + scalar
print(arr + 10)
# [11 12 13 14]

# different shape but works automatically
a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([10, 20, 30])

print(a + b)
# b automatically expands (broadcasts)