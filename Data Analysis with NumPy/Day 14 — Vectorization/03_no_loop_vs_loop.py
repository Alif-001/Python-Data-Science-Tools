import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# -----------------------------------
# Traditional Python loop (slow)
# -----------------------------------

result_loop = []

for x in arr:
    result_loop.append(x * 2)

print("Loop result:", result_loop)

# -----------------------------------
# NumPy Vectorization (fast)
# -----------------------------------

result_numpy = arr * 2

print("NumPy result:", result_numpy)