import numpy as np

# 1D array তৈরি
arr = np.array([10, 20, 30, 40, 50, 60])

# -----------------------------------
# Fancy Indexing (Important concept)
# → একসাথে multiple index ব্যবহার করা
# -----------------------------------

# index list দিয়ে specific elements নেওয়া
print(arr[[0, 2, 4]])
# Output: [10 30 50]

# order change করেও নিতে পারো
print(arr[[5, 1, 3]])
# Output: [60 20 40]

# duplicate index allowed
print(arr[[1, 1, 2]])
# Output: [20 20 30]