import numpy as np

# =========================
# Practice Summary
# =========================

# 1D base array
base = np.array([1, 2, 3])

# create different arrays from same shape idea
a = np.zeros_like(base)
b = np.ones_like(base)
c = np.full_like(base, 5)

print("Base:", base)
print("Zeros:", a)
print("Ones:", b)
print("Full:", c)

# identity check
eye = np.eye(3)
print("\nIdentity Matrix:\n", eye)

# diagonal
diag = np.diag([10, 20, 30])
print("\nDiagonal Matrix:\n", diag)