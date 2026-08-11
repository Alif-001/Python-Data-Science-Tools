import matplotlib.pyplot as plt

"""
BINS IN HISTOGRAM
-----------------
Bins = range intervals (grouping)

Example:
0-10, 10-20, 20-30 ...
"""

marks = [12, 15, 18, 22, 25, 28, 30, 35, 40, 45,
         50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

# bins = number of intervals
plt.hist(marks, bins=5, color="blue")

plt.title("Histogram with Bins")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.show()