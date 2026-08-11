import matplotlib.pyplot as plt

"""
TICK FORMATTING
---------------
Ticks = numbers shown on axes
We can customize them for readability
"""

x = [1, 2, 3, 4, 5]
y = [5, 10, 15, 20, 25]

plt.plot(x, y)

# Custom ticks
plt.xticks([1, 2, 3, 4, 5], ["A", "B", "C", "D", "E"])

plt.title("Custom Tick Labels")

plt.show()