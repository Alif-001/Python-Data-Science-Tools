import matplotlib.pyplot as plt

"""
DONUT CHART
-----------
Pie chart with a hole in the center.
"""

activities = ["Study", "Sleep", "Play", "Others"]
hours = [6, 8, 4, 6]

plt.pie(
    hours,
    labels=activities,
    autopct="%1.1f%%",
    wedgeprops={"width": 0.4}  # creates hole (donut effect)
)

plt.title("Donut Chart Example")

plt.show()