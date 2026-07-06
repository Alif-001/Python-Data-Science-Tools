import numpy as np

arr = np.array([10, 20, 30, 40])

# -----------------------------------
# Scalar + Array (Most common case)
# -----------------------------------

# scalar automatically সব element এ apply হয়
print(arr + 5)
# [15 25 35 45]

print(arr * 2)
# [20 40 60 80]

print(arr ** 2)
# [100 400 900 1600]