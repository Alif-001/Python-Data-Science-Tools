import matplotlib.pyplot as plt

"""
HISTOGRAM STYLING
-----------------
We combine multiple styles.
"""

data = [12, 15, 18, 20, 22, 25, 28, 30, 35, 40,
        42, 45, 50, 55, 60, 65, 70, 75, 80, 85]

plt.hist(
    data,
    bins=6,
    color="teal",
    edgecolor="black",
    alpha=0.8
)

plt.grid(True)  # adds background grid

plt.title("Styled Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")

plt.show()