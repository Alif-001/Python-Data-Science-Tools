import matplotlib.pyplot as plt

"""
DENSITY HISTOGRAM
-----------------
Instead of frequency, shows probability distribution.
"""

marks = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90]

plt.hist(
    marks,
    bins=5,
    density=True,   # converts frequency to probability
    color="purple",
    alpha=0.7
)

plt.title("Density Histogram (Probability)")
plt.xlabel("Marks")
plt.ylabel("Density")

plt.show()