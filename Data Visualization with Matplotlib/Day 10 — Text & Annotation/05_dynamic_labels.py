import matplotlib.pyplot as plt

"""
DYNAMIC LABELING
----------------
We label each data point dynamically.
"""

x = [1, 2, 3, 4]
y = [10, 15, 20, 25]

plt.plot(x, y, marker="o")

# Loop through all points
for i in range(len(x)):
    plt.text(x[i], y[i] + 0.5, str(y[i]), ha="center")

plt.title("Dynamic Point Labels")

plt.show()