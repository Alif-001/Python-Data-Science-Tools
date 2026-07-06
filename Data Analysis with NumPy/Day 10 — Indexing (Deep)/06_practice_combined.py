import numpy as np

# =========================
# Full Practice Mix
# =========================

arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

print("Original:\n", arr)

# row access
print("\nRow 1:", arr[1])

# column access
print("Column 2:", arr[:, 2])

# single element
print("Element (2,2):", arr[2, 2])

# modify element
arr[0, 0] = 999

# modify row
arr[2] = [111, 222, 333]

print("\nFinal Matrix:\n", arr)