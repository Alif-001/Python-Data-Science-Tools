import numpy as np
import time

# বড় array তৈরি
arr = np.arange(1, 1000000)

# -----------------------------------
# Python loop timing
# -----------------------------------

start = time.time()

result = []
for x in arr:
    result.append(x * 2)

end = time.time()

print("Loop time:", end - start)

# -----------------------------------
# NumPy vectorization timing
# -----------------------------------

start = time.time()

result_np = arr * 2

end = time.time()

print("NumPy time:", end - start)

# NumPy অনেক দ্রুত কারণ:
# → compiled C backend ব্যবহার করে
# → loop Python level এ নেই