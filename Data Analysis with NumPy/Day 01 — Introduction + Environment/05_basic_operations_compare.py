# Python list vs NumPy operations

# Python list
lst = [1, 2, 3]

# multiply manually using loop/list comprehension
lst_result = [x * 2 for x in lst]
print(lst_result)


# NumPy array
import numpy as np

arr = np.array([1, 2, 3])

# directly multiply (no loop needed)
print(arr * 2)