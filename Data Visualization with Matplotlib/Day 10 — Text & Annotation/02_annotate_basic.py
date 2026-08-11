import matplotlib.pyplot as plt

"""
ANNOTATE()
----------
Used to point out a specific point with explanation.
"""

x = [1, 2, 3, 4, 5]
y = [5, 15, 10, 25, 20]

plt.plot(x, y, marker="o")

# Annotate a point
plt.annotate(
    "Peak Point",           # text
    xy=(4, 25),            # point to highlight
    xytext=(2, 30),        # text position
    arrowprops=dict(facecolor="black", arrowstyle="->")
)

plt.title("Annotation Example")

plt.show()