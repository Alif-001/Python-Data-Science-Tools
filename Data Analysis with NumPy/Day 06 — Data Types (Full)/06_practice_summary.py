import numpy as np

# mixed practice

arr = np.array([1, 2, 3, 4.5, True])

print("Array:", arr)
print("dtype:", arr.dtype)

# convert to int
arr_int = arr.astype(np.int32)
print("\nConverted to int:", arr_int)

# convert to float32 (memory saving vs float64)
arr_float = arr.astype(np.float32)
print("\nConverted to float32:", arr_float)
print("dtype:", arr_float.dtype)