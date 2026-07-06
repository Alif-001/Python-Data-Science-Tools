import numpy as np

# ধরো exam marks
marks = np.array([45, 55, 60, 35, 80, 90, 20])

# -----------------------------------
# Real-world masking example
# -----------------------------------

# pass marks (>= 50)
passed = marks[marks >= 50]
print("Passed:", passed)

# fail marks (< 50)
failed = marks[marks < 50]
print("Failed:", failed)

# bonus: fail students get +10 marks
marks[marks < 50] += 10

print("Updated marks:", marks)