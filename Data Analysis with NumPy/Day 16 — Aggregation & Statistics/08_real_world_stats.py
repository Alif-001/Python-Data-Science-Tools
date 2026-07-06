import numpy as np

# -----------------------------------
# Real-world example: marks dataset
# -----------------------------------

marks = np.array([45, 55, 60, 35, 80, 90])

# average score
print("Mean:", np.mean(marks))

# highest score
print("Max:", np.max(marks))

# lowest score
print("Min:", np.min(marks))

# consistency check
print("Std deviation:", np.std(marks))

# -----------------------------------
# Business idea:
# - mean → overall performance
# - std → consistency
# - max/min → best/worst performer