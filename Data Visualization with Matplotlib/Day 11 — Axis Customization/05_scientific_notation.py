import matplotlib.pyplot as plt

"""
SCIENTIFIC NOTATION
-------------------
Used for very large/small numbers
"""

x = [1, 2, 3, 4, 5]
y = [1000, 2000, 3000, 4000, 5000]

plt.plot(x, y)

# Show scientific notation automatically
plt.ticklabel_format(style="sci", axis="y", scilimits=(0, 0))

plt.title("Scientific Notation Example")

plt.show()