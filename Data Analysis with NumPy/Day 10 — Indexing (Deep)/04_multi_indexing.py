import numpy as np

# =========================
# Multi Indexing (Fancy Selection)
# =========================

arr = np.array([100, 200, 300, 400, 500])

# multiple indices একসাথে access
selected = arr[[0, 2, 4]]

print("Original:", arr)
print("Selected elements:", selected)

# =========================
# 2D multi indexing
# =========================

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# select multiple rows
rows = matrix[[0, 2]]

print("\nSelected rows:\n", rows)

# select specific elements (row,col pairs)
values = matrix[[0, 1, 2], [0, 1, 2]]

print("\nDiagonal elements:", values)

# =========================
# Concept:
# fancy indexing → multiple selection
# =========================