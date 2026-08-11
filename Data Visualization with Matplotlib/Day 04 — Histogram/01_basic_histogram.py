import matplotlib.pyplot as plt

"""
DAY 4 - HISTOGRAM
-----------------
Histogram shows distribution of data.

Example:
- How many students got marks in 0–10, 10–20, etc.
"""

# Sample data (marks of students)
marks = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90,
         95, 40, 42, 47, 53, 58, 62, 68, 72, 78]

# Create histogram
plt.hist(marks)

plt.title("Basic Histogram")
plt.xlabel("Marks Range")
plt.ylabel("Frequency")

plt.show()