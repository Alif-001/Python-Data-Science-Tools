import matplotlib.pyplot as plt

"""
FONT CUSTOMIZATION
------------------
We can control:
- font size
- font family
"""

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.plot(x, y)

plt.title("Font Example", fontsize=18, fontweight="bold")
plt.xlabel("X Axis", fontsize=14)
plt.ylabel("Y Axis", fontsize=14)

plt.show()