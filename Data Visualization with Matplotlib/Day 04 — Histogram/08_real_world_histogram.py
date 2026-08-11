import matplotlib.pyplot as plt
import csv

"""
REAL WORLD HISTOGRAM
--------------------
We analyze exam score distribution.
"""

scores = []

# Read CSV file
with open("exam_scores.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        scores.append(int(row["score"]))

# Create histogram
plt.hist(
    scores,
    bins=[40, 50, 60, 70, 80, 90, 100],
    color="purple",
    edgecolor="black"
)

plt.title("Exam Score Distribution")
plt.xlabel("Score Range")
plt.ylabel("Number of Students")

plt.show()