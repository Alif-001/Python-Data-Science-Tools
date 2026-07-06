import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# -----------------------------------
# Statistics
# -----------------------------------

# variance (data spread measure)
print(np.var(arr))
# data কতটা spread

# standard deviation (std)
print(np.std(arr))
# sqrt of variance

# explanation:
# std ছোট হলে data consistent
# std বড় হলে data spread বেশি