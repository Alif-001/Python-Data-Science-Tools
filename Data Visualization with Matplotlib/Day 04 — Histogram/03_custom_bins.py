import matplotlib.pyplot as plt

"""
CUSTOM BINS
-----------
We define our own ranges.
"""

marks = [10, 15, 20, 25, 30, 35, 40, 45, 50,
         55, 60, 65, 70, 75, 80, 85, 90, 95]

# Custom bin ranges
bins = [0, 20, 40, 60, 80, 100]

plt.hist(marks, bins=bins, color="green", edgecolor="black")

plt.title("Custom Bins Histogram")
plt.xlabel("Marks Range")
plt.ylabel("Frequency")

plt.show()