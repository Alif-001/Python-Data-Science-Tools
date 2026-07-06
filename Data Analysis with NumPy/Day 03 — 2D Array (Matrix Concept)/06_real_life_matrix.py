import numpy as np

# student marks (rows = students, columns = subjects)
marks = np.array([
    [80, 70, 90],
    [60, 75, 85],
    [90, 88, 92]
])

print("Marks:")
print(marks)

# average per student (row-wise)
print("Student averages:")
print(marks.mean(axis=1))

# average per subject (column-wise)
print("Subject averages:")
print(marks.mean(axis=0))