import matplotlib.pyplot as plt

"""
EXPLODE FEATURE
---------------
explode = separates a slice from the pie
used to highlight important category
"""

activities = ["Study", "Sleep", "Play", "Others"]
hours = [6, 8, 4, 6]

# "explode" each slice (0 = normal, >0 = separated)
explode = [0.1, 0, 0, 0]

plt.pie(
    hours,
    labels=activities,
    autopct="%1.1f%%",
    explode=explode
)

plt.title("Pie Chart with Explode Effect")

plt.show()