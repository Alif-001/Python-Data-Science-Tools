import numpy as np

# -----------------------------------
# STEP 1: Create data
# -----------------------------------

marks = np.array([45, 60, 75, 30, 90, 50, 80])

print("Original Data:", marks)

# -----------------------------------
# STEP 2: Filter data (boolean indexing)
# -----------------------------------

passed = marks[marks >= 50]
failed = marks[marks < 50]

print("Passed:", passed)
print("Failed:", failed)

# -----------------------------------
# STEP 3: Transform data (reshape concept example)
# -----------------------------------

# reshape into 2D (for analysis style)
reshaped = marks.reshape(7, 1)

print("Reshaped:")
print(reshaped)

# -----------------------------------
# STEP 4: Analyze data (statistics)
# -----------------------------------

print("Mean:", np.mean(marks))
print("Max:", np.max(marks))
print("Min:", np.min(marks))
print("Std:", np.std(marks))

# -----------------------------------
# STEP 5: Summarize insight
# -----------------------------------

print("\nSUMMARY:")
print("Total Students:", len(marks))
print("Passed Students:", len(passed))
print("Failed Students:", len(failed))
print("Average Score:", np.mean(marks))