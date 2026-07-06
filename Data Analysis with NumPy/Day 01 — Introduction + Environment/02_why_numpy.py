# Python list vs NumPy array difference

# Python list
arr = [1, 2, 3]

# list * 5 করলে list repeat হয়
print(arr * 5)
# Output: [1,2,3,1,2,3,1,2,3,1,2,3,1,2,3]


# NumPy array
import numpy as np

arr_np = np.array([1, 2, 3])

# NumPy array * 5 করলে element-wise multiply হয়
print(arr_np * 5)
# Output: [5 10 15]