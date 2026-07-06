import numpy as np

# marks of students
marks = np.array([60, 70, 80, 90])

# give bonus marks
marks = marks + 5

print("Updated marks:", marks)

# increase only some students (slicing idea)
marks[1:3] = marks[1:3] + 10

print("Final marks:", marks)