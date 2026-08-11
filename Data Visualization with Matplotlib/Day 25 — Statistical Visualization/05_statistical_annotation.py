import numpy as np
import matplotlib.pyplot as plt

"""
STATISTICAL ANNOTATION
----------------------
We label important statistical values on plot.
"""

data = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18])

mean = np.mean(data)

x = np.arange(len(data))

plt.plot(x, data, marker="o")

# Draw mean line
plt.axhline(mean, color="red", linestyle="--")

# Add annotation (text + arrow)
plt.annotate(
    f"Mean = {mean}",
    xy=(0, mean),
    xytext=(2, mean + 3),
    arrowprops=dict(facecolor="black", arrowstyle="->")
)

plt.title("Statistical Annotation Example")
plt.xlabel("Index")
plt.ylabel("Value")

plt.grid(True)

plt.show()