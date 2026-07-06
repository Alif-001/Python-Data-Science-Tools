import numpy as np

# =========================
# _like → existing array এর shape copy করে
# =========================

base = np.array([[1, 2, 3],
                 [4, 5, 6]])

# zeros_like → same shape, all 0
z = np.zeros_like(base)

print("Base Array:\n", base)
print("\nZeros Like:\n", z)

# ones_like → same shape, all 1
o = np.ones_like(base)

print("\nOnes Like:\n", o)

# full_like → same shape, custom value
f = np.full_like(base, 9)

print("\nFull Like:\n", f)