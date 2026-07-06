import numpy as np

# =========================
# reshape → shape change without changing data
# =========================

arr = np.arange(1, 13)  # 1 to 12

print("Original:", arr)
print("Shape:", arr.shape)

# 1D → 2D
mat = arr.reshape(3, 4)

print("\nReshaped (3x4):\n", mat)

# 2D → 3D
tensor = arr.reshape(2, 2, 3)

print("\nReshaped (2x2x3):\n", tensor)

# ⚠️ rule:
# total elements must match
# 12 elements → only valid shapes like (3,4), (2,6), etc.