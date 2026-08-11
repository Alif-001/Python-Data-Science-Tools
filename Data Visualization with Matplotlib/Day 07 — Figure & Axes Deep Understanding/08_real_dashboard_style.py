import matplotlib.pyplot as plt
import csv

"""
REAL DASHBOARD STYLE PLOTS
--------------------------
We visualize multiple subjects using subplots.
"""

students = []
math = []
science = []
english = []

# Read CSV file
with open("student_performance.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        students.append(row["student"])
        math.append(int(row["math"]))
        science.append(int(row["science"]))
        english.append(int(row["english"]))

# Create figure with subplots
fig, ax = plt.subplots(1, 3, figsize=(12, 4))

# Math
ax[0].bar(students, math, color="blue")
ax[0].set_title("Math Scores")

# Science
ax[1].bar(students, science, color="green")
ax[1].set_title("Science Scores")

# English
ax[2].bar(students, english, color="orange")
ax[2].set_title("English Scores")

plt.tight_layout()

plt.show()