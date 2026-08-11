import matplotlib.pyplot as plt

"""
CUSTOM THEME
------------
We manually style everything.
"""

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.figure(facecolor="lightgray")  # background color

plt.plot(x, y, color="blue", linewidth=3)

plt.title("Custom Theme Example", fontsize=16, color="darkred")
plt.xlabel("X Axis", fontsize=12)
plt.ylabel("Y Axis", fontsize=12)

plt.show()