import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# row = horizontal line
# column = vertical line

# first row
print("Row 0:", arr[0])

# second row
print("Row 1:", arr[1])

# first column
print("Column 0:", arr[:, 0])

# second column
print("Column 1:", arr[:, 1])