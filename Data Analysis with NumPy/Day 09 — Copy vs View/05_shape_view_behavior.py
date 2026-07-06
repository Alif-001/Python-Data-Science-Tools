import numpy as np

# =========================
# reshape → usually view (not copy)
# =========================

arr = np.arange(1, 7)

reshaped = arr.reshape(2, 3)

print("Original:", arr)
print("Reshaped:\n", reshaped)

# modify reshaped
reshaped[0][0] = 999

print("\nAfter modification:")
print("Original:", arr)
print("Reshaped:\n", reshaped)

# =========================
# reshape often shares memory → view behavior
# =========================