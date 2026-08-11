import matplotlib.pyplot as plt
import csv

"""
REAL DATASET VIOLIN PLOT
------------------------
We analyze score distribution by subject.
"""

math = []
science = []
english = []

# Read CSV file
with open("student_scores.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        math.append(int(row["math"]))
        science.append(int(row["science"]))
        english.append(int(row["english"]))

# Combine data
data = [math, science, english]

plt.violinplot(data)

plt.xticks([1, 2, 3], ["Math", "Science", "English"])

plt.title("Student Score Distribution (Violin Plot)")

plt.show()