import numpy as np

# =========================
# Row & Column Access
# =========================

arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

# full row access
print("Row 0:", arr[0])
print("Row 2:", arr[2])

# full column access
print("Column 0:", arr[:, 0])
print("Column 2:", arr[:, 2])

# =========================
# Concept:
# arr[:, col] → column
# arr[row]    → row
# =========================