import matplotlib.pyplot as plt

"""
LABELS + AUTOPCT
-----------------
labels = names of sections
autopct = shows percentage value
"""

activities = ["Study", "Sleep", "Play", "Others"]
hours = [6, 8, 4, 6]

plt.pie(
    hours,
    labels=activities,     # category names
    autopct="%1.1f%%"      # show percentage
)

plt.title("Pie Chart with Labels & Percentages")

plt.show()