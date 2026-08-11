import matplotlib.pyplot as plt
import csv

"""
REAL DATASET SCATTER PLOT
-------------------------
We analyze relationship between:
Study Hours vs Marks
"""

study_hours = []
marks = []
attendance = []

# Read CSV file
with open("student_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        study_hours.append(int(row["study_hours"]))
        marks.append(int(row["marks"]))
        attendance.append(int(row["attendance"]))

# Scatter plot: Study Hours vs Marks
plt.scatter(
    study_hours,
    marks,
    s=attendance,   # bubble size based on attendance
    alpha=0.6,
    color="purple"
)

plt.title("Study Hours vs Marks (Bubble = Attendance)")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.show()