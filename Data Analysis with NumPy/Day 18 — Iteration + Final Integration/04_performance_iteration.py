import numpy as np
import time

arr = np.arange(1, 1000000)

# -----------------------------------
# Python loop (slow)
# -----------------------------------

start = time.time()

result = []
for x in arr:
    result.append(x * 2)

end = time.time()

print("Loop time:", end - start)

# -----------------------------------
# NumPy vectorization (fast)
# -----------------------------------

start = time.time()

result_np = arr * 2

end = time.time()

print("NumPy time:", end - start)

# conclusion:
# NumPy অনেক দ্রুত কারণ compiled C backend ব্যবহার করে