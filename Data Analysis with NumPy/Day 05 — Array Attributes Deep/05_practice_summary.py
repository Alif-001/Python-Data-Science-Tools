import numpy as np

# একটি mixed array তৈরি করো
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# সব attributes একসাথে check করো
print("Array:\n", arr)

print("\nndim:", arr.ndim)     # dimension
print("shape:", arr.shape)    # structure
print("size:", arr.size)      # total elements
print("dtype:", arr.dtype)    # data type