import matplotlib.pyplot as plt

"""
ARROW ANNOTATION
----------------
Used to point important changes or events.
"""

x = [1, 2, 3, 4, 5]
y = [3, 8, 6, 12, 10]

plt.plot(x, y, marker="o")

# Arrow pointing to a point
plt.annotate(
    "Increase Point",
    xy=(2, 8),
    xytext=(3, 12),
    arrowprops=dict(
        arrowstyle="->",
        color="red",
        lw=2
    )
)

plt.title("Arrow Annotation Example")

plt.show()