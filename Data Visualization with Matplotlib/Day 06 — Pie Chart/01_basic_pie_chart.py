import matplotlib.pyplot as plt

"""
DAY 6 - PIE CHART
-----------------
Pie chart shows parts of a whole (percentage distribution).
Example: How a student spends time in a day.
"""

# Data
activities = ["Study", "Sleep", "Play", "Others"]
hours = [6, 8, 4, 6]

# Create pie chart
plt.pie(hours)

plt.title("Basic Pie Chart")

plt.show()