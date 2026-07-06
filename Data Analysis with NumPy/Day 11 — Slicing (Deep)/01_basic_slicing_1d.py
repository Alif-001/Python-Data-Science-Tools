import numpy as np

# 1D array তৈরি
arr = np.array([10, 20, 30, 40, 50, 60])

# ----------------------------
# Basic slicing syntax:
# arr[start : end : step]
# ----------------------------

# index 1 থেকে 4 (4 excluded)
print(arr[1:4])   # [20 30 40]

# শুরু থেকে 3 পর্যন্ত
print(arr[:3])    # [10 20 30]

# 2 থেকে শেষ পর্যন্ত
print(arr[2:])    # [30 40 50 60]

# step ব্যবহার করে
print(arr[::2])   # every 2nd element