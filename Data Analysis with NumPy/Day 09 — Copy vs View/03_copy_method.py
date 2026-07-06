import numpy as np

# =========================
# .copy() → deep copy (independent memory)
# =========================

arr = np.array([10, 20, 30, 40])

copied = arr.copy()

print("Original:", arr)
print("Copied:", copied)

# copied change করলে original change হবে না
copied[0] = 999

print("\nAfter modification:")
print("Original:", arr)
print("Copied:", copied)

# =========================
# .copy() → safe for ML pipeline
# =========================