import numpy as np

# =========================
# flatten vs ravel difference
# =========================

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print("Original Array:\n", arr)

# =========================
# flatten → copy তৈরি করে (independent)
# =========================
flat = arr.flatten()

flat[0] = 999  # original array change হবে না

print("\nFlattened:", flat)
print("Original after flatten change:\n", arr)

# =========================
# ravel → view তৈরি করে (linked memory)
# =========================
rav = arr.ravel()

rav[0] = 888  # original array change হবে

print("\nRaveled:", rav)
print("Original after ravel change:\n", arr)