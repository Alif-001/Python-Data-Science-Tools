import matplotlib.pyplot as plt

"""
SHADOW + START ANGLE + COLORS
-----------------------------
shadow = 3D-like effect
startangle = rotate chart
colors = custom colors
"""

activities = ["Study", "Sleep", "Play", "Others"]
hours = [6, 8, 4, 6]

colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99"]

plt.pie(
    hours,
    labels=activities,
    autopct="%1.1f%%",
    colors=colors,
    shadow=True,        # 3D shadow effect
    startangle=90       # rotate starting point
)

plt.title("Styled Pie Chart")

plt.show()