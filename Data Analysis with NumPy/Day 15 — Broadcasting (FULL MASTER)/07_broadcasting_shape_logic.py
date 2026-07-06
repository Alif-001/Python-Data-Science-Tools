import numpy as np

# -----------------------------------
# Shape compatibility understanding
# -----------------------------------

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# valid shapes:
# (2,3) + (3,)  → OK
# (2,3) + (2,1) → OK

b1 = np.array([10, 20, 30])      # (3,)
b2 = np.array([[10], [20]])      # (2,1)

print(a + b1)
print(a + b2)